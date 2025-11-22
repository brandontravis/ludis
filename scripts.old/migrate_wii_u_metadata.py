#!/usr/bin/env python3
"""
Migrate Favorites and CUSTOM_The Best from old Wii U XML to new Wii U XML.
Matches games by title and updates the new XML with the old metadata.
"""
import xml.etree.ElementTree as ET
from pathlib import Path
import unicodedata
import shutil
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OLD_XML = PROJECT_ROOT / "Data" / "Platforms" / "Nintendo Wii U.xml"
NEW_XML = PROJECT_ROOT / "Data New" / "Platforms" / "Nintendo Wii U.xml"

def normalize_unicode(s):
    """Normalize Unicode to NFC (composed form)"""
    return unicodedata.normalize('NFC', s) if s else ""

def normalize_title(title):
    """Normalize title for matching"""
    title = normalize_unicode(title)
    # Remove common variations
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
    
    # Load old XML and build metadata index
    print("Loading old Wii U XML...")
    old_tree = ET.parse(OLD_XML)
    old_root = old_tree.getroot()
    
    old_metadata = {}
    for game in old_root.findall('.//Game'):
        title = game.findtext('Title', '').strip()
        favorite = game.findtext('Favorite', '').strip()
        
        # Find CUSTOM_The Best
        the_best = None
        for custom_field in game.findall('.//CustomField'):
            name = custom_field.findtext('Name', '').strip()
            if name == "The Best":
                the_best = custom_field.findtext('Value', '').strip()
                break
        
        if favorite or the_best:
            norm_title = normalize_title(title)
            old_metadata[norm_title] = {
                'title': title,
                'favorite': favorite,
                'the_best': the_best
            }
    
    print(f"Found {len(old_metadata)} games with Favorites or The Best in old XML")
    print()
    
    # Load new XML and update
    print("Loading new Wii U XML...")
    new_tree = ET.parse(NEW_XML)
    new_root = new_tree.getroot()
    
    updated_count = 0
    favorites_added = 0
    the_best_added = 0
    
    for game in new_root.findall('.//Game'):
        title = game.findtext('Title', '').strip()
        norm_title = normalize_title(title)
        
        if norm_title in old_metadata:
            old_data = old_metadata[norm_title]
            
            # Update Favorite
            if old_data['favorite']:
                favorite_elem = game.find('Favorite')
                if favorite_elem is None:
                    favorite_elem = ET.SubElement(game, 'Favorite')
                favorite_elem.text = old_data['favorite']
                favorites_added += 1
            
            # Update CUSTOM_The Best
            if old_data['the_best']:
                # Find or create CustomValues section
                custom_values = game.find('CustomValues')
                if custom_values is None:
                    custom_values = ET.SubElement(game, 'CustomValues')
                
                # Check if The Best already exists
                the_best_exists = False
                for custom_field in custom_values.findall('CustomField'):
                    name = custom_field.findtext('Name', '').strip()
                    if name == "The Best":
                        # Update existing
                        value_elem = custom_field.find('Value')
                        if value_elem is None:
                            value_elem = ET.SubElement(custom_field, 'Value')
                        value_elem.text = old_data['the_best']
                        the_best_exists = True
                        break
                
                if not the_best_exists:
                    # Create new CustomField
                    custom_field = ET.SubElement(custom_values, 'CustomField')
                    name_elem = ET.SubElement(custom_field, 'Name')
                    name_elem.text = "The Best"
                    value_elem = ET.SubElement(custom_field, 'Value')
                    value_elem.text = old_data['the_best']
                
                the_best_added += 1
            
            updated_count += 1
            print(f"Updated: {title}")
    
    # Save updated XML
    print()
    print("Saving updated XML...")
    new_tree.write(NEW_XML, encoding='utf-8', xml_declaration=True)
    
    print()
    print("=" * 80)
    print("MIGRATION COMPLETE")
    print("=" * 80)
    print(f"Games updated: {updated_count}")
    print(f"Favorites migrated: {favorites_added}")
    print(f"The Best migrated: {the_best_added}")
    print()
    print(f"Backup saved to: {backup_path}")
    print(f"Updated XML: {NEW_XML}")

if __name__ == "__main__":
    main()

