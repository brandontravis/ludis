#!/usr/bin/env python3
import csv, os, re, sys
import unicodedata
from pathlib import Path
from collections import defaultdict

# Project root is parent of scripts/ directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# These will be loaded from config.yaml
CONFIG = {}
PLATFORMS_CSV = None
INVENTORY_CSV = None
OUTPUT_CSV = None
WIN_ROOT = ""
SUBPATH_OVERRIDES = {}
EXCLUDED_PLATFORMS = []

# Load configuration
def load_config():
    """Load configuration from config.yaml"""
    global CONFIG, PLATFORMS_CSV, INVENTORY_CSV, OUTPUT_CSV, WIN_ROOT, SUBPATH_OVERRIDES, EXCLUDED_PLATFORMS
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if config_path.exists():
            with open(config_path) as f:
                CONFIG = yaml.safe_load(f)
                
                # Load paths from config
                paths = CONFIG.get('paths', {})
                output_directory = paths.get('output_directory', 'LB_Exports/')
                WIN_ROOT = paths.get('windows_root', '')
                
                # Set output paths based on output_directory
                if not Path(output_directory).is_absolute():
                    output_base = PROJECT_ROOT / output_directory
                else:
                    output_base = Path(output_directory)
                
                PLATFORMS_CSV = output_base / "all_platforms.csv"
                INVENTORY_CSV = output_base / "audits" / "nas_inventory.csv"
                OUTPUT_CSV = output_base / "master_inventory.csv"
                
                # Load path overrides
                path_overrides = CONFIG.get('options', {}).get('path_overrides', {})
                if path_overrides:
                    SUBPATH_OVERRIDES.update(path_overrides)
                    print(f"✓ Loaded {len(path_overrides)} path override(s)")
                
                # Load platform exclusions
                excluded = CONFIG.get('options', {}).get('exclude_platforms', [])
                EXCLUDED_PLATFORMS = [p.lower() for p in excluded]
                if EXCLUDED_PLATFORMS:
                    print(f"⚠ Excluding platforms: {', '.join(EXCLUDED_PLATFORMS)}")
                
                if not WIN_ROOT:
                    print("Warning: windows_root not configured in config.yaml")
                
                return True
    except Exception as e:
        print(f"ERROR: Could not load config.yaml: {e}")
        sys.exit(1)

# Config will be loaded lazily in main() to avoid issues when config.yaml doesn't exist yet

def is_platform_excluded(platform_name: str) -> bool:
    """Check if a platform should be excluded"""
    if not EXCLUDED_PLATFORMS:
        return False
    platform_lower = platform_name.lower()
    return any(excl in platform_lower for excl in EXCLUDED_PLATFORMS)

def st(x): return (x or "").strip()

def normalize_path(path: str) -> str:
    """
    Normalize a path for comparison.
    - Converts to forward slashes
    - Normalizes Unicode to NFC form (composed characters)
    - Converts to lowercase for case-insensitive comparison
    """
    if not path:
        return ""
    # Normalize Unicode (NFC = composed form, e.g., é as single char not e + combining accent)
    path = unicodedata.normalize('NFC', path)
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')
    # Lowercase for case-insensitive comparison
    return path.lower()

def leafbase(p: str) -> str:
    if not p:
        return ""
    return os.path.splitext(os.path.basename(p))[0]

def to_nas_rel(file_path: str) -> str:
    if not file_path:
        return ""
    p = file_path.replace("\\", "/")
    wr = WIN_ROOT.replace("\\", "/").rstrip("/")
    pl = p.lower()
    wrl = wr.lower()
    if pl == wrl:
        suffix = ""
    elif pl.startswith(wrl + "/"):
        suffix = p[len(wr) + 1:]
    else:
        return ""
    low = suffix.lower()
    for k, v in SUBPATH_OVERRIDES.items():
        if low.startswith(k):
            suffix = v + suffix[len(k):]
            break
    return suffix

