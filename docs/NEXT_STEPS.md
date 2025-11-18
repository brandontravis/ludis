# Ludis - Next Steps

## Overview

This document outlines the validation and enhancement tasks needed to complete the Ludis pipeline.

---

## Phase 1: Pipeline Validation ✓ (In Progress)

### 1.1 Test Each Pipeline Step

**Goal:** Verify each step runs without errors and produces expected output.

#### Step 1: Filesystem Scan
- [ ] Run `python3 ludis.py` → "Build Ludis Library"
- [ ] Verify `LB_Exports/audits/nas_inventory.csv` is created
- [ ] Check row count matches expected game files on disk
- [ ] Verify columns: `Filename`, `RelPath`, `Platform`, `Title`, `Ext`
- [ ] Spot-check 5-10 random rows for accuracy

#### Step 2: Platform Export
- [ ] Verify `LB_Exports/all_platforms.csv` is created
- [ ] Check row count matches total games in LaunchBox
- [ ] Verify all 24 columns are present (Platform, Title, Developer, etc.)
- [ ] Check individual platform CSVs in `LB_Exports/platforms/`
- [ ] Verify custom fields are included (see 1.2 below)

#### Step 3: Playlist Export
- [ ] Verify `LB_Exports/all_playlists.csv` is created
- [ ] Check that filtered playlists are excluded (genre, region, etc.)
- [ ] Verify categorized playlists have correct prefixes (BEST_, FRANCHISE_, etc.)
- [ ] Check individual playlist CSVs in `LB_Exports/playlists/`
- [ ] Verify filter-based playlists are correctly materialized (e.g., "The Best")

#### Step 4: Master Inventory Build
- [x] Verify `LB_Exports/master_inventory.csv` is created
- [x] Check column order: Platform (first), Filename, metadata, file paths (last)
- [ ] Verify row count = matched + unmatched + lb_only
- [ ] Check `Matched` column values (Yes/No)
- [ ] Check `MatchType` column values (exact/normalized/parent/lb_only/unmatched)
- [ ] Spot-check file path matching accuracy

#### Step 5: Playlist Enrichment
- [ ] Verify new columns are added to `master_inventory.csv`:
  - `IsPlatformBest` (Boolean)
  - `IsInFranchise` (Boolean)
  - `Franchises` (semicolon-separated)
  - `IsInCurated` (Boolean)
  - `CuratedPlaylists` (semicolon-separated)
  - `IsInClassicCollection` (Boolean)
  - `PlaylistCount` (Integer)
- [ ] Verify games in "The Best" playlists have `IsPlatformBest=True`
- [ ] Verify franchise playlists populate `Franchises` correctly
- [ ] Check `PlaylistCount` accuracy for 5-10 random games

---

### 1.2 Custom Field Validation

**Goal:** Ensure custom fields from LaunchBox are correctly extracted and carried through the pipeline.

#### Known Custom Fields:
- `CUSTOM_The Best`
- `CUSTOM_GOTY Winner`
- `CUSTOM_GOTY Nominee`
- `CUSTOM_Backlog`
- `CUSTOM_Play It Again`
- `CUSTOM_On Deck`
- (Add others as discovered)

#### Validation Steps:
- [ ] Check `all_platforms.csv` for custom field columns
- [ ] Verify custom field values match LaunchBox UI
- [ ] Test filter-based playlists that use custom fields (e.g., "The Best")
- [ ] Verify custom fields are preserved in `master_inventory.csv`
- [ ] Document all custom fields in use

#### Test Cases:
1. **"The Best" Playlists:**
   - [ ] Pick a game marked "The Best" in LaunchBox
   - [ ] Verify `CUSTOM_The Best=true` in `all_platforms.csv`
   - [ ] Verify game appears in corresponding "X The Best" playlist CSV
   - [ ] Verify `IsPlatformBest=True` in `master_inventory.csv`

2. **GOTY Fields:**
   - [ ] Pick a GOTY winner/nominee in LaunchBox
   - [ ] Verify `CUSTOM_GOTY Winner` or `CUSTOM_GOTY Nominee` in exports
   - [ ] Verify game appears in GOTY playlists

3. **Backlog/Progress Fields:**
   - [ ] Verify `CUSTOM_Backlog`, `CUSTOM_Play It Again`, `CUSTOM_On Deck` export correctly
   - [ ] Check if these should be included in curated playlists

---

### 1.3 Data Integrity Checks

**Goal:** Verify data consistency across all pipeline steps.

