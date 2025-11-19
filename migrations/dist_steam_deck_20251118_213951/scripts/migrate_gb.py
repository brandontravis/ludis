#!/usr/bin/env python3
# Auto-generated migration script for Nintendo Game Boy
# 160 games, 18.38 MB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo Game Boy'
ESDE_FOLDER = 'gb'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'The Addams Family',
        'filename': 'Addams Family, The (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Addams Family, The (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Addams Family, The (USA).7z',
        'size': 93185,
    },
    {
        'title': "The Addams Family: Pugsley's Scavenger Hunt",
        'filename': "Addams Family, The - Pugsley's Scavenger Hunt (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Addams Family, The - Pugsley's Scavenger Hunt (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Addams Family, The - Pugsley's Scavenger Hunt (USA, Europe).7z",
        'size': 92045,
    },
    {
        'title': 'Adventure Island',
        'filename': 'Adventure Island (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Adventure Island (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Adventure Island (USA, Europe).7z',
        'size': 68401,
    },
    {
        'title': 'Adventure Island II: Aliens in Paradise',
        'filename': 'Adventure Island II - Aliens in Paradise (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Adventure Island II - Aliens in Paradise (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Adventure Island II - Aliens in Paradise (USA, Europe).7z',
        'size': 106597,
    },
    {
        'title': 'Adventures of Lolo',
        'filename': 'Adventures of Lolo (Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Adventures of Lolo (Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Adventures of Lolo (Europe) (SGB Enhanced).7z',
        'size': 175557,
    },
    {
        'title': 'Arcade Classic 1: Asteroids / Missile Command',
        'filename': 'Arcade Classic No. 1 - Asteroids & Missile Command (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Arcade Classic No. 1 - Asteroids & Missile Command (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Arcade Classic No. 1 - Asteroids & Missile Command (USA, Europe) (SGB Enhanced).7z',
        'size': 72731,
    },
    {
        'title': 'Arcade Classic 2: Centipede / Millipede',
        'filename': 'Arcade Classic No. 2 - Centipede & Millipede (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Arcade Classic No. 2 - Centipede & Millipede (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Arcade Classic No. 2 - Centipede & Millipede (USA, Europe) (SGB Enhanced).7z',
        'size': 68174,
    },
    {
        'title': 'Arcade Classic No. 3: Galaga & Galaxian',
        'filename': 'Arcade Classic No. 3 - Galaga & Galaxian (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Arcade Classic No. 3 - Galaga & Galaxian (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Arcade Classic No. 3 - Galaga & Galaxian (USA) (SGB Enhanced).7z',
        'size': 39192,
    },
    {
        'title': 'Arcade Classic No. 4: Defender / Joust',
        'filename': 'Arcade Classic No. 4 - Defender & Joust (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Arcade Classic No. 4 - Defender & Joust (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Arcade Classic No. 4 - Defender & Joust (USA, Europe) (SGB Enhanced).7z',
        'size': 71002,
    },
    {
        'title': 'Arcade Classics: Super Breakout / Battlezone',
        'filename': 'Arcade Classics - Super Breakout & Battlezone (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Arcade Classics - Super Breakout & Battlezone (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Arcade Classics - Super Breakout & Battlezone (USA, Europe) (SGB Enhanced).7z',
        'size': 127387,
    },
    {
        'title': 'Balloon Kid',
        'filename': 'Balloon Kid (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Balloon Kid (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Balloon Kid (USA, Europe).7z',
        'size': 66654,
    },
    {
        'title': "Bart Simpson's Escape from Camp Deadly",
        'filename': "Bart Simpson's Escape from Camp Deadly (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Bart Simpson's Escape from Camp Deadly (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bart Simpson's Escape from Camp Deadly (USA, Europe).7z",
        'size': 67637,
    },
    {
        'title': 'Bases Loaded',
        'filename': 'Bases Loaded (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Bases Loaded (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bases Loaded (USA).7z',
        'size': 45367,
    },
    {
        'title': 'Batman: Return of the Joker',
        'filename': 'Batman - Return of the Joker (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Batman - Return of the Joker (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Batman - Return of the Joker (USA, Europe).7z',
        'size': 66113,
    },
    {
        'title': 'Batman: The Animated Series',
        'filename': 'Batman - The Animated Series (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Batman - The Animated Series (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Batman - The Animated Series (USA, Europe).7z',
        'size': 90509,
    },
    {
        'title': 'Batman: The Video Game',
        'filename': 'Batman - The Video Game (World).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Batman - The Video Game (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Batman - The Video Game (World).7z',
        'size': 57083,
    },
    {
        'title': 'Batman Forever',
        'filename': 'Batman Forever (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Batman Forever (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Batman Forever (USA, Europe).7z',
        'size': 132291,
    },
    {
        'title': 'Battletoads',
        'filename': 'Battletoads (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Battletoads (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Battletoads (USA, Europe).7z',
        'size': 108036,
    },
    {
        'title': "Battletoads in Ragnarok's World",
        'filename': "Battletoads in Ragnarok's World (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Battletoads in Ragnarok's World (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Battletoads in Ragnarok's World (USA).7z",
        'size': 101709,
    },
    {
        'title': 'Battletoads / Double Dragon',
        'filename': 'Battletoads-Double Dragon (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Battletoads-Double Dragon (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Battletoads-Double Dragon (USA).7z',
        'size': 165448,
    },
    {
        'title': 'Beavis and Butt-Head',
        'filename': 'Beavis and Butt-head (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Beavis and Butt-head (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Beavis and Butt-head (USA, Europe).7z',
        'size': 322346,
    },
    {
        'title': 'Beetlejuice',
        'filename': 'Beetlejuice (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Beetlejuice (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Beetlejuice (USA).7z',
        'size': 70752,
    },
    {
        'title': 'Bionic Commando',
        'filename': 'Bionic Commando (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Bionic Commando (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bionic Commando (USA).7z',
        'size': 154454,
    },
    {
        'title': 'Bomberman GB',
        'filename': 'Bomberman GB (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Bomberman GB (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bomberman GB (USA, Europe) (SGB Enhanced).7z',
        'size': 115943,
    },
    {
        'title': "Bonk's Adventure",
        'filename': "Bonk's Adventure (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Bonk's Adventure (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bonk's Adventure (USA).7z",
        'size': 84101,
    },
    {
        'title': "Bonk's Revenge",
        'filename': "Bonk's Revenge (USA) (SGB Enhanced).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Bonk's Revenge (USA) (SGB Enhanced).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bonk's Revenge (USA) (SGB Enhanced).7z",
        'size': 122186,
    },
    {
        'title': "Bram Stoker's Dracula",
        'filename': "Bram Stoker's Dracula (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Bram Stoker's Dracula (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bram Stoker's Dracula (USA, Europe).7z",
        'size': 80461,
    },
    {
        'title': 'Bubble Bobble',
        'filename': 'Bubble Bobble (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Bubble Bobble (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bubble Bobble (USA, Europe).7z',
        'size': 57991,
    },
    {
        'title': 'Bubble Bobble Part 2',
        'filename': 'Bubble Bobble Part 2 (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Bubble Bobble Part 2 (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bubble Bobble Part 2 (USA, Europe).7z',
        'size': 62177,
    },
    {
        'title': 'Bubsy II',
        'filename': 'Bubsy II (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Bubsy II (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Bubsy II (USA).7z',
        'size': 104235,
    },
    {
        'title': 'BurgerTime Deluxe',
        'filename': 'BurgerTime Deluxe (World).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/BurgerTime Deluxe (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/BurgerTime Deluxe (World).7z',
        'size': 35169,
    },
    {
        'title': 'Casper',
        'filename': 'Casper (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Casper (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Casper (USA).7z',
        'size': 70077,
    },
    {
        'title': 'Castlevania: The Adventure',
        'filename': 'Castlevania - The Adventure (USA) (Castlevania Anniversary Collection).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Castlevania - The Adventure (USA) (Castlevania Anniversary Collection).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Castlevania - The Adventure (USA) (Castlevania Anniversary Collection).7z',
        'size': 37930,
    },
    {
        'title': 'Castlevania: The Adventure',
        'filename': 'Castlevania - The Adventure (USA) (Castlevania Anniversary Collection).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Castlevania - The Adventure (USA) (Castlevania Anniversary Collection).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Castlevania - The Adventure (USA) (Castlevania Anniversary Collection).7z',
        'size': 37918,
    },
    {
        'title': "Castlevania II: Belmont's Revenge",
        'filename': "Castlevania II - Belmont's Revenge (USA, Europe) (Castlevania Anniversary Collection).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Castlevania II - Belmont's Revenge (USA, Europe) (Castlevania Anniversary Collection).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Castlevania II - Belmont's Revenge (USA, Europe) (Castlevania Anniversary Collection).7z",
        'size': 80710,
    },
    {
        'title': "Castlevania II: Belmont's Revenge",
        'filename': "Castlevania II - Belmont's Revenge (USA, Europe) (Castlevania Anniversary Collection).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Castlevania II - Belmont's Revenge (USA, Europe) (Castlevania Anniversary Collection).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Castlevania II - Belmont's Revenge (USA, Europe) (Castlevania Anniversary Collection).7z",
        'size': 80667,
    },
    {
        'title': 'Castlevania Legends',
        'filename': 'Castlevania Legends (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Castlevania Legends (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Castlevania Legends (USA, Europe) (SGB Enhanced).7z',
        'size': 105501,
    },
    {
        'title': 'Catrap',
        'filename': 'Catrap (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Catrap (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Catrap (USA).7z',
        'size': 21717,
    },
    {
        'title': 'Centipede',
        'filename': 'Centipede (USA) (Majesco).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Centipede (USA) (Majesco).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Centipede (USA) (Majesco).7z',
        'size': 67474,
    },
    {
        'title': 'Chuck Rock',
        'filename': 'Chuck Rock (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Chuck Rock (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Chuck Rock (USA, Europe).7z',
        'size': 92684,
    },
    {
        'title': 'College Slam',
        'filename': 'College Slam (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/College Slam (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/College Slam (USA).7z',
        'size': 242640,
    },
    {
        'title': 'Contra: The Alien Wars',
        'filename': 'Contra - The Alien Wars (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Contra - The Alien Wars (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Contra - The Alien Wars (USA) (SGB Enhanced).7z',
        'size': 87471,
    },
    {
        'title': 'Cool Spot',
        'filename': 'Cool Spot (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Cool Spot (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Cool Spot (USA).7z',
        'size': 82363,
    },
    {
        'title': 'Desert Strike: Return to the Gulf',
        'filename': 'Desert Strike - Return to the Gulf (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Desert Strike - Return to the Gulf (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Desert Strike - Return to the Gulf (USA) (SGB Enhanced).7z',
        'size': 128823,
    },
    {
        'title': 'Dig Dug',
        'filename': 'Dig Dug (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Dig Dug (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Dig Dug (USA).7z',
        'size': 48891,
    },
    {
        'title': 'Donkey Kong',
        'filename': 'Donkey Kong (Japan, USA) (En) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Donkey Kong (Japan, USA) (En) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Donkey Kong (Japan, USA) (En) (SGB Enhanced).7z',
        'size': 236098,
    },
    {
        'title': 'Donkey Kong Land',
        'filename': 'Donkey Kong Land (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Donkey Kong Land (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Donkey Kong Land (USA, Europe) (SGB Enhanced).7z',
        'size': 345828,
    },
    {
        'title': 'Donkey Kong Land 2',
        'filename': 'Donkey Kong Land 2 (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Donkey Kong Land 2 (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Donkey Kong Land 2 (USA, Europe) (SGB Enhanced).7z',
        'size': 370136,
    },
    {
        'title': 'Donkey Kong Land III',
        'filename': 'Donkey Kong Land III (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Donkey Kong Land III (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Donkey Kong Land III (USA, Europe) (SGB Enhanced).7z',
        'size': 366012,
    },
    {
        'title': 'Double Dragon',
        'filename': 'Double Dragon (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Double Dragon (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Double Dragon (USA, Europe).7z',
        'size': 61080,
    },
    {
        'title': 'Double Dragon 3: The Arcade Game',
        'filename': 'Double Dragon 3 - The Arcade Game (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Double Dragon 3 - The Arcade Game (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Double Dragon 3 - The Arcade Game (USA, Europe).7z',
        'size': 68253,
    },
    {
        'title': 'Double Dragon II',
        'filename': 'Double Dragon II (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Double Dragon II (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Double Dragon II (USA, Europe).7z',
        'size': 63040,
    },
    {
        'title': 'Dr. Mario',
        'filename': 'Dr. Mario (World) (Rev 1).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Dr. Mario (World) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Dr. Mario (World) (Rev 1).7z',
        'size': 19010,
    },
    {
        'title': "Dragon's Lair: The Legend",
        'filename': "Dragon's Lair - The Legend (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Dragon's Lair - The Legend (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Dragon's Lair - The Legend (USA).7z",
        'size': 76934,
    },
    {
        'title': 'DuckTales',
        'filename': 'DuckTales (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/DuckTales (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/DuckTales (USA).7z',
        'size': 42650,
    },
    {
        'title': 'DuckTales 2',
        'filename': 'DuckTales 2 (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/DuckTales 2 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/DuckTales 2 (USA).7z',
        'size': 74412,
    },
    {
        'title': 'Earthworm Jim',
        'filename': 'Earthworm Jim (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Earthworm Jim (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Earthworm Jim (USA).7z',
        'size': 148254,
    },
    {
        'title': 'Felix the Cat',
        'filename': 'Felix the Cat (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Felix the Cat (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Felix the Cat (USA, Europe).7z',
        'size': 54790,
    },
    {
        'title': 'Final Fantasy Adventure',
        'filename': 'Final Fantasy Adventure (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Final Fantasy Adventure (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Final Fantasy Adventure (USA).7z',
        'size': 141867,
    },
    {
        'title': 'Final Fantasy Legend II',
        'filename': 'Final Fantasy Legend II (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Final Fantasy Legend II (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Final Fantasy Legend II (USA).7z',
        'size': 161681,
    },
    {
        'title': 'Final Fantasy Legend III',
        'filename': 'Final Fantasy Legend III (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Final Fantasy Legend III (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Final Fantasy Legend III (USA).7z',
        'size': 174287,
    },
    {
        'title': 'The Final Fantasy Legend',
        'filename': 'Final Fantasy Legend, The (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Final Fantasy Legend, The (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Final Fantasy Legend, The (USA).7z',
        'size': 86925,
    },
    {
        'title': 'Frogger',
        'filename': 'Frogger (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Frogger (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Frogger (USA).7z',
        'size': 19017,
    },
    {
        'title': 'Game & Watch Gallery',
        'filename': 'Game & Watch Gallery (USA) (Rev 1) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Game & Watch Gallery (USA) (Rev 1) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Game & Watch Gallery (USA) (Rev 1) (SGB Enhanced).7z',
        'size': 159866,
    },
    {
        'title': "Gargoyle's Quest",
        'filename': "Gargoyle's Quest (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Gargoyle's Quest (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Gargoyle's Quest (USA, Europe).7z",
        'size': 78779,
    },
    {
        'title': 'Gauntlet II',
        'filename': 'Gauntlet II (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Gauntlet II (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Gauntlet II (USA, Europe).7z',
        'size': 124221,
    },
    {
        'title': 'Ghostbusters II',
        'filename': 'Ghostbusters II (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Ghostbusters II (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Ghostbusters II (USA, Europe).7z',
        'size': 63260,
    },
    {
        'title': 'Harvest Moon GB',
        'filename': 'Harvest Moon GB (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Harvest Moon GB (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Harvest Moon GB (USA) (SGB Enhanced).7z',
        'size': 221716,
    },
    {
        'title': 'Home Alone',
        'filename': 'Home Alone (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Home Alone (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Home Alone (USA, Europe).7z',
        'size': 67135,
    },
    {
        'title': 'Home Alone 2: Lost in New York',
        'filename': 'Home Alone 2 - Lost in New York (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Home Alone 2 - Lost in New York (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Home Alone 2 - Lost in New York (USA, Europe).7z',
        'size': 77431,
    },
    {
        'title': 'Hook',
        'filename': 'Hook (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Hook (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Hook (USA).7z',
        'size': 100197,
    },
    {
        'title': 'James Bond 007',
        'filename': 'James Bond 007 (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/James Bond 007 (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/James Bond 007 (USA, Europe) (SGB Enhanced).7z',
        'size': 186362,
    },
    {
        'title': 'Joe & Mac',
        'filename': 'Joe & Mac (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Joe & Mac (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Joe & Mac (USA).7z',
        'size': 178464,
    },
    {
        'title': 'Jungle Strike',
        'filename': 'Jungle Strike (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Jungle Strike (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Jungle Strike (USA).7z',
        'size': 132074,
    },
    {
        'title': 'Jurassic Park',
        'filename': 'Jurassic Park (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Jurassic Park (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Jurassic Park (USA).7z',
        'size': 153572,
    },
    {
        'title': 'Jurassic Park Part 2: The Chaos Continues',
        'filename': 'Jurassic Park Part 2 - The Chaos Continues (USA, Europe) (En,Fr,De,It).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Jurassic Park Part 2 - The Chaos Continues (USA, Europe) (En,Fr,De,It).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Jurassic Park Part 2 - The Chaos Continues (USA, Europe) (En,Fr,De,It).7z',
        'size': 106187,
    },
    {
        'title': 'Kid Dracula',
        'filename': 'Kid Dracula (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Kid Dracula (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kid Dracula (USA, Europe).7z',
        'size': 163069,
    },
    {
        'title': 'Kid Icarus: Of Myths and Monsters',
        'filename': 'Kid Icarus - Of Myths and Monsters (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Kid Icarus - Of Myths and Monsters (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kid Icarus - Of Myths and Monsters (USA, Europe).7z',
        'size': 58261,
    },
    {
        'title': "Kirby's Block Ball",
        'filename': "Kirby's Block Ball (USA, Europe) (SGB Enhanced).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Kirby's Block Ball (USA, Europe) (SGB Enhanced).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kirby's Block Ball (USA, Europe) (SGB Enhanced).7z",
        'size': 197840,
    },
    {
        'title': "Kirby's Dream Land",
        'filename': "Kirby's Dream Land (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Kirby's Dream Land (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kirby's Dream Land (USA, Europe).7z",
        'size': 103985,
    },
    {
        'title': "Kirby's Dream Land 2",
        'filename': "Kirby's Dream Land 2 (USA, Europe) (SGB Enhanced).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Kirby's Dream Land 2 (USA, Europe) (SGB Enhanced).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kirby's Dream Land 2 (USA, Europe) (SGB Enhanced).7z",
        'size': 295338,
    },
    {
        'title': "Kirby's Pinball Land",
        'filename': "Kirby's Pinball Land (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Kirby's Pinball Land (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kirby's Pinball Land (USA, Europe).7z",
        'size': 103909,
    },
    {
        'title': "Kirby's Star Stacker",
        'filename': "Kirby's Star Stacker (USA, Europe) (SGB Enhanced).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Kirby's Star Stacker (USA, Europe) (SGB Enhanced).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Kirby's Star Stacker (USA, Europe) (SGB Enhanced).7z",
        'size': 157034,
    },
    {
        'title': "Krusty's Fun House",
        'filename': "Krusty's Fun House (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Krusty's Fun House (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Krusty's Fun House (USA, Europe).7z",
        'size': 87447,
    },
    {
        'title': "The Legend of Zelda: Link's Awakening",
        'filename': "Legend of Zelda, The - Link's Awakening (USA, Europe) (Rev 2).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Legend of Zelda, The - Link's Awakening (USA, Europe) (Rev 2).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Legend of Zelda, The - Link's Awakening (USA, Europe) (Rev 2).7z",
        'size': 259020,
    },
    {
        'title': 'Lemmings',
        'filename': 'Lemmings (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Lemmings (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Lemmings (USA).7z',
        'size': 107352,
    },
    {
        'title': 'Lemmings 2: The Tribes',
        'filename': 'Lemmings 2 - The Tribes (Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Lemmings 2 - The Tribes (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Lemmings 2 - The Tribes (Europe).7z',
        'size': 221817,
    },
    {
        'title': 'Lost World, The: Jurassic Park',
        'filename': 'Lost World, The - Jurassic Park (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Lost World, The - Jurassic Park (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Lost World, The - Jurassic Park (USA, Europe) (SGB Enhanced).7z',
        'size': 261788,
    },
    {
        'title': 'Marble Madness',
        'filename': 'Marble Madness (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Marble Madness (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Marble Madness (USA, Europe).7z',
        'size': 76718,
    },
    {
        'title': "Mario's Picross",
        'filename': "Mario's Picross (USA, Europe) (SGB Enhanced).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Mario's Picross (USA, Europe) (SGB Enhanced).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mario's Picross (USA, Europe) (SGB Enhanced).7z",
        'size': 64809,
    },
    {
        'title': 'McDonaldland',
        'filename': 'McDonaldland (Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/McDonaldland (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/McDonaldland (Europe).7z',
        'size': 80380,
    },
    {
        'title': "Mega Man: Dr. Wily's Revenge",
        'filename': "Mega Man - Dr. Wily's Revenge (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Mega Man - Dr. Wily's Revenge (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mega Man - Dr. Wily's Revenge (USA).7z",
        'size': 91690,
    },
    {
        'title': 'Mega Man II',
        'filename': 'Mega Man II (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mega Man II (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mega Man II (USA).7z',
        'size': 78077,
    },
    {
        'title': 'Mega Man III',
        'filename': 'Mega Man III (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mega Man III (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mega Man III (USA).7z',
        'size': 136859,
    },
    {
        'title': 'Mega Man IV',
        'filename': 'Mega Man IV (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mega Man IV (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mega Man IV (USA).7z',
        'size': 240817,
    },
    {
        'title': 'Mega Man V',
        'filename': 'Mega Man V (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mega Man V (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mega Man V (USA) (SGB Enhanced).7z',
        'size': 247853,
    },
    {
        'title': 'Metroid II: Return of Samus',
        'filename': 'Metroid II - Return of Samus (World).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Metroid II - Return of Samus (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Metroid II - Return of Samus (World).7z',
        'size': 95965,
    },
    {
        'title': 'Mole Mania',
        'filename': 'Mole Mania (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mole Mania (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mole Mania (USA, Europe) (SGB Enhanced).7z',
        'size': 197027,
    },
    {
        'title': 'Mortal Kombat & Mortal Kombat II',
        'filename': 'Mortal Kombat & Mortal Kombat II (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mortal Kombat & Mortal Kombat II (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mortal Kombat & Mortal Kombat II (USA, Europe).7z',
        'size': 289409,
    },
    {
        'title': 'Mortal Kombat',
        'filename': 'Mortal Kombat (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mortal Kombat (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mortal Kombat (USA, Europe).7z',
        'size': 137142,
    },
    {
        'title': 'Mortal Kombat 3',
        'filename': 'Mortal Kombat 3 (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mortal Kombat 3 (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mortal Kombat 3 (USA, Europe).7z',
        'size': 193382,
    },
    {
        'title': 'Mortal Kombat II',
        'filename': 'Mortal Kombat II (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Mortal Kombat II (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Mortal Kombat II (USA, Europe).7z',
        'size': 151302,
    },
    {
        'title': 'Motocross Maniacs',
        'filename': 'Motocross Maniacs (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Motocross Maniacs (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Motocross Maniacs (USA).7z',
        'size': 22209,
    },
    {
        'title': 'NBA Jam',
        'filename': 'NBA Jam (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/NBA Jam (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/NBA Jam (USA, Europe).7z',
        'size': 112550,
    },
    {
        'title': 'NBA Jam: Tournament Edition',
        'filename': 'NBA Jam - Tournament Edition (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/NBA Jam - Tournament Edition (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/NBA Jam - Tournament Edition (USA, Europe).7z',
        'size': 240995,
    },
    {
        'title': 'Ninja Gaiden Shadow',
        'filename': 'Ninja Gaiden Shadow (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Ninja Gaiden Shadow (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Ninja Gaiden Shadow (USA).7z',
        'size': 77568,
    },
    {
        'title': 'Oddworld Adventures',
        'filename': 'Oddworld Adventures (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Oddworld Adventures (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Oddworld Adventures (USA, Europe).7z',
        'size': 96240,
    },
    {
        'title': 'Operation C',
        'filename': 'Operation C (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Operation C (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Operation C (USA).7z',
        'size': 78882,
    },
    {
        'title': 'Pac-Attack',
        'filename': 'Pac-Attack (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pac-Attack (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pac-Attack (USA) (SGB Enhanced).7z',
        'size': 34675,
    },
    {
        'title': 'Pac-in-Time',
        'filename': 'Pac-In-Time (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pac-In-Time (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pac-In-Time (USA) (SGB Enhanced).7z',
        'size': 178097,
    },
    {
        'title': 'Pac-Man',
        'filename': 'Pac-Man (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pac-Man (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pac-Man (USA).7z',
        'size': 16819,
    },
    {
        'title': 'The Pagemaster',
        'filename': 'Pagemaster, The (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pagemaster, The (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pagemaster, The (USA) (SGB Enhanced).7z',
        'size': 152922,
    },
    {
        'title': 'Paperboy',
        'filename': 'Paperboy (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Paperboy (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Paperboy (USA, Europe).7z',
        'size': 22924,
    },
    {
        'title': 'Paperboy 2',
        'filename': 'Paperboy 2 (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Paperboy 2 (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Paperboy 2 (USA, Europe).7z',
        'size': 81877,
    },
    {
        'title': "Pinball: Revenge of the 'Gator",
        'filename': "Pinball - Revenge of the 'Gator (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Pinball - Revenge of the 'Gator (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pinball - Revenge of the 'Gator (USA, Europe).7z",
        'size': 47910,
    },
    {
        'title': 'Pocket Bomberman',
        'filename': 'Pocket Bomberman (Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pocket Bomberman (Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pocket Bomberman (Europe) (SGB Enhanced).7z',
        'size': 138051,
    },
    {
        'title': 'Pokémon Blue Version',
        'filename': 'Pokemon - Blue Version (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pokemon - Blue Version (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pokemon - Blue Version (USA, Europe) (SGB Enhanced).7z',
        'size': 330753,
    },
    {
        'title': 'Pokémon Red Version',
        'filename': 'Pokemon - Red Version (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pokemon - Red Version (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pokemon - Red Version (USA, Europe) (SGB Enhanced).7z',
        'size': 330876,
    },
    {
        'title': 'Pokemon: Yellow Version: Special Pikachu Edition',
        'filename': 'Pokemon - Yellow Version - Special Pikachu Edition (USA, Europe) (CGB+SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Pokemon - Yellow Version - Special Pikachu Edition (USA, Europe) (CGB+SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Pokemon - Yellow Version - Special Pikachu Edition (USA, Europe) (CGB+SGB Enhanced).7z',
        'size': 450565,
    },
    {
        'title': 'Primal Rage',
        'filename': 'Primal Rage (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Primal Rage (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Primal Rage (USA, Europe).7z',
        'size': 166780,
    },
    {
        'title': 'Prince of Persia',
        'filename': 'Prince of Persia (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Prince of Persia (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Prince of Persia (USA).7z',
        'size': 58624,
    },
    {
        'title': 'Qix',
        'filename': 'QIX (World).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/QIX (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/QIX (World).7z',
        'size': 34984,
    },
    {
        'title': 'Quarth',
        'filename': 'Quarth (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Quarth (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Quarth (USA, Europe).7z',
        'size': 31888,
    },
    {
        'title': 'R-Type II',
        'filename': 'R-Type II (Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/R-Type II (Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/R-Type II (Europe).7z',
        'size': 65910,
    },
    {
        'title': 'The Real Ghostbusters',
        'filename': 'Real Ghostbusters, The (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Real Ghostbusters, The (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Real Ghostbusters, The (USA).7z',
        'size': 76508,
    },
    {
        'title': 'The Simpsons: Bart & the Beanstalk',
        'filename': 'Simpsons, The - Bart & the Beanstalk (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Simpsons, The - Bart & the Beanstalk (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Simpsons, The - Bart & the Beanstalk (USA, Europe).7z',
        'size': 59937,
    },
    {
        'title': 'The Simpsons: Bart vs. the Juggernauts',
        'filename': 'Simpsons, The - Bart vs. the Juggernauts (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Simpsons, The - Bart vs. the Juggernauts (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Simpsons, The - Bart vs. the Juggernauts (USA, Europe).7z',
        'size': 83733,
    },
    {
        'title': 'The Simpsons: Itchy & Scratchy in Miniature Golf Madness',
        'filename': 'Simpsons, The - Itchy & Scratchy - Miniature Golf Madness (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Simpsons, The - Itchy & Scratchy - Miniature Golf Madness (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Simpsons, The - Itchy & Scratchy - Miniature Golf Madness (USA, Europe).7z',
        'size': 90192,
    },
    {
        'title': 'Sonic 6',
        'filename': 'Sonic 6 (USA) (Pirate).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Sonic 6 (USA) (Pirate).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Sonic 6 (USA) (Pirate).7z',
        'size': 170745,
    },
    {
        'title': 'Space Invaders',
        'filename': 'Space Invaders (USA) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Space Invaders (USA) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Space Invaders (USA) (SGB Enhanced).7z',
        'size': 189564,
    },
    {
        'title': "Spider-Man & X-Men: Arcade's Revenge",
        'filename': "Spider-Man - X-Men - Arcade's Revenge (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Spider-Man - X-Men - Arcade's Revenge (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Spider-Man - X-Men - Arcade's Revenge (USA, Europe).7z",
        'size': 72537,
    },
    {
        'title': 'Star Wars',
        'filename': 'Star Wars (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Star Wars (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Star Wars (USA).7z',
        'size': 72848,
    },
    {
        'title': 'Star Wars: The Empire Strikes Back',
        'filename': 'Star Wars - The Empire Strikes Back (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Star Wars - The Empire Strikes Back (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Star Wars - The Empire Strikes Back (USA).7z',
        'size': 85101,
    },
    {
        'title': 'Stargate',
        'filename': 'Stargate (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Stargate (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Stargate (USA, Europe).7z',
        'size': 66459,
    },
    {
        'title': 'Street Fighter II',
        'filename': 'Street Fighter II (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Street Fighter II (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Street Fighter II (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'size': 263742,
    },
    {
        'title': 'Super Mario 4',
        'filename': 'Super Mario 4 (Unknown) (Ja) (Pirate).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Super Mario 4 (Unknown) (Ja) (Pirate).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Super Mario 4 (Unknown) (Ja) (Pirate).7z',
        'size': 72543,
    },
    {
        'title': 'Super Mario Land',
        'filename': 'Super Mario Land (World) (Rev 1).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Super Mario Land (World) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Super Mario Land (World) (Rev 1).7z',
        'size': 34101,
    },
    {
        'title': 'Super Mario Land 2: 6 Golden Coins',
        'filename': 'Super Mario Land 2 - 6 Golden Coins (USA, Europe) (Rev 2).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Super Mario Land 2 - 6 Golden Coins (USA, Europe) (Rev 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Super Mario Land 2 - 6 Golden Coins (USA, Europe) (Rev 2).7z',
        'size': 253932,
    },
    {
        'title': 'Super R.C. Pro-AM',
        'filename': 'Super R.C. Pro-Am (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Super R.C. Pro-Am (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Super R.C. Pro-Am (USA, Europe).7z',
        'size': 77067,
    },
    {
        'title': 'Super Star Wars: Return of the Jedi',
        'filename': 'Super Star Wars - Return of the Jedi (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Super Star Wars - Return of the Jedi (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Super Star Wars - Return of the Jedi (USA, Europe) (SGB Enhanced).7z',
        'size': 211889,
    },
    {
        'title': 'TaleSpin',
        'filename': 'TaleSpin (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/TaleSpin (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/TaleSpin (USA).7z',
        'size': 61069,
    },
    {
        'title': 'Tecmo Bowl',
        'filename': 'Tecmo Bowl (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Tecmo Bowl (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Tecmo Bowl (USA).7z',
        'size': 115479,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles: Fall of the Foot Clan',
        'filename': 'Teenage Mutant Ninja Turtles - Fall of the Foot Clan (USA) (Cowabunga Collection, The).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Teenage Mutant Ninja Turtles - Fall of the Foot Clan (USA) (Cowabunga Collection, The).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Teenage Mutant Ninja Turtles - Fall of the Foot Clan (USA) (Cowabunga Collection, The).7z',
        'size': 76337,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles II: Back from the Sewers',
        'filename': 'Teenage Mutant Ninja Turtles II - Back from the Sewers (USA) (Cowabunga Collection, The).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Teenage Mutant Ninja Turtles II - Back from the Sewers (USA) (Cowabunga Collection, The).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Teenage Mutant Ninja Turtles II - Back from the Sewers (USA) (Cowabunga Collection, The).7z',
        'size': 144669,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles III: Radical Rescue',
        'filename': 'Teenage Mutant Ninja Turtles III - Radical Rescue (USA) (Cowabunga Collection, The).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Teenage Mutant Ninja Turtles III - Radical Rescue (USA) (Cowabunga Collection, The).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Teenage Mutant Ninja Turtles III - Radical Rescue (USA) (Cowabunga Collection, The).7z',
        'size': 91312,
    },
    {
        'title': 'Tetris',
        'filename': 'Tetris (World) (Rev 1).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Tetris (World) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Tetris (World) (Rev 1).7z',
        'size': 17727,
    },
    {
        'title': 'Tetris 2',
        'filename': 'Tetris 2 (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Tetris 2 (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Tetris 2 (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'size': 51005,
    },
    {
        'title': 'Tetris Attack',
        'filename': 'Tetris Attack (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Tetris Attack (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Tetris Attack (USA, Europe) (Rev 1) (SGB Enhanced).7z',
        'size': 160762,
    },
    {
        'title': "Tiny Toon Adventures: Babs' Big Break",
        'filename': "Tiny Toon Adventures - Babs' Big Break (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Tiny Toon Adventures - Babs' Big Break (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Tiny Toon Adventures - Babs' Big Break (USA, Europe).7z",
        'size': 97117,
    },
    {
        'title': 'Tiny Toon Adventures: Wacky Sports',
        'filename': 'Tiny Toon Adventures - Wacky Sports (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Tiny Toon Adventures - Wacky Sports (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Tiny Toon Adventures - Wacky Sports (USA).7z',
        'size': 86787,
    },
    {
        'title': 'Top Gun: Guts & Glory',
        'filename': 'Top Gun - Guts & Glory (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Top Gun - Guts & Glory (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Top Gun - Guts & Glory (USA, Europe).7z',
        'size': 51270,
    },
    {
        'title': 'Turok: Battle of the Bionosaurs',
        'filename': 'Turok - Battle of the Bionosaurs (USA, Europe) (En,Fr,De,Es).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Turok - Battle of the Bionosaurs (USA, Europe) (En,Fr,De,Es).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Turok - Battle of the Bionosaurs (USA, Europe) (En,Fr,De,Es).7z',
        'size': 146691,
    },
    {
        'title': 'Ultima: Runes of Virtue',
        'filename': 'Ultima - Runes of Virtue (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Ultima - Runes of Virtue (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Ultima - Runes of Virtue (USA).7z',
        'size': 85937,
    },
    {
        'title': 'Ultima: Runes of Virtue II',
        'filename': 'Ultima - Runes of Virtue II (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Ultima - Runes of Virtue II (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Ultima - Runes of Virtue II (USA).7z',
        'size': 159592,
    },
    {
        'title': 'Wario Blast featuring Bomberman!',
        'filename': 'Wario Blast Featuring Bomberman! (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Wario Blast Featuring Bomberman! (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Wario Blast Featuring Bomberman! (USA, Europe) (SGB Enhanced).7z',
        'size': 69964,
    },
    {
        'title': 'Wario Land: Super Mario Land 3',
        'filename': 'Wario Land - Super Mario Land 3 (World).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Wario Land - Super Mario Land 3 (World).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Wario Land - Super Mario Land 3 (World).7z',
        'size': 242154,
    },
    {
        'title': 'Wario Land II',
        'filename': 'Wario Land II (USA, Europe) (SGB Enhanced).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Wario Land II (USA, Europe) (SGB Enhanced).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Wario Land II (USA, Europe) (SGB Enhanced).7z',
        'size': 342864,
    },
    {
        'title': 'Wave Race',
        'filename': 'Wave Race (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Wave Race (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Wave Race (USA, Europe).7z',
        'size': 63797,
    },
    {
        'title': 'Yoshi',
        'filename': 'Yoshi (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy [1989]/Yoshi (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Yoshi (USA).7z',
        'size': 29068,
    },
    {
        'title': "Yoshi's Cookie",
        'filename': "Yoshi's Cookie (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy [1989]/Yoshi's Cookie (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gb/Yoshi's Cookie (USA, Europe).7z",
        'size': 54105,
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