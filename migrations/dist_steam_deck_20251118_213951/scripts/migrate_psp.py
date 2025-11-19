#!/usr/bin/env python3
# Auto-generated migration script for Sony PSP
# 132 games, 118.22 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Sony PSP'
ESDE_FOLDER = 'psp'
OPERATION = 'copy'

GAMES = [
    {
        'title': "Assassin's Creed: Bloodlines",
        'filename': "Assassin's Creed - Bloodlines (USA) (En,Fr,De,Es,It).iso",
        'source_relative': "Handhelds/Sony PSP [2004]/Assassin's Creed - Bloodlines (USA) (En,Fr,De,Es,It).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Assassin's Creed - Bloodlines (USA) (En,Fr,De,Es,It).iso",
        'size': 809566208,
    },
    {
        'title': 'Atari Classics Evolved',
        'filename': 'Atari Classics Evolved (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Atari Classics Evolved (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Atari Classics Evolved (USA).iso',
        'size': 83984384,
    },
    {
        'title': 'Bomberman',
        'filename': 'Bomberman (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Bomberman (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Bomberman (USA).iso',
        'size': 110002176,
    },
    {
        'title': 'Bomberman Land',
        'filename': 'Bomberman Land (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Bomberman Land (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Bomberman Land (USA).iso',
        'size': 357171200,
    },
    {
        'title': 'Burnout Legends',
        'filename': 'Burnout Legends (USA) (En,Fr,De,Es,It,Nl) (v2.00).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Burnout Legends (USA) (En,Fr,De,Es,It,Nl) (v2.00).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Burnout Legends (USA) (En,Fr,De,Es,It,Nl) (v2.00).iso',
        'size': 505905152,
    },
    {
        'title': 'Burnout Legends',
        'filename': 'Burnout Legends (USA) (En,Fr,De,Es,It,Nl) (v2.00).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Burnout Legends (USA) (En,Fr,De,Es,It,Nl) (v2.00).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Burnout Legends (USA) (En,Fr,De,Es,It,Nl) (v2.00).iso',
        'size': 500301824,
    },
    {
        'title': 'Call of Duty: Roads to Victory',
        'filename': 'Call of Duty - Roads to Victory (USA) (En,Ja,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Call of Duty - Roads to Victory (USA) (En,Ja,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Call of Duty - Roads to Victory (USA) (En,Ja,Fr,De,Es,It).iso',
        'size': 640974848,
    },
    {
        'title': 'Capcom Classics Collection: Reloaded',
        'filename': 'Capcom Classics Collection Reloaded (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Capcom Classics Collection Reloaded (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Capcom Classics Collection Reloaded (USA).iso',
        'size': 633110528,
    },
    {
        'title': 'Capcom Classics Collection: Remixed',
        'filename': 'Capcom Classics Collection Remixed (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Capcom Classics Collection Remixed (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Capcom Classics Collection Remixed (USA).iso',
        'size': 571965440,
    },
    {
        'title': 'Castlevania: The Dracula X Chronicles',
        'filename': 'Castlevania - The Dracula X Chronicles (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Castlevania - The Dracula X Chronicles (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Castlevania - The Dracula X Chronicles (USA).iso',
        'size': 1111359488,
    },
    {
        'title': 'Crash: Mind Over Mutant',
        'filename': 'Crash - Mind over Mutant (USA) (En,Fr).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Crash - Mind over Mutant (USA) (En,Fr).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Crash - Mind over Mutant (USA) (En,Fr).iso',
        'size': 1576468480,
    },
    {
        'title': 'Crash of the Titans',
        'filename': 'Crash of the Titans (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Crash of the Titans (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Crash of the Titans (USA).iso',
        'size': 817135616,
    },
    {
        'title': 'Crash Tag Team Racing',
        'filename': 'Crash Tag Team Racing (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Crash Tag Team Racing (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Crash Tag Team Racing (USA).iso',
        'size': 1536065536,
    },
    {
        'title': 'Crazy Taxi: Fare Wars',
        'filename': 'Crazy Taxi - Fare Wars (USA) (v1.01).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Crazy Taxi - Fare Wars (USA) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Crazy Taxi - Fare Wars (USA) (v1.01).iso',
        'size': 906330112,
    },
    {
        'title': 'Crazy Taxi: Fare Wars',
        'filename': 'Crazy Taxi - Fare Wars (USA) (v1.01).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Crazy Taxi - Fare Wars (USA) (v1.01).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Crazy Taxi - Fare Wars (USA) (v1.01).iso',
        'size': 555909120,
    },
    {
        'title': 'Crisis Core: Final Fantasy VII',
        'filename': 'Crisis Core - Final Fantasy VII (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Crisis Core - Final Fantasy VII (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Crisis Core - Final Fantasy VII (USA).iso',
        'size': 1716715520,
    },
    {
        'title': 'Daxter',
        'filename': 'Daxter (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Daxter (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Daxter (USA) (En,Fr,De,Es,It).iso',
        'size': 1405845504,
    },
    {
        'title': 'Dead or Alive: Paradise',
        'filename': 'Dead or Alive - Paradise (USA) (En,Ja,Fr,De).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Dead or Alive - Paradise (USA) (En,Ja,Fr,De).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Dead or Alive - Paradise (USA) (En,Ja,Fr,De).iso',
        'size': 869990400,
    },
    {
        'title': 'Dead to Rights: Reckoning',
        'filename': 'Dead to Rights - Reckoning (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Dead to Rights - Reckoning (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Dead to Rights - Reckoning (USA).iso',
        'size': 193167360,
    },
    {
        'title': 'Dissidia 012: Final Fantasy',
        'filename': 'Dissidia 012 - Duodecim Final Fantasy (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Dissidia 012 - Duodecim Final Fantasy (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Dissidia 012 - Duodecim Final Fantasy (USA) (En,Fr,De,Es,It).iso',
        'size': 1754529792,
    },
    {
        'title': 'Dissidia: Final Fantasy',
        'filename': 'Dissidia Final Fantasy (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Dissidia Final Fantasy (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Dissidia Final Fantasy (USA).iso',
        'size': 1646657536,
    },
    {
        'title': 'Family Guy Video Game!',
        'filename': 'Family Guy - Video Game! (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Family Guy - Video Game! (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Family Guy - Video Game! (USA).iso',
        'size': 1186463744,
    },
    {
        'title': 'Final Fantasy',
        'filename': 'Final Fantasy - 20th Anniversary Edition (USA) (En,Ja) (FW3.03).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Final Fantasy - 20th Anniversary Edition (USA) (En,Ja) (FW3.03).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Final Fantasy - 20th Anniversary Edition (USA) (En,Ja) (FW3.03).iso',
        'size': 198115328,
    },
    {
        'title': 'Final Fantasy IV: The Complete Collection',
        'filename': 'Final Fantasy IV - The Complete Collection (USA) (En,Ja,Fr).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Final Fantasy IV - The Complete Collection (USA) (En,Ja,Fr).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Final Fantasy IV - The Complete Collection (USA) (En,Ja,Fr).iso',
        'size': 880771072,
    },
    {
        'title': 'Final Fantasy Tactics: The War of the Lions',
        'filename': 'Final Fantasy Tactics - The War of the Lions (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Final Fantasy Tactics - The War of the Lions (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Final Fantasy Tactics - The War of the Lions (USA).iso',
        'size': 418873344,
    },
    {
        'title': 'Frogger: Helmet Chaos',
        'filename': 'Frogger - Helmet Chaos (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Frogger - Helmet Chaos (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Frogger - Helmet Chaos (USA).iso',
        'size': 452526080,
    },
    {
        'title': 'Ghostbusters: The Video Game',
        'filename': 'Ghostbusters - The Video Game (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Ghostbusters - The Video Game (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Ghostbusters - The Video Game (USA).iso',
        'size': 1175552000,
    },
    {
        'title': 'God of War: Chains of Olympus',
        'filename': 'God of War - Chains of Olympus (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/God of War - Chains of Olympus (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/God of War - Chains of Olympus (USA).iso',
        'size': 1605664768,
    },
    {
        'title': 'God of War: Ghost of Sparta',
        'filename': 'God of War - Ghost of Sparta (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/God of War - Ghost of Sparta (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/God of War - Ghost of Sparta (USA) (En,Fr,Es).iso',
        'size': 1747714048,
    },
    {
        'title': 'The Golden Compass',
        'filename': 'Golden Compass, The (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Golden Compass, The (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Golden Compass, The (USA).iso',
        'size': 1265860608,
    },
    {
        'title': 'Gran Turismo',
        'filename': 'Gran Turismo (USA) (En,Fr,Es) (v2.00).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Gran Turismo (USA) (En,Fr,Es) (v2.00).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Gran Turismo (USA) (En,Fr,Es) (v2.00).iso',
        'size': 1097826304,
    },
    {
        'title': 'Grand Theft Auto: Chinatown Wars',
        'filename': 'Grand Theft Auto - Chinatown Wars (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Grand Theft Auto - Chinatown Wars (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Grand Theft Auto - Chinatown Wars (USA).iso',
        'size': 904298496,
    },
    {
        'title': 'Grand Theft Auto: Liberty City Stories',
        'filename': 'Grand Theft Auto - Liberty City Stories (USA) (En,Fr,De,Es,It) (v3.00).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Grand Theft Auto - Liberty City Stories (USA) (En,Fr,De,Es,It) (v3.00).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Grand Theft Auto - Liberty City Stories (USA) (En,Fr,De,Es,It) (v3.00).iso',
        'size': 1255243776,
    },
    {
        'title': 'Grand Theft Auto: Vice City Stories',
        'filename': 'Grand Theft Auto - Vice City Stories (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Grand Theft Auto - Vice City Stories (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Grand Theft Auto - Vice City Stories (USA).iso',
        'size': 1696006144,
    },
    {
        'title': 'Harry Potter and the Goblet of Fire',
        'filename': 'Harry Potter and the Goblet of Fire (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Harry Potter and the Goblet of Fire (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Harry Potter and the Goblet of Fire (USA).iso',
        'size': 410320896,
    },
    {
        'title': 'Harry Potter and the Half-Blood Prince',
        'filename': 'Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Harry Potter and the Half-Blood Prince (USA) (En,Fr,Es).iso',
        'size': 408027136,
    },
    {
        'title': 'Harry Potter and the Order of the Phoenix',
        'filename': 'Harry Potter and the Order of the Phoenix (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Harry Potter and the Order of the Phoenix (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Harry Potter and the Order of the Phoenix (USA).iso',
        'size': 763461632,
    },
    {
        'title': 'Harvest Moon: Boy & Girl',
        'filename': 'Harvest Moon - Boy & Girl (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Harvest Moon - Boy & Girl (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Harvest Moon - Boy & Girl (USA).iso',
        'size': 341508096,
    },
    {
        'title': 'Harvest Moon: Hero of Leaf Valley',
        'filename': 'Harvest Moon - Hero of Leaf Valley (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Harvest Moon - Hero of Leaf Valley (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Harvest Moon - Hero of Leaf Valley (USA).iso',
        'size': 421429248,
    },
    {
        'title': 'Jak and Daxter: The Lost Frontier',
        'filename': 'Jak and Daxter - The Lost Frontier (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Jak and Daxter - The Lost Frontier (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Jak and Daxter - The Lost Frontier (USA) (En,Fr,Es).iso',
        'size': 1453916160,
    },
    {
        'title': "James Cameron's Avatar: The Game",
        'filename': "James Cameron's Avatar - The Game (USA) (En,Fr,Es).iso",
        'source_relative': "Handhelds/Sony PSP [2004]/James Cameron's Avatar - The Game (USA) (En,Fr,Es).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/James Cameron's Avatar - The Game (USA) (En,Fr,Es).iso",
        'size': 695107584,
    },
    {
        'title': "Jeanne d'Arc",
        'filename': "Jeanne d'Arc (USA).iso",
        'source_relative': "Handhelds/Sony PSP [2004]/Jeanne d'Arc (USA).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Jeanne d'Arc (USA).iso",
        'size': 1247412224,
    },
    {
        'title': 'Killzone: Liberation',
        'filename': 'Killzone - Liberation (USA) (En,Fr,De,Es,It,Nl,Pl,Ru).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Killzone - Liberation (USA) (En,Fr,De,Es,It,Nl,Pl,Ru).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Killzone - Liberation (USA) (En,Fr,De,Es,It,Nl,Pl,Ru).iso',
        'size': 581632000,
    },
    {
        'title': 'Kingdom Hearts: Birth by Sleep',
        'filename': 'Kingdom Hearts - Birth by Sleep (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Kingdom Hearts - Birth by Sleep (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Kingdom Hearts - Birth by Sleep (USA) (En,Fr,Es).iso',
        'size': 1767473152,
    },
    {
        'title': 'Lara Croft: Tomb Raider: Anniversary',
        'filename': 'Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Lara Croft Tomb Raider - Anniversary (USA) (En,Fr,De,Es,It).iso',
        'size': 1291190272,
    },
    {
        'title': 'Lara Croft Tomb Raider: Legend',
        'filename': 'Lara Croft Tomb Raider - Legend (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Lara Croft Tomb Raider - Legend (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Lara Croft Tomb Raider - Legend (USA) (En,Fr,De,Es,It).iso',
        'size': 1514995712,
    },
    {
        'title': 'LEGO Batman: The Videogame',
        'filename': 'LEGO Batman - The Videogame (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Batman - The Videogame (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Batman - The Videogame (USA) (En,Fr,Es).iso',
        'size': 1136689152,
    },
    {
        'title': 'LEGO Harry Potter: Years 1-4',
        'filename': 'LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Harry Potter - Years 1-4 (USA) (En,Fr,Es).iso',
        'size': 1425866752,
    },
    {
        'title': 'LEGO Harry Potter: Years 5-7',
        'filename': 'LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es,Pt).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es,Pt).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Harry Potter - Years 5-7 (USA) (En,Fr,Es,Pt).iso',
        'size': 1513422848,
    },
    {
        'title': 'LEGO Indiana Jones: The Original Adventures',
        'filename': 'LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Indiana Jones - The Original Adventures (USA) (En,Fr,Es).iso',
        'size': 1241153536,
    },
    {
        'title': 'LEGO Indiana Jones 2: The Adventure Continues',
        'filename': 'LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Indiana Jones 2 - The Adventure Continues (USA) (En,Fr,Es).iso',
        'size': 677511168,
    },
    {
        'title': 'LEGO Pirates of the Caribbean: The Video Game',
        'filename': 'LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Pirates of the Caribbean - The Video Game (USA) (En,Fr,Es).iso',
        'size': 1478459392,
    },
    {
        'title': 'LEGO Star Wars II: The Original Trilogy',
        'filename': 'LEGO Star Wars II - The Original Trilogy (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Star Wars II - The Original Trilogy (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Star Wars II - The Original Trilogy (USA).iso',
        'size': 1225359360,
    },
    {
        'title': 'LEGO Star Wars III: The Clone Wars',
        'filename': 'LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LEGO Star Wars III - The Clone Wars (USA) (En,Fr,Es).iso',
        'size': 1746796544,
    },
    {
        'title': 'Lemmings',
        'filename': 'Lemmings (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Lemmings (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Lemmings (USA).iso',
        'size': 471498752,
    },
    {
        'title': 'LittleBigPlanet',
        'filename': 'LittleBigPlanet (USA) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Pl).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LittleBigPlanet (USA) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Pl).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LittleBigPlanet (USA) (En,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Pl).iso',
        'size': 1506869248,
    },
    {
        'title': 'LocoRoco',
        'filename': 'LocoRoco (USA) (En,Ja,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Zh,Ko,Ru).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LocoRoco (USA) (En,Ja,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Zh,Ko,Ru).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LocoRoco (USA) (En,Ja,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Zh,Ko,Ru).iso',
        'size': 589758464,
    },
    {
        'title': 'LocoRoco 2',
        'filename': 'LocoRoco 2 (USA) (En,Ja,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Ko,Ru).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/LocoRoco 2 (USA) (En,Ja,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Ko,Ru).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/LocoRoco 2 (USA) (En,Ja,Fr,De,Es,It,Nl,Pt,Sv,No,Da,Fi,Ko,Ru).iso',
        'size': 1805778944,
    },
    {
        'title': 'Manhunt 2',
        'filename': 'Manhunt 2 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Manhunt 2 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Manhunt 2 (USA).iso',
        'size': 1299513344,
    },
    {
        'title': 'Mega Man Maverick Hunter X',
        'filename': 'Mega Man - Maverick Hunter X (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Mega Man - Maverick Hunter X (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Mega Man - Maverick Hunter X (USA).iso',
        'size': 470515712,
    },
    {
        'title': 'Mega Man Powered Up',
        'filename': 'Mega Man - Powered Up (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Mega Man - Powered Up (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Mega Man - Powered Up (USA).iso',
        'size': 311721984,
    },
    {
        'title': 'Metal Gear Ac!d',
        'filename': 'Metal Gear Ac!d (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Gear Ac!d (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Gear Ac!d (USA).iso',
        'size': 201392128,
    },
    {
        'title': 'Metal Gear Ac!d 2',
        'filename': 'Metal Gear Ac!d 2 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Gear Ac!d 2 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Gear Ac!d 2 (USA).iso',
        'size': 917307392,
    },
    {
        'title': 'Metal Gear Solid: Digital Graphic Novel',
        'filename': 'Metal Gear Solid - Digital Graphic Novel (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Gear Solid - Digital Graphic Novel (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Gear Solid - Digital Graphic Novel (USA).iso',
        'size': 978124800,
    },
    {
        'title': 'Metal Gear Solid: Peace Walker',
        'filename': 'Metal Gear Solid - Peace Walker (USA) (En,Fr,Es) (v2.00).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Gear Solid - Peace Walker (USA) (En,Fr,Es) (v2.00).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Gear Solid - Peace Walker (USA) (En,Fr,Es) (v2.00).iso',
        'size': 1645936640,
    },
    {
        'title': 'Metal Gear Solid: Portable Ops',
        'filename': 'Metal Gear Solid - Portable Ops (USA) (v1.02).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Gear Solid - Portable Ops (USA) (v1.02).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Gear Solid - Portable Ops (USA) (v1.02).iso',
        'size': 1393426432,
    },
    {
        'title': 'Metal Gear Solid: Portable Ops Plus',
        'filename': 'Metal Gear Solid - Portable Ops Plus (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Gear Solid - Portable Ops Plus (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Gear Solid - Portable Ops Plus (USA).iso',
        'size': 1248067584,
    },
    {
        'title': 'Metal Slug Anthology',
        'filename': 'Metal Slug Anthology (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Slug Anthology (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Slug Anthology (USA).iso',
        'size': 1328939008,
    },
    {
        'title': 'Metal Slug XX',
        'filename': 'Metal Slug XX (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Metal Slug XX (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Metal Slug XX (USA).iso',
        'size': 463732736,
    },
    {
        'title': 'Michael Jackson: The Experience',
        'filename': 'Michael Jackson - The Experience (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Michael Jackson - The Experience (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Michael Jackson - The Experience (USA).iso',
        'size': 339443712,
    },
    {
        'title': 'Monster Hunter Freedom',
        'filename': 'Monster Hunter Freedom (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Monster Hunter Freedom (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Monster Hunter Freedom (USA).iso',
        'size': 741277696,
    },
    {
        'title': 'Monster Hunter Freedom 2',
        'filename': 'Monster Hunter Freedom 2 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Monster Hunter Freedom 2 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Monster Hunter Freedom 2 (USA).iso',
        'size': 837156864,
    },
    {
        'title': 'Monster Hunter: Freedom Unite',
        'filename': 'Monster Hunter Freedom Unite (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Monster Hunter Freedom Unite (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Monster Hunter Freedom Unite (USA) (En,Fr,De,Es,It).iso',
        'size': 886702080,
    },
    {
        'title': 'Mortal Kombat: Unchained',
        'filename': 'Mortal Kombat - Unchained (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Mortal Kombat - Unchained (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Mortal Kombat - Unchained (USA).iso',
        'size': 1568899072,
    },
    {
        'title': 'MotorStorm: Arctic Edge',
        'filename': 'MotorStorm - Arctic Edge (USA) (En,Fr,De,Es,It,Nl,Pt,Ru).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/MotorStorm - Arctic Edge (USA) (En,Fr,De,Es,It,Nl,Pt,Ru).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/MotorStorm - Arctic Edge (USA) (En,Fr,De,Es,It,Nl,Pt,Ru).iso',
        'size': 870809600,
    },
    {
        'title': 'MTV Pimp My Ride',
        'filename': 'MTV Pimp My Ride (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/MTV Pimp My Ride (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/MTV Pimp My Ride (USA).iso',
        'size': 833650688,
    },
    {
        'title': 'Namco Museum: Battle Collection',
        'filename': 'Namco Museum Battle Collection (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Namco Museum Battle Collection (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Namco Museum Battle Collection (USA).iso',
        'size': 174358528,
    },
    {
        'title': 'Napoleon Dynamite: The Game',
        'filename': 'Napoleon Dynamite - The Game (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Napoleon Dynamite - The Game (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Napoleon Dynamite - The Game (USA).iso',
        'size': 657883136,
    },
    {
        'title': 'Need for Speed: Carbon: Own the City',
        'filename': 'Need for Speed - Carbon - Own the City (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Need for Speed - Carbon - Own the City (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Need for Speed - Carbon - Own the City (USA).iso',
        'size': 894173184,
    },
    {
        'title': 'Need for Speed: Most Wanted 5-1-0',
        'filename': 'Need for Speed - Most Wanted - 5-1-0 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Need for Speed - Most Wanted - 5-1-0 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Need for Speed - Most Wanted - 5-1-0 (USA).iso',
        'size': 926580736,
    },
    {
        'title': 'Need for Speed: ProStreet',
        'filename': 'Need for Speed - ProStreet (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Need for Speed - ProStreet (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Need for Speed - ProStreet (USA).iso',
        'size': 896270336,
    },
    {
        'title': 'Need for Speed: Shift',
        'filename': 'Need for Speed - Shift (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Need for Speed - Shift (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Need for Speed - Shift (USA).iso',
        'size': 1798471680,
    },
    {
        'title': 'Need for Speed: Undercover',
        'filename': 'Need for Speed - Undercover (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Need for Speed - Undercover (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Need for Speed - Undercover (USA).iso',
        'size': 1304690688,
    },
    {
        'title': 'Need for Speed: Underground Rivals',
        'filename': 'Need for Speed - Underground Rivals (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Need for Speed - Underground Rivals (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Need for Speed - Underground Rivals (USA).iso',
        'size': 884801536,
    },
    {
        'title': 'OutRun 2006: Coast 2 Coast',
        'filename': 'OutRun 2006 - Coast 2 Coast (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/OutRun 2006 - Coast 2 Coast (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/OutRun 2006 - Coast 2 Coast (USA).iso',
        'size': 634781696,
    },
    {
        'title': 'Pac-Man World 3',
        'filename': 'Pac-Man World 3 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Pac-Man World 3 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Pac-Man World 3 (USA).iso',
        'size': 494239744,
    },
    {
        'title': 'Pac-Man World Rally',
        'filename': 'Pac-Man World Rally (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Pac-Man World Rally (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Pac-Man World Rally (USA).iso',
        'size': 432701440,
    },
    {
        'title': 'PaRappa the Rapper',
        'filename': 'PaRappa the Rapper (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/PaRappa the Rapper (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/PaRappa the Rapper (USA).iso',
        'size': 377290752,
    },
    {
        'title': 'Patapon',
        'filename': 'Patapon (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Patapon (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Patapon (USA).iso',
        'size': 341016576,
    },
    {
        'title': 'Patapon 2',
        'filename': 'Patapon 2 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Patapon 2 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Patapon 2 (USA).iso',
        'size': 586711040,
    },
    {
        'title': 'Patapon 3',
        'filename': 'Patapon 3 (USA) (En,Fr,Es,Pt).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Patapon 3 (USA) (En,Fr,Es,Pt).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Patapon 3 (USA) (En,Fr,Es,Pt).iso',
        'size': 556007424,
    },
    {
        'title': 'Pipe Mania',
        'filename': 'Pipe Mania (USA) (En,Fr).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Pipe Mania (USA) (En,Fr).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Pipe Mania (USA) (En,Fr).iso',
        'size': 321847296,
    },
    {
        'title': 'Prince of Persia: Revelations',
        'filename': 'Prince of Persia - Revelations (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Prince of Persia - Revelations (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Prince of Persia - Revelations (USA) (En,Fr,Es).iso',
        'size': 1696006144,
    },
    {
        'title': 'Prince of Persia: Rival Swords',
        'filename': 'Prince of Persia - Rival Swords (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Prince of Persia - Rival Swords (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Prince of Persia - Rival Swords (USA) (En,Fr,Es).iso',
        'size': 1269956608,
    },
    {
        'title': 'Prince of Persia: The Forgotten Sands',
        'filename': 'Prince of Persia - The Forgotten Sands (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Prince of Persia - The Forgotten Sands (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Prince of Persia - The Forgotten Sands (USA) (En,Fr,Es).iso',
        'size': 691437568,
    },
    {
        'title': 'Ratchet & Clank: Size Matters',
        'filename': 'Ratchet & Clank - Size Matters (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Ratchet & Clank - Size Matters (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Ratchet & Clank - Size Matters (USA) (En,Fr,De,Es,It).iso',
        'size': 961282048,
    },
    {
        'title': 'Resistance: Retribution',
        'filename': 'Resistance - Retribution (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Resistance - Retribution (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Resistance - Retribution (USA) (En,Fr,Es).iso',
        'size': 1669726208,
    },
    {
        'title': 'Ridge Racer',
        'filename': 'Ridge Racer (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Ridge Racer (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Ridge Racer (USA) (En,Fr,De,Es,It).iso',
        'size': 906362880,
    },
    {
        'title': 'Rock Band Unplugged',
        'filename': 'Rock Band Unplugged (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Rock Band Unplugged (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Rock Band Unplugged (USA).iso',
        'size': 1342275584,
    },
    {
        'title': 'Secret Agent Clank',
        'filename': 'Secret Agent Clank (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Secret Agent Clank (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Secret Agent Clank (USA) (En,Fr,De,Es,It).iso',
        'size': 1516077056,
    },
    {
        'title': 'Sega Genesis Collection',
        'filename': 'Sega Genesis Collection (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Sega Genesis Collection (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Sega Genesis Collection (USA).iso',
        'size': 856358912,
    },
    {
        'title': 'Shaun White Snowboarding',
        'filename': 'Shaun White Snowboarding (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Shaun White Snowboarding (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Shaun White Snowboarding (USA).iso',
        'size': 491454464,
    },
    {
        'title': 'Shin Megami Tensei: Persona',
        'filename': 'Shin Megami Tensei - Persona (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Shin Megami Tensei - Persona (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Shin Megami Tensei - Persona (USA).iso',
        'size': 820740096,
    },
    {
        'title': 'Shin Megami Tensei: Persona 2: Innocent Sin',
        'filename': 'Shin Megami Tensei - Persona 2 - Innocent Sin (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Shin Megami Tensei - Persona 2 - Innocent Sin (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Shin Megami Tensei - Persona 2 - Innocent Sin (USA).iso',
        'size': 1130889216,
    },
    {
        'title': 'Shin Megami Tensei: Persona 3 Portable',
        'filename': 'Shin Megami Tensei - Persona 3 Portable (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Shin Megami Tensei - Persona 3 Portable (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Shin Megami Tensei - Persona 3 Portable (USA).iso',
        'size': 1321861120,
    },
    {
        'title': 'The Simpsons Game',
        'filename': 'Simpsons Game, The (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Simpsons Game, The (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Simpsons Game, The (USA).iso',
        'size': 764805120,
    },
    {
        'title': 'The Sims 2',
        'filename': 'Sims 2, The (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Sims 2, The (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Sims 2, The (USA).iso',
        'size': 1115553792,
    },
    {
        'title': 'The Sims 2: Castaway',
        'filename': 'Sims 2, The - Castaway (USA) (En,Fr,De,Es,It,Nl,Pt).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Sims 2, The - Castaway (USA) (En,Fr,De,Es,It,Nl,Pt).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Sims 2, The - Castaway (USA) (En,Fr,De,Es,It,Nl,Pt).iso',
        'size': 1034158080,
    },
    {
        'title': 'The Sims 2: Pets',
        'filename': 'Sims 2, The - Pets (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Sims 2, The - Pets (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Sims 2, The - Pets (USA).iso',
        'size': 1517813760,
    },
    {
        'title': 'SNK Arcade Classics Vol. 1',
        'filename': 'SNK Arcade Classics Vol. 1 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/SNK Arcade Classics Vol. 1 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/SNK Arcade Classics Vol. 1 (USA).iso',
        'size': 1397620736,
    },
    {
        'title': 'Sonic Rivals',
        'filename': 'Sonic Rivals (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Sonic Rivals (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Sonic Rivals (USA).iso',
        'size': 246087680,
    },
    {
        'title': 'Sonic Rivals 2',
        'filename': 'Sonic Rivals 2 (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Sonic Rivals 2 (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Sonic Rivals 2 (USA).iso',
        'size': 515866624,
    },
    {
        'title': 'Soulcalibur: Broken Destiny',
        'filename': 'Soulcalibur - Broken Destiny (USA) (En,Ja,Fr,De,Es,It,Ru).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Soulcalibur - Broken Destiny (USA) (En,Ja,Fr,De,Es,It,Ru).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Soulcalibur - Broken Destiny (USA) (En,Ja,Fr,De,Es,It,Ru).iso',
        'size': 900923392,
    },
    {
        'title': 'Space Invaders Extreme',
        'filename': 'Space Invaders Extreme (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Space Invaders Extreme (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Space Invaders Extreme (USA) (En,Fr,De,Es,It).iso',
        'size': 153780224,
    },
    {
        'title': 'SSX on Tour',
        'filename': 'SSX On Tour (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/SSX On Tour (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/SSX On Tour (USA).iso',
        'size': 1414037504,
    },
    {
        'title': 'Star Ocean: First Departure',
        'filename': 'Star Ocean - First Departure (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Ocean - First Departure (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Ocean - First Departure (USA).iso',
        'size': 1150746624,
    },
    {
        'title': 'Star Ocean: Second Evolution',
        'filename': 'Star Ocean - Second Evolution (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Ocean - Second Evolution (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Ocean - Second Evolution (USA).iso',
        'size': 1439825920,
    },
    {
        'title': 'Star Wars: Battlefront II',
        'filename': 'Star Wars - Battlefront II (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Wars - Battlefront II (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Wars - Battlefront II (USA).iso',
        'size': 738656256,
    },
    {
        'title': 'Star Wars: Lethal Alliance',
        'filename': 'Star Wars - Lethal Alliance (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Wars - Lethal Alliance (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Wars - Lethal Alliance (USA) (En,Fr,De,Es,It).iso',
        'size': 899547136,
    },
    {
        'title': 'Star Wars: The Clone Wars: Republic Heroes',
        'filename': 'Star Wars - The Clone Wars - Republic Heroes (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Wars - The Clone Wars - Republic Heroes (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Wars - The Clone Wars - Republic Heroes (USA) (En,Fr,Es).iso',
        'size': 1478393856,
    },
    {
        'title': 'Star Wars: The Force Unleashed',
        'filename': 'Star Wars - The Force Unleashed (USA) (En,Fr).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Wars - The Force Unleashed (USA) (En,Fr).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Wars - The Force Unleashed (USA) (En,Fr).iso',
        'size': 1111490560,
    },
    {
        'title': 'Star Wars Battlefront: Elite Squadron',
        'filename': 'Star Wars Battlefront - Elite Squadron (USA) (En,Fr,Es).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Wars Battlefront - Elite Squadron (USA) (En,Fr,Es).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Wars Battlefront - Elite Squadron (USA) (En,Fr,Es).iso',
        'size': 1473740800,
    },
    {
        'title': 'Star Wars Battlefront: Renegade Squadron',
        'filename': 'Star Wars Battlefront - Renegade Squadron (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Star Wars Battlefront - Renegade Squadron (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Star Wars Battlefront - Renegade Squadron (USA).iso',
        'size': 930545664,
    },
    {
        'title': 'Super Monkey Ball Adventure',
        'filename': 'Super Monkey Ball Adventure (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Super Monkey Ball Adventure (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Super Monkey Ball Adventure (USA).iso',
        'size': 423657472,
    },
    {
        'title': 'Syphon Filter: Dark Mirror',
        'filename': 'Syphon Filter - Dark Mirror (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Syphon Filter - Dark Mirror (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Syphon Filter - Dark Mirror (USA).iso',
        'size': 1206910976,
    },
    {
        'title': 'Tactics Ogre: Let Us Cling Together',
        'filename': 'Tactics Ogre - Let Us Cling Together (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Tactics Ogre - Let Us Cling Together (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Tactics Ogre - Let Us Cling Together (USA).iso',
        'size': 1614610432,
    },
    {
        'title': 'TMNT',
        'filename': 'TMNT (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/TMNT (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/TMNT (USA).iso',
        'size': 953221120,
    },
    {
        'title': "Tony Hawk's Project 8",
        'filename': "Tony Hawk's Project 8 (USA) (v2.03).iso",
        'source_relative': "Handhelds/Sony PSP [2004]/Tony Hawk's Project 8 (USA) (v2.03).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Tony Hawk's Project 8 (USA) (v2.03).iso",
        'size': 1494056960,
    },
    {
        'title': "Tony Hawk's Underground 2 Remix",
        'filename': "Tony Hawk's Underground 2 Remix (USA).iso",
        'source_relative': "Handhelds/Sony PSP [2004]/Tony Hawk's Underground 2 Remix (USA).iso",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Tony Hawk's Underground 2 Remix (USA).iso",
        'size': 1216184320,
    },
    {
        'title': 'Twisted Metal: Head-On',
        'filename': 'Twisted Metal - Head-On (USA).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/Twisted Metal - Head-On (USA).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/Twisted Metal - Head-On (USA).iso',
        'size': 838664192,
    },
    {
        'title': 'WipEout Pulse',
        'filename': 'WipEout Pulse (USA) (En,Fr,De,Es,It).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/WipEout Pulse (USA) (En,Fr,De,Es,It).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/WipEout Pulse (USA) (En,Fr,De,Es,It).iso',
        'size': 456949760,
    },
    {
        'title': 'WipEout Pure',
        'filename': 'WipEout Pure (USA) (En,Fr,Es) (v2.00).iso',
        'source_relative': 'Handhelds/Sony PSP [2004]/WipEout Pure (USA) (En,Fr,Es) (v2.00).iso',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/psp/WipEout Pure (USA) (En,Fr,Es) (v2.00).iso',
        'size': 252968960,
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