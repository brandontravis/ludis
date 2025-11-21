#!/usr/bin/env python3
"""
Inventory Scanner - Analyzes master inventory for migration planning
====================================================================

This module scans the master_inventory.csv to provide platform statistics
for migration planning, including game counts and total file sizes.

Usage:
    from scripts.inventory_scanner import InventoryScanner
    
    scanner = InventoryScanner()
    platforms = scanner.get_platform_summary()
    for platform in platforms:
        print(f"{platform['name']}: {platform['game_count']} games, {platform['size_formatted']}")
"""

import csv
from pathlib import Path
from typing import Dict, List, Optional
from collections import defaultdict

# Project root is parent of scripts/ directory
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


class InventoryScanner:
    """Scans master inventory to provide platform statistics"""
    
    def __init__(self, inventory_path: Optional[Path] = None):
        """
        Initialize inventory scanner.
        
        Args:
            inventory_path: Path to master_inventory.csv (defaults to LB_Exports/master_inventory.csv)
        """
        if inventory_path is None:
            self.inventory_path = PROJECT_ROOT / "LB_Exports" / "master_inventory.csv"
        else:
            self.inventory_path = inventory_path
        
        if not self.inventory_path.exists():
            raise FileNotFoundError(f"Master inventory not found: {self.inventory_path}")
    
    def _format_size(self, size_bytes: int) -> str:
        """
        Format byte size to human-readable string.
        
        Args:
            size_bytes: Size in bytes
        
        Returns:
            Formatted string (e.g., "1.5 GB", "256 MB", "4.2 TB")
        """
        if size_bytes == 0:
            return "0 B"
        
        units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        unit_index = 0
        size = float(size_bytes)
        
        while size >= 1024.0 and unit_index < len(units) - 1:
            size /= 1024.0
            unit_index += 1
        
        # Format with appropriate precision
        if unit_index == 0:  # Bytes
            return f"{int(size)} {units[unit_index]}"
        elif size >= 100:
            return f"{int(size)} {units[unit_index]}"
        elif size >= 10:
            return f"{size:.1f} {units[unit_index]}"
        else:
            return f"{size:.2f} {units[unit_index]}"
    
    def _should_include_game(self, row: Dict[str, str], filters: Optional[Dict[str, bool]] = None) -> bool:
        """
        Determine if a game should be included based on filters.
        
        Args:
            row: CSV row from master_inventory
            filters: Dictionary of filter settings (same structure as config.yaml filters)
        
        Returns:
            True if game should be included, False otherwise
        """
        if filters is None:
            # No filters - include all games
            return True
        
        # Force exclude takes priority
        if filters.get('force_manual_exclude', True):
            manual_exclude = row.get('ManualExclude', '').strip().lower()
            if manual_exclude == 'true':
                return False
        
        # Force include overrides all other filters
        if filters.get('force_manual_include', True):
            manual_include = row.get('ManualInclude', '').strip().lower()
            if manual_include == 'true':
                return True
        
        # Check inclusion filters (OR logic - any match includes)
        matched = False
        
        # Check LaunchBox Favorites (native field)
        if filters.get('favorites', False):
            if row.get('Favorite', '').strip().lower() == 'true':
                matched = True
        
        # Check playlist-based filters
        playlists_str = row.get('Playlists', '')
        game_playlists = [p.strip() for p in playlists_str.split(';') if p.strip()]
        
        # Check each filter key
        for filter_key, enabled in filters.items():
            if not enabled:
                continue
            
            # Playlist filters start with 'playlist_'
            if filter_key.startswith('playlist_'):
                playlist_name = filter_key[9:]  # Remove 'playlist_' prefix
                if playlist_name in game_playlists:
                    matched = True
                    break
        
        # If no filters enabled (all False), include everything
        filter_keys = [k for k in filters.keys() if k not in ['force_manual_include', 'force_manual_exclude']]
        has_any_filter = any(filters.get(k, False) for k in filter_keys)
        
        if not has_any_filter:
            return True  # No filters enabled - include all
        
        return matched
    
    def get_platform_summary(self, filters: Optional[Dict[str, bool]] = None) -> List[Dict]:
        """
        Get summary statistics for all platforms in inventory.
        
        Args:
            filters: Optional filter settings to apply (same structure as config.yaml filters)
        
        Returns:
            List of dictionaries, each containing:
            - name: Platform name
            - game_count: Number of games
            - total_size_bytes: Total file size in bytes
            - size_formatted: Human-readable size string
            - games: List of game dictionaries (LBID, Title, FileSize)
        """
        platform_data = defaultdict(lambda: {
            'game_count': 0,
            'total_size_bytes': 0,
            'games': []
        })
        
        print(f"Scanning inventory: {self.inventory_path}")
        
        with open(self.inventory_path, 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                # Check if game should be included based on filters
                if not self._should_include_game(row, filters):
                    continue
                
                platform = row.get('Platform', '').strip()
                if not platform:
                    continue
                
                # Parse file size
                file_size = 0
                try:
                    file_size = int(row.get('FileSize', '0') or '0')
                except (ValueError, TypeError):
                    file_size = 0
                
                # Add to platform data
                platform_data[platform]['game_count'] += 1
                platform_data[platform]['total_size_bytes'] += file_size
                
                # Store game info
                game_info = {
                    'lbid': row.get('LBID', ''),
                    'title': row.get('Title', ''),
                    'file_size': file_size,
                }
                platform_data[platform]['games'].append(game_info)
        
        # Convert to list and format
        result = []
        for platform_name, data in platform_data.items():
            result.append({
                'name': platform_name,
                'game_count': data['game_count'],
                'total_size_bytes': data['total_size_bytes'],
                'size_formatted': self._format_size(data['total_size_bytes']),
                'games': data['games'],
            })
        
        # Sort by platform name
        result.sort(key=lambda x: x['name'])
        
        print(f"✓ Found {len(result)} platforms with games")
        
        return result
    
    def get_platform_details(self, platform_name: str, filters: Optional[Dict[str, bool]] = None) -> Optional[Dict]:
        """
        Get detailed information for a specific platform.
        
        Args:
            platform_name: Name of platform to get details for
            filters: Optional filter settings to apply
        
        Returns:
            Dictionary with platform statistics, or None if platform not found
        """
        platforms = self.get_platform_summary(filters)
        for platform in platforms:
            if platform['name'] == platform_name:
                return platform
        return None
    
    def get_total_statistics(self, filters: Optional[Dict[str, bool]] = None) -> Dict:
        """
        Get total statistics across all platforms.
        
        Args:
            filters: Optional filter settings to apply
        
        Returns:
            Dictionary with:
            - total_platforms: Number of platforms
            - total_games: Total number of games
            - total_size_bytes: Total file size in bytes
            - size_formatted: Human-readable total size
        """
        platforms = self.get_platform_summary(filters)
        
        total_games = sum(p['game_count'] for p in platforms)
        total_size = sum(p['total_size_bytes'] for p in platforms)
        
        return {
            'total_platforms': len(platforms),
            'total_games': total_games,
            'total_size_bytes': total_size,
            'size_formatted': self._format_size(total_size),
        }


def main():
    """Test the inventory scanner"""
    print("=" * 60)
    print("INVENTORY SCANNER TEST")
    print("=" * 60)
    
    scanner = InventoryScanner()
    
    # Test without filters
    print("\n" + "-" * 60)
    print("PLATFORM SUMMARY (NO FILTERS)")
    print("-" * 60)
    platforms = scanner.get_platform_summary()
    
    for platform in platforms[:10]:
        print(f"{platform['name']:40} {platform['game_count']:4} games  {platform['size_formatted']:>10}")
    
    if len(platforms) > 10:
        print(f"... and {len(platforms) - 10} more platforms")
    
    # Total statistics
    print("\n" + "-" * 60)
    print("TOTAL STATISTICS")
    print("-" * 60)
    totals = scanner.get_total_statistics()
    print(f"Platforms: {totals['total_platforms']}")
    print(f"Games:     {totals['total_games']:,}")
    print(f"Total Size: {totals['size_formatted']}")
    
    # Test with filters
    print("\n" + "-" * 60)
    print("PLATFORM SUMMARY (WITH FILTERS)")
    print("-" * 60)
    print("Filters: force_manual_include=True, include_favorites=True")
    
    test_filters = {
        'force_manual_include': True,
        'force_manual_exclude': True,
        'include_favorites': True,
    }
    
    filtered_platforms = scanner.get_platform_summary(test_filters)
    filtered_totals = scanner.get_total_statistics(test_filters)
    
    for platform in filtered_platforms[:10]:
        print(f"{platform['name']:40} {platform['game_count']:4} games  {platform['size_formatted']:>10}")
    
    if len(filtered_platforms) > 10:
        print(f"... and {len(filtered_platforms) - 10} more platforms")
    
    print(f"\nFiltered Total: {filtered_totals['total_games']} games, {filtered_totals['size_formatted']}")
    
    # Test specific platform
    print("\n" + "-" * 60)
    print("SPECIFIC PLATFORM DETAILS")
    print("-" * 60)
    
    if platforms:
        test_platform = platforms[0]['name']
        details = scanner.get_platform_details(test_platform)
        if details:
            print(f"Platform: {details['name']}")
            print(f"Games: {details['game_count']}")
            print(f"Size: {details['size_formatted']}")
            print(f"\nFirst 5 games:")
            for i, game in enumerate(details['games'][:5], 1):
                size_str = scanner._format_size(game['file_size'])
                print(f"  {i}. {game['title']:50} {size_str:>10}")


if __name__ == "__main__":
    main()

