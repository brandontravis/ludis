#!/usr/bin/env python3
# Auto-generated migration script for Sega Saturn
# 60 games, 0.00 B
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sega Saturn'
ESDE_FOLDER = 'saturn'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Casper',
        'filename': 'Casper (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Casper (NA)/Casper (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Casper (USA).cue',
        'size': 0,
    },
    {
        'title': 'Christmas NiGHTS into Dreams...',
        'filename': 'Christmas NiGHTS into Dreams... (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Christmas Nights into Dreams (NA)/Christmas NiGHTS into Dreams... (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Christmas NiGHTS into Dreams... (USA).cue',
        'size': 0,
    },
    {
        'title': 'College Slam',
        'filename': 'College Slam (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/College Slam (NA)/College Slam (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/College Slam (USA).cue',
        'size': 0,
    },
    {
        'title': 'Command & Conquer',
        'filename': 'Command & Conquer (USA) (Disc 1) (GDI Disc).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Command & Conquer (GDI Disc - NA)/Command & Conquer (USA) (Disc 1) (GDI Disc).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Command & Conquer (USA) (Disc 1) (GDI Disc).cue',
        'size': 0,
    },
    {
        'title': 'Contra: Legacy of War',
        'filename': 'Contra - Legacy of War (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Contra - Legacy of War (NA)/Contra - Legacy of War (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Contra - Legacy of War (USA).cue',
        'size': 0,
    },
    {
        'title': 'Croc: Legend of the Gobbos',
        'filename': 'Croc - Legend of the Gobbos (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Croc - Legend of the Gobbos (NA)/Croc - Legend of the Gobbos (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Croc - Legend of the Gobbos (USA).cue',
        'size': 0,
    },
    {
        'title': 'Die Hard Arcade',
        'filename': 'Die Hard Arcade (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Die Hard Arcade (NA)/Die Hard Arcade (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Die Hard Arcade (USA).cue',
        'size': 0,
    },
    {
        'title': 'Die Hard Trilogy',
        'filename': 'Die Hard Trilogy (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Die Hard Trilogy (NA)/Die Hard Trilogy (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Die Hard Trilogy (USA).cue',
        'size': 0,
    },
    {
        'title': 'Discworld II: Missing Presumed...!?',
        'filename': 'Discworld II - Missing Presumed...! (Europe) (En,Fr,De,Es,It).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Discworld II - Missing, Presumed...! (EU)/Discworld II - Missing Presumed...! (Europe) (En,Fr,De,Es,It).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Discworld II - Missing Presumed...! (Europe) (En,Fr,De,Es,It).cue',
        'size': 0,
    },
    {
        'title': 'DOOM',
        'filename': 'Doom (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Doom (NA)/Doom (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Doom (USA).cue',
        'size': 0,
    },
    {
        'title': 'Duke Nukem 3D',
        'filename': 'Duke Nukem 3D (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Duke Nukem 3D (NA)/Duke Nukem 3D (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Duke Nukem 3D (USA).cue',
        'size': 0,
    },
    {
        'title': 'Earthworm Jim 2',
        'filename': 'Earthworm Jim 2 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Earthworm Jim 2 (NA)/Earthworm Jim 2 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Earthworm Jim 2 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Gex',
        'filename': 'Gex (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Gex (NA)/Gex (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Gex (USA).cue',
        'size': 0,
    },
    {
        'title': 'Independence Day',
        'filename': 'Independence Day (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Independence Day (NA)/Independence Day (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Independence Day (USA).cue',
        'size': 0,
    },
    {
        'title': 'Mega Man 8',
        'filename': 'Mega Man 8 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Mega Man 8 (NA)/Mega Man 8 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Mega Man 8 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Mega Man X3',
        'filename': 'Mega Man X3 (Europe).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Mega Man X3 (EU)/Mega Man X3 (Europe).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Mega Man X3 (Europe).cue',
        'size': 0,
    },
    {
        'title': 'Mega Man X4',
        'filename': 'Mega Man X4 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Mega Man X4 (NA)/Mega Man X4 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Mega Man X4 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Mortal Kombat II',
        'filename': 'Mortal Kombat II (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Mortal Kombat II (NA)/Mortal Kombat II (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Mortal Kombat II (USA).cue',
        'size': 0,
    },
    {
        'title': 'Mortal Kombat Trilogy',
        'filename': 'Mortal Kombat Trilogy (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Mortal Kombat Trilogy (NA)/Mortal Kombat Trilogy (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Mortal Kombat Trilogy (USA).cue',
        'size': 0,
    },
    {
        'title': 'Myst',
        'filename': 'Myst (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Myst (NA)/Myst (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Myst (USA).cue',
        'size': 0,
    },
    {
        'title': 'NBA Jam Tournament Edition',
        'filename': 'NBA Jam - Tournament Edition (USA) (3S).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/NBA Jam - Tournament Edition (NA)/NBA Jam - Tournament Edition (USA) (3S).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/NBA Jam - Tournament Edition (USA) (3S).cue',
        'size': 0,
    },
    {
        'title': 'NBA Jam Extreme',
        'filename': 'NBA Jam Extreme (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/NBA Jam Extreme (NA)/NBA Jam Extreme (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/NBA Jam Extreme (USA).cue',
        'size': 0,
    },
    {
        'title': 'NiGHTS into Dreams...',
        'filename': 'NiGHTS into Dreams... (USA) (with 3D Control Pad) (RE).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Nights into Dreams... (NA)/NiGHTS into Dreams... (USA) (with 3D Control Pad) (RE).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/NiGHTS into Dreams... (USA) (with 3D Control Pad) (RE).cue',
        'size': 0,
    },
    {
        'title': 'Panzer Dragoon',
        'filename': 'Panzer Dragoon (USA) (5S).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Panzer Dragoon (NA)/Panzer Dragoon (USA) (5S).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Panzer Dragoon (USA) (5S).cue',
        'size': 0,
    },
    {
        'title': 'Panzer Dragoon II: Zwei',
        'filename': 'Panzer Dragoon II Zwei (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Panzer Dragoon II Zwei (NA)/Panzer Dragoon II Zwei (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Panzer Dragoon II Zwei (USA).cue',
        'size': 0,
    },
    {
        'title': 'Powerslave',
        'filename': 'Powerslave (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Powerslave (NA)/Powerslave (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Powerslave (USA).cue',
        'size': 0,
    },
    {
        'title': 'Quake',
        'filename': 'Quake (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Quake (NA)/Quake (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Quake (USA).cue',
        'size': 0,
    },
    {
        'title': 'Rampage World Tour',
        'filename': 'Rampage - World Tour (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Rampage - World Tour (NA)/Rampage - World Tour (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Rampage - World Tour (USA).cue',
        'size': 0,
    },
    {
        'title': 'Rayman',
        'filename': 'Rayman (USA) (R2).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Rayman (NA)/Rayman (USA) (R2).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Rayman (USA) (R2).cue',
        'size': 0,
    },
    {
        'title': 'Resident Evil',
        'filename': 'Resident Evil (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Resident Evil (NA)/Resident Evil (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Resident Evil (USA).cue',
        'size': 0,
    },
    {
        'title': 'Saturn Bomberman',
        'filename': 'Saturn Bomberman (USA) (1S).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Saturn Bomberman (NA)/Saturn Bomberman (USA) (1S).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Saturn Bomberman (USA) (1S).cue',
        'size': 0,
    },
    {
        'title': 'Sega Rally Championship',
        'filename': 'Sega Rally Championship (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Sega Rally Championship (NA)/Sega Rally Championship (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Sega Rally Championship (USA).cue',
        'size': 0,
    },
    {
        'title': "Sega Worldwide Soccer '97",
        'filename': "Sega Worldwide Soccer '97 (USA).cue",
        'source_relative': "Consoles/Sega Saturn [1994]/Sega Worldwide Soccer '97 (NA)/Sega Worldwide Soccer '97 (USA).cue",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Sega Worldwide Soccer '97 (USA).cue",
        'size': 0,
    },
    {
        'title': 'Shining Force III',
        'filename': 'Shining Force III (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Shining Force III (NA)/Shining Force III (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Shining Force III (USA).cue',
        'size': 0,
    },
    {
        'title': 'Shining the Holy Ark',
        'filename': 'Shining the Holy Ark (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Shining the Holy Ark (NA)/Shining the Holy Ark (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Shining the Holy Ark (USA).cue',
        'size': 0,
    },
    {
        'title': 'SimCity 2000',
        'filename': 'SimCity 2000 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/SimCity 2000 (NA)/SimCity 2000 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/SimCity 2000 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Sonic 3D Blast',
        'filename': 'Sonic 3D Blast (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Sonic 3D Blast (NA)/Sonic 3D Blast (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Sonic 3D Blast (USA).cue',
        'size': 0,
    },
    {
        'title': 'Sonic Jam',
        'filename': 'Sonic Jam (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Sonic Jam (NA)/Sonic Jam (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Sonic Jam (USA).cue',
        'size': 0,
    },
    {
        'title': 'Sonic R',
        'filename': 'Sonic R (USA, Brazil).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Sonic R (NA)/Sonic R (USA, Brazil).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Sonic R (USA, Brazil).cue',
        'size': 0,
    },
    {
        'title': 'Soviet Strike',
        'filename': 'Soviet Strike (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Soviet Strike (NA)/Soviet Strike (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Soviet Strike (USA).cue',
        'size': 0,
    },
    {
        'title': 'Space Jam',
        'filename': 'Space Jam (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Space Jam (NA)/Space Jam (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Space Jam (USA).cue',
        'size': 0,
    },
    {
        'title': 'Street Fighter: The Movie',
        'filename': 'Street Fighter - The Movie (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Street Fighter - The Movie (NA)/Street Fighter - The Movie (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Street Fighter - The Movie (USA).cue',
        'size': 0,
    },
    {
        'title': "Street Fighter Alpha: Warriors' Dreams",
        'filename': "Street Fighter Alpha - Warriors' Dreams (USA).cue",
        'source_relative': "Consoles/Sega Saturn [1994]/Street Fighter Alpha - Warriors' Dreams (NA)/Street Fighter Alpha - Warriors' Dreams (USA).cue",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Street Fighter Alpha - Warriors' Dreams (USA).cue",
        'size': 0,
    },
    {
        'title': 'Street Fighter Alpha 2',
        'filename': 'Street Fighter Alpha 2 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Street Fighter Alpha 2 (NA)/Street Fighter Alpha 2 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Street Fighter Alpha 2 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Street Fighter Collection',
        'filename': 'Street Fighter Collection (USA) (Disc 1).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Street Fighter Collection (Disc 1 - NA)/Street Fighter Collection (USA) (Disc 1).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Street Fighter Collection (USA) (Disc 1).cue',
        'size': 0,
    },
    {
        'title': "Terry Pratchett's Discworld",
        'filename': "Terry Pratchett's Discworld (Europe) (En,Fr,De,Es,It).cue",
        'source_relative': "Consoles/Sega Saturn [1994]/Terry Pratchett's Discworld (EU)/Terry Pratchett's Discworld (Europe) (En,Fr,De,Es,It).cue",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Terry Pratchett's Discworld (Europe) (En,Fr,De,Es,It).cue",
        'size': 0,
    },
    {
        'title': 'The House of the Dead',
        'filename': 'House of the Dead, The (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/The House of the Dead (NA)/House of the Dead, The (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/House of the Dead, The (USA).cue',
        'size': 0,
    },
    {
        'title': 'The Lost World: Jurassic Park',
        'filename': 'Lost World, The - Jurassic Park (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/The Lost World - Jurassic Park (NA)/Lost World, The - Jurassic Park (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Lost World, The - Jurassic Park (USA).cue',
        'size': 0,
    },
    {
        'title': 'ThunderStrike 2',
        'filename': 'Thunderstrike 2 (USA) (Rev A).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Thunderstrike 2 (NA, Rev A)/Thunderstrike 2 (USA) (Rev A).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Thunderstrike 2 (USA) (Rev A).cue',
        'size': 0,
    },
    {
        'title': 'Tomb Raider',
        'filename': 'Tomb Raider (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Tomb Raider (NA)/Tomb Raider (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Tomb Raider (USA).cue',
        'size': 0,
    },
    {
        'title': 'Ultimate Mortal Kombat 3',
        'filename': 'Ultimate Mortal Kombat 3 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Ultimate Mortal Kombat 3 (NA)/Ultimate Mortal Kombat 3 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Ultimate Mortal Kombat 3 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Virtua Cop',
        'filename': 'Virtua Cop (USA) (8S, 12S).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Virtua Cop (NA)/Virtua Cop (USA) (8S, 12S).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Virtua Cop (USA) (8S, 12S).cue',
        'size': 0,
    },
    {
        'title': 'Virtua Cop 2',
        'filename': 'Virtua Cop 2 (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Virtua Cop 2 (NA)/Virtua Cop 2 (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Virtua Cop 2 (USA).cue',
        'size': 0,
    },
    {
        'title': 'Virtua Fighter',
        'filename': 'Virtua Fighter (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Virtua Fighter (NA)/Virtua Fighter (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Virtua Fighter (USA).cue',
        'size': 0,
    },
    {
        'title': 'Virtua Fighter 2',
        'filename': 'Virtua Fighter 2 (USA) (RE).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Virtua Fighter 2 (NA)/Virtua Fighter 2 (USA) (RE).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Virtua Fighter 2 (USA) (RE).cue',
        'size': 0,
    },
    {
        'title': 'Virtua Fighter Kids',
        'filename': 'Virtua Fighter Kids (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Virtua Fighter Kids (NA)/Virtua Fighter Kids (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Virtua Fighter Kids (USA).cue',
        'size': 0,
    },
    {
        'title': 'Virtua Fighter Remix',
        'filename': 'Virtua Fighter Remix (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/Virtua Fighter Remix (NA)/Virtua Fighter Remix (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/Virtua Fighter Remix (USA).cue',
        'size': 0,
    },
    {
        'title': 'Warcraft II: The Dark Saga',
        'filename': 'WarCraft II - The Dark Saga (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/WarCraft II - The Dark Saga (NA)/WarCraft II - The Dark Saga (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/WarCraft II - The Dark Saga (USA).cue',
        'size': 0,
    },
    {
        'title': 'WipEout',
        'filename': 'WipEout (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/WipEout (NA)/WipEout (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/WipEout (USA).cue',
        'size': 0,
    },
    {
        'title': 'X-Men: Children of the Atom',
        'filename': 'X-Men - Children of the Atom (USA).cue',
        'source_relative': 'Consoles/Sega Saturn [1994]/X-Men - Children of the Atom (NA)/X-Men - Children of the Atom (USA).cue',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/saturn/X-Men - Children of the Atom (USA).cue',
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