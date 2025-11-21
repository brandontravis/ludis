#!/usr/bin/env python3
import argparse, csv, os, sys
from pathlib import Path
from collections import defaultdict
from typing import Optional, List, Dict
import time
import unicodedata
import subprocess

# Project root is parent of scripts/ directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "LB_Exports" / "all_platforms.csv"
OUTDIR = PROJECT_ROOT / "LB_Exports" / "audits"

# These will be loaded from config.yaml
WIN_ROOT = None
LIBRARY_ROOTS = []

# Load configuration from config.yaml
def load_config():
    """Load paths and exclusions from config.yaml"""
    global WIN_ROOT, LIBRARY_ROOTS
    
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if not config_path.exists():
            print("ERROR: config.yaml not found. Please run ludis.py setup first.")
            sys.exit(1)
        
        with open(config_path) as f:
            config = yaml.safe_load(f)
            
            # Load paths
            paths = config.get('paths', {})
            WIN_ROOT = paths.get('windows_root', '')
            LIBRARY_ROOTS = paths.get('library_roots', [])
            
            if not LIBRARY_ROOTS:
                # Fall back to old local_root for backward compatibility
                local_root = paths.get('local_root')
                if local_root:
                    LIBRARY_ROOTS = [local_root]
                else:
                    print("ERROR: No library_roots configured in config.yaml")
                    sys.exit(1)
            
            # Load exclusions
            excluded = config.get('options', {}).get('exclude_platforms', [])
            # Normalize to lowercase for case-insensitive matching
            excluded_platforms = [p.lower() for p in excluded]
            
            # Load platform structure config
            platform_structure = config.get('platform_structure', {})
            
            return excluded_platforms, platform_structure
    except Exception as e:
        print(f"ERROR: Could not load config.yaml: {e}")
        sys.exit(1)

EXCLUDED_PLATFORMS, PLATFORM_STRUCTURE_CONFIG = load_config()
if EXCLUDED_PLATFORMS:
    print(f"⚠ Excluding platforms: {', '.join(EXCLUDED_PLATFORMS)}")

def is_platform_excluded(platform_name: str) -> bool:
    """Check if a platform should be excluded"""
    if not EXCLUDED_PLATFORMS:
        return False
    platform_lower = platform_name.lower()
    # Check if any excluded platform name is in the platform string
    return any(excl in platform_lower for excl in EXCLUDED_PLATFORMS)

# Extensions considered as game payloads by default
DEFAULT_GAME_EXTS = {
    ".zip",".7z",".iso",".cue",".bin",".chd",".rvz",".gdi",".nrg",".wbfs",".gcm",".gcz",
    ".dol",".elf",".rom",".nes",".fds",".sfc",".smc",".gba",".gbc",".gb",".n64",".z64",
    ".nds",".3ds",".wad",".wua",".xci",".nsp",".pbp",".vpk",".adf",".m3u",".xiso",
    ".cpr",".vec",  # Amstrad GX4000 and GCE Vectrex
    ".bs",".pcm",  # Nintendo Satellaview
    ".pce",".sgx",  # TurboGrafx-16, PC Engine, SuperGrafx
    ".md",".sms",  # Sega Genesis and Master System
    ".nsz",  # Nintendo Switch compressed
}

# Special include/skip rules for specific platform folders
SPECIAL_RULES = {
    # Skip textures for GameCube
    "Consoles/Nintendo Gamecube [2001]/Textures": {"skip_dir": True},
    # Wii: ensure RVZ is scanned; default recursion already includes it, listed for clarity
    "Consoles/Nintendo Wii [2006]/RVZ": {"include_dir": True},
    # Switch: only Base Games
    "Consoles/Nintendo Switch [2017]": {"only_subdirs": ["Base Games"]},
    "Consoles/Nintendo Switch [2017]/Base Games": {"include_dir": True},
    # Wii U: only the merged decrypted folders (Base Games... and eShop... variants)
    "Consoles/Nintendo Wii U [2012]": {"only_subdirs": ["Base Games + Updates + DLC Merged (Decrypted ... use these!)", "eShop + Updates + DLC Merged (Decrypted ... use these!)"]},
    "Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)": {"include_dir": True},
    "Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)": {"include_dir": True},
    # PS2: scan both bin (nested) and iso
    "Consoles/Sony PlayStation 2 [2000]": {"only_subdirs": ["bin","iso"]},
    "Consoles/Sony PlayStation 2 [2000]/bin": {"include_dir": True},
    "Consoles/Sony PlayStation 2 [2000]/iso": {"include_dir": True},
    # PS3: only Base Games/EBoot subtree
    "Consoles/Sony PlayStation 3 [2006]": {"only_subdirs": ["Base Games"]},
    "Consoles/Sony PlayStation 3 [2006]/Base Games": {"only_subdirs": ["EBoot","PKG"]},
    "Consoles/Sony PlayStation 3 [2006]/Base Games/EBoot": {"include_dir": True},
    "Consoles/Sony PlayStation 3 [2006]/Base Games/PKG": {"include_dir": True},
    # PS Vita: exclude "_id imports"
    "Handhelds/Sony PS Vita [2011]/_id imports": {"skip_dir": True},
}

