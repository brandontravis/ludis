# Ludis Development Changelog

## 2025-11-14 - Renamed Inventory Command

### Updated: `audit_library.py` and `build_master_inventory.py`

**Changes:**
- Renamed `inventory` command to `nas-inventory` for clarity
- Renamed output file from `inventory.csv` to `nas_inventory.csv`
- Renamed subdirectory from `inventory/` to `nas_inventory/`
- Updated `build_master_inventory.py` to reference new filename
- Added helpful error message when nas_inventory.csv is missing

**Usage:**
```bash
# Generate NAS inventory
python3 audit_library.py nas-inventory

# Build master inventory (requires nas_inventory.csv)
python3 build_master_inventory.py
```

---

## 2025-11-14 - Cleaned Up Audit Library Script

### Updated: `audit_library.py`

**Changes:**
- Removed duplicate detection commands (no longer needed for Ludis workflow)
- Enhanced `read_csv_paths()` to preserve all metadata fields from `all_platforms.csv`
- Streamlined command structure to focus on core audit functions

**Removed Commands:**
- `duplicates-in-csv` - Detected duplicate file paths in LaunchBox CSV
- `duplicates-on-fs` - Detected duplicate filenames on NAS filesystem
- Related functions: `cmd_duplicates_in_csv()` and `cmd_duplicates_on_fs()`
- ~89 lines of code removed

**Remaining Commands:**
1. `list-platforms` - List known ES-DE slugs and discovered platforms
2. `missing-in-fs` - Report LaunchBox entries where files don't exist on NAS
3. `untracked-on-fs` - Report NAS files not in LaunchBox
4. `inventory` - Scan NAS and generate inventory.csv (Platform, Title, RelPath)
5. `all` - Run all audits (missing-in-fs, untracked-on-fs, inventory)

**Enhanced Metadata Preservation:**
- `read_csv_paths()` now copies ALL fields from `all_platforms.csv` instead of just Platform/Title
- Preserves: DatabaseID, Favorite, ReleaseType, StarRating, CommunityStarRating, Genre, etc.
- This enables richer reporting in missing-in-fs and untracked-on-fs audits

**Why These Changes:**
- Duplicate detection is better handled by specialized scripts (like `find_c64_dupes.py`)
- Ludis family detection will use DatabaseID matching, not filesystem-based duplicate detection
- Streamlined audit_library to focus on inventory management and LaunchBox↔NAS reconciliation

---

## 2025-11-14 - Enhanced Platform Export

### Updated: `export_all_platforms.py`

**Changes:**
- Expanded CSV output from 10 columns to 34 columns
- Added comprehensive metadata extraction from LaunchBox platform XMLs
- Added control columns for future curation logic

**New Column Structure:**

#### File Information (5 columns)
- `Filename` - Just the filename (e.g., "Game.7z")
- `RelPath` - NAS-relative path (e.g., "Consoles/Nintendo 64 [1996]/Game.7z")
- `LBFilePath` - Original LaunchBox Windows path
- `NASPath` - Same as RelPath (for compatibility)
- `FileExtension` - File extension (e.g., ".7z")

#### Metadata Information (22 columns)
- `Platform` - Platform name (e.g., "Nintendo 64")
- `Title` - Game title
- `Developer` - Developer name(s)
- `Publisher` - Publisher name(s)
- `Region` - Region (e.g., "North America", "Europe", "Japan")
- `ReleaseDate` - Release date (YYYY-MM-DD format)
- `LBID` - LaunchBox internal UUID
- `DatabaseID` - **CRITICAL** LaunchBox Games Database ID (for family detection)
- `Favorite` - "true" or "false"
- `Notes` - User notes/description
- `Rating` - ESRB/age rating (e.g., "T - Teen", "M - Mature")
- `StarRating` - User star rating (integer 0-5)
- `StarRatingFloat` - User star rating (float 0.0-5.0)
- `CommunityStarRating` - Community average rating
- `CommunityStarRatingTotalVotes` - Number of community votes
- `WikipediaURL` - Wikipedia URL
- `Version` - Version/region tag (e.g., "(USA)", "(Europe)")
- `PlayMode` - Play modes (e.g., "Single Player", "Cooperative; Multiplayer")
- `Genre` - Genre(s) (semicolon-separated)
- `MaxPlayers` - Maximum player count
- `ReleaseType` - Release type (e.g., "Released", "Remaster", "Remake", "Port", "Unreleased")
- `Series` - Game series name

#### Control Columns (7 columns)
These are initially empty and will be populated by future curation scripts:
- `Include` - Will be set to "true" for games to symlink/export
- `IsFavorite` - Pre-populated from `Favorite` field (lowercase)
- `IsPlatformBest` - Will be set for "best of platform" games
- `IsPlatformExclusive` - Will be set for platform exclusives
- `IsPreferredVersion` - Will be set for the preferred version in a family
- `HasClassicRelease` - Will be set if a classic/original version exists
- `HasRemasterRelease` - Will be set if a remaster/remake exists

**Statistics from Current Export:**
- Total games: 21,296
- Games with DatabaseID: 20,956 (98.4%) - excellent for family detection
- Games marked Favorite: 3,254 (15.3%)
- Games with ReleaseType: 20,215 (94.9%)
- Games with CommunityStarRating: 21,296 (100%)

**Key Insights:**
- 98.4% of games have a `DatabaseID` - this is our primary key for family detection
- Only 340 games lack a DatabaseID - these will need manual review or title-based matching
- `ReleaseType` field is well-populated and will be crucial for identifying remasters/ports
- Community ratings are available for all games - can be used as a quality signal

**Next Steps:**
1. Generate playlist membership flags CSV
2. Update `build_master_inventory.py` to use new column structure
3. Begin family detection using `DatabaseID` as primary key

---

## Project Status

### ✅ Phase 1: Data Foundation - In Progress
- [x] Enhanced platform export with full metadata (COMPLETED)
- [ ] Generate playlist membership flags CSV
- [ ] Update master inventory builder
- [ ] Validate data completeness

### 📋 Phase 2: Family Detection - Not Started
- [ ] Build auto-family detection script
- [ ] Build manual review tool
- [ ] Assign FamilyKeys to all entries

### 📋 Phase 3: Preference Engine - Not Started
- [ ] Build interactive config wizard
- [ ] Build preferred edition selection script
- [ ] Generate user preferences YAML

### 📋 Phase 4: Export - Not Started
- [ ] Build LaunchBox playlist exporter
- [ ] Build ES-DE collection exporter
- [ ] Build ROM symlink generator

