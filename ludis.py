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
import logging
from datetime import datetime
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
# audit_library_v2.py is called via subprocess, not imported

# ============================================================
# CONSTANTS
# ============================================================
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / "config.yaml"
CONFIG_SAMPLE = SCRIPT_DIR / "config.yaml.sample"
VERSION = "1.0.0"

# ============================================================
# LOGGING
# ============================================================

def setup_logging(config):
    """
    Configure logging to both file and console.
    
    Args:
        config: Config object (not used, but kept for future)
    """
    # Logs go in project root, NOT in output directory
    log_dir = SCRIPT_DIR / 'logs'
    
    # Create logs directory
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate log filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"ludis_{timestamp}.log"
    
    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers (in case of reconfiguration)
    logger.handlers.clear()
    
    # File handler - captures everything
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    # Console handler - only INFO and above (not DEBUG)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # Log startup
    logging.info(f"Ludis started - logging to: {log_file}")
    
    return log_file


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
        logging.info("Starting: Filesystem Scan")
        print("\n" + "=" * 60)
        print("STEP: Filesystem Scan")
        print("=" * 60)
        
        try:
            # Check if platform_structure is configured
            if not self.config.get('platform_structure'):
                logging.warning("Platform structure not configured")
                print("\n✗ Platform structure not configured yet")
                print("\nPlease run 'Configure Platform Structure' first,")
                print("or I can do it now.")
                
                run_now = inquirer.confirm("\nRun platform discovery now?", default=True)
                if not run_now:
                    logging.info("Filesystem scan skipped - user declined platform discovery")
                    print("\nSkipped. Configure platform structure from the menu first.")
                    return False
                
                result = subprocess.run(
                    [sys.executable, "scripts/interactive_scanner.py"],
                    cwd=SCRIPT_DIR,
                    capture_output=False,
                    text=True
                )
                if result.returncode != 0:
                    print("\n✗ Platform discovery failed or was cancelled")
                    return False
                
                # Reload config to get new platform_structure
                self.config.load()
                print("\n✓ Platform structure configured!")
            
            # Use the FAST scanner from audit_library.py
            logging.info("Running filesystem scanner...")
            result = subprocess.run(
                [sys.executable, "scripts/audit_library.py", "nas-inventory"],
                cwd=SCRIPT_DIR,
                capture_output=False,
                text=True
            )
            if result.returncode == 0:
                logging.info("Filesystem scan completed successfully")
                return True
            else:
                logging.error("Filesystem scan failed")
                return False
        except Exception as e:
            logging.error(f"Filesystem scan error: {e}")
            print(f"ERROR: {e}")
            return False
    
    def run_platform_export(self) -> bool:
        """Export LaunchBox platform data"""
        logging.info("Starting: Platform Export")
        print("\n" + "=" * 60)
        print("STEP: Platform Export")
        print("=" * 60)
        
        try:
            export_all_platforms.main()
            logging.info("Platform export completed successfully")
            return True
        except Exception as e:
            logging.error(f"Platform export error: {e}")
            print(f"ERROR: {e}")
            return False
    
    def run_playlist_export(self) -> bool:
        """Export LaunchBox playlist data"""
        logging.info("Starting: Playlist Export")
        print("\n" + "=" * 60)
        print("STEP: Playlist Export")
        print("=" * 60)
        
        try:
            export_all_playlists.main()
            logging.info("Playlist export completed successfully")
            return True
        except Exception as e:
            logging.error(f"Playlist export error: {e}")
            print(f"ERROR: {e}")
            return False
    
    def run_master_inventory(self) -> bool:
        """Build master inventory"""
        logging.info("Starting: Build Master Inventory")
        print("\n" + "=" * 60)
        print("STEP: Build Master Inventory")
        print("=" * 60)
        
        try:
            build_master_inventory.main()
            logging.info("Master inventory completed successfully")
            return True
        except Exception as e:
            logging.error(f"Master inventory error: {e}")
            print(f"ERROR: {e}")
            return False
    
    def run_playlist_enrichment(self) -> bool:
        """Enrich master inventory with playlist data"""
        logging.info("Starting: Enrich with Playlist Data")
        print("\n" + "=" * 60)
        print("STEP: Enrich with Playlist Data")
        print("=" * 60)
        
        try:
            enrich_with_playlists.main()
            logging.info("Playlist enrichment completed successfully")
            return True
        except Exception as e:
            logging.error(f"Playlist enrichment error: {e}")
            print(f"ERROR: {e}")
            return False
    
    def run_full_pipeline(self) -> bool:
        """Run all pipeline steps in sequence"""
        logging.info("Starting: Full Pipeline")
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
    print("LUDIS SETUP WIZARD")
    print("=" * 60)
    print("\nWhat Ludis does:")
    print("  • Exports LaunchBox XML → CSV")
    print("  • Scans your filesystem for games")
    print("  • Reconciles LaunchBox data + filesystem")
    print("  • Generates migration scripts for ES-DE, RetroDECK, etc.")
    
    print("\n" + "-" * 60)
    print("💡 TIP: Use a copy of your LaunchBox Data/ folder")
    print("-" * 60)
    print("\nInstead of pointing to your live LaunchBox installation,")
    print("copy Data/Platforms/ and Data/Playlists/ to this project.")
    print("Remove any platforms/playlists you DON'T want to migrate.")
    print("\nBenefits:")
    print("  ✓ Full control over what gets scanned")
    print("  ✓ Keeps LaunchBox installation untouched")
    print("  ✓ Can maintain multiple configs for different targets")
    
    print("\n" + "-" * 60)
    print("Setup will ask 3 main questions:")
    print("-" * 60)
    print("  1. Where are your LaunchBox XML files? (Data/Platforms/, Data/Playlists/)")
    print("  2. Where did LaunchBox THINK your games were? (Windows paths in XMLs)")
    print("  3. Where are your games ACTUALLY located? (This machine's paths)")
    
    print("\n" + "-" * 60)
    print("Let's get started!")
    print("-" * 60)
    
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
    print("STEP 1 of 6: LaunchBox XML Data")
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
    print("STEP 2 of 6: LaunchBox Installation Context")
    print("-" * 60)
    print("What path does LaunchBox use in its XML files for game ROMs?")
    print("\nLaunchBox stores paths IN the XML as they were on the Windows")
    print("machine where LaunchBox is installed.")
    print("\n  Example: Z:\\media\\games\\library")
    print("  (This is what's IN the XML, even if you're running on Mac/Linux)")
    
    if defaults.get('windows_root'):
        print(f"\n  [default: {defaults['windows_root']}]")
        windows_root = input("  Path: ").strip() or defaults['windows_root']
    else:
        windows_root = input("\n  Path: ").strip()
    
    if not windows_root:
        print("\n  ERROR: LaunchBox installation path is required")
        return False
    
    print("\n" + "-" * 60)
    print("STEP 3 of 6: Game Library Location")
    print("-" * 60)
    print("What is the base path for your games library?")
    print("\n  Examples:")
    print("    • /Volumes/NAS/media/games/library  (macOS with NAS mounted)")
    print("    • /mnt/nas/media/games/library      (Linux with NAS mounted)")
    print("    • C:\\Program Files\\LaunchBox\\Games  (Windows)")
    print(f"\n  Detected OS: {platform.system()}")
    
    # Get base library path
    if defaults.get('local_root'):
        print(f"\n  [default: {defaults['local_root']}]")
        base_path = input("  Base library path: ").strip() or defaults['local_root']
    else:
        base_path = input("\n  Base library path: ").strip()
    
    if not base_path:
        print("\n  ERROR: Library path is required")
        return False
    
    lib_path = Path(base_path)
    if not lib_path.exists():
        print(f"\n  ⚠ WARNING: Directory not found: {lib_path}")
        confirm = input("  Continue anyway? (y/N): ").strip().lower()
        if confirm != 'y':
            return False
    else:
        print(f"  ✓ Directory found: {lib_path}")
    
    # Check structure
    print("\n" + "-" * 60)
    print("Does this directory directly contain platform folders,")
    print("or are there additional organizational layers?")
    print("\n  Examples:")
    print("    Direct:     library/Nintendo 64/")
    print("    Nested:     library/Consoles/Nintendo 64/")
    print("    Nested:     library/Retro/Consoles/Nintendo 64/")
    
    print("\n  [1] This directory directly contains platform folders")
    print("  [2] There are subfolders before platform folders")
    
    structure_choice = input("\n  Choice (1 or 2): ").strip()
    
    library_roots = []
    
    if structure_choice == '1':
        # Direct - use base path
        library_roots.append(base_path)
        print(f"\n  ✓ Using: {base_path}")
    
    elif structure_choice == '2':
        # Nested - discover subfolders
        print("\n  Scanning for category folders...")
        
        if not lib_path.exists():
            print("  ⚠ Cannot scan - path doesn't exist. Using base path.")
            library_roots.append(base_path)
        else:
            # Scan for subfolders (only 1 level deep - category folders)
            discovered = []
            
            try:
                for item in lib_path.iterdir():
                    if item.is_dir() and not item.name.startswith('.'):
                        discovered.append(item.name)
            except PermissionError:
                print("  ⚠ Permission denied. Using base path.")
                library_roots.append(base_path)
            
            if not discovered:
                print("  ⚠ No subfolders found. Using base path.")
                library_roots.append(base_path)
            else:
                discovered.sort()
                print(f"\n  Found {len(discovered)} category folder(s)")
                
                # Use inquirer for consistent UI
                questions = [
                    inquirer.Checkbox('folders',
                                     message="Select folders to include (Space to toggle, Enter to confirm)",
                                     choices=discovered,
                                     default=discovered,  # Pre-select all
                                     ),
                ]
                
                answers = inquirer.prompt(questions)
                
                if not answers or not answers.get('folders'):
                    print("\n  ⚠ No folders selected. Using base path.")
                    library_roots.append(base_path)
                else:
                    selected_folders = answers['folders']
                    library_roots = [str(lib_path / folder) for folder in selected_folders]
                    print(f"\n  ✓ Selected {len(library_roots)} folder(s):")
                    for root in library_roots:
                        print(f"    • {root}")
    else:
        # Invalid choice - use base path
        print("\n  ⚠ Invalid choice. Using base path.")
        library_roots.append(base_path)
    
    print(f"\n  Final library configuration: {len(library_roots)} location(s)")
    
    print("\n" + "-" * 60)
    print("STEP 4 of 6: Filesystem Scanning")
    print("-" * 60)
    print("Do you want to scan your filesystem to match files with")
    print("LaunchBox entries?")
    print("\n  Yes: Required for file size calculations and file existence validation")
    print("  No:  Metadata-only mode (faster, but no file verification)")
    
    default_scan = 'Y' if defaults['scan_filesystem'] else 'n'
    print(f"\n  [default: {default_scan}]")
    scan_choice = input("  Enable filesystem scanning? (Y/n): ").lower().strip() or default_scan.lower()
    scan_filesystem = scan_choice == 'y'
    
    print("\n" + "-" * 60)
    print("STEP 5 of 6: Ignore Patterns (Optional)")
    print("-" * 60)
    print("Configure patterns to exclude system files and folders during scanning.")
    print("\nRecommended defaults:")
    print("  Files:   .DS_Store, Thumbs.db, ._* (macOS resource forks)")
    print("  Folders: _* (any folder starting with _), .git, .svn")
    print("\n  Yes: Use recommended defaults (you can edit later)")
    print("  No:  Skip exclusions (scan everything)")
    
    print(f"\n  [default: Y]")
    ignore_choice = input("  Use recommended ignore patterns? (Y/n): ").lower().strip() or 'y'
    use_ignore_patterns = ignore_choice == 'y'
    
    # Default ignore patterns
    ignore_patterns = None
    if use_ignore_patterns:
        ignore_patterns = {
            'files': ['.DS_Store', 'Thumbs.db', 'desktop.ini', '._*'],
            'folders': ['_*', '.git', '.svn']
        }
        print("\n  ✓ Will use recommended ignore patterns")
        print("  (You can customize these in config.yaml later)")
    else:
        print("\n  → No ignore patterns configured")
    
    print("\n" + "-" * 60)
    print("STEP 6 of 7: Custom Game File Extensions (Optional)")
    print("-" * 60)
    print("Ludis already scans for the most common ROM file extensions:")
    print("  .zip, .7z, .iso, .cue, .bin, .chd, .rvz, .gdi, .nrg,")
    print("  .wbfs, .gcm, .gcz, .dol, .elf, .rom, .nes, .fds, .sfc,")
    print("  .smc, .gba, .gbc, .gb, .n64, .z64, .nds, .3ds, .wad,")
    print("  .wua, .xci, .nsp, .pbp, .vpk, .adf, .m3u, .xiso, .cpr,")
    print("  .vec, .bs, .pcm, .pce, .sgx, .md, .sms, .nsz")
    print("\nIf you need to scan for additional file types (e.g., .exe, .lnk, .app),")
    print("enter them as a comma-separated list.")
    print("\n  Format: .exe, .lnk, .bat")
    print("  Leave blank to use only the default extensions")
    
    additional_extensions_input = input("\n  Additional extensions: ").strip()
    additional_extensions = None
    
    if additional_extensions_input:
        # Parse comma-separated list
        extensions = [ext.strip() for ext in additional_extensions_input.split(',')]
        # Ensure they start with a dot
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
        # Filter out empty strings
        extensions = [ext for ext in extensions if len(ext) > 1]
        
        if extensions:
            additional_extensions = extensions
            print(f"\n  ✓ Will scan for additional extensions: {', '.join(extensions)}")
        else:
            print("\n  → No valid extensions provided, using defaults only")
    else:
        print("\n  → Using default extensions only")
    
    # STEP 7: Path Overrides (Optional)
    print("\n" + "=" * 60)
    print("STEP 7 of 7: Path Overrides (Optional)")
    print("-" * 60)
    print("If your game files moved after LaunchBox imported them, the paths")
    print("in LaunchBox XML won't match your current filesystem structure.")
    print("\nLudis includes path corrections for some platforms.")
    print("These fix case/naming mismatches for TurboGrafx/PC Engine systems.")
    
    path_overrides = None
    import_overrides = input("\n  Import sample NEC path overrides? (Y/n): ").strip().lower()
    
    if import_overrides in ('', 'y', 'yes'):
        # Load sample overrides from config.yaml.sample
        try:
            sample_config_path = Path(__file__).parent / "config.yaml.sample"
            if sample_config_path.exists():
                with open(sample_config_path) as f:
                    sample_config = yaml.safe_load(f)
                    sample_overrides = sample_config.get('options', {}).get('path_overrides', {})
                    if sample_overrides:
                        path_overrides = sample_overrides
                        print(f"\n  ✓ Imported {len(sample_overrides)} path override(s)")
                        print("    (NEC TurboGrafx-16, TurboGrafx-CD, PC Engine SuperGrafx)")
                    else:
                        print("\n  ⚠ No path overrides found in sample config")
            else:
                print("\n  ⚠ Sample config not found, skipping")
        except Exception as e:
            print(f"\n  ⚠ Could not load sample overrides: {e}")
    else:
        print("\n  → Skipped path overrides (you can add them later in config.yaml)")
    
    # Create config dictionary
    options_dict = {
        'scan_filesystem': scan_filesystem,
        'verbose': False,
        'show_progress': True,
    }
    
    if ignore_patterns:
        options_dict['ignore_patterns'] = ignore_patterns
    
    if additional_extensions:
        options_dict['additional_game_extensions'] = additional_extensions
    
    if path_overrides:
        options_dict['path_overrides'] = path_overrides
    
    config_data = {
        'version': '2.0',
        'paths': {
            'launchbox_data': lb_data,
            'output_directory': 'LB_Exports/',
            'windows_root': windows_root,
            'library_base_path': base_path,  # The root path user provided
            'library_roots': library_roots if library_roots else [],
        },
        'options': options_dict,
        'platform_structure': {},  # Will be populated after first scan
        'export_targets': {}  # Will be configured when first creating a migration
    }
    
    # Write config file
    print("\n" + "=" * 60)
    print("CONFIGURATION SUMMARY")
    print("=" * 60)
    print(f"\n  LaunchBox XML Data:   {lb_data}")
    print(f"  LaunchBox Path (XML): {windows_root}")
    print(f"  Library Base Path:    {base_path}")
    if len(library_roots) > 1:
        print(f"  Library Scan Paths:   {len(library_roots)} location(s)")
        for i, path in enumerate(library_roots, 1):
            print(f"    {i}. {path}")
    print(f"  Filesystem Scanning:  {'Enabled' if scan_filesystem else 'Disabled'}")
    print(f"  Ignore Patterns:      {'Enabled' if ignore_patterns else 'Disabled'}")
    if additional_extensions:
        print(f"  Custom Extensions:    {', '.join(additional_extensions)}")
    if path_overrides:
        print(f"  Path Overrides:       {len(path_overrides)} mapping(s)")
    
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
    
    # Check what has been completed
    has_nas_inventory = deps.get('nas_inventory', False)
    has_platform_exports = deps.get('all_platforms_csv', False)
    has_playlist_exports = deps.get('all_playlists_csv', False)
    has_master_inventory = deps.get('master_inventory_csv', False)
    has_platform_structure = bool(config.get('platform_structure'))
    
    choices = []
    
    # Setup & Configuration section
    choices.append("--- Setup & Configuration ---")
    
    platform_status = "✓" if has_platform_structure else "○"
    choices.append(f"{platform_status} Configure Platform Structure")
    choices.append("Re-run YAML Setup (reconfigure)")
    
    # Ludis Discovery Pipeline section
    choices.append("---")
    choices.append("--- Ludis Discovery Pipeline ---")
    
    if config.get('options.scan_filesystem', True):
        status = "✓" if has_nas_inventory else "○"
        choices.append(f"{status} Step 1: Scan Filesystem")
    else:
        choices.append("○ Step 1: Scan Filesystem (disabled in config)")
    
    status = "✓" if has_platform_exports else "○"
    choices.append(f"{status} Step 2: Export Platform Data")
    
    status = "✓" if has_playlist_exports else "○"
    choices.append(f"{status} Step 3: Export Playlist Data")
    
    status = "✓" if has_master_inventory else "○"
    choices.append(f"{status} Step 4: Build Master Inventory")
    
    # Playlist enrichment check
    if has_master_inventory:
        # Check if enrichment has been run by looking at master_inventory.csv
        output_dir = config.get('paths', {}).get('output_directory', 'LB_Exports/')
        if not Path(output_dir).is_absolute():
            master_inv_path = SCRIPT_DIR / output_dir / 'master_inventory.csv'
        else:
            master_inv_path = Path(output_dir) / 'master_inventory.csv'
        enriched = False
        if master_inv_path.exists():
            with open(master_inv_path, 'r', encoding='utf-8-sig') as f:
                header = f.readline()
                enriched = 'InAnyPlaylist' in header or 'Playlists' in header
        status = "✓" if enriched else "○"
        choices.append(f"{status} Step 5: Add Playlist Data")
    else:
        choices.append("○ Step 5: Add Playlist Data (requires master inventory)")
    
    # Convenience option
    choices.append("---")
    choices.append("▶ Run All Steps (Full Pipeline)")
    
    # Manual selections (only if master inventory exists)
    if has_master_inventory:
        choices.append("---")
        choices.append("Extract Manual Selections")
        choices.append("Drop-in Manual Selections")
    
    # Ludis Migration Pipeline section
    choices.append("---")
    choices.append("--- Ludis Migration Pipeline ---")
    
    storage_configured = False
    export_targets = config.get('export_targets', {})
    for target_name, target_config in export_targets.items():
        if target_config.get('enabled') and 'platform_storage_defaults' in target_config:
            storage_configured = True
            break
    
    if storage_configured:
        choices.append("Reconfigure Platform Storage Defaults")
        if has_master_inventory:
            choices.append("Create Migration Script")
    else:
        choices.append("Configure Platform Storage Defaults")
    
    # Utility options
    choices.append("---")
    choices.append("Validate Existing Data")
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
        print("\n" + "=" * 60)
        print("⚠  NO CONFIGURATION FOUND")
        print("=" * 60)
        print("\nLudis needs a config.yaml file to run.")
        print("This will guide you through a 6-step setup to create one.")
        print("\nYou can also:")
        print("  • Copy config.yaml.sample and edit it manually")
        print("  • Exit now and come back later")
        
        # Ask if they want to proceed
        confirm = inquirer.confirm("\nWould you like to start the interactive setup?", default=True)
        if not confirm:
            print("\nNo problem! When you're ready:")
            print("  1. Run: python3 ludis.py")
            print("  2. Or manually create config.yaml from config.yaml.sample")
            print("\nGoodbye!")
            sys.exit(0)
        
        # Run setup
        if not create_config_interactively():
            print("\nSetup cancelled. Run ludis.py again when ready.")
            sys.exit(0)
        
        print("\n" + "=" * 60)
        print("✓ Setup complete! config.yaml created")
        print("=" * 60)
        
        # Offer to discover platform structure
        print("\n" + "-" * 60)
        print("NEXT: Discover Platform Structure")
        print("-" * 60)
        print("\nBefore we can scan your filesystem, Ludis needs to understand")
        print("how each platform is organized (files vs folders vs nested).")
        print("\nThis will:")
        print("  • Scan your library folders")
        print("  • Show you each platform it finds")
        print("  • Ask how each one is structured")
        print("  • Save results to config.yaml")
        
        discover_now = inquirer.confirm("\nWould you like to discover platform structure now?", default=True)
        if discover_now:
            result = subprocess.run(
                [sys.executable, "scripts/interactive_scanner.py"],
                cwd=SCRIPT_DIR,
                capture_output=False,
                text=True
            )
            if result.returncode == 0:
                print("\n✓ Platform structure configured!")
            else:
                print("\n⚠ Platform discovery skipped or failed")
                print("You can run it later from the menu: Setup & Configuration > Configure Platform Structure")
        else:
            print("\nNo problem! You can configure this later from the menu:")
            print("  Setup & Configuration > Configure Platform Structure")
        
        print("\n" + "=" * 60)
        print("Continuing with Ludis...")
        print("=" * 60)
    
    # Load configuration
    print("\nLoading configuration...")
    config = Config(CONFIG_FILE)
    
    # Setup logging
    try:
        log_file = setup_logging(config)
        print(f"✓ Logging to: {log_file}")
        logging.info("=" * 60)
        logging.info("LUDIS - LaunchBox Universal Data Integration System")
        logging.info("=" * 60)
        logging.info(f"Version: {VERSION}")
        logging.info(f"Config: {CONFIG_FILE}")
        logging.info("")
    except Exception as e:
        print(f"⚠ Warning: Logging setup failed: {e}")
        print("  Continuing without log file...")
    
    # Check dependencies
    logging.info("Checking dependencies...")
    checker = DependencyChecker(config)
    deps = checker.check_all()
    checker.print_status()
    
    # Create pipeline
    pipeline = Pipeline(config)
    
    # Show menu
    while True:
        action = show_menu(config, deps)
        logging.info(f"User selected: {action}")
        
        if action == "Exit":
            logging.info("User exited Ludis")
            print("\nGoodbye!")
            break
        
        # Setup & Configuration
        elif "Configure Platform Structure" in action:
            result = subprocess.run(
                [sys.executable, "scripts/interactive_scanner.py"],
                cwd=SCRIPT_DIR,
                capture_output=False,
                text=True
            )
            if result.returncode == 0:
                print("\n✓ Platform structure updated!")
                # Reload config
                config.load()
                deps = checker.check_all()
            else:
                print("\n⚠ Platform discovery cancelled or failed")
        
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
        
        # Ludis Discovery Pipeline
        elif "Step 1: Scan Filesystem" in action:
            if config.get('options.scan_filesystem', True):
                confirm = inquirer.confirm("Scan filesystem and build NAS inventory?", default=True)
                if confirm:
                    if pipeline.run_filesystem_scan():
                        print("\n✓ Filesystem scan complete!")
                    deps = checker.check_all()
        
        elif "Step 2: Export Platform Data" in action:
            confirm = inquirer.confirm("Export platform data from LaunchBox XMLs?", default=True)
            if confirm:
                if pipeline.run_platform_export():
                    print("\n✓ Platform export complete!")
                deps = checker.check_all()
        
        elif "Step 3: Export Playlist Data" in action:
            confirm = inquirer.confirm("Export playlist data from LaunchBox XMLs?", default=True)
            if confirm:
                if pipeline.run_playlist_export():
                    print("\n✓ Playlist export complete!")
                deps = checker.check_all()
        
        elif "Step 4: Build Master Inventory" in action:
            confirm = inquirer.confirm("Build master inventory (reconcile LaunchBox + filesystem)?", default=True)
            if confirm:
                if pipeline.run_master_inventory():
                    print("\n✓ Master inventory complete!")
                deps = checker.check_all()
        
        elif "Step 5: Add Playlist Data" in action:
            confirm = inquirer.confirm("Add playlist data to master inventory?", default=True)
            if confirm:
                if pipeline.run_playlist_enrichment():
                    print("\n✓ Playlist data added!")
                deps = checker.check_all()
        
        # Full pipeline
        elif "Run All Steps" in action:
            confirm = inquirer.confirm("This will run the complete pipeline. Continue?", default=True)
            if confirm:
                pipeline.run_full_pipeline()
                deps = checker.check_all()
        
        # Manual selections
        elif action == "Extract Manual Selections":
            confirm = inquirer.confirm("Extract includes and excludes to JSON files?", default=True)
            if confirm:
                pipeline.extract_manual_selections()
        
        elif action == "Drop-in Manual Selections":
            confirm = inquirer.confirm("Apply includes and excludes from JSON files?", default=True)
            if confirm:
                pipeline.dropin_manual_selections()
        
        # Migration script generation
        elif action in ("Configure Platform Storage Defaults", "Reconfigure Platform Storage Defaults"):
            logging.info("Starting: Configure Platform Storage Defaults")
            from scripts import migration_builder
            migration_builder.configure_storage_defaults(config)
            # Reload config and refresh dependencies
            config.load()
            deps = checker.check_all()
            logging.info("Platform storage defaults configuration complete")
        
        elif action == "Create Migration Script":
            logging.info("Starting: Create Migration Script")
            from scripts import migration_builder
            migration_builder.run_interactive(config)
            logging.info("Migration script generation complete")
        
        # Utility options
        elif action == "Validate Existing Data":
            deps = checker.check_all()
            checker.print_status()
        
        elif action.startswith("---"):
            # Visual separator - do nothing
            continue
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

