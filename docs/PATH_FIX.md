# Path Fix - Scripts Directory Move

## Issue

After moving scripts to `scripts/` directory, the scripts were looking for `LB_Exports/` relative to their new location instead of the project root.

**Error:**
```
ERROR: Platforms CSV not found: /Users/brandon.travis/Development/lb-game-exporter/scripts/LB_Exports/all_platforms.csv
```

## Root Cause

Scripts used:
```python
SCRIPT_DIR = Path(__file__).resolve().parent
PLATFORMS_CSV = SCRIPT_DIR / "LB_Exports" / "all_platforms.csv"
```

This resolved to `scripts/LB_Exports/...` instead of `LB_Exports/...`

## Solution

Changed all scripts to use project root:

```python
# Project root is parent of scripts/ directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PLATFORMS_CSV = PROJECT_ROOT / "LB_Exports" / "all_platforms.csv"
```

## Files Fixed

1. ✅ `scripts/build_master_inventory.py`
   - `PLATFORMS_CSV`
   - `INVENTORY_CSV`
   - `OUTPUT_CSV`

2. ✅ `scripts/enrich_with_playlists.py`
   - `MASTER_INVENTORY`
   - `ALL_PLAYLISTS`
   - `OUTPUT_CSV`

3. ✅ `scripts/audit_library.py`
   - `CSV_PATH`
   - `NAS_ROOT`
   - `OUTDIR`

## Files NOT Changed

- `scripts/export_all_platforms.py` - Uses relative paths via argparse (works correctly)
- `scripts/export_all_playlists.py` - Uses relative paths via argparse (works correctly)

## Verification

All paths now correctly resolve to project root:

```
✓ /Users/brandon.travis/Development/lb-game-exporter/LB_Exports/all_platforms.csv
✓ /Users/brandon.travis/Development/lb-game-exporter/LB_Exports/master_inventory.csv
✓ /Users/brandon.travis/Development/lb-game-exporter/LB_Exports/audits/
```

## Why Export Scripts Don't Need Changes

The export scripts (`export_all_platforms.py`, `export_all_playlists.py`) use argparse with default values like:

```python
ap.add_argument("--combined", default="LB_Exports/all_platforms.csv")
```

When called via `ludis.py`, these relative paths are resolved from the **current working directory** (project root), not from the script's location. This is the correct behavior.

## Testing

```bash
cd /Users/brandon.travis/Development/lb-game-exporter
python3 -c "from scripts import build_master_inventory; print(build_master_inventory.PLATFORMS_CSV)"
# Output: /Users/brandon.travis/Development/lb-game-exporter/LB_Exports/all_platforms.csv ✓
```

## Lesson Learned

When organizing scripts into subdirectories:
- Scripts that define paths as constants need `PROJECT_ROOT = Path(__file__).parent.parent`
- Scripts that use argparse with relative defaults work from CWD (no changes needed)

