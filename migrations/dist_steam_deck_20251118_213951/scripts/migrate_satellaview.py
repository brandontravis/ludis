#!/usr/bin/env python3
# Auto-generated migration script for Nintendo Satellaview
# 7 games, 63.65 MB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo Satellaview'
ESDE_FOLDER = 'satellaview'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'BS Zelda no Densetsu: Inishie no Sekiban: Dai-1-wa',
        'filename': 'BS Zelda - Ancient Stone Tablets 2-1.pcm',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/BS Zelda no Densetsu - Inishie no Sekiban (English Translated and Dubbed With MSU1 Patch, Rev 09-21-20)/Week 2/BS Zelda - Ancient Stone Tablets 2-1.pcm',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/BS Zelda - Ancient Stone Tablets 2-1.pcm',
        'size': 63597740,
    },
    {
        'title': 'Kirby no Omochabako: Arrange Ball',
        'filename': 'Kirby no Omochabako - Arrange Ball (JP).bs',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/Kirby no Omochabako - Arrange Ball (JP).bs',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/Kirby no Omochabako - Arrange Ball (JP).bs',
        'size': 524288,
    },
    {
        'title': 'Kirby no Omochabako: Ball Rally',
        'filename': 'Kirby no Omochabako - Ball Rally (JP).bs',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/Kirby no Omochabako - Ball Rally (JP).bs',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/Kirby no Omochabako - Ball Rally (JP).bs',
        'size': 524288,
    },
    {
        'title': 'Kirby no Omochabako: Cannon Ball',
        'filename': 'Kirby no Omochabako - Cannon Ball (JP).bs',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/Kirby no Omochabako - Cannon Ball (JP).bs',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/Kirby no Omochabako - Cannon Ball (JP).bs',
        'size': 524288,
    },
    {
        'title': 'Kirby no Omochabako: Guruguru Ball',
        'filename': 'Kirby no Omochabako - Guruguru Ball (JP).bs',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/Kirby no Omochabako - Guruguru Ball (JP).bs',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/Kirby no Omochabako - Guruguru Ball (JP).bs',
        'size': 524288,
    },
    {
        'title': 'Kirby no Omochabako: Pachinko',
        'filename': 'Kirby no Omochabako - Pachinko (JP).bs',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/Kirby no Omochabako - Pachinko (JP).bs',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/Kirby no Omochabako - Pachinko (JP).bs',
        'size': 524288,
    },
    {
        'title': 'Kirby no Omochabako: Pinball',
        'filename': 'Kirby no Omochabako - Pinball (JP).bs',
        'source_relative': 'Consoles/Nintendo Satellaview [1995]/Kirby no Omochabako - Pinball (JP).bs',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/satellaview/Kirby no Omochabako - Pinball (JP).bs',
        'size': 524288,
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