- [ ] **No Data Loss:** Row count in `master_inventory.csv` ≥ row count in `all_platforms.csv`
- [ ] **No Duplicate LBIDs:** Check for duplicate `LBID` values in `master_inventory.csv`
- [ ] **File Matching Accuracy:**
  - [ ] Calculate match rate: `Matched=Yes` / total rows
  - [ ] Investigate unmatched games (expected vs. unexpected)
  - [ ] Verify `lb_only` games are truly not on disk
- [ ] **Playlist Membership Accuracy:**
  - [ ] Pick 5 games from different playlists
  - [ ] Verify `PlaylistCount` matches manual count
  - [ ] Verify `Franchises` and `CuratedPlaylists` lists are complete
- [ ] **Platform Consistency:**
  - [ ] Verify all platform names are normalized consistently
  - [ ] Check for platform name mismatches between LaunchBox and filesystem

---

### 1.4 Edge Case Testing

**Goal:** Test unusual scenarios and edge cases.

- [ ] **Empty Playlists:** Verify empty playlists don't break export
- [ ] **Special Characters:** Test games with special chars in titles/filenames
- [ ] **Multi-disc Games:** Verify multi-disc sets are handled correctly
- [ ] **Parent/Clone Relationships:** Check parent ROM matching logic
- [ ] **Missing Files:** Test games in LaunchBox but not on disk
- [ ] **Orphan Files:** Test files on disk but not in LaunchBox
- [ ] **Custom Field Edge Cases:**
  - [ ] Games with multiple custom fields
  - [ ] Games with no custom fields
  - [ ] Custom fields with special values (empty, null, etc.)

---

### 1.5 Performance Benchmarks

**Goal:** Document pipeline performance for future optimization.

- [ ] Time each pipeline step
- [ ] Record total pipeline runtime
- [ ] Note any slow operations (> 30 seconds)
- [ ] Document system specs (CPU, RAM, disk type)
- [ ] Identify bottlenecks for future optimization

**Benchmark Template:**
```
System: [CPU, RAM, Disk]
Total Games: [count]
Total Platforms: [count]
Total Playlists: [count]

Step 1 - Filesystem Scan:     [XX:XX]
Step 2 - Platform Export:      [XX:XX]
Step 3 - Playlist Export:      [XX:XX]
Step 4 - Master Inventory:     [XX:XX]
Step 5 - Playlist Enrichment:  [XX:XX]
─────────────────────────────────────
Total Pipeline Runtime:        [XX:XX]
```

---

## Phase 2: Data Quality Validation ✓ (Pending Phase 1)

### 2.1 Custom Field Audit

**Goal:** Comprehensive audit of all custom fields in use.

- [ ] List all custom fields in LaunchBox
- [ ] Document purpose of each custom field
- [ ] Verify each field exports correctly
- [ ] Check for unused/deprecated custom fields
- [ ] Document which playlists use which custom fields

### 2.2 Playlist Categorization Review

**Goal:** Verify playlist categorization is correct.

- [ ] Review all `BEST_*` playlists - confirm they use `CUSTOM_The Best`
- [ ] Review all `FRANCHISE_*` playlists - confirm they're actual franchises
- [ ] Review all `CURATED_*` playlists - confirm they're manually curated
- [ ] Review all `CLASSIC_*` playlists - confirm they're classic console collections
- [ ] Check for miscategorized playlists
- [ ] Document any playlists that need recategorization

### 2.3 File Matching Quality

**Goal:** Improve file matching accuracy.

- [ ] Review unmatched games (Matched=No)
- [ ] Identify patterns in matching failures
- [ ] Update `SUBPATH_OVERRIDES` if needed
- [ ] Test parent ROM matching logic
- [ ] Consider fuzzy matching for edge cases
- [ ] Document known matching limitations

### 2.4 Metadata Completeness

**Goal:** Identify and fill metadata gaps.

- [ ] Check for games with missing `Developer`
- [ ] Check for games with missing `Publisher`
- [ ] Check for games with missing `ReleaseDate`
- [ ] Check for games with missing `Genre`
- [ ] Identify games that should be marked "The Best" but aren't
- [ ] Document metadata cleanup tasks for LaunchBox

---

## Phase 3: Feature Enhancements 🚀 (Future)

### 3.1 Symlink Generator

**Goal:** Create symlinks for curated game collections.

#### Requirements:
- Read `master_inventory.csv`
- Filter games based on criteria (e.g., `IsPlatformBest=True`, `IsInFranchise=True`)
- Create directory structure for target system (ES-DE, Steam Deck, etc.)
- Generate symlinks from source files to target directories
- Handle multi-file games (e.g., .cue + .bin)
- Support dry-run mode (preview without creating)

#### Design Considerations:
- **Target Systems:**
  - ES-DE on Linux/Mac
  - Steam Deck (Linux)
  - Batocera
  - RetroPie
  - Custom directory structure
  
