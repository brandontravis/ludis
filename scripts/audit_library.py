#!/usr/bin/env python3
"""
Ludis Library Scanner - Config-Driven Filesystem Auditing
Scans game library based on platform_structure configuration.
No hardcoded paths or platform-specific logic.
"""
import argparse
import csv
import fnmatch
import os
import sys
import time
import unicodedata
from pathlib import Path
from collections import defaultdict
from typing import Optional, Dict, List, Tuple

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "LB_Exports" / "all_platforms.csv"
OUTDIR = PROJECT_ROOT / "LB_Exports" / "audits"

# Global configuration (loaded from config.yaml)
CONFIG = {}
NAS_ROOT = None
WIN_ROOT = None
PLATFORM_LOOKUP = {}  # Maps relative paths to platform config
PLATFORM_PATH_MAP = {}  # Maps normalized path prefixes to LaunchBox platform names
PATH_OVERRIDES = {}  # Path overrides from config (disk path → LB path)


def build_platform_path_mapping():
    """
    Build a mapping from filesystem paths to LaunchBox platform names.
    Reads all Platform XMLs and extracts ApplicationPath elements to determine
    which filesystem paths belong to which LaunchBox platforms.
    """
    global PLATFORM_PATH_MAP
    
    import xml.etree.ElementTree as ET
    import re
    
    # Get LaunchBox data directory from config
    lb_data = CONFIG.get('paths', {}).get('launchbox_data', 'Data/')
    if not Path(lb_data).is_absolute():
        lb_data_path = PROJECT_ROOT / lb_data
    else:
        lb_data_path = Path(lb_data)
    
    platforms_dir = lb_data_path / "Platforms"
    if not platforms_dir.exists():
        print(f"WARNING: LaunchBox Platforms directory not found: {platforms_dir}")
        return
    
    platform_paths = defaultdict(set)  # platform_name → set of normalized path prefixes
    
    # Read each Platform XML
    for xml_file in platforms_dir.glob("*.xml"):
        platform_name = xml_file.stem  # Filename without .xml extension
        
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Extract all ApplicationPath elements
            for game in root.findall(".//Game"):
                app_path = game.findtext("ApplicationPath", "").strip()
                if not app_path:
                    continue
                
                # Convert Windows path to forward slashes
                app_path = app_path.replace("\\", "/")
                
                # Strip Windows drive letter and WIN_ROOT if present
                if WIN_ROOT:
                    win_root_normalized = WIN_ROOT.replace("\\", "/").rstrip("/")
                    win_root_lower = win_root_normalized.lower()
                    app_path_lower = app_path.lower()
                    
                    # Check if path starts with WIN_ROOT (case-insensitive)
                    if app_path_lower.startswith(win_root_lower):
                        # Strip WIN_ROOT prefix
                        app_path = app_path[len(win_root_normalized):].lstrip("/")
                    elif ":" in app_path:
                        # Strip drive letter (e.g., Z:/)
                        app_path = re.sub(r'^[A-Za-z]:', '', app_path).lstrip("/")
                
                # Extract the platform directory (first component of path)
                # e.g., "Consoles/NEC - TurboGrafx 16/game.zip" → "Consoles/NEC - TurboGrafx 16"
                path_parts = app_path.split("/")
                if len(path_parts) >= 2:
                    # Include category and platform folder
                    platform_dir = "/".join(path_parts[:2])
                    platform_paths[platform_name].add(platform_dir.lower())
                    
        except ET.ParseError:
            continue
    
    # Build reverse mapping: normalized_path_prefix → platform_name
    for platform_name, paths in platform_paths.items():
        for path_prefix in paths:
            # Store the mapping (use the longest/most specific path if there are conflicts)
            if path_prefix not in PLATFORM_PATH_MAP or len(path_prefix) > len(PLATFORM_PATH_MAP.get(path_prefix, '')):
                PLATFORM_PATH_MAP[path_prefix] = platform_name
    
    if PLATFORM_PATH_MAP:
        print(f"✓ Built platform mapping from LaunchBox XMLs ({len(PLATFORM_PATH_MAP)} path prefixes)")


