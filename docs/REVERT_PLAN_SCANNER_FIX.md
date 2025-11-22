# Scanner Performance Fix - Revert Plan

## Current Situation

The scanner has been running for 15+ minutes (should be 2-4 minutes). The performance regression was introduced when trying to make `audit_library.py` use config-driven platform detection instead of hardcoded rules.

**Current Branch:** `wip-interactive-scanner`
**Last Working Commit:** `232ff8c` - "feat: Complete ROM migration system with ES-DE integration"
**Problem Commits:** `8d93a14`, `0335899`, `44a80ff` (current HEAD)

---

## Safe Revert Strategy

### Step 1: Backup Current Config (CRITICAL!)

Your `config.yaml` now has valuable `platform_structure` data (50 platforms configured) that took time to discover. **SAVE THIS FIRST!**

```bash
cd /Users/brandon.travis/Development/lb-game-exporter

# Backup current config with platform_structure
cp config.yaml config.yaml.v2-with-platform-structure

# Also save the updated sample
cp config.yaml.sample config.yaml.sample.v2

# Verify backups exist
ls -lh config.yaml.v2-with-platform-structure
ls -lh config.yaml.sample.v2
```

### Step 2: Commit Current WIP Work

Save all the work in the branch so we can reference it later:

```bash
# Stage all changes
git add -A

# Commit with detailed message
git commit -m "WIP: Scanner performance debugging (still broken - saving for reference)

Includes:
- interactive_scanner.py for platform structure discovery
- platform_structure section in config.yaml (50 platforms configured)
- Modified audit_library.py to use config-driven rules (SLOW - needs redesign)

Key innovation: config.yaml platform_structure caching works great!
Implementation: Scanner integration needs complete rewrite for performance.

Preserving for future reference on what to keep vs. what to redesign."

# Verify commit
git log --oneline -1
```

### Step 3: Revert Master to Working Commit

```bash
# Switch back to master branch
git checkout master

# Hard reset to last working commit
git reset --hard 232ff8c

# Verify we're back to the working state
git log --oneline -5

# Should show:
# 232ff8c feat: Complete ROM migration system with ES-DE integration
# 5f3ea05 Initial commit: LUDIS v1.0.0
```

### Step 4: Restore platform_structure Config

After reverting, your `config.yaml` will be the old version. You need to restore the `platform_structure` section:

**Option A: Manual Merge (Safest)**

1. Open both files side-by-side:
   - `config.yaml` (current, reverted version)
   - `config.yaml.v2-with-platform-structure` (backup)

2. Copy ONLY the `platform_structure` section from backup to current

3. Verify your paths are still correct

**Option B: Use New Config Entirely**

If your paths haven't changed:

```bash
cp config.yaml.v2-with-platform-structure config.yaml
```

Then verify the config loads:

```bash
python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

### Step 5: Test That Everything Works Again

```bash
# Run the working scanner
python3 ludis.py

# Select: "Build Ludis Library (run all steps)"
# Should complete in ~2-4 minutes
```

---

## What's Preserved in the WIP Branch

The `wip-interactive-scanner` branch contains:

### Good Code (To Keep)
- ✅ `scripts/interactive_scanner.py` - Platform structure discovery UI
- ✅ `platform_structure` config schema in YAML
- ✅ Discovery workflow (ask files vs folders, auto-check)
- ✅ Config caching mechanism

### Bad Code (To Discard)
- ❌ Modified `audit_library.py` with config-driven rules (too slow)
- ❌ Modified `ludis.py` scanner integration (caused performance issues)
- ❌ Changed `scan_library()` function (broke hot path)

### To Reference Later

```bash
# View the WIP branch without checking it out
git log wip-interactive-scanner --oneline

# See all changes between working and WIP
git diff 232ff8c wip-interactive-scanner

