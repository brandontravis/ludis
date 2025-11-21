#!/usr/bin/env python3
"""
Enrich master_inventory.csv with playlist membership data.

Adds 2 columns:
- InAnyPlaylist (Boolean) - True if game appears in any playlist
- Playlists (Text) - Semicolon-separated list of all playlists containing this game
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

def read_all_playlists(csv_path: Path) -> dict:
    """
    Read all_playlists.csv and build a map of LBID -> list of playlists.
    
    Returns:
        dict: {LBID: [playlist1, playlist2, ...]}
    """
    playlist_index = defaultdict(list)
    
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
            
            # Simply add playlist to this game's list
            playlist_index[lbid].append(playlist)
    
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
            
            # Get list of playlists for this game
            playlists = playlist_index.get(lbid, [])
            
            # Add new columns
            row['InAnyPlaylist'] = 'True' if playlists else 'False'
            row['Playlists'] = ';'.join(sorted(playlists))
            
            rows.append(row)
    
    # Add new columns to header
    new_columns_to_add = ['InAnyPlaylist', 'Playlists']
    
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
    in_playlist_count = sum(1 for r in rows if r.get('InAnyPlaylist') == 'True')
    
    # Count unique playlists
    all_playlists = set()
    for r in rows:
        playlists_str = r.get('Playlists', '')
        if playlists_str:
            all_playlists.update(p.strip() for p in playlists_str.split(';') if p.strip())
    
    print(f"\nPlaylist Membership Summary:")
    print(f"  Games in playlists:  {in_playlist_count:5} games")
    print(f"  Total playlists:     {len(all_playlists):5} unique playlists")
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