PER_GAME_SUBFOLDER_PLATFORMS = {
    "Consoles/Panasonic 3DO Interactive Multiplayer [1993]",
    "Consoles/Sega Dreamcast [1998]",
    "Consoles/Sega Saturn [1994]",
    "Handhelds/Sony PS Vita [2011]",
    "Consoles/NEC TurboGrafx-CD (PC Engine CD-Rom) [1988]",
    "Consoles/SNK NeoGeo CD [1994]",  # alt naming variant without space
    # Computers contain one subfolder per title
    "Computers",
}

# Windows subpath (relative to WIN_ROOT) -> NAS subpath (relative to NAS_ROOT)
# Use lowercased keys for case-insensitive matching; values are used as-is.
SUBPATH_OVERRIDES = {
    "consoles/nec - turbografx 16 - pc engine [1987]": "Consoles/NEC TurboGrafx-16 (PC Engine) [1987]",
    "consoles/nec turbografx 16 (pc engine) [1987]": "Consoles/NEC TurboGrafx-16 (PC Engine) [1987]",
    "consoles/nec turbografx-cd [1988]": "Consoles/NEC TurboGrafx-CD (PC Engine CD-Rom) [1988]",
    "consoles/nec turbografx-cd (pc engine cd-rom) [1988]": "Consoles/NEC TurboGrafx-CD (PC Engine CD-Rom) [1988]",
    "consoles/nec pc engine supergrafx [1989]": "Consoles/NEC PC Engine SuperGrafx [1989]",
}

# ES-DE slugs -> mapping to LaunchBox platform names and NAS platform prefixes
# lb_platforms: names as they appear in the CSV "Platform" column
# nas_prefixes: first-two-level NAS path (relative to NAS_ROOT) for the platform
ESDE_SLUG_MAP = {
    "ps3": {
        "lb_platforms": {"Sony Playstation 3", "Sony PlayStation 3"},
        "nas_prefixes": {"Consoles/Sony PlayStation 3 [2006]"},
    },
    "ps2": {
        "lb_platforms": {"Sony Playstation 2", "Sony PlayStation 2"},
        "nas_prefixes": {"Consoles/Sony PlayStation 2 [2000]"},
    },
    "saturn": {
        "lb_platforms": {"Sega Saturn"},
        "nas_prefixes": {"Consoles/Sega Saturn [1994]"},
    },
    "dreamcast": {
        "lb_platforms": {"Sega Dreamcast"},
        "nas_prefixes": {"Consoles/Sega Dreamcast [1998]"},
    },
    "3do": {
        "lb_platforms": {"Panasonic 3DO Interactive Multiplayer", "3DO Interactive Multiplayer"},
        "nas_prefixes": {"Consoles/Panasonic 3DO Interactive Multiplayer [1993]"},
    },
    "psvita": {
        "lb_platforms": {"Sony Playstation Vita", "Sony PlayStation Vita"},
        "nas_prefixes": {"Handhelds/Sony PS Vita [2011]"},
    },
    "switch": {
        "lb_platforms": {"Nintendo Switch"},
        "nas_prefixes": {"Consoles/Nintendo Switch [2017]"},
    },
    "wiiu": {
        "lb_platforms": {"Nintendo Wii U"},
        "nas_prefixes": {"Consoles/Nintendo Wii U [2012]"},
    },
    "wii": {
        "lb_platforms": {"Nintendo Wii"},
        "nas_prefixes": {"Consoles/Nintendo Wii [2006]"},
    },
    "gamecube": {
        "lb_platforms": {"Nintendo GameCube", "Nintendo Gamecube"},
        "nas_prefixes": {"Consoles/Nintendo Gamecube [2001]"},
    },
    "neogeocd": {
        "lb_platforms": {"SNK Neo Geo CD", "SNK NeoGeo CD"},
        "nas_prefixes": {"Consoles/SNK NeoGeo CD [1994]"},
    },
    "msdos": {
        "lb_platforms": {"MS-DOS"},
        "nas_prefixes": {"Computers/MS-DOS [1981]"},
    },
    "windows": {
        "lb_platforms": {"Windows"},
        "nas_prefixes": {"PC/Windows [1985]", "PC/Windows"},  # allow variants
    },
}

