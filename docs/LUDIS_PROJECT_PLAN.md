# Ludis: Game Library Curation Engine — Project Plan

**Version:** 0.1  
**Last Updated:** 2025-11-14  
**Status:** Planning & Foundation Phase

---

## Executive Summary

Ludis is a Python-driven curation system that transforms a sprawling 35,000+ title game library into a personalized, curated collection. It reads LaunchBox metadata, applies user preferences, consolidates game variants across platforms, and exports curated playlists to LaunchBox and ES-DE.

**Core Philosophy:** One canonical version per game family, intelligently selected based on platform priority, metadata signals, and user overrides.

---

## Problem Statement

### Current Challenges
- **35,000+ titles** across consoles, handhelds, PC launchers, emulators
- **No automatic variant consolidation** (remasters, ports, regional releases, hacks)
- **No cross-platform family detection** (e.g., SNES vs Genesis Aladdin)
- **No preference engine** (platform priority, remaster vs original, region preference)
- **No unified "curated collection"** that works across LaunchBox, ES-DE, and other frontends
- **1000+ playlists** with valuable curation data (GOTY, Best-Of lists) not leveraged for automated decisions

### What Ludis Solves
- **Automatic family detection** across platforms
- **Intelligent variant selection** based on configurable preferences
- **Playlist-driven curation** (leverage existing "NES The Best" etc. as input signals)
- **Manual override system** for edge cases
- **Export to multiple frontends** (LaunchBox playlists, ES-DE collections, symlinked ROM folders)

---

## Core Concepts

### 1. Game Families
A **family** represents all variants of a "game" across platforms, regions, and editions.

**Examples from screenshots:**

#### Super Mario Bros. Family
- `Super Mario Bros.` (NES) — original
- `Super Mario Bros. 2` (NES, Famicom) — sequel
- `Super Mario Bros. 3` (NES) — sequel
- `Super Mario Bros. + Duck Hunt` (NES) — bundle
- `Super Mario Bros. Deluxe` (Game Boy) — enhanced port
- `Classic NES Series: Super Mario Bros.` (GBA) — rerelease
- `New Super Mario Bros.` (DS) — spiritual successor
- `New Super Mario Bros. 2` (3DS) — sequel to spiritual successor
- `New Super Mario Bros. U` (Wii U) — HD version
- `New Super Mario Bros. U Deluxe` (Switch) — enhanced remaster
- `All Night Nippon Super Mario Bros.` (Famicom) — promotional variant
- `Super Mario Advance 4: Super Mario Bros. 3` (GBA) — enhanced port

**Family Detection Strategy:**
- **Exact title match** across platforms (e.g., "Aladdin" on SNES vs Genesis → **different games**, same title)
- **LaunchBox DatabaseID** as primary key (from `<DatabaseID>` field in platform XMLs)
- **Manual FamilyKey assignment** for ambiguous cases (e.g., numbered sequels, subtitles, bundles)

#### Aladdin Family (Complex Case)
From screenshot:
- `Disney's Aladdin` (MS-DOS) — PC port
- `Aladdin` (NES - Hummer Team) — unlicensed clone
- `Aladdin` (Game Boy) — unique version
- `Aladdin` (Sega Genesis) — Capcom version (different from SNES)
- `Aladdin` (SNES) — Disney Interactive version (different from Genesis)
- `Aladdin` (Game Gear, Master System) — 8-bit ports
- `Aladdin in Nasira's Revenge` (PlayStation) — sequel
- `Aladdin Magic Racer` (Wii) — spin-off

**Challenge:** Same title, **different games** on SNES vs Genesis. Requires:
- DatabaseID matching (LaunchBox already distinguishes these)
- Manual review for unlicensed/bootleg variants

### 2. Preferred Edition
The **single version** of a family selected for "wine cellar" display, based on:
1. **Platform priority** (user-defined ranking)
2. **Region priority** (USA > Europe > Japan, configurable)
3. **Remaster preference** (prefer enhanced/remastered vs original, configurable)
4. **Playlist membership** (games in "Favorites" or "GOTY" lists get boosted)
5. **Star ratings** (user rating + community rating weighted)
6. **Manual overrides** (always trump automated selection)

### 3. Manual Overrides
Three columns in master inventory CSV:
- `ManualPreferred` — force this as the preferred edition (overrides all rules)
- `ManualInclude` — always include in exports (even if not preferred)
- `ManualExclude` — never export (even if selected as preferred)