def load_config():
    """Load configuration from config.yaml"""
    global CONFIG, NAS_ROOT, WIN_ROOT, PLATFORM_LOOKUP, PATH_OVERRIDES
    
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if not config_path.exists():
            print("ERROR: config.yaml not found. Run 'python ludis.py setup' first.")
            sys.exit(1)
        
        with open(config_path) as f:
            CONFIG = yaml.safe_load(f)
        
        # Extract paths
        paths = CONFIG.get('paths', {})
        WIN_ROOT = paths.get('windows_root', '')
        library_base_path = paths.get('library_base_path', '')
        library_roots = paths.get('library_roots', [])
        
        if not library_base_path:
            print("ERROR: No library_base_path configured in config.yaml")
            print("Run setup wizard again or manually add 'library_base_path' to config.yaml")
            sys.exit(1)
        
        # Use the base path directly (the user already told us what it is!)
        NAS_ROOT = Path(library_base_path).resolve()
        
        if not NAS_ROOT.exists():
            print(f"ERROR: Library base path does not exist: {NAS_ROOT}")
            print(f"Make sure the storage is mounted and accessible.")
            sys.exit(1)
        
        # Load path overrides (for files that moved after LaunchBox import)
        PATH_OVERRIDES = CONFIG.get('options', {}).get('path_overrides', {})
        if PATH_OVERRIDES:
            # Normalize keys for case-insensitive matching
            PATH_OVERRIDES = {k.lower(): v for k, v in PATH_OVERRIDES.items()}
            print(f"✓ Loaded {len(PATH_OVERRIDES)} path override(s)")
        
        # Build platform path mapping from LaunchBox XMLs
        build_platform_path_mapping()
        
        # Build platform lookup dictionary (fallback for platforms not in LB)
        platform_structure = CONFIG.get('platform_structure', {})
        if not platform_structure:
            print("WARNING: No platform_structure found in config.yaml")
            print("Run the scanner again to configure platforms interactively.")
        
        for platform_name, config in platform_structure.items():
            plat_path = Path(config['path']).resolve()
            plat_type = config['type']
            
            # Calculate relative path from NAS_ROOT
            try:
                rel_path = plat_path.relative_to(NAS_ROOT)
                PLATFORM_LOOKUP[str(rel_path)] = {
                    'name': platform_name,
                    'type': plat_type,
                    'path': plat_path
                }
            except ValueError:
                print(f"WARNING: Platform path {plat_path} is not under NAS_ROOT {NAS_ROOT}")
        
        print(f"✓ Loaded {len(PLATFORM_LOOKUP)} platforms from config")
        print(f"✓ NAS Root: {NAS_ROOT}")
        
    except Exception as e:
        print(f"ERROR: Could not load config.yaml: {e}")
        sys.exit(1)


def find_common_parent(paths: List[Path]) -> Optional[Path]:
    """Find the common parent directory of multiple paths"""
    if not paths:
        return None
    
    # Start with the first path's parent (since we want the parent of the category folders)
    common = paths[0].parent
    
    # Keep going up until we find a common parent for all paths
    while common != common.parent:
        try:
            # Check if all paths are relative to this common parent
            if all(p.relative_to(common) for p in paths):
                return common
        except ValueError:
            pass
        common = common.parent
    
    return None


def get_platform_config(rel_path: str) -> Optional[Dict]:
    """
    Get platform configuration for a relative path.
    Returns config dict if path matches a configured platform, None otherwise.
    """
    # Normalize path separators
    rel_path = rel_path.replace('\\', '/')
    
    # Check if this path matches any configured platform
    if rel_path in PLATFORM_LOOKUP:
        return PLATFORM_LOOKUP[rel_path]
    
    return None


