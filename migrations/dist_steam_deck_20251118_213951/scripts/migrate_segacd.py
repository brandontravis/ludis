#!/usr/bin/env python3
# Auto-generated migration script for Sega CD
# 7 games, 1.80 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sega CD'
ESDE_FOLDER = 'segacd'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'The Adventures of Batman & Robin',
        'filename': 'Adventures of Batman & Robin, The.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Adventures of Batman & Robin, The.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Adventures of Batman & Robin, The.chd',
        'size': 202469761,
    },
    {
        'title': 'Earthworm Jim: Special Edition',
        'filename': 'Earthworm Jim - Special Edition.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Earthworm Jim - Special Edition.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Earthworm Jim - Special Edition.chd',
        'size': 209030764,
    },
    {
        'title': 'Ecco: The Tides of Time',
        'filename': 'Ecco - The Tides of Time.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Ecco - The Tides of Time.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Ecco - The Tides of Time.chd',
        'size': 390386372,
    },
    {
        'title': 'Ecco the Dolphin',
        'filename': 'Ecco the Dolphin.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Ecco the Dolphin.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Ecco the Dolphin.chd',
        'size': 295372296,
    },
    {
        'title': 'Final Fight CD',
        'filename': 'Final Fight CD.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Final Fight CD.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Final Fight CD.chd',
        'size': 257500908,
    },
    {
        'title': 'Shining Force CD',
        'filename': 'Shining Force CD.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Shining Force CD.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Shining Force CD.chd',
        'size': 243747468,
    },
    {
        'title': 'Sonic The Hedgehog CD',
        'filename': 'Sonic the Hedgehog CD.chd',
        'source_relative': 'Consoles/Sega CD (Mega CD) [1991]/Sonic the Hedgehog CD.chd',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/segacd/Sonic the Hedgehog CD.chd',
        'size': 333757919,
    },
]

def migrate(nas_base_path, dry_run=False, overwrite=False):
    """Execute migration for this platform."""
    print(f'\nMigrating {PLATFORM_NAME}...')
    print(f'  {len(GAMES)} games')
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    nas_base = Path(nas_base_path)
    
    for game in GAMES:
        source = nas_base / game['source_relative']
        dest = Path(game['dest'])
        
        # Check if source exists
        if not source.exists():
            print(f"  ✗ Missing: {game['title']}")
            error_count += 1
            continue
        
        # Check if dest exists
        if dest.exists() and not overwrite:
            skip_count += 1
            continue
        
        if dry_run:
            print(f"  [DRY RUN] Would {OPERATION}: {game['title']}")
            success_count += 1
        else:
            try:
                # Create destination directory
                dest.parent.mkdir(parents=True, exist_ok=True)
                
                if OPERATION == 'copy':
                    shutil.copy2(source, dest)
                else:  # symlink
                    if dest.exists():
                        dest.unlink()
                    dest.symlink_to(source)
                
                success_count += 1
            except Exception as e:
                print(f"  ✗ Error with {game['title']}: {e}")
                error_count += 1
    
    return {
        'platform': PLATFORM_NAME,
        'success': success_count,
        'skipped': skip_count,
        'errors': error_count,
        'total': len(GAMES)
    }

if __name__ == '__main__':
    # Can be run standalone
    import sys
    
    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h']:
        print('Usage: {} <nas_base_path> [--dry-run] [--overwrite]'.format(sys.argv[0]))
        print('  nas_base_path: Where your NAS is mounted (e.g., /mnt/nas, /media/nas)')
        sys.exit(1)
    
    nas_base_path = sys.argv[1]
    dry_run = '--dry-run' in sys.argv
    overwrite = '--overwrite' in sys.argv
    result = migrate(nas_base_path, dry_run=dry_run, overwrite=overwrite)
    print(f"\n✓ {result['platform']}: {result['success']}/{result['total']} games")