---

## Data Sources

### LaunchBox XML Structure
Based on `Nintendo 64.xml` sample:

#### Key Fields Available
```xml
<Game>
  <ID>c3f81e4e-79d3-446d-bef8-295ef9d93efb</ID>
  <DatabaseID>415</DatabaseID>  <!-- CRITICAL: LaunchBox Games DB ID -->
  <Title>WWF Attitude</Title>
  <Platform>Nintendo 64</Platform>
  <ApplicationPath>Z:\media\games\library\Consoles\Nintendo 64 [1996]\WWF Attitude (USA).7z</ApplicationPath>
  
  <!-- Metadata -->
  <Developer>Acclaim Studios Salt Lake City</Developer>
  <Publisher>Acclaim Entertainment</Publisher>
  <Region>North America</Region>
  <ReleaseDate>1999-08-31</ReleaseDate>
  <Genre>Fighting; Sports</Genre>
  <Series />
  <PlayMode>Cooperative; Multiplayer</PlayMode>
  <MaxPlayers>4</MaxPlayers>
  <ReleaseType>Released</ReleaseType>  <!-- Can be: Released, Remaster, Remake, Port, etc. -->
  
  <!-- User Data -->
  <Favorite>true</Favorite>
  <Completed>false</Completed>
  <Status>Imported ROM</Status>
  <StarRatingFloat>0</StarRatingFloat>
  <StarRating>0</StarRating>
  <CommunityStarRating>3.2875</CommunityStarRating>
  <CommunityStarRatingTotalVotes>40</CommunityStarRatingTotalVotes>
  <PlayCount>0</PlayCount>
  <PlayTime>0</PlayTime>
  
  <!-- Notes, URLs, etc. -->
  <Notes>...</Notes>
  <WikipediaURL>https://en.wikipedia.org/wiki/WWF_Attitude</WikipediaURL>
  <VideoUrl>https://www.youtube.com/watch?v=ZfjyYJZzSsU</VideoUrl>
</Game>
```

#### Fields We'll Use for Curation
- **DatabaseID** — primary key for family detection
- **ReleaseType** — distinguish remasters/remakes/ports from originals
- **Favorite** — binary flag (boost in selection)
- **StarRating** / **CommunityStarRating** — quality signals
- **Region** — for region preference
- **ReleaseDate** — for "prefer newer" or "prefer original" logic
- **Genre** / **PlayMode** / **MaxPlayers** — for filtering/reporting
- **Series** — secondary family grouping hint

### Existing CSV Exports
1. **`LB_Exports/all_platforms.csv`** — all games from platform XMLs
   - Columns: Platform, Title, FilePath, Shortname, NASPath, Developer, Publisher, Region, ReleaseDate, ID
   - Generated by: `export_all_platforms.py`

2. **`LB_Exports/all_playlists.csv`** — all playlist memberships
   - Columns: Playlist, Title, FilePath, Shortname, Developer, Publisher, Region, ReleaseDate, GameId
   - Generated by: `export_all_playlists.py`

3. **`LB_Exports/audits/inventory.csv`** — filesystem scan of actual ROM files
   - Columns: Platform, Title, RelPath
   - Generated by: (audit script)

4. **`LB_Exports/master_inventory.csv`** — reconciled inventory + LaunchBox metadata
   - Columns: InvPlatform, InvTitle, RelPath, Matched, MatchType, + all all_platforms columns
   - Generated by: `build_master_inventory.py`

---

## Architecture

### Phase 1: Data Foundation (CURRENT)
**Goal:** Ensure clean, complete master inventory with all LaunchBox metadata

#### 1.1 Enhance Platform Export ✅ (DONE)
- ✅ Script: `export_all_platforms.py`
- ✅ Extracts: ID, DatabaseID, Title, Platform, Region, ReleaseDate, Developer, Publisher, Genre, Series, PlayMode, MaxPlayers, ReleaseType, Favorite, StarRating, CommunityStarRating, Status

**TODO:**
- [ ] Add missing fields to export:
  - `DatabaseID` (critical for family detection)
  - `ReleaseType` (for remaster detection)
  - `Favorite`, `StarRating`, `CommunityStarRating` (for selection scoring)
  - `Genre`, `Series`, `PlayMode`, `MaxPlayers` (for filtering/reporting)

#### 1.2 Enhance Playlist Export ✅ (DONE)
- ✅ Script: `export_all_playlists.py`
- ✅ Supports both explicit entries and filter-based smart playlists