def resolve_platform_name(rel_path: str) -> str:
    """
    Resolve the LaunchBox platform name for a given file path.
    
    Uses LaunchBox XML data to determine the correct platform name,
    applying path_overrides if configured.
    
    Args:
        rel_path: Relative path from library root (e.g., "Consoles/NEC TurboGrafx-16 [1987]/game.zip")
    
    Returns:
        LaunchBox platform name (e.g., "NEC TurboGrafx-16")
    """
    # Normalize path
    normalized_path = rel_path.replace('\\', '/').lower()
    
    # Apply path overrides first (translate disk reality → LB expectations)
    for override_key, override_value in PATH_OVERRIDES.items():
        if normalized_path.startswith(override_key):
            # Replace the beginning of the path with the override value
            normalized_path = override_value.lower() + normalized_path[len(override_key):]
            break
    
    # Extract platform directory (first two components: category/platform)
    # e.g., "consoles/nec turbografx-16 [1987]/game.zip" → "consoles/nec turbografx-16 [1987]"
    path_parts = normalized_path.split("/")
    if len(path_parts) >= 2:
        platform_dir = "/".join(path_parts[:2])
        
        # Look up in platform mapping
        if platform_dir in PLATFORM_PATH_MAP:
            return PLATFORM_PATH_MAP[platform_dir]
        
        # Try without year suffix: "consoles/platform [1987]" → "consoles/platform"
        import re
        platform_dir_no_year = re.sub(r'\s*\[\d{4}\]$', '', platform_dir)
        if platform_dir_no_year != platform_dir and platform_dir_no_year in PLATFORM_PATH_MAP:
            return PLATFORM_PATH_MAP[platform_dir_no_year]
    
    # Fallback: use the platform name from platform_structure config
    # This handles platforms that exist on disk but not in LaunchBox
    for lookup_key, lookup_config in PLATFORM_LOOKUP.items():
        if normalized_path.startswith(lookup_key.lower()):
            return lookup_config['name']
    
    # Last resort: extract platform name from path
    # "Consoles/Platform Name [1987]/file" → "Platform Name [1987]"
    if len(path_parts) >= 2:
        return path_parts[1]
    
    return "Unknown"


def should_ignore_file(filename: str) -> bool:
    """Check if a file should be ignored based on ignore patterns"""
    ignore_patterns = CONFIG.get('options', {}).get('ignore_patterns', {}).get('files', [])
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False


def should_ignore_folder(foldername: str) -> bool:
    """Check if a folder should be ignored based on ignore patterns"""
    ignore_patterns = CONFIG.get('options', {}).get('ignore_patterns', {}).get('folders', [])
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(foldername, pattern):
            return True
    return False


def is_game_file(file_path: Path) -> bool:
    """Check if a file is a game file based on extension"""
    # Default game extensions
    GAME_EXTENSIONS = {
        '.zip', '.7z', '.iso', '.cue', '.bin', '.chd', '.rvz', '.gdi', '.nrg',
        '.wbfs', '.gcm', '.gcz', '.dol', '.elf', '.rom', '.nes', '.fds', '.sfc',
        '.smc', '.gba', '.gbc', '.gb', '.n64', '.z64', '.nds', '.3ds', '.wad',
        '.wua', '.xci', '.nsp', '.pbp', '.vpk', '.adf', '.m3u', '.xiso', '.cpr',
        '.vec', '.bs', '.pcm', '.pce', '.sgx', '.md', '.sms', '.nsz'
    }
    
    # Add user-configured additional extensions
    additional_exts = CONFIG.get('options', {}).get('additional_game_extensions', [])
    if additional_exts:
        # Normalize to lowercase and add to set
        for ext in additional_exts:
            GAME_EXTENSIONS.add(ext.lower())
    
    # Check ignore patterns first
    if should_ignore_file(file_path.name):
        return False
    
    return file_path.suffix.lower() in GAME_EXTENSIONS




