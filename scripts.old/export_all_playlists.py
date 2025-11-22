#!/usr/bin/env python3
import csv, os, sys
from pathlib import Path
import xml.etree.ElementTree as ET

# Project root for config loading
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DEFAULT_ROOT = r"./"
OUTDIR_DEFAULT = "LB_Exports/playlists"
COMBINED_DEFAULT = "LB_Exports/all_playlists.csv"

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

def leafbase(p: str) -> str:
    return os.path.splitext(os.path.basename(p))[0] if p else ""

def st(x):  # safe text
    return (x or "").strip()

def get_text(elem, tag_candidates):
    for t in tag_candidates:
        v = elem.findtext(t)
        if v:
            return v.strip()
    return ""

def parse_custom_fields(game_elem) -> dict:
    custom = {}
    cf = game_elem.find("CustomFields")
    if cf is None:
        return custom
    for c in cf.findall("CustomField"):
        name = st(c.findtext("Name"))
        val = st(c.findtext("Value"))
        if name:
            custom[name] = val
    return custom

def index_all_platforms(platforms_dir: Path) -> dict:
    """ID -> info (Title/FilePath/Developer/Publisher/Region/ReleaseDate/Platform + extras)."""
    idx = {}
    if not platforms_dir.exists():
        return idx
    for xml in platforms_dir.glob("*.xml"):
        try:
            tree = ET.parse(xml)
        except ET.ParseError:
            continue
        root = tree.getroot()
        plat_name = xml.stem
        
        # Build a map of GameID -> custom fields (stored at root level)
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
            gid = st(g.findtext("ID"))
            if not gid:
                continue
            title = st(g.findtext("Title"))
            path  = st(g.findtext("ApplicationPath"))
            idx[gid] = {
                "Platform": plat_name,
                "Title": title,
                "FilePath": path,
                "Shortname": leafbase(path),
                "Developer": st(g.findtext("Developer")),
                "Publisher": st(g.findtext("Publisher")),
                "Region": st(g.findtext("Region")),
                "ReleaseDate": st(g.findtext("ReleaseDate")),
                # common filterable fields
                "Genre": st(g.findtext("Genre")),
                "Series": st(g.findtext("Series")),
                "PlayMode": st(g.findtext("PlayMode")),
                "Favorite": st(g.findtext("Favorite")),
                "Installed": st(g.findtext("Installed")),
                "Status": st(g.findtext("Status")),
                "LastPlayed": st(g.findtext("LastPlayed")),
                "PlayCount": st(g.findtext("PlayCount")),
                "Custom": custom_fields_by_game.get(gid, {}),
                "ID": gid,
            }
    return idx

def playlist_title(root, fallback):
    # Try several spots - prefer Name over Title
    p = root.find(".//Playlist")
    if p is not None:
        # Try Name first (LaunchBox standard field)
        name = st(p.findtext("Name"))
        if name: return name
        # Fallback to Title
        t = st(p.findtext("Title"))
        if t: return t
    t = st(root.findtext("Title"))
    return t or fallback

def iter_playlist_entries(root):
    """
    Yield possible playlist entries from multiple shapes:
    - <PlaylistGame>…</PlaylistGame>
    - <Game>…</Game> (older/handmade)
    """
    # Any tag ending with PlaylistGame (case-insensitive)
    for e in root.iter():
        if e.tag.lower().endswith("playlistgame"):
            yield e
    # Some files embed <Game> directly under playlist
    for e in root.iter("Game"):
        # Avoid picking up the <Game> elements from platform XMLs mistakenly;
        # playlist XMLs usually wrap with a <Playlist> parent.
        yield e

def row_from_elem(e, idx):
    # Try all common field names
    gid = get_text(e, ["GameId","GameID","ID"])
    title = get_text(e, ["Title"])
    platform = ""

    # Resolve missing fields via index if we have an ID
    if gid:
        info = idx.get(gid)
        if info:
            title = title or info.get("Title","")
            platform = info.get("Platform","")

    return {
        "Platform": platform,
        "Title": title,
        "LBID": gid,
    }

