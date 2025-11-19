#!/usr/bin/env python3
# Auto-generated migration script for Atari 2600
# 57 games, 266.93 KB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Atari 2600'
ESDE_FOLDER = 'atari2600'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Adventure',
        'filename': 'Adventure (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Adventure (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Adventure (USA).7z',
        'size': 3131,
    },
    {
        'title': 'Adventure',
        'filename': 'Adventure (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Adventure (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Adventure (USA).7z',
        'size': 3122,
    },
    {
        'title': 'Asteroids',
        'filename': 'Asteroids (USA) (Atari Anthology).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Asteroids (USA) (Atari Anthology).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Asteroids (USA) (Atari Anthology).7z',
        'size': 4832,
    },
    {
        'title': 'Atlantis',
        'filename': 'Atlantis (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Atlantis (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Atlantis (USA).7z',
        'size': 3194,
    },
    {
        'title': 'Bachelor Party',
        'filename': 'Bachelor Party (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Bachelor Party (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Bachelor Party (USA).7z',
        'size': 2308,
    },
    {
        'title': 'Bachelorette Party',
        'filename': 'Bachelorette Party (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Bachelorette Party (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Bachelorette Party (USA).7z',
        'size': 2344,
    },
    {
        'title': 'Berzerk',
        'filename': 'Berzerk (Japan, USA) (En).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Berzerk (Japan, USA) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Berzerk (Japan, USA) (En).7z',
        'size': 2920,
    },
    {
        'title': 'BurgerTime',
        'filename': 'BurgerTime (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/BurgerTime (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/BurgerTime (USA).7z',
        'size': 6296,
    },
    {
        'title': 'Centipede',
        'filename': 'Centipede (Japan, USA) (En).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Centipede (Japan, USA) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Centipede (Japan, USA) (En).7z',
        'size': 5058,
    },
    {
        'title': 'Combat',
        'filename': 'Combat (USA, Europe) (Atari Anthology).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Combat (USA, Europe) (Atari Anthology).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Combat (USA, Europe) (Atari Anthology).7z',
        'size': 2018,
    },
    {
        'title': 'Defender',
        'filename': 'Defender (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Defender (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Defender (USA).7z',
        'size': 3501,
    },
    {
        'title': 'Demon Attack',
        'filename': 'Demon Attack (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Demon Attack (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Demon Attack (USA) (Rev 1).7z',
        'size': 3553,
    },
    {
        'title': 'Dig Dug',
        'filename': 'Dig Dug (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Dig Dug (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Dig Dug (USA).7z',
        'size': 9765,
    },
    {
        'title': 'Donkey Kong',
        'filename': 'Donkey Kong (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Donkey Kong (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Donkey Kong (USA).7z',
        'size': 2953,
    },
    {
        'title': 'Donkey Kong Junior',
        'filename': 'Donkey Kong Junior (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Donkey Kong Junior (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Donkey Kong Junior (USA).7z',
        'size': 4789,
    },
    {
        'title': 'Double Dragon',
        'filename': 'Double Dragon (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Double Dragon (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Double Dragon (USA).7z',
        'size': 9728,
    },
    {
        'title': 'Dune',
        'filename': 'Dune (USA) (Proto).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Dune (USA) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Dune (USA) (Proto).7z',
        'size': 2343,
    },
    {
        'title': 'E.T. the Extra-Terrestrial',
        'filename': 'E.T. - The Extra-Terrestrial (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/E.T. - The Extra-Terrestrial (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/E.T. - The Extra-Terrestrial (USA).7z',
        'size': 5947,
    },
    {
        'title': 'Frogger',
        'filename': 'Frogger (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Frogger (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Frogger (USA).7z',
        'size': 3368,
    },
    {
        'title': 'Frogger II: Threeedeep!',
        'filename': 'Frogger II - Threeedeep! (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Frogger II - Threeedeep! (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Frogger II - Threeedeep! (USA).7z',
        'size': 6042,
    },
    {
        'title': 'Ghostbusters',
        'filename': 'Ghostbusters (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Ghostbusters (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Ghostbusters (USA).7z',
        'size': 6098,
    },
    {
        'title': 'Ghostbusters II',
        'filename': 'Ghostbusters II (Europe).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Ghostbusters II (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Ghostbusters II (Europe).7z',
        'size': 7477,
    },
    {
        'title': 'Halo 2600',
        'filename': 'Halo 2600 (World) (Aftermarket) (Homebrew).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Halo 2600 (World) (Aftermarket) (Homebrew).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Halo 2600 (World) (Aftermarket) (Homebrew).7z',
        'size': 3354,
    },
    {
        'title': 'Harem',
        'filename': 'Harem (USA) (Proto).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Harem (USA) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Harem (USA) (Proto).7z',
        'size': 3141,
    },
    {
        'title': 'Joust',
        'filename': 'Joust (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Joust (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Joust (USA).7z',
        'size': 5902,
    },
    {
        'title': 'Jr. Pac-Man',
        'filename': 'Jr. Pac-Man (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Jr. Pac-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Jr. Pac-Man (USA).7z',
        'size': 9264,
    },
    {
        'title': 'Jungle Hunt',
        'filename': 'Jungle Hunt (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Jungle Hunt (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Jungle Hunt (USA).7z',
        'size': 6108,
    },
    {
        'title': 'Mario Bros.',
        'filename': 'Mario Bros. (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Mario Bros. (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Mario Bros. (USA).7z',
        'size': 5038,
    },
    {
        'title': "McDonald's: Golden Arches Adventure",
        'filename': "McDonald's - Golden Arches Adventure (USA) (Proto).7z",
        'source_relative': "Consoles/Atari 2600 [1977]/McDonald's - Golden Arches Adventure (USA) (Proto).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/McDonald's - Golden Arches Adventure (USA) (Proto).7z",
        'size': 3531,
    },
    {
        'title': 'Millipede',
        'filename': 'Millipede (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Millipede (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Millipede (USA).7z',
        'size': 8948,
    },
    {
        'title': 'Missile Command',
        'filename': 'Missile Command (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Missile Command (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Missile Command (USA).7z',
        'size': 3461,
    },
    {
        'title': 'Missile Control',
        'filename': 'Missile Control (Europe).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Missile Control (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Missile Control (Europe).7z',
        'size': 3074,
    },
    {
        'title': 'Ms. Pac-Man',
        'filename': 'Ms. Pac-Man (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Ms. Pac-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Ms. Pac-Man (USA).7z',
        'size': 5416,
    },
    {
        'title': 'The Official Frogger',
        'filename': 'Official Frogger, The (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Official Frogger, The (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Official Frogger, The (USA).7z',
        'size': 4570,
    },
    {
        'title': 'Pac-Man',
        'filename': 'Pac-Man (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Pac-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Pac-Man (USA).7z',
        'size': 3302,
    },
    {
        'title': 'Pitfall II: Lost Caverns',
        'filename': 'Pitfall II - Lost Caverns (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Pitfall II - Lost Caverns (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Pitfall II - Lost Caverns (USA).7z',
        'size': 6383,
    },
    {
        'title': "Pitfall!: Pitfall Harry's Jungle Adventure",
        'filename': "Pitfall! - Pitfall Harry's Jungle Adventure (USA).7z",
        'source_relative': "Consoles/Atari 2600 [1977]/Pitfall! - Pitfall Harry's Jungle Adventure (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Pitfall! - Pitfall Harry's Jungle Adventure (USA).7z",
        'size': 3219,
    },
    {
        'title': 'Pole Position',
        'filename': 'Pole Position (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Pole Position (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Pole Position (USA).7z',
        'size': 5300,
    },
    {
        'title': 'Q-bert',
        'filename': 'Q-bert (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Q-bert (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Q-bert (USA).7z',
        'size': 3153,
    },
    {
        'title': 'Raiders of the Lost Ark',
        'filename': 'Raiders of the Lost Ark (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Raiders of the Lost Ark (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Raiders of the Lost Ark (USA).7z',
        'size': 6431,
    },
    {
        'title': 'Rampage',
        'filename': 'Rampage! (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Rampage! (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Rampage! (USA).7z',
        'size': 11521,
    },
    {
        'title': 'River Raid',
        'filename': 'River Raid (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/River Raid (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/River Raid (USA).7z',
        'size': 3278,
    },
    {
        'title': 'Space Invaders',
        'filename': 'Space Invaders (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Space Invaders (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Space Invaders (USA).7z',
        'size': 3433,
    },
    {
        'title': 'Spy Hunter',
        'filename': 'Spy Hunter (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Spy Hunter (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Spy Hunter (USA).7z',
        'size': 5712,
    },
    {
        'title': 'Star Wars: Jedi Arena',
        'filename': 'Star Wars - Jedi Arena (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Star Wars - Jedi Arena (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Star Wars - Jedi Arena (USA).7z',
        'size': 3245,
    },
    {
        'title': 'Star Wars: Return of the Jedi: Death Star Battle',
        'filename': 'Star Wars - Return of the Jedi - Death Star Battle (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Star Wars - Return of the Jedi - Death Star Battle (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Star Wars - Return of the Jedi - Death Star Battle (USA).7z',
        'size': 6334,
    },
    {
        'title': 'Star Wars: Return of the Jedi: Ewok Adventure',
        'filename': 'Star Wars - Return of the Jedi - Ewok Adventure (USA) (Proto).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Star Wars - Return of the Jedi - Ewok Adventure (USA) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Star Wars - Return of the Jedi - Ewok Adventure (USA) (Proto).7z',
        'size': 5782,
    },
    {
        'title': 'Star Wars: The Arcade Game',
        'filename': 'Star Wars - The Arcade Game (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Star Wars - The Arcade Game (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Star Wars - The Arcade Game (USA).7z',
        'size': 5646,
    },
    {
        'title': 'Star Wars: The Empire Strikes Back',
        'filename': 'Star Wars - The Empire Strikes Back (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Star Wars - The Empire Strikes Back (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Star Wars - The Empire Strikes Back (USA).7z',
        'size': 3553,
    },
    {
        'title': 'Super Breakout',
        'filename': 'Super Breakout (USA, Europe) (Atari Anthology).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Super Breakout (USA, Europe) (Atari Anthology).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Super Breakout (USA, Europe) (Atari Anthology).7z',
        'size': 2877,
    },
    {
        'title': 'Swordquest: EarthWorld',
        'filename': 'SwordQuest - EarthWorld (USA, Europe) (Atari Anthology).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/SwordQuest - EarthWorld (USA, Europe) (Atari Anthology).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/SwordQuest - EarthWorld (USA, Europe) (Atari Anthology).7z',
        'size': 5233,
    },
    {
        'title': 'Swordquest: FireWorld',
        'filename': 'SwordQuest - FireWorld (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/SwordQuest - FireWorld (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/SwordQuest - FireWorld (USA).7z',
        'size': 5514,
    },
    {
        'title': 'Swordquest: WaterWorld',
        'filename': 'SwordQuest - WaterWorld (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/SwordQuest - WaterWorld (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/SwordQuest - WaterWorld (USA).7z',
        'size': 5000,
    },
    {
        'title': 'Tapper',
        'filename': 'Tapper (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Tapper (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Tapper (USA).7z',
        'size': 6165,
    },
    {
        'title': 'Warlords',
        'filename': 'Warlords (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/Warlords (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Warlords (USA).7z',
        'size': 2933,
    },
    {
        'title': 'X-Man',
        'filename': 'X-Man (USA).7z',
        'source_relative': 'Consoles/Atari 2600 [1977]/X-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/X-Man (USA).7z',
        'size': 3268,
    },
    {
        'title': "Yars' Revenge",
        'filename': "Yars' Revenge (USA).7z",
        'source_relative': "Consoles/Atari 2600 [1977]/Yars' Revenge (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/atari2600/Yars' Revenge (USA).7z",
        'size': 3460,
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