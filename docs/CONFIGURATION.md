# Configuration Guide

This guide explains the `config.yaml` structure and advanced configuration options.

## Config File Location

`config.yaml` lives in the root of your Ludis installation. A sample is provided at `config.yaml.sample`.

## Schema Version

```yaml
version: "2.0"
```

Ludis uses schema versioning for future migrations. Do not modify this value.

## Path Configuration

### Basic Paths

```yaml
paths:
  launchbox_data: "Data/"
  output_directory: "LB_Exports/"
  windows_root: "Z:\\media\\games\\library"
  library_roots:
    - "/Volumes/NAS/media/games/library"
    - "/mnt/external/Windows_Games"
```

#### `launchbox_data`

Where your curated LaunchBox XML files live (Platforms/ and Playlists/ folders).

- Relative paths are relative to Ludis root
- Absolute paths are preserved
- **Recommendation:** Use `Data/` with curated XMLs

#### `output_directory`

Where Ludis writes all generated files:
- `all_platforms.csv`
- `all_playlists.csv`
- `master_inventory.csv`
- `nas_inventory.csv`
- `validation/` reports

Default: `LB_Exports/`

#### `windows_root`

The path **LaunchBox stores in its XML files**. This is typically a Windows path, even if you're running Ludis on macOS/Linux.

Ludis uses this to translate LaunchBox's recorded paths to your actual file locations.

Example: If LaunchBox XML says:
```
Z:\media\games\library\Consoles\Nintendo 64\GoldenEye.n64
```

And `windows_root` is `Z:\media\games\library`, Ludis extracts:
```
Consoles/Nintendo 64/GoldenEye.n64
```

#### `library_roots` (NEW in v2.0)

List of **actual** locations where your game files exist on THIS machine.

The setup wizard intelligently discovers your library structure:

**Direct structure (single path):**
```yaml
library_roots:
  - "/Volumes/NAS/media/games/library"
```

**Nested structure (multiple category paths):**
```yaml
library_roots:
  - "/Volumes/NAS/media/games/library/Consoles"
  - "/Volumes/NAS/media/games/library/Handhelds"
  - "/Volumes/NAS/media/games/library/Computers"
```

**How it's configured:**

During Step 3 of setup, Ludis asks:
1. What's your base library path?
2. Does it directly contain platforms, or are there category subfolders?
3. If subfolders, Ludis scans (1 level deep) and shows a checkbox UI to select categories

All discovered folders are pre-selected - just uncheck any you don't want.

This auto-discovers your library organization without manual path entry.

**Manual configuration:**

You can also edit this directly if your structure changes:
```yaml
library_roots:
  - "/mnt/nas/retro_roms"
  - "/mnt/external/modern_games"
```

## Options

```yaml
options:
  scan_filesystem: true
  verbose: false
  show_progress: true
```

### `scan_filesystem`

- **true:** Ludis scans your `library_roots` to build `nas_inventory.csv` and match files
- **false:** Metadata-only mode (skips file scanning)

**When to disable:**
- Running Ludis remotely without file access
- Speeding up reruns (if files haven't changed)
- Debugging XML export issues

### `verbose`

Enable detailed logging output. Useful for troubleshooting.

### `show_progress`

Show progress bars during long operations.

## Platform Structure (NEW in v2.0)

```yaml
platform_structure:
  "Nintendo Wii U":
    scan_paths:
      - path: "Games"
        type: "files"
      - path: "[Loadiine]"
        type: "files"
    skip_paths:
      - "Updates"
      - "DLC"
```

### Purpose

Some platforms have complex folder structures (PS3, Wii U, etc.). Instead of hardcoding assumptions, Ludis lets you configure how to scan each platform.

### Structure

- **scan_paths:** Folders to scan within the platform folder
  - **path:** Subfolder name
  - **type:** 
    - `"files"` - Each ROM is a file
    - `"folders"` - Each game is a folder (e.g., PS3 EBOOT games)

- **skip_paths:** Folders to ignore (Updates, DLC, Demos, etc.)

### Auto-Detection (Future)

In future versions, Ludis will auto-detect simple vs. complex platforms and only prompt for configuration when needed.

### Manual Configuration

Edit `config.yaml` directly or wait for the interactive platform configurator (coming soon).

## Export Targets

```yaml
export_targets:
  steam_deck:
    enabled: true
    format: "esde"
    storage_locations:
      internal_ssd:
        path: "/home/deck/Emulation/roms"
        label: "Internal SSD"
      sd_card:
        path: "/run/media/mmcblk0p1/Emulation/roms"
        label: "SD Card"
    defaults:
      operation: "copy"
      filters:
        favorites: false
        playlist_my_favorites: true
        playlist_goty_2023: false
```

### Target Name

Each export target has a unique name (e.g., `steam_deck`, `retroid_pocket`, `anbernic`).

You can have multiple targets with different configurations.

### `format`

Currently supported:
- `esde` - EmulationStation Desktop Edition

Future formats: RetroPie, Batocera, custom.

### `storage_locations`

Define storage locations for this target device:

```yaml
storage_locations:
  internal_ssd:
    path: ""  # Filled in during "Configure Platform Storage Defaults"
    label: "Internal SSD"
  sd_card:
    path: ""
    label: "SD Card"
```

**Note:** Paths are for the **target device**, not your local machine.

### `defaults`

#### `operation`

- `copy`: Copy files (safe, recommended)
- `symlink`: Create symbolic links (advanced)

#### `filters`

Default filters for migration. Can be overridden interactively.

**Filter types:**
- `favorites`: LaunchBox native favorites
- `playlist_*`: Playlist-based filters (e.g., `playlist_my_favorites`)

**Dynamic playlists:** Filter names are auto-generated from your playlists during migration setup.

### Platform Storage Defaults

```yaml
platform_storage_defaults:
  "Nintendo 64": "internal_ssd"
  "Sony Playstation 3": "sd_card"
```

Maps each platform to a default storage location. Configured via:
- Menu: "Configure Platform Storage Defaults"

## Migration History

```yaml
migration_history:
  steam_deck:
    - timestamp: "2025-11-18T20:31:00"
      platforms: ["Nintendo 64", "Sega Genesis"]
      filters:
        favorites: true
      storage_assignments:
        "Nintendo 64": "internal_ssd"
```

Ludis automatically saves your last 5 migration configurations per target. This allows you to quickly re-run previous migrations or modify them.

**Benefits:**
- "Use last configuration" option
- Modify previous configs without starting from scratch
- Audit trail of what was migrated

## Tips

### Quick Config Edits

For simple changes, edit `config.yaml` directly:

```bash
nano config.yaml
```

Changes take effect immediately (no restart needed).

### Multiple Configs

You can maintain multiple Ludis installations with different configs:

```
~/ludis-steam-deck/     (curated for Steam Deck)
~/ludis-retroid/        (curated for Retroid Pocket)
~/ludis-full-backup/    (all platforms, no filters)
```

### Backup Your Config

Before major changes:

```bash
cp config.yaml config.yaml.backup
```

### Reset to Defaults

Delete `config.yaml` and re-run setup:

```bash
rm config.yaml
python3 ludis.py
```

Ludis will launch the setup wizard again.

## Advanced: Manual Config Creation

If you prefer not to use the wizard:

```bash
cp config.yaml.sample config.yaml
nano config.yaml
```

Edit all sections, then run Ludis.

---

**Next:** [VALIDATION.md](VALIDATION.md) - Understanding validation reports

