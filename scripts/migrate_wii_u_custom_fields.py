#!/usr/bin/env python3
"""
Migrate ALL custom fields from old Wii U XML to new Wii U XML.
Matches games by title and migrates all custom field data.
"""
import xml.etree.ElementTree as ET
from pathlib import Path
import unicodedata
import shutil
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OLD_XML = PROJECT_ROOT / "Data Old" / "Platforms" / "Nintendo Wii U.xml"
NEW_XML = PROJECT_ROOT / "Data New" / "Platforms" / "Nintendo Wii U.xml"

def normalize_unicode(s):
    """Normalize Unicode to NFC (composed form)"""
    return unicodedata.normalize('NFC', s) if s else ""

def normalize_title(title):
    """Normalize title for matching"""
    title = normalize_unicode(title)
    title = title.lower().strip()
    return title

def main():
    if not OLD_XML.exists():
        print(f"Error: Old XML not found at {OLD_XML}")
        return
    
    if not NEW_XML.exists():
        print(f"Error: New XML not found at {NEW_XML}")
        return
    
    # Backup new XML first
    backup_path = NEW_XML.parent / f"{NEW_XML.stem}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xml"
    shutil.copy2(NEW_XML, backup_path)
    print(f"Created backup: {backup_path}")
    print()
    
    # Load old XML and build GameID -> Title mapping
    print("Loading old Wii U XML...")
    old_tree = ET.parse(OLD_XML)
    old_root = old_tree.getroot()
    
    # Build GameID -> Title map from old XML
    old_game_id_to_title = {}
    for game in old_root.findall('.//Game'):
        game_id = game.findtext('ID', '').strip()
        title = game.findtext('Title', '').strip()
        if game_id and title:
            old_game_id_to_title[game_id] = title
    
    # Build Title -> GameID map from old XML (for matching)
    old_title_to_game_id = {}
    for game_id, title in old_game_id_to_title.items():
        norm_title = normalize_title(title)
        old_title_to_game_id[norm_title] = game_id
    
    # Extract all custom fields from old XML (root level, referenced by GameID)
    old_custom_fields = {}  # game_id -> list of (name, value) tuples
    for custom_field in old_root.findall('CustomField'):
        game_id = custom_field.findtext('GameID', '').strip()
        name = custom_field.findtext('Name', '').strip()
        value = custom_field.findtext('Value', '').strip()
        
        if game_id and name:
            if game_id not in old_custom_fields:
                old_custom_fields[game_id] = []
            old_custom_fields[game_id].append((name, value))
    
    print(f"Found {len(old_custom_fields)} games with custom fields in old XML")
    print()
    
    # Load new XML
    print("Loading new Wii U XML...")
    new_tree = ET.parse(NEW_XML)
    new_root = new_tree.getroot()
    
    # Build Title -> GameID map from new XML
    new_title_to_game_id = {}
    for game in new_root.findall('.//Game'):
        game_id = game.findtext('ID', '').strip()
        title = game.findtext('Title', '').strip()
        if game_id and title:
            norm_title = normalize_title(title)
            new_title_to_game_id[norm_title] = game_id
    
    # Match old games to new games by title and migrate custom fields
    custom_fields_added = 0
    games_updated = 0
    field_counts = {}
    
    for norm_title, old_game_id in old_title_to_game_id.items():
        if norm_title in new_title_to_game_id:
            new_game_id = new_title_to_game_id[norm_title]
            
            # Get custom fields for this old game
            if old_game_id in old_custom_fields:
                custom_fields = old_custom_fields[old_game_id]
                
                # Add custom fields to new XML root
                for field_name, field_value in custom_fields:
                    # Create new CustomField element at root level
                    custom_field_elem = ET.SubElement(new_root, 'CustomField')
                    
                    game_id_elem = ET.SubElement(custom_field_elem, 'GameID')
                    game_id_elem.text = new_game_id
                    
                    name_elem = ET.SubElement(custom_field_elem, 'Name')
                    name_elem.text = field_name
                    
                    value_elem = ET.SubElement(custom_field_elem, 'Value')
                    value_elem.text = field_value
                    
                    custom_fields_added += 1
                    field_counts[field_name] = field_counts.get(field_name, 0) + 1
                
                games_updated += 1
                title = old_game_id_to_title[old_game_id]
                print(f"Migrated: {title} ({len(custom_fields)} fields)")
    
    # Save updated XML
    print()
    print("Saving updated XML...")
    new_tree.write(NEW_XML, encoding='utf-8', xml_declaration=True)
    
    print()
    print("=" * 80)
    print("MIGRATION COMPLETE")
    print("=" * 80)
    print(f"Games updated: {games_updated}")
    print(f"Custom fields added: {custom_fields_added}")
    print()
    print("Custom fields by type:")
    for field_name, count in sorted(field_counts.items(), key=lambda x: -x[1]):
        print(f"  {field_name:<30} {count:>5} games")
    print()
    print(f"Backup saved to: {backup_path}")
    print(f"Updated XML: {NEW_XML}")

if __name__ == "__main__":
    main()

