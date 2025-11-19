#!/usr/bin/env python3
# Ludis ROM Migration Runner for steam_deck
# Generated: 2025-11-18 21:39:51
# Operation: copy

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

# Import platform migration modules
import migrate_3do
import migrate_gx4000
import migrate_arcade
import migrate_atari2600
import migrate_atari7800
import migrate_atarijaguar
import migrate_atarilynx
import migrate_colecovision
import migrate_amigacd32
import migrate_dos
import migrate_intellivision
import migrate_xbox
import migrate_xbox360
import migrate_n3ds
import migrate_n64
import migrate_nds
import migrate_nes
import migrate_fds
import migrate_gb
import migrate_gba
import migrate_gbc
import migrate_gc
import migrate_satellaview
import migrate_switch
import migrate_wii
import migrate_wiiu
import migrate_neogeo
import migrate_neogeocd
import migrate_sega32x
import migrate_segacd
import migrate_dreamcast
import migrate_gamegear
import migrate_genesis
import migrate_mastersystem
import migrate_saturn
import migrate_psp
import migrate_psx
import migrate_ps2
import migrate_ps3
import migrate_psvita
import migrate_snes

PLATFORMS = {
    '3DO Interactive Multiplayer': {
        'module': migrate_3do,
        'games': 2,
        'size': '0.00 B',
        'esde_folder': '3do',
    },
    'Amstrad GX4000': {
        'module': migrate_gx4000,
        'games': 1,
        'size': '512.26 KB',
        'esde_folder': 'gx4000',
    },
    'Arcade': {
        'module': migrate_arcade,
        'games': 238,
        'size': '995.78 MB',
        'esde_folder': 'arcade',
    },
    'Atari 2600': {
        'module': migrate_atari2600,
        'games': 57,
        'size': '266.93 KB',
        'esde_folder': 'atari2600',
    },
    'Atari 7800': {
        'module': migrate_atari7800,
        'games': 3,
        'size': '78.40 KB',
        'esde_folder': 'atari7800',
    },
    'Atari Jaguar': {
        'module': migrate_atarijaguar,
        'games': 2,
        'size': '4.31 MB',
        'esde_folder': 'atarijaguar',
    },
    'Atari Lynx': {
        'module': migrate_atarilynx,
        'games': 2,
        'size': '346.50 KB',
        'esde_folder': 'atarilynx',
    },
    'ColecoVision': {
        'module': migrate_colecovision,
        'games': 2,
        'size': '24.06 KB',
        'esde_folder': 'colecovision',
    },
    'Commodore Amiga CD32': {
        'module': migrate_amigacd32,
        'games': 1,
        'size': '3.04 MB',
        'esde_folder': 'amigacd32',
    },
    'MS-DOS': {
        'module': migrate_dos,
        'games': 206,
        'size': '0.00 B',
        'esde_folder': 'dos',
    },
    'Mattel Intellivision': {
        'module': migrate_intellivision,
        'games': 2,
        'size': '13.49 KB',
        'esde_folder': 'intellivision',
    },
    'Microsoft Xbox': {
        'module': migrate_xbox,
        'games': 157,
        'size': '392.21 GB',
        'esde_folder': 'xbox',
    },
    'Microsoft Xbox 360': {
        'module': migrate_xbox360,
        'games': 277,
        'size': '2.05 TB',
        'esde_folder': 'xbox360',
    },
    'Nintendo 3DS': {
        'module': migrate_n3ds,
        'games': 152,
        'size': '136.50 GB',
        'esde_folder': 'n3ds',
    },
    'Nintendo 64': {
        'module': migrate_n64,
        'games': 119,
        'size': '1.54 GB',
        'esde_folder': 'n64',
    },
    'Nintendo DS': {
        'module': migrate_nds,
        'games': 110,
        'size': '6.75 GB',
        'esde_folder': 'nds',
    },
    'Nintendo Entertainment System': {
        'module': migrate_nes,
        'games': 172,
        'size': '16.64 MB',
        'esde_folder': 'nes',
    },
    'Nintendo Famicom Disk System': {
        'module': migrate_fds,
        'games': 5,
        'size': '220.60 KB',
        'esde_folder': 'fds',
    },
    'Nintendo Game Boy': {
        'module': migrate_gb,
        'games': 160,
        'size': '18.38 MB',
        'esde_folder': 'gb',
    },
    'Nintendo Game Boy Advance': {
        'module': migrate_gba,
        'games': 230,
        'size': '975.16 MB',
        'esde_folder': 'gba',
    },
    'Nintendo Game Boy Color': {
        'module': migrate_gbc,
        'games': 121,
        'size': '57.27 MB',
        'esde_folder': 'gbc',
    },
    'Nintendo GameCube': {
        'module': migrate_gc,
        'games': 180,
        'size': '237.93 GB',
        'esde_folder': 'gc',
    },
    'Nintendo Satellaview': {
        'module': migrate_satellaview,
        'games': 7,
        'size': '63.65 MB',
        'esde_folder': 'satellaview',
    },
    'Nintendo Switch': {
        'module': migrate_switch,
        'games': 209,
        'size': '1.17 TB',
        'esde_folder': 'switch',
    },
    'Nintendo Wii': {
        'module': migrate_wii,
        'games': 89,
        'size': '277.48 GB',
        'esde_folder': 'wii',
    },
    'Nintendo Wii U': {
        'module': migrate_wiiu,
        'games': 73,
        'size': '458.90 GB',
        'esde_folder': 'wiiu',
    },
    'SNK Neo Geo AES': {
        'module': migrate_neogeo,
        'games': 1,
        'size': '10.64 MB',
        'esde_folder': 'neogeo',
    },
    'SNK Neo Geo CD': {
        'module': migrate_neogeocd,
        'games': 1,
        'size': '0.00 B',
        'esde_folder': 'neogeocd',
    },
    'Sega 32X': {
        'module': migrate_sega32x,
        'games': 1,
        'size': '1.14 MB',
        'esde_folder': 'sega32x',
    },
    'Sega CD': {
        'module': migrate_segacd,
        'games': 7,
        'size': '1.80 GB',
        'esde_folder': 'segacd',
    },
    'Sega Dreamcast': {
        'module': migrate_dreamcast,
        'games': 66,
        'size': '0.00 B',
        'esde_folder': 'dreamcast',
    },
    'Sega Game Gear': {
        'module': migrate_gamegear,
        'games': 86,
        'size': '14.10 MB',
        'esde_folder': 'gamegear',
    },
    'Sega Genesis': {
        'module': migrate_genesis,
        'games': 211,
        'size': '152.74 MB',
        'esde_folder': 'genesis',
    },
    'Sega Master System': {
        'module': migrate_mastersystem,
        'games': 70,
        'size': '11.20 MB',
        'esde_folder': 'mastersystem',
    },
    'Sega Saturn': {
        'module': migrate_saturn,
        'games': 60,
        'size': '0.00 B',
        'esde_folder': 'saturn',
    },
    'Sony PSP': {
        'module': migrate_psp,
        'games': 132,
        'size': '118.22 GB',
        'esde_folder': 'psp',
    },
    'Sony Playstation': {
        'module': migrate_psx,
        'games': 301,
        'size': '89.42 GB',
        'esde_folder': 'psx',
    },
    'Sony Playstation 2': {
        'module': migrate_ps2,
        'games': 276,
        'size': '759.47 GB',
        'esde_folder': 'ps2',
    },
    'Sony Playstation 3': {
        'module': migrate_ps3,
        'games': 238,
        'size': '0.00 B',
        'esde_folder': 'ps3',
    },
    'Sony Playstation Vita': {
        'module': migrate_psvita,
        'games': 2,
        'size': '0.00 B',
        'esde_folder': 'psvita',
    },
    'Super Nintendo Entertainment System': {
        'module': migrate_snes,
        'games': 208,
        'size': '205.74 MB',
        'esde_folder': 'snes',
    },
}

