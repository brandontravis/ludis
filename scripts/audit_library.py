#!/usr/bin/env python3
"""
Ludis Library Scanner - Config-Driven Filesystem Auditing
Scans game library based on platform_structure configuration.
No hardcoded paths or platform-specific logic.
"""
import argparse
import csv
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


def load_config():
    """Load configuration from config.yaml"""
    global CONFIG, NAS_ROOT, WIN_ROOT, PLATFORM_LOOKUP
    
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
        library_roots = paths.get('library_roots', [])
        
        if not library_roots:
            print("ERROR: No library_roots configured in config.yaml")
            sys.exit(1)
        
        # Determine NAS_ROOT as common parent of all library_roots
        root_paths = [Path(p).resolve() for p in library_roots]
        NAS_ROOT = find_common_parent(root_paths)
        
        if not NAS_ROOT:
            print(f"ERROR: Could not determine NAS root from library_roots")
            sys.exit(1)
        
        if not NAS_ROOT.exists():
            print(f"ERROR: NAS root does not exist: {NAS_ROOT}")
            print(f"Make sure the NAS is mounted and accessible.")
            sys.exit(1)
        
        # Build platform lookup dictionary
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


def is_game_file(file_path: Path) -> bool:
    """Check if a file is a game file based on extension"""
    GAME_EXTENSIONS = {
        '.zip', '.7z', '.iso', '.cue', '.bin', '.chd', '.rvz', '.gdi', '.nrg',
        '.wbfs', '.gcm', '.gcz', '.dol', '.elf', '.rom', '.nes', '.fds', '.sfc',
        '.smc', '.gba', '.gbc', '.gb', '.n64', '.z64', '.nds', '.3ds', '.wad',
        '.wua', '.xci', '.nsp', '.pbp', '.vpk', '.adf', '.m3u', '.xiso', '.cpr',
        '.vec', '.bs', '.pcm', '.pce', '.sgx', '.md', '.sms', '.nsz'
    }
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
                    games.append({
                        'platform': platform_name,
                        'title': item.stem,
                        'rel_path': str(item.relative_to(NAS_ROOT)),
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
                # Assume no extension = folder (no stat calls)
                if not item.suffix:
                    games.append({
                        'platform': platform_name,
                        'title': item.name,
                        'rel_path': str(item.relative_to(NAS_ROOT)),
                        'size_bytes': 0
                    })
                    game_count += 1
            
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
