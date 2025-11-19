#!/usr/bin/env python3
# Auto-generated migration script for Nintendo DS
# 110 games, 6.75 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo DS'
ESDE_FOLDER = 'nds'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Advance Wars: Days of Ruin',
        'filename': 'Advance Wars - Days of Ruin (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Advance Wars - Days of Ruin (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Advance Wars - Days of Ruin (USA) (En,Fr,Es).zip',
        'size': 43581889,
    },
    {
        'title': 'Advance Wars: Dual Strike',
        'filename': 'Advance Wars - Dual Strike (USA, Australia).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Advance Wars - Dual Strike (USA, Australia).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Advance Wars - Dual Strike (USA, Australia).zip',
        'size': 20719015,
    },
    {
        'title': 'Animal Crossing: Wild World',
        'filename': 'Animal Crossing - Wild World (USA) (Rev 1).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Animal Crossing - Wild World (USA) (Rev 1).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Animal Crossing - Wild World (USA) (Rev 1).zip',
        'size': 21658767,
    },
    {
        'title': "Assassin's Creed: Altaïr's Chronicles",
        'filename': "Assassin's Creed - Altair's Chronicles (USA) (En,Fr,Es).zip",
        'source_relative': "Handhelds/Nintendo DS [2004]/Assassin's Creed - Altair's Chronicles (USA) (En,Fr,Es).zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Assassin's Creed - Altair's Chronicles (USA) (En,Fr,Es).zip",
        'size': 40211087,
    },
    {
        'title': "Assassin's Creed II: Discovery",
        'filename': "Assassin's Creed II - Discovery (USA) (En,Fr,Es) (NDSi Enhanced).zip",
        'source_relative': "Handhelds/Nintendo DS [2004]/Assassin's Creed II - Discovery (USA) (En,Fr,Es) (NDSi Enhanced).zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Assassin's Creed II - Discovery (USA) (En,Fr,Es) (NDSi Enhanced).zip",
        'size': 48832721,
    },
    {
        'title': 'Batman: The Brave and the Bold: The Videogame',
        'filename': 'Batman - The Brave and the Bold - The Videogame (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Batman - The Brave and the Bold - The Videogame (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Batman - The Brave and the Bold - The Videogame (USA) (En,Fr,Es).zip',
        'size': 19463491,
    },
    {
        'title': 'Call of Duty: Black Ops',
        'filename': 'Call of Duty - Black Ops (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Call of Duty - Black Ops (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Call of Duty - Black Ops (USA).zip',
        'size': 46117169,
    },
    {
        'title': 'Call of Duty: Modern Warfare: Mobilized',
        'filename': 'Call of Duty - Modern Warfare - Mobilized (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Call of Duty - Modern Warfare - Mobilized (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Call of Duty - Modern Warfare - Mobilized (USA).zip',
        'size': 44572863,
    },
    {
        'title': 'Call of Duty: Modern Warfare 3: Defiance',
        'filename': 'Call of Duty - Modern Warfare 3 - Defiance (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Call of Duty - Modern Warfare 3 - Defiance (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Call of Duty - Modern Warfare 3 - Defiance (USA).zip',
        'size': 46984715,
    },
    {
        'title': 'Call of Duty: World at War',
        'filename': 'Call of Duty - World at War (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Call of Duty - World at War (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Call of Duty - World at War (USA).zip',
        'size': 43402347,
    },
    {
        'title': 'Call of Duty 4: Modern Warfare',
        'filename': 'Call of Duty 4 - Modern Warfare (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Call of Duty 4 - Modern Warfare (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Call of Duty 4 - Modern Warfare (USA).zip',
        'size': 41671207,
    },
    {
        'title': 'Castlevania: Dawn of Sorrow',
        'filename': 'Castlevania - Dawn of Sorrow (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Castlevania - Dawn of Sorrow (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Castlevania - Dawn of Sorrow (USA).zip',
        'size': 24657183,
    },
    {
        'title': 'Castlevania: Order of Ecclesia',
        'filename': 'Castlevania - Order of Ecclesia (USA) (En,Fr).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Castlevania - Order of Ecclesia (USA) (En,Fr).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Castlevania - Order of Ecclesia (USA) (En,Fr).zip',
        'size': 30195190,
    },
    {
        'title': 'Castlevania: Portrait of Ruin',
        'filename': 'Castlevania - Portrait of Ruin (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Castlevania - Portrait of Ruin (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Castlevania - Portrait of Ruin (USA).zip',
        'size': 27629946,
    },
    {
        'title': 'Children of Mana',
        'filename': 'Children of Mana (USA, Australia).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Children of Mana (USA, Australia).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Children of Mana (USA, Australia).zip',
        'size': 44586562,
    },
    {
        'title': 'Chrono Trigger',
        'filename': 'Chrono Trigger (USA) (En,Fr).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Chrono Trigger (USA) (En,Fr).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Chrono Trigger (USA) (En,Fr).zip',
        'size': 63383269,
    },
    {
        'title': 'Contra 4',
        'filename': 'Contra 4 (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Contra 4 (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Contra 4 (USA).zip',
        'size': 16372976,
    },
    {
        'title': 'Diddy Kong Racing DS',
        'filename': 'Diddy Kong Racing DS (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Diddy Kong Racing DS (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Diddy Kong Racing DS (USA).zip',
        'size': 21921154,
    },
    {
        'title': 'Dragon Quest Heroes: Rocket Slime',
        'filename': 'Dragon Quest Heroes - Rocket Slime (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest Heroes - Rocket Slime (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest Heroes - Rocket Slime (USA).zip',
        'size': 23023185,
    },
    {
        'title': 'Dragon Quest IV: Chapters of the Chosen',
        'filename': 'Dragon Quest IV - Chapters of the Chosen (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest IV - Chapters of the Chosen (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest IV - Chapters of the Chosen (USA) (En,Fr,Es).zip',
        'size': 62922571,
    },
    {
        'title': 'Dragon Quest IX: Sentinels of the Starry Skies',
        'filename': 'Dragon Quest IX - Sentinels of the Starry Skies (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest IX - Sentinels of the Starry Skies (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest IX - Sentinels of the Starry Skies (USA) (En,Fr,Es).zip',
        'size': 182658269,
    },
    {
        'title': 'Dragon Quest Monsters: Joker',
        'filename': 'Dragon Quest Monsters - Joker (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest Monsters - Joker (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest Monsters - Joker (USA).zip',
        'size': 44969347,
    },
    {
        'title': 'Dragon Quest Monsters: Joker 2',
        'filename': 'Dragon Quest Monsters - Joker 2 (USA) (En,Fr,De,Es,It).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest Monsters - Joker 2 (USA) (En,Fr,De,Es,It).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest Monsters - Joker 2 (USA) (En,Fr,De,Es,It).zip',
        'size': 76117199,
    },
    {
        'title': 'Dragon Quest V: Hand of the Heavenly Bride',
        'filename': 'Dragon Quest V - Hand of the Heavenly Bride (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest V - Hand of the Heavenly Bride (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest V - Hand of the Heavenly Bride (USA) (En,Fr,Es).zip',
        'size': 79783343,
    },
    {
        'title': 'Dragon Quest VI: Realms of Revelation',
        'filename': 'Dragon Quest VI - Realms of Revelation (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Dragon Quest VI - Realms of Revelation (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Dragon Quest VI - Realms of Revelation (USA) (En,Fr,Es).zip',
        'size': 91298788,
    },
    {
        'title': 'Elite Beat Agents',
        'filename': 'Elite Beat Agents (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Elite Beat Agents (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Elite Beat Agents (USA).zip',
        'size': 110438262,
    },
    {
        'title': 'Final Fantasy: The 4 Heroes of Light',
        'filename': 'Final Fantasy - The 4 Heroes of Light (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy - The 4 Heroes of Light (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy - The 4 Heroes of Light (USA).zip',
        'size': 30700063,
    },
    {
        'title': 'Final Fantasy Crystal Chronicles: Echoes of Time',
        'filename': 'Final Fantasy Crystal Chronicles - Echoes of Time (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy Crystal Chronicles - Echoes of Time (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy Crystal Chronicles - Echoes of Time (USA) (En,Fr,Es).zip',
        'size': 96401234,
    },
    {
        'title': 'Final Fantasy Crystal Chronicles: Ring of Fates',
        'filename': 'Final Fantasy Crystal Chronicles - Ring of Fates (USA) (En,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy Crystal Chronicles - Ring of Fates (USA) (En,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy Crystal Chronicles - Ring of Fates (USA) (En,Es).zip',
        'size': 87295162,
    },
    {
        'title': 'Final Fantasy Fables: Chocobo Tales',
        'filename': 'Final Fantasy Fables - Chocobo Tales (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy Fables - Chocobo Tales (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy Fables - Chocobo Tales (USA).zip',
        'size': 45902660,
    },
    {
        'title': 'Final Fantasy III',
        'filename': 'Final Fantasy III (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy III (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy III (USA).zip',
        'size': 79024399,
    },
    {
        'title': 'Final Fantasy IV',
        'filename': 'Final Fantasy IV (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy IV (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy IV (USA) (En,Fr,Es).zip',
        'size': 105409081,
    },
    {
        'title': 'Final Fantasy Tactics A2: Grimoire of the Rift',
        'filename': 'Final Fantasy Tactics A2 - Grimoire of the Rift (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy Tactics A2 - Grimoire of the Rift (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy Tactics A2 - Grimoire of the Rift (USA) (En,Fr,Es).zip',
        'size': 72104067,
    },
    {
        'title': 'Final Fantasy XII: Revenant Wings',
        'filename': 'Final Fantasy XII - Revenant Wings (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Final Fantasy XII - Revenant Wings (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Final Fantasy XII - Revenant Wings (USA).zip',
        'size': 59662914,
    },
    {
        'title': 'Ghost Trick: Phantom Detective',
        'filename': 'Ghost Trick - Phantom Detective (USA) (En,Fr,De,Es,It).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Ghost Trick - Phantom Detective (USA) (En,Fr,De,Es,It).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Ghost Trick - Phantom Detective (USA) (En,Fr,De,Es,It).zip',
        'size': 86459654,
    },
    {
        'title': 'GhostBusters: The Video Game',
        'filename': 'Ghostbusters - The Video Game (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Ghostbusters - The Video Game (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Ghostbusters - The Video Game (USA) (En,Fr,Es).zip',
        'size': 34829661,
    },
    {
        'title': 'Grand Theft Auto: Chinatown Wars',
        'filename': 'Grand Theft Auto - Chinatown Wars.nds',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Grand Theft Auto - Chinatown Wars.nds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Grand Theft Auto - Chinatown Wars.nds',
        'size': 134217728,
    },
    {
        'title': 'Harry Potter and the Deathly Hallows: Part 1',
        'filename': 'Harry Potter and the Deathly Hallows - Part 1 (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Harry Potter and the Deathly Hallows - Part 1 (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Harry Potter and the Deathly Hallows - Part 1 (USA) (En,Fr,Es).zip',
        'size': 27054832,
    },
    {
        'title': 'Harry Potter and the Deathly Hallows: Part 2',
        'filename': 'Harry Potter and the Deathly Hallows - Part 2 (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Harry Potter and the Deathly Hallows - Part 2 (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Harry Potter and the Deathly Hallows - Part 2 (USA) (En,Fr,Es).zip',
        'size': 28853550,
    },
    {
        'title': 'Harry Potter and the Goblet of Fire',
        'filename': 'Harry Potter and the Goblet of Fire (USA) (En,Fr,De,Es,It).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Harry Potter and the Goblet of Fire (USA) (En,Fr,De,Es,It).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Harry Potter and the Goblet of Fire (USA) (En,Fr,De,Es,It).zip',
        'size': 38181097,
    },
    {
        'title': 'Harry Potter and the Half-Blood Prince',
        'filename': 'Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).zip',
        'size': 57792426,
    },
    {
        'title': 'Harry Potter and the Order of the Phoenix',
        'filename': 'Harry Potter and the Order of the Phoenix (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Harry Potter and the Order of the Phoenix (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Harry Potter and the Order of the Phoenix (USA).zip',
        'size': 48438749,
    },
    {
        'title': 'Heroes of Mana',
        'filename': 'Heroes of Mana (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Heroes of Mana (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Heroes of Mana (USA).zip',
        'size': 58738673,
    },
    {
        'title': 'Hotel Dusk: Room 215',
        'filename': 'Hotel Dusk - Room 215 (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Hotel Dusk - Room 215 (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Hotel Dusk - Room 215 (USA).zip',
        'size': 83461712,
    },
    {
        'title': 'Kingdom Hearts 358/2 Days',
        'filename': 'Kingdom Hearts - 358-2 Days (USA) (En,Fr).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Kingdom Hearts - 358-2 Days (USA) (En,Fr).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Kingdom Hearts - 358-2 Days (USA) (En,Fr).zip',
        'size': 226229397,
    },
    {
        'title': 'Kingdom Hearts Re:coded',
        'filename': 'Kingdom Hearts - Re-coded (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Kingdom Hearts - Re-coded (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Kingdom Hearts - Re-coded (USA) (En,Fr,Es).zip',
        'size': 209038893,
    },
    {
        'title': 'Kirby: Canvas Curse',
        'filename': 'Kirby - Canvas Curse (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Kirby - Canvas Curse (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Kirby - Canvas Curse (USA).zip',
        'size': 26902706,
    },
    {
        'title': 'Kirby: Squeak Squad',
        'filename': 'Kirby - Squeak Squad (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Kirby - Squeak Squad (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Kirby - Squeak Squad (USA).zip',
        'size': 14044126,
    },
    {
        'title': 'Kirby Mass Attack',
        'filename': 'Kirby Mass Attack (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Kirby Mass Attack (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Kirby Mass Attack (USA) (En,Fr,Es).zip',
        'size': 21794003,
    },
    {
        'title': 'Kirby Super Star Ultra',
        'filename': 'Kirby Super Star Ultra (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Kirby Super Star Ultra (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Kirby Super Star Ultra (USA).zip',
        'size': 63318913,
    },
    {
        'title': 'The Legend of Zelda: Phantom Hourglass',
        'filename': 'Legend of Zelda, The - Phantom Hourglass (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Legend of Zelda, The - Phantom Hourglass (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Legend of Zelda, The - Phantom Hourglass (USA) (En,Fr,Es).zip',
        'size': 48211868,
    },
    {
        'title': 'The Legend of Zelda: Spirit Tracks',
        'filename': 'Legend of Zelda, The - Spirit Tracks (USA, Australia) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Legend of Zelda, The - Spirit Tracks (USA, Australia) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Legend of Zelda, The - Spirit Tracks (USA, Australia) (En,Fr,Es).zip',
        'size': 69575212,
    },
    {
        'title': 'LEGO Batman: The Videogame',
        'filename': 'LEGO Batman - The Videogame (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Batman - The Videogame (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Batman - The Videogame (USA) (En,Fr,Es).zip',
        'size': 50879480,
    },
    {
        'title': 'LEGO Batman 2: DC Super Heroes',
        'filename': 'LEGO Batman 2 - DC Super Heroes (USA) (En,Fr,Es,Pt).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Batman 2 - DC Super Heroes (USA) (En,Fr,Es,Pt).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Batman 2 - DC Super Heroes (USA) (En,Fr,Es,Pt).zip',
        'size': 102085103,
    },
    {
        'title': 'LEGO Battles',
        'filename': 'LEGO Battles (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Battles (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Battles (USA) (En,Fr,Es).zip',
        'size': 95248154,
    },
    {
        'title': 'LEGO Battles: Ninjago',
        'filename': 'LEGO Battles - Ninjago (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Battles - Ninjago (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Battles - Ninjago (USA) (En,Fr,Es).zip',
        'size': 72610107,
    },
    {
        'title': 'LEGO Friends',
        'filename': 'LEGO Friends (USA) (En,Fr,Es,Pt).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Friends (USA) (En,Fr,Es,Pt).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Friends (USA) (En,Fr,Es,Pt).zip',
        'size': 111575031,
    },
    {
        'title': 'LEGO Harry Potter: Years 1-4',
        'filename': 'LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es).zip',
        'size': 121577768,
    },
    {
        'title': 'LEGO Harry Potter: Years 5-7',
        'filename': 'LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es).zip',
        'size': 111375345,
    },
    {
        'title': 'LEGO Indiana Jones: The Original Adventures',
        'filename': 'LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,De,Es,It,Da).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,De,Es,It,Da).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,De,Es,It,Da).zip',
        'size': 55347266,
    },
    {
        'title': 'LEGO Indiana Jones 2: The Adventure Continues',
        'filename': 'LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es).zip',
        'size': 54042526,
    },
    {
        'title': "LEGO Legends of Chima: Laval's Journey",
        'filename': "LEGO Legends of Chima - Laval's Journey (USA) (En,Fr,Es,Pt).zip",
        'source_relative': "Handhelds/Nintendo DS [2004]/LEGO Legends of Chima - Laval's Journey (USA) (En,Fr,Es,Pt).zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Legends of Chima - Laval's Journey (USA) (En,Fr,Es,Pt).zip",
        'size': 99112933,
    },
    {
        'title': 'LEGO Marvel Super Heroes: Universe in Peril',
        'filename': 'LEGO Marvel Super Heroes - Universe in Peril (USA) (En,Fr,Es,Pt).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Marvel Super Heroes - Universe in Peril (USA) (En,Fr,Es,Pt).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Marvel Super Heroes - Universe in Peril (USA) (En,Fr,Es,Pt).zip',
        'size': 117821761,
    },
    {
        'title': 'LEGO Pirates of the Caribbean: The Video Game',
        'filename': 'LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es).zip',
        'size': 111261671,
    },
    {
        'title': 'LEGO Rock Band',
        'filename': 'LEGO Rock Band (USA) (En,Fr,De,Es,It,Da).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Rock Band (USA) (En,Fr,De,Es,It,Da).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Rock Band (USA) (En,Fr,De,Es,It,Da).zip',
        'size': 204881691,
    },
    {
        'title': 'LEGO Star Wars: The Complete Saga',
        'filename': 'LEGO Star Wars - The Complete Saga (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Star Wars - The Complete Saga (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Star Wars - The Complete Saga (USA).zip',
        'size': 55087251,
    },
    {
        'title': 'LEGO Star Wars II: The Original Trilogy',
        'filename': 'LEGO Star Wars II - The Original Trilogy (USA) (Rev 1).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Star Wars II - The Original Trilogy (USA) (Rev 1).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Star Wars II - The Original Trilogy (USA) (Rev 1).zip',
        'size': 22987411,
    },
    {
        'title': 'LEGO Star Wars II: The Original Trilogy',
        'filename': 'LEGO Star Wars II - The Original Trilogy (USA) (Rev 1).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Star Wars II - The Original Trilogy (USA) (Rev 1).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Star Wars II - The Original Trilogy (USA) (Rev 1).zip',
        'size': 22074649,
    },
    {
        'title': 'LEGO Star Wars III: The Clone Wars',
        'filename': 'LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es).zip',
        'size': 114485217,
    },
    {
        'title': 'LEGO The Lord of the Rings',
        'filename': 'LEGO The Lord of the Rings (USA) (En,Fr,Es,Pt).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/LEGO The Lord of the Rings (USA) (En,Fr,Es,Pt).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/LEGO The Lord of the Rings (USA) (En,Fr,Es,Pt).zip',
        'size': 118848004,
    },
    {
        'title': "Mario & Luigi: Bowser's Inside Story",
        'filename': "Mario & Luigi - Bowser's Inside Story (USA) (En,Fr,Es).zip",
        'source_relative': "Handhelds/Nintendo DS [2004]/Mario & Luigi - Bowser's Inside Story (USA) (En,Fr,Es).zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mario & Luigi - Bowser's Inside Story (USA) (En,Fr,Es).zip",
        'size': 65135432,
    },
    {
        'title': 'Mario & Luigi: Partners in Time',
        'filename': 'Mario & Luigi - Partners in Time (USA) (Rev 1).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Mario & Luigi - Partners in Time (USA) (Rev 1).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mario & Luigi - Partners in Time (USA) (Rev 1).zip',
        'size': 41579780,
    },
    {
        'title': 'Mario & Luigi: Partners in Time',
        'filename': 'Mario & Luigi - Partners in Time (USA) (Rev 1).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Mario & Luigi - Partners in Time (USA) (Rev 1).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mario & Luigi - Partners in Time (USA) (Rev 1).zip',
        'size': 39492981,
    },
    {
        'title': 'Mario Kart DS',
        'filename': 'Mario Kart DS (USA) (En,Fr,De,Es,It).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Mario Kart DS (USA) (En,Fr,De,Es,It).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mario Kart DS (USA) (En,Fr,De,Es,It).zip',
        'size': 19241384,
    },
    {
        'title': 'Mario vs. Donkey Kong: Mini-Land Mayhem!',
        'filename': 'Mario vs. Donkey Kong - Mini-Land Mayhem! (USA) (En,Fr,Es) (Rev 1) (NDSi Enhanced).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Mario vs. Donkey Kong - Mini-Land Mayhem! (USA) (En,Fr,Es) (Rev 1) (NDSi Enhanced).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mario vs. Donkey Kong - Mini-Land Mayhem! (USA) (En,Fr,Es) (Rev 1) (NDSi Enhanced).zip',
        'size': 16511230,
    },
    {
        'title': 'Mario vs. Donkey Kong 2: March of the Minis',
        'filename': 'Mario vs. Donkey Kong 2 - March of the Minis (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Mario vs. Donkey Kong 2 - March of the Minis (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mario vs. Donkey Kong 2 - March of the Minis (USA).zip',
        'size': 20518398,
    },
    {
        'title': 'Mega Man Zero Collection',
        'filename': 'Mega Man Zero Collection (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Mega Man Zero Collection (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Mega Man Zero Collection (USA).zip',
        'size': 43495602,
    },
    {
        'title': 'Meteos',
        'filename': 'Meteos (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Meteos (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Meteos (USA).zip',
        'size': 43001548,
    },
    {
        'title': 'New Super Mario Bros.',
        'filename': 'New Super Mario Bros. (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/New Super Mario Bros. (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/New Super Mario Bros. (USA).zip',
        'size': 14457733,
    },
    {
        'title': 'Nine Hours, Nine Persons, Nine Doors',
        'filename': 'Nine Hours, Nine Persons, Nine Doors (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Nine Hours, Nine Persons, Nine Doors (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Nine Hours, Nine Persons, Nine Doors (USA).zip',
        'size': 106145550,
    },
    {
        'title': 'Phoenix Wright: Ace Attorney',
        'filename': 'Phoenix Wright - Ace Attorney (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Phoenix Wright - Ace Attorney (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Phoenix Wright - Ace Attorney (USA).zip',
        'size': 38626141,
    },
    {
        'title': 'Phoenix Wright: Ace Attorney: Justice for All',
        'filename': 'Phoenix Wright - Ace Attorney - Justice for All (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Phoenix Wright - Ace Attorney - Justice for All (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Phoenix Wright - Ace Attorney - Justice for All (USA).zip',
        'size': 13266710,
    },
    {
        'title': 'Phoenix Wright: Ace Attorney: Trials and Tribulations',
        'filename': 'Phoenix Wright - Ace Attorney - Trials and Tribulations (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Phoenix Wright - Ace Attorney - Trials and Tribulations (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Phoenix Wright - Ace Attorney - Trials and Tribulations (USA).zip',
        'size': 13624022,
    },
    {
        'title': 'Picross 3D',
        'filename': 'Picross 3D (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Picross 3D (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Picross 3D (USA) (En,Fr,Es).zip',
        'size': 25045082,
    },
    {
        'title': 'Picross DS',
        'filename': 'Picross DS (USA) (En,Fr,Es).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Picross DS (USA) (En,Fr,Es).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Picross DS (USA) (En,Fr,Es).zip',
        'size': 7789652,
    },
    {
        'title': 'Plants vs. Zombies',
        'filename': 'Plants vs. Zombies (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Plants vs. Zombies (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Plants vs. Zombies (USA).zip',
        'size': 25169183,
    },
    {
        'title': 'Pokemon: Black Version',
        'filename': 'Pokemon - Black Version (USA, Europe) (NDSi Enhanced).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - Black Version (USA, Europe) (NDSi Enhanced).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - Black Version (USA, Europe) (NDSi Enhanced).zip',
        'size': 110705538,
    },
    {
        'title': 'Pokemon: Black Version 2',
        'filename': 'Pokemon - Black Version 2 (USA, Europe) (NDSi Enhanced).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - Black Version 2 (USA, Europe) (NDSi Enhanced).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - Black Version 2 (USA, Europe) (NDSi Enhanced).zip',
        'size': 154068254,
    },
    {
        'title': 'Pokémon HeartGold Version',
        'filename': 'Pokemon - HeartGold Version (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - HeartGold Version (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - HeartGold Version (USA).zip',
        'size': 60677682,
    },
    {
        'title': 'Pokémon Platinum Version',
        'filename': 'Pokemon - Platinum Version (USA) (Rev 1).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - Platinum Version (USA) (Rev 1).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - Platinum Version (USA) (Rev 1).zip',
        'size': 50714177,
    },
    {
        'title': 'Pokémon SoulSilver Version',
        'filename': 'Pokemon - SoulSilver Version (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - SoulSilver Version (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - SoulSilver Version (USA).zip',
        'size': 60677718,
    },
    {
        'title': 'Pokemon: White Version',
        'filename': 'Pokemon - White Version (USA, Europe) (NDSi Enhanced).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - White Version (USA, Europe) (NDSi Enhanced).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - White Version (USA, Europe) (NDSi Enhanced).zip',
        'size': 110705517,
    },
    {
        'title': 'Pokémon White Version 2',
        'filename': 'Pokemon - White Version 2 (USA, Europe) (NDSi Enhanced).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon - White Version 2 (USA, Europe) (NDSi Enhanced).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon - White Version 2 (USA, Europe) (NDSi Enhanced).zip',
        'size': 153759810,
    },
    {
        'title': 'Pokemon Conquest',
        'filename': 'Pokemon Conquest (USA, Australia) (NDSi Enhanced).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon Conquest (USA, Australia) (NDSi Enhanced).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon Conquest (USA, Australia) (NDSi Enhanced).zip',
        'size': 75300957,
    },
    {
        'title': 'Pokémon Mystery Dungeon: Explorers of Darkness',
        'filename': 'Pokemon Mystery Dungeon - Explorers of Darkness (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon Mystery Dungeon - Explorers of Darkness (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon Mystery Dungeon - Explorers of Darkness (USA).zip',
        'size': 31687975,
    },
    {
        'title': 'Pokemon Mystery Dungeon: Explorers of Sky',
        'filename': 'Pokemon Mystery Dungeon - Explorers of Sky (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon Mystery Dungeon - Explorers of Sky (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon Mystery Dungeon - Explorers of Sky (USA).zip',
        'size': 46297044,
    },
    {
        'title': 'Pokémon Mystery Dungeon: Explorers of Time',
        'filename': 'Pokemon Mystery Dungeon - Explorers of Time (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Pokemon Mystery Dungeon - Explorers of Time (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Pokemon Mystery Dungeon - Explorers of Time (USA).zip',
        'size': 31687785,
    },
    {
        'title': 'Professor Layton and the Curious Village',
        'filename': 'Professor Layton and the Curious Village (USA, Australia).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Professor Layton and the Curious Village (USA, Australia).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Professor Layton and the Curious Village (USA, Australia).zip',
        'size': 53330146,
    },
    {
        'title': 'Professor Layton and the Diabolical Box',
        'filename': 'Professor Layton and the Diabolical Box (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Professor Layton and the Diabolical Box (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Professor Layton and the Diabolical Box (USA).zip',
        'size': 98262938,
    },
    {
        'title': 'Professor Layton and the Last Specter',
        'filename': 'Professor Layton and the Last Specter (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Professor Layton and the Last Specter (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Professor Layton and the Last Specter (USA).zip',
        'size': 216585314,
    },
    {
        'title': 'Professor Layton and the Unwound Future',
        'filename': 'Professor Layton and the Unwound Future (USA) (Video).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Professor Layton and the Unwound Future (USA) (Video).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Professor Layton and the Unwound Future (USA) (Video).zip',
        'size': 8502963,
    },
    {
        'title': 'Professor Layton and the Unwound Future',
        'filename': 'Professor Layton and the Unwound Future (USA) (Video).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Professor Layton and the Unwound Future (USA) (Video).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Professor Layton and the Unwound Future (USA) (Video).zip',
        'size': 217790029,
    },
    {
        'title': 'Radiant Historia',
        'filename': 'Radiant Historia (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Radiant Historia (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Radiant Historia (USA).zip',
        'size': 55204174,
    },
    {
        'title': 'Rhythm Heaven',
        'filename': 'Rhythm Heaven (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Rhythm Heaven (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Rhythm Heaven (USA).zip',
        'size': 108511080,
    },
    {
        'title': 'Shin Megami Tensei: Strange Journey',
        'filename': 'Shin Megami Tensei - Strange Journey (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Shin Megami Tensei - Strange Journey (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Shin Megami Tensei - Strange Journey (USA).zip',
        'size': 104851423,
    },
    {
        'title': "Sid Meier's Civilization Revolution",
        'filename': "Sid Meier's Civilization Revolution (USA) (En,Fr,De,Es,It).zip",
        'source_relative': "Handhelds/Nintendo DS [2004]/Sid Meier's Civilization Revolution (USA) (En,Fr,De,Es,It).zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Sid Meier's Civilization Revolution (USA) (En,Fr,De,Es,It).zip",
        'size': 26047075,
    },
    {
        'title': 'Tetris DS',
        'filename': 'Tetris DS (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Tetris DS (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Tetris DS (USA).zip',
        'size': 6968406,
    },
    {
        'title': 'Wario: Master of Disguise',
        'filename': 'Wario - Master of Disguise (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/Wario - Master of Disguise (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/Wario - Master of Disguise (USA).zip',
        'size': 37409399,
    },
    {
        'title': 'WarioWare: D.I.Y.',
        'filename': 'WarioWare - D.I.Y. (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/WarioWare - D.I.Y. (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/WarioWare - D.I.Y. (USA).zip',
        'size': 9052725,
    },
    {
        'title': 'The World Ends with You',
        'filename': 'World Ends with You, The (USA).zip',
        'source_relative': 'Handhelds/Nintendo DS [2004]/World Ends with You, The (USA).zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/nds/World Ends with You, The (USA).zip',
        'size': 75907415,
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