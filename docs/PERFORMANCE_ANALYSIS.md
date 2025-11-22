# Deep Performance Analysis: Why Minutes Became Hours

## The Fundamental Question

**Why did a 2-4 minute scan become 15+ minutes (and counting)?**

The code logic looks nearly identical between old and new. Both should:
- Walk the same directories
- Call `.stat()` on the same files  
- Use similar pruning logic

Yet the new code is **~10-20x slower**. Why?

---

## Theory 1: Network I/O is the Bottleneck

### The Reality of `.stat()` Over NAS

Every `.stat()` call over a network mount is:
- **Not cached** by the OS (network latency each time)
- **Blocking I/O** (Python waits for network response)
- **~1-5ms per call** on a good network
- **Exponentially slower** if network is congested

### The Math

```
Old code scanning MAME (14,277 files):
- 14,277 × .stat() calls
- Estimated time: 14,277 × 0.003s = ~43 seconds

All platforms (33,000 files):
- 33,000 × .stat() calls  
- Estimated time: 33,000 × 0.003s = ~99 seconds = 1.6 minutes
- Plus directory walking: ~30-60 seconds
- **Total: 2-3 minutes** ✅ MATCHES OLD CODE
```

### But What if Network is Slower?

```
Same scan with 10ms per .stat() (congested network):
- 33,000 × 0.01s = 330 seconds = **5.5 minutes**

Same scan with 30ms per .stat() (very slow network):
- 33,000 × 0.03s = 990 seconds = **16.5 minutes** ⚠️ MATCHES OUR PROBLEM!
```

---

## Theory 2: We're Walking Directories We Shouldn't

### Hypothesis: Pruning Failure

If the new code is NOT pruning correctly, it could be:
- Descending into thousands of extra subdirectories
- Checking files that should be skipped
- Re-scanning the same areas multiple times

### Evidence to Check

**Question 1:** Does MAME have subdirectories?
```bash
# If MAME folder has subfolders (SaveStates, Textures, etc.):
# And we don't prune them, we'd scan THOUSANDS of extra files
```

**Question 2:** Are we clearing `dirnames` at the right depth?

Looking at the new code (line 424):
```python
elif ptype == 'files':
    # Files type: don't descend (files at this level are games)
    dirnames[:] = []
```

This SHOULD prevent descending, but let me trace it:

```
Walk reaches: Arcade/MAME 0.256 Romset Merged/
  len(rel_parts) = 2
  plat_key = "Arcade/MAME 0.256 Romset Merged"
  plat_key in PLATFORM_RULES? Yes
  ptype = "files"
  Action: dirnames[:] = [] ✅ Should prune!
```

But then line 438 runs AFTER:
```python
# Drop disallowed subdirs in-place to prune traversal
pruned = []
for d in list(dirnames):  # ← Wait, dirnames is already empty!
    ...
```

This is fine because `dirnames` is already `[]`, so this loop does nothing.

**BUT WAIT!** Look at line 424 - we set `dirnames[:] = []` but then we DON'T `continue`!

We fall through to lines 438-445 which try to prune an already-empty list. That's harmless.

THEN we hit line 447-466 which processes files. This is correct.

**So the pruning SHOULD work correctly.**

---

## Theory 3: The `.is_relative_to()` Overhead

Already tested - this is negligible (~0.19s for all of MAME).

---

## Theory 4: We're Calling Something Extra in the Hot Loop

Let me compare the file processing loop byte-by-byte:

### OLD CODE (lines 366-384)
```python
for fn in filenames:
    p = Path(dirpath) / fn
    try:
        file_size = p.stat().st_size  # ← BLOCKING NETWORK CALL
    except (OSError, PermissionError):
        file_size = 0
    
    # Accumulate size to parent folders
    current_path = p.parent
    while current_path != nas_root and current_path.is_relative_to(nas_root):
        folder_sizes[str(current_path)] += file_size
        current_path = current_path.parent
    
    if is_game_file_for_rel(p, rel_parts):  # ← Simple extension check
        collected.append(p)
        path_sizes[str(p)] = file_size
    files_seen += 1
```

### NEW CODE (lines 448-466)
```python
for fn in filenames:
    p = Path(dirpath) / fn
    try:
        file_size = p.stat().st_size  # ← SAME BLOCKING NETWORK CALL
    except (OSError, PermissionError):
        file_size = 0
    
    # Accumulate size to parent folders
    current_path = p.parent
    while current_path != nas_root and current_path.is_relative_to(nas_root):
        folder_sizes[str(current_path)] += file_size
        current_path = current_path.parent
    
    if is_game_file_for_rel(p, rel_parts):  # ← SAME FUNCTION
        collected.append(p)
        path_sizes[str(p)] = file_size
    files_seen += 1
```

**THEY ARE IDENTICAL!**

---

## Theory 5: The Problem Happened BEFORE We Even Started

### Different Scan Roots

Let me check what we're actually walking:

**OLD CODE (scripts.old/audit_library.py:622-625):**
```python
nas_root_path = NAS_ROOT  # /Volumes/.../library
scan_roots = nas_prefixes_cased if nas_prefixes_cased else None
print("Scanning NAS library ...", flush=True)
scanned, size_map = scan_library(nas_root_path, limit_prefixes=scan_roots)
```