_norm_re = re.compile(r"[^a-z0-9]+")

def strip_metadata_tags(title: str) -> str:
    """
    Strip region tags, revision tags, language tags, version numbers, publishers,
    and other ROM metadata from title to enable fuzzy matching.
    This helps match games that differ only in these metadata fields.
    """
    if not title:
        return ""
    
    # Remove version numbers (v1.004, v1.008, etc.) - common in ROM file names
    title = re.sub(r'\s+v\d+\.\d+(?:\.\d+)?', '', title, flags=re.IGNORECASE)
    
    # Remove years in parentheses (1999), (2000), (2001)
    title = re.sub(r'\s*\(\d{4}\)', '', title)
    
    # Remove region tags (USA, Europe, Japan, World, etc.)
    title = re.sub(r'\s*\([^)]*(?:USA|US|Europe|Japan|World|Brazil|Germany|France|UK|Spain|Italy|Canada|Australia|Asia|Korea|China)[^)]*\)', '', title, flags=re.IGNORECASE)
    
    # Remove video standards (NTSC, PAL, SECAM)
    title = re.sub(r'\s*\((?:NTSC|PAL|SECAM)\)', '', title, flags=re.IGNORECASE)
    
    # Remove revision tags
    title = re.sub(r'\s*\(Rev\s+\d+\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\(v\d+(?:\.\d+)*\)', '', title, flags=re.IGNORECASE)
    
    # Remove language tags
    title = re.sub(r'\s*\((?:En|Fr|De|Es|It|Nl|Pt|Ja|Zh|Ko)(?:,(?:En|Fr|De|Es|It|Nl|Pt|Ja|Zh|Ko))*\)', '', title, flags=re.IGNORECASE)
    
    # Remove dump quality markers and flags [!], [b], [t], [h], etc.
    title = re.sub(r'\s*\[[^\]]*[!bthafo\d][^\]]*\]', '', title, flags=re.IGNORECASE)
    
    # Remove disc markers (M5), (Disc 1), (CD1), etc.
    title = re.sub(r'\s*\(M\d+\)', '', title, flags=re.IGNORECASE)
    
    # Remove serial numbers [10S 51035], [6S T-9701NGD], etc.
    title = re.sub(r'\s*\[\d+S\s+[^\]]+\]', '', title, flags=re.IGNORECASE)
    
    # Remove publisher names in parentheses (Sega), (Infogrames), (EIDOS), etc.
    # Only after more specific tags to avoid false positives
    # Matches: (Sega), (EIDOS), (Electronic Arts), etc.
    title = re.sub(r'\s*\([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*\)', '', title)
    
    # Remove "New Zealand" tags
    title = re.sub(r'\s*,\s*New\s+Zealand', '', title, flags=re.IGNORECASE)
    
    # Clean up any double spaces left behind
    title = re.sub(r'\s+', ' ', title)
    
    return title.strip()

def norm(s: str) -> str:
    """
    Normalize string for matching:
    - Unicode NFC normalization (handles é, smart quotes, etc.)
    - Lowercase
    - Strip all non-alphanumeric characters
    """
    # Apply Unicode normalization (NFC) to handle:
    # - Accent variations (é in NFC vs NFD form)
    # - Smart quotes (U+2019 ') vs regular quotes (U+0027 ')
    s = unicodedata.normalize('NFC', st(s))
    # Convert to lowercase and strip all non-alphanumeric characters
    return _norm_re.sub("", s.lower())

def norm_fuzzy(s: str) -> str:
    """
    Normalize string for fuzzy matching by stripping metadata tags first.
    This is more lenient than norm() and helps match regional variants.
    """
    s = strip_metadata_tags(s)
    return norm(s)