def main():
    print('=' * 60)
    print('LUDIS ROM MIGRATION - STEAM_DECK')
    print('=' * 60)
    print()
    print(f'Available platforms: {len(PLATFORMS)}')
    
    # Show platform list
    print('\nPlatforms:')
    for name, info in sorted(PLATFORMS.items()):
        print(f"  - {name}: {info['games']} games, {info['size']}")
    
    # Simple menu
    print('\n' + '=' * 60)
    print('OPTIONS')
    print('=' * 60)
    print('1. Migrate all platforms')
    print('2. Select specific platforms (not yet implemented)')
    print('3. Exit')
    
    choice = input('\nSelect option [1]: ').strip() or '1'
    
    if choice == '3':
        print('\nExiting.')
        return
    
    if choice != '1':
        print('\n⚠ Option not yet implemented. Exiting.')
        return
    
    # Get migration options
    print('\n' + '=' * 60)
    print('MIGRATION OPTIONS')
    print('=' * 60)
    
    # NAS base path
    print('\nWhere is your NAS/source library mounted on this device?')
    print('Examples:')
    print('  /mnt/nas')
    print('  /media/nas/games/library')
    print('  /run/media/USERNAME/DRIVE/games/library')
    
    nas_base_path = input('\nNAS mount path: ').strip()
    
    if not nas_base_path:
        print('\n✗ NAS path is required')
        return
    
    nas_base = Path(nas_base_path)
    if not nas_base.exists():
        print(f'\n⚠ Warning: Path does not exist: {nas_base_path}')
        confirm = input('Continue anyway? (y/N): ').strip().lower()
        if confirm != 'y':
            print('\nCancelled.')
            return
    
    dry_run_input = input('\nDry run mode? (y/N): ').strip().lower()
    dry_run = dry_run_input == 'y'
    
    overwrite_input = input('Overwrite existing files? (y/N): ').strip().lower()
    overwrite = overwrite_input == 'y'
    
    if dry_run:
        print('\n⚠ DRY RUN MODE - No files will be copied')
    
    # Confirm
    confirm = input('\nProceed? (Y/n): ').strip().lower()
    if confirm == 'n':
        print('\nCancelled.')
        return
    
    # Execute migrations
    print('\n' + '=' * 60)
    print('EXECUTING MIGRATION')
    print('=' * 60)
    
    results = []
    
    for platform_name in sorted(PLATFORMS.keys()):
        platform_info = PLATFORMS[platform_name]
        module = platform_info['module']
        
        try:
            result = module.migrate(nas_base_path, dry_run=dry_run, overwrite=overwrite)
            results.append(result)
        except Exception as e:
            print(f'\n✗ Error migrating {platform_name}: {e}')
            results.append({
                'platform': platform_name,
                'success': 0,
                'skipped': 0,
                'errors': platform_info['games'],
                'total': platform_info['games']
            })
    
    # Show summary
    print('\n' + '=' * 60)
    print('MIGRATION SUMMARY')
    print('=' * 60)
    
    total_success = sum(r['success'] for r in results)
    total_skipped = sum(r['skipped'] for r in results)
    total_errors = sum(r['errors'] for r in results)
    total_games = sum(r['total'] for r in results)
    
    print(f'\nTotal games: {total_games:,}')
    print(f'  Successful: {total_success:,}')
    print(f'  Skipped: {total_skipped:,}')
    print(f'  Errors: {total_errors:,}')
    
    if dry_run:
        print('\n(This was a dry run - no files were actually copied)')
    
    print('\n✓ Migration complete!')

if __name__ == '__main__':
    main()