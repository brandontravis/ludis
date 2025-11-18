# Ludis User Experience Flow

## Overview

Ludis provides a guided, hierarchical workflow that adapts based on whether you're running it for the first time or managing an existing library.

---

## First Run Experience

### 1. Welcome Screen
```
============================================================
LUDIS v1.0.0
LaunchBox Universal Data Integration System
============================================================
```

### 2. Configuration Setup

If `config.yaml` doesn't exist, Ludis guides you through interactive setup:

```
============================================================
FIRST RUN SETUP
============================================================

No configuration file found. Let's create one!

I'll ask you a few questions to set up your environment.
(You can always edit config.yaml later)

------------------------------------------------------------
CONFIGURATION MODE
------------------------------------------------------------
I found default values in config.yaml.sample.

Default paths:
  LaunchBox Data: Data/
  Windows Root:   Z:\media\games\library
  Local Root:     /Volumes/The_Stacks/media/games/library

Would you like to:
  1. Use these defaults (you can edit each one)
  2. Start with blank values

Choice (1/2) [default: 1]: _
```

#### Each Configuration Step Shows Clear Instructions:

**STEP 1: LaunchBox Data Directory**
```
Where is your LaunchBox Data directory?
(This contains Platforms/ and Playlists/ folders)

→ Press ENTER to use default: Data/
  Or type a new path to override

Path: _
```

**STEP 2: Windows Root Path**
```
What path does LaunchBox use in its XML files?
(This is usually a Windows path like Z:\media\games\library)

→ Press ENTER to use default: Z:\media\games\library
  Or type a new path to override

Path: _
```

**STEP 3: Local Filesystem Path**
```
Where are your game files actually located on THIS system?
Detected OS: Darwin

→ Press ENTER to use default: /Volumes/The_Stacks/media/games/library
  Or type a new path to override

Path: _
✓ Directory found: /Volumes/The_Stacks/media/games/library
```

**STEP 4: Filesystem Scanning**
```
Do you want to scan your filesystem to match files with LaunchBox entries?
(Required for file matching, but can be skipped for metadata-only exports)

→ Press ENTER to use default: Yes
  Or type 'y' or 'n' to override

Enable? (y/n): _
```

### 3. Initial Menu (Before Pipeline Has Run)

After configuration, you see a **simple 3-option menu**:

```
============================================================
DEPENDENCY STATUS
============================================================
✓ Configuration file found
✓ LaunchBox data directory found
  - 54 platform XMLs
  - 1009 playlist XMLs
✗ NAS inventory missing
✗ Platform export missing
✗ Playlist export missing
✗ Master inventory missing
============================================================

What would you like to do?
  > Build Ludis Library (run all steps)
    Re-run YAML Setup (reconfigure)
    Exit
```

**Options:**
1. **Build Ludis Library** - Runs the complete pipeline (scan → platforms → playlists → inventory → enrichment)
2. **Re-run YAML Setup** - Deletes `config.yaml` and restarts configuration
3. **Exit** - Quit Ludis

---

## After Pipeline Completion

Once `master_inventory.csv` exists, the menu **expands** to show advanced options:

```
============================================================
DEPENDENCY STATUS
============================================================
✓ Configuration file found
✓ LaunchBox data directory found
  - 54 platform XMLs
  - 1009 playlist XMLs
✓ NAS inventory found
✓ Platform export found (all_platforms.csv)
✓ Playlist export found (all_playlists.csv)
✓ Master inventory found (master_inventory.csv)
============================================================

What would you like to do?
  > Rebuild Everything (all steps)
    ---
    Re-run from: Filesystem Scan (→ platforms → playlists → inventory → enrichment)
    Re-run from: Platform Export (→ playlists → inventory → enrichment)
    Re-run from: Playlist Export (→ inventory → enrichment)
    Re-run from: Master Inventory (→ enrichment)
    Re-run from: Playlist Enrichment (final step only)
    ---
    Validate Existing Data
    Re-run YAML Setup (reconfigure)
    Exit
```

### Hierarchical Execution

**Key Principle:** Each step automatically runs all subsequent steps.

This ensures data consistency - you can't have stale data downstream.

#### Example: Re-run from Platform Export

If you select "Re-run from: Platform Export", Ludis will:

```
============================================================
RUNNING PIPELINE FROM: PLATFORMS
============================================================
Steps to execute: platforms → playlists → inventory → enrich
============================================================

STEP: Platform Export
═════════════════════
[Progress bars...]

STEP: Playlist Export
═════════════════════
[Progress bars...]

STEP: Master Inventory
══════════════════════
[Progress output...]

STEP: Playlist Enrichment
═════════════════════════
[Progress output...]

============================================================
✓ PIPELINE COMPLETE!
============================================================
```

### When to Use Each Option

| Option | Use Case |
|--------|----------|
| **Rebuild Everything** | LaunchBox data changed significantly, or you want a fresh start |
| **Re-run from: Filesystem Scan** | Added/removed game files on disk |
| **Re-run from: Platform Export** | Changed custom fields in LaunchBox (e.g., "The Best" tags) |
| **Re-run from: Playlist Export** | Created/modified playlists in LaunchBox |
| **Re-run from: Master Inventory** | Want to rebuild reconciliation without re-exporting |
| **Re-run from: Playlist Enrichment** | Only need to update playlist membership flags |
| **Validate Existing Data** | Check what data exists without running anything |
| **Re-run YAML Setup** | Change paths or configuration |

---

## Confirmation Prompts

Every destructive action requires confirmation:

```
Run: platforms → playlists → inventory → enrichment?
  > Yes
    No
```

This prevents accidental data rebuilds.

---

## Progress Feedback

Each pipeline step shows:
- Clear section headers with `═` borders
- Progress bars (via `tqdm`) for long operations
- Success/failure indicators (`✓` / `✗`)
- Summary statistics

Example:
```
STEP: Platform Export
═════════════════════
Exporting platforms: 100%|████████████████| 54/54 [00:12<00:00, 4.32it/s]
✓ Exported 54 platforms (12,847 games)
✓ Wrote LB_Exports/all_platforms.csv
```

---

## Error Handling

If a step fails:
```
✗ FAILED at step: platforms

ERROR: Could not read Data/Platforms/Nintendo 64.xml
```

The pipeline stops, and you return to the menu to fix the issue.

---

## Design Philosophy

1. **Progressive Disclosure**: Simple menu first, advanced options only after initial setup
2. **Clear Defaults**: Always show what will happen if you press Enter
3. **Hierarchical Execution**: Prevent data inconsistency by enforcing step dependencies
4. **Confirmation Gates**: Require explicit confirmation for destructive actions
5. **Visual Feedback**: Use borders, icons, and progress bars to guide the user
6. **Graceful Errors**: Show helpful error messages and allow recovery

---

## Summary

- **First Run**: 3 simple options (Build, Configure, Exit)
- **After Setup**: 9 options with hierarchical rebuild capabilities
- **Every step**: Clear instructions, default values, and confirmation prompts
- **Goal**: Make it impossible to create inconsistent data