**TODO:**
- [ ] Generate playlist membership flags CSV:
  - Columns: `GameId`, `InGOTY`, `InFavorites`, `InBestOf_NES`, `InBestOf_SNES`, etc.
  - Binary flags for key playlists (user-configurable list)

#### 1.3 Rebuild Master Inventory
- ✅ Script: `build_master_inventory.py`
- ✅ Reconciles filesystem inventory with LaunchBox metadata

**TODO:**
- [ ] Update to include new fields from enhanced platform export
- [ ] Add playlist membership flags (join with playlist CSV)
- [ ] Add computed columns:
  - `LudisID` — unique stable ID (use LaunchBox ID if available, else hash of Platform+Title+RelPath)
  - `FamilyKey` — initially empty, populated by family detection script
  - `PreferredEdition` — boolean, initially false
  - `ManualPreferred`, `ManualInclude`, `ManualExclude` — initially empty

---

### Phase 2: Family Detection & Consolidation
**Goal:** Group variants into families, assign FamilyKeys

#### 2.1 Auto-Family Detection Script (NEW)
**Script:** `detect_families.py`

**Strategy:**
1. **DatabaseID matching** (primary)
   - All games with same `DatabaseID` → same family
   - FamilyKey = `LBDB_{DatabaseID}`

2. **Exact title + series matching** (secondary)
   - Games with same normalized title + Series field → same family
   - Normalize: lowercase, strip parentheticals, strip "The/A/An"
   - FamilyKey = `TITLE_{normalized_title}`

3. **Numbered sequels** (tertiary)
   - Detect patterns: "Game 2", "Game II", "Game: Part 2"
   - Group into series families
   - FamilyKey = `SERIES_{base_title}`

4. **Ambiguous cases** → flag for manual review
   - Same title, different DatabaseID (e.g., Aladdin SNES vs Genesis)
   - No DatabaseID, no series, generic title
   - Output: `families_to_review.csv`

**Output:**
- Updates `master_inventory.csv` with `FamilyKey` column populated
- Generates `families_to_review.csv` for manual assignment

#### 2.2 Manual Family Review Workflow (NEW)
**Tool:** `review_families.py` (interactive CLI)

**Features:**
- Display ambiguous groups side-by-side
- User can:
  - Merge into single family
  - Split into separate families
  - Assign custom FamilyKey
- Updates `master_inventory.csv` with user decisions

---

### Phase 3: Preference Engine & Selection
**Goal:** Select preferred edition per family based on user preferences

#### 3.1 Interactive Config Wizard (NEW)
**Script:** `configure_ludis.py`

**Generates:** `ludis_config.yaml`

**Configuration Sections:**

##### Platform Priority
```yaml
platform_priority:
  # Higher number = higher priority
  # Auto-detected from master inventory, user ranks interactively
  handheld_8bit:
    - {name: "Nintendo Game Boy", priority: 100}
    - {name: "Sega Game Gear", priority: 90}
    - {name: "Atari Lynx", priority: 80}
  
  console_8bit:
    - {name: "Nintendo Entertainment System", priority: 100}
    - {name: "Sega Master System", priority: 90}
    - {name: "Atari 7800", priority: 80}
  
  console_16bit:
    - {name: "Super Nintendo Entertainment System", priority: 100}
    - {name: "Sega Genesis", priority: 95}
    - {name: "NEC TurboGrafx-16", priority: 85}
  
  # ... etc for all platform categories
```

##### Region Priority
```yaml
region_priority:
  - "North America"
  - "Europe"
  - "Japan"
  - "World"
```

##### Remaster Preferences
```yaml
remaster_preference:
  global: "prefer_remaster"  # or "prefer_original" or "case_by_case"
  
  # Per-family overrides (populated via manual review)
  overrides:
    - family_key: "LBDB_123"
      prefer: "original"
      reason: "Remaster has censorship"
```

##### Playlist Weights
```yaml
playlist_weights:
  # Only include playlists that should influence selection
  # (not all 1000+ playlists)
  - {name: "Favorites", weight: 100}
  - {name: "GOTY", weight: 50}
  - {name: "NES The Best", weight: 30}
  - {name: "SNES The Best", weight: 30}
  # ... user selects which playlists matter
```

##### Rating Weights
```yaml
rating_weights:
  user_rating: 2.0      # StarRating weight
  community_rating: 1.0 # CommunityStarRating weight
```