- **Filtering Options:**
  - By platform
  - By playlist membership
  - By custom fields
  - By rating threshold
  - By release date range
  - Combination of filters

- **Symlink Strategies:**
  - Flat structure (all games in one folder per platform)
  - Hierarchical (by franchise, genre, etc.)
  - Playlist-based (mirror LaunchBox playlists)

#### Implementation Plan:
1. [ ] Create `scripts/generate_symlinks.py`
2. [ ] Add filter configuration to `config.yaml`
3. [ ] Implement dry-run mode
4. [ ] Add progress bars for large collections
5. [ ] Handle errors gracefully (permission issues, disk space, etc.)
6. [ ] Create validation report (broken symlinks, missing files)
7. [ ] Add to ludis.py menu as optional step
8. [ ] Document usage in README

#### Example Usage:
```bash
# Generate symlinks for "The Best" games only
python3 scripts/generate_symlinks.py --filter IsPlatformBest=True --target /path/to/esde

# Generate symlinks for specific platforms
python3 scripts/generate_symlinks.py --platforms "Nintendo 64,Sony Playstation" --target /path/to/deck

# Dry run to preview
python3 scripts/generate_symlinks.py --filter IsPlatformBest=True --dry-run
```

---

### 3.2 ES-DE Playlist Export

**Goal:** Export LaunchBox playlists to ES-DE custom collection format.

#### Requirements:
- Read categorized playlists from `LB_Exports/playlists/`
- Convert to ES-DE `.txt` collection format
- Map LaunchBox platform names to ES-DE system names
- Generate `collections/` directory structure
- Support automatic vs. custom collections

#### ES-DE Collection Format:
```
# ES-DE Custom Collection
# Collection: The Best - Nintendo 64
/path/to/game1.z64
/path/to/game2.z64
```

#### Implementation Plan:
1. [ ] Create `scripts/export_esde_collections.py`
2. [ ] Map LaunchBox platforms to ES-DE system names
3. [ ] Add ES-DE path configuration to `config.yaml`
4. [ ] Generate collection metadata files
5. [ ] Support collection themes/artwork
6. [ ] Add to ludis.py menu
7. [ ] Test with actual ES-DE installation

---

### 3.3 Steam Deck Integration

**Goal:** Generate Steam ROM Manager configurations.

#### Requirements:
- Export game lists in Steam ROM Manager format
- Map platforms to emulators
- Generate artwork paths
- Support Steam Deck file paths

#### Implementation Plan:
1. [ ] Research Steam ROM Manager config format
2. [ ] Create `scripts/export_steam_deck.py`
3. [ ] Add emulator mapping configuration
4. [ ] Test on actual Steam Deck
5. [ ] Document installation process

---

### 3.4 Playlist Sync Back to LaunchBox

**Goal:** Create/update LaunchBox playlists from external edits.

#### Use Case:
User edits `master_inventory.csv` to mark games as "The Best" or add to franchises, then syncs back to LaunchBox.

#### Requirements:
- Read modified `master_inventory.csv`
- Compare with current LaunchBox data
- Generate LaunchBox playlist XML updates
- Update custom fields in platform XMLs
- Backup before making changes

#### Implementation Plan:
1. [ ] Create `scripts/sync_to_launchbox.py`
2. [ ] Implement diff detection
3. [ ] Generate XML updates
4. [ ] Add backup/restore functionality
5. [ ] Add to ludis.py menu
6. [ ] **CRITICAL:** Test extensively before running on real data

---

### 3.5 Web UI (Future Vision)

**Goal:** Browser-based interface for Ludis management.

#### Features:
- View/search `master_inventory.csv`
- Edit custom fields and playlist membership
- Preview symlink generation
- Run pipeline steps
- View statistics and reports
- Manage configuration

#### Tech Stack Ideas:
- Backend: Flask/FastAPI
- Frontend: React/Vue/Svelte
- Database: SQLite (import CSV on startup)
- Real-time updates via WebSocket

#### Implementation Plan:
- [ ] Phase 1: Read-only web viewer
- [ ] Phase 2: Add editing capabilities
- [ ] Phase 3: Pipeline execution from UI
- [ ] Phase 4: Advanced filtering and reporting

---

### 3.6 Advanced Filtering & Reporting

**Goal:** Generate reports and filtered exports from master inventory.

#### Report Ideas:
- **Collection Statistics:**
  - Games per platform
  - "The Best" games count
  - Franchise coverage
  - Completion percentage
  - Rating distributions
  
- **Quality Reports:**
  - Games missing metadata
  - Games missing artwork
  - Unmatched files
  - Duplicate detection
  
