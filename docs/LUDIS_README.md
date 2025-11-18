# LUDIS - LaunchBox Universal Data Integration System

**Version 1.0.0**

A unified, interactive pipeline for exporting and enriching LaunchBox game library data.

## Features

✅ **Single Script** - One command to run everything  
✅ **Interactive Menu** - User-friendly checkbox/selection interface  
✅ **Progressive Setup** - Guides you through first-time configuration  
✅ **Smart Dependencies** - Only shows options when prerequisites are met  
✅ **Config-Driven** - YAML configuration for easy customization  
✅ **Full Pipeline** - Or run individual steps as needed  

---

## Quick Start

### 1. Install Dependencies

```bash
pip3 install pyyaml inquirer tqdm
```

### 2. Run Ludis

```bash
python3 ludis.py
```

**That's it!** On first run, Ludis will:
- Detect your operating system
- Ask you a few questions about your setup
- Create `config.yaml` automatically
- Continue to the main menu

You'll be asked for:
- **LaunchBox Data directory** (default: `Data/`)
- **Windows root path** (the path LaunchBox uses, e.g., `Z:\media\games\library`)
- **Local filesystem path** (where files are on your system, e.g., `/Volumes/media/games/library`)
- **Enable filesystem scanning?** (yes/no)

### 3. Use the Interactive Menu

Navigate with arrow keys, select with Enter, and let Ludis do the rest!

---

## What It Does

### Full Pipeline (Recommended)

Runs all steps in sequence:

1. **Filesystem Scan** (optional) - Scans your game library and creates `nas_inventory.csv`
2. **Platform Export** - Exports all LaunchBox platform data to `all_platforms.csv` + individual platform CSVs
3. **Playlist Export** - Exports filtered playlists to `all_playlists.csv` + individual playlist CSVs
4. **Master Inventory** - Reconciles LaunchBox data with filesystem, creates `master_inventory.csv`
5. **Playlist Enrichment** - Adds playlist membership columns to master inventory

### Custom Selection

Pick and choose which steps to run using interactive checkboxes.

### Individual Steps

Run only what you need:
- Filesystem scan only
- Export platforms only
- Export playlists only
- Build master inventory only
- Enrich with playlists only

---

## Configuration Options

### `config.yaml` Structure

```yaml
version: "1.0"

paths:
  launchbox_data: "Data/"              # LaunchBox XML directory
  output_directory: "LB_Exports/"      # Where CSVs are written
  windows_root: "Z:\\media\\games\\library"  # LaunchBox's internal path
  local_root: "/Volumes/media/games/library"  # Actual filesystem path

options:
  scan_filesystem: true   # Enable/disable filesystem scanning
  verbose: false          # Detailed logging
  show_progress: true     # Progress bars
```

### Path Configuration

**Why two paths?**

- `windows_root`: The path LaunchBox stores in its XML files (usually a Windows path like `Z:\...`)
- `local_root`: Where the files actually exist on your current system
  - macOS: `/Volumes/...`
  - Linux: `/mnt/...` or `/media/...`
  - Windows: Same as `windows_root`

Ludis converts between these automatically.

### Filesystem Scanning

**When `scan_filesystem: true`:**
- Scans `local_root` for game files
- Creates `nas_inventory.csv`
- Master inventory matches LaunchBox entries to actual files
- Shows which games are on disk vs. only in LaunchBox

**When `scan_filesystem: false`:**
- Skips filesystem scan
- Master inventory contains only LaunchBox metadata
- Useful for metadata-only exports or when files aren't accessible

---

## Output Files

### Core Exports

- `LB_Exports/all_platforms.csv` - All games from all platforms
- `LB_Exports/all_playlists.csv` - All curated playlists
- `LB_Exports/master_inventory.csv` - **Main output** - Reconciled data with playlist enrichment

### Individual Exports

- `LB_Exports/platforms/*.csv` - One CSV per platform
- `LB_Exports/playlists/*.csv` - One CSV per playlist (with category prefixes)

### Audit Files

- `LB_Exports/audits/nas_inventory.csv` - Filesystem scan results

---

## Master Inventory Columns

The `master_inventory.csv` contains:

### File Information
- `Filename`, `RelPath`, `LBFilePath`, `NASPath`, `FileExtension`
- `Matched` (Yes/No), `MatchType` (how it was matched)