def get_platform_filters(slug: Optional[str]):
    """Return (lb_cf_set, nas_cf_set, nas_prefixes_cased) for a platform selector.
    Resolution order:
      1) Known ES-DE slug in ESDE_SLUG_MAP
      2) Fuzzy match against LB platform names (from CSV) and NAS prefixes (from NAS root)
         using case-insensitive substring matching
    """
    if not slug:
        return set(), set(), []
    key = slug.lower()
    # 1) Known ES-DE slug
    s = ESDE_SLUG_MAP.get(key)
    if s:
        lb = {x.casefold() for x in s.get("lb_platforms", set())}
        nas = {x.casefold() for x in s.get("nas_prefixes", set())}
        nas_cased = list(s.get("nas_prefixes", set()))
        return lb, nas, nas_cased

    # 2) Fuzzy discovery from current CSV and NAS contents
    lb_names = set()
    try:
        with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
            r = csv.DictReader(f)
            for row in r:
                plat = (row.get("Platform") or "").strip()
                if plat:
                    lb_names.add(plat)
    except Exception:
        pass

    nas_prefixes = set()
    try:
        for top in NAS_ROOT.iterdir():
            if not top.is_dir():
                continue
            for plat in top.iterdir():
                if plat.is_dir():
                    nas_prefixes.add(f"{top.name}/{plat.name}")
    except Exception:
        pass

    lb_cf = {p.casefold() for p in lb_names if key in p.casefold()}
    nas_cf = {p.casefold() for p in nas_prefixes if key in p.casefold()}
    nas_cased = [p for p in nas_prefixes if p.casefold() in nas_cf]
    if not lb_cf and not nas_cf:
        print(f"ERROR: Unknown platform selector '{slug}'.", file=sys.stderr)
        print(f"Known ES-DE slugs: {', '.join(sorted(ESDE_SLUG_MAP.keys()))}", file=sys.stderr)
        if lb_names:
            print(f"CSV Platforms: {', '.join(sorted(lb_names))}", file=sys.stderr)
        if nas_prefixes:
            print(f"NAS prefixes: {', '.join(sorted(nas_prefixes))}", file=sys.stderr)
        sys.exit(2)
    return lb_cf, nas_cf, nas_cased

def normalize_win_to_mac(path_str: str, win_root: str, nas_root: str) -> str:
    if not path_str:
        return ""
    p = path_str.replace("\\", "/")
    wr = win_root.replace("\\", "/").rstrip("/")
    if p.lower().startswith(wr.lower()):
        suffix = p[len(wr):]
        if suffix.startswith("/"):
            suffix = suffix[1:]
        # Apply subpath overrides
        low_suffix = suffix.lower()
        for k, v in SUBPATH_OVERRIDES.items():
            if low_suffix.startswith(k):
                # replace the matched prefix in a case-preserving way
                suffix = v + suffix[len(k):]
                break
        return str(Path(nas_root) / suffix)
    return p

def read_csv_paths(csv_path: Path, win_root: str, nas_root: str) -> list[dict]:
    """Read all_platforms.csv and preserve all metadata fields."""
    rows = []
    if not csv_path.exists():
        print(f"ERROR: CSV not found: {csv_path}", file=sys.stderr)
        return rows
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            file_path = (r.get("LBFilePath") or r.get("FilePath") or "").strip()
            mac_path = normalize_win_to_mac(file_path, win_root, nas_root)
            # Preserve all metadata fields from all_platforms.csv
            row = dict(r)  # Copy all fields
            row["FilePathWin"] = file_path
            row["FilePathMac"] = mac_path
            rows.append(row)
    return rows

