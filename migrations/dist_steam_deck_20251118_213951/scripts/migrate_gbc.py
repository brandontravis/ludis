#!/usr/bin/env python3
# Auto-generated migration script for Nintendo Game Boy Color
# 121 games, 57.27 MB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo Game Boy Color'
ESDE_FOLDER = 'gbc'
OPERATION = 'copy'

GAMES = [
    {
        'title': '720 Degrees',
        'filename': '720 Degrees (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/720 Degrees (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/720 Degrees (USA, Europe) (GB Compatible).7z',
        'size': 124006,
    },
    {
        'title': 'Aladdin',
        'filename': 'Aladdin (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Aladdin (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Aladdin (USA).7z',
        'size': 286971,
    },
    {
        'title': 'Asteroids',
        'filename': 'Asteroids (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Asteroids (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Asteroids (USA, Europe) (GB Compatible).7z',
        'size': 278971,
    },
    {
        'title': 'Batman: Chaos in Gotham',
        'filename': 'Batman - Chaos in Gotham (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Batman - Chaos in Gotham (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Batman - Chaos in Gotham (USA).7z',
        'size': 317407,
    },
    {
        'title': 'Batman Beyond: Return of the Joker',
        'filename': 'Batman Beyond - Return of the Joker (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Batman Beyond - Return of the Joker (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Batman Beyond - Return of the Joker (USA).7z',
        'size': 302338,
    },
    {
        'title': 'Bionic Commando: Elite Forces',
        'filename': 'Bionic Commando - Elite Forces (USA, Australia).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Bionic Commando - Elite Forces (USA, Australia).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Bionic Commando - Elite Forces (USA, Australia).7z',
        'size': 826561,
    },
    {
        'title': 'Boarder Zone',
        'filename': 'Boarder Zone (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Boarder Zone (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Boarder Zone (USA).7z',
        'size': 404920,
    },
    {
        'title': 'Casper',
        'filename': 'Casper (USA) (Rev 1) (Proto).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Casper (USA) (Rev 1) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Casper (USA) (Rev 1) (Proto).7z',
        'size': 270800,
    },
    {
        'title': 'Classic Bubble Bobble',
        'filename': 'Classic Bubble Bobble (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Classic Bubble Bobble (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Classic Bubble Bobble (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 100836,
    },
    {
        'title': 'Croc',
        'filename': 'Croc (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Croc (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Croc (USA, Europe).7z',
        'size': 332589,
    },
    {
        'title': 'Croc 2',
        'filename': 'Croc 2 (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Croc 2 (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Croc 2 (USA, Europe).7z',
        'size': 291609,
    },
    {
        'title': 'Crystalis',
        'filename': 'Crystalis (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Crystalis (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Crystalis (USA).7z',
        'size': 547804,
    },
    {
        'title': 'Dave Mirra Freestyle BMX',
        'filename': 'Dave Mirra Freestyle BMX (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Dave Mirra Freestyle BMX (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dave Mirra Freestyle BMX (USA, Europe).7z',
        'size': 400394,
    },
    {
        'title': 'Deja Vu I & II: The Casebooks of Ace Harding',
        'filename': 'Deja Vu I & II - The Casebooks of Ace Harding (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Deja Vu I & II - The Casebooks of Ace Harding (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Deja Vu I & II - The Casebooks of Ace Harding (USA).7z',
        'size': 366018,
    },
    {
        'title': 'Donkey Kong Country',
        'filename': 'Donkey Kong Country (USA, Europe) (En,Fr,De,Es,It).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Donkey Kong Country (USA, Europe) (En,Fr,De,Es,It).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Donkey Kong Country (USA, Europe) (En,Fr,De,Es,It).7z',
        'size': 1028465,
    },
    {
        'title': "Doug's Big Game",
        'filename': "Doug's Big Game (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Doug's Big Game (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Doug's Big Game (USA).7z",
        'size': 284370,
    },
    {
        'title': 'Dragon Ball Z: Legendary Super Warriors',
        'filename': 'Dragon Ball Z - Legendary Super Warriors (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Dragon Ball Z - Legendary Super Warriors (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dragon Ball Z - Legendary Super Warriors (USA).7z',
        'size': 551206,
    },
    {
        'title': 'Dragon Warrior I & II',
        'filename': 'Dragon Warrior I & II (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Dragon Warrior I & II (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dragon Warrior I & II (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 425917,
    },
    {
        'title': 'Dragon Warrior III',
        'filename': 'Dragon Warrior III (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Dragon Warrior III (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dragon Warrior III (USA).7z',
        'size': 1589952,
    },
    {
        'title': 'Dragon Warrior Monsters',
        'filename': 'Dragon Warrior Monsters (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Dragon Warrior Monsters (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dragon Warrior Monsters (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 666520,
    },
    {
        'title': "Dragon Warrior Monsters 2: Cobi's Journey",
        'filename': "Dragon Warrior Monsters 2 - Cobi's Journey (USA) (SGB Enhanced) (GB Compatible).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Dragon Warrior Monsters 2 - Cobi's Journey (USA) (SGB Enhanced) (GB Compatible).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dragon Warrior Monsters 2 - Cobi's Journey (USA) (SGB Enhanced) (GB Compatible).7z",
        'size': 1033809,
    },
    {
        'title': "Dragon Warrior Monsters 2: Tara's Adventure",
        'filename': "Dragon Warrior Monsters 2 - Tara's Adventure (USA) (SGB Enhanced) (GB Compatible).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Dragon Warrior Monsters 2 - Tara's Adventure (USA) (SGB Enhanced) (GB Compatible).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Dragon Warrior Monsters 2 - Tara's Adventure (USA) (SGB Enhanced) (GB Compatible).7z",
        'size': 1033858,
    },
    {
        'title': 'Duke Nukem',
        'filename': 'Duke Nukem (USA) (En,Fr,De,Es,It).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Duke Nukem (USA) (En,Fr,De,Es,It).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Duke Nukem (USA) (En,Fr,De,Es,It).7z',
        'size': 539086,
    },
    {
        'title': 'Earthworm Jim: Menace 2 the Galaxy',
        'filename': 'Earthworm Jim - Menace 2 the Galaxy (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Earthworm Jim - Menace 2 the Galaxy (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Earthworm Jim - Menace 2 the Galaxy (USA, Europe) (GB Compatible).7z',
        'size': 241166,
    },
    {
        'title': "The Emperor's New Groove",
        'filename': "Emperor's New Groove, The (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Emperor's New Groove, The (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Emperor's New Groove, The (USA).7z",
        'size': 276566,
    },
    {
        'title': 'Extreme Ghostbusters',
        'filename': 'Extreme Ghostbusters (Europe) (En,Fr,De,Es,It,Pt).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Extreme Ghostbusters (Europe) (En,Fr,De,Es,It,Pt).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Extreme Ghostbusters (Europe) (En,Fr,De,Es,It,Pt).7z',
        'size': 199600,
    },
    {
        'title': 'Frogger',
        'filename': 'Frogger (USA) (Rev 2) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Frogger (USA) (Rev 2) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Frogger (USA) (Rev 2) (GB Compatible).7z',
        'size': 26551,
    },
    {
        'title': "Frogger 2: Swampy's Revenge",
        'filename': 'Frogger 2 (USA) (Rev 1).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Frogger 2 (USA) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Frogger 2 (USA) (Rev 1).7z',
        'size': 103372,
    },
    {
        'title': 'Galaga: Destination Earth',
        'filename': 'Galaga - Destination Earth (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Galaga - Destination Earth (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Galaga - Destination Earth (USA).7z',
        'size': 128240,
    },
    {
        'title': 'Game & Watch Gallery 2',
        'filename': 'Game & Watch Gallery 2 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Game & Watch Gallery 2 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Game & Watch Gallery 2 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 333069,
    },
    {
        'title': 'Game & Watch Gallery 3',
        'filename': 'Game & Watch Gallery 3 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Game & Watch Gallery 3 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Game & Watch Gallery 3 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 388058,
    },
    {
        'title': 'Gex: Enter the Gecko',
        'filename': 'Gex - Enter the Gecko (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Gex - Enter the Gecko (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Gex - Enter the Gecko (USA, Europe) (GB Compatible).7z',
        'size': 206768,
    },
    {
        'title': 'Gex 3: Deep Pocket Gecko',
        'filename': 'Gex 3 - Deep Pocket Gecko (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Gex 3 - Deep Pocket Gecko (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Gex 3 - Deep Pocket Gecko (USA).7z',
        'size': 387278,
    },
    {
        'title': 'Grand Theft Auto',
        'filename': 'Grand Theft Auto (USA) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Grand Theft Auto (USA) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Grand Theft Auto (USA) (GB Compatible).7z',
        'size': 1017288,
    },
    {
        'title': 'Grand Theft Auto 2',
        'filename': 'Grand Theft Auto 2 (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Grand Theft Auto 2 (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Grand Theft Auto 2 (USA).7z',
        'size': 559494,
    },
    {
        'title': 'HamTaro: Ham-Hams Unite!',
        'filename': 'Hamtaro - Ham-Hams Unite! (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Hamtaro - Ham-Hams Unite! (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Hamtaro - Ham-Hams Unite! (USA).7z',
        'size': 791179,
    },
    {
        'title': 'Harry Potter 3 & the Mystical Halo',
        'filename': 'Harry Potter 3 (USA) (Unl).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Harry Potter 3 (USA) (Unl).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Harry Potter 3 (USA) (Unl).7z',
        'size': 179903,
    },
    {
        'title': 'Harry Potter and the Chamber of Secrets',
        'filename': 'Harry Potter and the Chamber of Secrets (USA, Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,Da).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Harry Potter and the Chamber of Secrets (USA, Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,Da).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Harry Potter and the Chamber of Secrets (USA, Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,Da).7z',
        'size': 2534555,
    },
    {
        'title': "Harry Potter and the Sorcerer's Stone",
        'filename': "Harry Potter and the Sorcerer's Stone (USA, Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Harry Potter and the Sorcerer's Stone (USA, Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Harry Potter and the Sorcerer's Stone (USA, Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z",
        'size': 2384822,
    },
    {
        'title': 'Harvest Moon 2 GBC',
        'filename': 'Harvest Moon 2 GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Harvest Moon 2 GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Harvest Moon 2 GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 352862,
    },
    {
        'title': 'Harvest Moon 3 GBC',
        'filename': 'Harvest Moon 3 GBC (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Harvest Moon 3 GBC (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Harvest Moon 3 GBC (USA).7z',
        'size': 477417,
    },
    {
        'title': 'Harvest Moon GBC',
        'filename': 'Harvest Moon GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Harvest Moon GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Harvest Moon GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 311141,
    },
    {
        'title': 'Hugo: Black Diamond Fever',
        'filename': 'Hugo - Black Diamond Fever (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Hugo - Black Diamond Fever (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Hugo - Black Diamond Fever (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z',
        'size': 217610,
    },
    {
        'title': 'Hugo: The Evil Mirror',
        'filename': 'Hugo - The Evil Mirror (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Hugo - The Evil Mirror (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Hugo - The Evil Mirror (Europe) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi).7z',
        'size': 317930,
    },
    {
        'title': "Kirby Tilt 'n' Tumble",
        'filename': "Kirby - Tilt 'n' Tumble (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Kirby - Tilt 'n' Tumble (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Kirby - Tilt 'n' Tumble (USA).7z",
        'size': 315503,
    },
    {
        'title': 'Konami GB Collection: Vol.1',
        'filename': 'Konami GB Collection Vol.1 (Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Konami GB Collection Vol.1 (Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Konami GB Collection Vol.1 (Europe) (GB Compatible).7z',
        'size': 304175,
    },
    {
        'title': 'Konami GB Collection: Vol.2',
        'filename': 'Konami GB Collection Vol.2 (Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Konami GB Collection Vol.2 (Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Konami GB Collection Vol.2 (Europe) (GB Compatible).7z',
        'size': 302836,
    },
    {
        'title': 'Konami GB Collection: Vol.3',
        'filename': 'Konami GB Collection Vol.3 (Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Konami GB Collection Vol.3 (Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Konami GB Collection Vol.3 (Europe) (GB Compatible).7z',
        'size': 361406,
    },
    {
        'title': 'Konami GB Collection: Vol.4',
        'filename': 'Konami GB Collection Vol.4 (Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Konami GB Collection Vol.4 (Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Konami GB Collection Vol.4 (Europe) (GB Compatible).7z',
        'size': 523890,
    },
    {
        'title': 'Legend of the River King 2',
        'filename': 'Legend of the River King 2 (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Legend of the River King 2 (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Legend of the River King 2 (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 369905,
    },
    {
        'title': 'Legend of the River King GBC',
        'filename': 'Legend of the River King GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Legend of the River King GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Legend of the River King GBC (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 219976,
    },
    {
        'title': "The Legend of Zelda: Link's Awakening DX",
        'filename': "Legend of Zelda, The - Link's Awakening DX (USA, Europe) (Rev 2) (SGB Enhanced) (GB Compatible).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Legend of Zelda, The - Link's Awakening DX (USA, Europe) (Rev 2) (SGB Enhanced) (GB Compatible).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Legend of Zelda, The - Link's Awakening DX (USA, Europe) (Rev 2) (SGB Enhanced) (GB Compatible).7z",
        'size': 368385,
    },
    {
        'title': 'The Legend of Zelda: Oracle of Ages',
        'filename': 'Legend of Zelda, The - Oracle of Ages (USA, Australia).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Legend of Zelda, The - Oracle of Ages (USA, Australia).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Legend of Zelda, The - Oracle of Ages (USA, Australia).7z',
        'size': 633387,
    },
    {
        'title': 'The Legend of Zelda: Oracle of Seasons',
        'filename': 'Legend of Zelda, The - Oracle of Seasons (USA, Australia).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Legend of Zelda, The - Oracle of Seasons (USA, Australia).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Legend of Zelda, The - Oracle of Seasons (USA, Australia).7z',
        'size': 613809,
    },
    {
        'title': 'LEGO Alpha Team',
        'filename': 'LEGO Alpha Team (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/LEGO Alpha Team (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/LEGO Alpha Team (USA).7z',
        'size': 109023,
    },
    {
        'title': "LEGO Island 2: The Brickster's Revenge",
        'filename': "LEGO Island 2 - The Brickster's Revenge (USA) (En,Fr,Es).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/LEGO Island 2 - The Brickster's Revenge (USA) (En,Fr,Es).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/LEGO Island 2 - The Brickster's Revenge (USA) (En,Fr,Es).7z",
        'size': 441771,
    },
    {
        'title': 'LEGO Racers',
        'filename': 'LEGO Racers (USA) (En,Fr,Es).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/LEGO Racers (USA) (En,Fr,Es).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/LEGO Racers (USA) (En,Fr,Es).7z',
        'size': 234236,
    },
    {
        'title': 'LEGO Stunt Rally',
        'filename': 'LEGO Stunt Rally (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/LEGO Stunt Rally (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/LEGO Stunt Rally (USA).7z',
        'size': 257707,
    },
    {
        'title': 'Lufia: The Legend Returns',
        'filename': 'Lufia - The Legend Returns (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Lufia - The Legend Returns (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Lufia - The Legend Returns (USA).7z',
        'size': 884145,
    },
    {
        'title': 'Marble Madness',
        'filename': 'Marble Madness (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Marble Madness (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Marble Madness (USA, Europe).7z',
        'size': 160104,
    },
    {
        'title': 'Mario Golf',
        'filename': 'Mario Golf (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Mario Golf (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mario Golf (USA).7z',
        'size': 915586,
    },
    {
        'title': 'Mario Tennis',
        'filename': 'Mario Tennis (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Mario Tennis (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mario Tennis (USA).7z',
        'size': 647186,
    },
    {
        'title': "Mat Hoffman's Pro BMX",
        'filename': "Mat Hoffman's Pro BMX (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Mat Hoffman's Pro BMX (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mat Hoffman's Pro BMX (USA, Europe).7z",
        'size': 249466,
    },
    {
        'title': 'Mega Man Xtreme',
        'filename': 'Mega Man Xtreme (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Mega Man Xtreme (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mega Man Xtreme (USA, Europe) (GB Compatible).7z',
        'size': 411412,
    },
    {
        'title': 'Mega Man Xtreme 2',
        'filename': 'Mega Man Xtreme 2 (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Mega Man Xtreme 2 (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mega Man Xtreme 2 (USA, Europe).7z',
        'size': 450603,
    },
    {
        'title': 'Metal Gear Solid',
        'filename': 'Metal Gear Solid (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Metal Gear Solid (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Metal Gear Solid (USA).7z',
        'size': 729017,
    },
    {
        'title': "Mickey's Racing Adventure",
        'filename': "Mickey's Racing Adventure (USA, Europe) (En,Fr,De,Es,It).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Mickey's Racing Adventure (USA, Europe) (En,Fr,De,Es,It).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mickey's Racing Adventure (USA, Europe) (En,Fr,De,Es,It).7z",
        'size': 887883,
    },
    {
        'title': 'Arcade Hits: Joust & Defender',
        'filename': 'Midway Presents Arcade Hits - Joust & Defender (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Midway Presents Arcade Hits - Joust & Defender (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Midway Presents Arcade Hits - Joust & Defender (USA, Europe) (GB Compatible).7z',
        'size': 199510,
    },
    {
        'title': 'Arcade Hits: Moon Patrol & Spy Hunter',
        'filename': 'Midway Presents Arcade Hits - Moon Patrol & Spy Hunter (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Midway Presents Arcade Hits - Moon Patrol & Spy Hunter (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Midway Presents Arcade Hits - Moon Patrol & Spy Hunter (USA, Europe) (GB Compatible).7z',
        'size': 175563,
    },
    {
        'title': 'Mortal Kombat 4',
        'filename': 'Mortal Kombat 4 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Mortal Kombat 4 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mortal Kombat 4 (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 281806,
    },
    {
        'title': 'Mr. Driller',
        'filename': 'Mr. Driller (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Mr. Driller (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Mr. Driller (USA).7z',
        'size': 131308,
    },
    {
        'title': 'Ms. Pac-Man: Special Color Edition',
        'filename': 'Ms. Pac-Man - Special Color Edition (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Ms. Pac-Man - Special Color Edition (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Ms. Pac-Man - Special Color Edition (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 62932,
    },
    {
        'title': 'MTV Sports: Pure Ride',
        'filename': 'MTV Sports - Pure Ride (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/MTV Sports - Pure Ride (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/MTV Sports - Pure Ride (USA, Europe).7z',
        'size': 219784,
    },
    {
        'title': 'MTV Sports: Skateboarding Featuring Andy Macdonald',
        'filename': 'MTV Sports - Skateboarding Featuring Andy MacDonald (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/MTV Sports - Skateboarding Featuring Andy MacDonald (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/MTV Sports - Skateboarding Featuring Andy MacDonald (USA, Europe).7z',
        'size': 238145,
    },
    {
        'title': "MTV Sports: T.J. Lavin's Ultimate BMX",
        'filename': "MTV Sports - T.J. Lavin's Ultimate BMX (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/MTV Sports - T.J. Lavin's Ultimate BMX (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/MTV Sports - T.J. Lavin's Ultimate BMX (USA, Europe).7z",
        'size': 356514,
    },
    {
        'title': 'NBA Jam 2001',
        'filename': 'NBA Jam 2001 (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/NBA Jam 2001 (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/NBA Jam 2001 (USA, Europe).7z',
        'size': 244746,
    },
    {
        'title': 'Oddworld Adventures 2',
        'filename': 'Oddworld Adventures 2 (USA) (En,Fr,De,Es,It) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Oddworld Adventures 2 (USA) (En,Fr,De,Es,It) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Oddworld Adventures 2 (USA) (En,Fr,De,Es,It) (GB Compatible).7z',
        'size': 392452,
    },
    {
        'title': 'Pac-Man: Special Color Edition',
        'filename': 'Pac-Man - Special Color Edition (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pac-Man - Special Color Edition (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pac-Man - Special Color Edition (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 57573,
    },
    {
        'title': 'Paperboy',
        'filename': 'Paperboy (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Paperboy (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Paperboy (USA, Europe).7z',
        'size': 69478,
    },
    {
        'title': 'Perfect Dark',
        'filename': 'Perfect Dark (USA, Europe) (En,Fr,De,Es,It) (Rumble Version).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Perfect Dark (USA, Europe) (En,Fr,De,Es,It) (Rumble Version).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Perfect Dark (USA, Europe) (En,Fr,De,Es,It) (Rumble Version).7z',
        'size': 1896657,
    },
    {
        'title': 'Pitfall: Beyond the Jungle',
        'filename': 'Pitfall - Beyond the Jungle (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pitfall - Beyond the Jungle (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pitfall - Beyond the Jungle (USA, Europe) (GB Compatible).7z',
        'size': 138518,
    },
    {
        'title': 'Pocket Bomberman',
        'filename': 'Pocket Bomberman (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pocket Bomberman (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pocket Bomberman (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 144496,
    },
    {
        'title': 'Pokemon: Crystal Version',
        'filename': 'Pokemon - Crystal Version (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon - Crystal Version (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon - Crystal Version (USA).7z',
        'size': 898437,
    },
    {
        'title': 'Pokémon Gold Version',
        'filename': 'Pokemon - Gold Version (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon - Gold Version (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon - Gold Version (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 652949,
    },
    {
        'title': 'Pokémon Silver Version',
        'filename': 'Pokemon - Silver Version (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon - Silver Version (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon - Silver Version (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 653123,
    },
    {
        'title': 'Pokemon: Yellow Version',
        'filename': 'Pokemon - Yellow Version (UE) (C).gbc',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon - Yellow Version (UE) (C).gbc',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon - Yellow Version (UE) (C).gbc',
        'size': 1048576,
    },
    {
        'title': 'Pokemon Pinball',
        'filename': 'Pokemon Pinball (USA, Australia) (Rumble Version) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon Pinball (USA, Australia) (Rumble Version) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon Pinball (USA, Australia) (Rumble Version) (SGB Enhanced) (GB Compatible).7z',
        'size': 252557,
    },
    {
        'title': 'Pokemon Puzzle Challenge',
        'filename': 'Pokemon Puzzle Challenge (USA, Australia).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon Puzzle Challenge (USA, Australia).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon Puzzle Challenge (USA, Australia).7z',
        'size': 574630,
    },
    {
        'title': 'Pokémon Trading Card Game',
        'filename': 'Pokemon Trading Card Game (USA, Australia) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Pokemon Trading Card Game (USA, Australia) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Pokemon Trading Card Game (USA, Australia) (SGB Enhanced) (GB Compatible).7z',
        'size': 415374,
    },
    {
        'title': 'Prince of Persia',
        'filename': 'Prince of Persia (USA, Europe) (En,Fr,De,Es,It) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Prince of Persia (USA, Europe) (En,Fr,De,Es,It) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Prince of Persia (USA, Europe) (En,Fr,De,Es,It) (GB Compatible).7z',
        'size': 110802,
    },
    {
        'title': 'R-Type DX',
        'filename': 'R-Type DX (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/R-Type DX (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/R-Type DX (USA, Europe) (GB Compatible).7z',
        'size': 244778,
    },
    {
        'title': 'Rampage: World Tour',
        'filename': 'Rampage - World Tour (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Rampage - World Tour (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Rampage - World Tour (USA, Europe) (GB Compatible).7z',
        'size': 137898,
    },
    {
        'title': 'Rampage 2: Universal Tour',
        'filename': 'Rampage 2 - Universal Tour (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Rampage 2 - Universal Tour (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Rampage 2 - Universal Tour (USA, Europe).7z',
        'size': 427432,
    },
    {
        'title': 'Rayman',
        'filename': 'Rayman (USA) (En,Fr,De,Es,It,Nl).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Rayman (USA) (En,Fr,De,Es,It,Nl).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Rayman (USA) (En,Fr,De,Es,It,Nl).7z',
        'size': 1018646,
    },
    {
        'title': 'Rayman 2',
        'filename': 'Rayman 2 (USA) (En,Fr,De,Es,It).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Rayman 2 (USA) (En,Fr,De,Es,It).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Rayman 2 (USA) (En,Fr,De,Es,It).7z',
        'size': 689849,
    },
    {
        'title': 'Razor: Freestyle Scooter',
        'filename': 'Razor Freestyle Scooter (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Razor Freestyle Scooter (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Razor Freestyle Scooter (USA).7z',
        'size': 257424,
    },
    {
        'title': 'Resident Evil',
        'filename': 'Resident Evil (World) (Proto 2).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Resident Evil (World) (Proto 2).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Resident Evil (World) (Proto 2).7z',
        'size': 1550773,
    },
    {
        'title': 'Resident Evil Gaiden',
        'filename': 'Resident Evil Gaiden (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Resident Evil Gaiden (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Resident Evil Gaiden (USA).7z',
        'size': 586946,
    },
    {
        'title': 'Road Rash',
        'filename': 'Road Rash (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Road Rash (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Road Rash (USA, Europe).7z',
        'size': 189354,
    },
    {
        'title': 'Shantae',
        'filename': 'Shantae (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Shantae (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Shantae (USA).7z',
        'size': 997131,
    },
    {
        'title': "Shaun Palmer's Pro Snowboarder",
        'filename': "Shaun Palmer's Pro Snowboarder (USA, Australia).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Shaun Palmer's Pro Snowboarder (USA, Australia).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Shaun Palmer's Pro Snowboarder (USA, Australia).7z",
        'size': 451461,
    },
    {
        'title': 'South Park',
        'filename': 'South Park (USA) (Proto).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/South Park (USA) (Proto).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/South Park (USA) (Proto).7z',
        'size': 322598,
    },
    {
        'title': 'Space Invaders',
        'filename': 'Space Invaders (USA, Europe) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Space Invaders (USA, Europe) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Space Invaders (USA, Europe) (GB Compatible).7z',
        'size': 78921,
    },
    {
        'title': "Star Wars Episode I: Obi-Wan's Adventures",
        'filename': "Star Wars Episode I - Obi-Wan's Adventures (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Star Wars Episode I - Obi-Wan's Adventures (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Star Wars Episode I - Obi-Wan's Adventures (USA).7z",
        'size': 627317,
    },
    {
        'title': 'Star Wars Episode I: Racer',
        'filename': 'Star Wars Episode I - Racer (USA, Europe) (Rumble Version).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Star Wars Episode I - Racer (USA, Europe) (Rumble Version).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Star Wars Episode I - Racer (USA, Europe) (Rumble Version).7z',
        'size': 532876,
    },
    {
        'title': "Street Fighter Alpha: Warriors' Dreams",
        'filename': "Street Fighter Alpha - Warriors' Dreams (USA).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Street Fighter Alpha - Warriors' Dreams (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Street Fighter Alpha - Warriors' Dreams (USA).7z",
        'size': 454553,
    },
    {
        'title': 'Super Mario Bros. Deluxe',
        'filename': 'Super Mario Bros. Deluxe (USA, Europe) (Rev 1).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Super Mario Bros. Deluxe (USA, Europe) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Super Mario Bros. Deluxe (USA, Europe) (Rev 1).7z',
        'size': 289536,
    },
    {
        'title': 'Survival Kids',
        'filename': 'Survival Kids (USA) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Survival Kids (USA) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Survival Kids (USA) (SGB Enhanced) (GB Compatible).7z',
        'size': 328302,
    },
    {
        'title': 'Tech Deck Skateboarding',
        'filename': 'Tech Deck Skateboarding (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Tech Deck Skateboarding (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tech Deck Skateboarding (USA, Europe).7z',
        'size': 192738,
    },
    {
        'title': 'Tetris DX',
        'filename': 'Tetris DX (World) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Tetris DX (World) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tetris DX (World) (SGB Enhanced) (GB Compatible).7z',
        'size': 90890,
    },
    {
        'title': 'Toki Tori',
        'filename': 'Toki Tori (USA, Europe) (En,Ja,Fr,De,Es).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Toki Tori (USA, Europe) (En,Ja,Fr,De,Es).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Toki Tori (USA, Europe) (En,Ja,Fr,De,Es).7z',
        'size': 199789,
    },
    {
        'title': "Tom Clancy's Rainbow Six",
        'filename': "Tom Clancy's Rainbow Six (USA, Europe) (En,Fr,De).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Tom Clancy's Rainbow Six (USA, Europe) (En,Fr,De).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tom Clancy's Rainbow Six (USA, Europe) (En,Fr,De).7z",
        'size': 432496,
    },
    {
        'title': 'Tomb Raider',
        'filename': 'Tomb Raider (USA, Europe) (En,Fr,De,Es,It).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Tomb Raider (USA, Europe) (En,Fr,De,Es,It).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tomb Raider (USA, Europe) (En,Fr,De,Es,It).7z',
        'size': 1442772,
    },
    {
        'title': 'Tomb Raider: Curse of the Sword',
        'filename': 'Tomb Raider - Curse of the Sword (USA, Europe).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Tomb Raider - Curse of the Sword (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tomb Raider - Curse of the Sword (USA, Europe).7z',
        'size': 1409325,
    },
    {
        'title': "Tony Hawk's Pro Skater",
        'filename': "Tony Hawk's Pro Skater (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Tony Hawk's Pro Skater (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tony Hawk's Pro Skater (USA, Europe).7z",
        'size': 168361,
    },
    {
        'title': "Tony Hawk's Pro Skater 2",
        'filename': "Tony Hawk's Pro Skater 2 (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Tony Hawk's Pro Skater 2 (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tony Hawk's Pro Skater 2 (USA, Europe).7z",
        'size': 630308,
    },
    {
        'title': "Tony Hawk's Pro Skater 3",
        'filename': "Tony Hawk's Pro Skater 3 (USA, Europe).7z",
        'source_relative': "Handhelds/Nintendo Game Boy Color [1998]/Tony Hawk's Pro Skater 3 (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Tony Hawk's Pro Skater 3 (USA, Europe).7z",
        'size': 443474,
    },
    {
        'title': 'Wario Land 3',
        'filename': 'Wario Land 3 (World) (En,Ja).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Wario Land 3 (World) (En,Ja).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Wario Land 3 (World) (En,Ja).7z',
        'size': 511211,
    },
    {
        'title': 'Wario Land II',
        'filename': 'Wario Land II (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Wario Land II (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Wario Land II (USA, Europe) (SGB Enhanced) (GB Compatible).7z',
        'size': 410966,
    },
    {
        'title': 'Warlocked',
        'filename': 'Warlocked (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Warlocked (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Warlocked (USA).7z',
        'size': 360439,
    },
    {
        'title': 'Yu-Gi-Oh! Dark Duel Stories',
        'filename': 'Yu-Gi-Oh! - Dark Duel Stories (USA).7z',
        'source_relative': 'Handhelds/Nintendo Game Boy Color [1998]/Yu-Gi-Oh! - Dark Duel Stories (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/gbc/Yu-Gi-Oh! - Dark Duel Stories (USA).7z',
        'size': 1528245,
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