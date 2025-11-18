#!/usr/bin/env python3
import csv, os, sys
from pathlib import Path
import xml.etree.ElementTree as ET

# Project root for config loading
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_ROOT = r"./"
WIN_ROOT = r"Z:\media\games\library"

# Load exclusions from config
def load_excluded_platforms():
    """Load platform exclusions from config.yaml"""
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if config_path.exists():
            with open(config_path) as f:
                config = yaml.safe_load(f)
                excluded = config.get('options', {}).get('exclude_platforms', [])
                return [p.lower() for p in excluded]
    except Exception as e:
        print(f"Warning: Could not load exclusions from config.yaml: {e}")
    return []

EXCLUDED_PLATFORMS = load_excluded_platforms()
if EXCLUDED_PLATFORMS:
    print(f"⚠ Excluding platforms: {', '.join(EXCLUDED_PLATFORMS)}")

def is_platform_excluded(platform_name: str) -> bool:
    """Check if a platform should be excluded"""
    if not EXCLUDED_PLATFORMS:
        return False
    platform_lower = platform_name.lower()
    return any(excl in platform_lower for excl in EXCLUDED_PLATFORMS)
# We only need the relative path (same as inventory's RelPath), so NAS_ROOT is not required here.
# Apply known Windows→NAS folder name overrides for relative prefix normalization.
SUBPATH_OVERRIDES = {
    # case-insensitive key -> cased replacement
    "consoles/nec - turbografx 16 - pc engine [1987]": "consoles/NEC TurboGrafx 16 (PC Engine) [1987]",
}

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

def parse_platform_xml(xml_path: Path, platform_name: str) -> list[dict]:
    rows = []
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError:
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
        
        rows.append({
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
            
            # Custom Fields
            "CUSTOM_The Best": custom_fields.get("The Best", ""),
            "CUSTOM_All Time Favorites": custom_fields.get("All Time Favorites", ""),
            "CUSTOM_Backlog": custom_fields.get("Backlog", ""),
            "CUSTOM_GOTY Winner": custom_fields.get("GOTY Winner", ""),
            "CUSTOM_GOTY Nominee": custom_fields.get("GOTY Nominee", ""),
            "CUSTOM_On Deck": custom_fields.get("On Deck", ""),
            "CUSTOM_Retro Collection": custom_fields.get("Retro Collection", ""),
            "CUSTOM_Finished": custom_fields.get("Finished", ""),
            
            # File Information
            "Filename": filename,
            "RelPath": rel_path,
            "LBFilePath": path,
            "NASPath": rel_path,  # Same as RelPath for now
            "FileExtension": file_ext,
        })
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
    plat_dir = root / "Data" / "Platforms"
    if not plat_dir.exists():
        print(f"ERROR: Platforms dir not found: {plat_dir}", file=sys.stderr)
        sys.exit(2)

    # Define column order matching your specification
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
        
        # Custom Fields
        "CUSTOM_The Best",
        "CUSTOM_All Time Favorites",
        "CUSTOM_Backlog",
        "CUSTOM_GOTY Winner",
        "CUSTOM_GOTY Nominee",
        "CUSTOM_On Deck",
        "CUSTOM_Retro Collection",
        "CUSTOM_Finished",
        
        # File Information
        "Filename",
        "RelPath",
        "LBFilePath",
        "NASPath",
        "FileExtension",
    ]
    
    all_rows = []
    for xml in sorted(plat_dir.glob("*.xml")):
        platform_name = xml.stem
        
        # Skip excluded platforms
        if is_platform_excluded(platform_name):
            print(f"⊘ Skipping excluded platform: {platform_name}")
            continue
        
        rows = parse_platform_xml(xml, platform_name)
        all_rows.extend(rows)
        out_path = Path(args.outdir) / f"{platform_name}.csv"
        write_csv(out_path, rows, header)
        print(f"Wrote {out_path} ({len(rows)} rows)")

    write_csv(Path(args.combined), all_rows, header)
    print(f"Wrote {args.combined} ({len(all_rows)} rows)")

if __name__ == "__main__":
    main()
