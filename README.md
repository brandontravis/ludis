# LaunchBox Game Exporter (Ludis)

A unified pipeline for exporting and enriching LaunchBox game library data.

## Quick Start

```bash
# Install dependencies
pip3 install pyyaml inquirer tqdm

# Run Ludis
python3 ludis.py
```

On first run, Ludis will guide you through configuration setup.

## Project Structure

```
lb-game-exporter/
├── ludis.py                 # Main entry point - run this!
├── config.yaml              # Your configuration (auto-generated)
├── config.yaml.sample       # Configuration template
│
├── scripts/                 # Pipeline modules
│   ├── audit_library.py            # Filesystem scanning
│   ├── export_all_platforms.py     # Platform data export
│   ├── export_all_playlists.py     # Playlist data export
│   ├── build_master_inventory.py   # Inventory reconciliation
│   └── enrich_with_playlists.py    # Playlist enrichment
│
├── docs/                    # Documentation
│   ├── LUDIS_README.md             # Full documentation
│   ├── LUDIS_PROJECT_PLAN.md       # Project planning
│   └── CHANGELOG.md                # Version history
│
├── archive/                 # Old/unused code (preserved for reference)
│
├── Data/                    # LaunchBox XML files (your data)
│   ├── Platforms/
│   └── Playlists/
│
└── LB_Exports/              # Generated CSV outputs
    ├── all_platforms.csv
    ├── all_playlists.csv
    ├── master_inventory.csv        # Main output!
    ├── platforms/
    ├── playlists/
    └── audits/
```

## What It Does

Ludis exports your LaunchBox library to CSV format with:
- ✅ All game metadata (titles, developers, ratings, etc.)
- ✅ Custom fields (The Best, GOTY, Backlog, etc.)
- ✅ Filesystem matching (which games are on disk)
- ✅ Playlist membership (franchise, curated collections, etc.)
- ✅ Filtered playlists (excludes auto-generated genre lists)

## Documentation

See [`docs/LUDIS_README.md`](docs/LUDIS_README.md) for complete documentation.

## Output

The main output is `LB_Exports/master_inventory.csv` which contains:
- All your games from all platforms
- Matched to actual files on disk
- Enriched with playlist membership data
- Ready for further processing (ES-DE exports, Steam Deck, etc.)

## Version

1.0.0

