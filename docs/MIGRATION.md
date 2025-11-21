# Migration Guide

This guide explains how to create and run migration scripts with Ludis.

## Overview

Ludis generates a **migration package** that you copy to your target device (Steam Deck, Retro handheld, etc.) and run there.

### What Gets Generated

```
dist_steam_deck_20251120_123456/
├── scripts/
│   ├── migrate_n64.py
│   ├── migrate_genesis.py
│   ├── migrate_ps2.py
│   └── ...
├── gamelists/
│   ├── n64/
│   │   └── gamelist.xml
│   ├── genesis/
│   │   └── gamelist.xml
│   └── ...
├── ludis-migrate.py          # Main orchestrator
├── manifest.json              # Migration metadata
└── install_list_windows.txt   # Windows games to install
```

## Prerequisites

Before creating a migration:

1. ✅ Master inventory built
2. ✅ Platform storage defaults configured
3. ✅ Validation reports reviewed
4. ✅ ManualInclude/ManualExclude set (if needed)

## Creating a Migration

### Step 1: Launch Migration Builder

```bash
python3 ludis.py
```

Select: **"Create Migration Script"**

### Step 2: Confirm Export Target

```
Export Target: steam_deck
Format: ESDE (EmulationStation Desktop Edition)

Proceed with this export target? (Y/n):
```

Choose your configured target or cancel to reconfigure.

### Step 3: Select Filters

Ludis shows all playlists found in your curated Data/ folder.

**Filter Presets:**
- **Use defaults:** Apply filters from config.yaml
- **Select all filters:** Include all playlists + favorites
- **Custom selection:** Pick individual playlists

**Example:**
```
[?] Filter preset: Custom selection

Select filters (Space to toggle, Enter to confirm):
☑ Include Overrides (ManualInclude/ManualExclude)
☐ Include LaunchBox Favorites
☑ Playlist: My Favorites
☑ Playlist: GOTY 2023
☐ Playlist: Backlog
☑ Playlist: NES Collection
```

**Tip:** The fewer filters, the smaller your migration.

### Step 4: Select Platforms

Ludis shows filtered game counts:

```
[X] Nintendo 64, 52 (of 625) Games, 1 GB (of 5 GB)
[X] Sega Genesis, 211 (of 1200) Games, 500 MB (of 2 GB)
[ ] Atari 2600, 0 (of 625) Games, 0 B (of 2 MB)
```

- Platforms with 0 filtered games are hidden
- All platforms are pre-selected (uncheck to exclude)

### Step 5: Review Storage Assignments

```
Default storage assignments:
[SSD] Nintendo 64 (52 games)
[SD ] Sega Genesis (211 games)
[SSD] Sony Playstation 2 (276 games)

Change any storage assignments? (y/N):
```

Assignments use your configured defaults. Override if needed.

### Step 6: Review Summary

```
MIGRATION SUMMARY
════════════════════════════════════════════════════════════
Target: steam_deck
Platforms: 41
Total games: 4,464
Total size: 5.64 TB

STORAGE REQUIREMENTS
────────────────────────────────────────────────────────────
/home/deck/Emulation/roms (Internal SSD)
  5 platforms, 1,157 games, 4.34 TB

/run/media/mmcblk0p1/Emulation/roms (SD Card)
  36 platforms, 3,080 games, 1.30 TB

Windows games: 191 (install list only)

Generate migration scripts? (Y/n):
```

**Check carefully:**
- Do you have enough space?
- Are storage paths correct for target device?
- Game count looks right?

### Step 7: Generation

```
GENERATING MIGRATION PACKAGE
────────────────────────────────────────────────────────────
Creating: dist_steam_deck_20251120_123456/
Generating platform scripts...
  ✓ migrate_n64.py
  ✓ migrate_genesis.py
  ...
Generating migration runner...
  ✓ ludis-migrate.py
Generating manifest...
  ✓ manifest.json
Generating gamelists...
  ✓ gamelists/n64/gamelist.xml
  ...
Generating Windows install list...
  ✓ install_list_windows.txt

✓ Migration package complete!
```

## Using the Migration Package

### Transfer to Target Device

Copy the entire `dist_XXX/` folder to your target device:

```bash
# Example: SCP to Steam Deck
scp -r dist_steam_deck_20251120_123456/ deck@steamdeck:~/

# Example: USB drive
cp -r dist_steam_deck_20251120_123456/ /Volumes/USB_DRIVE/
```

### On the Target Device

1. **Navigate to the folder:**
   ```bash
   cd ~/dist_steam_deck_20251120_123456/
   ```

2. **Run the orchestrator:**
   ```bash
   python3 ludis-migrate.py
   ```

### Migration Orchestrator Menu

```
LUDIS MIGRATION ORCHESTRATOR
════════════════════════════════════════════════════════════
Target: steam_deck
Created: 2025-11-20 12:34:56

Available platforms:
  [1] Nintendo 64 (52 games, 1.0 GB)
  [2] Sega Genesis (211 games, 500 MB)
  ...
  [41] Super Nintendo (208 games, 800 MB)
  [A] All platforms

Select platforms to migrate (comma-separated, or 'A' for all):
```