# Multi-disc detection patterns
_multidisc_patterns = [
    re.compile(r'\s*\(Disc\s+(\d+)\)', re.IGNORECASE),
    re.compile(r'\s*\(CD\s+(\d+)\)', re.IGNORECASE),
    re.compile(r'\s*\(Disk\s+(\d+)\)', re.IGNORECASE),
    re.compile(r'\s*-\s*Disc\s+(\d+)', re.IGNORECASE),
    re.compile(r'\s*-\s*CD\s+(\d+)', re.IGNORECASE),
    re.compile(r'\s*-\s*Disk\s+(\d+)', re.IGNORECASE),
]

def strip_disc_number(title: str):
    """
    Strip disc/CD number from title and return (base_title, disc_number).
    Returns (original_title, None) if no disc number found.
    """
    for pattern in _multidisc_patterns:
        match = pattern.search(title)
        if match:
            disc_num = int(match.group(1))
            # Only strip if disc number is 2 or higher (we want to keep Disc 1 as-is)
            if disc_num >= 2:
                base_title = pattern.sub('', title).strip()
                return (base_title, disc_num)
    return (title, None)

def strip_year_suffix(name: str) -> str:
    # Remove trailing " [YYYY]" if present
    m = re.match(r"^(.*)\s\[\d{4}\]$", st(name))
    return m.group(1) if m else st(name)

def normalize_platform_name(platform: str) -> str:
    """
    Normalize platform name for matching.
    Strips year suffix, path prefixes, and parenthetical variants to get clean platform name.
    """
    if not platform:
        return ""
    
    # First strip year suffix if present
    platform_clean = strip_year_suffix(platform)
    
    # Special handling for Arcade sub-platforms (MAME variants)
    # Arcade/MAME 0.256 Romset Merged -> Arcade
    if "/" in platform_clean:
        parts = platform_clean.split("/")
        # If first part is Arcade, use that as the platform name
        if parts[0].lower() == "arcade":
            return "Arcade"
    
    # Remove path prefixes (Consoles/, Handhelds/, Computers/)
    if "/" in platform_clean:
        parts = platform_clean.split("/")
        platform_clean = parts[-1] if len(parts) > 1 else platform_clean
    
    # Strip parenthetical variants: "NEC TurboGrafx-16 (PC Engine)" -> "NEC TurboGrafx-16"
    # This handles cases where filesystem has regional variants but LaunchBox doesn't
    platform_clean = re.sub(r'\s*\([^)]+\)\s*', ' ', platform_clean).strip()
    
    # Return cleaned version (preserves original case)
    return platform_clean

def inv_platform_to_lb_platform(inv_platform: str) -> str:
    # From "Consoles/Sony PlayStation 3 [2006]" -> "Sony PlayStation 3"
    # Now uses platform normalization to handle name variations
    return normalize_platform_name(inv_platform)

