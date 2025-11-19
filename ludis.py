#!/usr/bin/env python3
"""
LUDIS - LaunchBox Universal Data Integration System
====================================================
A unified pipeline for exporting and enriching LaunchBox game library data.

This script orchestrates all data export and processing steps with an
interactive menu system.

Usage:
    python3 ludis.py

Requirements:
    - config.yaml (copy from config.yaml.sample)
    - Python 3.7+
    - pip install pyyaml inquirer tqdm
"""

import sys
import subprocess
import json
import csv
from pathlib import Path
from collections import defaultdict

# Check for required dependencies
try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

try:
    import inquirer
except ImportError:
    print("ERROR: inquirer not installed. Run: pip install inquirer")
    sys.exit(1)

# Import pipeline scripts from scripts/ directory
sys.path.insert(0, str(Path(__file__).parent))
from scripts import export_all_platforms
from scripts import export_all_playlists
from scripts import build_master_inventory
from scripts import enrich_with_playlists
from scripts import audit_library

# ============================================================
# CONSTANTS
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / "config.yaml"
CONFIG_SAMPLE = SCRIPT_DIR / "config.yaml.sample"
VERSION = "1.0.0"

# ============================================================
# CONFIGURATION
# ============================================================

class Config:
    """Configuration manager"""
    
    def __init__(self, config_path: Path):
        self.config_path = config_path
        self.data = {}
        self.load()
    
    def load(self):
        """Load configuration from YAML file"""
        if not self.config_path.exists():
            return
        
        with open(self.config_path, 'r') as f:
            self.data = yaml.safe_load(f)
    
    def get(self, key: str, default=None):
        """Get configuration value using dot notation"""
        keys = key.split('.')
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def get_path(self, key: str) -> Path:
        """Get path configuration value, resolved relative to script directory"""
        value = self.get(key)
        if not value:
            return None
        path = Path(value)
        if not path.is_absolute():
            path = SCRIPT_DIR / path
        return path

# ============================================================
# DEPENDENCY CHECKER
# ============================================================

class DependencyChecker:
    """Check for required files and directories"""
    
    def __init__(self, config: Config):
        self.config = config
        self.results = {}
    
    def check_all(self) -> dict:
        """Check all dependencies and return status dict"""
        self.results = {
            'config': CONFIG_FILE.exists(),
            'launchbox_data': False,
            'platform_xmls': 0,
            'playlist_xmls': 0,
            'nas_inventory': False,
            'all_platforms_csv': False,
            'all_playlists_csv': False,
            'master_inventory_csv': False,
        }
        
        if not self.results['config']:
            return self.results
        
        # Check LaunchBox data directory
        lb_data = self.config.get_path('paths.launchbox_data')
        if lb_data and lb_data.exists():
            self.results['launchbox_data'] = True
            
            platforms_dir = lb_data / "Platforms"
            if platforms_dir.exists():
                self.results['platform_xmls'] = len(list(platforms_dir.glob("*.xml")))
            
            playlists_dir = lb_data / "Playlists"
            if playlists_dir.exists():
                self.results['playlist_xmls'] = len(list(playlists_dir.glob("*.xml")))
        
        # Check for generated CSVs
        output_dir = self.config.get_path('paths.output_directory')
        if output_dir and output_dir.exists():
            self.results['all_platforms_csv'] = (output_dir / "all_platforms.csv").exists()
            self.results['all_playlists_csv'] = (output_dir / "all_playlists.csv").exists()
            self.results['master_inventory_csv'] = (output_dir / "master_inventory.csv").exists()
            
            nas_inv = output_dir / "audits" / "nas_inventory.csv"
            self.results['nas_inventory'] = nas_inv.exists()
        
        return self.results
    
    def print_status(self):
        """Print dependency status to console"""
        print("\n" + "=" * 60)
        print("DEPENDENCY STATUS")
        print("=" * 60)
        
        if self.results['config']:
            print("✓ Configuration file found")
        else:
            print("✗ Configuration file missing (config.yaml)")
            return
        
        if self.results['launchbox_data']:
            print(f"✓ LaunchBox data directory found")
            print(f"  - {self.results['platform_xmls']} platform XMLs")
            print(f"  - {self.results['playlist_xmls']} playlist XMLs")
        else:
            print("✗ LaunchBox data directory not found")
        
        scan_enabled = self.config.get('options.scan_filesystem', True)
        if scan_enabled:
            if self.results['nas_inventory']:
                print("✓ NAS inventory found")
            else:
                print("✗ NAS inventory missing (filesystem scan not yet run)")
        else:
            print("○ Filesystem scanning disabled (metadata-only mode)")
        
        if self.results['all_platforms_csv']:
            print("✓ Platform export found (all_platforms.csv)")
        else:
            print("✗ Platform export missing")
        
        if self.results['all_playlists_csv']:
            print("✓ Playlist export found (all_playlists.csv)")
        else:
            print("✗ Playlist export missing")
        
        if self.results['master_inventory_csv']:
            print("✓ Master inventory found (master_inventory.csv)")
        else:
            print("✗ Master inventory missing")
        
        print("=" * 60)

