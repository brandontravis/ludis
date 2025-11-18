#!/usr/bin/env python3
"""
Sanity check unmatched entries against LaunchBox XML files.
This script directly checks if unmatched games exist in the platform XMLs.
"""
import csv
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
import unicodedata

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MASTER_CSV = PROJECT_ROOT / "LB_Exports" / "master_inventory.csv"
PLATFORMS_DIR = PROJECT_ROOT / "Data" / "Platforms"

def normalize_unicode(s):
    """Normalize Unicode to NFC (composed form)"""
    return unicodedata.normalize('NFC', s) if s else ""

def normalize_for_comparison(s):
    """Normalize string for fuzzy comparison"""
    if not s:
        return ""
    # Remove special characters, lowercase, remove spaces
    import re
    s = normalize_unicode(s)
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s

def strip_region_and_extras(title):
    """Strip region tags, version info, and other extras from title"""
    import re
    # Remove region tags
    title = re.sub(r'\s*\([^)]*(?:USA|Europe|Japan|World|Brazil|Germany|France|UK|Spain|Italy|Canada|Australia|Asia|Korea)[^)]*\)', '', title, flags=re.IGNORECASE)
    # Remove version tags
    title = re.sub(r'\s*\(v\d+\)', '', title, flags=re.IGNORECASE)
    # Remove Rev tags
    title = re.sub(r'\s*\(Rev\s+\d+\)', '', title, flags=re.IGNORECASE)
    # Remove language tags
    title = re.sub(r'\s*\(En(?:,\w+)*\)', '', title, flags=re.IGNORECASE)
    return title.strip()

def load_xml_titles(xml_path):
    """Load all game titles from a platform XML"""
    titles = []
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        for game in root.findall('.//Game'):
            title = game.findtext('Title', '').strip()
            if title:
                titles.append(normalize_unicode(title))
    except Exception as e:
        print(f"Error loading {xml_path}: {e}")
    return titles

def main():
    # Load unmatched entries from master inventory
    print("Loading unmatched entries from master_inventory.csv...")
    unmatched_by_platform = defaultdict(list)
    
    with open(MASTER_CSV, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            platform = row.get('Platform', '').strip()
            matched = row.get('Matched', '').strip()
            match_type = row.get('MatchType', '').strip()
            
            # Skip Windows and MS-DOS
            if platform in ['Windows', 'MS-DOS']:
                continue
            
            # Only check NAS-only entries (not lb_only)
            if matched == 'No' and match_type != 'lb_only':
                filename = row.get('Filename', '').strip()
                title = row.get('Title', '').strip()
                unmatched_by_platform[platform].append({
                    'filename': filename,
                    'title': title,
                })
    
    total_unmatched = sum(len(games) for games in unmatched_by_platform.values())
    print(f"Found {total_unmatched} NAS-only unmatched entries across {len(unmatched_by_platform)} platforms")
    print()
    
    # For each platform, load the XML and check for matches
    results = []
    
    for platform, games in sorted(unmatched_by_platform.items()):
        if not games:
            continue
            
        print(f"Checking {platform} ({len(games)} unmatched)...")
        
        # Find the XML file for this platform
        xml_files = list(PLATFORMS_DIR.glob("*.xml"))
        xml_file = None
        for xf in xml_files:
            if platform.lower() in xf.stem.lower() or xf.stem.lower() in platform.lower():
                xml_file = xf
                break
        
        if not xml_file or not xml_file.exists():
            print(f"  ⚠ Could not find XML file for {platform}")
            results.append({
                'platform': platform,
                'unmatched_count': len(games),
                'xml_found': False,
                'potential_matches': 0,
            })
            continue
        
        # Load all titles from XML
        xml_titles = load_xml_titles(xml_file)
        xml_titles_normalized = {normalize_for_comparison(t): t for t in xml_titles}
        
        # Check each unmatched game
        potential_matches = 0
        examples = []
        
        for game in games:
            nas_title = game['title'] or game['filename']
            nas_normalized = normalize_for_comparison(nas_title)
            
            # Try exact normalized match
            if nas_normalized in xml_titles_normalized:
                potential_matches += 1
                if len(examples) < 3:
                    examples.append({
                        'nas': nas_title,
                        'xml': xml_titles_normalized[nas_normalized],
                        'type': 'exact_normalized'
                    })
                continue
            
            # Try with region/extras stripped
            nas_stripped = strip_region_and_extras(nas_title)
            nas_stripped_norm = normalize_for_comparison(nas_stripped)
            
            if nas_stripped_norm in xml_titles_normalized:
                potential_matches += 1
                if len(examples) < 3:
                    examples.append({
                        'nas': nas_title,
                        'xml': xml_titles_normalized[nas_stripped_norm],
                        'type': 'region_stripped'
                    })
        
        results.append({
            'platform': platform,
            'unmatched_count': len(games),
            'xml_found': True,
            'potential_matches': potential_matches,
            'examples': examples,
        })
        
        if potential_matches > 0:
            print(f"  ✓ Found {potential_matches} potential matches in XML!")
            for ex in examples:
                print(f"    NAS: {ex['nas'][:60]}")
                print(f"    XML: {ex['xml'][:60]}")
                print(f"    Type: {ex['type']}")
                print()
        else:
            print(f"  ✗ No potential matches found")
    
    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"{'Platform':<40} {'Unmatched':>10} {'In XML':>10} {'%':>6}")
    print("-" * 80)
    
    total_unmatched = 0
    total_in_xml = 0
    
    for r in results:
        if r['xml_found']:
            pct = (r['potential_matches'] / r['unmatched_count'] * 100) if r['unmatched_count'] > 0 else 0
            print(f"{r['platform']:<40} {r['unmatched_count']:>10} {r['potential_matches']:>10} {pct:>5.1f}%")
            total_unmatched += r['unmatched_count']
            total_in_xml += r['potential_matches']
    
    print("-" * 80)
    pct_total = (total_in_xml / total_unmatched * 100) if total_unmatched > 0 else 0
    print(f"{'TOTAL':<40} {total_unmatched:>10} {total_in_xml:>10} {pct_total:>5.1f}%")
    print()
    print(f"This means {total_in_xml} out of {total_unmatched} unmatched games")
    print(f"actually EXIST in LaunchBox XMLs but aren't matching!")

if __name__ == "__main__":
    main()

