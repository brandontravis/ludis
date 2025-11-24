#!/usr/bin/env python3
import csv, os, sys
from pathlib import Path
import xml.etree.ElementTree as ET

# Project root for config loading
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# These will be loaded from config.yaml
CONFIG = {}
DEFAULT_ROOT = r"./"
WIN_ROOT = ""
SUBPATH_OVERRIDES = {}  # Path overrides (loaded from config)

# Load configuration
def load_config():
    """Load configuration from config.yaml"""
    global CONFIG, WIN_ROOT, DEFAULT_ROOT, SUBPATH_OVERRIDES
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if config_path.exists():
            with open(config_path) as f:
                CONFIG = yaml.safe_load(f)
                
                # Load paths from config
                paths = CONFIG.get('paths', {})
                WIN_ROOT = paths.get('windows_root', '')
                launchbox_data = paths.get('launchbox_data', 'Data/')
                
                # Set DEFAULT_ROOT based on launchbox_data
                if not Path(launchbox_data).is_absolute():
                    DEFAULT_ROOT = str(PROJECT_ROOT / launchbox_data)
                else:
                    DEFAULT_ROOT = launchbox_data
                
                # Load path overrides (for files that moved after LaunchBox import)
                path_overrides = CONFIG.get('options', {}).get('path_overrides', {})
                if path_overrides:
                    SUBPATH_OVERRIDES.update(path_overrides)
                    print(f"✓ Loaded {len(path_overrides)} path override(s)")
                
                if not WIN_ROOT:
                    print("Warning: windows_root not configured in config.yaml")
                
                return True
    except Exception as e:
        print(f"Warning: Could not load config.yaml: {e}")
    return False

def load_excluded_platforms():
    """Load platform exclusions from config.yaml"""
    excluded = CONFIG.get('options', {}).get('exclude_platforms', [])
    return [p.lower() for p in excluded]

# Load config first
load_config()
EXCLUDED_PLATFORMS = load_excluded_platforms()
if EXCLUDED_PLATFORMS:
    print(f"⚠ Excluding platforms: {', '.join(EXCLUDED_PLATFORMS)}")

def is_platform_excluded(platform_name: str) -> bool:
    """Check if a platform should be excluded"""
    if not EXCLUDED_PLATFORMS:
        return False
    platform_lower = platform_name.lower()
    return any(excl in platform_lower for excl in EXCLUDED_PLATFORMS)

def st(x):
    """Safe text extraction - strip and return empty string if None"""
    return (x or "").strip()

def leafbase(p: str) -> str:
    return os.path.splitext(os.path.basename(p))[0] if p else ""

def to_nas_rel(file_path: str) -> str:
    """
    Produce a NAS-relative path (same formatting as inventory RelPath), based on a
    Windows-style absolute path inside WIN_ROOT. Returns "" if mapping is not possible.
    """
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

def detect_windows_game_type(app_path: str, nas_path: str) -> dict:
    """
    Detect the type of Windows game (storefront launcher, manual install, or standalone).
    
    Args:
        app_path: Application path from LaunchBox XML
        nas_path: NAS/relative path for the game
    
    Returns:
        dict with keys: type, storefront, method
    """
    if not app_path:
        return {'type': 'unknown', 'storefront': '', 'method': ''}
    
    app_lower = app_path.lower()
    
    # Check for storefront launchers
    if app_path.startswith('steam://'):
        return {'type': 'steam', 'storefront': 'Steam', 'method': 'launcher'}
    elif 'epicgames.com' in app_lower:
        return {'type': 'epic', 'storefront': 'Epic Games', 'method': 'launcher'}
    elif 'gog.com' in app_lower or 'galaxyclient' in app_lower:
        return {'type': 'gog', 'storefront': 'GOG', 'method': 'launcher'}
    elif 'ea.com' in app_lower or 'origin' in app_lower:
        return {'type': 'origin', 'storefront': 'EA/Origin', 'method': 'launcher'}
    elif 'ubisoft' in app_lower or 'uplay' in app_lower:
        return {'type': 'ubisoft', 'storefront': 'Ubisoft Connect', 'method': 'launcher'}
    
    # File-based games
    if app_path.endswith('.exe'):
        # Check if it's in a folder structure (manual install) or standalone
        if nas_path and '/' in nas_path:
            return {'type': 'manual_install', 'storefront': '', 'method': 'manual'}
        else:
            return {'type': 'standalone', 'storefront': '', 'method': 'portable'}
    
    return {'type': 'unknown', 'storefront': '', 'method': ''}


