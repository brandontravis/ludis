#!/usr/bin/env python3
# Auto-generated migration script for Sega Dreamcast
# 66 games, 0.00 B
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sega Dreamcast'
ESDE_FOLDER = 'dreamcast'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Atari Anniversary Edition',
        'filename': 'Atari Anniversary Edition (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Atari Anniversary Edition (USA)/Atari Anniversary Edition (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Atari Anniversary Edition (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Capcom vs. SNK',
        'filename': 'Capcom vs. SNK (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Capcom vs. SNK (USA)/Capcom vs. SNK (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Capcom vs. SNK (USA).gdi',
        'size': 0,
    },
    {
        'title': 'ChuChu Rocket!',
        'filename': 'ChuChu Rocket! (USA) (En,Ja,Fr,De,Es).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/ChuChu Rocket! (USA) (En,Ja,Fr,De,Es)/ChuChu Rocket! (USA) (En,Ja,Fr,De,Es).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/ChuChu Rocket! (USA) (En,Ja,Fr,De,Es).gdi',
        'size': 0,
    },
    {
        'title': 'Crazy Taxi 2',
        'filename': 'Crazy Taxi 2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Crazy Taxi 2 (v1.004) (2001)(Sega)(NTSC)(US)[!]/Crazy Taxi 2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Crazy Taxi 2 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Crazy Taxi',
        'filename': 'Crazy Taxi (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Crazy Taxi v1.004 (1999)(Sega)(NTSC)(US)[!][10S 51035]/Crazy Taxi (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Crazy Taxi (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Dave Mirra Freestyle BMX',
        'filename': 'Dave Mirra Freestyle BMX (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Dave Mirra Freestyle BMX (USA)/Dave Mirra Freestyle BMX (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Dave Mirra Freestyle BMX (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Dead or Alive 2',
        'filename': 'Dead or Alive 2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Dead or Alive 2 v1.100 (2000)(Tecmo)(NTSC)(US)[!]/Dead or Alive 2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Dead or Alive 2 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Ecco the Dolphin: Defender of the Future',
        'filename': 'ECCO the Dolphin - Defender of the Future (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/ECCO the Dolphin - Defender of the Future v1.000 (2000)(Sega)(NTSC)(US)(M4)[!]/ECCO the Dolphin - Defender of the Future (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/ECCO the Dolphin - Defender of the Future (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Freestyle Scooter',
        'filename': 'Freestyle Scooter (Europe).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Freestyle Scooter (Europe)/Freestyle Scooter (Europe).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Freestyle Scooter (Europe).gdi',
        'size': 0,
    },
    {
        'title': "Frogger 2: Swampy's Revenge",
        'filename': "Frogger 2 - Swampy's Revenge (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Frogger 2 - Swampy's Revenge (USA)/Frogger 2 - Swampy's Revenge (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Frogger 2 - Swampy's Revenge (USA).gdi",
        'size': 0,
    },
    {
        'title': 'Grand Theft Auto 2',
        'filename': 'Grand Theft Auto 2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Grand Theft Auto 2 v1.002 (2000)(Rockstar)(NTSC)(US)[!]/Grand Theft Auto 2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Grand Theft Auto 2 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'The House of the Dead 2',
        'filename': 'House of the Dead 2, The (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/House of the Dead 2, The v1.001 (1999)(Sega)(NTSC)(US)[!][13S 51002]/House of the Dead 2, The (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/House of the Dead 2, The (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Jet Grind Radio',
        'filename': 'Jet Grind Radio (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Jet Grind Radio v1.005 (2000)(Sega)(NTSC)(US)[!]/Jet Grind Radio (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Jet Grind Radio (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Marvel vs. Capcom: Clash of Super Heroes',
        'filename': 'Marvel vs. Capcom - Clash of Super Heroes (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Marvel vs. Capcom - Clash of Super Heroes v1.000 (1999)(Capcom)(NTSC)(US)[!]/Marvel vs. Capcom - Clash of Super Heroes (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Marvel vs. Capcom - Clash of Super Heroes (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Marvel vs. Capcom 2',
        'filename': 'Marvel vs. Capcom 2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Marvel vs. Capcom 2 v1.001 (2000)(Capcom)(NTSC)(US)[!]/Marvel vs. Capcom 2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Marvel vs. Capcom 2 (USA).gdi',
        'size': 0,
    },
    {
        'title': "Midway's Greatest Arcade Hits Volume 1",
        'filename': "Midway's Greatest Arcade Hits - Volume 1 (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Midway's Greatest Arcade Hits - Volume 1 (USA)/Midway's Greatest Arcade Hits - Volume 1 (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Midway's Greatest Arcade Hits - Volume 1 (USA).gdi",
        'size': 0,
    },
    {
        'title': "Midway's Greatest Arcade Hits Volume 2",
        'filename': "Midway's Greatest Arcade Hits - Volume 2 (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Midway's Greatest Arcade Hits - Volume 2 (USA)/Midway's Greatest Arcade Hits - Volume 2 (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Midway's Greatest Arcade Hits - Volume 2 (USA).gdi",
        'size': 0,
    },
    {
        'title': 'Ms. Pac-Man Maze Madness',
        'filename': 'Ms. Pac-Man Maze Madness (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Ms. Pac-Man Maze Madness (USA)/Ms. Pac-Man Maze Madness (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Ms. Pac-Man Maze Madness (USA).gdi',
        'size': 0,
    },
    {
        'title': 'MTV Sports: Skateboarding featuring Andy Macdonald',
        'filename': 'MTV Sports - Skateboarding featuring Andy Macdonald (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/MTV Sports - Skateboarding featuring Andy Macdonald (USA)/MTV Sports - Skateboarding featuring Andy Macdonald (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/MTV Sports - Skateboarding featuring Andy Macdonald (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Namco Museum',
        'filename': 'Namco Museum (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Namco Museum (USA)/Namco Museum (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Namco Museum (USA).gdi',
        'size': 0,
    },
    {
        'title': 'NFL 2K2',
        'filename': 'NFL 2K2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/NFL 2K2 (USA)/NFL 2K2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/NFL 2K2 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Phantasy Star Online',
        'filename': 'Phantasy Star Online (USA) (En,Ja,Fr,De,Es) (Rev B).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Phantasy Star Online (USA) (En,Ja,Fr,De,Es) (Rev B)/Phantasy Star Online (USA) (En,Ja,Fr,De,Es) (Rev B).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Phantasy Star Online (USA) (En,Ja,Fr,De,Es) (Rev B).gdi',
        'size': 0,
    },
    {
        'title': 'Phantasy Star Online Ver. 2',
        'filename': 'Phantasy Star Online Ver. 2 (USA) (En,Ja,Fr,De,Es).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Phantasy Star Online Ver. 2 (USA) (En,Ja,Fr,De,Es)/Phantasy Star Online Ver. 2 (USA) (En,Ja,Fr,De,Es).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Phantasy Star Online Ver. 2 (USA) (En,Ja,Fr,De,Es).gdi',
        'size': 0,
    },
    {
        'title': 'Power Stone 2',
        'filename': 'Power Stone 2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Power Stone 2 (USA)/Power Stone 2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Power Stone 2 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Q-bert',
        'filename': 'Q-bert (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Q-bert (USA)/Q-bert (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Q-bert (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Quake III Arena',
        'filename': 'Quake III Arena (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Quake III Arena v0.800 (2000)(Sega)(NTSC)(US)[!]/Quake III Arena (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Quake III Arena (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Railroad Tycoon II: Gold Edition',
        'filename': 'Railroad Tycoon II - Gold Edition (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Railroad Tycoon II - Gold Edition v1.004 (2000)(GOD)(NTSC)(US)[!]/Railroad Tycoon II - Gold Edition (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Railroad Tycoon II - Gold Edition (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Rayman 2: The Great Escape',
        'filename': 'Rayman 2 - The Great Escape (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Rayman 2 - The Great Escape v1.003 (2000)(Ubi Soft)(NTSC)(US)[!]/Rayman 2 - The Great Escape (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Rayman 2 - The Great Escape (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Rayman 2: The Great Escape',
        'filename': 'Rayman 2 - The Great Escape (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Rayman 2 - The Great Escape v1.003 (2000)(Ubi Soft)(NTSC)(US)[!]/Rayman 2 - The Great Escape (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Rayman 2 - The Great Escape (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Resident Evil: Code: Veronica',
        'filename': 'Resident Evil - Code Veronica (USA) (Disc 1 of 2).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Resident Evil - Code Veronica v1.000 (2000)(Capcom)(NTSC)(US)(Disc 1 of 2)[!]/Resident Evil - Code Veronica (USA) (Disc 1 of 2).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Resident Evil - Code Veronica (USA) (Disc 1 of 2).gdi',
        'size': 0,
    },
    {
        'title': 'Resident Evil 2',
        'filename': 'Resident Evil 2 (USA) (Disc 1 of 2).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Resident Evil 2 v1.001 (2000)(Capcom)(NTSC)(US)(Disc 1 of 2)[!][Leon]/Resident Evil 2 (USA) (Disc 1 of 2).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Resident Evil 2 (USA) (Disc 1 of 2).gdi',
        'size': 0,
    },
    {
        'title': 'Resident Evil 3: Nemesis',
        'filename': 'Resident Evil 3 - Nemesis (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Resident Evil 3 - Nemesis v1.000 (2000)(Capcom)(NTSC)(US)[!]/Resident Evil 3 - Nemesis (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Resident Evil 3 - Nemesis (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Rez',
        'filename': 'Rez (Europe) (En,Ja,Fr,De,Es,It).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Rez (Europe) (En,Ja,Fr,De,Es,It)/Rez (Europe) (En,Ja,Fr,De,Es,It).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Rez (Europe) (En,Ja,Fr,De,Es,It).gdi',
        'size': 0,
    },
    {
        'title': "Rippin' Riders Snowboarding",
        'filename': "Rippin' Riders Snowboarding (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Rippin' Riders Snowboarding v1.001 (1999)(Sega)(NTSC)(US)[!]/Rippin' Riders Snowboarding (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Rippin' Riders Snowboarding (USA).gdi",
        'size': 0,
    },
    {
        'title': 'Seaman',
        'filename': 'Seaman (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Seaman (USA)/Seaman (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Seaman (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Sega Bass Fishing',
        'filename': 'Sega Bass Fishing (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Sega Bass Fishing (USA)/Sega Bass Fishing (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Sega Bass Fishing (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Sega Smash Pack: Volume 1',
        'filename': 'Sega Smash Pack - Volume 1 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Sega Smash Pack - Volume 1 (USA)/Sega Smash Pack - Volume 1 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Sega Smash Pack - Volume 1 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Shenmue',
        'filename': 'Shenmue (USA) (Disc 1).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue (USA) (Disc 1)/Shenmue (USA) (Disc 1).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue (USA) (Disc 1).gdi',
        'size': 0,
    },
    {
        'title': 'Shenmue',
        'filename': 'Shenmue (USA) (Disc 2)',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue (USA) (Disc 2)',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue (USA) (Disc 2)',
        'size': 0,
    },
    {
        'title': 'Shenmue',
        'filename': 'Shenmue (USA) (Disc 3)',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue (USA) (Disc 3)',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue (USA) (Disc 3)',
        'size': 0,
    },
    {
        'title': 'Shenmue II',
        'filename': 'Shenmue II (Europe) (En,Fr,De,Es) (Disc 1).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue II (Europe) (En,Fr,De,Es) (Disc 1)/Shenmue II (Europe) (En,Fr,De,Es) (Disc 1).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue II (Europe) (En,Fr,De,Es) (Disc 1).gdi',
        'size': 0,
    },
    {
        'title': 'Shenmue II',
        'filename': 'Shenmue II (Europe) (En,Fr,De,Es) (Disc 2)',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue II (Europe) (En,Fr,De,Es) (Disc 2)',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue II (Europe) (En,Fr,De,Es) (Disc 2)',
        'size': 0,
    },
    {
        'title': 'Shenmue II',
        'filename': 'Shenmue II (Europe) (En,Fr,De,Es) (Disc 3)',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue II (Europe) (En,Fr,De,Es) (Disc 3)',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue II (Europe) (En,Fr,De,Es) (Disc 3)',
        'size': 0,
    },
    {
        'title': 'Shenmue II',
        'filename': 'Shenmue II (Europe) (En,Fr,De,Es) (Disc 4)',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Shenmue II (Europe) (En,Fr,De,Es) (Disc 4)',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Shenmue II (Europe) (En,Fr,De,Es) (Disc 4)',
        'size': 0,
    },
    {
        'title': 'Skies of Arcadia',
        'filename': 'Skies of Arcadia (USA) (Disc 1).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Skies of Arcadia (USA) (Disc 1)/Skies of Arcadia (USA) (Disc 1).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Skies of Arcadia (USA) (Disc 1).gdi',
        'size': 0,
    },
    {
        'title': 'Skies of Arcadia',
        'filename': 'Skies of Arcadia (USA) (Disc 2)',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Skies of Arcadia (USA) (Disc 2)',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Skies of Arcadia (USA) (Disc 2)',
        'size': 0,
    },
    {
        'title': 'Sonic Adventure',
        'filename': 'Sonic Adventure (USA) (En,Ja,Fr,De,Es).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Sonic Adventure (USA) (En,Ja,Fr,De,Es)/Sonic Adventure (USA) (En,Ja,Fr,De,Es).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Sonic Adventure (USA) (En,Ja,Fr,De,Es).gdi',
        'size': 0,
    },
    {
        'title': 'Sonic Adventure 2',
        'filename': 'Sonic Adventure 2 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Sonic Adventure 2 v1.008 (2001)(Sega)(NTSC)(US)(M5)[!]/Sonic Adventure 2 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Sonic Adventure 2 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Soul Calibur',
        'filename': 'Soul Calibur (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Soul Calibur v1.000 (1999)(Namco)(NTSC)(US)[!][4S T-1401N]/Soul Calibur (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Soul Calibur (USA).gdi',
        'size': 0,
    },
    {
        'title': "South Park: Chef's Luv Shack",
        'filename': "South Park - Chef's Luv Shack (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/South Park - Chef's Luv Shack (USA)/South Park - Chef's Luv Shack (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/South Park - Chef's Luv Shack (USA).gdi",
        'size': 0,
    },
    {
        'title': 'Space Channel 5',
        'filename': 'Space Channel 5 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Space Channel 5 (USA)/Space Channel 5 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Space Channel 5 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Star Wars: Episode I: Racer',
        'filename': 'Star Wars - Episode I - Racer (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Star Wars - Episode I - Racer (USA)/Star Wars - Episode I - Racer (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Star Wars - Episode I - Racer (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Street Fighter Alpha 3',
        'filename': 'Street Fighter Alpha 3 (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Street Fighter Alpha 3 (USA)/Street Fighter Alpha 3 (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Street Fighter Alpha 3 (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Street Fighter III: 3rd Strike',
        'filename': 'Street Fighter III - 3rd Strike (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Street Fighter III - 3rd Strike (USA)/Street Fighter III - 3rd Strike (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Street Fighter III - 3rd Strike (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Street Fighter III: Double Impact',
        'filename': 'Street Fighter III - Double Impact (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Street Fighter III - Double Impact (USA)/Street Fighter III - Double Impact (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Street Fighter III - Double Impact (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Surf Rocket Racers',
        'filename': 'Surf Rocket Racers (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Surf Rocket Racers (USA)/Surf Rocket Racers (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Surf Rocket Racers (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Tomb Raider: The Last Revelation',
        'filename': 'Tomb Raider - The Last Revelation (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Tomb Raider - The Last Revelation v1.001 (2000)(EIDOS)(NTSC)(US)[!]/Tomb Raider - The Last Revelation (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Tomb Raider - The Last Revelation (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Tomb Raider Chronicles',
        'filename': 'Tomb Raider Chronicles (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Tomb Raider Chronicles v1.000 (2000)(EIDOS)(NTSC)(US)[!]/Tomb Raider Chronicles (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Tomb Raider Chronicles (USA).gdi',
        'size': 0,
    },
    {
        'title': "Tony Hawk's Pro Skater 2",
        'filename': "Tony Hawk's Pro Skater 2 (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Tony Hawk's Pro Skater 2 v1.001 (2000)(Activision)(NTSC)(US)[!]/Tony Hawk's Pro Skater 2 (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Tony Hawk's Pro Skater 2 (USA).gdi",
        'size': 0,
    },
    {
        'title': "Tony Hawk's Pro Skater",
        'filename': "Tony Hawk's Pro Skater (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Tony Hawk's Pro Skater v1.000 (2000)(Crave)(NTSC)(US)[!]/Tony Hawk's Pro Skater (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Tony Hawk's Pro Skater (USA).gdi",
        'size': 0,
    },
    {
        'title': 'Unreal Tournament',
        'filename': 'Unreal Tournament (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Unreal Tournament (USA)/Unreal Tournament (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Unreal Tournament (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Who Wants To Beat Up A Millionaire',
        'filename': 'Who Wants to Beat Up a Millionaire (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Who Wants to Beat Up a Millionaire (USA)/Who Wants to Beat Up a Millionaire (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Who Wants to Beat Up a Millionaire (USA).gdi',
        'size': 0,
    },
    {
        'title': 'Worms Armageddon',
        'filename': 'Worms Armageddon (USA) (En,Fr,De,Nl,Sv,No,Da).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Worms Armageddon (USA) (En,Fr,De,Nl,Sv,No,Da)/Worms Armageddon (USA) (En,Fr,De,Nl,Sv,No,Da).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Worms Armageddon (USA) (En,Fr,De,Nl,Sv,No,Da).gdi',
        'size': 0,
    },
    {
        'title': 'Worms World Party',
        'filename': 'Worms World Party (USA) (En,Fr,De,Es,It,Nl,Sv,Da).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Worms World Party (USA) (En,Fr,De,Es,It,Nl,Sv,Da)/Worms World Party (USA) (En,Fr,De,Es,It,Nl,Sv,Da).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Worms World Party (USA) (En,Fr,De,Es,It,Nl,Sv,Da).gdi',
        'size': 0,
    },
    {
        'title': "Army Men: Sarge's Heroes",
        'filename': "Army Men - Sarge's Heroes (USA).gdi",
        'source_relative': "Consoles/Sega Dreamcast [1998]/Army Men - Sarge's Heroes (v1.001) (2000)(Midway)(NTSC)(US)[!]/Army Men - Sarge's Heroes (USA).gdi",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Army Men - Sarge's Heroes (USA).gdi",
        'size': 0,
    },
    {
        'title': 'Mortal Kombat Gold',
        'filename': 'Mortal Kombat Gold (USA).gdi',
        'source_relative': 'Consoles/Sega Dreamcast [1998]/Mortal Kombat Gold v1.006 (1999)(Midway)(NTSC)(US)[!][6S T-9701NGD]/Mortal Kombat Gold (USA).gdi',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/dreamcast/Mortal Kombat Gold (USA).gdi',
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