def write_csv(path: Path, rows: list[dict], header):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def append_csv(path: Path, rows: list[dict], header):
    new = not path.exists()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=header, extrasaction="ignore")
        if new:
            w.writeheader()
        for r in rows:
            w.writerow(r)

def parse_playlist_filters(root) -> list[dict]:
    """Extract filters from <PlaylistFilter> entries (FieldKey, ComparisonTypeKey, Value)."""
    filters = []
    for pf in root.findall(".//PlaylistFilter"):
        filters.append({
            "field": st(pf.findtext("FieldKey")),
            "op": st(pf.findtext("ComparisonTypeKey")),
            "value": st(pf.findtext("Value")),
        })
    return filters

def should_skip_playlist(root_xml) -> tuple[bool, str]:
    """
    Determine if a playlist should be skipped.
    Returns: (should_skip: bool, reason: str)
    """
    p = root_xml.find(".//Playlist")
    if p is None:
        return (False, "")
    
    # Skip playlists for excluded platforms
    name = st(p.findtext("Name"))
    if is_platform_excluded(name):
        return (True, f"excluded platform: {name}")
    
    # Skip specific unwanted playlists by name or category (check ALL playlists, not just autogenerated)
    name_lower = name.lower()
    skip_names = {
        "vertically oriented games",
        "chd required",
        "switch all games release date",
        "wii u eshop",
        "wii u retail",
        "savvy",
        "continue playing",
        "the best psp",
        "favorites collection"
    }
    if name_lower in skip_names:
        return (True, f"excluded playlist: {name}")
    
    # Skip all store playlists
    store_keywords = ["steam", "gog", "epic games", "origin", "pc platform"]
    if any(keyword in name_lower for keyword in store_keywords):
        return (True, f"excluded store playlist: {name}")
    
    # Skip all publisher playlists
    publisher_keywords = ["rockstar", "ubisoft"]
    if any(keyword in name_lower for keyword in publisher_keywords):
        return (True, f"excluded publisher playlist: {name}")
    
    # Check if IsAutogenerated or AutoPopulate
    is_autogen = str_to_bool(st(p.findtext("IsAutogenerated")))
    is_autopop = str_to_bool(st(p.findtext("AutoPopulate")))
    
    if not (is_autogen or is_autopop):
        return (False, "")
    
    filters = parse_playlist_filters(root_xml)
    
    # Skip if IsAutogenerated and uses Genre, PlayMode, Publisher, Region, or Source fields
    if is_autogen:
        skip_fields = {"genre", "playmode", "publisher", "region", "source"}
        for f in filters:
            field = f.get("field", "").lower()
            if field in skip_fields:
                return (True, f"autogenerated {field} playlist")
        
        # Skip "All Games" playlists (only Platform filter)
        if len(filters) == 1 and filters[0].get("field", "").lower() == "platform":
            return (True, "autogenerated 'All Games' playlist")
        
        # Skip "Favorites" playlists (Platform + Favorite=IsTrue)
        if len(filters) == 2:
            fields_ops = [(f.get("field", "").lower(), f.get("op", "").lower()) for f in filters]
            has_platform = any(field == "platform" for field, _ in fields_ops)
            has_fav_true = any(field == "favorite" and op == "istrue" for field, op in fields_ops)
            if has_platform and has_fav_true:
                return (True, "autogenerated 'Favorites' playlist")
    
    # Skip if AutoPopulate and uses Favorite=IsFalse (i.e., "The Rest" playlists)
    if is_autopop:
        for f in filters:
            field = f.get("field", "").lower()
            op = f.get("op", "").lower()
            if field == "favorite" and op == "isfalse":
                return (True, "autopopulated 'The Rest' playlist")
    
    return (False, "")

