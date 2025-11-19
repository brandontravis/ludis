#!/usr/bin/env python3
# Auto-generated migration script for Nintendo Wii
# 89 games, 277.48 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo Wii'
ESDE_FOLDER = 'wii'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Bomberman Land',
        'filename': 'Bomberman Land (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Bomberman Land (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Bomberman Land (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'A Boy and His Blob',
        'filename': 'Boy and His Blob, A (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Boy and His Blob, A (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Boy and His Blob, A (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'Donkey Kong Country Returns',
        'filename': 'Donkey Kong Country Returns (USA) (En,Fr,Es) (v1.01).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Donkey Kong Country Returns (USA) (En,Fr,Es) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Donkey Kong Country Returns (USA) (En,Fr,Es) (v1.01).iso',
        'size': 4699979776,
    },
    {
        'title': 'Harvest Moon: Animal Parade',
        'filename': 'Harvest Moon - Animal Parade (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Harvest Moon - Animal Parade (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harvest Moon - Animal Parade (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'Harvest Moon: Tree of Tranquility',
        'filename': 'Harvest Moon - Tree of Tranquility (USA) (v1.01).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Harvest Moon - Tree of Tranquility (USA) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harvest Moon - Tree of Tranquility (USA) (v1.01).iso',
        'size': 4699979776,
    },
    {
        'title': "Kirby's Dream Collection: Special Edition",
        'filename': "Kirby's Dream Collection - Special Edition (USA).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Kirby's Dream Collection - Special Edition (USA).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Kirby's Dream Collection - Special Edition (USA).iso",
        'size': 4699979776,
    },
    {
        'title': "Kirby's Epic Yarn",
        'filename': "Kirby's Epic Yarn (USA) (En,Fr,Es).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Kirby's Epic Yarn (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Kirby's Epic Yarn (USA) (En,Fr,Es).iso",
        'size': 4699979776,
    },
    {
        'title': "Kirby's Return to Dream Land",
        'filename': "Kirby's Return to Dream Land (USA) (En,Fr,Es).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Kirby's Return to Dream Land (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Kirby's Return to Dream Land (USA) (En,Fr,Es).iso",
        'size': 4699979776,
    },
    {
        'title': 'Lara Croft: Tomb Raider: Anniversary',
        'filename': 'Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'The Legend of Spyro: Dawn of the Dragon',
        'filename': 'Legend of Spyro, The - Dawn of the Dragon (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Legend of Spyro, The - Dawn of the Dragon (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Legend of Spyro, The - Dawn of the Dragon (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'The Legend of Spyro: The Eternal Night',
        'filename': 'Legend of Spyro, The - The Eternal Night (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Legend of Spyro, The - The Eternal Night (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Legend of Spyro, The - The Eternal Night (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'The Legend of Zelda: Skyward Sword',
        'filename': 'Legend of Zelda, The - Skyward Sword (USA) (En,Fr,Es) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Legend of Zelda, The - Skyward Sword (USA) (En,Fr,Es) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Legend of Zelda, The - Skyward Sword (USA) (En,Fr,Es) (v1.02).iso',
        'size': 4699979776,
    },
    {
        'title': 'The Legend of Zelda: Twilight Princess',
        'filename': 'Legend of Zelda, The - Twilight Princess (USA) (En,Fr,Es) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Legend of Zelda, The - Twilight Princess (USA) (En,Fr,Es) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Legend of Zelda, The - Twilight Princess (USA) (En,Fr,Es) (v1.02).iso',
        'size': 4699979776,
    },
    {
        'title': "Little King's Story",
        'filename': "Little King's Story (USA) (En,Fr,Es).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Little King's Story (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Little King's Story (USA) (En,Fr,Es).iso",
        'size': 4699979776,
    },
    {
        'title': 'Mario Kart Wii',
        'filename': 'Mario Kart Wii (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Mario Kart Wii (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Mario Kart Wii (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'Mario Party 8',
        'filename': 'Mario Party 8 (USA) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Mario Party 8 (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Mario Party 8 (USA) (v1.02).iso',
        'size': 4699979776,
    },
    {
        'title': 'Mario Party 9',
        'filename': 'Mario Party 9 (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Mario Party 9 (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Mario Party 9 (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'Metroid: Other M',
        'filename': 'Metroid - Other M (USA) (En,Fr,Es) (v1.01).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Metroid - Other M (USA) (En,Fr,Es) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Metroid - Other M (USA) (En,Fr,Es) (v1.01).iso',
        'size': 8511160320,
    },
    {
        'title': 'Metroid Prime 3: Corruption',
        'filename': 'Metroid Prime 3 - Corruption (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Metroid Prime 3 - Corruption (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Metroid Prime 3 - Corruption (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'Metroid Prime Trilogy',
        'filename': 'Metroid Prime Trilogy (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Metroid Prime Trilogy (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Metroid Prime Trilogy (USA).iso',
        'size': 8511160320,
    },
    {
        'title': 'New Super Mario Bros. Wii',
        'filename': 'New Super Mario Bros. Wii (USA) (En,Fr,Es) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/New Super Mario Bros. Wii (USA) (En,Fr,Es) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/New Super Mario Bros. Wii (USA) (En,Fr,Es) (v1.02).iso',
        'size': 4699979776,
    },
    {
        'title': 'Punch-Out!!',
        'filename': 'Punch-Out!! (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Punch-Out!! (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Punch-Out!! (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'Batman: The Brave and the Bold: The Videogame',
        'filename': 'Batman - The Brave and the Bold - The Videogame (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Batman - The Brave and the Bold - The Videogame (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Batman - The Brave and the Bold - The Videogame (USA) (En,Fr,Es).rvz',
        'size': 2297720576,
    },
    {
        'title': 'Bomberman Land',
        'filename': 'Bomberman Land (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Bomberman Land (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Bomberman Land (USA).iso',
        'size': 508616820,
    },
    {
        'title': 'A Boy and His Blob',
        'filename': 'Boy and His Blob, A (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Boy and His Blob, A (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Boy and His Blob, A (USA).iso',
        'size': 995154796,
    },
    {
        'title': 'Call of Duty: Black Ops',
        'filename': 'Call of Duty - Black Ops (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Call of Duty - Black Ops (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Call of Duty - Black Ops (USA).rvz',
        'size': 3888326056,
    },
    {
        'title': 'Call of Duty: Modern Warfare: Reflex Edition',
        'filename': 'Call of Duty - Modern Warfare - Reflex (USA) (En,Fr).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Call of Duty - Modern Warfare - Reflex (USA) (En,Fr).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Call of Duty - Modern Warfare - Reflex (USA) (En,Fr).rvz',
        'size': 3746268948,
    },
    {
        'title': 'Call of Duty: Modern Warfare 3',
        'filename': 'Call of Duty - Modern Warfare 3 (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Call of Duty - Modern Warfare 3 (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Call of Duty - Modern Warfare 3 (USA).rvz',
        'size': 3756472392,
    },
    {
        'title': 'Call of Duty: World at War',
        'filename': 'Call of Duty - World at War (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Call of Duty - World at War (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Call of Duty - World at War (USA).rvz',
        'size': 2502448012,
    },
    {
        'title': 'Call of Duty 3',
        'filename': 'Call of Duty 3 (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Call of Duty 3 (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Call of Duty 3 (USA).rvz',
        'size': 2883737280,
    },
    {
        'title': 'Castlevania Judgment',
        'filename': 'Castlevania Judgment (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Castlevania Judgment (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Castlevania Judgment (USA).rvz',
        'size': 1626183868,
    },
    {
        'title': 'Donkey Kong: Barrel Blast',
        'filename': 'Donkey Kong - Barrel Blast (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Donkey Kong - Barrel Blast (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Donkey Kong - Barrel Blast (USA).rvz',
        'size': 487124516,
    },
    {
        'title': 'Donkey Kong Country Returns',
        'filename': 'Donkey Kong Country Returns (USA) (En,Fr,Es) (v1.01).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Donkey Kong Country Returns (USA) (En,Fr,Es) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Donkey Kong Country Returns (USA) (En,Fr,Es) (v1.01).iso',
        'size': 3492868500,
    },
    {
        'title': 'Donkey Kong: Jungle Beat',
        'filename': 'Donkey Kong Jungle Beat (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Donkey Kong Jungle Beat (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Donkey Kong Jungle Beat (USA) (En,Fr,Es).rvz',
        'size': 825689368,
    },
    {
        'title': 'Dragon Quest Swords: The Masked Queen and the Tower of Mirrors',
        'filename': 'Dragon Quest Swords - The Masked Queen and the Tower of Mirrors (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Dragon Quest Swords - The Masked Queen and the Tower of Mirrors (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Dragon Quest Swords - The Masked Queen and the Tower of Mirrors (USA).rvz',
        'size': 2455812528,
    },
    {
        'title': 'Final Fantasy Crystal Chronicles: Echoes of Time',
        'filename': 'Final Fantasy Crystal Chronicles - Echoes of Time (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Final Fantasy Crystal Chronicles - Echoes of Time (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Final Fantasy Crystal Chronicles - Echoes of Time (USA) (En,Fr,Es).rvz',
        'size': 2579790052,
    },
    {
        'title': 'Final Fantasy Crystal Chronicles: The Crystal Bearers',
        'filename': 'Final Fantasy Crystal Chronicles - The Crystal Bearers (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Final Fantasy Crystal Chronicles - The Crystal Bearers (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Final Fantasy Crystal Chronicles - The Crystal Bearers (USA) (En,Fr,Es).rvz',
        'size': 2573660532,
    },
    {
        'title': "Final Fantasy Fables: Chocobo's Dungeon",
        'filename': "Final Fantasy Fables - Chocobo's Dungeon (USA).rvz",
        'source_relative': "Consoles/Nintendo Wii [2006]/RVZ/Final Fantasy Fables - Chocobo's Dungeon (USA).rvz",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Final Fantasy Fables - Chocobo's Dungeon (USA).rvz",
        'size': 1428520488,
    },
    {
        'title': 'Ghostbusters: The Video Game',
        'filename': 'Ghostbusters - The Video Game (USA) (En,Fr,Es) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Ghostbusters - The Video Game (USA) (En,Fr,Es) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Ghostbusters - The Video Game (USA) (En,Fr,Es) (Rev 1).rvz',
        'size': 2677456280,
    },
    {
        'title': 'Harry Potter and the Deathly Hallows: Part 1',
        'filename': 'Harry Potter and the Deathly Hallows - Part 1 (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Harry Potter and the Deathly Hallows - Part 1 (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harry Potter and the Deathly Hallows - Part 1 (USA) (En,Fr,Es).rvz',
        'size': 2791371572,
    },
    {
        'title': 'Harry Potter and the Deathly Hallows: Part 2',
        'filename': 'Harry Potter and the Deathly Hallows - Part 2 (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Harry Potter and the Deathly Hallows - Part 2 (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harry Potter and the Deathly Hallows - Part 2 (USA) (En,Fr,Es).rvz',
        'size': 2888528092,
    },
    {
        'title': 'Harry Potter and the Half-Blood Prince',
        'filename': 'Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).rvz',
        'size': 2105554652,
    },
    {
        'title': 'Harry Potter and the Order of the Phoenix',
        'filename': 'Harry Potter and the Order of the Phoenix (USA).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/Harry Potter and the Order of the Phoenix (USA).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harry Potter and the Order of the Phoenix (USA).rvz',
        'size': 2115135856,
    },
    {
        'title': 'Harvest Moon: Animal Parade',
        'filename': 'Harvest Moon - Animal Parade (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Harvest Moon - Animal Parade (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harvest Moon - Animal Parade (USA).iso',
        'size': 1413395576,
    },
    {
        'title': 'Harvest Moon: Tree of Tranquility',
        'filename': 'Harvest Moon - Tree of Tranquility (USA) (v1.01).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Harvest Moon - Tree of Tranquility (USA) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Harvest Moon - Tree of Tranquility (USA) (v1.01).iso',
        'size': 838351880,
    },
    {
        'title': "Kirby's Dream Collection: Special Edition",
        'filename': "Kirby's Dream Collection - Special Edition (USA).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Kirby's Dream Collection - Special Edition (USA).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Kirby's Dream Collection - Special Edition (USA).iso",
        'size': 1919231676,
    },
    {
        'title': "Kirby's Epic Yarn",
        'filename': "Kirby's Epic Yarn (USA) (En,Fr,Es).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Kirby's Epic Yarn (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Kirby's Epic Yarn (USA) (En,Fr,Es).iso",
        'size': 1522450808,
    },
    {
        'title': "Kirby's Return to Dream Land",
        'filename': "Kirby's Return to Dream Land (USA) (En,Fr,Es).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Kirby's Return to Dream Land (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Kirby's Return to Dream Land (USA) (En,Fr,Es).iso",
        'size': 1308625404,
    },
    {
        'title': 'Lara Croft: Tomb Raider: Anniversary',
        'filename': 'Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,Es).iso',
        'size': 2532064584,
    },
    {
        'title': 'The Legend of Spyro: Dawn of the Dragon',
        'filename': 'Legend of Spyro, The - Dawn of the Dragon (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Legend of Spyro, The - Dawn of the Dragon (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Legend of Spyro, The - Dawn of the Dragon (USA) (En,Fr,Es).iso',
        'size': 3409179264,
    },
    {
        'title': 'The Legend of Spyro: The Eternal Night',
        'filename': 'Legend of Spyro, The - The Eternal Night (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Legend of Spyro, The - The Eternal Night (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Legend of Spyro, The - The Eternal Night (USA).iso',
        'size': 1999377084,
    },
    {
        'title': 'LEGO Batman: The Videogame',
        'filename': 'LEGO Batman - The Videogame (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Batman - The Videogame (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Batman - The Videogame (USA) (En,Fr,Es).rvz',
        'size': 1933882516,
    },
    {
        'title': 'LEGO Batman 2: DC Super Heroes',
        'filename': 'LEGO Batman 2 - DC Super Heroes (USA) (En,Fr,Es,Pt).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Batman 2 - DC Super Heroes (USA) (En,Fr,Es,Pt).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Batman 2 - DC Super Heroes (USA) (En,Fr,Es,Pt).rvz',
        'size': 1744308712,
    },
    {
        'title': 'LEGO Harry Potter: Years 1-4',
        'filename': 'LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es) (Rev 1).rvz',
        'size': 2310803688,
    },
    {
        'title': 'LEGO Harry Potter: Years 5-7',
        'filename': 'LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es,Pt) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es,Pt) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es,Pt) (Rev 1).rvz',
        'size': 2207148836,
    },
    {
        'title': 'LEGO Indiana Jones: The Original Adventures',
        'filename': 'LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,Es).rvz',
        'size': 1647475212,
    },
    {
        'title': 'LEGO Indiana Jones 2: The Adventure Continues',
        'filename': 'LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es) (Rev 1).rvz',
        'size': 3509977948,
    },
    {
        'title': 'LEGO Pirates of the Caribbean: The Video Game',
        'filename': 'LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es) (Rev 1).rvz',
        'size': 1491125428,
    },
    {
        'title': 'LEGO Rock Band',
        'filename': 'LEGO Rock Band (USA) (En,Fr,Es).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Rock Band (USA) (En,Fr,Es).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Rock Band (USA) (En,Fr,Es).rvz',
        'size': 3577113320,
    },
    {
        'title': 'LEGO Star Wars: The Complete Saga',
        'filename': 'LEGO Star Wars - The Complete Saga (USA) (En,Fr,Es) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Star Wars - The Complete Saga (USA) (En,Fr,Es) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Star Wars - The Complete Saga (USA) (En,Fr,Es) (Rev 1).rvz',
        'size': 2168363732,
    },
    {
        'title': 'LEGO Star Wars III: The Clone Wars',
        'filename': 'LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es) (Rev 1).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es) (Rev 1).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es) (Rev 1).rvz',
        'size': 1673358348,
    },
    {
        'title': 'LEGO The Lord of the Rings',
        'filename': 'LEGO The Lord of the Rings (USA) (En,Fr,Es,Pt).rvz',
        'source_relative': 'Consoles/Nintendo Wii [2006]/RVZ/LEGO The Lord of the Rings (USA) (En,Fr,Es,Pt).rvz',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/LEGO The Lord of the Rings (USA) (En,Fr,Es,Pt).rvz',
        'size': 2513450652,
    },
    {
        'title': "Little King's Story",
        'filename': "Little King's Story (USA) (En,Fr,Es).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Little King's Story (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Little King's Story (USA) (En,Fr,Es).iso",
        'size': 3175009404,
    },
    {
        'title': 'Mario Kart Wii',
        'filename': 'Mario Kart Wii (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Mario Kart Wii (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Mario Kart Wii (USA) (En,Fr,Es).iso',
        'size': 2785150188,
    },
    {
        'title': 'Mario Party 8',
        'filename': 'Mario Party 8 (USA) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Mario Party 8 (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Mario Party 8 (USA) (v1.02).iso',
        'size': 1341116460,
    },
    {
        'title': 'Mario Party 9',
        'filename': 'Mario Party 9 (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Mario Party 9 (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Mario Party 9 (USA) (En,Fr,Es).iso',
        'size': 937856696,
    },
    {
        'title': 'Metroid: Other M',
        'filename': 'Metroid - Other M (USA) (En,Fr,Es) (v1.01).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Metroid - Other M (USA) (En,Fr,Es) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Metroid - Other M (USA) (En,Fr,Es) (v1.01).iso',
        'size': 6261031232,
    },
    {
        'title': 'Metroid Prime 3: Corruption',
        'filename': 'Metroid Prime 3 - Corruption (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Metroid Prime 3 - Corruption (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Metroid Prime 3 - Corruption (USA).iso',
        'size': 4062965232,
    },
    {
        'title': 'Metroid Prime Trilogy',
        'filename': 'Metroid Prime Trilogy (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Metroid Prime Trilogy (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Metroid Prime Trilogy (USA).iso',
        'size': 7142274304,
    },
    {
        'title': 'New Super Mario Bros. Wii',
        'filename': 'New Super Mario Bros. Wii (USA) (En,Fr,Es) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/New Super Mario Bros. Wii (USA) (En,Fr,Es) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/New Super Mario Bros. Wii (USA) (En,Fr,Es) (v1.02).iso',
        'size': 439557680,
    },
    {
        'title': 'Punch-Out!!',
        'filename': 'Punch-Out!! (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Punch-Out!! (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Punch-Out!! (USA) (En,Fr,Es).iso',
        'size': 3171471820,
    },
    {
        'title': 'Super Mario All-Stars',
        'filename': 'Super Mario All-Stars (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Mario All-Stars (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Mario All-Stars (USA).iso',
        'size': 203470496,
    },
    {
        'title': 'Super Mario Galaxy',
        'filename': 'Super Mario Galaxy (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Mario Galaxy (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Mario Galaxy (USA) (En,Fr,Es).iso',
        'size': 3425535460,
    },
    {
        'title': 'Super Mario Galaxy 2',
        'filename': 'Super Mario Galaxy 2 (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Mario Galaxy 2 (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Mario Galaxy 2 (USA) (En,Fr,Es).iso',
        'size': 1438368956,
    },
    {
        'title': 'Super Monkey Ball: Banana Blitz',
        'filename': 'Super Monkey Ball - Banana Blitz (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Monkey Ball - Banana Blitz (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Monkey Ball - Banana Blitz (USA).iso',
        'size': 858626004,
    },
    {
        'title': 'Super Monkey Ball: Step & Roll',
        'filename': 'Super Monkey Ball - Step & Roll (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Monkey Ball - Step & Roll (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Monkey Ball - Step & Roll (USA).iso',
        'size': 811458516,
    },
    {
        'title': 'Super Paper Mario',
        'filename': 'Super Paper Mario (USA) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Paper Mario (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Paper Mario (USA) (v1.02).iso',
        'size': 406348928,
    },
    {
        'title': 'Super Smash Bros. Brawl',
        'filename': 'Super Smash Bros. Brawl (USA) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Smash Bros. Brawl (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Smash Bros. Brawl (USA) (v1.02).iso',
        'size': 5952572196,
    },
    {
        'title': 'Xenoblade Chronicles',
        'filename': 'Xenoblade Chronicles (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Xenoblade Chronicles (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Xenoblade Chronicles (USA) (En,Fr,Es).iso',
        'size': 5099165372,
    },
    {
        'title': "Zack & Wiki: Quest for Barbaros' Treasure",
        'filename': "Zack & Wiki - Quest for Barbaros' Treasure (USA).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Zack & Wiki - Quest for Barbaros' Treasure (USA).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Zack & Wiki - Quest for Barbaros' Treasure (USA).iso",
        'size': 1135656048,
    },
    {
        'title': 'Super Mario All-Stars',
        'filename': 'Super Mario All-Stars (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Mario All-Stars (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Mario All-Stars (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'Super Mario Galaxy',
        'filename': 'Super Mario Galaxy (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Mario Galaxy (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Mario Galaxy (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'Super Mario Galaxy 2',
        'filename': 'Super Mario Galaxy 2 (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Mario Galaxy 2 (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Mario Galaxy 2 (USA) (En,Fr,Es).iso',
        'size': 4699979776,
    },
    {
        'title': 'Super Monkey Ball: Banana Blitz',
        'filename': 'Super Monkey Ball - Banana Blitz (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Monkey Ball - Banana Blitz (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Monkey Ball - Banana Blitz (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'Super Monkey Ball: Step & Roll',
        'filename': 'Super Monkey Ball - Step & Roll (USA).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Monkey Ball - Step & Roll (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Monkey Ball - Step & Roll (USA).iso',
        'size': 4699979776,
    },
    {
        'title': 'Super Paper Mario',
        'filename': 'Super Paper Mario (USA) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Paper Mario (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Paper Mario (USA) (v1.02).iso',
        'size': 4699979776,
    },
    {
        'title': 'Super Smash Bros. Brawl',
        'filename': 'Super Smash Bros. Brawl (USA) (v1.02).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Super Smash Bros. Brawl (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Super Smash Bros. Brawl (USA) (v1.02).iso',
        'size': 8511160320,
    },
    {
        'title': 'Xenoblade Chronicles',
        'filename': 'Xenoblade Chronicles (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Nintendo Wii [2006]/Xenoblade Chronicles (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Xenoblade Chronicles (USA) (En,Fr,Es).iso',
        'size': 8511160320,
    },
    {
        'title': "Zack & Wiki: Quest for Barbaros' Treasure",
        'filename': "Zack & Wiki - Quest for Barbaros' Treasure (USA).iso",
        'source_relative': "Consoles/Nintendo Wii [2006]/Zack & Wiki - Quest for Barbaros' Treasure (USA).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wii/Zack & Wiki - Quest for Barbaros' Treasure (USA).iso",
        'size': 4699979776,
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