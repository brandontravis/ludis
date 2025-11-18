# Ludis Validation Checklist

Quick reference checklist for validating the Ludis pipeline.

---

## Pre-Flight Check

- [ ] `config.yaml` exists and has correct paths
- [ ] LaunchBox `Data/` directory accessible
- [ ] Game library filesystem accessible
- [ ] Dependencies installed (`pyyaml`, `inquirer`, `tqdm`)

---

## Step 1: Filesystem Scan

**Command:** Run ludis.py → "Build Ludis Library" (or "Re-run from: Filesystem Scan")

### Checks:
- [ ] `LB_Exports/audits/nas_inventory.csv` created
- [ ] File has 5 columns: `Filename`, `RelPath`, `Platform`, `Title`, `Ext`
- [ ] Row count seems reasonable (matches expected game count)

### Spot Check (pick 3-5 random rows):
| Filename | RelPath | Platform | Title | Ext |
|----------|---------|----------|-------|-----|
| ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |

**Notes:**
```
[Any issues or observations]
```

---

## Step 2: Platform Export

**Output:** `LB_Exports/all_platforms.csv` + `LB_Exports/platforms/*.csv`

### Checks:
- [ ] `all_platforms.csv` created
- [ ] Has 24+ columns (Platform, Title, Developer, Publisher, etc.)
- [ ] Row count matches LaunchBox game count
- [ ] Individual platform CSVs created (54 files)

### Custom Fields Check:
Open `all_platforms.csv` and verify these columns exist:
- [ ] `CUSTOM_The Best`
- [ ] `CUSTOM_GOTY Winner`
- [ ] `CUSTOM_GOTY Nominee`
- [ ] `CUSTOM_Backlog`
- [ ] `CUSTOM_Play It Again`
- [ ] `CUSTOM_On Deck`
- [ ] Other: _______________

### Spot Check (pick 1 game you know is marked "The Best"):
- Game: _______________
- Platform: _______________
- `CUSTOM_The Best` value: _______________
- [ ] Value matches LaunchBox UI

**Notes:**
```
[Any issues or observations]
```

---

## Step 3: Playlist Export

**Output:** `LB_Exports/all_playlists.csv` + `LB_Exports/playlists/*.csv`

### Checks:
- [ ] `all_playlists.csv` created
- [ ] Has 4 columns: `Playlist`, `Platform`, `Title`, `LBID`
- [ ] Individual playlist CSVs created (~100-200 files)

### Categorization Check:
Count files by prefix:
- `BEST_*.csv`: _____ files
- `FRANCHISE_*.csv`: _____ files
- `CURATED_*.csv`: _____ files
- `CLASSIC_*.csv`: _____ files
- `OTHER_*.csv`: _____ files

### Exclusion Check (these should NOT exist):
- [ ] No genre playlists (e.g., "Action.csv", "RPG.csv")
- [ ] No "All Games" playlists
- [ ] No "Favorites" playlists
- [ ] No "The Rest" playlists
- [ ] No region playlists (e.g., "USA.csv", "Japan.csv")

### Spot Check - "The Best" Playlists:
Pick one "The Best" playlist (e.g., `BEST_Nintendo 64 The Best.csv`):
- Playlist: _______________
- Row count: _______________
- [ ] All games in this playlist have `CUSTOM_The Best=true` in `all_platforms.csv`

### Spot Check - Franchise Playlists:
Pick one franchise (e.g., `FRANCHISE_Mario.csv`):
- Playlist: _______________
- Row count: _______________
- [ ] Games look correct (spot check 3-5 titles)

**Notes:**
```
[Any issues or observations]
```

---

## Step 4: Master Inventory Build

**Output:** `LB_Exports/master_inventory.csv`

### Checks:
- [ ] `master_inventory.csv` created
- [ ] First column is `Platform`
- [ ] Second column is `Filename`
- [ ] Last 4 columns are `RelPath`, `LBFilePath`, `NASPath`, `FileExtension`

### Column Count:
- Expected: 34 columns
- Actual: _____ columns

### Row Counts:
- Total rows: _____
- `Matched=Yes`: _____
- `Matched=No`: _____
- Match rate: _____% (should be > 90%)

### Match Type Distribution:
- `MatchType=exact`: _____
- `MatchType=normalized`: _____
- `MatchType=parent`: _____
- `MatchType=lb_only`: _____
- `MatchType=unmatched`: _____

### Spot Check (pick 5 random rows):
| Platform | Filename | Matched | MatchType | RelPath | Notes |
|----------|----------|---------|-----------|---------|-------|
| | | ✓/✗ | | ✓/✗ | |
| | | ✓/✗ | | ✓/✗ | |
| | | ✓/✗ | | ✓/✗ | |
| | | ✓/✗ | | ✓/✗ | |
| | | ✓/✗ | | ✓/✗ | |

**Notes:**
```
[Any issues or observations]
```

---

## Step 5: Playlist Enrichment

**Output:** Updated `LB_Exports/master_inventory.csv`

### New Columns Check:
- [ ] `IsPlatformBest`
- [ ] `IsInFranchise`
- [ ] `Franchises`
- [ ] `IsInCurated`
- [ ] `CuratedPlaylists`
- [ ] `IsInClassicCollection`
- [ ] `PlaylistCount`

### Spot Check - "The Best" Games:
Pick 3 games you know are marked "The Best":

**Game 1:**
- Title: _______________
- Platform: _______________
- `IsPlatformBest`: _____ (should be `True`)
- `PlaylistCount`: _____ (should be > 0)

**Game 2:**
- Title: _______________
- Platform: _______________
- `IsPlatformBest`: _____ (should be `True`)
- `PlaylistCount`: _____ (should be > 0)

**Game 3:**
- Title: _______________
- Platform: _______________
- `IsPlatformBest`: _____ (should be `True`)
- `PlaylistCount`: _____ (should be > 0)

### Spot Check - Franchise Games:
Pick 1 game in a franchise (e.g., "Super Mario 64"):
- Title: _______________
- Platform: _______________
- `IsInFranchise`: _____ (should be `True`)
- `Franchises`: _______________
- [ ] Franchise name looks correct

### Spot Check - Playlist Count:
Pick 1 game and manually count its playlists:
- Title: _______________
- Manual count: _____
- `PlaylistCount` value: _____
- [ ] Values match

**Notes:**
```
[Any issues or observations]
```

---

## Performance Benchmark

Record timing for each step:

| Step | Duration | Notes |
|------|----------|-------|
| 1. Filesystem Scan | _____ | |
| 2. Platform Export | _____ | |
| 3. Playlist Export | _____ | |
| 4. Master Inventory | _____ | |
| 5. Playlist Enrichment | _____ | |
| **Total** | **_____** | |

**System Info:**
- CPU: _______________
- RAM: _______________
- Disk: _______________
- Total Games: _____
- Total Platforms: _____
- Total Playlists: _____

---

## Issues Found

### Critical (Blocks Usage):
```
1. 
2. 
3. 
```

### Major (Affects Accuracy):
```
1. 
2. 
3. 
```

### Minor (Cosmetic/Nice-to-have):
```
1. 
2. 
3. 
```

---

## Overall Status

- [ ] ✅ **PASS** - All checks passed, ready for production use
- [ ] ⚠️ **PASS WITH ISSUES** - Works but has known limitations
- [ ] ❌ **FAIL** - Critical issues found, needs fixes

**Summary:**
```
[Overall assessment of pipeline health]
```

---

## Next Actions

1. 
2. 
3. 

---

**Validation Date:** _______________  
**Validated By:** _______________  
**Ludis Version:** 1.0.0