### LaunchBox Metadata
- `Platform`, `Title`, `Developer`, `Publisher`, `Region`, `ReleaseDate`
- `LBID` (LaunchBox ID)
- `Favorite`, `Notes`, `Rating`, `StarRating`, etc.
- `Genre`, `PlayMode`, `MaxPlayers`
- `WikipediaURL`, `Version`

### Custom Fields
- `CUSTOM_The Best`, `CUSTOM_All Time Favorites`, `CUSTOM_Backlog`
- `CUSTOM_GOTY Winner`, `CUSTOM_GOTY Nominee`
- `CUSTOM_On Deck`, `CUSTOM_Retro Collection`, `CUSTOM_Finished`

### Playlist Enrichment (NEW!)
- `IsPlatformBest` (Boolean) - In a "The Best" playlist
- `IsInFranchise` (Boolean) - In a franchise playlist
- `Franchises` (Text) - Semicolon-separated franchise names
- `IsInCurated` (Boolean) - In a curated playlist
- `CuratedPlaylists` (Text) - Semicolon-separated playlist names
- `IsInClassicCollection` (Boolean) - In a classic console collection
- `PlaylistCount` (Integer) - Total playlists this game is in

### Future Use
- `IsPreferredVersion`, `HasClassicConsoleRelease`, `HasRemasterRelease`
- `IncludeInExport`, `IsPlatformExclusive`

---

## Playlist Filtering

Ludis automatically filters playlists to export only curated/meaningful ones:

### ✅ Included
- **Platform "The Best"** playlists (e.g., "PS2 The Best")
- **Franchise** playlists (e.g., "Mario", "Zelda", "Final Fantasy")
- **Curated** playlists (e.g., "GOTY Winners", "Backlog", "All Time Favorites")
- **Classic Collections** (e.g., "NES Mini", "PSOne Classic")

### ❌ Excluded
- Auto-generated **Genre** playlists (redundant with Genre column)
- Auto-generated **Region**, **PlayMode**, **Publisher** playlists
- Auto-generated **Source** playlists
- "All Games" playlists (redundant with platform exports)
- "Favorites" playlists (redundant with `IsFavorite` column)
- "The Rest" playlists (inverse of Favorites)
- Specific unwanted playlists (CHD Required, Vertically Oriented, etc.)

### Category Prefixes

Exported playlists are prefixed by category:
- `BEST_*.csv` - Platform "The Best" playlists
- `FRANCHISE_*.csv` - Franchise playlists
- `CURATED_*.csv` - Cross-platform curated playlists
- `CLASSIC_*.csv` - Classic console collections

---

## Interactive Menu

Ludis uses an interactive terminal menu system:

- **Arrow keys** to navigate
- **Spacebar** to select/deselect (in checkbox menus)
- **Enter** to confirm

### Menu Options

The menu adapts based on what's already been done:

- **Full rebuild** - Always available
- **Custom selection** - Choose specific steps
- **Individual steps** - Only shown when appropriate
- **Validate** - Re-check all dependencies
- **Regenerate config** - Reset configuration file
- **Exit** - Quit

---

## Troubleshooting

### "No configuration file found"

Run: `cp config.yaml.sample config.yaml` and edit the paths.

### "LaunchBox data directory not found"

Check `paths.launchbox_data` in `config.yaml`. Should point to your LaunchBox `Data/` directory.

### "NAS inventory missing"

Either:
1. Run "Filesystem scan" from the menu
2. Or set `options.scan_filesystem: false` to skip it

### "ERROR: PyYAML not installed"

Run: `pip3 install pyyaml inquirer tqdm`

### Interactive menu not working

Make sure you're running in a real terminal (not through an IDE's output panel).

---

## Architecture

Ludis is an **orchestrator** that coordinates existing modular scripts:

- `audit_library.py` - Filesystem scanning
- `export_all_platforms.py` - Platform export
- `export_all_playlists.py` - Playlist export
- `build_master_inventory.py` - Inventory reconciliation
- `enrich_with_playlists.py` - Playlist enrichment

This design keeps the codebase modular and maintainable while providing a unified user experience.

---

## Future Enhancements

- [ ] Export to ES-DE format
- [ ] Generate symlink/copy scripts for Steam Deck
- [ ] Smart timestamp-based incremental updates
- [ ] Validation mode with detailed reports
- [ ] Support for additional emulation frontends
- [ ] Web-based configuration UI

---

## Credits

Built for managing large LaunchBox game libraries with a focus on curation and export to limited-storage devices (e.g., Steam Deck with ES-DE).

**Version:** 1.0.0  
**License:** MIT  
**Author:** Brandon Travis

