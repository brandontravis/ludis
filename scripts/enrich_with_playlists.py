#!/usr/bin/env python3
"""
Enrich master_inventory.csv with playlist membership data.

Adds 7 columns:
- IsPlatformBest (Boolean)
- IsInFranchise (Boolean)
- Franchises (Text - semicolon-separated)
- IsInCurated (Boolean)
- CuratedPlaylists (Text - semicolon-separated)
- IsInClassicCollection (Boolean)
- PlaylistCount (Integer)
"""

import csv
from pathlib import Path
from collections import defaultdict

# Project root is parent of scripts/ directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
MASTER_INVENTORY = PROJECT_ROOT / "LB_Exports" / "master_inventory.csv"
ALL_PLAYLISTS = PROJECT_ROOT / "LB_Exports" / "all_playlists.csv"
OUTPUT_CSV = PROJECT_ROOT / "LB_Exports" / "master_inventory.csv"

def st(x):
    """Safe text extraction"""
    return (x or "").strip()

def categorize_playlist(playlist_name: str) -> str:
    """Determine playlist category from name prefix or content"""
    name = st(playlist_name)
    if name.startswith("BEST_"):
        return "BEST"
    elif name.startswith("FRANCHISE_"):
        return "FRANCHISE"
    elif name.startswith("CURATED_"):
        return "CURATED"
    elif name.startswith("CLASSIC_"):
        return "CLASSIC"
    else:
        return "OTHER"

def read_all_playlists(csv_path: Path) -> dict:
    """
    Read all_playlists.csv and build a map of LBID -> playlist memberships.
    
    Returns:
        dict: {
            LBID: {
                'best': set(),
                'franchise': set(),
                'curated': set(),
                'classic': set(),
                'count': int
            }
        }
    """
    playlist_index = defaultdict(lambda: {
        'best': set(),
        'franchise': set(),
        'curated': set(),
        'classic': set(),
        'count': 0
    })
    
    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found!")
        return {}
    
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            lbid = st(row.get('LBID', ''))
            playlist = st(row.get('Playlist', ''))
            
            if not lbid or not playlist:
                continue
            
            # Determine category from the actual playlist CSV filename pattern
            # We need to infer the category from the playlist name itself
            category = None
            
            # Check for "The Best" playlists
            if "the best" in playlist.lower():
                category = "BEST"
            # Check for classic collections
            elif any(keyword in playlist.lower() for keyword in [" mini", " classic"]):
                category = "CLASSIC"
            # Check for curated playlists
            elif any(keyword in playlist.lower() for keyword in [
                "goty", "backlog", "all time favorites", 
                "play it again", "on deck", "retro remakes"
            ]):
                category = "CURATED"
            # Everything else is likely a franchise
            else:
                category = "FRANCHISE"
            
            # Add to appropriate set
            if category == "BEST":
                playlist_index[lbid]['best'].add(playlist)
            elif category == "FRANCHISE":
                playlist_index[lbid]['franchise'].add(playlist)
            elif category == "CURATED":
                playlist_index[lbid]['curated'].add(playlist)
            elif category == "CLASSIC":
                playlist_index[lbid]['classic'].add(playlist)
            
            playlist_index[lbid]['count'] += 1
    
    return playlist_index

def enrich_inventory(inventory_path: Path, playlist_index: dict, output_path: Path):
    """
    Read master_inventory.csv, add playlist columns, write back.
    """
    if not inventory_path.exists():
        print(f"ERROR: {inventory_path} not found!")
        print("Please run build_master_inventory.py first.")
        return
    
    rows = []
    original_headers = []
    
    # Read existing inventory
    with open(inventory_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        original_headers = reader.fieldnames
        
        for row in reader:
            lbid = st(row.get('LBID', ''))
            
            # Get playlist data for this game
            playlist_data = playlist_index.get(lbid, {
                'best': set(),
                'franchise': set(),
                'curated': set(),
                'classic': set(),
                'count': 0
            })
            
            # Add new columns
            row['IsPlatformBest'] = 'True' if playlist_data['best'] else 'False'
            row['IsInFranchise'] = 'True' if playlist_data['franchise'] else 'False'
            row['Franchises'] = ';'.join(sorted(playlist_data['franchise']))
            row['IsInCurated'] = 'True' if playlist_data['curated'] else 'False'
            row['CuratedPlaylists'] = ';'.join(sorted(playlist_data['curated']))
            row['IsInClassicCollection'] = 'True' if playlist_data['classic'] else 'False'
            row['PlaylistCount'] = str(playlist_data['count'])
            
            rows.append(row)
    
    # Define new header order
    # IsPlatformBest already exists in original headers, so we'll update it
    # Add the other new columns
    new_columns_to_add = [
        'IsInFranchise',
        'Franchises',
        'IsInCurated',
        'CuratedPlaylists',
        'IsInClassicCollection',
        'PlaylistCount'
    ]
    
    # Use original headers and add only the new ones
    new_headers = list(original_headers) + new_columns_to_add
    
    # Write enriched inventory
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=new_headers, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"✓ Enriched {len(rows)} rows with playlist data")
    
    # Print summary statistics
    best_count = sum(1 for r in rows if r.get('IsPlatformBest') == 'True')
    franchise_count = sum(1 for r in rows if r.get('IsInFranchise') == 'True')
    curated_count = sum(1 for r in rows if r.get('IsInCurated') == 'True')
    classic_count = sum(1 for r in rows if r.get('IsInClassicCollection') == 'True')
    
    print(f"\nPlaylist Membership Summary:")
    print(f"  Platform Best:       {best_count:5} games")
    print(f"  Franchise:           {franchise_count:5} games")
    print(f"  Curated:             {curated_count:5} games")
    print(f"  Classic Collection:  {classic_count:5} games")
    print(f"\nWrote: {output_path}")

def main():
    print("=" * 60)
    print("Enriching Master Inventory with Playlist Data")
    print("=" * 60)
    
    # Read playlist data
    print(f"\n1. Reading playlist data from {ALL_PLAYLISTS.name}...")
    playlist_index = read_all_playlists(ALL_PLAYLISTS)
    print(f"   ✓ Indexed {len(playlist_index)} unique games across playlists")
    
    # Enrich inventory
    print(f"\n2. Enriching {MASTER_INVENTORY.name}...")
    enrich_inventory(MASTER_INVENTORY, playlist_index, OUTPUT_CSV)
    
    print("\n" + "=" * 60)
    print("✓ Enrichment Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()