#### 3.2 Preferred Edition Selection Script (NEW)
**Script:** `select_preferred_editions.py`

**Algorithm:**
For each family:
1. **Check manual overrides first**
   - If any entry has `ManualPreferred=true` → select that, done

2. **Filter out excluded entries**
   - Remove entries with `ManualExclude=true`

3. **Score each remaining entry:**
   ```python
   score = (
       platform_priority_score +
       region_priority_score +
       remaster_preference_score +
       playlist_membership_score +
       (user_rating * user_rating_weight) +
       (community_rating * community_rating_weight)
   )
   ```

4. **Select highest score** → set `PreferredEdition=true`

5. **Handle ties:**
   - Prefer entry with `Favorite=true`
   - Prefer newer ReleaseDate (for remasters) or older (for originals)
   - Prefer shorter filename (fewer region tags = cleaner release)

**Output:**
- Updates `master_inventory.csv` with `PreferredEdition` column
- Generates `selection_report.csv` with scores and reasons per family

---

### Phase 4: Export to Frontends
**Goal:** Generate playlists, collections, and ROM symlinks for LaunchBox and ES-DE

#### 4.1 LaunchBox Playlist Export (NEW)
**Script:** `export_launchbox_playlists.py`

**Generates:**
- `Data/Playlists/Ludis - Curated.xml` — all PreferredEdition=true entries
- `Data/Playlists/Ludis - Top Shelf.xml` — PreferredEdition=true + (Favorite=true OR InGOTY=true)
- `Data/Playlists/Ludis - {Platform}.xml` — per-platform curated collections

**XML Format:**
```xml
<?xml version="1.0" standalone="yes"?>
<LaunchBox>
  <Playlist>
    <Title>Ludis - Curated</Title>
    <NestedName>Ludis</NestedName>
  </Playlist>
  <PlaylistGame>
    <GameId>{LaunchBox ID}</GameId>
    <GameTitle>{Title}</GameTitle>
    <GamePlatform>{Platform}</GamePlatform>
    <GameFileName>{Filename}</GameFileName>
  </PlaylistGame>
  <!-- ... more entries ... -->
</LaunchBox>
```

#### 4.2 ES-DE Collection Export (NEW)
**Script:** `export_esde_collections.py`

**TODO:** Research ES-DE collection format
- [ ] Determine ES-DE gamelist.xml schema
- [ ] Determine ES-DE collection.cfg format
- [ ] Map LaunchBox artwork paths to ES-DE structure

**Planned Outputs:**
- `esde_exports/collections/Ludis - Curated.cfg`
- `esde_exports/gamelists/{platform}/gamelist.xml` (filtered to PreferredEdition=true)

#### 4.3 ROM Symlink Generator (NEW)
**Script:** `generate_rom_symlinks.py`

**Purpose:** Create curated ROM folder structure for copying to devices

**Example:**
```
curated_roms/
  nes/
    Super Mario Bros. 3.zip -> ../../Consoles/Nintendo Entertainment System [1983]/Super Mario Bros. 3 (USA).zip
    Legend of Zelda, The.zip -> ../../Consoles/Nintendo Entertainment System [1983]/Legend of Zelda, The (USA).zip
  snes/
    Super Metroid.zip -> ../../Consoles/Super Nintendo Entertainment System [1990]/Super Metroid (USA).zip
```

**Features:**
- Symlinks for PreferredEdition=true entries
- Optional: include ManualInclude=true entries
- Organized by platform
- Optionally rename to clean titles (strip region tags)

---

## Current Status

### ✅ Completed
- [x] Platform XML export script (`export_all_platforms.py`)
- [x] Playlist XML export script (`export_all_playlists.py`)
- [x] Master inventory reconciliation (`build_master_inventory.py`)
- [x] Filesystem audit script (generates `inventory.csv`)
- [x] C64 ROM deduplication logic (can be adapted for family detection)

### 🚧 In Progress
- [ ] Enhance platform export with missing fields (DatabaseID, ReleaseType, ratings, etc.)
- [ ] Generate playlist membership flags CSV

### 📋 Next Up (Phase 2)
- [ ] Auto-family detection script
- [ ] Manual family review tool
- [ ] FamilyKey assignment workflow

---

## Open Questions & Discussion Items

### 1. Family Detection Edge Cases
**Question:** How should we handle these scenarios?

