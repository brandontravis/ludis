# Phase 4 Completion Plan

## Critical Issue: audit_library.py

The `scripts/audit_library.py` file contains extensive hardcoding specific to your system that MUST be refactored before public release.

### Hardcoded Elements

1. **Lines 13-14:** WIN_ROOT and NAS_ROOT hardcoded paths
2. **Lines 86-109:** SPECIAL_RULES dictionary with your specific folder structure
3. **Lines 111-120:** PER_GAME_SUBFOLDER_PLATFORMS set with your folder paths
4. **Lines 124-130:** SUBPATH_OVERRIDES for your naming conventions
5. **Lines 135-188:** ESDE_SLUG_MAP with hardcoded folder paths
6. **Lines 220-242:** Fuzzy matching that assumes NAS_ROOT structure

### Solution: Complete Rewrite Required

The `audit_library.py` script needs to be completely rewritten to:

1. Load all paths from `config.yaml` (library_roots)
2. Auto-detect file types by extension (no hardcoded platform structures)
3. Simple recursive scanning without complex rules
4. Use normalized path resolution from LaunchBox XML to library_roots

### Proposed New Architecture

```python
def scan_library_roots(library_roots: List[str], known_extensions: Set[str]) -> Dict:
    """
    Simple generic scan:
    1. Walk each library_root recursively
    2. Find files matching known_extensions  
    3. Calculate sizes (file or folder with du)
    4. Return {relative_path: {size, type}}
    """
    
def match_csv_to_scanned(csv_data: List[Dict], scanned_files: Dict) -> List[Dict]:
    """
    Match LaunchBox entries to scanned files:
    1. Extract relative path from LBFilePath
    2. Fuzzy match against scanned_files keys
    3. Assign FileSize and NASPath
    """
```

### Implementation Steps

#### Step 1: Create audit_library_v2.py (Generic Version)

- [x] Load config from config.yaml
- [ ] Simple recursive file scanning
- [ ] Extension-based file type detection
- [ ] No platform-specific rules
- [ ] Fuzzy path matching only

#### Step 2: Test With Multiple Users' Libraries

- [ ] Test on at least 3 different LaunchBox installations
- [ ] Verify all file types detected
- [ ] Check path resolution accuracy
- [ ] Validate performance

#### Step 3: Replace audit_library.py

- [ ] Backup old version
- [ ] Deploy new version
- [ ] Update ludis.py to use new scanner
- [ ] Update documentation

### Temporary Workaround

**For immediate use:** Users can manually edit lines 13-14 in `audit_library.py`:

```python
# Edit these lines to match YOUR system:
WIN_ROOT = r"YOUR_WINDOWS_PATH"  # From LaunchBox XML
LIBRARY_ROOTS = ["YOUR_ACTUAL_PATH"]  # Where files really are
```

However, this still requires:
- Configuring SPECIAL_RULES for their platforms
- Setting up SUBPATH_OVERRIDES for naming mismatches
- Understanding Python dict syntax

**This is NOT acceptable for public release.**

### Alternative: Skip Filesystem Scanning

Users can disable filesystem scanning in config.yaml:

```yaml
options:
  scan_filesystem: false
```

This allows Ludis to work in **metadata-only mode**:
- ✅ Extract platforms and playlists from XML
- ✅ Build master inventory
- ✅ Configure migrations
- ❌ No file size calculations
- ❌ No file existence validation
- ❌ Migration scripts will fail if paths are wrong

**This reduces Ludis functionality significantly.**

### Recommended Path Forward

1. **Immediate (Today):**
   - Add clear warning in README about audit_library.py hardcoding
   - Document the temporary manual edit workaround
   - Add `scan_filesystem: false` recommendation for new users

2. **Short-term (Next 2-3 days):**
   - Implement audit_library_v2.py with generic scanning
   - Test with multiple libraries
   - Deploy as default

3. **Long-term (Next week):**
   - Implement platform structure configurator UI
   - Allow users to define complex platform rules interactively
   - Save to config.yaml's platform_structure section

### Files That Need audit_library.py

- `ludis.py` - Calls as part of filesystem scan step
- `build_master_inventory.py` - Reads nas_inventory.csv output

Without fixing this, Ludis **cannot** be released publicly.

### Estimated Effort

- **audit_library_v2.py rewrite:** 4-6 hours
- **Testing with multiple libraries:** 2-3 hours  
- **Integration and documentation:** 1-2 hours

**Total:** 7-11 hours

### Status

- Started: 2025-11-20
- Status: **BLOCKED - Critical blocker for public release**
- Priority: **P0 - Must fix before any release**

---

## What HAS Been Genericized ✅

Everything else in Ludis is now fully generic:

- ✅ Setup wizard (multi-library support)
- ✅ Export platform scripts (dynamic custom fields)
- ✅ Playlist handling (no hardcoded categories)
- ✅ Filter system (playlist-based)
- ✅ Windows game detection (storefront/manual)
- ✅ Validation reports
- ✅ Migration builder
- ✅ Documentation

**Only audit_library.py remains hardcoded.**

Once this is fixed, Ludis will be 100% generic and ready for public use.

