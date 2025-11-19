# Migration Configuration Schema

## Overview

The migration system allows you to create ROM migration scripts for various devices (Steam Deck, retro handhelds, etc.) using ES-DE (EmulationStation Desktop Edition) format.

## Configuration Structure

### Export Targets

Each export target represents a destination device or location where you want to deploy ROMs.

```yaml
export_targets:
  steam_deck:                    # Target identifier (can be any name)
    enabled: true                # Whether this target is active
    format: "esde"               # Output format (currently only ES-DE supported)
    
    storage_locations:           # Available storage destinations on target device
      internal_ssd:              # Storage location identifier
        path: ""                 # Filesystem path on target device
        label: "Internal SSD"    # Human-readable label
      
      sd_card:
        path: ""
        label: "SD Card"
      
      # keep_on_nas is implicit - no path needed
    
    defaults:                    # Default preferences for migrations
      operation: "copy"          # "copy" or "symlink"
      
      filters:                   # Which games to include
        include_platform_best: false      # Games marked as "The Best"
        include_franchises: false         # Games in any franchise
        include_goty: false               # GOTY winners/nominees
        include_favorites: false          # All favorited games
        force_manual_include: true        # Always include ManualInclude=true
        force_manual_exclude: true        # Always exclude ManualExclude=true
        custom_fields: []                 # List of custom fields to filter by
```

### Migration History

Stores configurations from previous migrations to allow quick reuse of settings.

```yaml
migration_history:
  last_migration: "2025-11-18T15:30:00"  # ISO timestamp of last migration
  
  configurations:
    - timestamp: "2025-11-18T15:30:00"
      export_target: "steam_deck"
      operation: "symlink"
      platforms:
        - name: "Nintendo Wii U"
          storage: "sd_card"
          game_count: 754
        - name: "Sony Playstation 3"
          storage: "internal_ssd"
          game_count: 1234
      filters:
        include_platform_best: true
        include_franchises: false
        include_goty: true
        include_favorites: true
        force_manual_include: true
        force_manual_exclude: true
      total_games: 1988
      total_size_bytes: 524288000000
```

## Storage Location Options

### Internal SSD
- **Use case**: High-performance games that benefit from fast load times
- **Path example**: `/home/deck/Emulation/roms` (Steam Deck)
- **Operation modes**: Both copy and symlink supported

### SD Card
- **Use case**: Large libraries where internal storage is limited
- **Path example**: `/run/media/mmcblk0p1/Emulation/roms` (Steam Deck)
- **Operation modes**: Copy recommended, symlink supported

### Custom Path
- **Use case**: Platform-specific locations or external storage
- **Path example**: User-specified during migration
- **Operation modes**: Both copy and symlink supported

## Platform Storage Defaults

Platform storage defaults are configured per export target and determine the default storage location for each platform. This is a **required one-time setup** before creating your first migration.

### Configuration

Use the **"Configure Platform Storage Defaults"** menu option in Ludis to:

