# Excluding Platforms

## Overview

You can temporarily exclude platforms from the Ludis pipeline by adding them to `config.yaml`. This is useful for:
- Debugging without processing large platforms (e.g., Arcade/MAME)
- Testing with a subset of platforms
- Excluding problematic platforms temporarily

---

## How to Exclude Platforms

### 1. Edit `config.yaml`

Add or modify the `exclude_platforms` list under `options`:

```yaml
options:
  scan_filesystem: true
  verbose: false
  show_progress: true
  exclude_platforms:
    - Arcade
    - MAME
```

### 2. Run the Pipeline

The exclusion will apply to all pipeline steps:
- ✓ Filesystem scan will skip Arcade folders
- ✓ Platform export will skip Arcade.xml
- ✓ Playlist export will skip Arcade playlists
- ✓ Master inventory won't include Arcade games

---

## What Gets Excluded

When you exclude a platform, the following are skipped:

### Filesystem Scan (`audit_library.py`)
- Skips scanning directories matching excluded platform names
- Example: `Arcade/` folder won't be scanned

### Platform Export (`export_all_platforms.py`)
- Skips reading platform XML files
- Example: `Data/Platforms/Arcade.xml` won't be processed
- Won't create `LB_Exports/platforms/Arcade.csv`

### Playlist Export (`export_all_playlists.py`)
- Skips playlists with excluded platform names in title
- Example: "Arcade The Best" playlist won't be exported
- Games from excluded platforms won't appear in cross-platform playlists

### Master Inventory
- Excluded platforms won't appear in `master_inventory.csv`
- No file matching for excluded platforms
- No playlist enrichment for excluded platforms

---

## How Matching Works

The exclusion uses **substring matching** (case-insensitive):

```yaml
exclude_platforms:
  - Arcade  # Matches: "Arcade", "arcade", "Arcade The Best", etc.
  - MAME    # Matches: "MAME", "mame", "MAME 2003", etc.
```

**Examples:**
- `Arcade` excludes:
  - Platform: "Arcade"
  - Playlist: "Arcade The Best"
  - Folder: "Arcade/"
  
- `Nintendo` would exclude:
  - "Nintendo 64"
  - "Nintendo GameCube"
  - "Super Nintendo Entertainment System"
  - etc.

**Be specific!** Use exact platform names to avoid unintended exclusions.

---

## Current Configuration

Your current `config.yaml` excludes:
```yaml
exclude_platforms:
  - Arcade
  - MAME
```

This will skip:
- ✗ Arcade platform
- ✗ MAME platform (if it exists)
- ✗ Any playlists with "Arcade" or "MAME" in the name

---

## Re-enabling Platforms

### Option 1: Remove from List

Edit `config.yaml` and remove the platform:

```yaml
options:
  scan_filesystem: true
  verbose: false
  show_progress: true
  exclude_platforms: []  # Empty list = no exclusions
```

### Option 2: Comment Out

Use `#` to comment out specific platforms:

```yaml
options:
  scan_filesystem: true
  verbose: false
  show_progress: true
  exclude_platforms:
    # - Arcade  # Temporarily re-enabled
    - MAME
```

### Option 3: Delete the Section

Remove the entire `exclude_platforms` section:

```yaml
options:
  scan_filesystem: true
  verbose: false
  show_progress: true
  # exclude_platforms removed
```

---

## Verification

When you run the pipeline, you'll see a warning at the start of each step:

```
⚠ Excluding platforms: arcade, mame
```

And when processing:

```
⊘ Skipping excluded platform: Arcade
```

---

## Testing Exclusions

You can test which platforms will be excluded without running the full pipeline:

```bash
python3 -c "
from scripts import export_all_platforms

test_platforms = ['Arcade', 'Nintendo 64', 'MAME', 'Sony Playstation']
for plat in test_platforms:
    excluded = export_all_platforms.is_platform_excluded(plat)
    status = '✗ EXCLUDED' if excluded else '✓ INCLUDED'
    print(f'{plat:20} {status}')
"
```

---

## Common Use Cases

### 1. Debug Without Arcade (Current Setup)
```yaml
exclude_platforms:
  - Arcade
  - MAME
```
**Why:** Arcade has thousands of games and can slow down testing.

### 2. Test With Only Modern Consoles
```yaml
exclude_platforms:
  - Atari
  - Commodore
  - Amstrad
  - Fairchild
  - Magnavox
  - Mattel
  # ... add other retro platforms
```

### 3. Skip Problematic Platforms
```yaml
exclude_platforms:
  - "Platform With Issues"  # Use quotes if name has spaces
```

---

## Important Notes

1. **Case-Insensitive:** "Arcade", "arcade", and "ARCADE" all work the same
2. **Substring Matching:** "Nintendo" will exclude ALL Nintendo platforms
3. **Persistent:** Exclusions persist until you remove them from `config.yaml`
4. **No Partial Rebuild:** You must rebuild from scratch after changing exclusions
5. **Data Loss:** Excluded platforms won't be in `master_inventory.csv` until re-enabled

---

## Troubleshooting

### Platform Still Appearing?

1. Check spelling in `config.yaml`
2. Verify YAML syntax (indentation matters!)
3. Look for the warning message: `⚠ Excluding platforms: ...`
4. Try exact platform name from LaunchBox

### Too Many Platforms Excluded?

1. Check for overly broad exclusions (e.g., "Nintendo")
2. Use more specific names
3. Test with the verification script above

### Can't Re-enable?

1. Make sure you removed the platform from the list
2. Check for typos or extra spaces
3. Verify YAML syntax is correct
4. Restart ludis.py to reload config

---

## Example Workflow

### Initial Testing (Exclude Arcade)
```yaml
exclude_platforms:
  - Arcade
  - MAME
```

Run pipeline, verify everything works.

### Full Production Run (Include Everything)
```yaml
exclude_platforms: []
```

Run pipeline again to include all platforms.

---

**Remember:** Always rebuild from scratch after changing exclusions!

Use: "Re-run from: Filesystem Scan" or "Rebuild Everything" in ludis.py menu.

