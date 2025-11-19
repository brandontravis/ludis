#!/usr/bin/env python3
# Auto-generated migration script for Sega Master System
# 70 games, 11.20 MB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sega Master System'
ESDE_FOLDER = 'mastersystem'
OPERATION = 'copy'

GAMES = [
    {
        'title': 'Aladdin',
        'filename': 'Aladdin.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Aladdin.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Aladdin.zip',
        'size': 287719,
    },
    {
        'title': 'Alex Kidd: High-Tech World',
        'filename': 'Alex Kidd - High-Tech World (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Alex Kidd - High-Tech World (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Alex Kidd - High-Tech World (USA, Europe, Brazil) (En).7z',
        'size': 74572,
    },
    {
        'title': 'Alex Kidd: The Lost Stars',
        'filename': 'Alex Kidd - The Lost Stars.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Alex Kidd - The Lost Stars.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Alex Kidd - The Lost Stars.zip',
        'size': 121623,
    },
    {
        'title': 'Alex Kidd in Miracle World',
        'filename': 'Alex Kidd in Miracle World (USA, Europe, Brazil) (En) (Rev 1).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Alex Kidd in Miracle World (USA, Europe, Brazil) (En) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Alex Kidd in Miracle World (USA, Europe, Brazil) (En) (Rev 1).7z',
        'size': 72610,
    },
    {
        'title': 'Alex Kidd in Miracle World 2',
        'filename': 'Alex Kidd in Miracle World 2.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Alex Kidd in Miracle World 2.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Alex Kidd in Miracle World 2.zip',
        'size': 112217,
    },
    {
        'title': 'Alex Kidd in Shinobi World',
        'filename': 'Alex Kidd in Shinobi World (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Alex Kidd in Shinobi World (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Alex Kidd in Shinobi World (USA, Europe, Brazil) (En).7z',
        'size': 110828,
    },
    {
        'title': 'Alien Syndrome',
        'filename': 'Alien Syndrome (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Alien Syndrome (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Alien Syndrome (USA, Europe, Brazil) (En).7z',
        'size': 112012,
    },
    {
        'title': 'Asterix',
        'filename': 'Asterix.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Asterix.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Asterix.zip',
        'size': 311263,
    },
    {
        'title': 'Batman Returns',
        'filename': 'Batman Returns.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Batman Returns.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Batman Returns.zip',
        'size': 125616,
    },
    {
        'title': 'Battlemaniacs',
        'filename': 'Battletoads in Battlemaniacs.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Battletoads in Battlemaniacs.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Battletoads in Battlemaniacs.zip',
        'size': 146851,
    },
    {
        'title': 'Bubble Bobble',
        'filename': 'Bubble Bobble.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Bubble Bobble.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Bubble Bobble.zip',
        'size': 131483,
    },
    {
        'title': 'California Games',
        'filename': 'California Games (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/California Games (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/California Games (USA, Europe, Brazil) (En).7z',
        'size': 164022,
    },
    {
        'title': 'Castle of Illusion Starring Mickey Mouse',
        'filename': 'Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (En) (Rev 1).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (En) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Castle of Illusion Starring Mickey Mouse (USA, Europe, Brazil) (En) (Rev 1).7z',
        'size': 126063,
    },
    {
        'title': 'Columns',
        'filename': 'Columns (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Columns (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Columns (USA, Europe, Brazil) (En).7z',
        'size': 23117,
    },
    {
        'title': 'Desert Strike',
        'filename': 'Desert Strike - Return to the Gulf.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Desert Strike - Return to the Gulf.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Desert Strike - Return to the Gulf.zip',
        'size': 201899,
    },
    {
        'title': 'Double Dragon',
        'filename': 'Double Dragon.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Double Dragon.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Double Dragon.zip',
        'size': 98426,
    },
    {
        'title': "Dr. Robotnik's Mean Bean Machine",
        'filename': "Dr. Robotnik's Mean Bean Machine.zip",
        'source_relative': "Consoles/Sega Master System (Mark III) [1985]/Dr. Robotnik's Mean Bean Machine.zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Dr. Robotnik's Mean Bean Machine.zip",
        'size': 121560,
    },
    {
        'title': 'Earthworm Jim',
        'filename': 'Earthworm Jim.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Earthworm Jim.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Earthworm Jim.zip',
        'size': 253372,
    },
    {
        'title': 'Ecco: The Tides of Time',
        'filename': 'Ecco - The Tides of Time.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ecco - The Tides of Time.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ecco - The Tides of Time.zip',
        'size': 221853,
    },
    {
        'title': 'Ecco the Dolphin',
        'filename': 'Ecco the Dolphin.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ecco the Dolphin.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ecco the Dolphin.zip',
        'size': 221250,
    },
    {
        'title': 'Enduro Racer',
        'filename': 'Enduro Racer (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Enduro Racer (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Enduro Racer (USA, Europe, Brazil) (En).7z',
        'size': 70743,
    },
    {
        'title': 'Fantasy Zone: The Maze',
        'filename': 'Fantasy Zone - The Maze (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Fantasy Zone - The Maze (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Fantasy Zone - The Maze (USA, Europe, Brazil) (En).7z',
        'size': 59683,
    },
    {
        'title': 'Fantasy Zone II: The Tears of Opa-Opa',
        'filename': 'Fantasy Zone II (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Fantasy Zone II (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Fantasy Zone II (USA, Europe, Brazil) (En).7z',
        'size': 147792,
    },
    {
        'title': 'Ghostbusters',
        'filename': 'Ghostbusters (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ghostbusters (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ghostbusters (USA, Europe, Brazil) (En).7z',
        'size': 59702,
    },
    {
        'title': "Ghouls'n Ghosts",
        'filename': "Ghouls'n Ghosts (USA, Europe, Brazil) (En).7z",
        'source_relative': "Consoles/Sega Master System (Mark III) [1985]/Ghouls'n Ghosts (USA, Europe, Brazil) (En).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ghouls'n Ghosts (USA, Europe, Brazil) (En).7z",
        'size': 141188,
    },
    {
        'title': 'Golden Axe',
        'filename': 'Golden Axe (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Golden Axe (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Golden Axe (USA, Europe, Brazil) (En).7z',
        'size': 222713,
    },
    {
        'title': 'Golden Axe Warrior',
        'filename': 'Golden Axe Warrior (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Golden Axe Warrior (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Golden Axe Warrior (USA, Europe, Brazil) (En).7z',
        'size': 132349,
    },
    {
        'title': 'Golvellius: Valley of Doom',
        'filename': 'Golvellius - Valley of Doom (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Golvellius - Valley of Doom (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Golvellius - Valley of Doom (USA, Europe, Brazil) (En).7z',
        'size': 150821,
    },
    {
        'title': 'Hang-On & Astro Warrior',
        'filename': 'Hang On & Astro Warrior (USA).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Hang On & Astro Warrior (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Hang On & Astro Warrior (USA).7z',
        'size': 57845,
    },
    {
        'title': 'Hang-On & Safari Hunt',
        'filename': 'Hang On & Safari Hunt (USA).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Hang On & Safari Hunt (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Hang On & Safari Hunt (USA).7z',
        'size': 46562,
    },
    {
        'title': "King's Quest: Quest for the Crown",
        'filename': "King's Quest - Quest for the Crown (USA).7z",
        'source_relative': "Consoles/Sega Master System (Mark III) [1985]/King's Quest - Quest for the Crown (USA).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/King's Quest - Quest for the Crown (USA).7z",
        'size': 69768,
    },
    {
        'title': 'Lemmings',
        'filename': 'Lemmings.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Lemmings.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Lemmings.zip',
        'size': 127278,
    },
    {
        'title': 'The Lion King',
        'filename': 'Lion King, The.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Lion King, The.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Lion King, The.zip',
        'size': 282286,
    },
    {
        'title': 'The Lucky Dime Caper starring Donald Duck',
        'filename': 'Lucky Dime Caper Starring Donald Duck, The.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Lucky Dime Caper Starring Donald Duck, The.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Lucky Dime Caper Starring Donald Duck, The.zip',
        'size': 172237,
    },
    {
        'title': 'Marble Madness',
        'filename': 'Marble Madness.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Marble Madness.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Marble Madness.zip',
        'size': 94456,
    },
    {
        'title': "Michael Jackson's Moonwalker",
        'filename': "Michael Jackson's Moonwalker (USA, Europe, Brazil) (En).7z",
        'source_relative': "Consoles/Sega Master System (Mark III) [1985]/Michael Jackson's Moonwalker (USA, Europe, Brazil) (En).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Michael Jackson's Moonwalker (USA, Europe, Brazil) (En).7z",
        'size': 116856,
    },
    {
        'title': 'Missile Defense 3-D',
        'filename': 'Missile Defense 3-D (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Missile Defense 3-D (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Missile Defense 3-D (USA, Europe, Brazil) (En).7z',
        'size': 70856,
    },
    {
        'title': 'Mortal Kombat 3',
        'filename': 'Mortal Kombat 3.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Mortal Kombat 3.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Mortal Kombat 3.zip',
        'size': 273196,
    },
    {
        'title': 'Mortal Kombat II',
        'filename': 'Mortal Kombat II.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Mortal Kombat II.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Mortal Kombat II.zip',
        'size': 394673,
    },
    {
        'title': 'Mortal Kombat',
        'filename': 'Mortal Kombat.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Mortal Kombat.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Mortal Kombat.zip',
        'size': 382089,
    },
    {
        'title': 'Ms. Pac-Man',
        'filename': 'Ms. Pac-Man.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ms. Pac-Man.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ms. Pac-Man.zip',
        'size': 54654,
    },
    {
        'title': 'Ninja Gaiden',
        'filename': 'Ninja Gaiden.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ninja Gaiden.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ninja Gaiden.zip',
        'size': 164070,
    },
    {
        'title': 'OutRun',
        'filename': 'OutRun.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/OutRun.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/OutRun.zip',
        'size': 142547,
    },
    {
        'title': 'Pac-Mania',
        'filename': 'Pac-Mania.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Pac-Mania.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Pac-Mania.zip',
        'size': 56145,
    },
    {
        'title': 'Paperboy',
        'filename': 'Paperboy (USA, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Paperboy (USA, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Paperboy (USA, Brazil) (En).7z',
        'size': 56275,
    },
    {
        'title': 'Phantasy Star',
        'filename': 'Phantasy Star (USA, Europe) (Rev A).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Phantasy Star (USA, Europe) (Rev A).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Phantasy Star (USA, Europe) (Rev A).7z',
        'size': 289435,
    },
    {
        'title': 'Prince of Persia',
        'filename': 'Prince of Persia.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Prince of Persia.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Prince of Persia.zip',
        'size': 112626,
    },
    {
        'title': 'Psycho Fox',
        'filename': 'Psycho Fox (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Psycho Fox (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Psycho Fox (USA, Europe, Brazil) (En).7z',
        'size': 87410,
    },
    {
        'title': 'R-Type',
        'filename': 'R-Type (World).sms',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/R-Type (World).sms',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/R-Type (World).sms',
        'size': 524288,
    },
    {
        'title': 'Rampage',
        'filename': 'Rampage (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Rampage (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Rampage (USA, Europe, Brazil) (En).7z',
        'size': 103626,
    },
    {
        'title': 'Rescue Mission',
        'filename': 'Rescue Mission (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Rescue Mission (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Rescue Mission (USA, Europe, Brazil) (En).7z',
        'size': 69025,
    },
    {
        'title': 'Shinobi',
        'filename': 'Shinobi (USA, Europe, Brazil) (En) (Rev 1).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Shinobi (USA, Europe, Brazil) (En) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Shinobi (USA, Europe, Brazil) (En) (Rev 1).7z',
        'size': 121415,
    },
    {
        'title': 'The Simpsons: Bart vs. the Space Mutants',
        'filename': 'Simpsons, The - Bart vs. the Space Mutants (Europe, Brazil).sms',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Simpsons, The - Bart vs. the Space Mutants (Europe, Brazil).sms',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Simpsons, The - Bart vs. the Space Mutants (Europe, Brazil).sms',
        'size': 262144,
    },
    {
        'title': 'The Simpsons: Bart vs. the World',
        'filename': 'Simpsons, The - Bart vs. the World (Europe, Brazil).sms',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Simpsons, The - Bart vs. the World (Europe, Brazil).sms',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Simpsons, The - Bart vs. the World (Europe, Brazil).sms',
        'size': 262144,
    },
    {
        'title': 'Sonic Blast',
        'filename': 'Sonic Blast.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Sonic Blast.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Sonic Blast.zip',
        'size': 460336,
    },
    {
        'title': 'Sonic Chaos',
        'filename': 'Sonic Chaos.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Sonic Chaos.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Sonic Chaos.zip',
        'size': 210427,
    },
    {
        'title': 'Sonic Spinball',
        'filename': 'Sonic Spinball.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Sonic Spinball.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Sonic Spinball.zip',
        'size': 235423,
    },
    {
        'title': 'Sonic the Hedgehog',
        'filename': 'Sonic The Hedgehog (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Sonic The Hedgehog (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Sonic The Hedgehog (USA, Europe, Brazil) (En).7z',
        'size': 131788,
    },
    {
        'title': 'Sonic the Hedgehog 2',
        'filename': 'Sonic the Hedgehog 2.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Sonic the Hedgehog 2.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Sonic the Hedgehog 2.zip',
        'size': 219291,
    },
    {
        'title': 'Star Wars',
        'filename': 'Star Wars.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Star Wars.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Star Wars.zip',
        'size': 289275,
    },
    {
        'title': "Street Fighter II'",
        'filename': "Street Fighter II'.zip",
        'source_relative': "Consoles/Sega Master System (Mark III) [1985]/Street Fighter II'.zip",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Street Fighter II'.zip",
        'size': 397716,
    },
    {
        'title': 'Streets of Rage II',
        'filename': 'Streets of Rage 2.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Streets of Rage 2.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Streets of Rage 2.zip',
        'size': 257941,
    },
    {
        'title': 'Streets of Rage',
        'filename': 'Streets of Rage.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Streets of Rage.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Streets of Rage.zip',
        'size': 212003,
    },
    {
        'title': 'Strider',
        'filename': 'Strider (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Strider (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Strider (USA, Europe, Brazil) (En).7z',
        'size': 118498,
    },
    {
        'title': 'Super Monaco GP',
        'filename': 'Super Monaco GP (USA).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Super Monaco GP (USA).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Super Monaco GP (USA).7z',
        'size': 88401,
    },
    {
        'title': 'Ultima IV: Quest of the Avatar',
        'filename': 'Ultima IV - Quest of the Avatar.zip',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ultima IV - Quest of the Avatar.zip',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ultima IV - Quest of the Avatar.zip',
        'size': 243030,
    },
    {
        'title': 'Wonder Boy',
        'filename': 'Wonder Boy (USA, Europe, Brazil) (En) (Rev 1).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Wonder Boy (USA, Europe, Brazil) (En) (Rev 1).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Wonder Boy (USA, Europe, Brazil) (En) (Rev 1).7z',
        'size': 70370,
    },
    {
        'title': "Wonder Boy III: The Dragon's Trap",
        'filename': "Wonder Boy III - The Dragon's Trap (USA, Europe).7z",
        'source_relative': "Consoles/Sega Master System (Mark III) [1985]/Wonder Boy III - The Dragon's Trap (USA, Europe).7z",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Wonder Boy III - The Dragon's Trap (USA, Europe).7z",
        'size': 121893,
    },
    {
        'title': 'Wonder Boy in Monster Land',
        'filename': 'Wonder Boy in Monster Land (USA, Europe).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Wonder Boy in Monster Land (USA, Europe).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Wonder Boy in Monster Land (USA, Europe).7z',
        'size': 117566,
    },
    {
        'title': 'Ys: The Vanished Omens',
        'filename': 'Ys - The Vanished Omens (USA, Europe, Brazil) (En).7z',
        'source_relative': 'Consoles/Sega Master System (Mark III) [1985]/Ys - The Vanished Omens (USA, Europe, Brazil) (En).7z',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/mastersystem/Ys - The Vanished Omens (USA, Europe, Brazil) (En).7z',
        'size': 157991,
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