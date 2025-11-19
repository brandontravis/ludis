#!/usr/bin/env python3
# Auto-generated migration script for Sega Game Gear
# 86 games, 14.10 MB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sega Game Gear'
ESDE_FOLDER = 'gamegear'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'The Addams Family',
        'filename': 'Addams Family, The (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Addams Family, The (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Addams Family, The (World).7z',
        'size': 168999,
    },
    {
        'title': 'The Adventures of Batman & Robin',
        'filename': 'Adventures of Batman & Robin, The (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Adventures of Batman & Robin, The (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Adventures of Batman & Robin, The (USA, Europe).7z',
        'size': 246163,
    },
    {
        'title': 'Arcade Classics',
        'filename': 'Arcade Classics (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Arcade Classics (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Arcade Classics (USA).7z',
        'size': 52632,
    },
    {
        'title': 'Arch Rivals: The Arcade Game',
        'filename': 'Arch Rivals - The Arcade Game (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Arch Rivals - The Arcade Game (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Arch Rivals - The Arcade Game (USA).7z',
        'size': 92080,
    },
    {
        'title': 'Baku Baku',
        'filename': 'Baku Baku (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Baku Baku (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Baku Baku (USA).7z',
        'size': 130190,
    },
    {
        'title': 'Batman Forever',
        'filename': 'Batman Forever (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Batman Forever (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Batman Forever (World).7z',
        'size': 229293,
    },
    {
        'title': 'Batman Returns',
        'filename': 'Batman Returns (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Batman Returns (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Batman Returns (World).7z',
        'size': 148161,
    },
    {
        'title': 'Battletoads',
        'filename': 'Battletoads (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Battletoads (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Battletoads (USA).7z',
        'size': 146191,
    },
    {
        'title': 'Beavis and Butt-Head',
        'filename': 'Beavis and Butt-Head (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Beavis and Butt-Head (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Beavis and Butt-Head (USA, Europe).7z',
        'size': 250908,
    },
    {
        'title': 'Bubble Bobble',
        'filename': 'Bubble Bobble (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Bubble Bobble (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Bubble Bobble (USA).7z',
        'size': 109200,
    },
    {
        'title': 'Bugs Bunny in Double Trouble',
        'filename': 'Bugs Bunny in Double Trouble (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Bugs Bunny in Double Trouble (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Bugs Bunny in Double Trouble (USA, Europe).7z',
        'size': 242580,
    },
    {
        'title': 'Castle of Illusion Starring Mickey Mouse',
        'filename': 'Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (En).7z',
        'size': 128653,
    },
    {
        'title': 'Chuck Rock',
        'filename': 'Chuck Rock (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Chuck Rock (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Chuck Rock (World).7z',
        'size': 139484,
    },
    {
        'title': 'Columns',
        'filename': 'Columns (USA, Europe, Brazil) (En) (Rev 2).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Columns (USA, Europe, Brazil) (En) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Columns (USA, Europe, Brazil) (En) (Rev 2).7z',
        'size': 19384,
    },
    {
        'title': 'Defenders of Oasis',
        'filename': 'Defenders of Oasis (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Defenders of Oasis (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Defenders of Oasis (USA, Europe).7z',
        'size': 286810,
    },
    {
        'title': 'Desert Strike: Return to the Gulf',
        'filename': 'Desert Strike - Return to the Gulf (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Desert Strike - Return to the Gulf (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Desert Strike - Return to the Gulf (USA).7z',
        'size': 173783,
    },
    {
        'title': 'Double Dragon',
        'filename': 'Double Dragon (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Double Dragon (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Double Dragon (USA, Europe).7z',
        'size': 202724,
    },
    {
        'title': "Dr. Robotnik's Mean Bean Machine",
        'filename': "Dr. Robotnik's Mean Bean Machine (USA, Europe).7z",
        'source_relative': "Handhelds/Sega Game Gear [1990]/Dr. Robotnik's Mean Bean Machine (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Dr. Robotnik's Mean Bean Machine (USA, Europe).7z",
        'size': 111577,
    },
    {
        'title': 'Dynamite Headdy',
        'filename': 'Dynamite Headdy (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Dynamite Headdy (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Dynamite Headdy (USA, Europe).7z',
        'size': 157435,
    },
    {
        'title': 'Earthworm Jim',
        'filename': 'Earthworm Jim (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Earthworm Jim (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Earthworm Jim (USA).7z',
        'size': 220343,
    },
    {
        'title': 'Ecco: The Tides of Time',
        'filename': 'Ecco - The Tides of Time (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Ecco - The Tides of Time (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Ecco - The Tides of Time (USA, Europe, Brazil) (En).7z',
        'size': 177244,
    },
    {
        'title': 'Ecco the Dolphin',
        'filename': 'Ecco The Dolphin (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Ecco The Dolphin (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Ecco The Dolphin (USA, Europe, Brazil) (En).7z',
        'size': 183769,
    },
    {
        'title': 'Factory Panic',
        'filename': 'Factory Panic (Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Factory Panic (Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Factory Panic (Europe, Brazil) (En).7z',
        'size': 55283,
    },
    {
        'title': 'Fatal Fury Special',
        'filename': 'Fatal Fury Special (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Fatal Fury Special (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Fatal Fury Special (USA).7z',
        'size': 271041,
    },
    {
        'title': 'Frogger',
        'filename': 'Frogger (USA) (Proto).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Frogger (USA) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Frogger (USA) (Proto).7z',
        'size': 46097,
    },
    {
        'title': 'Galaga 2',
        'filename': 'Galaga 2 (Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Galaga 2 (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Galaga 2 (Europe).7z',
        'size': 50725,
    },
    {
        'title': 'Home Alone',
        'filename': 'Home Alone (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Home Alone (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Home Alone (USA, Europe, Brazil) (En).7z',
        'size': 130586,
    },
    {
        'title': 'Hook',
        'filename': 'Hook (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Hook (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Hook (USA).7z',
        'size': 133782,
    },
    {
        'title': 'The Itchy & Scratchy Game',
        'filename': 'Itchy & Scratchy Game, The (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Itchy & Scratchy Game, The (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Itchy & Scratchy Game, The (USA, Europe).7z',
        'size': 111158,
    },
    {
        'title': 'Jungle Strike',
        'filename': 'Jungle Strike (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Jungle Strike (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Jungle Strike (USA).7z',
        'size': 222238,
    },
    {
        'title': 'Jurassic Park',
        'filename': 'Jurassic Park (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Jurassic Park (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Jurassic Park (USA, Europe, Brazil) (En).7z',
        'size': 314030,
    },
    {
        'title': "Krusty's Fun House",
        'filename': "Krusty's Fun House (USA, Europe).7z",
        'source_relative': "Handhelds/Sega Game Gear [1990]/Krusty's Fun House (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Krusty's Fun House (USA, Europe).7z",
        'size': 148265,
    },
    {
        'title': 'Legend of Illusion Starring Mickey Mouse',
        'filename': 'Legend of Illusion Starring Mickey Mouse (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Legend of Illusion Starring Mickey Mouse (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Legend of Illusion Starring Mickey Mouse (USA, Europe).7z',
        'size': 233611,
    },
    {
        'title': 'Lemmings',
        'filename': 'Lemmings (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Lemmings (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Lemmings (World).7z',
        'size': 110664,
    },
    {
        'title': 'The Lion King',
        'filename': 'Lion King, The (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Lion King, The (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Lion King, The (USA).7z',
        'size': 248866,
    },
    {
        'title': 'The Lost World: Jurassic Park',
        'filename': 'Lost World, The - Jurassic Park (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Lost World, The - Jurassic Park (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Lost World, The - Jurassic Park (USA).7z',
        'size': 303013,
    },
    {
        'title': 'Marble Madness',
        'filename': 'Marble Madness (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Marble Madness (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Marble Madness (USA, Europe).7z',
        'size': 77545,
    },
    {
        'title': 'Mega Man',
        'filename': 'Mega Man (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Mega Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Mega Man (USA).7z',
        'size': 163480,
    },
    {
        'title': 'Mortal Kombat',
        'filename': 'Mortal Kombat (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Mortal Kombat (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Mortal Kombat (USA, Europe).7z',
        'size': 351830,
    },
    {
        'title': 'Mortal Kombat 3',
        'filename': 'Mortal Kombat 3 (Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Mortal Kombat 3 (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Mortal Kombat 3 (Europe).7z',
        'size': 227811,
    },
    {
        'title': 'Mortal Kombat II',
        'filename': 'Mortal Kombat II (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Mortal Kombat II (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Mortal Kombat II (World).7z',
        'size': 366138,
    },
    {
        'title': 'Ms. Pac-Man',
        'filename': 'Ms. Pac-Man (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Ms. Pac-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Ms. Pac-Man (USA).7z',
        'size': 43246,
    },
    {
        'title': 'NBA Jam',
        'filename': 'NBA Jam (USA) (Rev 1).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/NBA Jam (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/NBA Jam (USA) (Rev 1).7z',
        'size': 202192,
    },
    {
        'title': 'NBA Jam Tournament Edition',
        'filename': 'NBA Jam - Tournament Edition (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/NBA Jam - Tournament Edition (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/NBA Jam - Tournament Edition (World).7z',
        'size': 256005,
    },
    {
        'title': 'Ninja Gaiden',
        'filename': 'Ninja Gaiden (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Ninja Gaiden (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Ninja Gaiden (USA, Europe, Brazil) (En).7z',
        'size': 58351,
    },
    {
        'title': 'OutRun',
        'filename': 'OutRun (Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/OutRun (Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/OutRun (Europe, Brazil) (En).7z',
        'size': 57717,
    },
    {
        'title': 'OutRun Europa',
        'filename': 'OutRun Europa (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/OutRun Europa (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/OutRun Europa (USA).7z',
        'size': 86707,
    },
    {
        'title': 'Pac-Attack',
        'filename': 'Pac-Attack (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Pac-Attack (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Pac-Attack (USA).7z',
        'size': 64032,
    },
    {
        'title': 'Pac-in-Time',
        'filename': 'Pac-in-Time (USA) (Proto).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Pac-in-Time (USA) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Pac-in-Time (USA) (Proto).7z',
        'size': 172578,
    },
    {
        'title': 'Pac-Man',
        'filename': 'Pac-Man (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Pac-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Pac-Man (USA).7z',
        'size': 17835,
    },
    {
        'title': 'Paperboy',
        'filename': 'Paperboy (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Paperboy (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Paperboy (USA, Europe).7z',
        'size': 47067,
    },
    {
        'title': 'Paperboy 2',
        'filename': 'Paperboy 2 (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Paperboy 2 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Paperboy 2 (USA).7z',
        'size': 120692,
    },
    {
        'title': 'Primal Rage',
        'filename': 'Primal Rage (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Primal Rage (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Primal Rage (USA, Europe).7z',
        'size': 276172,
    },
    {
        'title': 'Prince of Persia',
        'filename': 'Prince of Persia (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Prince of Persia (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Prince of Persia (USA, Europe).7z',
        'size': 96841,
    },
    {
        'title': "R.B.I. Baseball '94",
        'filename': "R.B.I. Baseball '94 (USA).7z",
        'source_relative': "Handhelds/Sega Game Gear [1990]/R.B.I. Baseball '94 (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/R.B.I. Baseball '94 (USA).7z",
        'size': 123513,
    },
    {
        'title': 'Shaq Fu',
        'filename': 'Shaq Fu (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Shaq Fu (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Shaq Fu (USA).7z',
        'size': 257185,
    },
    {
        'title': 'Shining Force: The Sword of Hajya',
        'filename': 'Shining Force - The Sword of Hajya (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Shining Force - The Sword of Hajya (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Shining Force - The Sword of Hajya (USA).7z',
        'size': 355853,
    },
    {
        'title': 'GG Shinobi ~ Shinobi',
        'filename': 'Shinobi (World) (Rev A).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Shinobi (World) (Rev A).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Shinobi (World) (Rev A).7z',
        'size': 168263,
    },
    {
        'title': 'Shinobi II: The Silent Fury',
        'filename': 'Shinobi II - The Silent Fury (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Shinobi II - The Silent Fury (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Shinobi II - The Silent Fury (World).7z',
        'size': 155935,
    },
    {
        'title': 'The Simpsons: Bart vs. the Space Mutants',
        'filename': 'Simpsons, The - Bart vs. the Space Mutants (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Simpsons, The - Bart vs. the Space Mutants (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Simpsons, The - Bart vs. the Space Mutants (USA, Europe).7z',
        'size': 134104,
    },
    {
        'title': 'The Simpsons: Bart vs. the World',
        'filename': 'Simpsons, The - Bart vs. the World (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Simpsons, The - Bart vs. the World (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Simpsons, The - Bart vs. the World (World).7z',
        'size': 152615,
    },
    {
        'title': 'The Simpsons: Bartman Meets Radioactive Man',
        'filename': 'Simpsons, The - Bartman Meets Radioactive Man (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Simpsons, The - Bartman Meets Radioactive Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Simpsons, The - Bartman Meets Radioactive Man (USA).7z',
        'size': 168563,
    },
    {
        'title': 'G-Sonic: Sonic Blast',
        'filename': 'Sonic Blast (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic Blast (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic Blast (World).7z',
        'size': 373288,
    },
    {
        'title': 'Sonic Chaos',
        'filename': 'Sonic Chaos (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic Chaos (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic Chaos (USA, Europe, Brazil) (En).7z',
        'size': 194819,
    },
    {
        'title': 'Sonic Drift 2',
        'filename': 'Sonic Drift 2 (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic Drift 2 (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic Drift 2 (World).7z',
        'size': 255796,
    },
    {
        'title': 'Sonic Labyrinth',
        'filename': 'Sonic Labyrinth (USA, Europe) (Virtual Console).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic Labyrinth (USA, Europe) (Virtual Console).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic Labyrinth (USA, Europe) (Virtual Console).7z',
        'size': 171216,
    },
    {
        'title': 'Sonic Spinball',
        'filename': 'Sonic Spinball (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic Spinball (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic Spinball (USA, Europe, Brazil) (En).7z',
        'size': 194578,
    },
    {
        'title': 'Sonic the Hedgehog',
        'filename': 'Sonic The Hedgehog (World) (Rev 1) (Virtual Console).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic The Hedgehog (World) (Rev 1) (Virtual Console).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic The Hedgehog (World) (Rev 1) (Virtual Console).7z',
        'size': 139604,
    },
    {
        'title': 'Sonic the Hedgehog: Triple Trouble',
        'filename': 'Sonic The Hedgehog - Triple Trouble (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic The Hedgehog - Triple Trouble (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic The Hedgehog - Triple Trouble (USA, Europe, Brazil) (En).7z',
        'size': 248805,
    },
    {
        'title': 'Sonic the Hedgehog 2',
        'filename': 'Sonic The Hedgehog 2 (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Sonic The Hedgehog 2 (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Sonic The Hedgehog 2 (World).7z',
        'size': 190773,
    },
    {
        'title': 'Star Trek: The Next Generation: Advanced Holodeck Tutorial',
        'filename': 'Star Trek - The Next Generation - The Advanced Holodeck Tutorial (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Star Trek - The Next Generation - The Advanced Holodeck Tutorial (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Star Trek - The Next Generation - The Advanced Holodeck Tutorial (USA).7z',
        'size': 147925,
    },
    {
        'title': 'Star Trek: Generations: Beyond the Nexus',
        'filename': 'Star Trek Generations - Beyond the Nexus (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Star Trek Generations - Beyond the Nexus (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Star Trek Generations - Beyond the Nexus (USA).7z',
        'size': 134840,
    },
    {
        'title': 'Star Wars',
        'filename': 'Star Wars (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Star Wars (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Star Wars (USA, Europe).7z',
        'size': 241223,
    },
    {
        'title': 'Stargate',
        'filename': 'Stargate (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Stargate (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Stargate (World).7z',
        'size': 120496,
    },
    {
        'title': 'Street Fighter II',
        'filename': 'Street Battle (USA) (Proto) (Unl).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Street Battle (USA) (Proto) (Unl).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Street Battle (USA) (Proto) (Unl).7z',
        'size': 87499,
    },
    {
        'title': 'Bare Knuckle ~ Streets of Rage',
        'filename': 'Streets of Rage (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Streets of Rage (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Streets of Rage (World).7z',
        'size': 128469,
    },
    {
        'title': 'Bare Knuckle II: Streets of Rage 2: Streets of Rage II',
        'filename': 'Streets of Rage 2 (World).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Streets of Rage 2 (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Streets of Rage 2 (World).7z',
        'size': 223843,
    },
    {
        'title': 'Super Columns',
        'filename': 'Super Columns (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Super Columns (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Super Columns (USA, Europe).7z',
        'size': 56821,
    },
    {
        'title': 'Super Star Wars: Return of the Jedi',
        'filename': 'Super Star Wars - Return of the Jedi (USA, Europe).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Super Star Wars - Return of the Jedi (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Super Star Wars - Return of the Jedi (USA, Europe).7z',
        'size': 309258,
    },
    {
        'title': 'Tails Adventure',
        'filename': 'Tails Adventure (World) (En,Ja).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Tails Adventure (World) (En,Ja).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Tails Adventure (World) (En,Ja).7z',
        'size': 209407,
    },
    {
        'title': 'TaleSpin',
        'filename': 'TaleSpin (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/TaleSpin (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/TaleSpin (USA, Europe, Brazil) (En).7z',
        'size': 126036,
    },
    {
        'title': 'Taz in Escape from Mars',
        'filename': 'Taz in Escape from Mars (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Taz in Escape from Mars (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Taz in Escape from Mars (USA, Europe, Brazil) (En).7z',
        'size': 267472,
    },
    {
        'title': 'Urban Strike',
        'filename': 'Urban Strike (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Urban Strike (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Urban Strike (USA).7z',
        'size': 266613,
    },
    {
        'title': 'Vampire: Master of Darkness',
        'filename': 'Vampire - Master of Darkness (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/Vampire - Master of Darkness (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Vampire - Master of Darkness (USA).7z',
        'size': 149344,
    },
    {
        'title': "Wonder Boy III: The Dragon's Trap",
        'filename': "Wonder Boy - The Dragon's Trap (Europe).7z",
        'source_relative': "Handhelds/Sega Game Gear [1990]/Wonder Boy - The Dragon's Trap (Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/Wonder Boy - The Dragon's Trap (Europe).7z",
        'size': 119993,
    },
    {
        'title': 'X-Men',
        'filename': 'X-Men (USA).7z',
        'source_relative': 'Handhelds/Sega Game Gear [1990]/X-Men (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gamegear/X-Men (USA).7z',
        'size': 230496,
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