def should_skip_dir(rel_parts: list[str]) -> bool:
    rel = "/".join(rel_parts)
    # Skip hidden/system-like folders quickly
    if any(p.startswith(".") for p in rel_parts):
        return True
    # Apply explicit skip rules
    for key, rule in SPECIAL_RULES.items():
        if rel.lower() == key.lower() and rule.get("skip_dir"):
            return True
    return False

def is_within_allowed_tree(rel_parts: list[str]) -> bool:
    # Enforce "only_subdirs" constraints on parent anchors
    for anchor, rule in SPECIAL_RULES.items():
        only = rule.get("only_subdirs")
        if not only:
            continue
        anchor_parts = anchor.split("/")
        if len(rel_parts) < len(anchor_parts):
            continue
        if "/".join(rel_parts[:len(anchor_parts)]).lower() == anchor.lower():
            # If we're exactly one level deeper than anchor, enforce membership
            if len(rel_parts) == len(anchor_parts) + 1:
                return rel_parts[-1] in only
    return True

def is_game_file_default(path: Path) -> bool:
    ext = path.suffix.lower()
    return ext in DEFAULT_GAME_EXTS

def is_game_file_for_rel(path: Path, rel_parts: list[str]) -> bool:
    """Platform-aware file inclusion."""
    name_lower = path.name.lower()
    # Determine platform from first two segments when available
    plat = ""
    if len(rel_parts) >= 2:
        plat = f"{rel_parts[0]}/{rel_parts[1]}"
    # PS3: Only count EBOOT.BIN files as the game payload
    if plat == "Consoles/Sony PlayStation 3 [2006]":
        return name_lower == "eboot.bin"
    # Default behavior for others: rely on extension list
    return is_game_file_default(path)

def scan_library(nas_root: Path, limit_prefixes: Optional[List[str]] = None) -> tuple[list[Path], dict[str, int]]:
    collected: list[Path] = []
    path_sizes: dict[str, int] = {}  # Track sizes during scan
    folder_sizes: dict[str, int] = defaultdict(int)  # Accumulate folder sizes
    
    # Determine roots to scan
    roots = [nas_root]
    if limit_prefixes:
        roots = [nas_root / p for p in limit_prefixes]
    for start in roots:
        if not start.exists():
            continue
        print(f"  Walking {start} ...", flush=True)
        dirs_seen = 0
        files_seen = 0
        last_log = time.time()
        for dirpath, dirnames, filenames in os.walk(start):
            rel = Path(dirpath).relative_to(nas_root)
            rel_parts = list(rel.parts) if str(rel) != "." else []
            
            # Skip excluded platforms at the directory level
            if rel_parts:
                # Check if any part of the path contains an excluded platform
                path_str = "/".join(rel_parts)
                if is_platform_excluded(path_str):
                    # Skip this entire directory tree
                    dirnames[:] = []
                    continue
            
            # Collapse to folder-level for per-game platforms at the appropriate depth
            collapse_here = False
            if len(rel_parts) >= 2:
                plat_key = f"{rel_parts[0]}/{rel_parts[1]}"
                # Computers: titles are immediate children under Computers/<platform>
                if rel_parts[0] == "Computers" and len(rel_parts) == 2:
                    collapse_here = True
                # Console/Handheld per-game platforms: titles under platform root
                if plat_key in PER_GAME_SUBFOLDER_PLATFORMS and len(rel_parts) == 2:
                    collapse_here = True
                # PS2 bin: titles directly under Consoles/Sony PlayStation 2 [2000]/bin/<Title>
                if plat_key == "Consoles/Sony PlayStation 2 [2000]" and len(rel_parts) == 3 and rel_parts[2].lower() == "bin":
                    collapse_here = True
                # PS3: titles under Base Games/EBoot/<Title>
                if plat_key == "Consoles/Sony PlayStation 3 [2006]" and len(rel_parts) == 4:
                    level2 = rel_parts[2].lower()
                    level3 = rel_parts[3].lower()
                    if level2 == "base games" and level3 in ("eboot","pkg"):
                        collapse_here = True
            if collapse_here:
                # Record each immediate subdirectory as a candidate and do not descend further
                for d in list(dirnames):
                    # Apply skip_dir rule if any
                    child_rel = rel_parts + [d]
                    if should_skip_dir(child_rel):
                        continue
                    folder_path = Path(dirpath) / d
                    collected.append(folder_path)
                    # Get folder size using du command (fast, doesn't require walking all files)
                    folder_size = get_folder_size(folder_path)
                    path_sizes[str(folder_path)] = folder_size
                    dirs_seen += 1
                dirnames[:] = []
                continue
            # Drop disallowed subdirs in-place to prune traversal
            pruned = []
            for d in list(dirnames):
                child_rel = rel_parts + [d]
                if should_skip_dir(child_rel) or not is_within_allowed_tree(child_rel):
                    pruned.append(d)
            for d in pruned:
                dirnames.remove(d)
            dirs_seen += 1

            # Collect files and accumulate sizes
            for fn in filenames:
                p = Path(dirpath) / fn
                # Get file size while we're here
                try:
                    file_size = p.stat().st_size
                except (OSError, PermissionError):
                    file_size = 0
                
                # Accumulate size to all parent folders up to the game folder level
                current_path = p.parent
                while current_path != nas_root and current_path.is_relative_to(nas_root):
                    folder_sizes[str(current_path)] += file_size
                    current_path = current_path.parent
                
                if is_game_file_for_rel(p, rel_parts):
                    collected.append(p)
                    # For individual files, store their size directly
                    path_sizes[str(p)] = file_size
                files_seen += 1
            if files_seen and (files_seen % 5000 == 0 or (time.time() - last_log) > 2.0):
                print(f"    ... scanned {dirs_seen} dirs, {files_seen} files, {len(collected)} candidates", flush=True)
                last_log = time.time()
    
    # Merge folder sizes into path_sizes
    for folder_path, size in folder_sizes.items():
        path_sizes[folder_path] = size
    
    return collected, path_sizes