def categorize_playlist(root_xml, plist_name: str) -> str:
    """
    Determine the category/prefix for a playlist that will be exported.
    Returns: category prefix (e.g., "BEST", "FRANCHISE", "CURATED", etc.)
    """
    p = root_xml.find(".//Playlist")
    if p is None:
        return "OTHER"
    
    filters = parse_playlist_filters(root_xml)
    name_lower = plist_name.lower()
    
    # Check for "The Best" playlists (CUSTOM_The Best field OR "the best" in name)
    for f in filters:
        field = f.get("field", "").lower()
        if field == "custom_the best":
            return "BEST"
    if "the best" in name_lower:
        return "BEST"
    
    # Check for classic console collections (Mini, Classic in name)
    if " mini" in name_lower or " classic" in name_lower:
        return "CLASSIC"
    
    # Check for store/platform collections
    store_keywords = ["steam", "gog", "epic", "origin", "pc platforms"]
    if any(keyword in name_lower for keyword in store_keywords):
        return "STORE"
    
    # Check for special technical collections
    if "vertically oriented" in name_lower or "chd required" in name_lower:
        return "TECHNICAL"
    
    # Check for cross-platform curated (Favorites Collection, GOTY, Backlog, etc.)
    curated_keywords = ["favorites collection", "goty", "backlog", "all time favorites", 
                        "play it again", "on deck", "retro remakes"]
    if any(keyword in name_lower for keyword in curated_keywords):
        return "CURATED"
    
    # Check if it has Title filter (likely a franchise) OR is a known franchise
    franchise_overrides = ["mana"]
    if any(franchise in name_lower for franchise in franchise_overrides):
        return "FRANCHISE"
    
    for f in filters:
        field = f.get("field", "").lower()
        if field == "title":
            return "FRANCHISE"
    
    # Check for other custom fields (custom playlists)
    for f in filters:
        field = f.get("field", "").lower()
        if field.startswith("custom_"):
            return "CURATED"
    
    # Check for publisher collections
    publisher_keywords = ["rockstar", "ubisoft"]
    if any(keyword in name_lower for keyword in publisher_keywords):
        return "PUBLISHER"
    
    # Default to OTHER for anything else
    return "OTHER"

def get_game_field_value(game: dict, field_key: str) -> str:
    """Resolve a LaunchBox FieldKey to a value in our indexed game dict."""
    if not field_key:
        return ""
    if field_key.upper().startswith("CUSTOM_"):
        suffix = field_key[7:]
        custom = game.get("Custom") or {}
        return st(custom.get(suffix, ""))
    mapping = {
        "Platform": "Platform",
        "Title": "Title",
        "FilePath": "FilePath",
        "Developer": "Developer",
        "Publisher": "Publisher",
        "Region": "Region",
        "ReleaseDate": "ReleaseDate",
        "Genre": "Genre",
        "Series": "Series",
        "PlayMode": "PlayMode",
        "Favorite": "Favorite",
        "Installed": "Installed",
        "Status": "Status",
        "LastPlayed": "LastPlayed",
        "PlayCount": "PlayCount",
        "ID": "ID",
        "GameId": "ID",
    }
    key = mapping.get(field_key, field_key)
    return st(game.get(key, ""))

def str_to_bool(s: str) -> bool:
    return st(s).lower() in ("true","1","yes","y","on")

def matches_filter(game: dict, filt: dict) -> bool:
    """Evaluate a single filter against a game."""
    from datetime import datetime, timezone
    field = filt.get("field", "")
    op = st(filt.get("op", "")).lower()
    value = filt.get("value", "")
    gv = get_game_field_value(game, field)

    if op == "equalto":
        return st(gv).lower() == st(value).lower()
    if op == "notequalto":
        return st(gv).lower() != st(value).lower()
    if op == "contains":
        return st(value).lower() in st(gv).lower()
    if op == "startswith":
        return st(gv).lower().startswith(st(value).lower())
    if op == "endswith":
        return st(gv).lower().endswith(st(value).lower())
    if op == "istrue":
        return str_to_bool(gv)
    if op == "isfalse":
        return not str_to_bool(gv)
    if op == "isnotempty":
        return st(gv) != ""
    if op == "isempty":
        return st(gv) == ""
    if op == "recentdays":
        try:
            n = int(st(value) or "0")
        except ValueError:
            return False
        if not gv:
            return False
        try:
            lp = datetime.fromisoformat(gv)
            now = datetime.now(lp.tzinfo) if lp.tzinfo else datetime.now(timezone.utc)
            return (now - lp).days <= n
        except Exception:
            return False
    # default fallback = exact equals if value provided, else non-empty check
    return st(value).lower() == st(gv).lower() if value else (st(gv) != "")