def collect_all_custom_fields(plat_dir: Path) -> list[str]:
    """
    Scan all platform XMLs to collect unique custom field names.
    Returns sorted list of custom field names found across all platforms.
    """
    all_custom_fields = set()
    
    for xml in plat_dir.glob("*.xml"):
        try:
            tree = ET.parse(xml)
            root = tree.getroot()
            for cf in root.findall(".//CustomField"):
                name = st(cf.findtext("Name"))
                if name:
                    all_custom_fields.add(name)
        except ET.ParseError:
            continue
    
    return sorted(all_custom_fields)

def parse_platform_xml(xml_path: Path, platform_name: str, custom_field_names: list[str] = None) -> list[dict]:
    rows = []
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as e:
        print(f"  ✗ ERROR: Failed to parse {xml_path.name}: {e}")
        return rows
    root = tree.getroot()
    
    # Build a map of GameID -> custom fields
    custom_fields_by_game = {}
    for cf in root.findall(".//CustomField"):
        game_id = st(cf.findtext("GameID"))
        name = st(cf.findtext("Name"))
        value = st(cf.findtext("Value"))
        if game_id and name:
            if game_id not in custom_fields_by_game:
                custom_fields_by_game[game_id] = {}
            custom_fields_by_game[game_id][name] = value
    
    for g in root.findall(".//Game"):
        # File Information
        path = st(g.findtext("ApplicationPath"))
        filename = os.path.basename(path.replace("\\", "/")) if path else ""
        rel_path = to_nas_rel(path)
        file_ext = os.path.splitext(filename)[1] if filename else ""
        
        # Metadata Information
        title = st(g.findtext("Title"))
        developer = st(g.findtext("Developer"))
        publisher = st(g.findtext("Publisher"))
        region = st(g.findtext("Region"))
        release_date = st(g.findtext("ReleaseDate"))
        lb_id = st(g.findtext("ID"))
        favorite = st(g.findtext("Favorite"))
        notes = st(g.findtext("Notes"))
        rating = st(g.findtext("Rating"))
        star_rating = st(g.findtext("StarRating"))
        star_rating_float = st(g.findtext("StarRatingFloat"))
        community_star_rating = st(g.findtext("CommunityStarRating"))
        community_star_rating_votes = st(g.findtext("CommunityStarRatingTotalVotes"))
        wikipedia_url = st(g.findtext("WikipediaURL"))
        version = st(g.findtext("Version"))
        play_mode = st(g.findtext("PlayMode"))
        genre = st(g.findtext("Genre"))
        max_players = st(g.findtext("MaxPlayers"))
        
        # Get custom fields for this game
        custom_fields = custom_fields_by_game.get(lb_id, {})
        
        # Detect Windows game type if this looks like a Windows game
        # (has .exe, steam:// URL, or other Windows indicators)
        windows_info = {'type': '', 'storefront': '', 'method': ''}
        if path and (path.lower().endswith('.exe') or 'steam://' in path.lower() or 
                     any(storefront in path.lower() for storefront in ['epicgames.com', 'gog.com', 'origin', 'uplay', 'ubisoft'])):
            windows_info = detect_windows_game_type(path, rel_path)
        
        # Build base row with metadata
        row = {
            # Metadata Information
            "Platform": platform_name,
            "Title": title,
            "Developer": developer,
            "Publisher": publisher,
            "Region": region,
            "ReleaseDate": release_date,
            "LBID": lb_id,
            "Favorite": favorite,
            "Notes": notes,
            "Rating": rating,
            "StarRating": star_rating,
            "StarRatingFloat": star_rating_float,
            "CommunityStarRating": community_star_rating,
            "CommunityStarRatingTotalVotes": community_star_rating_votes,
            "WikipediaURL": wikipedia_url,
            "Version": version,
            "PlayMode": play_mode,
            "Genre": genre,
            "MaxPlayers": max_players,
            # Windows-specific fields
            "WindowsGameType": windows_info['type'],
            "WindowsStorefront": windows_info['storefront'],
            "WindowsInstallMethod": windows_info['method'],
        }
        
        # Add all discovered custom fields dynamically
        if custom_field_names:
            for field_name in custom_field_names:
                sanitized_name = field_name.replace(" ", "_").replace("-", "_")
                row[f"CUSTOM_{sanitized_name}"] = custom_fields.get(field_name, "")
        
        # Add file information
        row.update({
            "Filename": filename,
            "RelPath": rel_path,
            "LBFilePath": path,
            "FileExtension": file_ext,
        })
        
        rows.append(row)
    return rows

