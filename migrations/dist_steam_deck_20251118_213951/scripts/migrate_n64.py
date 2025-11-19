#!/usr/bin/env python3
# Auto-generated migration script for Nintendo 64
# 119 games, 1.54 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo 64'
ESDE_FOLDER = 'n64'
OPERATION = 'copy'

GAMES = [
    {
        'title': '1080° Snowboarding',
        'filename': '1080 Snowboarding (Japan, USA) (En,Ja).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/1080 Snowboarding (Japan, USA) (En,Ja).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/1080 Snowboarding (Japan, USA) (En,Ja).7z',
        'size': 10438124,
    },
    {
        'title': 'Banjo-Kazooie',
        'filename': 'Banjo-Kazooie (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Banjo-Kazooie (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Banjo-Kazooie (USA) (Rev 1).7z',
        'size': 16277473,
    },
    {
        'title': 'Banjo-Tooie',
        'filename': 'Banjo-Tooie (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Banjo-Tooie (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Banjo-Tooie (USA).7z',
        'size': 32632582,
    },
    {
        'title': 'Batman Beyond: Return of the Joker',
        'filename': 'Batman Beyond - Return of the Joker (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Batman Beyond - Return of the Joker (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Batman Beyond - Return of the Joker (USA).7z',
        'size': 2663046,
    },
    {
        'title': 'Beetle Adventure Racing!',
        'filename': 'Beetle Adventure Racing! (USA) (En,Fr,De).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Beetle Adventure Racing! (USA) (En,Fr,De).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Beetle Adventure Racing! (USA) (En,Fr,De).7z',
        'size': 11651969,
    },
    {
        'title': 'Blast Corps',
        'filename': 'Blast Corps (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Blast Corps (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Blast Corps (USA) (Rev 1).7z',
        'size': 6733775,
    },
    {
        'title': 'Bomberman 64',
        'filename': 'Bomberman 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Bomberman 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Bomberman 64 (USA).7z',
        'size': 4762954,
    },
    {
        'title': 'Bomberman 64: The Second Attack!',
        'filename': 'Bomberman 64 - The Second Attack! (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Bomberman 64 - The Second Attack! (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Bomberman 64 - The Second Attack! (USA).7z',
        'size': 10209559,
    },
    {
        'title': 'Bomberman Hero',
        'filename': 'Bomberman Hero (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Bomberman Hero (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Bomberman Hero (USA).7z',
        'size': 8657149,
    },
    {
        'title': 'Castlevania',
        'filename': 'Castlevania (USA) (Rev 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Castlevania (USA) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Castlevania (USA) (Rev 2).7z',
        'size': 8919363,
    },
    {
        'title': 'Castlevania: Legacy of Darkness',
        'filename': 'Castlevania - Legacy of Darkness (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Castlevania - Legacy of Darkness (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Castlevania - Legacy of Darkness (USA).7z',
        'size': 13335807,
    },
    {
        'title': "Clay Fighter: Sculptor's Cut",
        'filename': "Clay Fighter - Sculptor's Cut (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Clay Fighter - Sculptor's Cut (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Clay Fighter - Sculptor's Cut (USA).7z",
        'size': 13280944,
    },
    {
        'title': 'Clay Fighter 63 1/3',
        'filename': 'Clay Fighter 63 1-3 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Clay Fighter 63 1-3 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Clay Fighter 63 1-3 (USA).7z',
        'size': 9593904,
    },
    {
        'title': 'Command & Conquer',
        'filename': 'Command & Conquer (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Command & Conquer (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Command & Conquer (USA).7z',
        'size': 12800850,
    },
    {
        'title': "Conker's Bad Fur Day",
        'filename': "Conker's Bad Fur Day (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Conker's Bad Fur Day (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Conker's Bad Fur Day (USA).7z",
        'size': 60077904,
    },
    {
        'title': "Cruis'n USA",
        'filename': "Cruis'n USA (USA) (Rev 1).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Cruis'n USA (USA) (Rev 1).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Cruis'n USA (USA) (Rev 1).7z",
        'size': 3877130,
    },
    {
        'title': "Cruis'n World",
        'filename': "Cruis'n World (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Cruis'n World (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Cruis'n World (USA).7z",
        'size': 10937091,
    },
    {
        'title': 'Diddy Kong Racing',
        'filename': 'Diddy Kong Racing (USA) (En,Fr) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Diddy Kong Racing (USA) (En,Fr) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Diddy Kong Racing (USA) (En,Fr) (Rev 1).7z',
        'size': 9863489,
    },
    {
        'title': 'Die Hard 64',
        'filename': 'Die Hard 64 (USA) (Proto) (Level 3).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Die Hard 64 (USA) (Proto) (Level 3).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Die Hard 64 (USA) (Proto) (Level 3).7z',
        'size': 6044428,
    },
    {
        'title': 'Donkey Kong 64',
        'filename': 'Donkey Kong 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Donkey Kong 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Donkey Kong 64 (USA).7z',
        'size': 26708197,
    },
    {
        'title': 'DOOM 64',
        'filename': 'Doom 64 (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Doom 64 (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Doom 64 (USA) (Rev 1).7z',
        'size': 7098356,
    },
    {
        'title': 'Dr. Mario 64',
        'filename': 'Dr. Mario 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Dr. Mario 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Dr. Mario 64 (USA).7z',
        'size': 3007011,
    },
    {
        'title': 'Duke Nukem: Zero Hour',
        'filename': 'Duke Nukem - Zero Hour (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Duke Nukem - Zero Hour (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Duke Nukem - Zero Hour (USA).7z',
        'size': 22806789,
    },
    {
        'title': 'Duke Nukem 64',
        'filename': 'Duke Nukem 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Duke Nukem 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Duke Nukem 64 (USA).7z',
        'size': 7281915,
    },
    {
        'title': 'Earthworm Jim 3D',
        'filename': 'Earthworm Jim 3D (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Earthworm Jim 3D (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Earthworm Jim 3D (USA).7z',
        'size': 9962305,
    },
    {
        'title': 'Excitebike 64',
        'filename': 'Excitebike 64 (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Excitebike 64 (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Excitebike 64 (USA) (Rev 1).7z',
        'size': 14972666,
    },
    {
        'title': 'F-Zero X',
        'filename': 'F-Zero X (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/F-Zero X (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/F-Zero X (USA).7z',
        'size': 12483980,
    },
    {
        'title': "Frogger 2: Swampy's Revenge",
        'filename': 'Frogger 2 (USA) (Proto 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Frogger 2 (USA) (Proto 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Frogger 2 (USA) (Proto 2).7z',
        'size': 649669,
    },
    {
        'title': 'Gex 3: Deep Cover Gecko',
        'filename': 'Gex 3 - Deep Cover Gecko (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Gex 3 - Deep Cover Gecko (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Gex 3 - Deep Cover Gecko (USA).7z',
        'size': 24163651,
    },
    {
        'title': 'Gex 64: Enter the Gecko',
        'filename': 'Gex 64 - Enter the Gecko (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Gex 64 - Enter the Gecko (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Gex 64 - Enter the Gecko (USA).7z',
        'size': 14925047,
    },
    {
        'title': 'Glover',
        'filename': 'Glover (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Glover (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Glover (USA).7z',
        'size': 5220296,
    },
    {
        'title': "Goemon's Great Adventure",
        'filename': "Goemon's Great Adventure (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Goemon's Great Adventure (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Goemon's Great Adventure (USA).7z",
        'size': 14032455,
    },
    {
        'title': 'GoldenEye 007',
        'filename': 'GoldenEye 007 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/GoldenEye 007 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/GoldenEye 007 (USA).7z',
        'size': 10146766,
    },
    {
        'title': 'Harvest Moon 64',
        'filename': 'Harvest Moon 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Harvest Moon 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Harvest Moon 64 (USA).7z',
        'size': 4634245,
    },
    {
        'title': 'Hey You, Pikachu!',
        'filename': 'Hey You, Pikachu! (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Hey You, Pikachu! (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Hey You, Pikachu! (USA).7z',
        'size': 8008565,
    },
    {
        'title': "International Superstar Soccer '98",
        'filename': "International Superstar Soccer '98 (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/International Superstar Soccer '98 (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/International Superstar Soccer '98 (USA).7z",
        'size': 8676858,
    },
    {
        'title': 'Jet Force Gemini',
        'filename': 'Jet Force Gemini (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Jet Force Gemini (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Jet Force Gemini (USA).7z',
        'size': 28737353,
    },
    {
        'title': 'Kirby 64: The Crystal Shards',
        'filename': 'Kirby 64 - The Crystal Shards (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Kirby 64 - The Crystal Shards (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Kirby 64 - The Crystal Shards (USA).7z',
        'size': 8778384,
    },
    {
        'title': "The Legend of Zelda: Majora's Mask",
        'filename': "Legend of Zelda, The - Majora's Mask (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Legend of Zelda, The - Majora's Mask (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Legend of Zelda, The - Majora's Mask (USA).7z",
        'size': 24239956,
    },
    {
        'title': 'The Legend of Zelda: Ocarina of Time',
        'filename': 'Legend of Zelda, The - Ocarina of Time (USA) (Rev 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Legend of Zelda, The - Ocarina of Time (USA) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Legend of Zelda, The - Ocarina of Time (USA) (Rev 2).7z',
        'size': 23003946,
    },
    {
        'title': 'The Legend of Zelda: Ocarina of Time Master Quest',
        'filename': 'Legend of Zelda, The - Ocarina of Time - Master Quest (USA) (GameCube).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Legend of Zelda, The - Ocarina of Time - Master Quest (USA) (GameCube).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Legend of Zelda, The - Ocarina of Time - Master Quest (USA) (GameCube).7z',
        'size': 22985123,
    },
    {
        'title': 'LEGO Racers',
        'filename': 'LEGO Racers (USA) (En,Fr,De,Es,It,Nl,Sv,No,Da,Fi).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/LEGO Racers (USA) (En,Fr,De,Es,It,Nl,Sv,No,Da,Fi).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/LEGO Racers (USA) (En,Fr,De,Es,It,Nl,Sv,No,Da,Fi).7z',
        'size': 8254623,
    },
    {
        'title': 'Madden NFL 2001',
        'filename': 'Madden NFL 2001 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Madden NFL 2001 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Madden NFL 2001 (USA).7z',
        'size': 10782763,
    },
    {
        'title': 'Mario Golf',
        'filename': 'Mario Golf (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mario Golf (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mario Golf (USA).7z',
        'size': 15536962,
    },
    {
        'title': 'Mario Kart 64',
        'filename': 'Mario Kart 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mario Kart 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mario Kart 64 (USA).7z',
        'size': 8007331,
    },
    {
        'title': 'Mario Party',
        'filename': 'Mario Party (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mario Party (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mario Party (USA).7z',
        'size': 18183250,
    },
    {
        'title': 'Mario Party 2',
        'filename': 'Mario Party 2 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mario Party 2 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mario Party 2 (USA).7z',
        'size': 20722980,
    },
    {
        'title': 'Mario Party 3',
        'filename': 'Mario Party 3 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mario Party 3 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mario Party 3 (USA).7z',
        'size': 22459202,
    },
    {
        'title': 'Mario Tennis',
        'filename': 'Mario Tennis (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mario Tennis (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mario Tennis (USA).7z',
        'size': 13375952,
    },
    {
        'title': 'Mega Man 64',
        'filename': 'Mega Man 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mega Man 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mega Man 64 (USA).7z',
        'size': 25184230,
    },
    {
        'title': "Midway's Greatest Arcade Hits: Volume 1",
        'filename': "Midway's Greatest Arcade Hits - Volume 1 (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Midway's Greatest Arcade Hits - Volume 1 (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Midway's Greatest Arcade Hits - Volume 1 (USA).7z",
        'size': 1632989,
    },
    {
        'title': 'Mischief Makers',
        'filename': 'Mischief Makers (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mischief Makers (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mischief Makers (USA) (Rev 1).7z',
        'size': 5252033,
    },
    {
        'title': 'Mischief Makers',
        'filename': 'Mischief Makers (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mischief Makers (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mischief Makers (USA) (Rev 1).7z',
        'size': 5249221,
    },
    {
        'title': 'Mortal Kombat 4',
        'filename': 'Mortal Kombat 4 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mortal Kombat 4 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mortal Kombat 4 (USA).7z',
        'size': 13393827,
    },
    {
        'title': 'Mortal Kombat Mythologies: Sub-Zero',
        'filename': 'Mortal Kombat Mythologies - Sub-Zero (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mortal Kombat Mythologies - Sub-Zero (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mortal Kombat Mythologies - Sub-Zero (USA).7z',
        'size': 12812530,
    },
    {
        'title': 'Mortal Kombat Trilogy',
        'filename': 'Mortal Kombat Trilogy (USA) (Rev 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mortal Kombat Trilogy (USA) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mortal Kombat Trilogy (USA) (Rev 2).7z',
        'size': 10073855,
    },
    {
        'title': 'Ms. Pac-Man Maze Madness',
        'filename': 'Ms. Pac-Man - Maze Madness (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Ms. Pac-Man - Maze Madness (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Ms. Pac-Man - Maze Madness (USA).7z',
        'size': 9360643,
    },
    {
        'title': 'Mystical Ninja Starring Goemon',
        'filename': 'Mystical Ninja Starring Goemon (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Mystical Ninja Starring Goemon (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Mystical Ninja Starring Goemon (USA).7z',
        'size': 11851175,
    },
    {
        'title': 'Namco Museum 64',
        'filename': 'Namco Museum 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Namco Museum 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Namco Museum 64 (USA).7z',
        'size': 2798697,
    },
    {
        'title': 'NBA Courtside 2 featuring Kobe Bryant',
        'filename': 'NBA Courtside 2 featuring Kobe Bryant (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/NBA Courtside 2 featuring Kobe Bryant (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/NBA Courtside 2 featuring Kobe Bryant (USA).7z',
        'size': 13022286,
    },
    {
        'title': 'NBA Hangtime',
        'filename': 'NBA Hangtime (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/NBA Hangtime (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/NBA Hangtime (USA).7z',
        'size': 9843101,
    },
    {
        'title': 'NBA Jam 2000',
        'filename': 'NBA Jam 2000 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/NBA Jam 2000 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/NBA Jam 2000 (USA).7z',
        'size': 14049509,
    },
    {
        'title': 'NBA Jam 99',
        'filename': 'NBA Jam 99 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/NBA Jam 99 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/NBA Jam 99 (USA).7z',
        'size': 10659695,
    },
    {
        'title': 'The New Tetris',
        'filename': 'New Tetris, The (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/New Tetris, The (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/New Tetris, The (USA).7z',
        'size': 9330916,
    },
    {
        'title': 'Nightmare Creatures',
        'filename': 'Nightmare Creatures (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Nightmare Creatures (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Nightmare Creatures (USA).7z',
        'size': 9567938,
    },
    {
        'title': 'Nuclear Strike 64',
        'filename': 'Nuclear Strike 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Nuclear Strike 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Nuclear Strike 64 (USA).7z',
        'size': 15899631,
    },
    {
        'title': 'Ogre Battle 64: Person of Lordly Caliber',
        'filename': 'Ogre Battle 64 - Person of Lordly Caliber (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Ogre Battle 64 - Person of Lordly Caliber (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Ogre Battle 64 - Person of Lordly Caliber (USA) (Rev 1).7z',
        'size': 32824650,
    },
    {
        'title': 'Paper Mario',
        'filename': 'Paper Mario (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Paper Mario (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Paper Mario (USA).7z',
        'size': 18951833,
    },
    {
        'title': 'Paperboy',
        'filename': 'Paperboy (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Paperboy (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Paperboy (USA).7z',
        'size': 5663185,
    },
    {
        'title': 'Perfect Dark',
        'filename': 'Perfect Dark (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Perfect Dark (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Perfect Dark (USA) (Rev 1).7z',
        'size': 28827843,
    },
    {
        'title': 'Pilotwings 64',
        'filename': 'Pilotwings 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Pilotwings 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Pilotwings 64 (USA).7z',
        'size': 4499988,
    },
    {
        'title': 'Pokemon Puzzle League',
        'filename': 'Pokemon Puzzle League (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Pokemon Puzzle League (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Pokemon Puzzle League (USA).7z',
        'size': 19667303,
    },
    {
        'title': 'Pokemon Snap',
        'filename': 'Pokemon Snap (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Pokemon Snap (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Pokemon Snap (USA).7z',
        'size': 7905193,
    },
    {
        'title': 'Pokemon Stadium',
        'filename': 'Pokemon Stadium (USA) (Rev 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Pokemon Stadium (USA) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Pokemon Stadium (USA) (Rev 2).7z',
        'size': 24959270,
    },
    {
        'title': 'Pokemon Stadium 2',
        'filename': 'Pokemon Stadium 2 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Pokemon Stadium 2 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Pokemon Stadium 2 (USA).7z',
        'size': 42137790,
    },
    {
        'title': 'Quake',
        'filename': 'Quake (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Quake (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Quake (USA).7z',
        'size': 11471751,
    },
    {
        'title': 'Quake II',
        'filename': 'Quake II (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Quake II (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Quake II (USA).7z',
        'size': 11501204,
    },
    {
        'title': 'Quest 64',
        'filename': 'Quest 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Quest 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Quest 64 (USA).7z',
        'size': 5116413,
    },
    {
        'title': 'Rampage: World Tour',
        'filename': 'Rampage - World Tour (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Rampage - World Tour (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Rampage - World Tour (USA).7z',
        'size': 9810829,
    },
    {
        'title': 'Rampage 2: Universal Tour',
        'filename': 'Rampage 2 - Universal Tour (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Rampage 2 - Universal Tour (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Rampage 2 - Universal Tour (USA).7z',
        'size': 10430736,
    },
    {
        'title': 'Rayman 2: The Great Escape',
        'filename': 'Rayman 2 - The Great Escape (USA) (En,Fr,De,Es,It).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Rayman 2 - The Great Escape (USA) (En,Fr,De,Es,It).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Rayman 2 - The Great Escape (USA) (En,Fr,De,Es,It).7z',
        'size': 14841605,
    },
    {
        'title': 'Razor Freestyle Scooter',
        'filename': 'Razor Freestyle Scooter (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Razor Freestyle Scooter (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Razor Freestyle Scooter (USA).7z',
        'size': 6104044,
    },
    {
        'title': 'Resident Evil 2',
        'filename': 'Resident Evil 2 (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Resident Evil 2 (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Resident Evil 2 (USA) (Rev 1).7z',
        'size': 64839574,
    },
    {
        'title': 'Road Rash 64',
        'filename': 'Road Rash 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Road Rash 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Road Rash 64 (USA).7z',
        'size': 16173701,
    },
    {
        'title': 'Shadowgate 64: Trials of the Four Towers',
        'filename': 'Shadowgate 64 - Trials of the Four Towers (USA) (En,Es).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Shadowgate 64 - Trials of the Four Towers (USA) (En,Es).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Shadowgate 64 - Trials of the Four Towers (USA) (En,Es).7z',
        'size': 10849035,
    },
    {
        'title': 'Snowboard Kids',
        'filename': 'Snowboard Kids (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Snowboard Kids (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Snowboard Kids (USA).7z',
        'size': 4577998,
    },
    {
        'title': 'Snowboard Kids 2',
        'filename': 'Snowboard Kids 2 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Snowboard Kids 2 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Snowboard Kids 2 (USA).7z',
        'size': 10102371,
    },
    {
        'title': 'South Park',
        'filename': 'South Park (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/South Park (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/South Park (USA).7z',
        'size': 12420187,
    },
    {
        'title': "South Park: Chef's Luv Shack",
        'filename': "South Park - Chef's Luv Shack (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/South Park - Chef's Luv Shack (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/South Park - Chef's Luv Shack (USA).7z",
        'size': 13819482,
    },
    {
        'title': 'South Park Rally',
        'filename': 'South Park Rally (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/South Park Rally (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/South Park Rally (USA).7z',
        'size': 13145648,
    },
    {
        'title': 'Space Invaders',
        'filename': 'Space Invaders (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Space Invaders (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Space Invaders (USA).7z',
        'size': 5623529,
    },
    {
        'title': 'Star Fox 64',
        'filename': 'Star Fox 64 (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Star Fox 64 (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Star Fox 64 (USA) (Rev 1).7z',
        'size': 9887751,
    },
    {
        'title': 'Star Wars: Rogue Squadron',
        'filename': 'Star Wars - Rogue Squadron (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Star Wars - Rogue Squadron (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Star Wars - Rogue Squadron (USA) (Rev 1).7z',
        'size': 13940680,
    },
    {
        'title': 'Star Wars: Shadows of the Empire',
        'filename': 'Star Wars - Shadows of the Empire (USA) (Rev 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Star Wars - Shadows of the Empire (USA) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Star Wars - Shadows of the Empire (USA) (Rev 2).7z',
        'size': 11739750,
    },
    {
        'title': 'Star Wars: Episode I: Battle for Naboo',
        'filename': 'Star Wars Episode I - Battle for Naboo (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Star Wars Episode I - Battle for Naboo (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Star Wars Episode I - Battle for Naboo (USA).7z',
        'size': 25065349,
    },
    {
        'title': 'Star Wars: Episode I: Racer',
        'filename': 'Star Wars Episode I - Racer (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Star Wars Episode I - Racer (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Star Wars Episode I - Racer (USA).7z',
        'size': 23891929,
    },
    {
        'title': 'StarCraft 64',
        'filename': 'StarCraft 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/StarCraft 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/StarCraft 64 (USA).7z',
        'size': 24286362,
    },
    {
        'title': 'Super Mario 64',
        'filename': 'Super Mario 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Super Mario 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Super Mario 64 (USA).7z',
        'size': 5638835,
    },
    {
        'title': 'Super Smash Bros.',
        'filename': 'Super Smash Bros. (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Super Smash Bros. (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Super Smash Bros. (USA).7z',
        'size': 11681853,
    },
    {
        'title': 'Taz Express',
        'filename': 'Taz Express (USA) (Proto) (2000-05-15).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Taz Express (USA) (Proto) (2000-05-15).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Taz Express (USA) (Proto) (2000-05-15).7z',
        'size': 13195329,
    },
    {
        'title': "Tom Clancy's Rainbow Six",
        'filename': "Tom Clancy's Rainbow Six (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Tom Clancy's Rainbow Six (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Tom Clancy's Rainbow Six (USA).7z",
        'size': 13525273,
    },
    {
        'title': "Tony Hawk's Pro Skater",
        'filename': "Tony Hawk's Pro Skater (USA) (Rev 1).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Tony Hawk's Pro Skater (USA) (Rev 1).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Tony Hawk's Pro Skater (USA) (Rev 1).7z",
        'size': 10745952,
    },
    {
        'title': "Tony Hawk's Pro Skater 2",
        'filename': "Tony Hawk's Pro Skater 2 (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Tony Hawk's Pro Skater 2 (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Tony Hawk's Pro Skater 2 (USA).7z",
        'size': 14906466,
    },
    {
        'title': "Tony Hawk's Pro Skater 3",
        'filename': "Tony Hawk's Pro Skater 3 (USA).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Tony Hawk's Pro Skater 3 (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Tony Hawk's Pro Skater 3 (USA).7z",
        'size': 14659876,
    },
    {
        'title': 'Turok: Dinosaur Hunter',
        'filename': 'Turok - Dinosaur Hunter (USA) (Rev 2).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Turok - Dinosaur Hunter (USA) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Turok - Dinosaur Hunter (USA) (Rev 2).7z',
        'size': 7271651,
    },
    {
        'title': 'Turok: Rage Wars',
        'filename': 'Turok - Rage Wars (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Turok - Rage Wars (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Turok - Rage Wars (USA) (Rev 1).7z',
        'size': 5225143,
    },
    {
        'title': 'Turok 2: Seeds of Evil',
        'filename': 'Turok 2 - Seeds of Evil (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Turok 2 - Seeds of Evil (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Turok 2 - Seeds of Evil (USA) (Rev 1).7z',
        'size': 27735883,
    },
    {
        'title': 'Turok 3: Shadow of Oblivion',
        'filename': 'Turok 3 - Shadow of Oblivion (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Turok 3 - Shadow of Oblivion (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Turok 3 - Shadow of Oblivion (USA).7z',
        'size': 25734942,
    },
    {
        'title': 'Wave Race 64: Kawasaki Jet Ski',
        'filename': 'Wave Race 64 - Kawasaki Jet Ski (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Wave Race 64 - Kawasaki Jet Ski (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Wave Race 64 - Kawasaki Jet Ski (USA) (Rev 1).7z',
        'size': 5497928,
    },
    {
        'title': 'WCW Mayhem',
        'filename': 'WCW Mayhem (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WCW Mayhem (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WCW Mayhem (USA).7z',
        'size': 12673971,
    },
    {
        'title': 'WCW Nitro',
        'filename': 'WCW Nitro (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WCW Nitro (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WCW Nitro (USA).7z',
        'size': 5910772,
    },
    {
        'title': 'WCW Vs. nWo: World Tour',
        'filename': 'WCW vs. nWo - World Tour (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WCW vs. nWo - World Tour (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WCW vs. nWo - World Tour (USA) (Rev 1).7z',
        'size': 6865166,
    },
    {
        'title': 'WCW/nWo Revenge',
        'filename': 'WCW-nWo Revenge (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WCW-nWo Revenge (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WCW-nWo Revenge (USA).7z',
        'size': 9677998,
    },
    {
        'title': 'Wipeout 64',
        'filename': 'Wipeout 64 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/Wipeout 64 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Wipeout 64 (USA).7z',
        'size': 5402950,
    },
    {
        'title': 'WWF Attitude',
        'filename': 'WWF Attitude (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WWF Attitude (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WWF Attitude (USA).7z',
        'size': 29616891,
    },
    {
        'title': 'WWF No Mercy',
        'filename': 'WWF No Mercy (USA) (Rev 1).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WWF No Mercy (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WWF No Mercy (USA) (Rev 1).7z',
        'size': 22345185,
    },
    {
        'title': 'WWF War Zone',
        'filename': 'WWF War Zone (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WWF War Zone (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WWF War Zone (USA).7z',
        'size': 10731531,
    },
    {
        'title': 'WWF WrestleMania 2000',
        'filename': 'WWF WrestleMania 2000 (USA).7z',
        'source_relative': 'Consoles/Nintendo 64 [1996]/WWF WrestleMania 2000 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/WWF WrestleMania 2000 (USA).7z',
        'size': 19540706,
    },
    {
        'title': "Yoshi's Story",
        'filename': "Yoshi's Story (USA) (En,Ja).7z",
        'source_relative': "Consoles/Nintendo 64 [1996]/Yoshi's Story (USA) (En,Ja).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n64/Yoshi's Story (USA) (En,Ja).7z",
        'size': 8213020,
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