# ============================================================
# PIPELINE ORCHESTRATOR
# ============================================================

class Pipeline:
    """Orchestrates all pipeline steps"""
    
    def __init__(self, config: Config):
        self.config = config
    
    def run_filesystem_scan(self) -> bool:
        """Run filesystem scan to build NAS inventory"""
        print("\n" + "=" * 60)
        print("STEP: Filesystem Scan")
        print("=" * 60)
        
        try:
            # Call audit_library nas-inventory command
            result = subprocess.run(
                [sys.executable, "scripts/audit_library.py", "nas-inventory"],
                cwd=SCRIPT_DIR,
                capture_output=False,
                text=True
            )
            return result.returncode == 0
        except Exception as e:
            print(f"ERROR: {e}")
            return False
    
    def run_platform_export(self) -> bool:
        """Export LaunchBox platform data"""
        print("\n" + "=" * 60)
        print("STEP: Platform Export")
        print("=" * 60)
        
        try:
            export_all_platforms.main()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False
    
    def run_playlist_export(self) -> bool:
        """Export LaunchBox playlist data"""
        print("\n" + "=" * 60)
        print("STEP: Playlist Export")
        print("=" * 60)
        
        try:
            export_all_playlists.main()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False
    
    def run_master_inventory(self) -> bool:
        """Build master inventory"""
        print("\n" + "=" * 60)
        print("STEP: Build Master Inventory")
        print("=" * 60)
        
        try:
            build_master_inventory.main()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False
    
    def run_playlist_enrichment(self) -> bool:
        """Enrich master inventory with playlist data"""
        print("\n" + "=" * 60)
        print("STEP: Enrich with Playlist Data")
        print("=" * 60)
        
        try:
            enrich_with_playlists.main()
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False
    
    def run_full_pipeline(self) -> bool:
        """Run all pipeline steps in sequence"""
        print("\n" + "=" * 60)
        print("RUNNING FULL PIPELINE")
        print("=" * 60)
        
        steps = [
            ("Filesystem Scan", self.run_filesystem_scan, self.config.get('options.scan_filesystem', True)),
            ("Platform Export", self.run_platform_export, True),
            ("Playlist Export", self.run_playlist_export, True),
            ("Master Inventory", self.run_master_inventory, True),
            ("Playlist Enrichment", self.run_playlist_enrichment, True),
        ]
        
        for step_name, step_func, enabled in steps:
            if not enabled:
                print(f"\n○ Skipping: {step_name} (disabled in config)")
                continue
            
            if not step_func():
                print(f"\n✗ FAILED: {step_name}")
                return False
        
        print("\n" + "=" * 60)
        print("✓ PIPELINE COMPLETE!")
        print("=" * 60)
        return True
    
    def extract_manual_selections(self, include_only=False, exclude_only=False) -> bool:
        """Extract manual include/exclude selections from master inventory to JSON files"""
        output_dir = self.config.get_path('paths.output_directory')
        master_csv = output_dir / "master_inventory.csv"
        
        if not master_csv.exists():
            print(f"ERROR: Master inventory not found: {master_csv}")
            return False
        
        # Determine what to extract
        if include_only:
            print("\n" + "=" * 60)
            print("EXTRACTING MANUAL INCLUDES")
            print("=" * 60)
            extract_types = ["include"]
        elif exclude_only:
            print("\n" + "=" * 60)
            print("EXTRACTING MANUAL EXCLUDES")
            print("=" * 60)
            extract_types = ["exclude"]
        else:
            print("\n" + "=" * 60)
            print("EXTRACTING MANUAL SELECTIONS (INCLUDES + EXCLUDES)")
            print("=" * 60)
            extract_types = ["include", "exclude"]
        
        # Read master inventory and organize by platform
        includes_by_platform = defaultdict(list)
        excludes_by_platform = defaultdict(list)
        
        with open(master_csv, 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                platform = row.get('Platform', '').strip()
                game_id = row.get('LBID', '').strip()
                manual_include = row.get('ManualInclude', '').strip().lower()
                manual_exclude = row.get('ManualExclude', '').strip().lower()
                
                if not platform or not game_id:
                    continue
                
                # Check for manual includes
                if "include" in extract_types and manual_include == 'true':
                    includes_by_platform[platform].append(game_id)
                
                # Check for manual excludes
                if "exclude" in extract_types and manual_exclude == 'true':
                    excludes_by_platform[platform].append(game_id)
        
        # Write JSON files to project root
        files_written = []
        
        if "include" in extract_types:
            include_file = SCRIPT_DIR / "config.includes.json"
            with open(include_file, 'w', encoding='utf-8') as f:
                json.dump(dict(includes_by_platform), f, indent=2, sort_keys=True)
            
            total_includes = sum(len(ids) for ids in includes_by_platform.values())
            print(f"\n✓ Extracted {total_includes} manual includes across {len(includes_by_platform)} platforms")
            print(f"  Saved to: {include_file}")
            files_written.append(include_file)
        
        if "exclude" in extract_types:
            exclude_file = SCRIPT_DIR / "config.excludes.json"
            with open(exclude_file, 'w', encoding='utf-8') as f:
                json.dump(dict(excludes_by_platform), f, indent=2, sort_keys=True)
            
            total_excludes = sum(len(ids) for ids in excludes_by_platform.values())
            print(f"\n✓ Extracted {total_excludes} manual excludes across {len(excludes_by_platform)} platforms")
            print(f"  Saved to: {exclude_file}")
            files_written.append(exclude_file)
        
        if files_written:
            print("\n" + "=" * 60)
            print("✓ EXTRACTION COMPLETE!")
            print("=" * 60)
            return True
        else:
            print("\n⚠ No manual selections found to extract")
            return True
    
    def dropin_manual_selections(self, include_only=False, exclude_only=False) -> bool:
        """Apply manual selections from JSON files to master inventory"""
        output_dir = self.config.get_path('paths.output_directory')
        master_csv = output_dir / "master_inventory.csv"
        
        if not master_csv.exists():
            print(f"ERROR: Master inventory not found: {master_csv}")
            return False
        
        # Determine what to apply
        if include_only:
            print("\n" + "=" * 60)
            print("APPLYING MANUAL INCLUDES")
            print("=" * 60)
            apply_types = ["include"]
        elif exclude_only:
            print("\n" + "=" * 60)
            print("APPLYING MANUAL EXCLUDES")
            print("=" * 60)
            apply_types = ["exclude"]
        else:
            print("\n" + "=" * 60)
            print("APPLYING MANUAL SELECTIONS (INCLUDES + EXCLUDES)")
            print("=" * 60)
            apply_types = ["include", "exclude"]
        
        # Load JSON files from project root
        include_ids = set()
        exclude_ids = set()
        
        if "include" in apply_types:
            include_file = SCRIPT_DIR / "config.includes.json"
            if include_file.exists():
                with open(include_file, 'r', encoding='utf-8') as f:
                    includes_by_platform = json.load(f)
                    for platform, ids in includes_by_platform.items():
                        include_ids.update(ids)
                print(f"✓ Loaded {len(include_ids)} manual includes from {include_file}")
            else:
                print(f"⚠ No manual includes file found: {include_file}")
        
        if "exclude" in apply_types:
            exclude_file = SCRIPT_DIR / "config.excludes.json"
            if exclude_file.exists():
                with open(exclude_file, 'r', encoding='utf-8') as f:
                    excludes_by_platform = json.load(f)
                    for platform, ids in excludes_by_platform.items():
                        exclude_ids.update(ids)
                print(f"✓ Loaded {len(exclude_ids)} manual excludes from {exclude_file}")
            else:
                print(f"⚠ No manual excludes file found: {exclude_file}")
        
        if not include_ids and not exclude_ids:
            print("\n⚠ No manual selections to apply")
            return False
        
        # Read master inventory, update rows, and write back
        print("\nUpdating master inventory...")
        rows = []
        updated_includes = 0
        updated_excludes = 0
        
        with open(master_csv, 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            
            for row in reader:
                game_id = row.get('LBID', '').strip()
                
                # Apply manual include
                if "include" in apply_types and game_id in include_ids:
                    if row.get('ManualInclude', '').strip().lower() != 'true':
                        row['ManualInclude'] = 'true'
                        updated_includes += 1
                
                # Apply manual exclude
                if "exclude" in apply_types and game_id in exclude_ids:
                    if row.get('ManualExclude', '').strip().lower() != 'true':
                        row['ManualExclude'] = 'true'
                        updated_excludes += 1
                
                rows.append(row)
        
        # Write updated CSV
        with open(master_csv, 'w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"\n✓ Updated master inventory:")
        if "include" in apply_types:
            print(f"  - {updated_includes} games marked as ManualInclude")
        if "exclude" in apply_types:
            print(f"  - {updated_excludes} games marked as ManualExclude")
        
        print("\n" + "=" * 60)
        print("✓ DROP-IN COMPLETE!")
        print("=" * 60)
        return True

# ============================================================
# INTERACTIVE MENU
# ============================================================

def show_welcome():
    """Display welcome banner"""
    print("\n" + "=" * 60)
    print(f"LUDIS v{VERSION}")
    print("LaunchBox Universal Data Integration System")
    print("=" * 60)

def create_config_interactively() -> bool:
    """Interactively create config.yaml on first run"""
    import os
    import platform
    
    print("\n" + "=" * 60)
    print("WELCOME TO LUDIS!")
    print("=" * 60)
    print("\nLudis is a platform-agnostic ROM library migration tool used to")
    print("assist you with migrating a monolithic Windows LaunchBox library to")
    print("smaller, more curated formats.")
    print("\nThis means Ludis can run:")
    print("  • On Windows where LaunchBox is installed")
    print("  • On macOS/Linux where your NAS is mounted")
    print("  • On a remote server with access to your files")
    print("  • Anywhere with access to your LaunchBox XML data")
    print("\nI'll ask you a few questions to understand YOUR setup:")
    print("  1. Where are your LaunchBox XML files?")
    print("  2. Where did LaunchBox THINK your games were located?")
    print("  3. Where are your games ACTUALLY located on THIS machine?")
    print("  4. What platforms do you want to export to?")
    print("\nLet's begin!")
    print("\n(You can always edit config.yaml later)")
    
    # Load defaults from sample config if it exists
    defaults = {
        'launchbox_data': 'Data/',
        'windows_root': '',
        'local_root': '',
        'scan_filesystem': True
    }
    
    if CONFIG_SAMPLE.exists():
        try:
            with open(CONFIG_SAMPLE, 'r') as f:
                sample_config = yaml.safe_load(f)
                if sample_config:
                    defaults['launchbox_data'] = sample_config.get('paths', {}).get('launchbox_data', 'Data/')
                    defaults['windows_root'] = sample_config.get('paths', {}).get('windows_root', '')
                    defaults['local_root'] = sample_config.get('paths', {}).get('local_root', '')
                    defaults['scan_filesystem'] = sample_config.get('options', {}).get('scan_filesystem', True)
        except:
            pass  # If sample config can't be loaded, use hardcoded defaults
    
    print("\n" + "-" * 60)
    print("STEP 1: LaunchBox XML Data")
    print("-" * 60)
    print("Where is your LaunchBox Data directory?")
    print("This contains the Platforms/ and Playlists/ folders with XML files.")
    print("\n  Examples:")
    print("    • Data/                    (if running from Ludis)")
    print("    • /path/to/LaunchBox/Data/ (if running elsewhere)")
    
    print(f"\n  [default: {defaults['launchbox_data']}]")
    lb_data = input("  Path: ").strip() or defaults['launchbox_data']
    
    # Validate LaunchBox directory
    lb_path = Path(lb_data)
    if not lb_path.is_absolute():
        lb_path = SCRIPT_DIR / lb_path
    
    if not lb_path.exists():
        print(f"\n⚠ WARNING: Directory not found: {lb_path}")
        confirm = input("Continue anyway? (y/n): ").lower()
        if confirm != 'y':
            return False
    
    print("\n" + "-" * 60)
    print("STEP 2: LaunchBox Installation Context")
    print("-" * 60)
    print("What path does LaunchBox use in its XML files for game ROMs?")
    print("\nLaunchBox stores paths IN the XML as they were on the Windows")
    print("machine where LaunchBox is installed.")
    print("\n  Example: Z:\\media\\games\\library")
    print("  (This is what's IN the XML, even if you're running on Mac/Linux)")
    
    if defaults['windows_root']:
        print(f"\n  [default: {defaults['windows_root']}]")
        windows_root = input("  Path: ").strip() or defaults['windows_root']
    else:
        windows_root = input("\n  Path: ").strip()
    
    if not windows_root:
        print("\n  ERROR: LaunchBox installation path is required")
        return False
    
    print("\n" + "-" * 60)
    print("STEP 3: Actual Game Location (THIS Machine)")
    print("-" * 60)
    print("Where are your game files ACTUALLY located relative to THIS machine running Ludis?")
    print("\nThis is where the files physically exist right now, which might be")
    print("different from what LaunchBox thinks.")
    print("\n  Examples:")
    print("    • /Volumes/NAS/media/games/library  (macOS with NAS mounted)")
    print("    • /mnt/nas/media/games/library      (Linux with NAS mounted)")
    print("    • C:\\Program Files\\LaunchBox\\Games  (Windows, same as LaunchBox)")
    print(f"\n  Detected OS: {platform.system()}")
    
    if defaults['local_root']:
        print(f"\n  [default: {defaults['local_root']}]")
        local_root = input("  Path: ").strip() or defaults['local_root']
    else:
        local_root = input("\n  Path: ").strip()
    
    # Validate local root if filesystem scanning is enabled
    if local_root:
        local_path = Path(local_root)
        if local_path.exists():
            print(f"\n  ✓ Directory found: {local_path}")
        else:
            print(f"\n  ⚠ WARNING: Directory not found: {local_path}")
            print("  (You can still use Ludis for metadata-only exports)")
    
    print("\n" + "-" * 60)
    print("STEP 4: Export Targets")
    print("-" * 60)
    print("What platforms do you want to export game libraries to?")
    print("\nCurrently supported:")
    print("  • ES-DE (EmulationStation Desktop Edition)")
    print("    For Steam Deck, Retro handhelds, etc.")
    print("\nFuture support:")
    print("  • RetroPie")
    print("  • Batocera")
    
    print("\n  [default: Y]")
    enable_esde_choice = input("  Enable ES-DE export? (Y/n): ").lower().strip() or 'y'
    enable_esde = enable_esde_choice == 'y'
    
    target_name = 'steam_deck'  # Default name
    if enable_esde:
        print("\nWhat would you like to name this export target?")
        print("  Common names: steam_deck, retroid_pocket, anbernic, etc.")
        print("\n  [default: steam_deck]")
        target_name = input("  Target name: ").strip() or 'steam_deck'
    
    print("\n" + "-" * 60)
    print("STEP 5: Filesystem Scanning")
    print("-" * 60)
    print("Do you want to scan your filesystem to match files with")
    print("LaunchBox entries?")
    print("\n  Yes: Required for file size calculations and file existence validation")
    print("  No:  Metadata-only mode (faster, but no file verification)")
    
    default_scan = 'Y' if defaults['scan_filesystem'] else 'n'
    print(f"\n  [default: {default_scan}]")
    scan_choice = input("  Enable filesystem scanning? (Y/n): ").lower().strip() or default_scan.lower()
    scan_filesystem = scan_choice == 'y'
    
    # Create config dictionary
    config_data = {
        'version': '1.0',
        'paths': {
            'launchbox_data': lb_data,
            'output_directory': 'LB_Exports/',
            'windows_root': windows_root,
            'local_root': local_root,
        },
        'options': {
            'scan_filesystem': scan_filesystem,
            'verbose': False,
            'show_progress': True,
        },
        'export_targets': {}
    }
    
    # Add export target if ES-DE is enabled
    if enable_esde:
        config_data['export_targets'][target_name] = {
            'enabled': True,
            'format': 'esde',
            'storage_locations': {
                'internal_ssd': {
                    'path': '',
                    'label': 'Internal SSD'
                },
                'sd_card': {
                    'path': '',
                    'label': 'SD Card'
                }
            },
            'defaults': {
                'operation': 'copy',
                'filters': {
                    'include_platform_best': False,
                    'include_all_time_favorites': False,
                    'include_favorites': False,
                    'include_backlog': False,
                    'include_goty_winner': False,
                    'include_goty_nominee': False,
                    'include_on_deck': False,
                    'include_retro': False,
                    'include_classic_titles': False,
                    'include_franchises': False,
                    'force_manual_include': True,
                    'force_manual_exclude': True,
                    'custom_fields': []
                }
            }
        }
    
    # Write config file
    print("\n" + "=" * 60)
    print("CONFIGURATION SUMMARY")
    print("=" * 60)
    print(f"\n  LaunchBox XML Data:   {lb_data}")
    print(f"  LaunchBox Path (XML): {windows_root}")
    print(f"  Actual Files (Ludis): {local_root}")
    print(f"  Filesystem Scanning:  {'Enabled' if scan_filesystem else 'Disabled'}")
    if enable_esde:
        print(f"  Export Targets:       ES-DE (target: {target_name})")
    else:
        print(f"  Export Targets:       None (can add later in config.yaml)")
    
    print("\n" + "-" * 60)
    print("Creating config.yaml...")
    print("-" * 60)
    
    with open(CONFIG_FILE, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n  ✓ Created {CONFIG_FILE}")
    print("\n  Configuration saved! You can edit this file anytime.")
    print(f"  Sample config is available at: {CONFIG_SAMPLE}")
    
    return True

def show_menu(config: Config, deps: dict) -> str:
    """Show interactive menu and return user choice"""
    
    # Check if master inventory exists (pipeline has been run)
    pipeline_complete = deps['master_inventory_csv']
    
    choices = []
    
    if not pipeline_complete:
        # INITIAL MENU: Before pipeline has been run
        choices.append("Build Ludis Library (run all steps)")
        choices.append("Re-run YAML Setup (reconfigure)")
        choices.append("Exit")
    else:
        # ADVANCED MENU: After pipeline is complete
        choices.append("Re-run filesystem scan (will force a rebuild of everything)")
        choices.append("Re-build master inventory")
        choices.append("Extract Manual Selections")
        choices.append("Drop-in Manual Selections")
        
        # Check if platform storage defaults are configured for any enabled export target
        storage_configured = False
        export_targets = config.get('export_targets', {})
        for target_name, target_config in export_targets.items():
            if target_config.get('enabled') and 'platform_storage_defaults' in target_config:
                storage_configured = True
                break
        
        choices.append("---")  # Visual separator
        
        if storage_configured:
            choices.append("Reconfigure Platform Storage Defaults")
            choices.append("Create Migration Script")
        else:
            choices.append("Configure Platform Storage Defaults")
            # Hide "Create Migration Script" until defaults are configured
        
        choices.append("---")  # Visual separator
        choices.append("Validate Existing Data")
        choices.append("Re-run YAML Setup (reconfigure)")
        choices.append("Exit")
    
    # Show menu
    questions = [
        inquirer.List('action',
                     message="What would you like to do?",
                     choices=choices,
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    return answers['action'] if answers else "Exit"

def run_pipeline_from_step(pipeline: 'Pipeline', start_step: str, config: Config) -> bool:
    """Run pipeline starting from a specific step (hierarchical execution)"""
    steps_order = ['scan', 'platforms', 'playlists', 'inventory', 'enrich']
    
    # Find starting index
    try:
        start_idx = steps_order.index(start_step)
    except ValueError:
        print(f"ERROR: Unknown step '{start_step}'")
        return False
    
    # Run from start_step to end
    steps_to_run = steps_order[start_idx:]
    
    step_functions = {
        'scan': (pipeline.run_filesystem_scan, config.get('options.scan_filesystem', True)),
        'platforms': (pipeline.run_platform_export, True),
        'playlists': (pipeline.run_playlist_export, True),
        'inventory': (pipeline.run_master_inventory, True),
        'enrich': (pipeline.run_playlist_enrichment, True),
    }
    
    print("\n" + "=" * 60)
    print(f"RUNNING PIPELINE FROM: {start_step.upper()}")
    print("=" * 60)
    print(f"Steps to execute: {' → '.join(steps_to_run)}")
    print("=" * 60)
    
    for step in steps_to_run:
        func, enabled = step_functions[step]
        if not enabled:
            print(f"\n○ Skipping: {step} (disabled in config)")
            continue
        
        if not func():
            print(f"\n✗ FAILED at step: {step}")
            return False
    
    print("\n" + "=" * 60)
    print("✓ PIPELINE COMPLETE!")
    print("=" * 60)
    return True

# ============================================================
# MAIN
# ============================================================

def main():
    """Main application entry point"""
    show_welcome()
    
    # Check for config file - create interactively if missing
    if not CONFIG_FILE.exists():
        if not create_config_interactively():
            print("\nSetup cancelled. Run ludis.py again when ready.")
            sys.exit(0)
        print("\n" + "=" * 60)
        print("Setup complete! Continuing with Ludis...")
        print("=" * 60)
    
    # Load configuration
    print("\nLoading configuration...")
    config = Config(CONFIG_FILE)
    
    # Check dependencies
    print("Checking dependencies...")
    checker = DependencyChecker(config)
    deps = checker.check_all()
    checker.print_status()
    
    # Create pipeline
    pipeline = Pipeline(config)
    
    # Show menu
    while True:
        action = show_menu(config, deps)
        
        if action == "Exit":
            print("\nGoodbye!")
            break
        
        # Simple menu options (initial or reconfigure)
        elif action == "Build Ludis Library (run all steps)":
            confirm = inquirer.confirm("This will run the complete pipeline. Continue?", default=True)
            if confirm:
                pipeline.run_full_pipeline()
                deps = checker.check_all()
        
        elif action == "Re-run filesystem scan (will force a rebuild of everything)":
            confirm = inquirer.confirm("This will rebuild all data from scratch. Continue?", default=True)
            if confirm:
                pipeline.run_full_pipeline()
                deps = checker.check_all()
        
        elif action == "Re-build master inventory":
            confirm = inquirer.confirm("Run: inventory → enrichment?", default=True)
            if confirm:
                run_pipeline_from_step(pipeline, 'inventory', config)
                deps = checker.check_all()
        
        elif action == "Re-run YAML Setup (reconfigure)":
            confirm = inquirer.confirm("This will delete config.yaml and restart setup. Continue?", default=False)
            if confirm:
                CONFIG_FILE.unlink()
                print("\nDeleted config.yaml. Restarting setup...\n")
                if not create_config_interactively():
                    print("\nSetup cancelled.")
                    break
                # Reload config
                config = Config(CONFIG_FILE)
                deps = checker.check_all()
                checker.print_status()
        
        elif action == "Extract Manual Selections":
            confirm = inquirer.confirm("Extract includes and excludes to JSON files?", default=True)
            if confirm:
                pipeline.extract_manual_selections()
        
        elif action == "Drop-in Manual Selections":
            confirm = inquirer.confirm("Apply includes and excludes from JSON files?", default=True)
            if confirm:
                pipeline.dropin_manual_selections()
        
        elif action in ("Configure Platform Storage Defaults", "Reconfigure Platform Storage Defaults"):
            # Run the platform storage defaults configuration
            from scripts import migration_builder
            migration_builder.configure_storage_defaults(config)
        
        elif action == "Create Migration Script":
            # Run the migration script builder
            from scripts import migration_builder
            migration_builder.run_interactive(config)
        
        elif action == "Validate Existing Data":
            deps = checker.check_all()
            checker.print_status()
        
        elif action == "---":
            # Visual separator - do nothing
            continue
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