def get_folder_size(folder_path: Path) -> int:
    """
    Get total size of a folder using the du command (much faster than walking all files).
    
    Args:
        folder_path: Path to the folder
        
    Returns:
        Total size in bytes, or 0 if the command fails
    """
    try:
        # Use du -sk to get size in kilobytes (works on both macOS and Linux)
        # -s: summarize (don't show subdirectories)
        # -k: kilobytes (macOS doesn't support -b for bytes)
        result = subprocess.run(
            ['du', '-sk', str(folder_path)],
            capture_output=True,
            text=True,
            timeout=60  # Timeout after 60 seconds for very large folders
        )
        if result.returncode == 0:
            # Output format: "12345\t/path/to/folder"
            size_kb_str = result.stdout.split('\t')[0].strip()
            size_kb = int(size_kb_str)
            # Convert kilobytes to bytes
            return size_kb * 1024
    except (subprocess.TimeoutExpired, subprocess.SubprocessError, ValueError, IndexError) as e:
        print(f"    Warning: Failed to get size for {folder_path}: {e}")
    return 0

def rel_to_root(paths: list[Path], root: Path) -> list[str]:
    out: list[str] = []
    for p in paths:
        try:
            # Normalize Unicode to NFC (composed form) to match LaunchBox
            # macOS uses NFD (decomposed), which causes mismatches with special characters like é
            rel_path = str(p.relative_to(root))
            normalized = unicodedata.normalize('NFC', rel_path)
            out.append(normalized)
        except Exception:
            normalized = unicodedata.normalize('NFC', str(p))
            out.append(normalized)
    return out

def sanitize_name(name: str) -> str:
    # Safe filename for per-platform outputs
    s = name.replace("/", "_").replace("\\", "_")
    s = s.replace(":", "-").replace("*", "-").replace("?", "-").replace("|", "-").replace('"', "'").strip()
    return s or "_"

def infer_platform_from_rel(rel_path: str) -> str:
    parts = [p for p in rel_path.split("/") if p]
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    if parts:
        return parts[0]
    return "(root)"

def is_per_game_platform_parts(parts: list[str]) -> bool:
    if not parts:
        return False
    # Treat any "Computers/*" as per-title subfolder
    if parts[0] == "Computers":
        return True
    if len(parts) >= 2:
        plat = f"{parts[0]}/{parts[1]}"
        if plat in PER_GAME_SUBFOLDER_PLATFORMS:
            return True
        if plat == "Consoles/Sony PlayStation 3 [2006]":
            return True
    return False

def is_ps3_parts(parts: list[str]) -> bool:
    return len(parts) >= 2 and parts[0] == "Consoles" and parts[1] == "Sony PlayStation 3 [2006]"