def read_all_platforms(csv_path: Path):
    # Build indices by platform:
    # - by normalized title
    # - by normalized shortname
    # - by normalized file basename
    by_platform = {}
    by_naspath = defaultdict(list)  # rel path (cf) -> rows
    by_parent = defaultdict(list)   # parent dir (cf) -> rows
    if not csv_path.exists():
        print(f"ERROR: Platforms CSV not found: {csv_path}", file=sys.stderr)
        return by_platform, [], by_naspath, by_parent
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        lb_headers = list(r.fieldnames or [])
        # Map LB platform normalized key to canonical platform name
        plat_key_to_name = {}
        for row in r:
            plat = st(row.get("Platform"))
            title = st(row.get("Title"))
            # LBFilePath contains the full Windows path (e.g., Z:\...\game.exe)
            fpath = st(row.get("LBFilePath"))
            shortname = st(row.get("Shortname"))
            gid = st(row.get("ID"))
            if not plat:
                continue
            # Normalize platform name first, then apply norm()
            plat_normalized = normalize_platform_name(plat)
            plat_key = norm(plat_normalized)
            plat_key_to_name.setdefault(plat_key, plat_normalized)
            pidx = by_platform.setdefault(plat_key, {
                "name": plat_key_to_name[plat_key],
                "by_title": defaultdict(list),
                "by_shortname": defaultdict(list),
                "by_basename": defaultdict(list),
                "by_basetitle": defaultdict(list),  # title with disc number stripped
                "rows": [],
            })
            # Use LBFilePath if available, otherwise fall back to Filename
            base = leafbase(fpath) if fpath else leafbase(st(row.get("Filename")))
            pidx["rows"].append(row)
            nas_rel = st(row.get("NASPath"))
            if not nas_rel:
                nas_rel = to_nas_rel(fpath)
                row["NASPath"] = nas_rel
                if "NASPath" not in lb_headers:
                    lb_headers.append("NASPath")
            if title:
                pidx["by_title"][norm(title)].append(row)
            if shortname:
                pidx["by_shortname"][norm(shortname)].append(row)
            if base:
                pidx["by_basename"][norm(base)].append(row)
                # Also index by base filename (disc number stripped) for multi-disc matching
                # We need to strip ALL disc numbers (including Disc 1) for the index
                base_for_index = base
                for pattern in _multidisc_patterns:
                    base_for_index = pattern.sub('', base_for_index).strip()
                if base_for_index != base:
                    pidx["by_basetitle"][norm(base_for_index)].append(row)
            if nas_rel:
                key = normalize_path(nas_rel)
                by_naspath[key].append(row)
                
                # For folder-based platforms (PS3, MS-DOS, etc.), also index by ALL ancestor folders
                # This allows inventory folders to match against LaunchBox files deep inside those folders
                # Example: Inventory has "Game", LB has "Game/Sub/Deep/file.bin"
                #          Add entries for: "Game/Sub/Deep", "Game/Sub", and "Game"
                current = nas_rel
                for _ in range(10):  # Limit depth
                    parent = os.path.dirname(current)
                    if not parent or parent == current:
                        break
                    parent_key = normalize_path(parent)
                    by_parent[parent_key].append(row)
                    by_naspath[parent_key].append(row)
                    current = parent
    return by_platform, lb_headers, by_naspath, by_parent

def read_inventory(csv_path: Path):
    """Read NAS inventory CSV (generated by audit_library.py nas-inventory command)."""
    items = []
    excluded_count = 0
    if not csv_path.exists():
        print(f"ERROR: NAS Inventory CSV not found: {csv_path}", file=sys.stderr)
        print(f"       Run: python3 audit_library.py nas-inventory", file=sys.stderr)
        return items
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            # Handle both lowercase (nas_inventory.csv) and title-case (legacy) column names
            platform = st(row.get("platform") or row.get("Platform"))
            
            # Skip excluded platforms
            if is_platform_excluded(platform):
                excluded_count += 1
                continue
            
            # Parse FileSize as integer (default to 0 if missing or invalid)
            file_size = 0
            try:
                file_size = int(row.get("size_bytes") or row.get("FileSize") or "0")
            except ValueError:
                pass
            
            items.append({
                "Platform": platform,
                "Title": st(row.get("title") or row.get("Title")),
                "RelPath": st(row.get("rel_path") or row.get("RelPath")),
                "FileSize": file_size,
            })
    
    if excluded_count > 0:
        print(f"  ⊘ Filtered out {excluded_count} entries from excluded platforms")
    
    return items

def choose_best_match(cands_title, cands_short, cands_base):
    # Prefer title matches, else shortname, else basename; if multiple, keep first
    if cands_title:
        return cands_title[0], "title"
    if cands_short:
        return cands_short[0], "shortname"
    if cands_base:
        return cands_base[0], "basename"
    return None, ""