def write_csv(path: Path, rows: list[dict], header: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Export ALL LaunchBox Platforms to CSVs (+ combined).")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="LaunchBox root (default: %(default)s)")
    ap.add_argument("--outdir", default="LB_Exports/platforms", help="Output directory for per-platform CSVs")
    ap.add_argument("--combined", default="LB_Exports/all_platforms.csv", help="Combined CSV path")
    args = ap.parse_args()

    root = Path(args.root)
    plat_dir = root / "Platforms"
    if not plat_dir.exists():
        print(f"ERROR: Platforms dir not found: {plat_dir}", file=sys.stderr)
        sys.exit(2)

    # First pass: collect all unique custom field names
    print("Scanning for custom fields...")
    custom_field_names = collect_all_custom_fields(plat_dir)
    print(f"Found {len(custom_field_names)} unique custom field(s)")
    if custom_field_names:
        print(f"  Custom fields: {', '.join(custom_field_names[:10])}")
        if len(custom_field_names) > 10:
            print(f"  ... and {len(custom_field_names) - 10} more")
    
    # Build header dynamically
    header = [
        # Metadata Information
        "Platform",
        "Title",
        "Developer",
        "Publisher",
        "Region",
        "ReleaseDate",
        "LBID",
        "Favorite",
        "Notes",
        "Rating",
        "StarRating",
        "StarRatingFloat",
        "CommunityStarRating",
        "CommunityStarRatingTotalVotes",
        "WikipediaURL",
        "Version",
        "PlayMode",
        "Genre",
        "MaxPlayers",
        # Windows-specific fields
        "WindowsGameType",
        "WindowsStorefront",
        "WindowsInstallMethod",
    ]
    
    # Add custom field columns dynamically
    for field_name in custom_field_names:
        sanitized_name = field_name.replace(" ", "_").replace("-", "_")
        header.append(f"CUSTOM_{sanitized_name}")
    
    # Add file information columns
    header.extend([
        "Filename",
        "RelPath",
        "LBFilePath",
        "FileExtension",
    ])
    
    # Second pass: parse all platforms with discovered custom fields
    print("\nProcessing platforms...")
    all_rows = []
    platforms_exported = 0
    platforms_skipped = 0
    
    for xml in sorted(plat_dir.glob("*.xml")):
        platform_name = xml.stem
        
        # Skip excluded platforms
        if is_platform_excluded(platform_name):
            print(f"⊘ Skipping excluded platform: {platform_name}")
            platforms_skipped += 1
            continue
        
        rows = parse_platform_xml(xml, platform_name, custom_field_names)
        all_rows.extend(rows)
        out_path = Path(args.outdir) / f"{platform_name}.csv"
        write_csv(out_path, rows, header)
        print(f"  ✓ {platform_name}: {len(rows)} games")
        platforms_exported += 1

    write_csv(Path(args.combined), all_rows, header)
    
    # Print summary
    print("\n" + "=" * 60)
    print("EXPORT COMPLETE")
    print("=" * 60)
    print(f"Platforms exported: {platforms_exported}")
    if platforms_skipped > 0:
        print(f"Platforms skipped:  {platforms_skipped}")
    print(f"Total games:        {len(all_rows):,}")
    print(f"Combined CSV:       {args.combined}")
    print("=" * 60)

if __name__ == "__main__":
    main()