def game_folder_key_from_rel(rel_path: str) -> Optional[str]:
    parts = [p for p in rel_path.split("/") if p]
    if not parts:
        return None
    # PS3: Consoles/PS3/Base Games/(EBoot|PKG)/<Title>
    if is_ps3_parts(parts):
        if len(parts) >= 5 and parts[2].lower() == "base games" and parts[3].lower() in ("eboot","pkg"):
            return "/".join(parts[:5])
        return None
    # Computers and other per-game platforms: Consoles/<Platform>/<Title> or Computers/<Platform>/<Title>
    if is_per_game_platform_parts(parts) and len(parts) >= 3:
        return "/".join(parts[:3])
    return None

def game_folder_rel_from_parts(parts: list[str]) -> str:
    if len(parts) >= 3:
        return "/".join(parts[:3])
    return "/".join(parts)

def guess_title_from_rel(rel_path: str) -> str:
    parts = [p for p in rel_path.split("/") if p]
    try:
        # PS3: title is the folder under EBoot/PKG
        if is_ps3_parts(parts) and len(parts) >= 5 and parts[2].lower() == "base games" and parts[3].lower() in ("eboot","pkg"):
            return parts[4]
        if is_per_game_platform_parts(parts) and len(parts) >= 3:
            return parts[2]
        # fallback to file stem
        p = Path(rel_path)
        return p.stem
    except Exception:
        return ""

def cmd_missing_in_fs(args):
    print("Starting missing-in-fs ...")
    csv_rows = read_csv_paths(CSV_PATH, WIN_ROOT, str(NAS_ROOT))
    lb_filter, _, _ = get_platform_filters(args.platform)
    all_rows = []
    per_platform: dict[str, list[dict]] = {}
    platforms = sorted({r["Platform"] for r in csv_rows if r.get("Platform")})
    if lb_filter:
        platforms = [p for p in platforms if p.casefold() in lb_filter]
        if not platforms:
            print(f"No CSV platforms match slug '{args.platform}'.")
            return
    for plat in platforms:
        print(f"Starting platform {plat} ...")
        per_list = []
        for r in csv_rows:
            if r.get("Platform") != plat:
                continue
            mac = r["FilePathMac"]
            if not mac:
                per_list.append({
                    "Platform": plat,
                    "Title": r.get("Title",""),
                    "CsvPath": r["FilePathWin"],
                    "MacPath": mac,
                    "Status": "Not Found",
                    "Reason": "Empty path",
                })
            else:
                exists = os.path.exists(mac)
                per_list.append({
                    "Platform": plat,
                    "Title": r.get("Title",""),
                    "CsvPath": r["FilePathWin"],
                    "MacPath": mac,
                    "Status": "Found" if exists else "Not Found",
                    "Reason": "" if exists else "Missing on NAS",
                })
        per_platform[plat] = per_list
        all_rows.extend(per_list)
        # per-platform file
        subdir = OUTDIR / "missing-in-fs"
        subdir.mkdir(parents=True, exist_ok=True)
        _write_report(subdir / f"{sanitize_name(plat)}.csv", ["Platform","Title","CsvPath","MacPath","Status","Reason"], per_list)
        print(f"Finished {plat} ({len(per_list)} rows)")
    # master file
    if not lb_filter:
        _write_report(OUTDIR / "missing_in_fs.csv", ["Platform","Title","CsvPath","MacPath","Status","Reason"], all_rows)
        print(f"Wrote {OUTDIR / 'missing_in_fs.csv'} ({len(all_rows)} rows)")
    print("Completed missing-in-fs")

