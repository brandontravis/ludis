#!/usr/bin/env python3
"""
Interactive Library Scanner
============================

FAST scanner using the proven os.walk() approach from audit_library.py,
adapted to use platform_structure from config instead of hardcoded rules.
"""

import sys
import os
import fnmatch
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


def should_ignore_folder(foldername: str, config_data: Dict) -> bool:
    """Check if a folder should be ignored based on ignore patterns"""
    ignore_patterns = config_data.get('options', {}).get('ignore_patterns', {}).get('folders', [])
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(foldername, pattern):
            return True
    return False


def save_platform_structure(config_data: Dict, platform_structure: Dict):
    """Save platform structure back to config.yaml"""
    import yaml
    
    config_data['platform_structure'] = platform_structure
    config_path = PROJECT_ROOT / "config.yaml"
    
    with open(config_path, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n✓ Saved platform structure to config.yaml")


def configure_nested_path(parent_path: Path, relative_path: str = "", config_data: Dict = None) -> List[Dict]:
    """
    Recursively configure a nested path structure.
    Returns a list of scan path configurations with their relative paths.
    
    Each entry is like: {'path': 'Base Games/EBoot', 'type': 'folders'}
    """
    # Get all subdirectories
    subdirs = []
    has_files = False
    
    try:
        for item in parent_path.iterdir():
            if item.name.startswith('.'):
                continue
            if item.is_dir():
                # Skip folders matching ignore patterns
                if config_data and should_ignore_folder(item.name, config_data):
                    continue
                subdirs.append(item)
            elif item.is_file():
                has_files = True
    except Exception as e:
        print(f"  ⚠ Error reading directory: {e}")
        return []
    
    subdirs.sort(key=lambda x: x.name)
    
    # Determine what this folder contains
    all_files = has_files and len(subdirs) == 0
    all_dirs = not has_files and len(subdirs) > 0
    mixed = has_files and len(subdirs) > 0
    
    # Show preview
    display_path = relative_path if relative_path else "(root)"
    print(f"\n{display_path}/")
    
    preview_items = []
    try:
        for i, item in enumerate(parent_path.iterdir()):
            if i >= 5:
                break
            if not item.name.startswith('.'):
                if item.is_file():
                    preview_items.append(item.name)
                elif item.is_dir():
                    preview_items.append(item.name + '/')
    except:
        preview_items = ['(unreadable)']
    
    preview = ', '.join(preview_items)
    if len(list(parent_path.iterdir())) > 5:
        preview += ', ...'
    print(f"  ({preview})")
    
    # Auto-detect if it's all ROM files
    if all_files:
        print("  ✓ Auto-detected: ROM files")
        return [{
            'path': relative_path,
            'type': 'files'
        }] if relative_path else []
    
    # Ask user what to do
    choices = []
    if all_dirs:
        choices = [
            ('Game folders (each subfolder = 1 game)', 'folders'),
            ('Scan deeper (configure subfolders)', 'deeper'),
            ('Skip this folder', 'skip')
        ]
    elif mixed:
        choices = [
            ('ROM files (scan for individual game files)', 'files'),
            ('Game folders (each subfolder = 1 game)', 'folders'),
            ('Scan deeper (configure subfolders)', 'deeper'),
            ('Skip this folder', 'skip')
        ]
    else:
        choices = [
            ('ROM files (scan for individual game files)', 'files'),
            ('Game folders (each subfolder = 1 game)', 'folders'),
            ('Skip this folder', 'skip')
        ]
    
    action = inquirer.prompt([
        inquirer.List(
            'action',
            message=f"[?] How should '{display_path}/' be scanned?",
            choices=choices
        )
    ])
    
    if not action or action['action'] == 'skip':
        print(f"  → Skipped")
        return []
    
    if action['action'] in ['files', 'folders']:
        print(f"  ✓ Will scan for {action['action']}")
        return [{
            'path': relative_path,
            'type': action['action']
        }] if relative_path else []
    
    # action['action'] == 'deeper' - recursively configure subfolders
    print(f"  → Scanning subfolders...")
    
    if not subdirs:
        print("    ⚠ No subdirectories found")
        return []
    
    # Show available subdirs
    print(f"\n  Found {len(subdirs)} subdirectories:")
    for subdir in subdirs:
        print(f"    • {subdir.name}/")
    
    # Let user select which to configure
    subdir_choices = [(f"{sd.name}/", sd.name) for sd in subdirs]
    
    selected = inquirer.prompt([
        inquirer.Checkbox(
            'folders',
            message="  Select folders to SCAN (Space to toggle, Enter to confirm)",
            choices=subdir_choices,
        )
    ])
    
    if not selected or not selected['folders']:
        print("  → No folders selected")
        return []
    
    # Recursively configure each selected subfolder
    all_scan_paths = []
    for folder_name in selected['folders']:
        folder_path = parent_path / folder_name
        new_relative = f"{relative_path}/{folder_name}" if relative_path else folder_name
        
        # Recursive call
        sub_paths = configure_nested_path(folder_path, new_relative, config_data)
        all_scan_paths.extend(sub_paths)
    
    return all_scan_paths


def configure_nested_structure(platform_name: str, platform_path: Path, config_data: Dict) -> Dict:
    """
    Configure a complex platform with nested folder structure.
    Uses recursive descent to handle arbitrary nesting depth.
    """
    print(f"\n{'='*60}")
    print(f"CONFIGURING: {platform_name}")
    print(f"{'='*60}")
    print("\nThis platform has subdirectories. Let's configure which to scan.\n")
    
    # Get subdirectories at the root level
    subdirs = []
    try:
        for item in platform_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                # Skip folders matching ignore patterns
                if should_ignore_folder(item.name, config_data):
                    continue
                subdirs.append(item)
    except Exception as e:
        print(f"ERROR: Could not read directory: {e}")
        return None
    
    if not subdirs:
        print("No subdirectories found!")
        return None
    
    subdirs.sort(key=lambda x: x.name)
    
    # Show available subdirectories
    print(f"Found {len(subdirs)} subdirectories:\n")
    for subdir in subdirs:
        # Preview contents (first 3 items)
        preview_items = []
        try:
            for i, item in enumerate(subdir.iterdir()):
                if i >= 3:
                    break
                if not item.name.startswith('.'):
                    preview_items.append(item.name + ('/' if item.is_dir() else ''))
        except:
            preview_items = ['(unreadable)']
        
        preview = ', '.join(preview_items)
        try:
            total_items = sum(1 for _ in subdir.iterdir())
            if total_items > 3:
                preview += ', ...'
        except:
            pass
        print(f"  • {subdir.name}/")
        print(f"    ({preview})")
    
    # Let user select which subdirectories to configure
    print()
    subdir_choices = [(f"{sd.name}/", sd.name) for sd in subdirs]
    
    selected = inquirer.prompt([
        inquirer.Checkbox(
            'folders',
            message="Select folders to SCAN (Space to toggle, Enter to confirm)",
            choices=subdir_choices,
        )
    ])
    
    if not selected or not selected['folders']:
        print("\n→ No folders selected, skipping platform")
        return None
    
    # Recursively configure each selected subfolder
    scan_paths = []
    for folder_name in selected['folders']:
        folder_path = platform_path / folder_name
        
        # Start recursive configuration from this subfolder
        sub_paths = configure_nested_path(folder_path, folder_name, config_data)
        scan_paths.extend(sub_paths)
    
    if not scan_paths:
        print("\n⚠ No paths configured, skipping platform")
        return None
    
    print(f"\n{'='*60}")
    print(f"CONFIGURATION COMPLETE")
    print(f"{'='*60}")
    print(f"Configured {len(scan_paths)} scan paths:")
    for sp in scan_paths:
        print(f"  • {sp['path']}/  [{sp['type']}]")
    
    # Return nested structure
    return {
        'path': str(platform_path),
        'type': 'nested',
        'scan_paths': scan_paths
    }


def configure_hybrid_structure(platform_name: str, platform_path: Path, config_data: Dict) -> Dict:
    """
    Configure a platform with BOTH root-level files AND subfolders.
    Creates a nested config that scans root files + selected subfolders.
    
    Performance: Only peeks at first 5 items per folder (fast).
    """
    print(f"\n{'='*60}")
    print(f"CONFIGURING HYBRID PLATFORM: {platform_name}")
    print(f"{'='*60}")
    print("\nThis platform has files at the root AND subfolders.")
    print("We'll scan the root files, then ask about each subfolder.\n")
    
    # Always include root level files
    scan_paths = [{
        'path': '',      # Empty string = root level
        'type': 'files'
    }]
    print("[✓] Will scan root-level files")
    
    # Get all subfolders (excluding ignore patterns and hidden)
    subfolders = []
    try:
        for item in platform_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                if should_ignore_folder(item.name, config_data):
                    continue
                subfolders.append(item)
    except Exception as e:
        print(f"ERROR: Could not read directory: {e}")
        return None
    
    if not subfolders:
        print("\n✓ No subfolders to configure")
        return {
            'path': str(platform_path),
            'type': 'nested',
            'scan_paths': scan_paths
        }
    
    subfolders.sort(key=lambda x: x.name)
    print(f"\nFound {len(subfolders)} subfolder(s). Checking each...\n")
    
    # For each subfolder, peek and ask
    for subfolder in subfolders:
        print(f"Checking: {subfolder.name}/")
        
        # Peek at first 5 items (FAST - no full scan)
        peek_items = []
        try:
            for i, item in enumerate(subfolder.iterdir()):
                if i >= 5:
                    break
                if not item.name.startswith('.'):
                    peek_items.append(item)
        except Exception:
            print("  (unreadable, skipping)")
            continue
        
        if not peek_items:
            print("  (empty, skipping)")
            continue
        
        # Classify content: all files? all folders? mixed?
        preview = []
        all_files = True
        all_dirs = True
        
        for item in peek_items:
            if item.is_file():
                preview.append(item.name)
                all_dirs = False
            elif item.is_dir():
                preview.append(item.name + '/')
                all_files = False
        
        more = ', ...' if len(peek_items) >= 5 else ''
        print(f"  Contains: {', '.join(preview)}{more}")
        
        # Auto-detect if all files (like main discovery does)
        if all_files:
            scan_paths.append({
                'path': subfolder.name,
                'type': 'files'
            })
            print(f"  ✓ Auto-detected: Files")
        
        # Ask if all folders (could be game folders or need deeper scan)
        elif all_dirs:
            folder_choice = inquirer.prompt([
                inquirer.List(
                    'action',
                    message=f"What's in {subfolder.name}/?",
                    choices=[
                        ('Game folders (1 folder = 1 game)', 'folders'),
                        ('Skip this subfolder', 'skip')
                    ]
                )
            ])
            
            if folder_choice and folder_choice['action'] == 'folders':
                scan_paths.append({
                    'path': subfolder.name,
                    'type': 'folders'
                })
                print(f"  [✓] Will scan {subfolder.name}/ as game folders")
            else:
                print(f"  → Skipping {subfolder.name}/")
        
        # Ask if mixed content
        else:
            mixed_choice = inquirer.prompt([
                inquirer.List(
                    'action',
                    message=f"Scan {subfolder.name}/ as:",
                    choices=[
                        ('Files (ROM files)', 'files'),
                        ('Folders (game folders)', 'folders'),
                        ('Skip', 'skip')
                    ]
                )
            ])
            
            if mixed_choice and mixed_choice['action'] != 'skip':
                scan_paths.append({
                    'path': subfolder.name,
                    'type': mixed_choice['action']
                })
                print(f"  [✓] Will scan {subfolder.name}/ as {mixed_choice['action']}")
            else:
                print(f"  → Skipping {subfolder.name}/")
    
    # Show final configuration
    print(f"\n{'='*60}")
    print(f"HYBRID CONFIGURATION COMPLETE")
    print(f"{'='*60}")
    print(f"Configured {len(scan_paths)} scan paths:")
    for sp in scan_paths:
        path_display = sp['path'] if sp['path'] else '(root level)'
        print(f"  • {path_display}  [{sp['type']}]")
    
    return {
        'path': str(platform_path),
        'type': 'nested',
        'scan_paths': scan_paths
    }


def discover_structure_interactively(library_roots: List[str], config_data: Dict) -> Dict:
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
                    # Skip folders matching ignore patterns
                    if should_ignore_folder(item.name, config_data):
                        continue
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
                print("  → Scanning subfolders...")
                nested_config = configure_nested_structure(name, path, config_data)
                if nested_config:
                    platform_structure[name] = nested_config
                else:
                    # User cancelled nested config
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
                        ('Both (files + subfolders)', 'both'),
                        ('Skip this platform', 'skip')
                    ]
                )
            ])
            
            if not choice or choice['action'] == 'skip':
                print("  → Skipped")
                continue
            elif choice['action'] == 'both':
                print("  → Configuring hybrid structure...")
                hybrid_config = configure_hybrid_structure(name, path, config_data)
                if hybrid_config:
                    platform_structure[name] = hybrid_config
                else:
                    print("  ⚠ Configuration failed, skipping")
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
            elif ptype == 'nested':
                scan_paths = config.get('scan_paths', [])
                print(f"  {name}: Nested ({len(scan_paths)} paths)")
                for sp in scan_paths:
                    print(f"    • {sp['path']}/  [{sp['type']}]")
        
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
            elif ptype == 'nested':
                scan_paths = config.get('scan_paths', [])
                label = f"{name}: Nested ({len(scan_paths)} paths)"
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
                        ('Hybrid (files + subfolders)', 'hybrid'),
                        ('Nested (configure subfolders)', 'nested'),
                        ('Skip (complex structure)', 'skip')
                    ]
                )
            ])
            
            if choice:
                if choice['action'] == 'nested':
                    nested_config = configure_nested_structure(name, path, config_data)
                    if nested_config:
                        platform_structure[name] = nested_config
                        print(f"  ✓ Configured as nested")
                    else:
                        print(f"  → Configuration cancelled")
                elif choice['action'] == 'hybrid':
                    hybrid_config = configure_hybrid_structure(name, path, config_data)
                    if hybrid_config:
                        platform_structure[name] = hybrid_config
                        print(f"  ✓ Configured as hybrid")
                    else:
                        print(f"  → Configuration cancelled")
                else:
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
        platform_structure = discover_structure_interactively(library_roots, config_data)
        save_platform_structure(config_data, platform_structure)
        print("\n" + "=" * 60)
        print("✓ DISCOVERY COMPLETE")
        print("=" * 60)
        print("\nPlatform structure has been saved to config.yaml")
        print("The fast scanner (audit_library.py) will now be used for scanning.")
    else:
        print(f"\n✓ Using cached platform structure ({len(platform_structure)} platforms)")
        print("Platform structure already configured - nothing to do.")


if __name__ == "__main__":
    main()