def build_master(by_platform, lb_headers, by_naspath, by_parent, inventory_items):
    out_rows = []
    seen_rel = set()
    matched_count = 0
    unmatched_count = 0
    lb_used_keys = set()
    
    # Track detailed match statistics
    match_type_counts = {
        'matched': {},      # MatchType -> count (for "Yes")
        'expected': {},     # MatchType -> count (for "Expected")
        'unknown': 0        # Count for "No" (truly unmatched)
    }

    def lb_row_key(row: dict) -> str:
        # Prefer stable ID; fall back to NASPath then FilePath
        rid = st(row.get("ID"))
        if rid:
            return f"id:{rid}"
        nasp = normalize_path(st(row.get("NASPath")))
        if nasp:
            return f"nas:{nasp}"
        fp = normalize_path(st(row.get("FilePath")))
        if fp:
            return f"fp:{fp}"
        # Finally use normalized title + platform
        return f"tp:{norm(row.get('Platform',''))}:{norm(row.get('Title',''))}"
    for it in inventory_items:
        rel = it["RelPath"]
        if not rel:
            continue
        rel_key = normalize_path(rel)
        if rel_key in seen_rel:
            continue
        seen_rel.add(rel_key)

        inv_plat = it["Platform"]
        inv_title = it["Title"]
        lb_plat_guess = inv_platform_to_lb_platform(inv_plat)
        lb_plat_key = norm(lb_plat_guess)
        pidx = by_platform.get(lb_plat_key)

        matched = False
        match_row = None
        match_kind = ""
        # Path-first matching
        cands = by_naspath.get(rel_key, [])
        if cands:
            match_row = cands[0]
            match_kind = "relpath"
            matched = True
            lb_used_keys.add(lb_row_key(match_row))
            # No direct path match found - will fall through to title-based matching
        # Fallback to title-based within guessed platform
        if pidx and inv_title and not matched:
            t = norm(inv_title)
            cands_title = pidx["by_title"].get(t, [])
            cands_short = pidx["by_shortname"].get(t, [])
            cands_base = pidx["by_basename"].get(t, [])
            match_row, match_kind = choose_best_match(cands_title, cands_short, cands_base)
            matched = match_row is not None
            if matched:
                lb_used_keys.add(lb_row_key(match_row))
        
        # Multi-disc fallback: try matching with disc number stripped
        if pidx and inv_title and not matched:
            base_title, disc_num = strip_disc_number(inv_title)
            if disc_num is not None:
                # Try matching the base title against both exact matches and base title index
                t_base = norm(base_title)
                cands_title = pidx["by_title"].get(t_base, [])
                cands_short = pidx["by_shortname"].get(t_base, [])
                cands_base = pidx["by_basename"].get(t_base, [])
                cands_basetitle = pidx["by_basetitle"].get(t_base, [])
                
                # Combine all candidates
                all_cands = cands_title + cands_short + cands_base + cands_basetitle
                if all_cands:
                    match_row = all_cands[0]
                    matched = True
                    match_kind = f"multidisc_{disc_num}"
                    lb_used_keys.add(lb_row_key(match_row))
        
        # Fuzzy matching fallback: try matching with metadata tags stripped (region, revision, language)
        if pidx and inv_title and not matched:
            t_fuzzy = norm_fuzzy(inv_title)
            if t_fuzzy:  # Only try if we have something after stripping
                # Build a fuzzy index on-the-fly for this platform if not already done
                if "by_title_fuzzy" not in pidx:
                    pidx["by_title_fuzzy"] = defaultdict(list)
                    for row in pidx["by_title"].values():
                        for r in row:
                            title_fuzzy = norm_fuzzy(r.get("Title", ""))
                            if title_fuzzy:
                                pidx["by_title_fuzzy"][title_fuzzy].append(r)
                
                cands_fuzzy = pidx["by_title_fuzzy"].get(t_fuzzy, [])
                if cands_fuzzy:
                    match_row = cands_fuzzy[0]
                    matched = True
                    match_kind = "fuzzy"
                    lb_used_keys.add(lb_row_key(match_row))

        # Extract file information from matched LaunchBox row or inventory
        if matched:
            lb_filepath = st(match_row.get("LBFilePath"))
            file_ext = st(match_row.get("FileExtension"))
            nas_path = st(match_row.get("NASPath"))
            
            # For multi-disc matches, use the NAS filename (Disc 2, 3, etc.) not the LaunchBox filename (Disc 1)
            if match_kind.startswith("multidisc_"):
                filename = os.path.basename(rel.replace("\\", "/")) if rel else ""
                file_ext = os.path.splitext(filename)[1] if filename else ""
                nas_path = rel
            else:
                filename = st(match_row.get("Filename"))
        else:
            lb_filepath = ""
            filename = os.path.basename(rel.replace("\\", "/")) if rel else ""
            file_ext = os.path.splitext(filename)[1] if filename else ""
            nas_path = rel
        
        # Determine MatchType and Matched status
        if matched:
            final_match_type = match_kind
            match_status = "Yes"
            # Track matched types
            match_type_counts['matched'][final_match_type] = match_type_counts['matched'].get(final_match_type, 0) + 1
        else:
            # Tag unmatched Arcade ROMs as MAME non-games
            if lb_plat_guess == "Arcade":
                final_match_type = "mame_not_game"
                match_status = "Expected"
                match_type_counts['expected'][final_match_type] = match_type_counts['expected'].get(final_match_type, 0) + 1
            else:
                final_match_type = ""
                match_status = "No"
                match_type_counts['unknown'] += 1
        
        base = {
            # Inventory columns (file-focused)
            "Filename": filename,
            "RelPath": rel,
            "LBFilePath": lb_filepath,
            "NASPath": nas_path,
            "FileExtension": file_ext,
            "FileSize": it.get("FileSize", 0),
            "Matched": match_status,
            "MatchType": final_match_type,
        }
        
        # Preserve all all_platforms columns (metadata)
        # Skip file columns since they're already set in base dict above
        file_columns = {"Filename", "RelPath", "LBFilePath", "NASPath", "FileExtension", "FileSize"}
        for col in lb_headers:
            if col in file_columns:
                continue  # Already set in base dict
            if matched:
                base[col] = match_row.get(col, "")
            else:
                # For unmatched rows, preserve Platform and Title from inventory if available
                if col == "Platform":
                    base[col] = lb_plat_guess  # Use the cleaned platform name
                elif col == "Title":
                    base[col] = inv_title
                else:
                    base[col] = ""
        
        # Add new control columns (blank for now)
        base["ManualInclude"] = ""
        base["ManualExclude"] = ""
        
        out_rows.append(base)
        if matched:
            matched_count += 1
        else:
            unmatched_count += 1
    # Append LB-only rows that were not matched to any inventory path
    lb_only_count = 0
    storefront_count = 0
    lb_pc_count = 0
    for pidx in by_platform.values():
        for row in pidx["rows"]:
            key = lb_row_key(row)
            if key in lb_used_keys:
                continue
            # Populate inventory-side columns from LB so these rows are visible and filterable
            lb_filepath = st(row.get("LBFilePath"))
            filename = st(row.get("Filename"))
            file_ext = st(row.get("FileExtension"))
            lb_rel = st(row.get("NASPath")) or to_nas_rel(st(row.get("LBFilePath")))
            platform = st(row.get("Platform"))
            
            # Determine match type for Windows/MS-DOS games
            match_type = "lb_only"
            match_status = "Expected"  # LB-only items are expected to not have filesystem matches
            
            if platform in ["Windows", "MS-DOS"]:
                # Check if it's a storefront/cloud game
                lb_filepath_lower = lb_filepath.lower()
                if any(x in lb_filepath_lower for x in [
                    "steam://",
                    "uplay://",
                    "com.epicgames.launcher://",
                    "gog galaxy\\games\\",
                    "gog.com",
                ]):
                    match_type = "storefront"
                    storefront_count += 1
                # Check if it's a local PC game (Savvy directory)
                elif "savvy" in lb_filepath_lower or "\\savvy\\" in lb_filepath_lower:
                    match_type = "lb_pc"
                    lb_pc_count += 1
                else:
                    lb_only_count += 1
            else:
                lb_only_count += 1
            
            # Track expected non-matches
            match_type_counts['expected'][match_type] = match_type_counts['expected'].get(match_type, 0) + 1
            
            base = {
                # Inventory columns (file-focused)
                "Filename": filename,
                "RelPath": lb_rel,
                "LBFilePath": lb_filepath,
                "NASPath": lb_rel,
                "FileExtension": file_ext,
                "FileSize": 0,  # LB-only games don't have file size from inventory
                "Matched": match_status,
                "MatchType": match_type,
            }
            
            # Preserve all all_platforms columns (metadata)
            for col in lb_headers:
                base[col] = row.get(col, "")
            
            # Add new control columns (blank for now)
            base["ManualInclude"] = ""
            base["ManualExclude"] = ""
            
            out_rows.append(base)
    return out_rows, matched_count, unmatched_count, lb_only_count, storefront_count, lb_pc_count, match_type_counts

