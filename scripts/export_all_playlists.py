#!/usr/bin/env python3
import csv, os, sys
from pathlib import Path
import xml.etree.ElementTree as ET

# Project root for config loading
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# These will be loaded from config.yaml
CONFIG = {}
DEFAULT_ROOT = r"./"
OUTDIR_DEFAULT = "LB_Exports/playlists"
COMBINED_DEFAULT = "LB_Exports/all_playlists.csv"

# Load configuration
def load_config():
    """Load configuration from config.yaml"""
    global CONFIG, DEFAULT_ROOT, OUTDIR_DEFAULT, COMBINED_DEFAULT
    try:
        import yaml
        config_path = PROJECT_ROOT / "config.yaml"
        if config_path.exists():
            with open(config_path) as f:
                CONFIG = yaml.safe_load(f)
                
                # Load paths from config
                paths = CONFIG.get('paths', {})
                launchbox_data = paths.get('launchbox_data', 'Data/')
                output_directory = paths.get('output_directory', 'LB_Exports/')
                
                # Set DEFAULT_ROOT based on launchbox_data
                if not Path(launchbox_data).is_absolute():
                    DEFAULT_ROOT = str(PROJECT_ROOT / launchbox_data)
                else:
                    DEFAULT_ROOT = launchbox_data
                
                # Set output paths
                if not Path(output_directory).is_absolute():
                    output_base = PROJECT_ROOT / output_directory
                else:
                    output_base = Path(output_directory)
                
                OUTDIR_DEFAULT = str(output_base / "playlists")
                COMBINED_DEFAULT = str(output_base / "all_playlists.csv")
                
                return True
    except Exception as e:
        print(f"Warning: Could not load config.yaml: {e}")
    return False

# Config will be loaded lazily in main() to avoid issues when config.yaml doesn't exist yet

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
    # Load config at runtime (not at import time) to get fresh values
    load_config()
    
    import argparse
    ap = argparse.ArgumentParser(description="Export all LaunchBox Playlists to CSV files")
    ap.add_argument("--root", default=DEFAULT_ROOT, help="LaunchBox root (default: %(default)s)")
    ap.add_argument("--outdir", default=OUTDIR_DEFAULT, help="Per-playlist CSV folder (default: %(default)s)")
    ap.add_argument("--combined", default=COMBINED_DEFAULT, help="Combined CSV path (default: %(default)s)")
    ap.add_argument("--no-index", action="store_true", help="Skip platform index (faster, fewer resolved rows)")
    ap.add_argument("--verbose", action="store_true", help="Show detailed per-playlist information")
    args = ap.parse_args()

    root = Path(args.root)
    plist_dir = root / "Playlists"
    plat_dir  = root / "Platforms"

    if not plist_dir.exists():
        print(f"ERROR: Playlists dir not found: {plist_dir}", file=sys.stderr)
        sys.exit(2)

    index = {} if args.no_index else index_all_platforms(plat_dir)

    header = ["Playlist","Platform","Title","LBID"]

    # Count total playlists
    all_playlist_xmls = list(plist_dir.glob("*.xml"))
    print(f"\nFound {len(all_playlist_xmls)} playlist(s)")
    
    # Clean up old exports
    combined = Path(args.combined)
    if combined.exists():
        combined.unlink()
    
    # Clean up old individual playlist CSVs
    outdir = Path(args.outdir)
    if outdir.exists():
        for old_csv in outdir.glob("*.csv"):
            old_csv.unlink()

    print("\nProcessing playlists...")
    total_rows = 0
    playlists_exported = 0
    playlists_failed = 0
    
    for xml in sorted(plist_dir.glob("*.xml")):
        try:
            tree = ET.parse(xml)
        except ET.ParseError as e:
            print(f"  ✗ ERROR: Failed to parse {xml.name}: {e}")
            playlists_failed += 1
            continue

        root_xml = tree.getroot()
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
                    print(f"  {plist_name}: {len(mat)} games via filters")
            else:
                if args.verbose:
                    reason = "no index" if (filters and not index) else "no entries, no rules"
                    print(f"  {plist_name}: 0 games ({reason})")

        # Use playlist filename as-is (no categorization)
        out_path = Path(args.outdir) / f"{xml.stem}.csv"
        
        # Tag Playlist name on each row
        for r in rows:
            r["Playlist"] = plist_name
        write_csv(out_path, rows, header)
        append_csv(combined, rows, header)

        total_rows += len(rows)
        playlists_exported += 1
        print(f"  ✓ {plist_name}: {len(rows)} games")

    # Print summary
    print("\n" + "=" * 60)
    print("EXPORT COMPLETE")
    print("=" * 60)
    print(f"Playlists exported: {playlists_exported}")
    if playlists_failed > 0:
        print(f"Playlists failed:   {playlists_failed}")
    print(f"Total games:        {total_rows:,}")
    print(f"Combined CSV:       {args.combined}")
    print("=" * 60)

if __name__ == "__main__":
    main()
