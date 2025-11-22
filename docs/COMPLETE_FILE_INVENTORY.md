# Complete File Inventory - Current Broken State

## Root Directory

### `ludis.py` (970 lines)
**Status:** ✅ ACTIVE - Main entry point
**Functions:**
- `main()` - Entry point
- `create_config_interactively()` - Setup wizard
- `Pipeline.run_full_pipeline()` - Orchestrates all steps
- `Pipeline.run_filesystem_scan()` - Calls scanner
- `Pipeline.run_platform_export()` - Exports LaunchBox XMLs
- `Pipeline.run_playlist_export()` - Exports playlists
- `Pipeline.run_master_inventory()` - Builds master CSV
- `Pipeline.run_playlist_enrichment()` - Adds playlist data
- `Pipeline.extract_manual_selections()` - JSON export
- `Pipeline.dropin_manual_selections()` - JSON import

**What it does:**
- Interactive menu system
- Orchestrates entire pipeline
- Calls scripts via subprocess
- Modified since 232ff8c: Better setup wizard, interactive export targets

**Issues:**
- Line 226: Calls `audit_library.py nas-inventory` (broken scanner)

---

### `ludis.old.py` (970 lines)
**Status:** ❌ BACKUP - Not used
**What it is:** Copy of working ludis.py from before WIP changes
**Purpose:** Reference/backup only

---

### `config.yaml` (196 lines)
**Status:** ✅ ACTIVE - User configuration
**Contains:**
- `paths`: LaunchBox data, Windows root, library_roots
- `platform_structure`: 50 platforms with types (files/folders/skip)
- `export_targets`: steam_deck configuration
- `options`: Various settings

**Issues:**
- Has `type: skip` platforms that scanner doesn't handle

---

### `config.yaml.sample` (220 lines)
**Status:** ✅ ACTIVE - Template
**What it is:** Sample configuration with documentation

---

### `.gitignore`
**Status:** ✅ ACTIVE

---

### `README.md`
**Status:** ✅ ACTIVE - Project readme

---

