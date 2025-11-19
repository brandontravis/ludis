#!/usr/bin/env python3
# Auto-generated migration script for Microsoft Xbox
# 157 games, 392.21 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Microsoft Xbox'
ESDE_FOLDER = 'xbox'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Amped: Freestyle Snowboarding',
        'filename': 'Amped - Freestyle Snowboarding (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Amped - Freestyle Snowboarding (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Amped - Freestyle Snowboarding (USA).iso',
        'size': 2379808768,
    },
    {
        'title': 'Amped 2',
        'filename': 'Amped 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Amped 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Amped 2 (USA).iso',
        'size': 4250533888,
    },
    {
        'title': 'Atari Anthology',
        'filename': 'Atari Anthology (Japan, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Atari Anthology (Japan, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Atari Anthology (Japan, Europe) (En,Fr,De,Es,It).iso',
        'size': 1172045824,
    },
    {
        'title': "Baldur's Gate: Dark Alliance",
        'filename': "Baldur's Gate - Dark Alliance (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Baldur's Gate - Dark Alliance (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Baldur's Gate - Dark Alliance (USA).iso",
        'size': 2793406464,
    },
    {
        'title': "Baldur's Gate: Dark Alliance II",
        'filename': "Baldur's Gate - Dark Alliance II (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Baldur's Gate - Dark Alliance II (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Baldur's Gate - Dark Alliance II (USA).iso",
        'size': 2807889920,
    },
    {
        'title': "The Bard's Tale",
        'filename': "Bard's Tale, The (Europe) (En,Fr,De,Es).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Bard's Tale, The (Europe) (En,Fr,De,Es).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Bard's Tale, The (Europe) (En,Fr,De,Es).iso",
        'size': 4884135936,
    },
    {
        'title': 'Batman Begins',
        'filename': 'Batman Begins (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Batman Begins (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Batman Begins (USA).iso',
        'size': 2027225088,
    },
    {
        'title': 'BMX XXX',
        'filename': 'BMX XXX (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/BMX XXX (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/BMX XXX (USA).iso',
        'size': 792788992,
    },
    {
        'title': 'Brothers in Arms: Road to Hill 30',
        'filename': 'Brothers in Arms - Road to Hill 30 (World) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Brothers in Arms - Road to Hill 30 (World) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Brothers in Arms - Road to Hill 30 (World) (En,Fr,De,Es,It).iso',
        'size': 3596353536,
    },
    {
        'title': 'Burnout 3: Takedown',
        'filename': 'Burnout 3 - Takedown (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Burnout 3 - Takedown (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Burnout 3 - Takedown (USA).iso',
        'size': 2476867584,
    },
    {
        'title': 'Call of Cthulhu: Dark Corners of the Earth',
        'filename': 'Call of Cthulhu - Dark Corners of the Earth (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Call of Cthulhu - Dark Corners of the Earth (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Call of Cthulhu - Dark Corners of the Earth (USA).iso',
        'size': 3401515008,
    },
    {
        'title': 'Call of Duty: Finest Hour',
        'filename': 'Call of Duty - Finest Hour (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Call of Duty - Finest Hour (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Call of Duty - Finest Hour (USA, Europe).iso',
        'size': 2167668736,
    },
    {
        'title': 'Call of Duty 2: Big Red One',
        'filename': 'Call of Duty 2 - Big Red One (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Call of Duty 2 - Big Red One (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Call of Duty 2 - Big Red One (USA, Europe).iso',
        'size': 3187539968,
    },
    {
        'title': 'Call of Duty 3',
        'filename': 'Call of Duty 3 (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Call of Duty 3 (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Call of Duty 3 (USA, Europe).iso',
        'size': 4251910144,
    },
    {
        'title': 'Capcom Classics Collection Vol. 1',
        'filename': 'Capcom Classics Collection Vol. 1 (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Capcom Classics Collection Vol. 1 (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Capcom Classics Collection Vol. 1 (USA, Europe).iso',
        'size': 3200909312,
    },
    {
        'title': 'Capcom Classics Collection Vol. 2',
        'filename': 'Capcom Classics Collection Vol. 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Capcom Classics Collection Vol. 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Capcom Classics Collection Vol. 2 (USA).iso',
        'size': 2585133056,
    },
    {
        'title': 'Capcom vs. SNK 2 EO',
        'filename': 'Capcom vs. SNK 2 EO (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Capcom vs. SNK 2 EO (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Capcom vs. SNK 2 EO (USA).iso',
        'size': 409927680,
    },
    {
        'title': 'Castlevania: Curse of Darkness',
        'filename': 'Castlevania - Curse of Darkness (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Castlevania - Curse of Darkness (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Castlevania - Curse of Darkness (USA).iso',
        'size': 3070099456,
    },
    {
        'title': 'Conker: Live & Reloaded',
        'filename': 'Conker - Live & Reloaded (USA) (En,Ja,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Conker - Live & Reloaded (USA) (En,Ja,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Conker - Live & Reloaded (USA) (En,Ja,Fr,De,Es,It).iso',
        'size': 4757782528,
    },
    {
        'title': 'Crash Bandicoot: The Wrath of Cortex',
        'filename': 'Crash Bandicoot - The Wrath of Cortex (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Crash Bandicoot - The Wrath of Cortex (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Crash Bandicoot - The Wrath of Cortex (USA).iso',
        'size': 975896576,
    },
    {
        'title': 'Crash Nitro Kart',
        'filename': 'Crash Nitro Kart (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Crash Nitro Kart (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Crash Nitro Kart (USA).iso',
        'size': 2897739776,
    },
    {
        'title': 'Crash Tag Team Racing',
        'filename': 'Crash Tag Team Racing (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Crash Tag Team Racing (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Crash Tag Team Racing (USA).iso',
        'size': 3126001664,
    },
    {
        'title': 'Crazy Taxi 3: High Roller',
        'filename': 'Crazy Taxi 3 - High Roller (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Crazy Taxi 3 - High Roller (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Crazy Taxi 3 - High Roller (USA).iso',
        'size': 395313152,
    },
    {
        'title': 'Crimson Skies: High Road to Revenge',
        'filename': 'Crimson Skies - High Road to Revenge (USA) (En,Fr,De,Zh,Ko).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Crimson Skies - High Road to Revenge (USA) (En,Fr,De,Zh,Ko).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Crimson Skies - High Road to Revenge (USA) (En,Fr,De,Zh,Ko).iso',
        'size': 4381802496,
    },
    {
        'title': 'Dave Mirra Freestyle BMX 2',
        'filename': 'Dave Mirra Freestyle BMX 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Dave Mirra Freestyle BMX 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Dave Mirra Freestyle BMX 2 (USA).iso',
        'size': 887226368,
    },
    {
        'title': 'Dead or Alive Ultimate',
        'filename': 'Dead or Alive 1 Ultimate (USA, Japan) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Dead or Alive 1 Ultimate (USA, Japan) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Dead or Alive 1 Ultimate (USA, Japan) (En,Ja).iso',
        'size': 4387635200,
    },
    {
        'title': 'Dead or Alive 2 Ultimate',
        'filename': 'Dead or Alive 2 Ultimate (USA, Japan) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Dead or Alive 2 Ultimate (USA, Japan) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Dead or Alive 2 Ultimate (USA, Japan) (En,Ja).iso',
        'size': 4387635200,
    },
    {
        'title': 'Dead or Alive 3',
        'filename': 'Dead or Alive 3 (USA) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Dead or Alive 3 (USA) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Dead or Alive 3 (USA) (En,Ja).iso',
        'size': 4191748096,
    },
    {
        'title': 'Dead or Alive: Xtreme Beach Volleyball',
        'filename': 'Dead or Alive Xtreme Beach Volleyball (USA) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Dead or Alive Xtreme Beach Volleyball (USA) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Dead or Alive Xtreme Beach Volleyball (USA) (En,Ja).iso',
        'size': 4349952000,
    },
    {
        'title': 'DOOM 3',
        'filename': 'Doom 3 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Doom 3 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Doom 3 (USA).iso',
        'size': 2272919552,
    },
    {
        'title': 'Doom 3: Resurrection of Evil',
        'filename': 'Doom 3 - Resurrection of Evil (USA, Europe) (En,Fr,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Doom 3 - Resurrection of Evil (USA, Europe) (En,Fr,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Doom 3 - Resurrection of Evil (USA, Europe) (En,Fr,Es,It).iso',
        'size': 2333081600,
    },
    {
        'title': 'The Elder Scrolls III: Morrowind',
        'filename': 'Elder Scrolls III, The - Morrowind (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Elder Scrolls III, The - Morrowind (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Elder Scrolls III, The - Morrowind (USA).iso',
        'size': 864223232,
    },
    {
        'title': 'The Elder Scrolls III: Morrowind: Game of the Year Edition',
        'filename': 'Elder Scrolls III, The - Morrowind - Game of the Year Edition (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Elder Scrolls III, The - Morrowind - Game of the Year Edition (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Elder Scrolls III, The - Morrowind - Game of the Year Edition (USA).iso',
        'size': 1015808000,
    },
    {
        'title': 'Enter the Matrix',
        'filename': 'Enter the Matrix (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Enter the Matrix (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Enter the Matrix (USA).iso',
        'size': 5120327680,
    },
    {
        'title': 'Fable',
        'filename': 'Fable (USA) (Limited Edition Bonus DVD).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Fable (USA) (Limited Edition Bonus DVD).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Fable (USA) (Limited Edition Bonus DVD).iso',
        'size': 5999034368,
    },
    {
        'title': 'Fable: The Lost Chapters',
        'filename': 'Fable - The Lost Chapters (USA) (En,Es).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Fable - The Lost Chapters (USA) (En,Es).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Fable - The Lost Chapters (USA) (En,Es).iso',
        'size': 3511877632,
    },
    {
        'title': 'Fallout: Brotherhood of Steel',
        'filename': 'Fallout - Brotherhood of Steel (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Fallout - Brotherhood of Steel (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Fallout - Brotherhood of Steel (USA).iso',
        'size': 2774859776,
    },
    {
        'title': 'Family Guy Video Game!',
        'filename': 'Family Guy - Video Game! (Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Family Guy - Video Game! (Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Family Guy - Video Game! (Europe).iso',
        'size': 3341549568,
    },
    {
        'title': 'Far Cry Instincts',
        'filename': 'Far Cry Instincts (USA, Europe) (En,Fr,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Far Cry Instincts (USA, Europe) (En,Fr,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Far Cry Instincts (USA, Europe) (En,Fr,Es,It).iso',
        'size': 2693201920,
    },
    {
        'title': 'Far Cry Instincts: Evolution',
        'filename': 'Far Cry Instincts - Evolution (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Far Cry Instincts - Evolution (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Far Cry Instincts - Evolution (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 2268069888,
    },
    {
        'title': 'Forza Motorsport',
        'filename': 'Forza Motorsport (USA) (En,Ja,Fr,De,Es,It,Pt,Zh,Ko) (Rev 1).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Forza Motorsport (USA) (En,Ja,Fr,De,Es,It,Pt,Zh,Ko) (Rev 1).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Forza Motorsport (USA) (En,Ja,Fr,De,Es,It,Pt,Zh,Ko) (Rev 1).iso',
        'size': 3572629504,
    },
    {
        'title': 'Futurama',
        'filename': 'Futurama (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Futurama (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Futurama (USA).iso',
        'size': 1281294336,
    },
    {
        'title': 'Grand Theft Auto: San Andreas',
        'filename': 'Grand Theft Auto - San Andreas (USA) (En,Es) (Rev 1).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Grand Theft Auto - San Andreas (USA) (En,Es) (Rev 1).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Grand Theft Auto - San Andreas (USA) (En,Es) (Rev 1).iso',
        'size': 3062431744,
    },
    {
        'title': 'Grand Theft Auto: Vice City',
        'filename': 'Grand Theft Auto - Vice City (USA) (Rev 1).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Grand Theft Auto - Vice City (USA) (Rev 1).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Grand Theft Auto - Vice City (USA) (Rev 1).iso',
        'size': 1384644608,
    },
    {
        'title': 'Grand Theft Auto III',
        'filename': 'Grand Theft Auto III (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Grand Theft Auto III (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Grand Theft Auto III (USA).iso',
        'size': 769785856,
    },
    {
        'title': 'Half-Life 2',
        'filename': 'Half-Life 2 (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Half-Life 2 (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Half-Life 2 (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 2059796480,
    },
    {
        'title': 'Halo: Combat Evolved',
        'filename': 'Halo - Combat Evolved (USA) (Rev 2).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Halo - Combat Evolved (USA) (Rev 2).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Halo - Combat Evolved (USA) (Rev 2).iso',
        'size': 3625713664,
    },
    {
        'title': 'Halo 2',
        'filename': 'Halo 2 (USA, Europe) (En,Ja,Fr,De,Es,It,Zh,Ko).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Halo 2 (USA, Europe) (En,Ja,Fr,De,Es,It,Zh,Ko).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Halo 2 (USA, Europe) (En,Ja,Fr,De,Es,It,Zh,Ko).iso',
        'size': 4721410048,
    },
    {
        'title': 'Hitman: Blood Money',
        'filename': 'Hitman - Blood Money (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Hitman - Blood Money (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Hitman - Blood Money (USA, Europe).iso',
        'size': 3889430528,
    },
    {
        'title': 'Hitman: Contracts',
        'filename': 'Hitman - Contracts (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Hitman - Contracts (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Hitman - Contracts (USA).iso',
        'size': 2417491968,
    },
    {
        'title': 'Hitman 2: Silent Assassin',
        'filename': 'Hitman 2 - Silent Assassin (USA, Asia) (Rev 1).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Hitman 2 - Silent Assassin (USA, Asia) (Rev 1).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Hitman 2 - Silent Assassin (USA, Asia) (Rev 1).iso',
        'size': 894173184,
    },
    {
        'title': 'Intellivision Lives!',
        'filename': 'Intellivision Lives! (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Intellivision Lives! (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Intellivision Lives! (USA).iso',
        'size': 316014592,
    },
    {
        'title': 'Jade Empire',
        'filename': 'Jade Empire (USA, Europe) (En,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Jade Empire (USA, Europe) (En,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Jade Empire (USA, Europe) (En,Es,It).iso',
        'size': 6587744256,
    },
    {
        'title': 'JSRF: Jet Set Radio Future',
        'filename': 'JSRF - Jet Set Radio Future (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/JSRF - Jet Set Radio Future (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/JSRF - Jet Set Radio Future (USA).iso',
        'size': 2502426624,
    },
    {
        'title': 'Just Cause',
        'filename': 'Just Cause (Europe) (En,Fr,De).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Just Cause (Europe) (En,Fr,De).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Just Cause (Europe) (En,Fr,De).iso',
        'size': 3597664256,
    },
    {
        'title': "Kelly Slater's Pro Surfer",
        'filename': "Kelly Slater's Pro Surfer (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Kelly Slater's Pro Surfer (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Kelly Slater's Pro Surfer (USA).iso",
        'size': 2462580736,
    },
    {
        'title': 'Lara Croft Tomb Raider: Legend',
        'filename': 'Lara Croft Tomb Raider - Legend (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Lara Croft Tomb Raider - Legend (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Lara Croft Tomb Raider - Legend (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 5015404544,
    },
    {
        'title': 'The Legend of Spyro: A New Beginning',
        'filename': 'Legend of Spyro, The - A New Beginning (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Legend of Spyro, The - A New Beginning (USA) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Legend of Spyro, The - A New Beginning (USA) (En,Fr,De,Es,It).iso',
        'size': 2078408704,
    },
    {
        'title': 'Leisure Suit Larry: Magna Cum Laude',
        'filename': 'Leisure Suit Larry - Magna Cum Laude (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Leisure Suit Larry - Magna Cum Laude (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Leisure Suit Larry - Magna Cum Laude (USA).iso',
        'size': 2966749184,
    },
    {
        'title': 'Manhunt',
        'filename': 'Manhunt (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Manhunt (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Manhunt (USA).iso',
        'size': 2493972480,
    },
    {
        'title': 'Marvel: Ultimate Alliance',
        'filename': 'Marvel - Ultimate Alliance (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Marvel - Ultimate Alliance (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Marvel - Ultimate Alliance (USA, Europe).iso',
        'size': 3895984128,
    },
    {
        'title': 'Marvel vs. Capcom 2: New Age of Heroes',
        'filename': 'Marvel vs. Capcom 2 - New Age of Heroes (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Marvel vs. Capcom 2 - New Age of Heroes (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Marvel vs. Capcom 2 - New Age of Heroes (USA).iso',
        'size': 252575744,
    },
    {
        'title': "Mat Hoffman's Pro BMX 2",
        'filename': "Mat Hoffman's Pro BMX 2 (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Mat Hoffman's Pro BMX 2 (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Mat Hoffman's Pro BMX 2 (USA).iso",
        'size': 3296395264,
    },
    {
        'title': 'The Matrix: Path of Neo',
        'filename': 'Matrix, The - Path of Neo (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Matrix, The - Path of Neo (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Matrix, The - Path of Neo (USA).iso',
        'size': 4780261376,
    },
    {
        'title': 'Max Payne',
        'filename': 'Max Payne (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Max Payne (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Max Payne (USA).iso',
        'size': 1738866688,
    },
    {
        'title': 'Max Payne 2: The Fall of Max Payne',
        'filename': 'Max Payne 2 - The Fall of Max Payne (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Max Payne 2 - The Fall of Max Payne (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Max Payne 2 - The Fall of Max Payne (USA).iso',
        'size': 1766719488,
    },
    {
        'title': 'MechAssault',
        'filename': 'MechAssault (USA) (En,Fr,De) (Rev 1).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/MechAssault (USA) (En,Fr,De) (Rev 1).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/MechAssault (USA) (En,Fr,De) (Rev 1).iso',
        'size': 3272802304,
    },
    {
        'title': 'Mega Man: Anniversary Collection',
        'filename': 'Mega Man Anniversary Collection (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Mega Man Anniversary Collection (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Mega Man Anniversary Collection (USA).iso',
        'size': 2882142208,
    },
    {
        'title': 'Minority Report: Everybody Runs',
        'filename': 'Minority Report - Everybody Runs (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Minority Report - Everybody Runs (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Minority Report - Everybody Runs (USA).iso',
        'size': 1340997632,
    },
    {
        'title': 'Mortal Kombat: Armageddon',
        'filename': 'Mortal Kombat - Armageddon (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Mortal Kombat - Armageddon (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Mortal Kombat - Armageddon (USA).iso',
        'size': 4635688960,
    },
    {
        'title': 'Mortal Kombat: Deadly Alliance',
        'filename': 'Mortal Kombat - Deadly Alliance (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Mortal Kombat - Deadly Alliance (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Mortal Kombat - Deadly Alliance (USA).iso',
        'size': 1617297408,
    },
    {
        'title': 'Mortal Kombat: Deception',
        'filename': "Mortal Kombat - Deception (USA) (Kollector's Edition Bonus Disc).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Mortal Kombat - Deception (USA) (Kollector's Edition Bonus Disc).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Mortal Kombat - Deception (USA) (Kollector's Edition Bonus Disc).iso",
        'size': 2446458880,
    },
    {
        'title': 'Mortal Kombat: Deception',
        'filename': "Mortal Kombat - Deception (USA) (Kollector's Edition Bonus Disc).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Mortal Kombat - Deception (USA) (Kollector's Edition Bonus Disc).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Mortal Kombat - Deception (USA) (Kollector's Edition Bonus Disc).iso",
        'size': 4051107840,
    },
    {
        'title': 'Mortal Kombat: Shaolin Monks',
        'filename': 'Mortal Kombat - Shaolin Monks (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Mortal Kombat - Shaolin Monks (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Mortal Kombat - Shaolin Monks (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 3930128384,
    },
    {
        'title': 'MTV Celebrity Deathmatch',
        'filename': 'MTV Celebrity Deathmatch (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/MTV Celebrity Deathmatch (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/MTV Celebrity Deathmatch (USA).iso',
        'size': 389939200,
    },
    {
        'title': 'Myst III: Exile',
        'filename': 'Myst III - Exile (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Myst III - Exile (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Myst III - Exile (USA).iso',
        'size': 2791833600,
    },
    {
        'title': 'Myst IV: Revelation',
        'filename': 'Myst IV - Revelation (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Myst IV - Revelation (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Myst IV - Revelation (USA).iso',
        'size': 4909236224,
    },
    {
        'title': 'Namco Museum: 50th Anniversary Arcade Collection',
        'filename': 'Namco Museum 50th Anniversary (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Namco Museum 50th Anniversary (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Namco Museum 50th Anniversary (USA).iso',
        'size': 281673728,
    },
    {
        'title': 'NBA Jam',
        'filename': 'NBA Jam (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/NBA Jam (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/NBA Jam (USA).iso',
        'size': 1200422912,
    },
    {
        'title': 'Need for Speed: Carbon',
        'filename': 'Need for Speed - Carbon (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Need for Speed - Carbon (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Need for Speed - Carbon (USA).iso',
        'size': 3033661440,
    },
    {
        'title': 'Need for Speed: Hot Pursuit 2',
        'filename': 'Need for Speed - Hot Pursuit 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Need for Speed - Hot Pursuit 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Need for Speed - Hot Pursuit 2 (USA).iso',
        'size': 896466944,
    },
    {
        'title': 'Need for Speed: Most Wanted: Black Edition',
        'filename': 'Need for Speed - Most Wanted - Black Edition (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Need for Speed - Most Wanted - Black Edition (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Need for Speed - Most Wanted - Black Edition (USA).iso',
        'size': 3113156608,
    },
    {
        'title': 'Need for Speed: Underground',
        'filename': 'Need for Speed - Underground (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Need for Speed - Underground (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Need for Speed - Underground (USA).iso',
        'size': 1884618752,
    },
    {
        'title': 'Need for Speed: Underground 2',
        'filename': 'Need for Speed - Underground 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Need for Speed - Underground 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Need for Speed - Underground 2 (USA).iso',
        'size': 2724986880,
    },
    {
        'title': 'Ninja Gaiden',
        'filename': 'Ninja Gaiden (USA, Japan) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Ninja Gaiden (USA, Japan) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Ninja Gaiden (USA, Japan) (En,Ja).iso',
        'size': 6319505408,
    },
    {
        'title': 'Ninja Gaiden Black',
        'filename': 'Ninja Gaiden Black (USA) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Ninja Gaiden Black (USA) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Ninja Gaiden Black (USA) (En,Ja).iso',
        'size': 6337134592,
    },
    {
        'title': "Oddworld: Stranger's Wrath",
        'filename': "Oddworld - Stranger's Wrath (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Oddworld - Stranger's Wrath (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Oddworld - Stranger's Wrath (USA).iso",
        'size': 2261975040,
    },
    {
        'title': 'OutRun 2',
        'filename': 'OutRun 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/OutRun 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/OutRun 2 (USA).iso',
        'size': 1140654080,
    },
    {
        'title': 'OutRun 2006: Coast 2 Coast',
        'filename': 'OutRun 2006 - Coast 2 Coast (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/OutRun 2006 - Coast 2 Coast (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/OutRun 2006 - Coast 2 Coast (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 866779136,
    },
    {
        'title': 'Panzer Dragoon Orta',
        'filename': 'Panzer Dragoon Orta (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Panzer Dragoon Orta (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Panzer Dragoon Orta (USA).iso',
        'size': 3098279936,
    },
    {
        'title': 'Phantasy Star Online Episode I & II',
        'filename': 'Phantasy Star Online Episode I & II (USA) (En,Ja,Fr,De,Es).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Phantasy Star Online Episode I & II (USA) (En,Ja,Fr,De,Es).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Phantasy Star Online Episode I & II (USA) (En,Ja,Fr,De,Es).iso',
        'size': 1916862464,
    },
    {
        'title': 'Pitfall: The Lost Expedition',
        'filename': 'Pitfall - The Lost Expedition (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Pitfall - The Lost Expedition (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Pitfall - The Lost Expedition (USA).iso',
        'size': 1004929024,
    },
    {
        'title': 'Playboy: The Mansion',
        'filename': 'Playboy - The Mansion (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Playboy - The Mansion (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Playboy - The Mansion (USA).iso',
        'size': 934150144,
    },
    {
        'title': 'Prince of Persia: The Sands of Time',
        'filename': 'Prince of Persia - The Sands of Time (USA) (En,Fr,Es).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Prince of Persia - The Sands of Time (USA) (En,Fr,Es).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Prince of Persia - The Sands of Time (USA) (En,Fr,Es).iso',
        'size': 2500657152,
    },
    {
        'title': 'Prince of Persia: The Two Thrones',
        'filename': 'Prince of Persia - The Two Thrones (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Prince of Persia - The Two Thrones (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Prince of Persia - The Two Thrones (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 2588540928,
    },
    {
        'title': 'Prince of Persia: Warrior Within',
        'filename': 'Prince of Persia - Warrior Within (USA, Europe) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Prince of Persia - Warrior Within (USA, Europe) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Prince of Persia - Warrior Within (USA, Europe) (En,Fr,De,Es,It).iso',
        'size': 2950103040,
    },
    {
        'title': 'Project Gotham Racing',
        'filename': 'Project Gotham Racing (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Project Gotham Racing (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Project Gotham Racing (USA).iso',
        'size': 2222522368,
    },
    {
        'title': 'Project Gotham Racing 2',
        'filename': 'Project Gotham Racing 2 (USA, Japan) (En,Ja,Fr,De,Es,It,Zh,Ko).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Project Gotham Racing 2 (USA, Japan) (En,Ja,Fr,De,Es,It,Zh,Ko).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Project Gotham Racing 2 (USA, Japan) (En,Ja,Fr,De,Es,It,Zh,Ko).iso',
        'size': 5649793024,
    },
    {
        'title': 'Psychonauts',
        'filename': 'Psychonauts (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Psychonauts (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Psychonauts (USA).iso',
        'size': 4134010880,
    },
    {
        'title': 'Rayman 3: Hoodlum Havoc',
        'filename': 'Rayman 3 - Hoodlum Havoc (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Rayman 3 - Hoodlum Havoc (USA) (En,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Rayman 3 - Hoodlum Havoc (USA) (En,Fr,De,Es,It).iso',
        'size': 2268069888,
    },
    {
        'title': 'Rayman Arena',
        'filename': 'Rayman Arena (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Rayman Arena (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Rayman Arena (USA).iso',
        'size': 1124270080,
    },
    {
        'title': 'Red Dead Revolver',
        'filename': 'Red Dead Revolver (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Red Dead Revolver (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Red Dead Revolver (USA).iso',
        'size': 3135176704,
    },
    {
        'title': 'Return to Castle Wolfenstein: Tides of War',
        'filename': 'Return to Castle Wolfenstein - Tides of War (World).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Return to Castle Wolfenstein - Tides of War (World).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Return to Castle Wolfenstein - Tides of War (World).iso',
        'size': 3736010752,
    },
    {
        'title': 'RollerCoaster Tycoon',
        'filename': 'RollerCoaster Tycoon (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/RollerCoaster Tycoon (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/RollerCoaster Tycoon (USA).iso',
        'size': 243466240,
    },
    {
        'title': 'Shadow the Hedgehog',
        'filename': 'Shadow the Hedgehog (USA) (En,Ja,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Shadow the Hedgehog (USA) (En,Ja,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Shadow the Hedgehog (USA) (En,Ja,Fr,De,Es,It).iso',
        'size': 2538209280,
    },
    {
        'title': 'Shenmue II',
        'filename': 'Shenmue II (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Shenmue II (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Shenmue II (USA).iso',
        'size': 5255790592,
    },
    {
        'title': 'The Simpsons: Hit & Run',
        'filename': 'Simpsons, The - Hit & Run (USA, Japan).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Simpsons, The - Hit & Run (USA, Japan).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Simpsons, The - Hit & Run (USA, Japan).iso',
        'size': 1995702272,
    },
    {
        'title': 'The Simpsons: Road Rage',
        'filename': 'Simpsons, The - Road Rage (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Simpsons, The - Road Rage (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Simpsons, The - Road Rage (USA).iso',
        'size': 325320704,
    },
    {
        'title': 'The Sims 2',
        'filename': 'Sims 2, The (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Sims 2, The (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Sims 2, The (USA).iso',
        'size': 1986920448,
    },
    {
        'title': 'The Sims',
        'filename': 'Sims, The (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Sims, The (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Sims, The (USA).iso',
        'size': 413532160,
    },
    {
        'title': "The Sims: Bustin' Out",
        'filename': "Sims, The - Bustin' Out (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Sims, The - Bustin' Out (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Sims, The - Bustin' Out (USA).iso",
        'size': 2104754176,
    },
    {
        'title': 'Sniper Elite',
        'filename': 'Sniper Elite (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Sniper Elite (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Sniper Elite (USA).iso',
        'size': 1790509056,
    },
    {
        'title': 'Sonic Heroes',
        'filename': 'Sonic Heroes (USA) (En,Ja,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Sonic Heroes (USA) (En,Ja,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Sonic Heroes (USA) (En,Ja,Fr,De,Es,It).iso',
        'size': 4099407872,
    },
    {
        'title': 'Sonic Mega Collection Plus',
        'filename': 'Sonic Mega Collection Plus (World) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Sonic Mega Collection Plus (World) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Sonic Mega Collection Plus (World) (En,Ja).iso',
        'size': 3742957568,
    },
    {
        'title': 'Sonic Riders',
        'filename': 'Sonic Riders (USA) (En,Ja,Fr,De,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Sonic Riders (USA) (En,Ja,Fr,De,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Sonic Riders (USA) (En,Ja,Fr,De,Es,It).iso',
        'size': 2570190848,
    },
    {
        'title': 'SoulCalibur II',
        'filename': 'Soulcalibur II (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Soulcalibur II (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Soulcalibur II (USA).iso',
        'size': 1374158848,
    },
    {
        'title': 'SoulCalibur II',
        'filename': 'Soulcalibur II (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Soulcalibur II (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Soulcalibur II (USA).iso',
        'size': 1376845824,
    },
    {
        'title': 'Spider-Man',
        'filename': 'Spider-Man (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Spider-Man (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Spider-Man (USA).iso',
        'size': 1999896576,
    },
    {
        'title': 'Spider-Man 2',
        'filename': 'Spider-Man 2 (World).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Spider-Man 2 (World).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Spider-Man 2 (World).iso',
        'size': 1715666944,
    },
    {
        'title': "Spyro: A Hero's Tail",
        'filename': "Spyro - A Hero's Tail (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Spyro - A Hero's Tail (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Spyro - A Hero's Tail (USA).iso",
        'size': 915537920,
    },
    {
        'title': 'SSX 3',
        'filename': 'SSX 3 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/SSX 3 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/SSX 3 (USA).iso',
        'size': 2102525952,
    },
    {
        'title': 'SSX on Tour',
        'filename': 'SSX On Tour (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/SSX On Tour (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/SSX On Tour (USA).iso',
        'size': 2046099456,
    },
    {
        'title': 'SSX Tricky',
        'filename': 'SSX Tricky (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/SSX Tricky (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/SSX Tricky (USA).iso',
        'size': 3012493312,
    },
    {
        'title': 'Star Wars: Battlefront',
        'filename': 'Star Wars - Battlefront (USA, Europe).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Battlefront (USA, Europe).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Battlefront (USA, Europe).iso',
        'size': 2423586816,
    },
    {
        'title': 'Star Wars: Battlefront II',
        'filename': 'Star Wars - Battlefront II (USA, Europe) (En,Es,It).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Battlefront II (USA, Europe) (En,Es,It).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Battlefront II (USA, Europe) (En,Es,It).iso',
        'size': 3415932928,
    },
    {
        'title': 'Star Wars: Episode III: Revenge of the Sith',
        'filename': 'Star Wars - Episode III - Revenge of the Sith (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Episode III - Revenge of the Sith (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Episode III - Revenge of the Sith (USA).iso',
        'size': 2610167808,
    },
    {
        'title': 'Star Wars: Jedi Knight: Jedi Academy',
        'filename': 'Star Wars - Jedi Knight - Jedi Academy (USA) (En,Fr,De).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Jedi Knight - Jedi Academy (USA) (En,Fr,De).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Jedi Knight - Jedi Academy (USA) (En,Fr,De).iso',
        'size': 1494941696,
    },
    {
        'title': 'Star Wars: Jedi Knight II: Jedi Outcast',
        'filename': 'Star Wars - Jedi Knight II - Jedi Outcast (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Jedi Knight II - Jedi Outcast (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Jedi Knight II - Jedi Outcast (USA).iso',
        'size': 1734606848,
    },
    {
        'title': 'Star Wars: Jedi Starfighter',
        'filename': 'Star Wars - Jedi Starfighter (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Jedi Starfighter (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Jedi Starfighter (USA).iso',
        'size': 3224240128,
    },
    {
        'title': 'Star Wars: Knights of the Old Republic',
        'filename': 'Star Wars - Knights of the Old Republic (USA) (Rev 1).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Knights of the Old Republic (USA) (Rev 1).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Knights of the Old Republic (USA) (Rev 1).iso',
        'size': 3939303424,
    },
    {
        'title': 'Star Wars: Knights of the Old Republic II: The Sith Lords',
        'filename': 'Star Wars - Knights of the Old Republic II - The Sith Lords (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Knights of the Old Republic II - The Sith Lords (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Knights of the Old Republic II - The Sith Lords (USA).iso',
        'size': 4112318464,
    },
    {
        'title': 'Star Wars: Obi-Wan',
        'filename': 'Star Wars - Obi-Wan (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Obi-Wan (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Obi-Wan (USA).iso',
        'size': 2221146112,
    },
    {
        'title': 'Star Wars: Republic Commando',
        'filename': 'Star Wars - Republic Commando (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - Republic Commando (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - Republic Commando (USA).iso',
        'size': 3637903360,
    },
    {
        'title': 'Star Wars: The Clone Wars',
        'filename': 'Star Wars - The Clone Wars (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Star Wars - The Clone Wars (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Star Wars - The Clone Wars (USA).iso',
        'size': 1474822144,
    },
    {
        'title': 'Street Fighter Anniversary Collection',
        'filename': 'Street Fighter Anniversary Collection (USA) (En,Ja).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Street Fighter Anniversary Collection (USA) (En,Ja).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Street Fighter Anniversary Collection (USA) (En,Ja).iso',
        'size': 3624402944,
    },
    {
        'title': 'Super Monkey Ball Deluxe',
        'filename': 'Super Monkey Ball Deluxe (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Super Monkey Ball Deluxe (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Super Monkey Ball Deluxe (USA).iso',
        'size': 2953707520,
    },
    {
        'title': 'Tecmo Classic Arcade',
        'filename': 'Tecmo Classic Arcade (USA, Japan).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Tecmo Classic Arcade (USA, Japan).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Tecmo Classic Arcade (USA, Japan).iso',
        'size': 271712256,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles',
        'filename': 'Teenage Mutant Ninja Turtles (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Teenage Mutant Ninja Turtles (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Teenage Mutant Ninja Turtles (USA).iso',
        'size': 1417150464,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles 2: Battle Nexus',
        'filename': 'Teenage Mutant Ninja Turtles 2 - Battle Nexus (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Teenage Mutant Ninja Turtles 2 - Battle Nexus (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Teenage Mutant Ninja Turtles 2 - Battle Nexus (USA).iso',
        'size': 2923364352,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles 3: Mutant Nightmare',
        'filename': 'Teenage Mutant Ninja Turtles 3 - Mutant Nightmare (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Teenage Mutant Ninja Turtles 3 - Mutant Nightmare (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Teenage Mutant Ninja Turtles 3 - Mutant Nightmare (USA).iso',
        'size': 2617114624,
    },
    {
        'title': 'Thief: Deadly Shadows',
        'filename': 'Thief - Deadly Shadows (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Thief - Deadly Shadows (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Thief - Deadly Shadows (USA).iso',
        'size': 2350841856,
    },
    {
        'title': 'TimeSplitters: Future Perfect',
        'filename': 'TimeSplitters - Future Perfect (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/TimeSplitters - Future Perfect (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/TimeSplitters - Future Perfect (USA).iso',
        'size': 4047372288,
    },
    {
        'title': 'TimeSplitters 2',
        'filename': 'TimeSplitters 2 (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/TimeSplitters 2 (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/TimeSplitters 2 (USA).iso',
        'size': 1821966336,
    },
    {
        'title': 'TMNT: Mutant Melee',
        'filename': 'TMNT - Mutant Melee (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/TMNT - Mutant Melee (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/TMNT - Mutant Melee (USA).iso',
        'size': 1012400128,
    },
    {
        'title': 'ToeJam & Earl III: Mission to Earth',
        'filename': 'ToeJam & Earl III - Mission to Earth (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/ToeJam & Earl III - Mission to Earth (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/ToeJam & Earl III - Mission to Earth (USA).iso',
        'size': 2669150208,
    },
    {
        'title': "Tom Clancy's Splinter Cell",
        'filename': "Tom Clancy's Splinter Cell (USA) (En,Fr).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tom Clancy's Splinter Cell (USA) (En,Fr).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tom Clancy's Splinter Cell (USA) (En,Fr).iso",
        'size': 2947678208,
    },
    {
        'title': "Tom Clancy's Splinter Cell: Chaos Theory",
        'filename': "Tom Clancy's Splinter Cell - Chaos Theory (USA, Europe) (En,Fr,De,Es,It).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tom Clancy's Splinter Cell - Chaos Theory (USA, Europe) (En,Fr,De,Es,It).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tom Clancy's Splinter Cell - Chaos Theory (USA, Europe) (En,Fr,De,Es,It).iso",
        'size': 5755502592,
    },
    {
        'title': "Tom Clancy's Splinter Cell: Pandora Tomorrow",
        'filename': "Tom Clancy's Splinter Cell - Pandora Tomorrow (USA, Europe) (En,Fr,De,Es,It).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tom Clancy's Splinter Cell - Pandora Tomorrow (USA, Europe) (En,Fr,De,Es,It).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tom Clancy's Splinter Cell - Pandora Tomorrow (USA, Europe) (En,Fr,De,Es,It).iso",
        'size': 3115581440,
    },
    {
        'title': "Tony Hawk's American Wasteland",
        'filename': "Tony Hawk's American Wasteland (USA, Europe) (En,Fr,De,Es,It).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's American Wasteland (USA, Europe) (En,Fr,De,Es,It).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's American Wasteland (USA, Europe) (En,Fr,De,Es,It).iso",
        'size': 3105882112,
    },
    {
        'title': "Tony Hawk's Pro Skater 2x",
        'filename': "Tony Hawk's Pro Skater 2x (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's Pro Skater 2x (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's Pro Skater 2x (USA).iso",
        'size': 1228341248,
    },
    {
        'title': "Tony Hawk's Pro Skater 3",
        'filename': "Tony Hawk's Pro Skater 3 (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's Pro Skater 3 (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's Pro Skater 3 (USA).iso",
        'size': 3472490496,
    },
    {
        'title': "Tony Hawk's Pro Skater 4",
        'filename': "Tony Hawk's Pro Skater 4 (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's Pro Skater 4 (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's Pro Skater 4 (USA).iso",
        'size': 1615396864,
    },
    {
        'title': "Tony Hawk's Project 8",
        'filename': "Tony Hawk's Project 8 (USA, Europe) (En,Fr,De,Es,It).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's Project 8 (USA, Europe) (En,Fr,De,Es,It).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's Project 8 (USA, Europe) (En,Fr,De,Es,It).iso",
        'size': 3856596992,
    },
    {
        'title': "Tony Hawk's Underground",
        'filename': "Tony Hawk's Underground (USA).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's Underground (USA).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's Underground (USA).iso",
        'size': 3409444864,
    },
    {
        'title': "Tony Hawk's Underground 2",
        'filename': "Tony Hawk's Underground 2 (USA, Europe) (En,Fr,De).iso",
        'source_relative': "Consoles/Microsoft Xbox [2001]/Tony Hawk's Underground 2 (USA, Europe) (En,Fr,De).iso",
        'dest': "/home/idealbrandon/Emulation/sym_roms/xbox/Tony Hawk's Underground 2 (USA, Europe) (En,Fr,De).iso",
        'size': 3575709696,
    },
    {
        'title': 'Turok: Evolution',
        'filename': 'Turok - Evolution (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Turok - Evolution (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Turok - Evolution (USA).iso',
        'size': 2516582400,
    },
    {
        'title': 'Wakeboarding Unleashed Featuring Shaun Murray',
        'filename': 'Wakeboarding Unleashed featuring Shaun Murray (USA).iso',
        'source_relative': 'Consoles/Microsoft Xbox [2001]/Wakeboarding Unleashed featuring Shaun Murray (USA).iso',
        'dest': '/home/idealbrandon/Emulation/sym_roms/xbox/Wakeboarding Unleashed featuring Shaun Murray (USA).iso',
        'size': 1516306432,
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