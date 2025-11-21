#!/usr/bin/env python3
"""
Interactive Library Scanner
============================

FAST scanner using the proven os.walk() approach from audit_library.py,
adapted to use platform_structure from config instead of hardcoded rules.
"""

import sys
import os
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict
import time

# Check for inquirer
try:
    import inquirer
except ImportError:
    print("ERROR: inquirer not installed. Run: pip install inquirer")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_config():
    """Load configuration from config.yaml"""
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if not config_path.exists():
            print("ERROR: config.yaml not found")
            sys.exit(1)
        
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
            
        paths = config_data.get('paths', {})
        library_roots = paths.get('library_roots', [])
        platform_structure = config_data.get('platform_structure', {})
        
        return library_roots, platform_structure, config_data
        
    except Exception as e:
        print(f"ERROR loading config: {e}")
        sys.exit(1)


def save_platform_structure(config_data: Dict, platform_structure: Dict):
    """Save platform structure back to config.yaml"""
    import yaml
    
    config_data['platform_structure'] = platform_structure
    config_path = PROJECT_ROOT / "config.yaml"
    
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n✓ Saved platform structure to config.yaml")


def discover_structure_interactively(library_roots: List[str]) -> Dict:
    """
    Interactively discover folder structure.
    Each immediate subdirectory under library_roots is a platform.
    """
    print("\n" + "=" * 60)
    print("INTERACTIVE STRUCTURE DISCOVERY")
    print("=" * 60)
    print("\nFirst-time setup: I'll ask you about your folder structure.")
    print("This only happens once - answers are saved to config.yaml")
    print("\nScanning your library roots for platforms...")
    
    all_platforms = []
    
    for root_str in library_roots:
        root = Path(root_str)
        if not root.exists():
            print(f"⚠ Path does not exist: {root_str}")
            continue
        
        try:
            for item in root.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    all_platforms.append({
                        'name': item.name,
                        'path': item,
                        'root': root.name
                    })
        except Exception as e:
            print(f"⚠ Error reading {root_str}: {e}")
            continue
    
    if not all_platforms:
        print("\n✗ No platforms found in library roots")
        return {}
    
    print(f"\n✓ Found {len(all_platforms)} platforms across {len(library_roots)} library roots\n")
    print("=" * 60)
    
    platform_structure = {}
    
    for platform in sorted(all_platforms, key=lambda x: (x['root'], x['name'])):
        name = platform['name']
        path = platform['path']
        root = platform['root']
        
        print(f"\n{root}/{name}")
        
        items = []
        try:
            for i, item in enumerate(path.iterdir()):
                if i >= 5:
                    break
                if not item.name.startswith('.'):
                    items.append(item)
        except Exception as e:
            print(f"  ⚠ Error reading: {e}")
            continue
        
        if not items:
            print("  (empty or inaccessible)")
            continue
        
        preview = []
        all_files = True
        all_dirs = True
        
        for item in items:
            if item.is_file():
                preview.append(item.name)
                all_dirs = False
            elif item.is_dir():
                preview.append(item.name + '/')
                all_files = False
        
        print(f"  ({', '.join(preview)}{', ...' if len(items) >= 5 else ''})")
        
        if all_files:
            print("  ✓ Auto-detected: Files (ROM files)")
            platform_structure[name] = {
                'path': str(path),
                'type': 'files'
            }
            continue
        
        if all_dirs:
            choice = inquirer.prompt([
                inquirer.List(
                    'action',
                    message="This folder contains:",
                    choices=[
                        ('Game directories (1 folder = 1 game)', 'folders'),
                        ('Subfolders (scan deeper)', 'deeper'),
                        ('Skip this platform', 'skip')
                    ]
                )
            ])
            
            if not choice or choice['action'] == 'skip':
                print("  → Skipped")
                continue
            elif choice['action'] == 'folders':
                print("  ✓ Will scan for game directories")
                platform_structure[name] = {
                    'path': str(path),
                    'type': 'folders'
                }
            elif choice['action'] == 'deeper':
                print("  → Complex structure (will be skipped for now)")
                platform_structure[name] = {
                    'path': str(path),
                    'type': 'skip',
                    'reason': 'complex'
                }
        else:
            choice = inquirer.prompt([
                inquirer.List(
                    'action',
                    message="This folder contains mixed content:",
                    choices=[
                        ('Treat as files (scan for ROM files)', 'files'),
                        ('Treat as folders (1 folder = 1 game)', 'folders'),
                        ('Skip this platform', 'skip')
                    ]
                )
            ])
            
            if not choice or choice['action'] == 'skip':
                print("  → Skipped")
                continue
            else:
                print(f"  ✓ Will scan for {choice['action']}")
                platform_structure[name] = {
                    'path': str(path),
                    'type': choice['action']
                }
    
    # Confirmation screen
    while True:
        print("\n" + "=" * 60)
        print("REVIEW PLATFORM CONFIGURATION")
        print("=" * 60)
        
        for name in sorted(platform_structure.keys()):
            config = platform_structure[name]
            ptype = config['type']
            if ptype == 'skip':
                print(f"  {name}: Skipped (complex)")
            elif ptype == 'files':
                print(f"  {name}: Files")
            elif ptype == 'folders':
                print(f"  {name}: Folders")
        
        scannable = sum(1 for p in platform_structure.values() if p['type'] != 'skip')
        print(f"\n✓ {scannable} platforms configured")
        
        choices = []
        for name in sorted(platform_structure.keys()):
            config = platform_structure[name]
            ptype = config['type']
            if ptype == 'skip':
                label = f"{name}: Skipped (complex)"
            elif ptype == 'files':
                label = f"{name}: Files"
            elif ptype == 'folders':
                label = f"{name}: Folders"
            else:
                label = f"{name}: {ptype}"
            choices.append((label, name))
        
        reconfigure = inquirer.prompt([
            inquirer.Checkbox(
                'platforms',
                message="Check any platforms to RECONFIGURE (or leave empty to proceed)",
                choices=choices
            )
        ])
        
        if not reconfigure or not reconfigure['platforms']:
            break
        
        print("\n" + "=" * 60)
        print("RECONFIGURING SELECTED PLATFORMS")
        print("=" * 60)
        
        for name in reconfigure['platforms']:
            config = platform_structure[name]
            path = Path(config['path'])
            
            print(f"\n{name}")
            print(f"  Current: {config['type']}")
            
            items = []
            try:
                for i, item in enumerate(path.iterdir()):
                    if i >= 5:
                        break
                    if not item.name.startswith('.'):
                        items.append(item)
            except Exception as e:
                print(f"  ⚠ Error reading: {e}")
                continue
            
            preview = []
            for item in items:
                if item.is_file():
                    preview.append(item.name)
                elif item.is_dir():
                    preview.append(item.name + '/')
            
            print(f"  ({', '.join(preview)}{', ...' if len(items) >= 5 else ''})")
            
            choice = inquirer.prompt([
                inquirer.List(
                    'action',
                    message="Configure as:",
                    choices=[
                        ('Files (scan for ROM files)', 'files'),
                        ('Folders (1 folder = 1 game)', 'folders'),
                        ('Skip (complex structure)', 'skip')
                    ]
                )
            ])
            
            if choice:
                platform_structure[name]['type'] = choice['action']
                print(f"  ✓ Updated to: {choice['action']}")
    
    scannable = sum(1 for p in platform_structure.values() if p['type'] != 'skip')
    skipped = len(platform_structure) - scannable
    
    print("\n" + "=" * 60)
    print(f"✓ Configured {scannable} platforms")
    if skipped > 0:
        print(f"  ({skipped} skipped)")
    print("=" * 60)
    
    return platform_structure


