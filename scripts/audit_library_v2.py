#!/usr/bin/env python3
"""
Generic Library Scanner - No Hardcoded Assumptions
===================================================

Scans library_roots from config.yaml and matches to LaunchBox XML entries.
Works with ANY folder structure - no platform-specific rules.
"""

import argparse
import csv
import sys
import os
import subprocess
from pathlib import Path
from typing import List, Dict, Set, Optional
import time

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "LB_Exports" / "all_platforms.csv"
OUTDIR = PROJECT_ROOT / "LB_Exports" / "audits"


def load_config():
    """Load configuration from config.yaml"""
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if not config_path.exists():
            print("ERROR: config.yaml not found. Please complete initial setup in ludis.py first.")
            print("(This scanner requires config.yaml to know where your library is located)")
            return None, [], []
        
        with open(config_path) as f:
            config = yaml.safe_load(f)
            
            paths = config.get('paths', {})
            windows_root = paths.get('windows_root', '')
            library_roots = paths.get('library_roots', [])
            
            if not library_roots:
                # Backward compatibility
                local_root = paths.get('local_root')
                if local_root:
                    library_roots = [local_root]
                else:
                    print("ERROR: No library_roots in config.yaml")
                    sys.exit(1)
            
            excluded = config.get('options', {}).get('exclude_platforms', [])
            excluded_platforms = [p.lower() for p in excluded]
            
            return windows_root, library_roots, excluded_platforms
            
    except Exception as e:
        print(f"ERROR loading config.yaml: {e}")
        sys.exit(1)


def get_known_extensions() -> Set[str]:
    """
    Return set of known game file extensions.
    Users can extend this in config.yaml (future enhancement).
    """
    return {
        # Archives
        ".zip", ".7z", ".rar",
        # Disc images
        ".iso", ".cue", ".bin", ".chd", ".rvz", ".gdi", ".nrg", ".wbfs", ".gcm", ".gcz",
        # Nintendo
        ".nes", ".fds", ".sfc", ".smc", ".n64", ".z64", ".v64", ".nds", ".3ds",
        ".wad", ".wua", ".xci", ".nsp",
        # Sega
        ".md", ".sms", ".gg", ".32x",
        # Sony
        ".pbp",
        # Handhelds
        ".gba", ".gbc", ".gb",
        # Other
        ".rom", ".dol", ".elf", ".adf", ".m3u", ".xiso",
        ".cpr", ".vec", ".bs", ".pcm", ".pce", ".sgx", ".nsz",
        # PC
        ".exe", ".bat",
    }


def get_folder_size(folder_path: Path) -> int:
    """Get folder size using du command (fast)."""
    try:
        result = subprocess.run(
            ['du', '-sk', str(folder_path)],
            capture_output=True,
            text=True,
            check=True,
            timeout=30
        )
        size_kb = int(result.stdout.split()[0])
        return size_kb * 1024
    except Exception:
        return 0


