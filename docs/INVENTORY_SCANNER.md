# Inventory Scanner

## Overview

The Inventory Scanner module (`scripts/inventory_scanner.py`) analyzes the master inventory to provide platform statistics for migration planning, including game counts and total file sizes.

## Purpose

When building a migration script, users need to see:
- Which platforms have games in their library
- How many games per platform
- Total file size per platform (for storage planning)
- Filtered views based on custom criteria

## Features

### Platform Summary
- **Game counts** per platform
- **Total file sizes** with human-readable formatting (B, KB, MB, GB, TB)
- **Sorted alphabetically** for easy browsing
- **Filter support** for all config.yaml filter options

### File Size Formatting
Automatically formats sizes to appropriate units:
- `74.9 MB` (Nintendo Entertainment System, 867 games)
- `1.15 TB` (Nintendo Wii U, 766 games)
- `73.3 GB` (Arcade, 14,647 games)

### Filter Integration
Full integration with all filter options from `config.yaml`:
- Platform Best, All-Time Favorites, Favorites
- Backlog, GOTY Winners/Nominees, On Deck
- Retro Collection, Classic Titles, Franchises
- Manual Include/Exclude (forced)
- Custom fields

## Usage

### Basic Usage

```python
from scripts.inventory_scanner import InventoryScanner

# Initialize scanner
scanner = InventoryScanner()

# Get all platforms (no filters)
platforms = scanner.get_platform_summary()

for platform in platforms:
    print(f"{platform['name']}, {platform['game_count']} Games, {platform['size_formatted']}")

# Output:
# Nintendo Entertainment System, 867 Games, 74.9 MB
# Nintendo Wii U, 766 Games, 1.15 TB
# Sony Playstation 3, 331 Games, 0 B
```

### With Filters

```python
# Apply filters (same structure as config.yaml)
filters = {
    'force_manual_include': True,
    'force_manual_exclude': True,
    'include_favorites': True,
    'include_goty_winner': True,
}

platforms = scanner.get_platform_summary(filters)

# Only shows platforms with favorite or GOTY games
# (excluding ManualExclude=true games)
```

### Total Statistics

```python
# Get totals across all platforms
totals = scanner.get_total_statistics()

print(f"Platforms: {totals['total_platforms']}")
print(f"Games: {totals['total_games']:,}")
print(f"Total Size: {totals['size_formatted']}")

# Output:
# Platforms: 54
# Games: 34,517
# Total Size: 11.5 TB
```

### Specific Platform

```python
# Get details for one platform
details = scanner.get_platform_details("Nintendo Wii U")

print(f"Platform: {details['name']}")
print(f"Games: {details['game_count']}")
print(f"Size: {details['size_formatted']}")

# Access individual games
for game in details['games'][:5]:
    print(f"  - {game['title']}")
```

## Data Structure

### Platform Summary

Each platform in the summary contains:

```python
{
    'name': 'Nintendo Wii U',
    'game_count': 766,
    'total_size_bytes': 1267650116608,  # 1.15 TB in bytes
    'size_formatted': '1.15 TB',
    'games': [
        {
            'lbid': 'game-id-123',
            'title': 'The Legend of Zelda: Breath of the Wild',
            'file_size': 13631488000  # bytes
        },
        # ... more games
    ]
}
```

### Total Statistics

```python
{
    'total_platforms': 54,
    'total_games': 34517,
    'total_size_bytes': 12621557248000,  # 11.5 TB
    'size_formatted': '11.5 TB'
}
```

## Filter Logic

Filters follow the same logic as defined in the migration schema:

1. **Force Exclude**: `ManualExclude=true` games are removed first (if enabled)
2. **Force Include**: `ManualInclude=true` games are included regardless (if enabled)
3. **OR Logic**: Any other filter match includes the game
4. **No Filters**: If all filters are false, all games are included

### Example Filter Scenarios

**Scenario 1: Only Favorites**
```python
filters = {'include_favorites': True}
# Result: Only games with Favorite=true
```

**Scenario 2: GOTY or Platform Best**
```python
filters = {
    'include_goty_winner': True,
    'include_platform_best': True
}
# Result: Games that are GOTY winners OR platform best (OR both)
```

**Scenario 3: Manual Control Only**
```python
filters = {
    'force_manual_include': True,
    'force_manual_exclude': True
}
# Result: Only manually included games (excluding manually excluded)
```

## Performance

**Your Library Statistics:**
- **54 platforms**
- **34,517 total games**
- **11.5 TB total size**
- **Scan time**: ~200ms for full inventory

**With Filters (favorites only):**
- **25 platforms**
- **3,449 games**
- **4.88 TB**
- **Scan time**: ~220ms (includes filtering logic)

Performance is excellent even with large libraries due to:
- Single CSV pass
- Efficient defaultdict aggregation
- Lazy loading (only loads when needed)

## File Size Accuracy

### Source Data
File sizes come from `master_inventory.csv` column `FileSize` (in bytes).

### Known Limitations

**Some platforms show 0 B:**
- **3DO Interactive Multiplayer**: No file size data in inventory
- **Sony Playstation 3**: PKG installs may not have size data
- **MS-DOS**: Some entries are shortcuts or metadata

**This is expected** - the inventory scanner reports what's in the master_inventory. If file sizes are missing, they'll need to be added during the inventory build process.

### File Size Calculation

```python
# Sum all game file sizes for platform
total_size = sum(game['file_size'] for game in platform['games'])

# Format to human-readable
# 1267650116608 bytes → 1.15 TB
```

## Integration

The Inventory Scanner integrates with:

### Migration Builder (Phase 2)
```python
# Show platforms to user for selection
scanner = InventoryScanner()
platforms = scanner.get_platform_summary(config_filters)

for platform in platforms:
    print(f"☐ {platform['name']}, {platform['game_count']} Games, {platform['size_formatted']}")
```

### Storage Planning
```python
# Calculate required storage per destination
internal_ssd_size = 0
sd_card_size = 0

for platform in selected_platforms:
    if platform['storage'] == 'internal_ssd':
        internal_ssd_size += platform['total_size_bytes']
    elif platform['storage'] == 'sd_card':
        sd_card_size += platform['total_size_bytes']

print(f"Internal SSD needed: {format_size(internal_ssd_size)}")
print(f"SD Card needed: {format_size(sd_card_size)}")
```

### Pre-flight Validation
```python
# Warn if total size exceeds available storage
totals = scanner.get_total_statistics(filters)

if totals['total_size_bytes'] > available_storage:
    print(f"⚠ Warning: {totals['size_formatted']} needed, but only {format_size(available_storage)} available")
```

## Testing

Run the test suite:
```bash
python3 scripts/inventory_scanner.py
```

This will:
- Scan full inventory (no filters)
- Show top 10 platforms with sizes
- Display total statistics
- Test with sample filters
- Show specific platform details

## Example Output

```
Platform Summary:
Arcade, 14647 Games, 73.3 GB
Nintendo Entertainment System, 867 Games, 74.9 MB
Nintendo Wii U, 766 Games, 1.15 TB
Sony Playstation 3, 331 Games, 0 B
Super Nintendo Entertainment System, 1011 Games, 140 MB

Total Statistics:
Platforms: 54
Games: 34,517
Total Size: 11.5 TB
```

## Future Enhancements

Potential improvements:
- **Size estimation**: Estimate sizes for platforms with missing data
- **Compression ratios**: Account for CHD/7z compression
- **Cache results**: Cache scans for faster repeated access
- **Delta scanning**: Only rescan changed platforms
- **Parallel processing**: Multi-threaded scanning for huge libraries