def get_known_extensions() -> Set[str]:
    """Known game file extensions"""
    return {
        ".zip", ".7z", ".rar", ".iso", ".cue", ".bin", ".chd", ".rvz", ".gdi", ".nrg",
        ".wbfs", ".gcm", ".gcz", ".dol", ".elf", ".rom", ".nes", ".fds", ".sfc", ".smc",
        ".gba", ".gbc", ".gb", ".n64", ".z64", ".v64", ".nds", ".3ds", ".wad", ".wua",
        ".xci", ".nsp", ".pbp", ".vpk", ".adf", ".m3u", ".xiso", ".cpr", ".vec", ".bs",
        ".pcm", ".pce", ".sgx", ".md", ".sms", ".gg", ".32x", ".nsz", ".exe", ".bat",
    }


def scan_with_structure(library_roots: List[str], platform_structure: Dict) -> Dict:
    """
    FAST scan using os.walk() - copied from old audit_library.py.
    Adapted to use platform_structure instead of hardcoded rules.
    """
    print("\n" + "=" * 60)
    print("SCANNING LIBRARY")
    print("=" * 60)
    
    found = {}
    known_exts = get_known_extensions()
    folder_sizes = defaultdict(int)
    
    # Build fast lookup: "Category/Platform" -> (type, depth_to_collapse)
    platform_rules = {}
    for platform_name, config in platform_structure.items():
        ptype = config.get('type', 'files')
        if ptype == 'skip':
            print(f"  ⊘ Skipping: {platform_name}")
            continue
        
        platform_path = Path(config['path'])
        # Extract the relative key (e.g., "Consoles/Nintendo 64")
        for root_str in library_roots:
            root_path = Path(root_str)
            if platform_path.is_relative_to(root_path):
                rel_key = str(platform_path.relative_to(root_path))
                platform_rules[rel_key] = (ptype, platform_name)
                break
    
    total_files = 0
    total_folders = 0
    
    # ONE os.walk() per library root (FAST like the old code)
    for root_str in library_roots:
        root = Path(root_str)
        if not root.exists():
            continue
        
        print(f"\n  Walking: {root.name}")
        dirs_seen = 0
        files_seen = 0
        last_log = time.time()
        scan_start = time.time()
        
        for dirpath, dirnames, filenames in os.walk(root):
            rel = Path(dirpath).relative_to(root)
            rel_str = str(rel) if str(rel) != "." else ""
            rel_parts = list(rel.parts) if rel_str else []
            
            dirs_seen += 1
            
            # Progress
            if dirs_seen % 100 == 0 or (time.time() - last_log) > 1.0:
                elapsed = time.time() - scan_start
                rate = dirs_seen / elapsed if elapsed > 0 else 0
                display_path = rel_str if len(rel_str) < 50 else "..." + rel_str[-47:]
                print(f"\r    {display_path:<50} | {dirs_seen} dirs, {rate:.0f}/s  ", end='', flush=True)
                last_log = time.time()
            
            # Check if this path matches a configured platform
            if rel_str in platform_rules:
                ptype, platform_name = platform_rules[rel_str]
                
                if ptype == 'files':
                    # File platform: collect game files here, don't descend
                    count = 0
                    for fn in filenames:
                        if Path(fn).suffix.lower() in known_exts:
                            try:
                                file_path = Path(dirpath) / fn
                                size = file_path.stat().st_size
                                rel_path = file_path.relative_to(root)
                                found[str(rel_path)] = {
                                    'size': size,
                                    'type': 'file',
                                    'name': fn
                                }
                                count += 1
                                total_files += 1
                                files_seen += 1
                            except:
                                pass
                    print(f"\n    ✓ {platform_name}: {count} files")
                    dirnames[:] = []  # Don't descend
                    continue
                
                elif ptype == 'folders':
                    # Folder platform: record immediate subdirs as games, walk for sizes
                    # Don't prune yet - need to accumulate sizes
                    pass
            
            # Check if we're ONE level inside a 'folders' platform
            if len(rel_parts) >= 2:
                parent_key = "/".join(rel_parts[:-1])
                if parent_key in platform_rules:
                    ptype, platform_name = platform_rules[parent_key]
                    if ptype == 'folders':
                        # We're at the game folder level (1 level inside folders platform)
                        # Record it if we haven't already
                        game_folder_rel = rel
                        if str(game_folder_rel) not in found:
                            found[str(game_folder_rel)] = {
                                'size': 0,  # Will update
                                'type': 'folder',
                                'name': rel_parts[-1]
                            }
                            total_folders += 1
                        
                        # Accumulate file sizes as we walk
                        for fn in filenames:
                            try:
                                fp = Path(dirpath) / fn
                                size = fp.stat().st_size
                                folder_sizes[str(game_folder_rel)] += size
                                files_seen += 1
                            except:
                                pass
            
            # Regular file processing for size accumulation
            if files_seen and (files_seen % 5000 == 0 or (time.time() - last_log) > 2.0):
                print(f"\n    ... {dirs_seen} dirs, {files_seen} files, {total_files + total_folders} games", flush=True)
                last_log = time.time()
    
    # Update folder sizes
    for path_str, data in found.items():
        if data['type'] == 'folder' and path_str in folder_sizes:
            data['size'] = folder_sizes[path_str]
    
    # Summary
    print("\n\n" + "=" * 60)
    print("SCAN SUMMARY")
    print("=" * 60)
    print(f"Total game files: {total_files:,}")
    print(f"Total game folders: {total_folders:,}")
    print(f"Total games: {total_files + total_folders:,}")
    
    return found