def cmd_untracked_on_fs(args):
    print("Starting untracked-on-fs ...")
    csv_rows = read_csv_paths(CSV_PATH, WIN_ROOT, str(NAS_ROOT))
    _, nas_filter_cf, nas_prefixes_cased = get_platform_filters(args.platform)
    # Build a set of CSV-relative paths for comparison
    csv_set = set()
    tracked_game_folders = set()  # for per-game platforms, track folder-level coverage
    nas_root_path = NAS_ROOT
    print("Indexing CSV paths under NAS root ...")
    nas_norm = str(nas_root_path).replace("\\", "/").rstrip("/").lower()
    processed = 0
    for r in csv_rows:
        mac = r["FilePathMac"]
        if not mac:
            continue
        p = mac.replace("\\", "/")
        pl = p.lower()
        if pl == nas_norm:
            rel = ""
        elif pl.startswith(nas_norm + "/"):
            rel = p[len(nas_norm) + 1:]
        else:
            # Outside NAS root, ignore
            continue
        csv_set.add(rel.casefold())
        # Record the game folder for per-game platforms
        key = game_folder_key_from_rel(rel)
        if key:
            tracked_game_folders.add(key.casefold())
        processed += 1
        if processed and processed % 50000 == 0:
            print(f"  Indexed {processed} CSV paths ...", flush=True)
    print(f"Indexed {processed} CSV rows mapped to {len(csv_set)} unique paths", flush=True)

    # Scan NAS
    print("Scanning NAS library ...", flush=True)
    scan_roots = nas_prefixes_cased if nas_prefixes_cased else None
    scanned, _size_map = scan_library(nas_root_path, limit_prefixes=scan_roots)
    rel_scanned = rel_to_root(scanned, nas_root_path)
    print(f"Scanned {len(rel_scanned)} candidate files on NAS", flush=True)
    untracked = []
    # Group by inferred platform (from NAS path)
    per_platform: dict[str, list[dict]] = {}
    # Single pass: group rel paths per platform for efficiency
    platform_to_rels: dict[str, list[str]] = defaultdict(list)
    for rel in rel_scanned:
        platform_to_rels[infer_platform_from_rel(rel)].append(rel)
    plats = sorted(platform_to_rels.keys())
    if nas_filter_cf:
        plats = [p for p in plats if p.casefold() in nas_filter_cf]
        if not plats:
            print(f"No NAS platform prefixes match slug '{args.platform}'.")
            return
    print(f"Preparing to process {len(plats)} platforms ...", flush=True)
    for plat in plats:
        print(f"Starting platform {plat} ...", flush=True)
        per_list = []
        rels = platform_to_rels[plat]
        # Check whether this platform uses per-title subfolders
        plat_parts = plat.split("/")
        per_game = is_per_game_platform_parts(plat_parts)
        if per_game:
            # Collapse to game-folder level (first 3 segments)
            game_folders = set()
            for rel in rels:
                key = game_folder_key_from_rel(rel)
                if key:
                    game_folders.add(key)
            for gf in sorted(game_folders, key=str.casefold):
                if gf.casefold() not in tracked_game_folders:
                    per_list.append({
                        "Platform": plat,
                        "Title": guess_title_from_rel(gf),
                        "RelPath": gf,
                    })
        else:
            # File-level comparison
            for rel in rels:
                if rel.casefold() not in csv_set:
                    per_list.append({
                        "Platform": plat,
                        "Title": guess_title_from_rel(rel),
                        "RelPath": rel,
                    })
        per_platform[plat] = per_list
        untracked.extend(per_list)
        subdir = OUTDIR / "untracked-on-fs"
        subdir.mkdir(parents=True, exist_ok=True)
        _write_report(subdir / f"{sanitize_name(plat)}.csv", ["Platform","Title","RelPath"], per_list)
        print(f"Finished {plat} ({len(per_list)} rows)", flush=True)
    if not nas_filter_cf:
        _write_report(OUTDIR / "untracked_on_fs.csv", ["Platform","Title","RelPath"], untracked)
        print(f"Wrote {OUTDIR / 'untracked_on_fs.csv'} ({len(untracked)} rows)")
    print("Completed untracked-on-fs")