1. Select which platforms should go to **Internal SSD** by default
2. Select which platforms should go to **SD Card** by default
3. Any remaining platforms will use **Custom Path** (you'll specify during migration)

### Example

```yaml
export_targets:
  steam_deck:
    platform_storage_defaults:
      "Nintendo Entertainment System": "internal_ssd"
      "Nintendo Game Boy": "internal_ssd"
      "Atari 2600": "internal_ssd"
      "Nintendo Wii U": "sd_card"
      "Sony Playstation 3": "sd_card"
      "Arcade": "custom"
```

### Benefits

- **Speed**: Configure once, reuse for all migrations
- **Consistency**: Each platform always goes to its logical location
- **Flexibility**: Override defaults for specific migrations when needed
- **Organization**: Small/retro games on SSD, large/modern games on SD card

### When to Reconfigure

Run "Configure Platform Storage Defaults" again to:
- Add newly imported platforms
- Change storage strategy (e.g., move more games to SD card)
- Set up a different export target (each target has its own defaults)

## Operation Modes

### Copy
- **Description**: Creates independent copy of ROM files on target device
- **Pros**: 
  - Self-contained (no network dependency)
  - Portable device works offline
  - Best performance
- **Cons**:
  - Requires storage space
  - Duplicate files

### Symlink
- **Description**: Creates symbolic links pointing to original files
- **Pros**:
  - No duplicate files
  - Minimal storage usage
  - Changes to source reflect immediately
- **Cons**:
  - Requires network access (if NAS)
  - Dependent on source availability
  - May be slower over network

## Filter Options

All filters are **optional** and use OR logic (any match includes the game), except `force_manual_exclude` which always takes priority.

### include_platform_best
Includes games marked in `CUSTOM_The Best` field (platform-specific best games curated per platform).

### include_all_time_favorites
Includes games marked in `CUSTOM_All Time Favorites` field (your absolute favorite games across all platforms).

### include_favorites
Includes all games where `Favorite=true` in LaunchBox (the standard LaunchBox favorites system).

### include_backlog
Includes games marked in `CUSTOM_Backlog` field (games you plan to play).

### include_goty_winner
Includes games marked in `CUSTOM_GOTY Winner` field (Game of the Year winners).

### include_goty_nominee
Includes games marked in `CUSTOM_GOTY Nominee` field (Game of the Year nominees).

### include_on_deck
Includes games marked in `CUSTOM_On Deck` field (games you're currently playing or about to start).

### include_retro
Includes games marked in `CUSTOM_Retro Collection` field (classic/retro games collection).

### include_classic_titles
Includes games where `IsInClassicCollection=true` (games that appear in any curated "classic" playlist).

### include_franchises
Includes all games where `IsInFranchise=true` (games that belong to any franchise).

### force_manual_include
**Enabled by default**. Includes games where `ManualInclude=true`, regardless of other filters. This ensures manually selected games are always included.

### force_manual_exclude
**Enabled by default**. Excludes games where `ManualExclude=true`, regardless of other filters. This ensures manually excluded games are never included.

### custom_fields
**Flexible catch-all filter** for any additional LaunchBox custom fields not explicitly listed above.

**Use cases:**
- Future custom fields you create in LaunchBox
- Temporary/project-specific filters (e.g., "CUSTOM_Summer Sale")
- One-off collections (e.g., "CUSTOM_Kids Safe", "CUSTOM_Multiplayer Focus")
- Already-completed games (e.g., "CUSTOM_Finished")

**How it works:**
Any game where **any** of the listed custom fields equals `TRUE` will be included.

**Example:**
```yaml
custom_fields:
  - "CUSTOM_Finished"           # Games you've completed
  - "CUSTOM_Multiplayer Focus"  # Custom field for multiplayer games
  - "CUSTOM_Speed Run Worthy"   # Custom field for speedrunning
```

**Note:** The predefined filters above are recommended for permanent/common use cases, while `custom_fields` is for flexibility and ad-hoc filtering.

## Filter Logic

Filters use **OR** logic (any match includes the game), except for `force_manual_exclude` which takes priority:

1. **First**: Apply `force_manual_exclude` (removes games regardless of other filters)
2. **Then**: Apply inclusion filters (any match includes game):
   - `force_manual_include` OR
   - `include_platform_best` OR
   - `include_all_time_favorites` OR
   - `include_favorites` OR
   - `include_backlog` OR
   - `include_goty_winner` OR
   - `include_goty_nominee` OR
   - `include_on_deck` OR
   - `include_retro` OR
   - `include_classic_titles` OR
   - `include_franchises` OR
   - `custom_fields` match (any field in the list)

**Example**: If you enable `include_goty_winner` and `include_all_time_favorites`, a game will be included if it's EITHER a GOTY winner OR an all-time favorite (or both).

## ES-DE Platform Mapping

The system uses `scripts/platforms-esde.json` to map LaunchBox platform names to ES-DE folder names.

**Example mappings:**
- LaunchBox: "Nintendo Wii U" → ES-DE folder: "wiiu"
- LaunchBox: "Sony Playstation 3" → ES-DE folder: "ps3"
- LaunchBox: "NEC TurboGrafx-16" → ES-DE folder: "tg16"

## Generated Files

When you run "Build Migration Script", the system generates:

### Migration Script
**Location**: `migrations/migrate_to_[target]_[timestamp].sh`

Bash script containing:
- File copy/symlink commands
- Progress indicators
- Error handling
- Verification steps
- Summary report

### Manifest
**Location**: `migrations/manifest_[timestamp].json`

JSON file containing:
- Source → Destination mappings
- File sizes
- Platform groupings
- Filter settings used
- Total counts and sizes

### ES-DE Gamelist XML
**Location**: `migrations/gamelists/[platform]/gamelist.xml`

ES-DE compatible XML files containing:
- Game metadata (title, developer, publisher, etc.)
- Ratings and descriptions
- Release dates
- Genre information
- Path to ROM file

## Workflow

1. **Configure** export target in `config.yaml`
2. **Configure** platform storage defaults (one-time setup per target)
3. **Mark games** using ManualInclude/ManualExclude or custom fields
4. **Run** "Create Migration Script" from Ludis menu
5. **Configure** filters (or use defaults)
6. **Select** platforms to include
7. **Assign** storage locations (uses defaults, can override)
8. **Review** summary and confirm
9. **Execute** generated script on target device

## Notes

- Migration history stores last 5 configurations by default
- All paths use forward slashes, even on Windows
- Symlinks require source files to be accessible from target device
- ES-DE expects specific folder structure: `ROMs/[platform]/[game_files]`
- Original files in NAS are **never** modified or moved