def materialize_by_filters(filters: list[dict], all_games: list[dict]) -> list[dict]:
    rows = []
    if not filters:
        return rows
    
    # Group filters by field - filters on the same field are OR'd, different fields are AND'd
    from collections import defaultdict
    filters_by_field = defaultdict(list)
    for f in filters:
        field = f.get("field", "").lower()
        filters_by_field[field].append(f)
    
    for g in all_games:
        # All field groups must match (AND)
        ok = True
        for field, field_filters in filters_by_field.items():
            # At least one filter in this field group must match (OR)
            field_ok = False
            for f in field_filters:
                if matches_filter(g, f):
                    field_ok = True
                    break
            if not field_ok:
                ok = False
                break
        
        if ok:
            rows.append({
                "Platform": g.get("Platform",""),
                "Title": g.get("Title",""),
                "LBID": g.get("ID",""),
            })
    return rows

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Export ALL LaunchBox Playlists to CSVs (+ combined), robust.")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="LaunchBox root (default: %(default)s)")
    ap.add_argument("--outdir", default=OUTDIR_DEFAULT, help="Per-playlist CSV folder (default: %(default)s)")
    ap.add_argument("--combined", default=COMBINED_DEFAULT, help="Combined CSV path (default: %(default)s)")
    ap.add_argument("--no-index", action="store_true", help="Skip platform index (faster, fewer resolved rows)")
    ap.add_argument("--verbose", action="store_true", help="Log counts per playlist")
    args = ap.parse_args()

    root = Path(args.root)
    plist_dir = root / "Data" / "Playlists"
    plat_dir  = root / "Data" / "Platforms"

    if not plist_dir.exists():
        print(f"ERROR: Playlists dir not found: {plist_dir}", file=sys.stderr)
        sys.exit(2)

    index = {} if args.no_index else index_all_platforms(plat_dir)

    header = ["Playlist","Platform","Title","LBID"]

    # Clean up old exports
    combined = Path(args.combined)
    if combined.exists():
        combined.unlink()
    
    # Clean up old individual playlist CSVs
    outdir = Path(args.outdir)
    if outdir.exists():
        for old_csv in outdir.glob("*.csv"):
            old_csv.unlink()

    total = 0
    skipped = 0
    for xml in sorted(plist_dir.glob("*.xml")):
        try:
            tree = ET.parse(xml)
        except ET.ParseError:
            if args.verbose:
                print(f"SKIP (bad XML): {xml.name}")
            continue

        root_xml = tree.getroot()
        
        # Check if we should skip this playlist
        should_skip, skip_reason = should_skip_playlist(root_xml)
        if should_skip:
            skipped += 1
            if args.verbose:
                print(f"SKIP ({skip_reason}): {xml.name}")
            continue
        
        plist_name = playlist_title(root_xml, xml.stem)

        rows = []
        had_entries = False
        for e in iter_playlist_entries(root_xml):
            had_entries = True
            rows.append(row_from_elem(e, index))

        # If no explicit entries, try to materialize via PlaylistFilter rules
        if not had_entries:
            filters = parse_playlist_filters(root_xml)
            if filters and index:
                mat = materialize_by_filters(filters, list(index.values()))
                rows.extend(mat)
                if args.verbose:
                    print(f"{xml.name}: {len(mat)} rows via rules")
            else:
                if args.verbose:
                    reason = "no index" if (filters and not index) else "no entries, no rules"
                    print(f"{xml.name}: 0 rows ({reason})")

        # Categorize playlist and create prefixed filename
        category = categorize_playlist(root_xml, plist_name)
        out_path = Path(args.outdir) / f"{category}_{xml.stem}.csv"
        
        # Tag Playlist name on each row
        for r in rows:
            r["Playlist"] = plist_name
        write_csv(out_path, rows, header)
        append_csv(combined, rows, header)

        total += len(rows)
        if args.verbose:
            print(f"{xml.name}: {len(rows)} rows → {out_path}")

    print(f"Wrote {combined} (total rows: {total}, skipped {skipped} playlists)")

if __name__ == "__main__":
    main()
