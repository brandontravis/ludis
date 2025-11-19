#!/usr/bin/env python3
# Auto-generated migration script for Sony Playstation Vita
# 2 games, 0.00 B
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sony Playstation Vita'
ESDE_FOLDER = 'psvita'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'God of War Collection',
        'filename': 'PCSA00126.txt',
        'source_relative': 'Handhelds/Sony PS Vita [2011]/_id imports/PCSA00126.txt',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psvita/PCSA00126.txt',
        'size': 0,
    },
    {
        'title': 'Final Fantasy X/X-2: HD Remaster',
        'filename': 'PCSE00283.txt',
        'source_relative': 'Handhelds/Sony PS Vita [2011]/_id imports/PCSE00283.txt',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psvita/PCSE00283.txt',
        'size': 0,
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