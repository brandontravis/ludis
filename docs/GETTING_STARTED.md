# Getting Started with Ludis

Welcome to Ludis! This guide will walk you through installing and setting up Ludis for the first time.

## What is Ludis?

Ludis (LaunchBox Universal Data Integration System) is a **platform-agnostic** ROM library migration tool. It helps you:

- **Analyze** your massive LaunchBox collection
- **Filter** games by playlists, favorites, and custom criteria
- **Export** curated libraries to devices like Steam Deck, Retro handhelds, etc.
- **Generate** migration scripts that handle the actual file copying

### Key Philosophy

Ludis is designed to run **anywhere** with access to your LaunchBox data:
- On Windows where LaunchBox is installed
- On macOS/Linux where your NAS is mounted
- On a remote server with network access to your files
- Anywhere with Python 3.9+

## Prerequisites

### Required
- Python 3.9 or higher
- LaunchBox with XML data exported
- Access to your game library files (local or network)

### Recommended
- 500MB free disk space for exports
- Understanding of your file structure

## Installation

### 1. Clone or Download Ludis

```bash
git clone https://github.com/brandontravis/ludis.git
cd ludis
```

### 2. Install Python Dependencies

```bash
pip3 install pyyaml inquirer
```

### 3. Curate Your Data Folder

**⚠ IMPORTANT:** We strongly recommend creating a **curated copy** of your LaunchBox data rather than pointing Ludis directly at your live LaunchBox installation.

#### Why?

- You have full control over what platforms/playlists are scanned
- No need to deselect from 1000+ playlists in Ludis menus
- Keeps your LaunchBox installation pristine
- Allows multiple Ludis configurations for different targets

#### How to Curate

```bash
# From your LaunchBox installation
cp -r "C:/LaunchBox/Data/Platforms" ./ludis/Data/Platforms/
cp -r "C:/LaunchBox/Data/Playlists" ./ludis/Data/Playlists/

# Remove unwanted platforms
rm "./ludis/Data/Platforms/DOS.xml"

# Remove unwanted playlists
rm "./ludis/Data/Playlists/Franchise - Mario.xml"
```

**Keep only what you want to export.**

## First Run

### Run the Setup Wizard

```bash
python3 ludis.py
```

Ludis will detect that `config.yaml` doesn't exist and launch the interactive setup wizard.

### Setup Questions

#### 1. LaunchBox XML Data

**Where is your LaunchBox Data directory?**

This is where your curated Platforms/ and Playlists/ XML files live.

Examples:
- `Data/` (if you curated inside ludis/)
- `/path/to/LaunchBox/Data/` (if pointing to live installation)

#### 2. LaunchBox Installation Context

**What path does LaunchBox use in its XML files?**

LaunchBox stores file paths as they were on the Windows machine where it was installed. This might be different from where the files actually are now.

Example:
- `Z:\media\games\library` (Windows mapped drive)
- `C:\LaunchBox\Games` (Windows local install)

#### 3. Game Library Location

**What is the base path for your games library?**

This is where Ludis will look for the physical files.

Examples:
- `/Volumes/NAS/media/games/library` (macOS with NAS)
- `/mnt/nas/games/library` (Linux with NAS)
- `C:\LaunchBox\Games` (Windows local)

**Structure Discovery:**

After entering your base path, Ludis will ask if your folder structure is:

1. **Direct** - Platform folders directly in base path:
   ```
   library/
     ├── Nintendo 64/
     ├── Sega Genesis/
     └── Sony Playstation/
   ```

2. **Nested** - Organized with categories:
   ```
   library/
     ├── Consoles/
     │   ├── Nintendo 64/
     │   └── Sega Genesis/
     └── Handhelds/
         └── Game Boy/
   ```

If you choose **Nested**, Ludis will scan for category folders and present a checkbox UI to select which ones to include (e.g., "Consoles", "Handhelds"). All folders are pre-selected - just uncheck any you don't want.

#### 4. Filesystem Scanning

**Enable filesystem scanning?**

- **Yes:** Ludis scans your library paths to match files with LaunchBox entries and calculate sizes
- **No:** Metadata-only mode (faster, but no file validation)

Recommended: **Yes** for first run

## Verify Configuration

After setup, Ludis will create `config.yaml` with your settings. Review it:

```bash
cat config.yaml
```

## Next Steps

You're ready to start using Ludis! See [CONFIGURATION.md](CONFIGURATION.md) for advanced settings.

### Quick Start Workflow

1. **Run initial scan:**
   ```bash
   python3 ludis.py
   ```
   Select: "Re-run filesystem scan"

2. **Build inventory:**
   Select: "Re-build master inventory"

3. **Create your first export target:**
   Select: "Create Migration Script"
   - First time: You'll be prompted to create an export target
   - Name it (e.g., `steam_deck`, `retroid_pocket`)
   - Confirm ES-DE format

4. **Configure storage defaults:**
   Select: "Configure Platform Storage Defaults"
   - Define internal SSD and SD card paths
   - Assign platforms to storage locations

5. **Create migration script:**
   Select: "Create Migration Script" again
   - Select filters
   - Choose platforms
   - Review and generate

6. **Copy the generated `dist_XXX/` folder to your target device and run:**
   ```bash
   python3 ludis-migrate.py
   ```

## Troubleshooting

### "ERROR: Platforms dir not found"

Make sure your `launchbox_data` path in `config.yaml` points to a folder containing `Platforms/` and `Playlists/` subdirectories.

### "WARNING: Directory not found" for library paths

If you're running on a machine that doesn't have access to your game files, you can still generate metadata. Disable filesystem scanning or fix the paths.

### Permissions errors

Make sure you have read access to LaunchBox data and write access to the `LB_Exports/` folder.

## Getting Help

- Check [CONFIGURATION.md](CONFIGURATION.md) for config options
- See [MIGRATION.md](MIGRATION.md) for migration workflow details
- Review [VALIDATION.md](VALIDATION.md) for handling detected issues

---

**Ready to start?** Run `python3 ludis.py` and follow the wizard!