- **Curation Reports:**
  - Platform "The Best" coverage (% of library)
  - Franchise completeness
  - GOTY coverage
  - Hidden gems (high rating, not in "The Best")

#### Implementation Plan:
1. [ ] Create `scripts/generate_reports.py`
2. [ ] Add report templates
3. [ ] Support HTML/Markdown/CSV output
4. [ ] Add charts/visualizations
5. [ ] Add to ludis.py menu

---

### 3.7 Multi-Version Management

**Goal:** Handle multiple versions of the same game intelligently.

#### Use Cases:
- USA vs. Europe vs. Japan releases
- Original vs. Remaster vs. Remake
- Physical vs. Digital editions
- Different ROM formats (z64 vs. n64 vs. v64)

#### Features:
- Detect game families (same title, different regions/versions)
- Auto-select "preferred version" based on rules:
  - Region preference (USA > Europe > Japan)
  - Format preference (z64 > n64)
  - Remaster vs. Original preference
- Flag remasters/remakes in metadata
- Link related versions together

#### Implementation Plan:
1. [ ] Add version detection logic
2. [ ] Implement preference rules in `config.yaml`
3. [ ] Add `PreferredVersion` column to master inventory
4. [ ] Create `GameFamily` grouping
5. [ ] Add manual override support

---

## Phase 4: Documentation & Polish 📚

### 4.1 User Documentation

- [ ] Complete `docs/LUDIS_README.md`
- [ ] Create quick start guide
- [ ] Document all configuration options
- [ ] Add troubleshooting section
- [ ] Create video walkthrough (optional)

### 4.2 Developer Documentation

- [ ] Document code architecture
- [ ] Add inline code comments
- [ ] Create API documentation
- [ ] Document data flow diagrams
- [ ] Add contributing guidelines

### 4.3 Testing & CI/CD

- [ ] Create unit tests for core functions
- [ ] Add integration tests for pipeline
- [ ] Set up GitHub Actions (if applicable)
- [ ] Add code quality checks (linting, formatting)

### 4.4 Packaging & Distribution

- [ ] Create `requirements.txt` with pinned versions
- [ ] Add `setup.py` for pip installation
- [ ] Create Docker container (optional)
- [ ] Publish to PyPI (optional)
- [ ] Create release process

---

## Immediate Next Steps (This Week)

### Priority 1: Validation
1. [ ] Run full pipeline and verify each step completes
2. [ ] Check custom fields are exporting correctly
3. [ ] Verify playlist categorization is accurate
4. [ ] Test file matching accuracy
5. [ ] Document any issues found

### Priority 2: Bug Fixes
1. [ ] Fix any issues discovered in validation
2. [ ] Update documentation with findings
3. [ ] Test hierarchical menu system in real terminal

### Priority 3: Planning
1. [ ] Review Phase 3 features and prioritize
2. [ ] Decide on first enhancement to implement
3. [ ] Create detailed design doc for chosen feature

---

## Success Criteria

### Phase 1 Complete When:
- ✓ All pipeline steps run without errors
- ✓ All custom fields export correctly
- ✓ Playlist categorization is accurate
- ✓ File matching rate > 95%
- ✓ Data integrity checks pass
- ✓ Performance benchmarks documented

### Phase 2 Complete When:
- ✓ All custom fields documented
- ✓ All playlists correctly categorized
- ✓ Metadata completeness > 90%
- ✓ Known limitations documented

### Phase 3 Complete When:
- ✓ At least 2 major features implemented
- ✓ Features tested and documented
- ✓ User feedback incorporated

---

## Questions to Resolve

1. **Custom Fields:**
   - What custom fields are currently in use?
   - Are there deprecated fields to remove?
   - Should we add new custom fields?

2. **Playlist Strategy:**
   - Are current playlist categories sufficient?
   - Should we add more categories?
   - How to handle overlapping playlists?

3. **File Matching:**
   - What's an acceptable match rate?
   - How to handle multi-file games?
   - Should we support fuzzy matching?

4. **Target Systems:**
   - Which systems to prioritize for export?
   - ES-DE, Steam Deck, or both?
   - Other systems to support?

5. **Symlink Strategy:**
   - Flat or hierarchical structure?
   - How to organize by franchise?
   - How to handle multi-platform franchises?

---

## Notes

- Keep this document updated as work progresses
- Mark items complete with `[x]` when done
- Add new sections as needed
- Document decisions and rationale
- Track blockers and dependencies

---

**Last Updated:** November 15, 2025  
**Status:** Phase 1 - Pipeline Validation (In Progress)  
**Next Review:** After Phase 1 validation complete

