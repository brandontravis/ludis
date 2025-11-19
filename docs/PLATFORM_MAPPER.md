# Platform Mapper

## Overview

The Platform Mapper module (`scripts/platform_mapper.py`) handles the mapping between LaunchBox platform names and ES-DE (EmulationStation Desktop Edition) platform folder names.

## Purpose

LaunchBox and ES-DE use different naming conventions for platforms. For example:
- **LaunchBox**: "Nintendo Wii U"
- **ES-DE**: "wiiu" (folder name)

The mapper provides bidirectional translation between these naming schemes.

## Features

### Bidirectional Mapping
- **LaunchBox → ES-DE**: Convert LB platform names to ES-DE folder names
- **ES-DE → LaunchBox**: Convert ES-DE folder names back to LB names

### Comprehensive Coverage
- **168 ES-DE platforms** loaded from `platforms-esde.json`
- **54 manual mappings** for common platforms
- **98.1% coverage** of your library (53/54 platforms)

### Validation
- Check if a platform is supported
- Get list of supported platforms
- Identify unsupported platforms in your library

## Usage

### Basic Usage

```python
from scripts.platform_mapper import PlatformMapper

# Initialize mapper
mapper = PlatformMapper()

# Convert LaunchBox → ES-DE
esde_folder = mapper.lb_to_esde("Nintendo Wii U")
print(esde_folder)  # Output: "wiiu"

# Convert ES-DE → LaunchBox
lb_name = mapper.esde_to_lb("wiiu")
print(lb_name)  # Output: "Nintendo Wii U"

# Check if platform is supported
if mapper.is_platform_supported("Nintendo Wii U"):
    print("Platform is supported!")

# Get full ES-DE info
info = mapper.get_esde_info("Wii U")
print(info["description"])  # Output: "A home video game console developed by Nintendo."
```

### Working with Your Library

```python
# Get all supported LaunchBox platforms
supported = mapper.get_supported_platforms()
print(f"Total supported: {len(supported)}")

# Check which platforms in your library are unsupported
your_platforms = ["Nintendo Wii U", "Sony Playstation 3", "Microsoft Xbox 360"]
unsupported = mapper.get_unsupported_platforms(your_platforms)
print(f"Unsupported: {unsupported}")  # Output: ['Microsoft Xbox 360']

# Get mapping statistics
stats = mapper.get_mapping_summary()
print(stats)
# Output: {
#   'total_esde_platforms': 168,
#   'total_mapped_platforms': 54,
#   'total_esde_folders': 54
# }
```

## Supported Platforms

Currently supports **54 platforms** including:

### Nintendo
- NES, SNES, N64, GameCube, Wii, Wii U, Switch
- Game Boy, Game Boy Color, Game Boy Advance
- DS, 3DS, Virtual Boy, Pokémon Mini
- Famicom Disk System, Satellaview

### Sega
- Genesis, Master System, Sega CD, 32X
- Saturn, Dreamcast, Game Gear, SG-1000

### Sony
- PlayStation (1, 2, 3), PSP, PS Vita

### Microsoft
- Xbox (original)
- *Note: Xbox 360 not yet supported by ES-DE*

### NEC
- TurboGrafx-16, TurboGrafx-CD, SuperGrafx

### SNK
- Neo Geo, Neo Geo CD, Neo Geo Pocket Color

### Atari
- 2600, 5200, 7800, Jaguar, Lynx, ST

### Other Consoles
- 3DO, ColecoVision, Intellivision, Odyssey 2
- Channel F, Vectrex, Supervision, GX4000

### Computers
- Amiga CD32, MS-DOS, Windows

### Arcade
- MAME/Arcade

## Unsupported Platforms

### Microsoft Xbox 360
**Status**: Not in ES-DE platform definitions

**Reason**: Xbox 360 emulation is still experimental. The Xenia emulator exists but is not yet integrated into ES-DE's official platform definitions.

**Workaround**: When building migrations, Xbox 360 titles will be flagged and can be handled separately or skipped.

## Adding New Mappings

If you need to add a new platform mapping:

1. **Check if ES-DE supports it**: Look in `scripts/platforms-esde.json`
2. **Add to manual mappings**: Edit `scripts/platform_mapper.py`
3. **Add entry in `manual_mappings` dict**:
   ```python
   "LaunchBox Name": "ES-DE Name (from JSON key)",
   ```

Example:
```python
manual_mappings = {
    # ... existing mappings ...
    "New Platform Name": "ES-DE Platform Name",
}
```

## Testing

Run the test suite:
```bash
python3 scripts/platform_mapper.py
```

This will:
- Load ES-DE platform definitions
- Build all mappings
- Test sample platforms
- Show mapping summary
- Display supported platforms list

## ES-DE Platform Reference

The complete ES-DE platform list is in `scripts/platforms-esde.json`. Each entry contains:
- **Platform name** (key)
- **folder**: ES-DE folder name
- **description**: Platform description

Example:
```json
{
  "Wii U": {
    "folder": "wiiu",
    "description": "A home video game console developed by Nintendo."
  }
}
```

## Integration

The Platform Mapper integrates with:
- **Migration Builder**: Maps platforms when generating migration scripts
- **Inventory Scanner**: Validates platforms during inventory scan
- **Export Targets**: Ensures export destinations use correct folder names

## Performance

- **Load time**: ~10ms (loads 168 platform definitions)
- **Lookup time**: O(1) (hash table lookup)
- **Memory usage**: ~50KB (platform definitions + mappings)

## Future Enhancements

Potential improvements:
- **Fuzzy matching**: Auto-suggest mappings for unknown platforms
- **User-defined mappings**: Store custom mappings in config.yaml
- **Multi-format support**: Support other frontend formats (RetroArch playlists, etc.)
- **Platform detection**: Auto-detect platform from ROM file structure