**Options:**
- Select specific platforms: `1,3,5`
- Select all: `A`
- Dry run: Add `--dry-run` flag
- Force overwrite: Add `--overwrite` flag

### Dry Run (Recommended First)

```bash
python3 ludis-migrate.py --dry-run
```

This simulates the migration without copying files:
- Shows what would be copied
- Validates source file existence
- Reports any errors
- **Safe to run multiple times**

### Actual Migration

```bash
python3 ludis-migrate.py
```

**What happens:**
1. Prompts for NAS mount point
2. Validates source file paths
3. Creates destination directories
4. Copies game files
5. Copies gamelist.xml files
6. Shows progress and results

**Overwrite behavior:**
- **Default (skip):** Existing files are skipped
- **--overwrite:** Existing files are replaced

### Post-Migration

#### 1. Verify Game Counts

Check each platform folder:
```bash
ls -1 /home/deck/Emulation/roms/n64/ | wc -l
# Should match migration summary
```

#### 2. Launch ES-DE

ES-DE should automatically detect:
- New game files
- Gamelist.xml metadata
- Box art (if configured in LaunchBox)

#### 3. Windows Games

Open `install_list_windows.txt` to see what needs manual installation:

```
CLOUD LAUNCHERS
────────────────────────────────────────────────────────────

  STEAM (89 games)
  ───────────────────────────────────────────────────────────
  • Cyberpunk 2077
  • Elden Ring
  ...

  EPIC GAMES (32 games)
  ───────────────────────────────────────────────────────────
  • Control
  • Alan Wake 2
  ...

MANUAL INSTALLS (79 games)
────────────────────────────────────────────────────────────
  • Diablo II (Folder: Windows/Blizzard/Diablo II)
  ...
```

Follow install instructions for each game.

## Migration Modes

### Copy (Default)

```
operation: copy
```

Files are **copied** from source to destination:
- Safe (original files unchanged)
- Requires destination storage space
- **Recommended for most users**

### Symlink (Advanced)

```
operation: symlink
```

Files are **symlinked** from source:
- Saves space (no duplication)
- Requires source files accessible from target
- **Use only if target device can access source (e.g., both on same network)**

## Troubleshooting

### "NAS not mounted"

**Problem:** Target device can't access source files

**Solution:**
1. Mount your NAS on the target device:
   ```bash
   sudo mount -t cifs //nas/share /mnt/nas
   ```
2. Provide correct mount point when prompted

### "Permission denied"

**Problem:** Can't write to destination

**Solution:**
```bash
sudo chown -R $USER:$USER /home/deck/Emulation/
```

### "File not found"

**Problem:** Source file path is wrong

**Solution:**
- Verify NAS mount point is correct
- Check that source files haven't moved
- Re-run filesystem scan in Ludis

### Migration Takes Forever

**Problem:** Network is slow or many large files

**Solution:**
- Run overnight
- Migrate smaller platforms first
- Use rsync for resume capability:
  ```bash
  rsync -avh --progress /mnt/nas/games/ /home/deck/Emulation/roms/
  ```

## Re-running Migrations

### Same Configuration

Ludis saves your last 5 configurations. Next time:

1. Select "Create Migration Script"
2. Choose "Use this configuration (with optional modifications)"
3. Optional: Change filters, platforms, or storage
4. Generate

### Modified Configuration

1. Adjust filters in menu
2. Add/remove platforms
3. Reassign storage
4. Generate new package

### Incremental Updates

**Scenario:** You added new games to a playlist

**Solution:**
1. Re-scan filesystem (if files changed)
2. Re-build master inventory
3. Create new migration with `--overwrite` flag
4. Only new/changed files will be copied

## Tips

### Test Small First

Before migrating 5TB:
1. Create migration with 1-2 small platforms
2. Verify on target device
3. Iterate and refine
4. Scale up to full migration

### Keep Migration Packages

Archive generated packages:
```bash
mkdir ~/ludis_migrations/
mv dist_steam_deck_* ~/ludis_migrations/
```

Useful for:
- Re-running later
- Auditing what was migrated
- Disaster recovery

### Parallel Migrations

Migrate to multiple devices simultaneously:

```bash
# Generate for Steam Deck
ludis.py > Create Migration Script (target: steam_deck)

# Generate for Retroid Pocket
ludis.py > Create Migration Script (target: retroid_pocket)

# Copy each to respective device
```

### Automation (Advanced)

For repeated migrations, script the orchestrator:

```bash
#!/bin/bash
cd /path/to/dist/
python3 ludis-migrate.py --non-interactive --platform=all --nas-mount=/mnt/nas
```

---

**Complete!** You now have a fully curated game library on your target device.

For questions or issues, refer to [GETTING_STARTED.md](GETTING_STARTED.md) or [CONFIGURATION.md](CONFIGURATION.md).

