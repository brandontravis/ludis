#!/usr/bin/env python3
# Auto-generated migration script for Atari Lynx
# 2 games, 346.50 KB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Atari Lynx'
ESDE_FOLDER = 'atarilynx'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Batman Returns',
        'filename': 'Batman Returns (USA, Europe).zip',
        'source_relative': 'Handhelds/Atari Lynx [1989]/Batman Returns (USA, Europe).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atarilynx/Batman Returns (USA, Europe).zip',
        'size': 175492,
    },
    {
        'title': 'Double Dragon',
        'filename': 'Double Dragon (USA, Europe).zip',
        'source_relative': 'Handhelds/Atari Lynx [1989]/Double Dragon (USA, Europe).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atarilynx/Double Dragon (USA, Europe).zip',
        'size': 179326,
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