def scan_library_root(root: Path, known_exts: Set[str], verbose: bool = False) -> Dict[str, Dict]:
    """
    Efficiently scan a library root for game files.
    
    Strategy:
    - Walk directory tree with os.walk() (faster than rglob)
    - Skip common non-game folders early
    - Only check files with known extensions
    - Use platform/subfolder detection for folder-based games
    
    Returns:
        {relative_path: {'size': int, 'type': 'file'|'folder', 'name': str}}
    """
    if not root.exists():
        print(f"⚠ Warning: Library root not found: {root}")
        return {}
    
    found = {}
    
    print(f"\nScanning: {root.name}")
    start_time = time.time()
    file_count = 0
    folder_count = 0
    platform_count = 0
    last_update = time.time()
    
    skip_names = {'bios', 'saves', 'screenshots', 'manuals', 'artwork', 'videos', 'music'}
    
    # Walk the tree (much faster than rglob)
    for dirpath, dirnames, filenames in os.walk(root):
        current_dir = Path(dirpath)
        relative_dir = current_dir.relative_to(root)
        
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        # Skip common non-game folders
        dirnames[:] = [d for d in dirnames if not any(skip in d.lower() for skip in skip_names)]
        
        # Progress indicator every 2 seconds
        now = time.time()
        if now - last_update > 2:
            print(f"  Scanning: {relative_dir} ({file_count} files, {folder_count} folders found)", end='\r')
            last_update = now
        
        # Check if we're in a platform folder (1-2 levels deep from root)
        depth = len(relative_dir.parts)
        if depth == 1:
            platform_count += 1
            print(f"  Platform {platform_count}: {relative_dir}")
        
        # Scan files in this directory
        game_files_here = []
        for filename in filenames:
            ext = Path(filename).suffix.lower()
            if ext in known_exts:
                filepath = current_dir / filename
                try:
                    size = filepath.stat().st_size
                    rel_path = filepath.relative_to(root)
                    found[str(rel_path)] = {
                        'size': size,
                        'type': 'file',
                        'name': filename
                    }
                    file_count += 1
                    game_files_here.append(filename)
                except Exception:
                    pass
        
        # Check if this is a "folder-per-game" situation
        # If there are subdirectories but no game files at this level
        if dirnames and not game_files_here and depth >= 1:
            # This folder might contain game folders
            # Sample first few subdirs to see if they're game folders
            for subdir_name in dirnames[:5]:  # Only check first 5
                subdir = current_dir / subdir_name
                # Quick check: does this subfolder have game files or looks like a game?
                has_content = False
                try:
                    for item in subdir.iterdir():
                        if item.is_file():
                            has_content = True
                            break
                except PermissionError:
                    continue
                
                if has_content:
                    # This looks like a game folder - record the subdirs, not this parent
                    for subdir_name in dirnames:
                        subdir = current_dir / subdir_name
                        if subdir.is_dir():
                            size = get_folder_size(subdir)
                            if size > 0:
                                rel_path = subdir.relative_to(root)
                                found[str(rel_path)] = {
                                    'size': size,
                                    'type': 'folder',
                                    'name': subdir_name
                                }
                                folder_count += 1
                    
                    # Don't descend into these game folders
                    dirnames.clear()
                    break
    
    elapsed = time.time() - start_time
    print(f"\n  ✓ Found {file_count} files and {folder_count} folders in {elapsed:.1f}s")
    
    return found


def normalize_path(path_str: str, windows_root: str) -> str:
    """
    Convert Windows path from LaunchBox XML to relative path.
    
    Example:
        windows_root: Z:\\media\\games\\library
        path_str: Z:\\media\\games\\library\\Consoles\\N64\\Game.n64
        returns: Consoles/N64/Game.n64
    """
    if not path_str:
        return ""
    
    # Normalize separators
    path = path_str.replace("\\", "/")
    win_root = windows_root.replace("\\", "/").rstrip("/")
    
    # Remove windows_root prefix (case-insensitive)
    if path.lower().startswith(win_root.lower()):
        suffix = path[len(win_root):]
        if suffix.startswith("/"):
            suffix = suffix[1:]
        return suffix
    
    return path


def fuzzy_match(needle: str, haystack: Dict[str, Dict], threshold: float = 0.8) -> Optional[str]:
    """
    Find best fuzzy match for needle in haystack keys.
    
    Matching strategy:
    1. Exact match (case-insensitive)
    2. Filename match (last component)
    3. Partial path match
    """
    needle_lower = needle.lower()
    needle_name = Path(needle).name.lower()
    
    # Try exact match first
    if needle_lower in {k.lower() for k in haystack.keys()}:
        for k in haystack.keys():
            if k.lower() == needle_lower:
                return k
    
    # Try filename match
    for path, data in haystack.items():
        if data['name'].lower() == needle_name:
            return path
    
    # Try partial path match (last 2-3 components)
    needle_parts = Path(needle).parts[-3:]  # Last 3 path components
    best_match = None
    best_score = 0
    
    for path in haystack.keys():
        path_parts = Path(path).parts
        
        # Count matching components
        matches = sum(1 for n in needle_parts if any(n.lower() in p.lower() for p in path_parts))
        score = matches / len(needle_parts)
        
        if score > best_score and score >= threshold:
            best_score = score
            best_match = path
    
    return best_match