def scan_library() -> Tuple[List[Dict], int]:
    """
    Scan the library by directly iterating configured platform paths.
    NO os.walk(), NO tree traversal - just iterate the exact paths from config.
    
    Returns (list of game entries, total games scanned)
    """
    platform_structure = CONFIG.get('platform_structure', {})
    if not platform_structure:
        print("ERROR: No platforms configured. Run interactive discovery first.")
        return [], 0
    
    games = []
    stats = defaultdict(int)
    
    print(f"\n{'='*60}")
    print(f"SCANNING LIBRARY")
    print(f"{'='*60}\n")
    
    total_start_time = time.time()
    
    # Iterate through configured platforms
    for platform_name, config in platform_structure.items():
        platform_path = Path(config['path'])
        platform_type = config['type']
        
        if platform_type == 'skip':
            print(f"[SKIP] {platform_name}")
            stats['skip'] += 1
            continue
        
        if not platform_path.exists():
            print(f"[ERROR] {platform_name} - path does not exist: {platform_path}")
            continue
        
        platform_start = time.time()
        
        if platform_type == 'files':
            # List files in this directory only
            print(f"[START] {platform_name} (files)")
            game_count = 0
            
            for item in platform_path.iterdir():
                # Check extension only - no stat calls
                if is_game_file(item):
                    rel_path = str(item.relative_to(NAS_ROOT))
                    # Resolve LaunchBox platform name from path
                    lb_platform_name = resolve_platform_name(rel_path)
                    
                    games.append({
                        'platform': lb_platform_name,
                        'title': item.stem,
                        'rel_path': rel_path,
                        'size_bytes': 0
                    })
                    game_count += 1
            
            elapsed = time.time() - platform_start
            print(f"[DONE]  {platform_name} - {game_count} games in {elapsed:.1f}s")
            stats['games'] += game_count
        
        elif platform_type == 'folders':
            # List folders in this directory only
            print(f"[START] {platform_name} (folders)")
            game_count = 0
            
            for item in platform_path.iterdir():
                # Skip ignored folders
                if should_ignore_folder(item.name):
                    continue
                    
                # Check if it's actually a directory (not just no extension)
                if item.is_dir():
                    rel_path = str(item.relative_to(NAS_ROOT))
                    # Resolve LaunchBox platform name from path
                    lb_platform_name = resolve_platform_name(rel_path)
                    
                    games.append({
                        'platform': lb_platform_name,
                        'title': item.name,
                        'rel_path': rel_path,
                        'size_bytes': 0
                    })
                    game_count += 1
            
            elapsed = time.time() - platform_start
            print(f"[DONE]  {platform_name} - {game_count} games in {elapsed:.1f}s")
            stats['games'] += game_count
        
        elif platform_type == 'nested':
            # Scan configured subpaths
            scan_paths = config.get('scan_paths', [])
            print(f"[START] {platform_name} (nested: {len(scan_paths)} paths)")
            game_count = 0
            
            for scan_config in scan_paths:
                subpath = scan_config['path']
                subpath_type = scan_config['type']
                full_subpath = platform_path / subpath
                
                if not full_subpath.exists():
                    print(f"  [WARN] Subpath not found: {subpath}")
                    continue
                
                print(f"  → {subpath}/ ({subpath_type})")
                subpath_games = 0
                
                if subpath_type == 'files':
                    # Scan for ROM files in this subfolder
                    for item in full_subpath.iterdir():
                        if is_game_file(item):
                            rel_path = str(item.relative_to(NAS_ROOT))
                            # Resolve LaunchBox platform name from path
                            lb_platform_name = resolve_platform_name(rel_path)
                            
                            games.append({
                                'platform': lb_platform_name,
                                'title': item.stem,
                                'rel_path': rel_path,
                                'size_bytes': 0
                            })
                            subpath_games += 1
                            game_count += 1
                
                elif subpath_type == 'folders':
                    # Scan for game folders in this subfolder
                    for item in full_subpath.iterdir():
                        # Skip ignored folders
                        if should_ignore_folder(item.name):
                            continue
                        
                        # Check if it's actually a directory
                        if item.is_dir():
                            rel_path = str(item.relative_to(NAS_ROOT))
                            # Resolve LaunchBox platform name from path
                            lb_platform_name = resolve_platform_name(rel_path)
                            
                            games.append({
                                'platform': lb_platform_name,
                                'title': item.name,
                                'rel_path': rel_path,
                                'size_bytes': 0
                            })
                            subpath_games += 1
                            game_count += 1
                
                print(f"    → {subpath_games} games")
            
            elapsed = time.time() - platform_start
            print(f"[DONE]  {platform_name} - {game_count} games in {elapsed:.1f}s")
            stats['games'] += game_count
    
    total_elapsed = time.time() - total_start_time
    total_games = len(games)
    
    print(f"\n{'='*60}")
    print(f"SCAN COMPLETE")
    print(f"{'='*60}")
    print(f"Total games: {total_games}")
    print(f"Total time: {total_elapsed:.1f}s")
    
    return games, total_games