#### Scenario A: Same Title, Different Games
- **Example:** Aladdin (SNES) vs Aladdin (Genesis)
- **LaunchBox:** Different DatabaseIDs (already distinguished)
- **Decision:** Trust DatabaseID; if missing, flag for manual review

#### Scenario B: Numbered Sequels
- **Example:** Super Mario Bros. 2 vs Super Mario Bros. 3
- **Decision:** Separate families (they're distinct games, not variants)
- **But:** "New Super Mario Bros. U" vs "New Super Mario Bros. U Deluxe" → same family

#### Scenario C: Bundles
- **Example:** "Super Mario Bros. + Duck Hunt"
- **Decision:** Separate family (it's a distinct release, not a variant of SMB1)

#### Scenario D: Enhanced Ports
- **Example:** "Super Mario Advance 4: Super Mario Bros. 3" (GBA port of NES game)
- **Decision:** Same family as "Super Mario Bros. 3" (it's a port/remaster)

**Proposed Rule:**
- Same DatabaseID → same family (trust LaunchBox)
- Different DatabaseID but similar title → flag for manual review
- User assigns FamilyKey manually for ambiguous cases

### 2. Platform Priority Strategy
**Question:** Should platform priority be:
- **Global ranking** (PS5 > PS4 > PS3 > PS2 > PS1)?
- **Era-based ranking** (within 8-bit, prefer NES; within 16-bit, prefer SNES)?
- **Hybrid** (global + era overrides)?

**Proposed:** Hybrid approach
- Define era categories (8-bit handheld, 8-bit console, 16-bit console, 32-bit, HD, modern)
- Rank platforms within each era
- For cross-era families (e.g., NES game remastered on Switch), use global ranking

### 3. Remaster Preference
**Question:** How to handle "prefer remaster" vs "prefer original"?

**Examples:**
- **Prefer remaster:** Metroid: Zero Mission (GBA) over Metroid (NES)
- **Prefer original:** Final Fantasy VI (SNES) over Final Fantasy VI Advance (GBA) — sprite changes controversial

**Proposed:**
- Global default setting (`prefer_remaster: true`)
- Per-family overrides via `ManualPreferred` column
- Heuristic: If user has original in "Favorites" playlist but remaster is not favorited → prefer original

### 4. Playlist Selection for Weighting
**Question:** With 1000+ playlists, which should influence selection?

**Proposed:**
- Config wizard asks user to select playlists to include
- Auto-suggest playlists with "Best", "GOTY", "Favorite", "Top" in name
- User assigns weights (0-100)

### 5. Manual Override Workflow
**Question:** Where should manual overrides live?

**Option A:** Columns in `master_inventory.csv`
- ✅ Simple, single source of truth
- ❌ Risk of accidental edits, large file

**Option B:** Separate `overrides.csv`
- ✅ Cleaner, safer
- ❌ Need to join during processing

**Option C:** LaunchBox custom fields
- ✅ Integrated with LaunchBox UI
- ❌ Requires XML parsing/writing, more complex

**Proposed:** Option A (columns in master CSV) for MVP, Option C for future enhancement

### 6. ES-DE Integration
**Question:** What's the ES-DE collection/gamelist format?

**TODO:**
- [ ] Research ES-DE documentation
- [ ] Examine sample ES-DE gamelist.xml files
- [ ] Determine artwork path mapping (LaunchBox → ES-DE)

### 7. Technology Stack
**Question:** Should this be Python or Node.js?

**Current:** Python
- ✅ Existing scripts are Python
- ✅ Great for CSV/XML processing
- ✅ Rich ecosystem (pandas, lxml, pyyaml)
- ❌ User is less familiar with Python

**Alternative:** Node.js
- ✅ User may be more comfortable
- ✅ Fast, good for file operations
- ❌ Would require rewriting existing scripts

**Proposed:** Stick with Python for MVP
- Scripts are simple, well-commented
- Can add interactive CLI tools (using `click` or `questionary` libraries)
- If user wants a web UI later, can build separate Node/React frontend that calls Python scripts

---

## Development Roadmap

### Milestone 1: Foundation (2 weeks)
- [ ] Enhance `export_all_platforms.py` to include all metadata fields
- [ ] Generate playlist membership flags CSV
- [ ] Update `build_master_inventory.py` to include new fields + LudisID + FamilyKey columns
- [ ] Validate master inventory completeness

### Milestone 2: Family Detection (2 weeks)
- [ ] Build `detect_families.py` (auto-assign FamilyKeys via DatabaseID)
- [ ] Build `review_families.py` (interactive manual review tool)
- [ ] Process full library, assign FamilyKeys to all entries
- [ ] Document family detection decisions

### Milestone 3: Preference Engine (2 weeks)
- [ ] Build `configure_ludis.py` (interactive config wizard)
- [ ] Build `select_preferred_editions.py` (scoring + selection algorithm)
- [ ] Generate `ludis_config.yaml` with user preferences
- [ ] Run selection, validate results

### Milestone 4: Export (2 weeks)
- [ ] Build `export_launchbox_playlists.py`
- [ ] Research ES-DE format
- [ ] Build `export_esde_collections.py`
- [ ] Build `generate_rom_symlinks.py`
- [ ] Test exports in LaunchBox and ES-DE

### Milestone 5: Refinement (ongoing)
- [ ] Add per-family override UI/workflow
- [ ] Add validation/reporting tools (detect missing artwork, broken paths, etc.)
- [ ] Add incremental update support (only reprocess changed entries)
- [ ] Add export profiles (different curated sets for different devices)

---

## File Structure

```
lb-game-exporter/
├── README.md
├── LUDIS_PROJECT_PLAN.md (this file)
├── ludis_config.yaml (generated by configure_ludis.py)
│
├── Data/ (LaunchBox data, read-only)
│   ├── Platforms/*.xml
│   ├── Playlists/*.xml
│   └── ... (other LaunchBox data)
│
├── LB_Exports/ (generated CSVs)
│   ├── all_platforms.csv
│   ├── all_playlists.csv
│   ├── playlist_flags.csv (NEW)
│   ├── master_inventory.csv
│   ├── families_to_review.csv (NEW)
│   ├── selection_report.csv (NEW)
│   └── audits/
│       └── inventory.csv
│
├── ludis_exports/ (NEW - final outputs)
│   ├── launchbox/
│   │   └── Playlists/
│   │       ├── Ludis - Curated.xml
│   │       ├── Ludis - Top Shelf.xml
│   │       └── Ludis - {Platform}.xml
│   ├── esde/
│   │   ├── collections/
│   │   └── gamelists/
│   └── curated_roms/ (symlinks)
│       ├── nes/
│       ├── snes/
│       └── ...
│
├── Scripts (existing)
│   ├── export_all_platforms.py
│   ├── export_all_playlists.py
│   ├── build_master_inventory.py
│   ├── find_c64_dupes.py
│   └── move_c64_kills.py
│
└── Scripts (NEW)
    ├── detect_families.py
    ├── review_families.py
    ├── configure_ludis.py
    ├── select_preferred_editions.py
    ├── export_launchbox_playlists.py
    ├── export_esde_collections.py
    └── generate_rom_symlinks.py
```

---

## Success Criteria

### MVP Success (End of Milestone 4)
- [ ] Master inventory includes all 35k+ titles with complete metadata
- [ ] All titles assigned to families (via DatabaseID or manual review)
- [ ] Preferred edition selected for each family
- [ ] LaunchBox "Ludis - Curated" playlist generated and functional
- [ ] Symlinked ROM folder structure created for at least one platform

### Long-Term Success
- [ ] User can re-run entire pipeline in < 5 minutes
- [ ] User can add new games and re-curate incrementally
- [ ] User can export curated collections to multiple devices (PC, Steam Deck, Retro handheld)
- [ ] User can override any automated decision via simple CSV edit
- [ ] System scales to 50k+ titles without performance issues

---

## Next Steps

1. **Review this plan** — discuss open questions, adjust priorities
2. **Enhance platform export** — add DatabaseID, ReleaseType, ratings fields
3. **Generate playlist flags CSV** — binary flags for key playlists
4. **Update master inventory** — include new fields + LudisID + FamilyKey columns
5. **Begin family detection** — start with DatabaseID matching

---

## Notes

- **DatabaseID is critical** — this is LaunchBox's internal Games Database ID, the best signal for "same game across platforms"
- **Aladdin edge case** — SNES and Genesis versions have different DatabaseIDs (they're different games), so auto-detection will correctly separate them
- **Super Mario Bros. complexity** — many variants, but most have distinct DatabaseIDs (bundles, ports, remasters); family detection will group correctly
- **Playlist integration** — existing "NES The Best" etc. playlists are gold; use them as input signals, not just output targets
- **Manual overrides are essential** — no algorithm is perfect; user must be able to override any decision easily

---

**End of Project Plan**