def match_csv_to_scanned(csv_data: List[Dict], scanned: Dict[str, Dict], windows_root: str) -> List[Dict]:
    """
    Match LaunchBox CSV entries to scanned files.
    
    Returns augmented CSV data with FileSize and NASPath.
    """
    matched_count = 0
    unmatched_count = 0
    
    print(f"\nMatching {len(csv_data)} LaunchBox entries to {len(scanned)} scanned files...")
    
    for row in csv_data:
        lb_path = row.get('LBFilePath', '').strip()
        if not lb_path:
            row['FileSize'] = 0
            row['NASPath'] = ''
            unmatched_count += 1
            continue
        
        # Normalize LaunchBox path
        relative = normalize_path(lb_path, windows_root)
        
        # Try to find in scanned files
        matched_path = fuzzy_match(relative, scanned)
        
        if matched_path:
            row['FileSize'] = scanned[matched_path]['size']
            row['NASPath'] = matched_path
            matched_count += 1
        else:
            row['FileSize'] = 0
            row['NASPath'] = ''
            unmatched_count += 1
    
    print(f"  ✓ Matched: {matched_count}")
    print(f"  ✗ Unmatched: {unmatched_count}")
    
    return csv_data


def main():
    parser = argparse.ArgumentParser(description="CSV-driven library scanner (fast!)")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    args = parser.parse_args()
    
    print("=" * 60)
    print("LIBRARY SCANNER v2.0 (CSV-Driven)")
    print("=" * 60)
    
    # Load config
    print("\n1. Loading configuration...")
    config_result = load_config()
    if config_result == (None, [], []):
        print("\nPlease run: python3 ludis.py")
        print("Complete the setup wizard to create config.yaml")
        sys.exit(1)
    
    windows_root, library_roots, excluded = config_result
    print(f"  Windows root: {windows_root}")
    print(f"  Library roots: {len(library_roots)}")
    for root in library_roots:
        print(f"    - {root}")
    
    # Load CSV first (CSV-driven approach)
    print("\n2. Loading LaunchBox data...")
    if not CSV_PATH.exists():
        print(f"ERROR: {CSV_PATH} not found. Run platform export first.")
        sys.exit(1)
    
    csv_data = []
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        csv_data = list(reader)
    
    print(f"  Loaded {len(csv_data)} LaunchBox entries")
    
    # Verify files exist and get sizes (CSV-driven!)
    print("\n3. Verifying files from LaunchBox...")
    print(f"  (Checking {len(csv_data)} entries - much faster than scanning everything!)")
    
    matched_count = 0
    missing_count = 0
    last_update = time.time()
    
    for i, row in enumerate(csv_data):
        # Progress every 2 seconds
        now = time.time()
        if now - last_update > 2 or i % 1000 == 0:
            print(f"  Checked: {i}/{len(csv_data)} ({matched_count} found, {missing_count} missing)", end='\r')
            last_update = now
        
        lb_path = row.get('LBFilePath', '').strip()
        if not lb_path:
            row['FileSize'] = 0
            row['NASPath'] = ''
            missing_count += 1
            continue
        
        # Normalize path
        relative = normalize_path(lb_path, windows_root)
        
        # Try to find the file in library_roots
        found = False
        for root_str in library_roots:
            root = Path(root_str)
            full_path = root / relative
            
            if full_path.exists():
                if full_path.is_file():
                    try:
                        size = full_path.stat().st_size
                        row['FileSize'] = size
                        row['NASPath'] = relative
                        matched_count += 1
                        found = True
                        break
                    except Exception:
                        pass
                elif full_path.is_dir():
                    # Folder-based game
                    size = get_folder_size(full_path)
                    row['FileSize'] = size
                    row['NASPath'] = relative
                    matched_count += 1
                    found = True
                    break
        
        if not found:
            row['FileSize'] = 0
            row['NASPath'] = ''
            missing_count += 1
    
    print(f"\n  ✓ Matched: {matched_count}")
    print(f"  ✗ Missing: {missing_count}")
    
    # Write output
    print("\n4. Writing nas_inventory.csv...")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    output_path = PROJECT_ROOT / "LB_Exports" / "nas_inventory.csv"
    
    if csv_data:
        fieldnames = list(csv_data[0].keys())
        
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(csv_data)
        
        print(f"  ✓ Wrote {output_path}")
    
    print("\n" + "=" * 60)
    print("✓ SCAN COMPLETE")
    print("=" * 60)
    
    # Summary statistics
    total_size = sum(row.get('FileSize', 0) for row in csv_data)
    size_gb = total_size / (1024**3)
    print(f"\nTotal library size: {size_gb:.2f} GB")
    print(f"Match rate: {matched_count}/{len(csv_data)} ({matched_count/len(csv_data)*100:.1f}%)")


if __name__ == "__main__":
    main()