def cmd_nas_inventory(args):
    print("Starting nas-inventory ...")
    _, nas_filter_cf, nas_prefixes_cased = get_platform_filters(args.platform)
    nas_root_path = NAS_ROOT
    scan_roots = nas_prefixes_cased if nas_prefixes_cased else None
    print("Scanning NAS library ...", flush=True)
    scanned, size_map = scan_library(nas_root_path, limit_prefixes=scan_roots)
    rel_scanned = rel_to_root(scanned, nas_root_path)
    print(f"Scanned {len(rel_scanned)} candidate files on NAS", flush=True)

    # Group by inferred platform
    platform_to_rels: dict[str, list[str]] = defaultdict(list)
    for rel in rel_scanned:
        platform_to_rels[infer_platform_from_rel(rel)].append(rel)
    plats = sorted(platform_to_rels.keys())
    if nas_filter_cf:
        plats = [p for p in plats if p.casefold() in nas_filter_cf]
        if not plats:
            print(f"No NAS platform prefixes match slug '{args.platform}'.")
            return

    all_rows: list[dict] = []
    subdir = OUTDIR / "nas_inventory"
    subdir.mkdir(parents=True, exist_ok=True)
    
    # Filter out excluded platforms
    plats = [p for p in plats if not is_platform_excluded(p)]
    
    print(f"Preparing to process {len(plats)} platforms ...", flush=True)
    for plat in plats:
        print(f"Starting platform {plat} ...", flush=True)
        rels = platform_to_rels[plat]
        plat_parts = plat.split("/")
        per_game = is_per_game_platform_parts(plat_parts)
        rows: list[dict] = []
        if per_game:
            game_folders = set()
            for rel in rels:
                key = game_folder_key_from_rel(rel)
                if key:
                    game_folders.add(key)
            for gf in sorted(game_folders, key=str.casefold):
                full_path = nas_root_path / gf
                file_size = size_map.get(str(full_path), 0)
                rows.append({
                    "Platform": plat, 
                    "Title": guess_title_from_rel(gf), 
                    "RelPath": gf,
                    "FileSize": file_size
                })
        else:
            for rel in sorted(rels, key=str.casefold):
                full_path = nas_root_path / rel
                file_size = size_map.get(str(full_path), 0)
                rows.append({
                    "Platform": plat, 
                    "Title": guess_title_from_rel(rel), 
                    "RelPath": rel,
                    "FileSize": file_size
                })
        _write_report(subdir / f"{sanitize_name(plat)}.csv", ["Platform","Title","RelPath","FileSize"], rows)
        print(f"Finished {plat} ({len(rows)} rows)", flush=True)
        all_rows.extend(rows)
    if not nas_filter_cf:
        _write_report(OUTDIR / "nas_inventory.csv", ["Platform","Title","RelPath","FileSize"], all_rows)
        print(f"Wrote {OUTDIR / 'nas_inventory.csv'} ({len(all_rows)} rows)")
    print("Completed nas-inventory")

def _write_report(path: Path, header: list[str], rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

def build_parser():
    ap = argparse.ArgumentParser(description="Audit LaunchBox exports against NAS library. Paths are hardcoded in this script.")
    ap.add_argument("--platform", help="ES-DE platform slug to limit processing (e.g., ps3, saturn, ps2, wiiu, switch)")

    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list-platforms", help="List known slugs and discovered platforms (CSV + NAS)")
    sub.add_parser("missing-in-fs", help="Report CSV-referenced files missing on NAS")
    sub.add_parser("untracked-on-fs", help="Report NAS files not referenced in CSV")
    sub.add_parser("nas-inventory", help="Scan NAS (or a single platform) and list existing titles/files")
    sub.add_parser("all", help="Run all audits")
    return ap

def main():
    ap = build_parser()
    args = ap.parse_args()
    if args.cmd == "list-platforms":
        print("Known ES-DE slugs:")
        for k in sorted(ESDE_SLUG_MAP.keys()):
            cfg = ESDE_SLUG_MAP[k]
            lb = ", ".join(sorted(cfg.get("lb_platforms", [])))
            nas = ", ".join(sorted(cfg.get("nas_prefixes", [])))
            print(f"  {k:12}  LB=[{lb}]  NAS=[{nas}]")
        # CSV platforms
        try:
            csv_plats = set()
            with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
                r = csv.DictReader(f)
                for row in r:
                    p = (row.get("Platform") or "").strip()
                    if p:
                        csv_plats.add(p)
            print("\nCSV Platforms:")
            for p in sorted(csv_plats):
                print(f"  {p}")
        except Exception:
            pass
        # NAS prefixes
        try:
            nas_prefixes = []
            for top in NAS_ROOT.iterdir():
                if not top.is_dir():
                    continue
                for plat in top.iterdir():
                    if plat.is_dir():
                        nas_prefixes.append(f"{top.name}/{plat.name}")
            print("\nNAS platform folders (first two levels):")
            for p in sorted(nas_prefixes):
                print(f"  {p}")
        except Exception:
            pass
        return
    if args.cmd == "missing-in-fs":
        cmd_missing_in_fs(args)
    elif args.cmd == "untracked-on-fs":
        cmd_untracked_on_fs(args)
    elif args.cmd == "nas-inventory":
        cmd_nas_inventory(args)
    elif args.cmd == "all":
        # Run all audits independently; if a platform slug is provided, each will be scoped
        cmd_missing_in_fs(args)
        cmd_untracked_on_fs(args)
        cmd_nas_inventory(args)
    else:
        ap.print_help()
        sys.exit(2)

if __name__ == "__main__":
    main()


