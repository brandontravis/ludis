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
        selections_dir = output_dir / "manual_selections"
        
        if not master_csv.exists():
            print(f"ERROR: Master inventory not found: {master_csv}")
            return False
        
        selections_dir.mkdir(parents=True, exist_ok=True)
        
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
                game_id = row.get('ID', '').strip()
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
        
        # Write JSON files
        files_written = []
        
        if "include" in extract_types:
            include_file = selections_dir / "manual_includes.json"
            with open(include_file, 'w', encoding='utf-8') as f:
                json.dump(dict(includes_by_platform), f, indent=2, sort_keys=True)
            
            total_includes = sum(len(ids) for ids in includes_by_platform.values())
            print(f"\n✓ Extracted {total_includes} manual includes across {len(includes_by_platform)} platforms")
            print(f"  Saved to: {include_file}")
            files_written.append(include_file)
        
        if "exclude" in extract_types:
            exclude_file = selections_dir / "manual_excludes.json"
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
        selections_dir = output_dir / "manual_selections"
        
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
        
        # Load JSON files
        include_ids = set()
        exclude_ids = set()
        
        if "include" in apply_types:
            include_file = selections_dir / "manual_includes.json"
            if include_file.exists():
                with open(include_file, 'r', encoding='utf-8') as f:
                    includes_by_platform = json.load(f)
                    for platform, ids in includes_by_platform.items():
                        include_ids.update(ids)
                print(f"✓ Loaded {len(include_ids)} manual includes from {include_file}")
            else:
                print(f"⚠ No manual includes file found: {include_file}")
        
        if "exclude" in apply_types:
            exclude_file = selections_dir / "manual_excludes.json"
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
                game_id = row.get('ID', '').strip()
                
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
    print("FIRST RUN SETUP")
    print("=" * 60)
    print("\nNo configuration file found. Let's create one!")
    print("\nI'll ask you a few questions to set up your environment.")
    print("(You can always edit config.yaml later)")
    
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
    
    # Ask if user wants to use defaults or start blank
    print("\n" + "-" * 60)
    print("CONFIGURATION MODE")
    print("-" * 60)
    
    if defaults['windows_root'] and defaults['local_root']:
        print("I found default values in config.yaml.sample.")
        print("\nDefault paths:")
        print(f"  LaunchBox Data: {defaults['launchbox_data']}")
        print(f"  Windows Root:   {defaults['windows_root']}")
        print(f"  Local Root:     {defaults['local_root']}")
        print("\nWould you like to:")
        print("  1. Use these defaults (you can edit each one)")
        print("  2. Start with blank values")
        
        choice = input("\nChoice (1/2) [default: 1]: ").strip() or "1"
        use_defaults = choice == "1"
    else:
        use_defaults = False
        print("No defaults found. Starting with blank values.")
    
    # If not using defaults, clear them
    if not use_defaults:
        defaults['launchbox_data'] = 'Data/'  # Keep this default
        defaults['windows_root'] = ''
        defaults['local_root'] = ''
    
    print("\n" + "-" * 60)
    print("STEP 1: LaunchBox Data Directory")
    print("-" * 60)
    print("Where is your LaunchBox Data directory?")
    print("(This contains Platforms/ and Playlists/ folders)")
    if use_defaults:
        print(f"\n→ Press ENTER to use default: {defaults['launchbox_data']}")
        print("  Or type a new path to override")
    
    lb_data = input(f"\nPath: ").strip() or defaults['launchbox_data']
    
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
    print("STEP 2: Windows Root Path")
    print("-" * 60)
    print("What path does LaunchBox use in its XML files?")
    print("(This is usually a Windows path like Z:\\media\\games\\library)")
    
    if use_defaults and defaults['windows_root']:
        print(f"\n→ Press ENTER to use default: {defaults['windows_root']}")
        print("  Or type a new path to override")
        windows_root = input(f"\nPath: ").strip() or defaults['windows_root']
    else:
        windows_root = input(f"\nPath: ").strip()
    
    if not windows_root:
        print("ERROR: Windows root path is required")
        return False
    
    print("\n" + "-" * 60)
    print("STEP 3: Local Filesystem Path")
    print("-" * 60)
    print("Where are your game files actually located on THIS system?")
    print(f"Detected OS: {platform.system()}")
    
    if use_defaults and defaults['local_root']:
        print(f"\n→ Press ENTER to use default: {defaults['local_root']}")
        print("  Or type a new path to override")
        local_root = input(f"\nPath: ").strip() or defaults['local_root']
    else:
        local_root = input(f"\nPath: ").strip()
    
    # Validate local root if filesystem scanning is enabled
    local_path = Path(local_root)
    if local_path.exists():
        print(f"✓ Directory found: {local_path}")
    else:
        print(f"⚠ WARNING: Directory not found: {local_path}")
        print("(You can still use Ludis for metadata-only exports)")
    
    print("\n" + "-" * 60)
    print("STEP 4: Filesystem Scanning")
    print("-" * 60)
    print("Do you want to scan your filesystem to match files with LaunchBox entries?")
    print("(Required for file matching, but can be skipped for metadata-only exports)")
    
    default_scan = 'y' if defaults['scan_filesystem'] else 'n'
    if use_defaults:
        print(f"\n→ Press ENTER to use default: {'Yes' if default_scan == 'y' else 'No'}")
        print("  Or type 'y' or 'n' to override")
    
    scan_choice = input(f"\nEnable? (y/n): ").lower().strip() or default_scan
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
        'export_targets': {
            'steam_deck': {
                'enabled': False,
                'path': '',
                'format': 'esde',
            }
        }
    }
    
    # Write config file
    print("\n" + "-" * 60)
    print("Creating config.yaml...")
    print("-" * 60)
    
    with open(CONFIG_FILE, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    print(f"✓ Created {CONFIG_FILE}")
    print("\nConfiguration saved! You can edit this file anytime.")
    print(f"Sample config is available at: {CONFIG_SAMPLE}")
    
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
        # ADVANCED MENU: After pipeline is complete, show hierarchical rebuild options
        choices.append("Rebuild Everything (all steps)")
        choices.append("---")  # Visual separator
        
        # Hierarchical options - each forces subsequent steps
        choices.append("Re-run from: Filesystem Scan (→ platforms → playlists → inventory → enrichment)")
        choices.append("Re-run from: Platform Export (→ playlists → inventory → enrichment)")
        choices.append("Re-run from: Playlist Export (→ inventory → enrichment)")
        choices.append("Re-run from: Master Inventory (→ enrichment)")
        choices.append("Re-run from: Playlist Enrichment (final step only)")
        
        choices.append("---")  # Visual separator
        
        # Manual selection management
        choices.append("Extract Manual Selections")
        choices.append("Extract Manual Includes")
        choices.append("Extract Manual Excludes")
        
        choices.append("---")  # Visual separator
        
        choices.append("Drop-in Manual Selections")
        choices.append("Drop-in Manual Includes")
        choices.append("Drop-in Manual Excludes")
        
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
        
        elif action == "Rebuild Everything (all steps)":
            confirm = inquirer.confirm("This will rebuild all data from scratch. Continue?", default=True)
            if confirm:
                pipeline.run_full_pipeline()
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
        
        # Hierarchical rebuild options
        elif "Re-run from: Filesystem Scan" in action:
            confirm = inquirer.confirm("Run: scan → platforms → playlists → inventory → enrichment?", default=True)
            if confirm:
                run_pipeline_from_step(pipeline, 'scan', config)
                deps = checker.check_all()
        
        elif "Re-run from: Platform Export" in action:
            confirm = inquirer.confirm("Run: platforms → playlists → inventory → enrichment?", default=True)
            if confirm:
                run_pipeline_from_step(pipeline, 'platforms', config)
                deps = checker.check_all()
        
        elif "Re-run from: Playlist Export" in action:
            confirm = inquirer.confirm("Run: playlists → inventory → enrichment?", default=True)
            if confirm:
                run_pipeline_from_step(pipeline, 'playlists', config)
                deps = checker.check_all()
        
        elif "Re-run from: Master Inventory" in action:
            confirm = inquirer.confirm("Run: inventory → enrichment?", default=True)
            if confirm:
                run_pipeline_from_step(pipeline, 'inventory', config)
                deps = checker.check_all()
        
        elif "Re-run from: Playlist Enrichment" in action:
            confirm = inquirer.confirm("Run: enrichment only?", default=True)
            if confirm:
                run_pipeline_from_step(pipeline, 'enrich', config)
                deps = checker.check_all()
        
        elif action == "Extract Manual Selections":
            confirm = inquirer.confirm("Extract both includes and excludes to JSON files?", default=True)
            if confirm:
                pipeline.extract_manual_selections()
        
        elif action == "Extract Manual Includes":
            confirm = inquirer.confirm("Extract manual includes to JSON file?", default=True)
            if confirm:
                pipeline.extract_manual_selections(include_only=True)
        
        elif action == "Extract Manual Excludes":
            confirm = inquirer.confirm("Extract manual excludes to JSON file?", default=True)
            if confirm:
                pipeline.extract_manual_selections(exclude_only=True)
        
        elif action == "Drop-in Manual Selections":
            confirm = inquirer.confirm("Apply both includes and excludes from JSON files?", default=True)
            if confirm:
                pipeline.dropin_manual_selections()
        
        elif action == "Drop-in Manual Includes":
            confirm = inquirer.confirm("Apply manual includes from JSON file?", default=True)
            if confirm:
                pipeline.dropin_manual_selections(include_only=True)
        
        elif action == "Drop-in Manual Excludes":
            confirm = inquirer.confirm("Apply manual excludes from JSON file?", default=True)
            if confirm:
                pipeline.dropin_manual_selections(exclude_only=True)
        
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

