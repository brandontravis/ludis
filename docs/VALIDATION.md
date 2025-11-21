# Validation Guide

After building your master inventory, Ludis generates validation reports to help you identify potential issues before migration.

## Validation Reports Location

All reports are saved in:
```
LB_Exports/validation/
```

## Report Types

### 1. Potential Multi-File Games

**File:** `potential_multi_file_games.csv`

This report identifies games that might be split across multiple files.

#### Why This Matters

Multi-disc/multi-file games can inflate your library size if all files are migrated. Often, you only need Disc 1.

#### Issue Types

##### MULTI_DISC

**Example:**
```
Platform: Sony Playstation
TitleGroup: Final Fantasy VII
FileCount: 3
Files: FF7 (Disc 1).bin; FF7 (Disc 2).bin; FF7 (Disc 3).bin
Suggestion: Keep only Disc 1 (optional)
```

**Action:**
- Most emulators support disc-swapping via menu
- Migrating Disc 1 only saves space
- Use `ManualExclude` to exclude Disc 2, 3, etc.

##### BIN_CUE_PAIR

**Example:**
```
Platform: Sega CD
TitleGroup: Sonic CD
FileCount: 2
Files: Sonic CD.bin; Sonic CD.cue
Suggestion: Both files needed - no action required
```

**Action:**
- Keep both files (they work as a pair)
- No action needed

##### DIFFERENT_REGIONS

**Example:**
```
Platform: Nintendo 64
TitleGroup: GoldenEye 007
FileCount: 3
Files: GoldenEye (USA).n64; GoldenEye (Europe).n64; GoldenEye (Japan).n64
Suggestion: Choose preferred region (found: USA, Europe, Japan)
```

**Action:**
- Keep your preferred region
- Use `ManualExclude` for others

## Using ManualInclude / ManualExclude

These columns in `master_inventory.csv` give you manual control over what gets migrated.

### Workflow

1. **Review validation reports**

2. **Open master_inventory.csv in Excel/LibreOffice**

3. **Find games to exclude**
   - Filter by Title or Platform
   - Locate unwanted discs/regions

4. **Set ManualExclude = TRUE**
   ```
   Title: Final Fantasy VII (Disc 2)
   ManualExclude: TRUE
   ```

5. **Save CSV** (keep UTF-8-sig encoding)

6. **Drop-in changes:**
   ```bash
   python3 ludis.py
   ```
   Select: "Drop-in Manual Selections"

This updates the internal config files Ludis uses for filtering.

### ManualInclude

Force a game to be included even if it doesn't match any filters.

**Example use case:**
- You have a hidden gem that's not in any playlist
- You want to include a demo or beta
- A game was incorrectly excluded by filters

**Usage:**
```
Title: Obscure Indie Game
ManualInclude: TRUE
```

### Filter Precedence

```
ManualExclude > ManualInclude > Other Filters
```

1. If `ManualExclude = TRUE`, game is always excluded
2. If `ManualInclude = TRUE`, game is always included (unless excluded)
3. Otherwise, standard filters apply

## Validation Before Migration

Before creating a migration script, Ludis shows a storage requirements summary:

```
STORAGE REQUIREMENTS
════════════════════════════════════════════════════════════
/home/deck/Emulation/roms
  5 platforms
  1,157 games
  4.34 TB

/run/media/mmcblk0p1/Emulation/roms
  36 platforms
  3,080 games
  1.30 TB
```

**Check:**
- Do you have enough space on each storage location?
- Are the paths correct for your target device?

**If not:**
- Reconfigure storage assignments
- Enable more restrictive filters
- Manually exclude large games

## Common Validation Scenarios

### Scenario 1: Too Many Multi-Disc Games

**Problem:** 500 multi-disc PS1 games = 3x storage needed

**Solution:**
1. Open `potential_multi_file_games.csv`
2. Filter for `IssueType = MULTI_DISC`
3. Export list of all "Disc 2", "Disc 3", etc.
4. Batch-set `ManualExclude = TRUE` in master_inventory.csv
5. Drop-in changes

### Scenario 2: Region Duplicates

**Problem:** Games in USA, Europe, and Japan regions

**Solution:**
1. Decide on preferred region hierarchy (e.g., USA > Europe > Japan)
2. Sort validation report by TitleGroup
3. For each group, keep preferred region
4. Set `ManualExclude = TRUE` for others

### Scenario 3: Hidden Gems Not Included

**Problem:** A few specific games you want don't match any playlists

**Solution:**
1. Find games in master_inventory.csv
2. Set `ManualInclude = TRUE`
3. Drop-in changes

## Validation Workflow Example

```bash
# 1. Build inventory
python3 ludis.py
> Re-build master inventory

# 2. Review validation reports
cd LB_Exports/validation/
open potential_multi_file_games.csv

# 3. Edit master inventory
# (Open in Excel, set ManualExclude/ManualInclude)

# 4. Drop-in changes
python3 ludis.py
> Drop-in Manual Selections

# 5. Create migration
python3 ludis.py
> Create Migration Script
```

## Advanced: Custom Validation Scripts

You can write custom Python scripts to analyze `master_inventory.csv`:

```python
import csv

with open('LB_Exports/master_inventory.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Custom logic
        if int(row.get('FileSize', 0)) > 10_000_000_000:  # 10GB+
            print(f"Large game: {row['Title']} - {row['Platform']}")
```

## Tips

### Save Validation Reports

Keep validation reports for reference:
```bash
cp -r LB_Exports/validation/ validation_backup_2025-11-20/
```

### Iterative Refinement

Don't aim for perfection on first pass:
1. Do a quick migration with broad filters
2. Review what got included
3. Refine with ManualExclude/ManualInclude
4. Re-run migration

### Playlist-Based Filtering

The best validation is having well-curated playlists in LaunchBox:
- Create playlists for your must-play games
- Use dynamic playlists with filters
- Only copy those playlist XMLs to Ludis

---

**Next:** [MIGRATION.md](MIGRATION.md) - Creating and running migration scripts

