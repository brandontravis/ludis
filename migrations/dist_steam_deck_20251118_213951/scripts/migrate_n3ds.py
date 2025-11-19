#!/usr/bin/env python3
# Auto-generated migration script for Nintendo 3DS
# 152 games, 136.50 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo 3DS'
ESDE_FOLDER = 'n3ds'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Animal Crossing Happy Home Designer',
        'filename': 'Animal Crossing - Happy Home Designer (USA)(En,Fr) (3DS1348).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Animal Crossing - Happy Home Designer (USA)(En,Fr) (3DS1348).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Animal Crossing - Happy Home Designer (USA)(En,Fr) (3DS1348).3ds',
        'size': 537915392,
    },
    {
        'title': 'Animal Crossing: New Leaf',
        'filename': 'Animal Crossing - New Leaf (USA) (3DS0493).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Animal Crossing - New Leaf (USA) (3DS0493).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Animal Crossing - New Leaf (USA) (3DS0493).3ds',
        'size': 807264768,
    },
    {
        'title': 'Batman Arkham Origins: Blackgate',
        'filename': 'Batman Arkham Origins Blackgate (USA) (3DS0527).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Batman Arkham Origins Blackgate (USA) (3DS0527).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Batman Arkham Origins Blackgate (USA) (3DS0527).3ds',
        'size': 754233344,
    },
    {
        'title': 'Bravely Default',
        'filename': 'Bravely Default (USA) (3DS0611).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Bravely Default (USA) (3DS0611).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Bravely Default (USA) (3DS0611).3ds',
        'size': 3504934912,
    },
    {
        'title': 'Bravely Default: For the Sequel',
        'filename': 'Bravely Default - For the Sequel.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Bravely Default - For the Sequel.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Bravely Default - For the Sequel.3ds',
        'size': 3498717184,
    },
    {
        'title': 'Bravely Second: End Layer',
        'filename': 'Bravely Second - End Layer (USA) (3DS1479).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Bravely Second - End Layer (USA) (3DS1479).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Bravely Second - End Layer (USA) (3DS1479).3ds',
        'size': 2707890176,
    },
    {
        'title': 'Captain Toad: Treasure Tracker',
        'filename': 'Captain Toad - Treasure Tracker (USA) (3DS1830).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Captain Toad - Treasure Tracker (USA) (3DS1830).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Captain Toad - Treasure Tracker (USA) (3DS1830).3ds',
        'size': 490684416,
    },
    {
        'title': 'Castlevania: Lords of Shadow: Mirror of Fate',
        'filename': 'Castlevania Lords of Shadow - Mirror of Fate (USA) (3DS0260).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Castlevania Lords of Shadow - Mirror of Fate (USA) (3DS0260).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Castlevania Lords of Shadow - Mirror of Fate (USA) (3DS0260).3ds',
        'size': 1558274560,
    },
    {
        'title': 'Dead or Alive: Dimensions',
        'filename': 'Dead or Alive Dimensions (USA) (3DS0051).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Dead or Alive Dimensions (USA) (3DS0051).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Dead or Alive Dimensions (USA) (3DS0051).3ds',
        'size': 1440866816,
    },
    {
        'title': 'Donkey Kong Country Returns 3D',
        'filename': 'Donkey Kong Country Returns 3D.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Donkey Kong Country Returns 3D.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Donkey Kong Country Returns 3D.3ds',
        'size': 2346623488,
    },
    {
        'title': 'Dragon Quest VII: Fragments of the Forgotten Past',
        'filename': 'Dragon Quest VII - Fragments of the Forgotten Past (USA) (3DS1570).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Dragon Quest VII - Fragments of the Forgotten Past (USA) (3DS1570).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Dragon Quest VII - Fragments of the Forgotten Past (USA) (3DS1570).3ds',
        'size': 1566871552,
    },
    {
        'title': 'Dragon Quest VIII: Journey of the Cursed King',
        'filename': 'Dragon Quest VIII - Journey of the Cursed King (USA) (3DS1639).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Dragon Quest VIII - Journey of the Cursed King (USA) (3DS1639).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Dragon Quest VIII - Journey of the Cursed King (USA) (3DS1639).3ds',
        'size': 3241426944,
    },
    {
        'title': 'Driver: Renegade',
        'filename': 'Driver Renegade (USA) (3DS0098).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Driver Renegade (USA) (3DS0098).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Driver Renegade (USA) (3DS0098).3ds',
        'size': 491901440,
    },
    {
        'title': 'Ever Oasis',
        'filename': 'Ever Oasis (USA) (3DS1724).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Ever Oasis (USA) (3DS1724).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Ever Oasis (USA) (3DS1724).3ds',
        'size': 860192768,
    },
    {
        'title': 'Fantasy Life',
        'filename': 'Fantasy Life (USA) (3DS1122).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Fantasy Life (USA) (3DS1122).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Fantasy Life (USA) (3DS1122).3ds',
        'size': 926597120,
    },
    {
        'title': 'Final Fantasy: Explorers',
        'filename': 'Final Fantasy Explorers (USA) (3DS1444).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Final Fantasy Explorers (USA) (3DS1444).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Final Fantasy Explorers (USA) (3DS1444).3ds',
        'size': 699514880,
    },
    {
        'title': 'Fire Emblem Awakening',
        'filename': 'Fire Emblem - Awakening (USA) (3DS0247).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Fire Emblem - Awakening (USA) (3DS0247).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Fire Emblem - Awakening (USA) (3DS0247).3ds',
        'size': 1154982400,
    },
    {
        'title': 'Fire Emblem Echoes: Shadows of Valentia',
        'filename': 'Fire Emblem Echoes - Shadows of Valentia (USA) (3DS1703).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Fire Emblem Echoes - Shadows of Valentia (USA) (3DS1703).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Fire Emblem Echoes - Shadows of Valentia (USA) (3DS1703).3ds',
        'size': 1722757120,
    },
    {
        'title': 'Harvest Moon: Skytree Village',
        'filename': 'Harvest Moon - Skytree Village (USA) (3DS1588).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Harvest Moon - Skytree Village (USA) (3DS1588).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Harvest Moon - Skytree Village (USA) (3DS1588).3ds',
        'size': 135925760,
    },
    {
        'title': 'Harvest Moon 3D: The Lost Valley',
        'filename': 'Harvest Moon 3D - The Lost Valley (USA) (3DS1097).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Harvest Moon 3D - The Lost Valley (USA) (3DS1097).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Harvest Moon 3D - The Lost Valley (USA) (3DS1097).3ds',
        'size': 110596096,
    },
    {
        'title': 'Harvest Moon 3D: A New Beginning',
        'filename': 'Harvest Moon 3D A New Beginning (USA) (3DS0266).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Harvest Moon 3D A New Beginning (USA) (3DS0266).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Harvest Moon 3D A New Beginning (USA) (3DS0266).3ds',
        'size': 389415936,
    },
    {
        'title': 'Harvest Moon 3D: The Tale of Two Towns',
        'filename': 'Harvest Moon 3D The Tale of Two Towns (USA) (3DS0050).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Harvest Moon 3D The Tale of Two Towns (USA) (3DS0050).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Harvest Moon 3D The Tale of Two Towns (USA) (3DS0050).3ds',
        'size': 268802560,
    },
    {
        'title': 'Kid Icarus: Uprising',
        'filename': 'Kid Icarus Uprising (USA) (3DS0143).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Kid Icarus Uprising (USA) (3DS0143).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Kid Icarus Uprising (USA) (3DS0143).3ds',
        'size': 1721903616,
    },
    {
        'title': 'Kingdom Hearts 3D: Dream Drop Distance',
        'filename': 'Kingdom Hearts 3D - Dream Drop Distance.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Kingdom Hearts 3D - Dream Drop Distance.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Kingdom Hearts 3D - Dream Drop Distance.3ds',
        'size': 1916649984,
    },
    {
        'title': 'Kirby: Planet Robobot',
        'filename': 'Kirby - Planet Robobot (USA) (3DS1518).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Kirby - Planet Robobot (USA) (3DS1518).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Kirby - Planet Robobot (USA) (3DS1518).3ds',
        'size': 739065856,
    },
    {
        'title': 'Kirby Battle Royale',
        'filename': 'Kirby Battle Royale (USA) (3DS1792).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Kirby Battle Royale (USA) (3DS1792).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Kirby Battle Royale (USA) (3DS1792).3ds',
        'size': 263299072,
    },
    {
        'title': 'Kirby: Triple Deluxe',
        'filename': 'Kirby Triple Deluxe (USA)  (3DS0899).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Kirby Triple Deluxe (USA)  (3DS0899).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Kirby Triple Deluxe (USA)  (3DS0899).3ds',
        'size': 656900096,
    },
    {
        'title': 'The Legend of Zelda: A Link Between Worlds',
        'filename': 'Legend of Zelda - A Link Between Worlds, The (USA) (3DS0494).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Legend of Zelda - A Link Between Worlds, The (USA) (3DS0494).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Legend of Zelda - A Link Between Worlds, The (USA) (3DS0494).3ds',
        'size': 745197568,
    },
    {
        'title': "The Legend of Zelda: Majora's Mask 3D",
        'filename': "Legend of Zelda - Majora's Mask 3D, The (v01) (USA) (3DS1561).3ds",
        'source_relative': "Handhelds/Nintendo 3DS [2011]/Legend of Zelda - Majora's Mask 3D, The (v01) (USA) (3DS1561).3ds",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Legend of Zelda - Majora's Mask 3D, The (v01) (USA) (3DS1561).3ds",
        'size': 696496128,
    },
    {
        'title': 'The Legend of Zelda: Ocarina of Time 3D',
        'filename': 'Legend of Zelda - Ocarina of Time 3D, The (USA) (En,Fr,Es) (Rev 1) (3DS1259).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Legend of Zelda - Ocarina of Time 3D, The (USA) (En,Fr,Es) (Rev 1) (3DS1259).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Legend of Zelda - Ocarina of Time 3D, The (USA) (En,Fr,Es) (Rev 1) (3DS1259).3ds',
        'size': 508766720,
    },
    {
        'title': 'The Legend of Zelda: Tri Force Heroes',
        'filename': 'Legend of Zelda - TriForce Heroes, The.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Legend of Zelda - TriForce Heroes, The.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Legend of Zelda - TriForce Heroes, The.3ds',
        'size': 591937536,
    },
    {
        'title': 'LEGO Batman 2: DC Super Heroes',
        'filename': 'LEGO Batman 2 DC Super Heroes (USA) (3DS0264).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Batman 2 DC Super Heroes (USA) (3DS0264).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Batman 2 DC Super Heroes (USA) (3DS0264).3ds',
        'size': 467585536,
    },
    {
        'title': 'LEGO Batman 3: Beyond Gotham',
        'filename': 'LEGO Batman 3 - Beyond Gotham (USA) (En,Fr,Es,Pt) (3DS1101).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Batman 3 - Beyond Gotham (USA) (En,Fr,Es,Pt) (3DS1101).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Batman 3 - Beyond Gotham (USA) (En,Fr,Es,Pt) (3DS1101).3ds',
        'size': 456175616,
    },
    {
        'title': 'LEGO City Undercover: The Chase Begins',
        'filename': 'LEGO City Undercover The Chase Begins (USA) (3DS0262).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO City Undercover The Chase Begins (USA) (3DS0262).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO City Undercover The Chase Begins (USA) (3DS0262).3ds',
        'size': 803082752,
    },
    {
        'title': 'LEGO Friends',
        'filename': 'LEGO Friends(USA) (3DS0620).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Friends(USA) (3DS0620).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Friends(USA) (3DS0620).3ds',
        'size': 394571776,
    },
    {
        'title': 'LEGO Harry Potter: Years 5-7',
        'filename': 'LEGO Harry Potter - Years 5-7 (USA) (3DS0072).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Harry Potter - Years 5-7 (USA) (3DS0072).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Harry Potter - Years 5-7 (USA) (3DS0072).3ds',
        'size': 509037568,
    },
    {
        'title': 'LEGO Jurassic World',
        'filename': 'LEGO Jurassic World (USA) (3DS1283).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Jurassic World (USA) (3DS1283).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Jurassic World (USA) (3DS1283).3ds',
        'size': 517791744,
    },
    {
        'title': "LEGO Legends of Chima: Laval's Journey",
        'filename': 'LEGO Legends of Chima - Lavals Journey(USA) (3DS0599).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Legends of Chima - Lavals Journey(USA) (3DS0599).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Legends of Chima - Lavals Journey(USA) (3DS0599).3ds',
        'size': 468025856,
    },
    {
        'title': 'LEGO Marvel Avengers',
        'filename': 'LEGO Marvel Avengers (USA) (En,Fr,Es,Pt) (3DS1443).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Marvel Avengers (USA) (En,Fr,Es,Pt) (3DS1443).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Marvel Avengers (USA) (En,Fr,Es,Pt) (3DS1443).3ds',
        'size': 505933824,
    },
    {
        'title': 'LEGO Marvel Super Heroes: Universe in Peril',
        'filename': 'LEGO Marvel Super Heroes - Universe in Peril (USA) (3DS0464).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Marvel Super Heroes - Universe in Peril (USA) (3DS0464).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Marvel Super Heroes - Universe in Peril (USA) (3DS0464).3ds',
        'size': 479576064,
    },
    {
        'title': 'LEGO Ninjago: Nindroids',
        'filename': 'LEGO Ninjago Nindroids (USA) (3DS1011).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Ninjago Nindroids (USA) (3DS1011).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Ninjago Nindroids (USA) (3DS1011).3ds',
        'size': 499961856,
    },
    {
        'title': 'LEGO Ninjago: Shadow of Ronin',
        'filename': 'LEGO Ninjago Shadow of Ronin (USA) (3DS1219).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Ninjago Shadow of Ronin (USA) (3DS1219).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Ninjago Shadow of Ronin (USA) (3DS1219).3ds',
        'size': 457719808,
    },
    {
        'title': 'LEGO Pirates of the Caribbean: The Video Game',
        'filename': 'LEGO Pirates of The Caribbean The Video Game (USA) (3DS0073).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Pirates of The Caribbean The Video Game (USA) (3DS0073).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Pirates of The Caribbean The Video Game (USA) (3DS0073).3ds',
        'size': 431718400,
    },
    {
        'title': 'LEGO Star Wars: The Force Awakens',
        'filename': 'LEGO Star Wars - The Force Awakens (USA) (3DS1539).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Star Wars - The Force Awakens (USA) (3DS1539).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Star Wars - The Force Awakens (USA) (3DS1539).3ds',
        'size': 522919936,
    },
    {
        'title': 'LEGO Star Wars III: The Clone Wars',
        'filename': 'LEGO Star Wars III - The Clone Wars (USA) (3DS0075).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO Star Wars III - The Clone Wars (USA) (3DS0075).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO Star Wars III - The Clone Wars (USA) (3DS0075).3ds',
        'size': 491603456,
    },
    {
        'title': 'LEGO The Hobbit',
        'filename': 'LEGO The Hobbit (USA) (3DS0770).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO The Hobbit (USA) (3DS0770).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO The Hobbit (USA) (3DS0770).3ds',
        'size': 505155584,
    },
    {
        'title': 'LEGO The Lord of the Rings',
        'filename': 'LEGO The Lord of the Rings (USA)  (3DS0298).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/LEGO The Lord of the Rings (USA)  (3DS0298).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/LEGO The Lord of the Rings (USA)  (3DS0298).3ds',
        'size': 492315136,
    },
    {
        'title': "Luigi's Mansion",
        'filename': 'Luigis Mansion (USA) (3DS1837).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Luigis Mansion (USA) (3DS1837).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Luigis Mansion (USA) (3DS1837).3ds',
        'size': 275107840,
    },
    {
        'title': "Luigi's Mansion: Dark Moon",
        'filename': 'Luigis Mansion Dark Moon (USA) (3DS0346).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Luigis Mansion Dark Moon (USA) (3DS0346).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Luigis Mansion Dark Moon (USA) (3DS0346).3ds',
        'size': 915325440,
    },
    {
        'title': "Mario & Luigi: Bowser's Inside Story + Bowser Jr's Journey",
        'filename': "Mario & Luigi - Bowser's Inside Story + Bowser Jr.'s Journey (USA) (3DS1847).3ds",
        'source_relative': "Handhelds/Nintendo 3DS [2011]/Mario & Luigi - Bowser's Inside Story + Bowser Jr.'s Journey (USA) (3DS1847).3ds",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario & Luigi - Bowser's Inside Story + Bowser Jr.'s Journey (USA) (3DS1847).3ds",
        'size': 770699264,
    },
    {
        'title': 'Mario & Luigi: Dream Team',
        'filename': 'Mario & Luigi - Dream Team (v01)(USA)(M3) (3DS1672).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario & Luigi - Dream Team (v01)(USA)(M3) (3DS1672).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario & Luigi - Dream Team (v01)(USA)(M3) (3DS1672).3ds',
        'size': 895787008,
    },
    {
        'title': 'Mario & Luigi: Paper Jam',
        'filename': 'Mario & Luigi - Paper Jam (USA) (3DS1440).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario & Luigi - Paper Jam (USA) (3DS1440).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario & Luigi - Paper Jam (USA) (3DS1440).3ds',
        'size': 492908544,
    },
    {
        'title': "Mario & Luigi: Superstar Saga + Bowser's Minions",
        'filename': "Mario & Luigi - Superstar Saga + Bowser's Minions (USA)(M3) (3DS1760).3ds",
        'source_relative': "Handhelds/Nintendo 3DS [2011]/Mario & Luigi - Superstar Saga + Bowser's Minions (USA)(M3) (3DS1760).3ds",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario & Luigi - Superstar Saga + Bowser's Minions (USA)(M3) (3DS1760).3ds",
        'size': 616869888,
    },
    {
        'title': 'Mario & Sonic at the Rio 2016 Olympic Games',
        'filename': 'Mario & Sonic at the Rio 2016 Olympic Games (USA) (En,Fr,Es) (3DS1468).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario & Sonic at the Rio 2016 Olympic Games (USA) (En,Fr,Es) (3DS1468).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario & Sonic at the Rio 2016 Olympic Games (USA) (En,Fr,Es) (3DS1468).3ds',
        'size': 757968896,
    },
    {
        'title': 'Mario & Sonic at the London 2012 Olympic Games',
        'filename': 'Mario and Sonic at the London 2012 Olympic Games (USA) (3DS0104).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario and Sonic at the London 2012 Olympic Games (USA) (3DS0104).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario and Sonic at the London 2012 Olympic Games (USA) (3DS0104).3ds',
        'size': 411406336,
    },
    {
        'title': 'Mario Golf: World Tour',
        'filename': 'Mario Golf World Tour (USA) (3DS0911).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Golf World Tour (USA) (3DS0911).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Golf World Tour (USA) (3DS0911).3ds',
        'size': 579244032,
    },
    {
        'title': 'Mario Kart 7',
        'filename': 'Mario Kart 7 (USA) (Rev 1) (3DS0852).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Kart 7 (USA) (Rev 1) (3DS0852).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Kart 7 (USA) (Rev 1) (3DS0852).3ds',
        'size': 696706048,
    },
    {
        'title': 'Mario Party: Island Tour',
        'filename': 'Mario Party - Island Tour (USA) (3DS0492).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Party - Island Tour (USA) (3DS0492).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Party - Island Tour (USA) (3DS0492).3ds',
        'size': 278147072,
    },
    {
        'title': 'Mario Party: Star Rush',
        'filename': 'Mario Party - Star Rush (USA) (3DS1595).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Party - Star Rush (USA) (3DS1595).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Party - Star Rush (USA) (3DS1595).3ds',
        'size': 436572160,
    },
    {
        'title': 'Mario Party: The Top 100',
        'filename': 'Mario Party - The Top 100 (USA) (3DS1769).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Party - The Top 100 (USA) (3DS1769).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Party - The Top 100 (USA) (3DS1769).3ds',
        'size': 315990016,
    },
    {
        'title': 'Mario Sports Superstars',
        'filename': 'Mario Sports Superstars (USA) (3DS1680).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Sports Superstars (USA) (3DS1680).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Sports Superstars (USA) (3DS1680).3ds',
        'size': 905838592,
    },
    {
        'title': 'Mario Tennis Open',
        'filename': 'Mario Tennis Open (USA) (3DS0257).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mario Tennis Open (USA) (3DS0257).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mario Tennis Open (USA) (3DS0257).3ds',
        'size': 295068160,
    },
    {
        'title': 'Mega Man Legacy Collection',
        'filename': 'Mega Man Legacy Collection (USA) (3DS1454).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Mega Man Legacy Collection (USA) (3DS1454).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Mega Man Legacy Collection (USA) (3DS1454).3ds',
        'size': 528801792,
    },
    {
        'title': 'Metal Gear Solid 3D: Snake Eater',
        'filename': 'Metal Gear Solid 3D Snake Eater (USA) (3DS0107).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Metal Gear Solid 3D Snake Eater (USA) (3DS0107).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Metal Gear Solid 3D Snake Eater (USA) (3DS0107).3ds',
        'size': 3248401408,
    },
    {
        'title': 'Metroid: Samus Returns',
        'filename': 'Metroid - Samus Returns (USA) (3DS1754).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Metroid - Samus Returns (USA) (3DS1754).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Metroid - Samus Returns (USA) (3DS1754).3ds',
        'size': 757235712,
    },
    {
        'title': 'Metroid Prime: Federation Force',
        'filename': 'Metroid Prime - Federation Force (USA) (En,Fr,Es) (3DS1560).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Metroid Prime - Federation Force (USA) (En,Fr,Es) (3DS1560).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Metroid Prime - Federation Force (USA) (En,Fr,Es) (3DS1560).3ds',
        'size': 1384108032,
    },
    {
        'title': 'Michael Jackson: The Experience 3D',
        'filename': 'Michael Jackson The Experience 3D (USA) (3DS0169).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Michael Jackson The Experience 3D (USA) (3DS0169).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Michael Jackson The Experience 3D (USA) (3DS0169).3ds',
        'size': 461094400,
    },
    {
        'title': 'Miitopia',
        'filename': 'Miitopia (USA)(M3) (3DS1744).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Miitopia (USA)(M3) (3DS1744).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Miitopia (USA)(M3) (3DS1744).3ds',
        'size': 941469696,
    },
    {
        'title': 'Monster Hunter 3: Ultimate',
        'filename': 'Monster Hunter 3 Ultimate (USA) (3DS0256).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Monster Hunter 3 Ultimate (USA) (3DS0256).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Monster Hunter 3 Ultimate (USA) (3DS0256).3ds',
        'size': 1901615104,
    },
    {
        'title': 'Monster Hunter 4 Ultimate',
        'filename': 'Monster Hunter 4 Ultimate (USA) (3DS1191).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Monster Hunter 4 Ultimate (USA) (3DS1191).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Monster Hunter 4 Ultimate (USA) (3DS1191).3ds',
        'size': 2754797568,
    },
    {
        'title': 'Monster Hunter Generations',
        'filename': 'Monster Hunter Generations (USA) (3DS1551).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Monster Hunter Generations (USA) (3DS1551).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Monster Hunter Generations (USA) (3DS1551).3ds',
        'size': 1677115392,
    },
    {
        'title': 'Monster Hunter Stories',
        'filename': 'Monster Hunter Stories (USA) (3DS1751).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Monster Hunter Stories (USA) (3DS1751).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Monster Hunter Stories (USA) (3DS1751).3ds',
        'size': 1973596160,
    },
    {
        'title': 'Myst',
        'filename': 'Myst (USA) (3DS0440).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Myst (USA) (3DS0440).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Myst (USA) (3DS0440).3ds',
        'size': 241789952,
    },
    {
        'title': 'New Super Mario Bros. 2',
        'filename': 'New Super Mario Bros. 2 (USA) (3DS0255).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/New Super Mario Bros. 2 (USA) (3DS0255).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/New Super Mario Bros. 2 (USA) (3DS0255).3ds',
        'size': 388309504,
    },
    {
        'title': 'Pac-Man & Galaga Dimensions',
        'filename': 'Pac-Man & Galaga - Dimensions (USA) (3DS0100).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pac-Man & Galaga - Dimensions (USA) (3DS0100).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pac-Man & Galaga - Dimensions (USA) (3DS0100).3ds',
        'size': 471647232,
    },
    {
        'title': 'Pac-Man and the Ghostly Adventures 2',
        'filename': 'Pac-Man and the Ghostly Adventures 2 (USA) (3DS1061).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pac-Man and the Ghostly Adventures 2 (USA) (3DS1061).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pac-Man and the Ghostly Adventures 2 (USA) (3DS1061).3ds',
        'size': 510779392,
    },
    {
        'title': 'Pac-Man Party 3D',
        'filename': 'Pac-Man Party 3D(USA) (3DS0085).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pac-Man Party 3D(USA) (3DS0085).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pac-Man Party 3D(USA) (3DS0085).3ds',
        'size': 224494080,
    },
    {
        'title': 'Pac-Man and the Ghostly Adventures',
        'filename': 'PacMan and the Ghostly Adventures (USA) (3DS0480).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/PacMan and the Ghostly Adventures (USA) (3DS0480).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/PacMan and the Ghostly Adventures (USA) (3DS0480).3ds',
        'size': 180523008,
    },
    {
        'title': 'Paper Mario: Sticker Star',
        'filename': 'Paper Mario - Sticker Star (USA) (3DS0254).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Paper Mario - Sticker Star (USA) (3DS0254).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Paper Mario - Sticker Star (USA) (3DS0254).3ds',
        'size': 581517824,
    },
    {
        'title': 'Persona Q: Shadow of the Labyrinth',
        'filename': 'Persona Q - Shadow of the Labyrinth (USA) (3DS1111).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Persona Q - Shadow of the Labyrinth (USA) (3DS1111).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Persona Q - Shadow of the Labyrinth (USA) (3DS1111).3ds',
        'size': 1889366016,
    },
    {
        'title': 'Persona Q2: New Cinema Labyrinth',
        'filename': 'Persona Q2 - New Cinema Labyrinth (USA) (3DS1861).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Persona Q2 - New Cinema Labyrinth (USA) (3DS1861).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Persona Q2 - New Cinema Labyrinth (USA) (3DS1861).3ds',
        'size': 2890895360,
    },
    {
        'title': 'Phoenix Wright: Ace Attorney: Dual Destinies',
        'filename': 'Phoenix Wright - Ace Attorney - Dual Destinies.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Phoenix Wright - Ace Attorney - Dual Destinies.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Phoenix Wright - Ace Attorney - Dual Destinies.3ds',
        'size': 580575232,
    },
    {
        'title': 'Pilotwings Resort',
        'filename': 'Pilotwings Resort (USA) (3DS0032).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pilotwings Resort (USA) (3DS0032).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pilotwings Resort (USA) (3DS0032).3ds',
        'size': 101605888,
    },
    {
        'title': 'Pokemon Alpha Sapphire',
        'filename': 'Pokemon Alpha Sapphire (USA)(En,Fr,Ge,It,Ja,Ko,Es) (3DS1123).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Alpha Sapphire (USA)(En,Fr,Ge,It,Ja,Ko,Es) (3DS1123).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Alpha Sapphire (USA)(En,Fr,Ge,It,Ja,Ko,Es) (3DS1123).3ds',
        'size': 1927225344,
    },
    {
        'title': 'Pokémon Moon',
        'filename': 'Pokemon Moon (USA) (En,Ja,Fr,De,Es,It,Zh,Ko) (3DS1610).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Moon (USA) (En,Ja,Fr,De,Es,It,Zh,Ko) (3DS1610).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Moon (USA) (En,Ja,Fr,De,Es,It,Zh,Ko) (3DS1610).3ds',
        'size': 3246936064,
    },
    {
        'title': 'Pokemon Omega Ruby',
        'filename': 'Pokemon Omega Ruby (USA)(En,Fr,Ge,It,Ja,Ko,Es) (3DS1124).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Omega Ruby (USA)(En,Fr,Ge,It,Ja,Ko,Es) (3DS1124).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Omega Ruby (USA)(En,Fr,Ge,It,Ja,Ko,Es) (3DS1124).3ds',
        'size': 1927106560,
    },
    {
        'title': 'Pokemon Rumble Blast',
        'filename': 'Pokemon Rumble Blast (USA) (3DS0070).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Rumble Blast (USA) (3DS0070).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Rumble Blast (USA) (3DS0070).3ds',
        'size': 340543488,
    },
    {
        'title': 'Pokémon Rumble World',
        'filename': 'Pokemon Rumble World (USA) (3DS1490).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Rumble World (USA) (3DS1490).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Rumble World (USA) (3DS1490).3ds',
        'size': 150716416,
    },
    {
        'title': 'Pokémon Sun',
        'filename': 'Pokemon Sun (USA) (En,Ja,Fr,De,Es,It,Zh,Ko) (3DS1609).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Sun (USA) (En,Ja,Fr,De,Es,It,Zh,Ko) (3DS1609).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Sun (USA) (En,Ja,Fr,De,Es,It,Zh,Ko) (3DS1609).3ds',
        'size': 3262697472,
    },
    {
        'title': 'Pokémon Super Mystery Dungeon',
        'filename': 'Pokemon Super Mystery Dungeon (USA)(En) (3DS1400).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Super Mystery Dungeon (USA)(En) (3DS1400).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Super Mystery Dungeon (USA)(En) (3DS1400).3ds',
        'size': 1890422784,
    },
    {
        'title': 'Pokémon Ultra Moon',
        'filename': 'Pokemon Ultra Moon (USA)(M8) (3DS1776).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Ultra Moon (USA)(M8) (3DS1776).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Ultra Moon (USA)(M8) (3DS1776).3ds',
        'size': 3750944768,
    },
    {
        'title': 'Pokemon Ultra Sun',
        'filename': 'Pokemon Ultra Sun (USA)(M8) (3DS1777).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Ultra Sun (USA)(M8) (3DS1777).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Ultra Sun (USA)(M8) (3DS1777).3ds',
        'size': 3738267648,
    },
    {
        'title': 'Pokemon X',
        'filename': 'Pokemon X (USA) (3DS0511).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon X (USA) (3DS0511).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon X (USA) (3DS0511).3ds',
        'size': 1840214016,
    },
    {
        'title': 'Pokemon Y',
        'filename': 'Pokemon Y (USA) (3DS0510).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Pokemon Y (USA) (3DS0510).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Pokemon Y (USA) (3DS0510).3ds',
        'size': 1840214016,
    },
    {
        'title': "Poochy & Yoshi's Woolly World",
        'filename': 'Poochy & Yoshis Woolly World (USA) (3DS1647).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Poochy & Yoshis Woolly World (USA) (3DS1647).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Poochy & Yoshis Woolly World (USA) (3DS1647).3ds',
        'size': 1063575552,
    },
    {
        'title': 'Professor Layton and the Azran Legacy',
        'filename': 'Professor Layton and the Azran Legacy(USA) (3DS0647).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Professor Layton and the Azran Legacy(USA) (3DS0647).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Professor Layton and the Azran Legacy(USA) (3DS0647).3ds',
        'size': 983674880,
    },
    {
        'title': 'Professor Layton and the Miracle Mask',
        'filename': 'Professor Layton and the Miracle Mask (v01)(USA) (3DS1681).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Professor Layton and the Miracle Mask (v01)(USA) (3DS1681).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Professor Layton and the Miracle Mask (v01)(USA) (3DS1681).3ds',
        'size': 859996672,
    },
    {
        'title': 'Professor Layton vs Phoenix Wright: Ace Attorney',
        'filename': 'Professor Layton vs Phoenix Wright Ace Attorney (USA) (3DS1028).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Professor Layton vs Phoenix Wright Ace Attorney (USA) (3DS1028).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Professor Layton vs Phoenix Wright Ace Attorney (USA) (3DS1028).3ds',
        'size': 1498349568,
    },
    {
        'title': 'Rabbids Rumble',
        'filename': 'Rabbids Rumble (USA) (3DS0299).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Rabbids Rumble (USA) (3DS0299).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Rabbids Rumble (USA) (3DS0299).3ds',
        'size': 396771840,
    },
    {
        'title': 'Rabbids Travel in Time 3D',
        'filename': 'Rabbids Travel in Time 3D (USA) (3DS0086).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Rabbids Travel in Time 3D (USA) (3DS0086).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Rabbids Travel in Time 3D (USA) (3DS0086).3ds',
        'size': 124189696,
    },
    {
        'title': 'Rayman 3D',
        'filename': 'Rayman 3D (USA) (3DS0114).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Rayman 3D (USA) (3DS0114).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Rayman 3D (USA) (3DS0114).3ds',
        'size': 203188224,
    },
    {
        'title': 'Rayman Origins',
        'filename': 'Rayman Origins (USA) (3DS0252).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Rayman Origins (USA) (3DS0252).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Rayman Origins (USA) (3DS0252).3ds',
        'size': 219863040,
    },
    {
        'title': 'Resident Evil: Revelations',
        'filename': 'Resident Evil Revelations (USA) (3DS0108).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Resident Evil Revelations (USA) (3DS0108).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Resident Evil Revelations (USA) (3DS0108).3ds',
        'size': 3396517888,
    },
    {
        'title': 'Resident Evil: The Mercenaries 3D',
        'filename': 'Resident Evil The Mercenaries 3D (USA) (3DS0115).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Resident Evil The Mercenaries 3D (USA) (3DS0115).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Resident Evil The Mercenaries 3D (USA) (3DS0115).3ds',
        'size': 703942144,
    },
    {
        'title': 'RollerCoaster Tycoon 3D',
        'filename': 'RollerCoaster Tycoon 3D(USA) (3DS0622).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/RollerCoaster Tycoon 3D(USA) (3DS0622).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/RollerCoaster Tycoon 3D(USA) (3DS0622).3ds',
        'size': 333492224,
    },
    {
        'title': 'Rune Factory 4',
        'filename': 'Rune Factory 4 (USA) (3DS0437).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Rune Factory 4 (USA) (3DS0437).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Rune Factory 4 (USA) (3DS0437).3ds',
        'size': 1467789312,
    },
    {
        'title': 'Sega 3D Classics Collection',
        'filename': 'Sega 3D Classics Collection (USA) (3DS1489).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Sega 3D Classics Collection (USA) (3DS1489).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Sega 3D Classics Collection (USA) (3DS1489).3ds',
        'size': 138350592,
    },
    {
        'title': "Shantae and the Pirate's Curse",
        'filename': 'Shantae and the Pirates Curse (USA) (3DS1583).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shantae and the Pirates Curse (USA) (3DS1583).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shantae and the Pirates Curse (USA) (3DS1583).3ds',
        'size': 352088064,
    },
    {
        'title': 'Shifting World',
        'filename': 'Shifting World (USA) (3DS0180).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shifting World (USA) (3DS0180).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shifting World (USA) (3DS0180).3ds',
        'size': 56080896,
    },
    {
        'title': 'Shin Megami Tensei: Devil Summoner: Soul Hackers',
        'filename': 'Shin Megami Tensei - Devil Summoner - Soul Hackers (USA) (3DS0429).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shin Megami Tensei - Devil Summoner - Soul Hackers (USA) (3DS0429).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shin Megami Tensei - Devil Summoner - Soul Hackers (USA) (3DS0429).3ds',
        'size': 1970041344,
    },
    {
        'title': 'Shin Megami Tensei: Devil Survivor 2 Record Breaker',
        'filename': 'Shin Megami Tensei - Devil Survivor 2 Record Breaker (USA)(En) (3DS1240).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shin Megami Tensei - Devil Survivor 2 Record Breaker (USA)(En) (3DS1240).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shin Megami Tensei - Devil Survivor 2 Record Breaker (USA)(En) (3DS1240).3ds',
        'size': 3017236480,
    },
    {
        'title': 'Shin Megami Tensei: Devil Survivor Overclocked',
        'filename': 'Shin Megami Tensei Devil Survivor Overclocked (USA) (3DS0053).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shin Megami Tensei Devil Survivor Overclocked (USA) (3DS0053).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shin Megami Tensei Devil Survivor Overclocked (USA) (3DS0053).3ds',
        'size': 1208507392,
    },
    {
        'title': 'Shin Megami Tensei IV',
        'filename': 'Shin Megami Tensei IV (USA) (3DS0414).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shin Megami Tensei IV (USA) (3DS0414).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shin Megami Tensei IV (USA) (3DS0414).3ds',
        'size': 1909621248,
    },
    {
        'title': 'Shin Megami Tensei IV: Apocalypse',
        'filename': 'Shin Megami Tensei IV - Apocalypse (USA) (3DS1568).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shin Megami Tensei IV - Apocalypse (USA) (3DS1568).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shin Megami Tensei IV - Apocalypse (USA) (3DS1568).3ds',
        'size': 1843347456,
    },
    {
        'title': 'Shovel Knight',
        'filename': 'Shovel Knight (USA) (3DS1378).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shovel Knight (USA) (3DS1378).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shovel Knight (USA) (3DS1378).3ds',
        'size': 134627328,
    },
    {
        'title': 'Shovel Knight',
        'filename': 'Shovel Knight (USA) (3DS1378).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Shovel Knight (USA) (3DS1378).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Shovel Knight (USA) (3DS1378).3ds',
        'size': 133853184,
    },
    {
        'title': "Skylanders: Spyro's Adventure",
        'filename': 'Skylanders - Spyros Adventure (USA) (3DS0101).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Skylanders - Spyros Adventure (USA) (3DS0101).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Skylanders - Spyros Adventure (USA) (3DS0101).3ds',
        'size': 425972224,
    },
    {
        'title': 'Skylanders: Swap Force',
        'filename': 'Skylanders - Swap Force (USA) (3DS0471).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Skylanders - Swap Force (USA) (3DS0471).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Skylanders - Swap Force (USA) (3DS0471).3ds',
        'size': 880693248,
    },
    {
        'title': 'Skylanders Giants',
        'filename': 'Skylanders Giants (USA) (3DS0419).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Skylanders Giants (USA) (3DS0419).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Skylanders Giants (USA) (3DS0419).3ds',
        'size': 473604608,
    },
    {
        'title': 'Skylanders SuperChargers Racing',
        'filename': 'Skylanders SuperChargers Racing (USA) (3DS1509).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Skylanders SuperChargers Racing (USA) (3DS1509).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Skylanders SuperChargers Racing (USA) (3DS1509).3ds',
        'size': 655319040,
    },
    {
        'title': 'Skylanders: Trap Team',
        'filename': 'Skylanders Trap Team (USA) (3DS1078).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Skylanders Trap Team (USA) (3DS1078).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Skylanders Trap Team (USA) (3DS1078).3ds',
        'size': 778285056,
    },
    {
        'title': 'Sonic & All-Stars Racing Transformed',
        'filename': 'Sonic & All-Stars Racing Transformed(USA) (3DS0639).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Sonic & All-Stars Racing Transformed(USA) (3DS0639).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Sonic & All-Stars Racing Transformed(USA) (3DS0639).3ds',
        'size': 886821376,
    },
    {
        'title': 'Sonic Lost World',
        'filename': 'Sonic - Lost World(USA) (3DS0612).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Sonic - Lost World(USA) (3DS0612).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Sonic - Lost World(USA) (3DS0612).3ds',
        'size': 1342181376,
    },
    {
        'title': 'Sonic Boom: Fire & Ice',
        'filename': 'Sonic Boom - Fire & Ice (USA) (3DS1573).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Sonic Boom - Fire & Ice (USA) (3DS1573).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Sonic Boom - Fire & Ice (USA) (3DS1573).3ds',
        'size': 1780932608,
    },
    {
        'title': 'Sonic Boom: Shattered Crystal',
        'filename': 'Sonic Boom - Shattered Crystal (USA) (3DS1102).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Sonic Boom - Shattered Crystal (USA) (3DS1102).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Sonic Boom - Shattered Crystal (USA) (3DS1102).3ds',
        'size': 892477440,
    },
    {
        'title': 'Sonic Generations',
        'filename': 'Sonic Generations (v01)(USA)(M3) (3DS1670).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Sonic Generations (v01)(USA)(M3) (3DS1670).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Sonic Generations (v01)(USA)(M3) (3DS1670).3ds',
        'size': 669791744,
    },
    {
        'title': 'Star Fox 64 3D',
        'filename': 'Star Fox 64 3D.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Star Fox 64 3D.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Star Fox 64 3D.3ds',
        'size': 620524544,
    },
    {
        'title': 'SteamWorld Heist',
        'filename': 'SteamWorld Heist.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/SteamWorld Heist.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/SteamWorld Heist.3ds',
        'size': 185946112,
    },
    {
        'title': 'Story of Seasons: Trio of Towns',
        'filename': 'Story of Seasons - Trio of Towns (USA) (3DS1660).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Story of Seasons - Trio of Towns (USA) (3DS1660).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Story of Seasons - Trio of Towns (USA) (3DS1660).3ds',
        'size': 754999296,
    },
    {
        'title': 'Super Mario 3D Land',
        'filename': 'Super Mario 3D Land (v01)(USA)(M3) (3DS1669).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Super Mario 3D Land (v01)(USA)(M3) (3DS1669).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Super Mario 3D Land (v01)(USA)(M3) (3DS1669).3ds',
        'size': 335029760,
    },
    {
        'title': 'Super Mario Maker for Nintendo 3DS',
        'filename': 'Super Mario Maker for Nintendo 3DS (USA) (3DS1620).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Super Mario Maker for Nintendo 3DS (USA) (3DS1620).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Super Mario Maker for Nintendo 3DS (USA) (3DS1620).3ds',
        'size': 424443904,
    },
    {
        'title': 'Super Monkey Ball 3D',
        'filename': 'Super Monkey Ball 3D.3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Super Monkey Ball 3D.3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Super Monkey Ball 3D.3ds',
        'size': 232271360,
    },
    {
        'title': 'Super Smash Bros. for Nintendo 3DS',
        'filename': 'Super Smash Bros. for Nintendo 3DS (USA) (3DS1051).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Super Smash Bros. for Nintendo 3DS (USA) (3DS1051).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Super Smash Bros. for Nintendo 3DS (USA) (3DS1051).3ds',
        'size': 1189982208,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles',
        'filename': 'Teenage Mutant Ninja Turtles (USA) (3DS0465).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Teenage Mutant Ninja Turtles (USA) (3DS0465).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Teenage Mutant Ninja Turtles (USA) (3DS0465).3ds',
        'size': 247771136,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles: Danger of the Ooze',
        'filename': 'Teenage Mutant Ninja Turtles - Danger of the Ooze (USA) (3DS1104).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Teenage Mutant Ninja Turtles - Danger of the Ooze (USA) (3DS1104).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Teenage Mutant Ninja Turtles - Danger of the Ooze (USA) (3DS1104).3ds',
        'size': 254447616,
    },
    {
        'title': 'Teenage Mutant Ninja Turtles: Master Splinters Training Pack',
        'filename': "Teenage Mutant Ninja Turtles - Master Splinter's Training Pack (USA) (En,Fr) (3DS1506).3ds",
        'source_relative': "Handhelds/Nintendo 3DS [2011]/Teenage Mutant Ninja Turtles - Master Splinter's Training Pack (USA) (En,Fr) (3DS1506).3ds",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Teenage Mutant Ninja Turtles - Master Splinter's Training Pack (USA) (En,Fr) (3DS1506).3ds",
        'size': 492474368,
    },
    {
        'title': 'Tetris Axis',
        'filename': 'Tetris Axis (USA) (3DS0054).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Tetris Axis (USA) (3DS0054).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Tetris Axis (USA) (3DS0054).3ds',
        'size': 177206272,
    },
    {
        'title': 'Tetris Ultimate',
        'filename': 'Tetris Ultimate (USA) (3DS1108).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Tetris Ultimate (USA) (3DS1108).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Tetris Ultimate (USA) (3DS1108).3ds',
        'size': 80613376,
    },
    {
        'title': 'The LEGO Movie Videogame',
        'filename': 'The LEGO Movie Videogame(USA) (3DS0609).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/The LEGO Movie Videogame(USA) (3DS0609).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/The LEGO Movie Videogame(USA) (3DS0609).3ds',
        'size': 466644992,
    },
    {
        'title': 'The Oregon Trail',
        'filename': 'The Oregon Trail (USA) (3DS0158).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/The Oregon Trail (USA) (3DS0158).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/The Oregon Trail (USA) (3DS0158).3ds',
        'size': 109152256,
    },
    {
        'title': 'The Sims 3',
        'filename': 'The Sims 3 (USA) (3DS0120).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/The Sims 3 (USA) (3DS0120).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/The Sims 3 (USA) (3DS0120).3ds',
        'size': 409545728,
    },
    {
        'title': 'The Sims 3: Pets',
        'filename': 'The Sims 3 Pets (USA) (3DS0071).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/The Sims 3 Pets (USA) (3DS0071).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/The Sims 3 Pets (USA) (3DS0071).3ds',
        'size': 423903744,
    },
    {
        'title': 'Theatrhythm Final Fantasy',
        'filename': 'Theatrhythm Final Fantasy (USA) (3DS0344).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Theatrhythm Final Fantasy (USA) (3DS0344).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Theatrhythm Final Fantasy (USA) (3DS0344).3ds',
        'size': 943097856,
    },
    {
        'title': 'Theatrhythm Final Fantasy: Curtain Call',
        'filename': 'Theatrhythm Final Fantasy - Curtain Call (USA) (3DS1035).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Theatrhythm Final Fantasy - Curtain Call (USA) (3DS1035).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Theatrhythm Final Fantasy - Curtain Call (USA) (3DS1035).3ds',
        'size': 1785122816,
    },
    {
        'title': "Tom Clancy's Splinter Cell 3D",
        'filename': 'Tom Clancys Splinter Cell 3D (USA) (3DS0079).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Tom Clancys Splinter Cell 3D (USA) (3DS0079).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Tom Clancys Splinter Cell 3D (USA) (3DS0079).3ds',
        'size': 1388244480,
    },
    {
        'title': 'Ultimate NES Remix',
        'filename': 'Ultimate NES Remix (USA) (3DS1150).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Ultimate NES Remix (USA) (3DS1150).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Ultimate NES Remix (USA) (3DS1150).3ds',
        'size': 146997248,
    },
    {
        'title': 'WarioWare Gold',
        'filename': 'WarioWare Gold (USA) (3DS1831).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/WarioWare Gold (USA) (3DS1831).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/WarioWare Gold (USA) (3DS1831).3ds',
        'size': 1331396608,
    },
    {
        'title': 'Wipeout: Create & Crash',
        'filename': 'Wipeout - Create and Crash (USA) (3DS0462).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Wipeout - Create and Crash (USA) (3DS0462).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Wipeout - Create and Crash (USA) (3DS0462).3ds',
        'size': 446005248,
    },
    {
        'title': 'Wipeout 2',
        'filename': 'Wipeout 2 (USA) (3DS0083).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Wipeout 2 (USA) (3DS0083).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Wipeout 2 (USA) (3DS0083).3ds',
        'size': 213237248,
    },
    {
        'title': 'Wipeout 3',
        'filename': 'Wipeout 3 (USA) (3DS0457).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Wipeout 3 (USA) (3DS0457).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Wipeout 3 (USA) (3DS0457).3ds',
        'size': 438854144,
    },
    {
        'title': "Yoshi's New Island",
        'filename': 'Yoshis New Island (USA) (3DS0655).3ds',
        'source_relative': 'Handhelds/Nintendo 3DS [2011]/Yoshis New Island (USA) (3DS0655).3ds',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Yoshis New Island (USA) (3DS0655).3ds',
        'size': 467869696,
    },
    {
        'title': "Zero Escape: Virtue's Last Reward",
        'filename': "Zero Escape - Virtue's Last Reward (v02)(USA) (3DS1676).3ds",
        'source_relative': "Handhelds/Nintendo 3DS [2011]/Zero Escape - Virtue's Last Reward (v02)(USA) (3DS1676).3ds",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/n3ds/Zero Escape - Virtue's Last Reward (v02)(USA) (3DS1676).3ds",
        'size': 893897216,
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