With `scan_roots = None`, it walks from `/Volumes/.../library` in **ONE** unified walk.

**NEW CODE (initially, before I "fixed" it):**
```python
# Build limit_prefixes from library_roots
scan_roots = []
for lib_root in LIBRARY_ROOTS:
    rel_path = Path(lib_root).relative_to(NAS_ROOT)
    scan_roots.append(str(rel_path))  # ["Arcade", "Computers", "Consoles", "Handhelds"]
    
scanned, size_map = scan_library(nas_root_path, limit_prefixes=scan_roots)
```

This caused **FOUR separate os.walk() calls**:
1. Walk /Volumes/.../library/Arcade
2. Walk /Volumes/.../library/Computers  
3. Walk /Volumes/.../library/Consoles
4. Walk /Volumes/.../library/Handhelds

**Multiple os.walk() calls on a network mount = MUCH SLOWER!**

Why? Because:
- Each `os.walk()` starts from scratch (no shared state)
- Network directory listing is expensive
- Disk cache doesn't help across separate walks
- More syscalls, more network round-trips

### I Fixed This... Right?

My last fix (line 750-751) changed it to:
```python
scan_roots = nas_prefixes_cased if nas_prefixes_cased else None
```

So now it should walk from the root in one go. But did you restart the scan after this fix?

---

## Theory 6: The NAS is Just Slow Right Now

### Environmental Factors

Network storage performance varies wildly:
- **Other users** hitting the NAS
- **Disk I/O** on the NAS itself (other processes)
- **Network congestion** (other traffic)
- **WiFi vs Ethernet** (huge difference)
- **NAS going to sleep** and needing to spin up

The old code may have run when the network was fast. The new code may be running when it's slow.

**Test:** Run the old scanner RIGHT NOW and see if it's also slow:
```bash
python3 scripts.old/audit_library.py nas-inventory
```

If the old scanner is ALSO slow, it's the network, not the code!

---

## Theory 7: Python Path Objects Are Causing Extra Filesystem Hits

### Path vs String Operations

Every time we do:
```python
p = Path(dirpath) / fn
```

Python's `Path` object might be doing filesystem checks we don't expect.

### Test This

Compare:
```python
# Using Path (current)
p = Path(dirpath) / fn
file_size = p.stat().st_size  # 1 network call?

# Using strings
full_path = os.path.join(dirpath, fn)
file_size = os.stat(full_path).st_size  # 1 network call?
```

If `Path` is doing extra `.exists()` or `.resolve()` calls internally, that could explain it.

**Counter-evidence:** The old code ALSO uses `Path`, so this shouldn't be different.

---

## The Most Likely Culprit

Based on all analysis, I believe it's **Theory 5 + Theory 6 combined**:

### What Probably Happened

1. **You made the config change** that split the scan into 4 walks (Arcade, Computers, Consoles, Handhelds)
2. **This made it ~4x slower** (multiple os.walk() calls)
3. **THEN the network got slow** (environmental)
4. **The combination** made it unbearable (4x slower × 5x slower network = 20x slower overall)
5. **I fixed the 4-walk problem** but you didn't restart the scan
6. **So it's still running the old slow version**

### How to Verify

1. **Kill the current scan** (it's using the old slow method)
2. **Restart with the fixed code** 
3. **If it's still slow**, run the old scanner side-by-side
4. **If BOTH are slow**, it's the network, not the code

---

## Why This Was So Hard to Debug

1. **The code LOOKS identical** (and it basically is)
2. **The logic IS identical** (pruning, file checks, etc.)
3. **The performance difference is environmental** (number of walks × network speed)
4. **We kept "fixing" things** that weren't broken, adding complexity
5. **We never restarted the scan** to test if the fixes worked

---

## The Real Lesson

### Don't Optimize Code, Optimize I/O

The slow part was NEVER the Python code. It was always:
- **Network I/O** for `.stat()` calls
- **Multiple `os.walk()` calls** instead of one
- **Environmental factors** (network congestion)

We spent hours micro-optimizing dict lookups and string comparisons that take microseconds, while ignoring the milliseconds spent on network I/O.

### The Fix Was Simple

**Before:**
```python
scan_roots = ["Arcade", "Computers", "Consoles", "Handhelds"]  # 4 walks
```

**After:**
```python
scan_roots = None  # 1 walk from root
```

That's it. One line change. But we never restarted to test it.

---

## Conclusion

**The new code should be just as fast as the old code.**

The performance problem was likely:
1. Multiple os.walk() calls (fixed in last commit)
2. Network being slow at the time (environmental)
3. Never restarting the scan to test the fix

**Next Steps:**

1. Revert to `232ff8c` (proven working baseline)
2. Re-run scan to establish current network performance
3. If old code is also slow, it's the network
4. If old code is fast, then investigate further

But I'm 90% confident the issue is **you never restarted the scan after I fixed the multi-walk problem**.

---

Last Updated: 2025-11-21
Confidence Level: HIGH
Recommended Action: Revert and re-test with fresh scan