def write_nas_inventory(games: List[Dict], platform_filter: Optional[str] = None):
    """Write NAS inventory to CSV files"""
    if platform_filter:
        games = [g for g in games if platform_filter.lower() in g['platform'].lower()]
        if not games:
            print(f"No games found matching filter: {platform_filter}")
            return
    
    # Group by platform
    by_platform = defaultdict(list)
    for game in games:
        by_platform[game['platform']].append(game)
    
    # Write per-platform files
    subdir = OUTDIR / "nas_inventory"
    subdir.mkdir(parents=True, exist_ok=True)
    
    for platform_name, platform_games in sorted(by_platform.items()):
        safe_name = sanitize_filename(platform_name)
        output_file = subdir / f"{safe_name}.csv"
        
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=['platform', 'title', 'rel_path', 'size_bytes'])
            writer.writeheader()
            for game in sorted(platform_games, key=lambda x: x['title'].lower()):
                writer.writerow({
                    'platform': game['platform'],
                    'title': game['title'],
                    'rel_path': game['rel_path'],
                    'size_bytes': game['size_bytes']
                })
        
        print(f"✓ {platform_name}: {len(platform_games)} games → {output_file.name}")
    
    # Write combined file if no filter
    if not platform_filter:
        output_file = OUTDIR / "nas_inventory.csv"
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=['platform', 'title', 'rel_path', 'size_bytes'])
            writer.writeheader()
            for game in sorted(games, key=lambda x: (x['platform'], x['title'].lower())):
                writer.writerow({
                    'platform': game['platform'],
                    'title': game['title'],
                    'rel_path': game['rel_path'],
                    'size_bytes': game['size_bytes']
                })
        print(f"\n✓ Combined inventory: {output_file} ({len(games)} total games)")


def sanitize_filename(name: str) -> str:
    """Make a string safe for use as a filename"""
    return name.replace('/', '_').replace('\\', '_').replace(':', '-').replace('*', '-').strip()


def cmd_nas_inventory(args):
    """Command: Generate NAS inventory"""
    games, _ = scan_library()
    write_nas_inventory(games, args.platform)


def main():
    parser = argparse.ArgumentParser(
        description="Ludis Library Scanner - Config-driven filesystem auditing"
    )
    parser.add_argument(
        '--platform',
        help='Filter by platform name (partial match)',
        default=None
    )
    
    subparsers = parser.add_subparsers(dest='cmd', required=True)
    subparsers.add_parser('nas-inventory', help='Scan library and generate inventory CSV')
    
    args = parser.parse_args()
    
    # Load config first
    load_config()
    
    # Route to command
    if args.cmd == 'nas-inventory':
        cmd_nas_inventory(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