def write_csv(path: Path, rows: list[dict], lb_headers: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Column order:
    # 1. Platform (first)
    # 2. Filename
    # 3. All metadata columns (excluding Platform and file-related columns)
    # 4. Matched/MatchType
    # 5. New metadata/control columns
    # 6. File path columns at the end: RelPath, LBFilePath, NASPath, FileExtension, FileSize
    
    file_columns = {"Filename", "RelPath", "LBFilePath", "NASPath", "FileExtension", "FileSize", "Platform"}
    metadata_headers = [h for h in lb_headers if h not in file_columns]
    
    header = (
        ["Platform", "Filename"] +
        metadata_headers + 
        ["Matched", "MatchType"] +
        ["ManualInclude", "ManualExclude"] +
        ["RelPath", "LBFilePath", "NASPath", "FileExtension", "FileSize"]
    )
    
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)

def main():
    # Load config at runtime (not at import time) to get fresh values
    load_config()
    
    print("Loading all_platforms ...")
    by_platform, lb_headers, by_naspath, by_parent = read_all_platforms(PLATFORMS_CSV)
    print(f"  ✓ Loaded {len(by_platform)} platform(s)")
    
    print("\nLoading inventory ...")
    inventory_items = read_inventory(INVENTORY_CSV)
    print(f"  ✓ Loaded {len(inventory_items)} inventory item(s)")
    
    print("\nReconciling LaunchBox data with filesystem inventory...")
    rows, matched_count, unmatched_count, lb_only_count, storefront_count, lb_pc_count, match_type_counts = build_master(by_platform, lb_headers, by_naspath, by_parent, inventory_items)
    
    print(f"\nWriting master inventory...")
    write_csv(OUTPUT_CSV, rows, lb_headers)
    
    # Calculate totals by status
    total_matched = sum(match_type_counts['matched'].values())
    total_expected = sum(match_type_counts['expected'].values())
    total_unknown = match_type_counts['unknown']
    
    # Print enhanced summary
    print("\n" + "=" * 60)
    print("MASTER INVENTORY COMPLETE")
    print("=" * 60)
    print(f"Total entries:        {len(rows):,}")
    print()
    
    # Matched breakdown
    print(f"Matched (Yes):        {total_matched:,}")
    if match_type_counts['matched']:
        for match_type in sorted(match_type_counts['matched'].keys()):
            count = match_type_counts['matched'][match_type]
            print(f"  - {match_type:20} {count:,}")
    print()
    
    # Expected non-matches breakdown
    print(f"Expected (No Match):  {total_expected:,}")
    if match_type_counts['expected']:
        for match_type in sorted(match_type_counts['expected'].keys()):
            count = match_type_counts['expected'][match_type]
            print(f"  - {match_type:20} {count:,}")
    print()
    
    # Unknown non-matches (needs investigation!)
    print(f"Unknown (No Match):   {total_unknown:,}  ← INVESTIGATE")
    
    print(f"\nOutput: {OUTPUT_CSV}")
    print("=" * 60)

if __name__ == "__main__":
    main()