### `GENERICIZATION_COMPLETE.md` (149 lines)
**Status:** ⚠️ DOCUMENTATION - Outdated
**What it claims:** All genericization is complete (IT'S NOT)

---

## scripts/ Directory (Active)

### `scripts/__init__.py`
**Status:** ✅ ACTIVE
**Exports:** All script modules

---

### `scripts/audit_library.py` (827 lines)
**Status:** 💔 ACTIVE BUT BROKEN - Main filesystem scanner
**Functions:**
- `load_config()` - Loads config.yaml
- `build_platform_rules()` - Converts platform_structure to dict
- `scan_library()` - Main scanning function (BROKEN)
- `cmd_nas_inventory()` - CLI entry point
- `is_game_file_for_rel()` - File type checking
- `is_platform_excluded()` - Platform exclusion

**What it does:**
- Scans filesystem for game files
- Generates `nas_inventory.csv`

**Issues:**
- Lines 412-425: Incomplete platform detection logic
- Only checks `len(rel_parts) == 2` (misses complex platforms)
- Doesn't handle `type: skip` platforms
- Still has hardcoded PS3/PS2/Wii U checks (lines 433-495)
- Mix of old and new logic

**Why it's broken:**
- `PLATFORM_RULES` dict is populated from config
- But scanner logic doesn't properly use it
- Skip platforms not in PLATFORM_RULES, so they get fully traversed
- Thousands of unnecessary directory walks

---

### `scripts/audit_library_v2.py` (448 lines)
**Status:** ❌ NOT USED - Abandoned attempt
**What it was:** Generic scanner attempt (CSV-driven)
**Why it exists:** Failed approach, never completed
**Should be:** DELETED

---

### `scripts/interactive_scanner.py` (505 lines)
**Status:** ⚠️ PARTIALLY ACTIVE - Discovery only
**Functions:**
- `load_config()` - Loads config
- `discover_structure_interactively()` - UI for platform discovery
- `save_platform_structure()` - Saves to config.yaml
- `scan_with_structure()` - REMOVED (was too slow)
- `main()` - Entry point

**What it does:**
- Interactive platform structure discovery
- Asks user: files or folders per platform
- Saves to `platform_structure` in config.yaml

**Issues:**
- Called by ludis.py if platform_structure not configured
- Was supposed to also scan, but that was removed
- Now only does discovery, then exits

**Status:** Discovery logic works, but never integrated properly

---

### `scripts/build_master_inventory.py` (645 lines)
**Status:** ✅ ACTIVE - Works
**Functions:**
- `main()` - Builds master_inventory.csv
- `normalize_platform_name()` - Platform name mapping
- Processes all_platforms.csv + nas_inventory.csv

**What it does:**
- Combines LaunchBox data with filesystem scan results
- Outputs `master_inventory.csv`

**No issues with this file**

---

### `scripts/export_all_platforms.py`
**Status:** ✅ ACTIVE - Works
**Functions:**
- `main()` - Exports platform XMLs to CSV
- Dynamic custom field extraction
- Windows game type detection

**What it does:**
- Parses Data/Platforms/*.xml
- Outputs `all_platforms.csv` and per-platform CSVs

**No issues with this file**

---

### `scripts/export_all_playlists.py`
**Status:** ✅ ACTIVE - Works
**Functions:**
- `main()` - Exports playlist XMLs
- Dynamic playlist resolution

**What it does:**
- Parses Data/Playlists/*.xml
- Outputs `all_playlists.csv`

**No issues with this file**

---

### `scripts/enrich_with_playlists.py`
**Status:** ✅ ACTIVE - Works
**Functions:**
- `main()` - Enriches inventory with playlist data
- Adds `InAnyPlaylist` and `Playlists` columns

**What it does:**
- Updates `master_inventory.csv` with playlist membership

**No issues with this file**

---

### `scripts/inventory_scanner.py` (326 lines)
**Status:** ✅ ACTIVE - Works
**Functions:**
- `InventoryScanner` class
- `get_platform_summary()` - Platform stats
- `get_platform_details()` - Detailed platform data
- `_should_include_game()` - Filter logic

**What it does:**
- Reads master_inventory.csv
- Provides stats for migration builder

**No issues with this file**

---

### `scripts/migration_builder.py`
**Status:** ✅ ACTIVE - Works
**Functions:**
- `select_export_target()` - Target selection
- `configure_filters()` - Filter UI
- `select_platforms()` - Platform selection
- `configure_storage_defaults()` - Storage config
- `run_interactive()` - Main workflow
- `build_file_list()` - Generates migration data
- `generate_platform_script()` - Per-platform scripts
- `generate_migration_runner()` - Main orchestrator

**What it does:**
- Interactive migration package builder
- Generates dist/ folder with scripts

**No issues with this file**

---

### `scripts/platform_mapper.py`
**Status:** ✅ ACTIVE - Works
**Functions:**
- `PlatformMapper` class
- `lb_to_esde()` - LaunchBox → ES-DE mapping
- Loads platforms-esde.json

**What it does:**
- Maps platform names between systems

**No issues with this file**

---

### `scripts/platforms-esde.json`
**Status:** ✅ ACTIVE - Data file
**What it is:** ES-DE platform definitions

---

### `scripts/validation_reports.py`
**Status:** ✅ ACTIVE - Works (but not called)
**Functions:**
- Validation report generation
- Multi-disc detection

**What it does:**
- Generates validation CSVs

**Status:** Code works, but not integrated into menu yet

---

### `scripts/migrate_wii_u_*.py`
**Status:** ❌ OLD - Not used
**What they are:** Legacy migration scripts

---

### `scripts/sanity_check_unmatched.py`
**Status:** ❌ OLD - Not used

---

## scripts.old/ Directory (Backups)

### ALL FILES IN scripts.old/
**Status:** ❌ BACKUPS - Not actively used
**What they are:** Working copies from 232ff8c
**Files:**
- `audit_library.py` - WORKING FAST SCANNER
- `build_master_inventory.py`
- `enrich_with_playlists.py`
- `export_all_platforms.py`
- `export_all_playlists.py`
- `inventory_scanner.py`
- `migration_builder.py`
- `platform_mapper.py`
- `platforms-esde.json`

**Purpose:** Reference and emergency restore

**Key file:** `scripts.old/audit_library.py` is the WORKING scanner

---

## docs/ Directory (23 files)

### `docs/REVERT_PLAN_SCANNER_FIX.md` (336 lines)
**Status:** ✅ USEFUL - Revert instructions
**Created:** Today
**What it is:** Step-by-step revert plan

---

### `docs/PERFORMANCE_ANALYSIS.md`
**Status:** ✅ USEFUL - Analysis
**Created:** Today
**What it is:** Deep dive into why scanner is slow

---

### `docs/IMPLEMENTATION_STATUS.md`
**Status:** ⚠️ OUTDATED
**What it claims:** Genericization phases complete
**Reality:** Phase 4 (scanner) is broken

---

### `docs/PHASE4_COMPLETION_PLAN.md`
**Status:** ✅ USEFUL - Original plan
**What it is:** How Phase 4 should have been done

---

### `docs/GENERICIZATION_COMPLETE.md` (in root)
**Status:** ❌ LIES
**What it claims:** Everything is ready for release
**Reality:** Scanner is completely broken

---

### Other docs/ files:
**Status:** ⚠️ MIXED - Some useful, some outdated
- `GETTING_STARTED.md` - Useful
- `CONFIGURATION.md` - Useful
- `MIGRATION_SCHEMA.md` - Useful
- `MIGRATION.md` - Useful
- `VALIDATION.md` - Useful
- Rest are session notes, old plans, etc.

---

## Summary: What's Actually Broken

### BROKEN FILES (1):
1. `scripts/audit_library.py` - Scanner logic incomplete

### FILES THAT SHOULD BE DELETED (2):
1. `scripts/audit_library_v2.py` - Failed attempt
2. `scripts/interactive_scanner.py` - Can keep discovery, but scan function was removed

### BACKUP FILES (Can keep or delete):
1. `scripts.old/*` - All working versions from 232ff8c
2. `ludis.old.py` - Working main script

### DOCUMENTATION OVERLOAD (23 files):
- Half are useful (setup guides, schema docs)
- Half are session notes and outdated status updates

---

## What's Actually In Use (Execution Flow)

1. **User runs:** `python3 ludis.py`
2. **ludis.py calls:**
   - `scripts/audit_library.py nas-inventory` ← BROKEN
   - `scripts/export_all_platforms.py` ← Works
   - `scripts/export_all_playlists.py` ← Works
   - `scripts/build_master_inventory.py` ← Works
   - `scripts/enrich_with_playlists.py` ← Works
3. **For migration:**
   - `scripts/migration_builder.py` ← Works
   - Uses `scripts/inventory_scanner.py` ← Works
   - Uses `scripts/platform_mapper.py` ← Works

**The ONLY broken link in the chain: `scripts/audit_library.py`**

Everything else actually works.

---

## The Fix

**ONE file needs fixing:** `scripts/audit_library.py`

**Lines that need work:** 412-425 (platform detection logic)

**What it needs:**
1. Check PLATFORM_RULES for configured platforms
2. Check PLATFORM_STRUCTURE_CONFIG for skip platforms and actually skip them
3. Handle complex nested platforms (PS3/PS2/Switch/Wii U)

**Everything else can stay as-is.**

---

Last Updated: 2025-11-21
Status: Complete inventory of broken state

