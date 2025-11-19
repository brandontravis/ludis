#!/usr/bin/env python3
# Auto-generated migration script for Nintendo Wii U
# 73 games, 458.90 GB
# Operation: copy

import os
import shutil
from pathlib import Path

PLATFORM_NAME = 'Nintendo Wii U'
ESDE_FOLDER = 'wiiu'
OPERATION = 'copy'

GAMES = [
    {
        'title': "Assassin's Creed III",
        'filename': "Assassin's Creed III (USA) (DLC) (v80).wua",
        'source_relative': "Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Assassin's Creed III (USA) (DLC) (v80).wua",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Assassin's Creed III (USA) (DLC) (v80).wua",
        'size': 20942752467,
    },
    {
        'title': "Assassin's Creed IV: Black Flag",
        'filename': "Assassin's Creed IV Black Flag (USA) (v32).wua",
        'source_relative': "Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Assassin's Creed IV Black Flag (USA) (v32).wua",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Assassin's Creed IV Black Flag (USA) (v32).wua",
        'size': 13215349847,
    },
    {
        'title': 'Batman: Arkham Origins',
        'filename': 'Batman - Arkham Origins (USA) (DLC) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Batman - Arkham Origins (USA) (DLC) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Batman - Arkham Origins (USA) (DLC) (v16).wua',
        'size': 13240856096,
    },
    {
        'title': 'Batman: Arkham City: Armored Edition',
        'filename': 'Batman Arkham City - Armored Edition (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Batman Arkham City - Armored Edition (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Batman Arkham City - Armored Edition (USA).wua',
        'size': 17001774619,
    },
    {
        'title': 'Bayonetta',
        'filename': 'BAYONETTA (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/BAYONETTA (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/BAYONETTA (USA).wua',
        'size': 11168369027,
    },
    {
        'title': 'Bayonetta 2',
        'filename': 'BAYONETTA 2 (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/BAYONETTA 2 (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/BAYONETTA 2 (USA).wua',
        'size': 13813438114,
    },
    {
        'title': 'Call of Duty: Black Ops II',
        'filename': 'Call of Duty - Black Ops II (USA) (v128).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Call of Duty - Black Ops II (USA) (v128).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Call of Duty - Black Ops II (USA) (v128).wua',
        'size': 17730211706,
    },
    {
        'title': 'Call of Duty: Ghosts',
        'filename': 'Call of Duty - Ghosts (USA) (DLC) (v112).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Call of Duty - Ghosts (USA) (DLC) (v112).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Call of Duty - Ghosts (USA) (DLC) (v112).wua',
        'size': 13708922137,
    },
    {
        'title': 'Captain Toad: Treasure Tracker',
        'filename': 'Captain Toad Treasure Tracker (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Captain Toad Treasure Tracker (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Captain Toad Treasure Tracker (USA) (v16).wua',
        'size': 1151238231,
    },
    {
        'title': 'Donkey Kong Country: Tropical Freeze',
        'filename': 'Donkey Kong Country - Tropical Freeze (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Donkey Kong Country - Tropical Freeze (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Donkey Kong Country - Tropical Freeze (USA) (v16).wua',
        'size': 9929835673,
    },
    {
        'title': 'DuckTales: Remastered',
        'filename': 'DuckTales Remastered (USA) (v32).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/DuckTales Remastered (USA) (v32).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/DuckTales Remastered (USA) (v32).wua',
        'size': 863103522,
    },
    {
        'title': 'Hyrule Warriors',
        'filename': 'Hyrule Warriors (USA) (DLC) (v208).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Hyrule Warriors (USA) (DLC) (v208).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Hyrule Warriors (USA) (DLC) (v208).wua',
        'size': 7638962974,
    },
    {
        'title': 'Injustice: Gods Among Us',
        'filename': 'Injustice Gods Among Us (USA) (DLC) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Injustice Gods Among Us (USA) (DLC) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Injustice Gods Among Us (USA) (DLC) (v16).wua',
        'size': 8221238985,
    },
    {
        'title': 'Kirby and the Rainbow Curse',
        'filename': 'Kirby and the Rainbow Curse (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Kirby and the Rainbow Curse (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Kirby and the Rainbow Curse (USA) (v16).wua',
        'size': 2906784642,
    },
    {
        'title': 'LEGO Batman 2: DC Super Heroes',
        'filename': 'LEGO Batman 2 - DC Super Heroes (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO Batman 2 - DC Super Heroes (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO Batman 2 - DC Super Heroes (USA).wua',
        'size': 4117873379,
    },
    {
        'title': 'LEGO Batman 3: Beyond Gotham',
        'filename': 'LEGO Batman 3 - Beyond Gotham (USA) (v48).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO Batman 3 - Beyond Gotham (USA) (v48).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO Batman 3 - Beyond Gotham (USA) (v48).wua',
        'size': 5744686456,
    },
    {
        'title': 'LEGO City: Undercover',
        'filename': 'LEGO CITY UNDERCOVER (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO CITY UNDERCOVER (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO CITY UNDERCOVER (USA).wua',
        'size': 18379415514,
    },
    {
        'title': 'LEGO Dimensions',
        'filename': 'LEGO DIMENSIONS (USA) (DLC) (v320).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO DIMENSIONS (USA) (DLC) (v320).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO DIMENSIONS (USA) (DLC) (v320).wua',
        'size': 19791902305,
    },
    {
        'title': 'LEGO Jurassic World',
        'filename': 'LEGO Jurassic World (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO Jurassic World (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO Jurassic World (USA) (v16).wua',
        'size': 5949601129,
    },
    {
        'title': 'LEGO Marvel Super Heroes',
        'filename': 'LEGO Marvel Super Heroes (USA) (v32).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO Marvel Super Heroes (USA) (v32).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO Marvel Super Heroes (USA) (v32).wua',
        'size': 5368257694,
    },
    {
        'title': "LEGO Marvel's Avengers",
        'filename': "LEGO MARVEL's Avengers (USA) (DLC) (v64).wua",
        'source_relative': "Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO MARVEL's Avengers (USA) (DLC) (v64).wua",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO MARVEL's Avengers (USA) (DLC) (v64).wua",
        'size': 8115097309,
    },
    {
        'title': 'LEGO Star Wars: The Force Awakens',
        'filename': 'LEGO STAR WARS - The Force Awakens (USA) (v32).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO STAR WARS - The Force Awakens (USA) (v32).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO STAR WARS - The Force Awakens (USA) (v32).wua',
        'size': 6270045707,
    },
    {
        'title': 'LEGO The Hobbit',
        'filename': 'LEGO The Hobbit (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/LEGO The Hobbit (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/LEGO The Hobbit (USA).wua',
        'size': 5883447691,
    },
    {
        'title': 'Mario Kart 8',
        'filename': 'MARIO KART 8 (USA) (DLC) (v81).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/MARIO KART 8 (USA) (DLC) (v81).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/MARIO KART 8 (USA) (DLC) (v81).wua',
        'size': 4648084082,
    },
    {
        'title': 'Mario vs. Donkey Kong: Tipping Stars',
        'filename': 'Mario vs. Donkey Kong - Tipping Stars (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Mario vs. Donkey Kong - Tipping Stars (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Mario vs. Donkey Kong - Tipping Stars (USA).wua',
        'size': 386621047,
    },
    {
        'title': 'Monster Hunter 3 Ultimate',
        'filename': 'MONSTER HUNTER 3 ULTIMATE (USA) (v32).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/MONSTER HUNTER 3 ULTIMATE (USA) (v32).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/MONSTER HUNTER 3 ULTIMATE (USA) (v32).wua',
        'size': 5836353199,
    },
    {
        'title': 'NES Remix Pack',
        'filename': 'NES REMIX PACK (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/NES REMIX PACK (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/NES REMIX PACK (USA).wua',
        'size': 133415254,
    },
    {
        'title': 'New Super Luigi U',
        'filename': 'New SUPER LUIGI U (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/New SUPER LUIGI U (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/New SUPER LUIGI U (USA).wua',
        'size': 1202713826,
    },
    {
        'title': 'New Super Mario Bros. U',
        'filename': 'New SUPER MARIO BROS. U (USA) (DLC) (v64).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/New SUPER MARIO BROS. U (USA) (DLC) (v64).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/New SUPER MARIO BROS. U (USA) (DLC) (v64).wua',
        'size': 2060117679,
    },
    {
        'title': 'New Super Mario Bros. U + New Super Luigi U',
        'filename': 'New SUPER MARIO BROS. U + New SUPER LUIGI U (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/New SUPER MARIO BROS. U + New SUPER LUIGI U (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/New SUPER MARIO BROS. U + New SUPER LUIGI U (USA).wua',
        'size': 13820260960,
    },
    {
        'title': "Ninja Gaiden 3: Razor's Edge",
        'filename': "NINJA GAIDEN 3 Razor's Edge (USA) (v80).wua",
        'source_relative': "Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/NINJA GAIDEN 3 Razor's Edge (USA) (v80).wua",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/NINJA GAIDEN 3 Razor's Edge (USA) (v80).wua",
        'size': 5561243824,
    },
    {
        'title': 'Nintendo Land',
        'filename': 'Nintendo Land (USA) (v32).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Nintendo Land (USA) (v32).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Nintendo Land (USA) (v32).wua',
        'size': 2818845862,
    },
    {
        'title': 'Pac-Man and the Ghostly Adventures',
        'filename': 'PAC-MAN and the Ghostly Adventures (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/PAC-MAN and the Ghostly Adventures (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/PAC-MAN and the Ghostly Adventures (USA).wua',
        'size': 3085680737,
    },
    {
        'title': 'PAC-MAN and the Ghostly Adventures 2',
        'filename': 'PAC-MAN and the Ghostly Adventures 2 (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/PAC-MAN and the Ghostly Adventures 2 (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/PAC-MAN and the Ghostly Adventures 2 (USA).wua',
        'size': 3449857461,
    },
    {
        'title': 'Paper Mario: Color Splash',
        'filename': 'PAPER MARIO Color Splash (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/PAPER MARIO Color Splash (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/PAPER MARIO Color Splash (USA).wua',
        'size': 7160365414,
    },
    {
        'title': 'Pikmin 3',
        'filename': 'PIKMIN 3 (USA) (DLC) (v96).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/PIKMIN 3 (USA) (DLC) (v96).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/PIKMIN 3 (USA) (DLC) (v96).wua',
        'size': 4480008879,
    },
    {
        'title': 'Rabbids Land',
        'filename': 'Rabbids Land (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Rabbids Land (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Rabbids Land (USA) (v16).wua',
        'size': 6687585881,
    },
    {
        'title': 'Rayman Legends',
        'filename': 'Rayman Legends (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Rayman Legends (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Rayman Legends (USA).wua',
        'size': 6697315343,
    },
    {
        'title': 'Resident Evil: Revelations',
        'filename': 'RESIDENT EVIL REVELATIONS (USA) (DLC) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/RESIDENT EVIL REVELATIONS (USA) (DLC) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/RESIDENT EVIL REVELATIONS (USA) (DLC) (v16).wua',
        'size': 12687704291,
    },
    {
        'title': 'Shovel Knight',
        'filename': 'Shovel Knight (USA) (v96).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Shovel Knight (USA) (v96).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Shovel Knight (USA) (v96).wua',
        'size': 249991900,
    },
    {
        'title': 'Skylanders Giants',
        'filename': 'Skylanders Giants (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Skylanders Giants (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Skylanders Giants (USA).wua',
        'size': 10395951109,
    },
    {
        'title': 'Skylanders: Imaginators',
        'filename': 'Skylanders Imaginators (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Skylanders Imaginators (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Skylanders Imaginators (USA) (v16).wua',
        'size': 18997313526,
    },
    {
        'title': 'Skylanders: SuperChargers',
        'filename': 'Skylanders SuperChargers (USA) (v96).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Skylanders SuperChargers (USA) (v96).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Skylanders SuperChargers (USA) (v96).wua',
        'size': 14554458970,
    },
    {
        'title': 'Skylanders: SWAP Force',
        'filename': 'Skylanders SWAP Force (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Skylanders SWAP Force (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Skylanders SWAP Force (USA) (v16).wua',
        'size': 13550136018,
    },
    {
        'title': 'Skylanders: Trap Team',
        'filename': 'Skylanders Trap Team (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Skylanders Trap Team (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Skylanders Trap Team (USA) (v16).wua',
        'size': 10282751432,
    },
    {
        'title': 'Sonic & All-Stars Racing Transformed',
        'filename': 'Sonic & All-Stars Racing Transformed (USA) (v48).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Sonic & All-Stars Racing Transformed (USA) (v48).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Sonic & All-Stars Racing Transformed (USA) (v48).wua',
        'size': 3572304399,
    },
    {
        'title': 'Splatoon',
        'filename': 'Splatoon (USA) (v288).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Splatoon (USA) (v288).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Splatoon (USA) (v288).wua',
        'size': 2150189121,
    },
    {
        'title': "Tom Clancy's Splinter Cell: Blacklist",
        'filename': 'Splinter Cell Blacklist (USA) (DLC) (v48).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Splinter Cell Blacklist (USA) (DLC) (v48).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Splinter Cell Blacklist (USA) (DLC) (v48).wua',
        'size': 14210580592,
    },
    {
        'title': 'Star Fox Guard',
        'filename': 'Star Fox Guard (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Star Fox Guard (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Star Fox Guard (USA) (v16).wua',
        'size': 1375424843,
    },
    {
        'title': 'Star Fox Zero',
        'filename': 'Star Fox Zero (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Star Fox Zero (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Star Fox Zero (USA) (v16).wua',
        'size': 4840913296,
    },
    {
        'title': 'SteamWorld Collection',
        'filename': 'SteamWorld Collection (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/SteamWorld Collection (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/SteamWorld Collection (USA).wua',
        'size': 308208634,
    },
    {
        'title': 'Super Mario 3D World',
        'filename': 'SUPER MARIO 3D WORLD (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/SUPER MARIO 3D WORLD (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/SUPER MARIO 3D WORLD (USA).wua',
        'size': 1484470607,
    },
    {
        'title': 'Super Mario Maker',
        'filename': 'Super Mario Maker (USA) (v272).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Super Mario Maker (USA) (v272).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Super Mario Maker (USA) (v272).wua',
        'size': 932309427,
    },
    {
        'title': 'Super Smash Bros. for Wii U',
        'filename': 'Super Smash Bros. for Wii U (USA) (DLC) (v304).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Super Smash Bros. for Wii U (USA) (DLC) (v304).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Super Smash Bros. for Wii U (USA) (DLC) (v304).wua',
        'size': 14363867696,
    },
    {
        'title': 'The Legend of Zelda: Breath of the Wild',
        'filename': 'The Legend of Zelda - Breath of the Wild (USA) (DLC) (v208).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/The Legend of Zelda - Breath of the Wild (USA) (DLC) (v208).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/The Legend of Zelda - Breath of the Wild (USA) (DLC) (v208).wua',
        'size': 13660330872,
    },
    {
        'title': 'The Legend of Zelda: Hyrule Historia',
        'filename': 'The Legend of Zelda - Hyrule Historia (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/The Legend of Zelda - Hyrule Historia (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/The Legend of Zelda - Hyrule Historia (USA).wua',
        'size': 317801052,
    },
    {
        'title': 'The Legend of Zelda: The Wind Waker HD',
        'filename': 'The Legend of Zelda - The Wind Waker HD (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/The Legend of Zelda - The Wind Waker HD (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/The Legend of Zelda - The Wind Waker HD (USA).wua',
        'size': 1489764491,
    },
    {
        'title': 'The Legend of Zelda: Twilight Princess HD',
        'filename': 'The Legend of Zelda - Twilight Princess HD (USA) (v81).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/The Legend of Zelda - Twilight Princess HD (USA) (v81).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/The Legend of Zelda - Twilight Princess HD (USA) (v81).wua',
        'size': 4559783561,
    },
    {
        'title': 'The LEGO Movie Videogame',
        'filename': 'The LEGO Movie - Videogame (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/The LEGO Movie - Videogame (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/The LEGO Movie - Videogame (USA) (v16).wua',
        'size': 5297173695,
    },
    {
        'title': 'Watch Dogs',
        'filename': 'WATCH_DOGS (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/WATCH_DOGS (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/WATCH_DOGS (USA).wua',
        'size': 13102489051,
    },
    {
        'title': 'Xenoblade Chronicles X',
        'filename': 'Xenoblade Chronicles X (USA) (DLC) (v48).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Xenoblade Chronicles X (USA) (DLC) (v48).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Xenoblade Chronicles X (USA) (DLC) (v48).wua',
        'size': 18643801178,
    },
    {
        'title': "Yoshi's Woolly World",
        'filename': "Yoshi's Woolly World (USA) (v32).wua",
        'source_relative': "Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Yoshi's Woolly World (USA) (v32).wua",
        'dest': "/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Yoshi's Woolly World (USA) (v32).wua",
        'size': 6414970497,
    },
    {
        'title': 'Batman: Arkham Origins Blackgate: Deluxe Edition',
        'filename': 'Batman Arkham Origins Blackgate - Deluxe Edition (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/Batman Arkham Origins Blackgate - Deluxe Edition (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Batman Arkham Origins Blackgate - Deluxe Edition (USA).wua',
        'size': 2076545856,
    },
    {
        'title': 'Child of Light',
        'filename': 'CHILD of LIGHT (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/CHILD of LIGHT (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/CHILD of LIGHT (USA) (v16).wua',
        'size': 2360913230,
    },
    {
        'title': 'Dr. Luigi',
        'filename': 'Dr. Luigi (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/Dr. Luigi (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Dr. Luigi (USA).wua',
        'size': 96441828,
    },
    {
        'title': 'Island Flight Simulator',
        'filename': 'Island Flight Simulator (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/Island Flight Simulator (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Island Flight Simulator (USA).wua',
        'size': 316994427,
    },
    {
        'title': 'Mario vs. Donkey Kong: Tipping Stars',
        'filename': 'Mario vs. Donkey Kong - Tipping Stars (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/Mario vs. Donkey Kong - Tipping Stars (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/Mario vs. Donkey Kong - Tipping Stars (USA).wua',
        'size': 386621047,
    },
    {
        'title': 'NES Remix',
        'filename': 'NES REMIX (USA) (v16).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/NES REMIX (USA) (v16).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/NES REMIX (USA) (v16).wua',
        'size': 79191938,
    },
    {
        'title': 'NES Remix 2',
        'filename': 'NES REMIX 2 (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/NES REMIX 2 (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/NES REMIX 2 (USA).wua',
        'size': 86241643,
    },
    {
        'title': 'OlliOlli',
        'filename': 'OlliOlli (USA) (v17).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/OlliOlli (USA) (v17).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/OlliOlli (USA) (v17).wua',
        'size': 110617711,
    },
    {
        'title': 'SteamWorld Dig',
        'filename': 'SteamWorld Dig (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/SteamWorld Dig (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/SteamWorld Dig (USA).wua',
        'size': 72803423,
    },
    {
        'title': 'SteamWorld Heist',
        'filename': 'SteamWorld Heist (USA) (DLC).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/eShop + Updates + DLC Merged (Decrypted ... use these!)/SteamWorld Heist (USA) (DLC).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/SteamWorld Heist (USA) (DLC).wua',
        'size': 213504968,
    },
    {
        'title': 'The Legend of Zelda: Hyrule Historia',
        'filename': 'The Legend of Zelda - Hyrule Historia (USA).wua',
        'source_relative': 'Consoles/Nintendo Wii U [2012]/Base Games + Updates + DLC Merged (Decrypted ... use these!)/The Legend of Zelda - Hyrule Historia (USA).wua',
        'dest': '/run/media/idealbrandon/Bazzite-SD/Emulation/roms/wiiu/The Legend of Zelda - Hyrule Historia (USA).wua',
        'size': 317801052,
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