# Extract specific files from WIP
git show wip-interactive-scanner:scripts/interactive_scanner.py > /tmp/interactive_scanner_reference.py
git show wip-interactive-scanner:config.yaml > /tmp/config_with_platform_structure.yaml
```

---

## What We Learned

### What Worked ✅

1. **Interactive Platform Structure Discovery**
   - Asking user about files vs. folders per platform
   - Auto-checking based on first 5 items
   - Saving discovered structure to config

2. **Config Schema Design**
   ```yaml
   platform_structure:
     "MAME 0.256 Romset Merged":
       path: /Volumes/.../Arcade/MAME 0.256 Romset Merged
       type: files
     "MS-DOS [1981]":
       path: /Volumes/.../Computers/MS-DOS [1981]
       type: folders
   ```

3. **Caching Mechanism**
   - First run: interactive discovery (~2 min)
   - Subsequent runs: use cached structure (instant)

### What Failed ❌

1. **Modifying Old Scanner**
   - The old `audit_library.py` is a performance-tuned beast
   - Every change we made broke something:
     - Added dict lookups in hot loop
     - Changed pruning logic
     - Added extra checks on file collection
     - Multiple `os.walk()` calls instead of one

2. **Integration Approach**
   - Tried to retrofit config-driven rules into old code
   - Should have created clean new implementation instead
   - "Don't fix what ain't broke" - we broke it by fixing it

### Root Causes of Slowdown

1. **Multiple `os.walk()` calls** - Scanning 4 category folders separately instead of one unified walk
2. **Dict lookups in file loop** - Checking `PLATFORM_RULES` for every file
3. **Incorrect pruning** - Not stopping descent at platform boundaries
4. **Over-engineering** - Added complexity where old code was simple

---

## The Right Way Forward (Next Attempt)

### Don't Touch These Files
- ❌ `scripts/audit_library.py` - Keep as fast working baseline
- ❌ `ludis.py` scanner integration - Keep using old scanner

### Create These New Files

#### 1. `scripts/generic_scanner.py` (New, Clean Implementation)

```python
"""
Generic filesystem scanner using platform_structure from config.

Design goals:
- Read platform_structure from config.yaml
- Single os.walk() from common parent
- Simple dict lookup for platform detection
- Fast pruning at platform boundaries
- NO legacy code baggage
"""

def scan_library_generic(config: dict) -> dict:
    """
    Scan using config-driven platform structure.
    
    Returns: {relative_path: {size, type}}
    """
    pass
```

#### 2. Make It Optional

```yaml
# config.yaml
options:
  use_generic_scanner: false  # Default to old working scanner
```

```python
# ludis.py
if config.get('options', {}).get('use_generic_scanner', False):
    # Use new generic scanner
    result = subprocess.run([sys.executable, "scripts/generic_scanner.py"])
else:
    # Use proven fast scanner
    result = subprocess.run([sys.executable, "scripts/audit_library.py", "nas-inventory"])
```

### Incremental Migration Path

1. **Phase A:** Revert to working code ✅
2. **Phase B:** Create `generic_scanner.py` from scratch
3. **Phase C:** Test side-by-side (both scanners on same library)
4. **Phase D:** Once new scanner is proven fast, make it default
5. **Phase E:** Eventually deprecate old scanner

**Benefits:**
- Production stays working
- New users can opt-in to test generic scanner
- No risk of breaking everything again
- Clean separation allows A/B testing

---

## Key Files and Backups

After running this revert plan, you'll have:

### Active (Post-Revert)
- `config.yaml` - Working config from `232ff8c` + platform_structure section
- `scripts/audit_library.py` - Original fast working scanner
- `ludis.py` - Original working main script

### Backups
- `config.yaml.v2-with-platform-structure` - Your discovered platform config
- `config.yaml.sample.v2` - Updated sample with schema docs
- `ludis.old.py` - Already exists, can delete after revert
- `scripts.old/` - Already exists, can delete after revert

### Branch Archive
- `wip-interactive-scanner` - All attempted changes saved here
  - Reference for `interactive_scanner.py` logic
  - Reference for config schema
  - Evidence of what NOT to do for performance

---

## Verification Checklist

After completing the revert:

- [ ] `git log --oneline -1` shows `232ff8c`
- [ ] `config.yaml` has `platform_structure` section
- [ ] `python3 ludis.py` runs
- [ ] Filesystem scan completes in 2-4 minutes
- [ ] `nas_inventory.csv` has ~33,000 entries
- [ ] All platforms scanned correctly
- [ ] No performance issues

---

## Emergency Rollback

If something goes wrong during revert:

```bash
# Your work is safe in the branch!
git reflog

# Find the commit before you started reverting
git reset --hard HEAD@{N}

# Or just go back to the WIP branch
git checkout wip-interactive-scanner
```

---

## Summary

**What You're Saving:**
- Interactive discovery UI concept ✅
- Config schema for platform_structure ✅
- 50 platforms worth of discovered structure ✅

**What You're Discarding:**
- Slow scanner implementation ❌
- Performance-breaking changes ❌
- Over-engineered integration ❌

**What You're Keeping:**
- Fast working scanner (2-4 min) ✅
- All downstream features (migration, playlists) ✅
- Your sanity ✅

---

Last Updated: 2025-11-21
Status: Ready to execute
Risk Level: LOW (everything backed up)