def write_nas_inventory(found: Dict):
    """Write NAS inventory CSV"""
    import csv
    
    output_path = PROJECT_ROOT / "LB_Exports" / "nas_inventory.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    rows = []
    for path, data in found.items():
        rows.append({
            'NASPath': path,
            'Filename': data['name'],
            'FileSize': data['size'],
            'Type': data['type'],
        })
    
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['NASPath', 'Filename', 'FileSize', 'Type'])
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"\n✓ Wrote {output_path}")
    
    total_size = sum(r['FileSize'] for r in rows)
    size_gb = total_size / (1024**3)
    print(f"  Total size: {size_gb:.2f} GB")


def main():
    print("=" * 60)
    print("INTERACTIVE LIBRARY SCANNER")
    print("=" * 60)
    
    library_roots, platform_structure, config_data = load_config()
    
    if not platform_structure:
        print("\n⚠ No platform structure configured")
        platform_structure = discover_structure_interactively(library_roots)
        save_platform_structure(config_data, platform_structure)
    else:
        print(f"\n✓ Using cached platform structure ({len(platform_structure)} platforms)")
    
    found = scan_with_structure(library_roots, platform_structure)
    write_nas_inventory(found)
    
    print("\n" + "=" * 60)
    print("✓ SCAN COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
