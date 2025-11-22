#!/usr/bin/env python3
"""
Migration Builder - Interactive migration script generator
==========================================================

This module provides an interactive workflow for building ROM migration
scripts for various devices (Steam Deck, retro handhelds, etc.).

Usage:
    from scripts import migration_builder
    migration_builder.run_interactive(config)
"""

import sys
from pathlib import Path
from typing import Dict, Optional, List

try:
    import inquirer
except ImportError:
    print("ERROR: inquirer not installed. Run: pip install inquirer")
    sys.exit(1)

# Import local modules
from .inventory_scanner import InventoryScanner
from .platform_mapper import PlatformMapper

# Project root
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


def select_export_target(config) -> Optional[Dict]:
    """
    Select export target from config.yaml.
    
    Handles three scenarios:
    1. No targets enabled - show error and exit
    2. One target enabled - confirm with user
    3. Multiple targets enabled - let user choose
    
    Args:
        config: Config object with export_targets
    
    Returns:
        Dictionary with target name and configuration, or None if cancelled
    """
    print("\n" + "=" * 60)
    print("CREATE MIGRATION SCRIPT")
    print("=" * 60)
    
    # Get all export targets from config
    export_targets = config.get('export_targets', {})
    
    if not export_targets:
        print("\n✗ No export targets configured in config.yaml")
        print("\nTo use this feature:")
        print("1. Edit config.yaml")
        print("2. Add an export target (see config.yaml.sample for examples)")
        print("3. Set 'enabled: true' for the target")
        print("4. Run this command again")
        input("\nPress Enter to continue...")
        return None
    
    # Find enabled targets
    enabled_targets = {}
    for target_name, target_config in export_targets.items():
        if target_config.get('enabled', False):
            enabled_targets[target_name] = target_config
    
    # Scenario 1: No targets enabled
    if not enabled_targets:
        print("\n✗ No export targets enabled in config.yaml")
        print("\nAvailable targets (all disabled):")
        for target_name in export_targets.keys():
            print(f"  - {target_name}")
        print("\nTo use this feature:")
        print("1. Edit config.yaml")
        print("2. Set 'enabled: true' for at least one export target")
        print("3. Run this command again")
        input("\nPress Enter to continue...")
        return None
    
    # Scenario 2: One target enabled
    if len(enabled_targets) == 1:
        target_name = list(enabled_targets.keys())[0]
        target_config = enabled_targets[target_name]
        
        print(f"\nExport Target: {target_name}")
        print(f"Format: {target_config.get('format', 'unknown').upper()}", end="")
        if target_config.get('format', '').lower() == 'esde':
            print(" (EmulationStation Desktop Edition)")
        else:
            print()
        
        # Confirm with user
        confirm = inquirer.confirm(
            message="Proceed with this export target?",
            default=True
        )
        
        if not confirm:
            print("\nMigration cancelled.")
            return None
        
        return {
            'name': target_name,
            'config': target_config
        }
    
    # Scenario 3: Multiple targets enabled
    print(f"\nFound {len(enabled_targets)} enabled export targets.")
    
    # Build choices for inquirer
    choices = []
    for target_name, target_config in enabled_targets.items():
        format_str = target_config.get('format', 'unknown').upper()
        display_name = f"{target_name} ({format_str})"
        choices.append((display_name, target_name))
    
    questions = [
        inquirer.List('target',
                     message="Which export target?",
                     choices=choices,
                     ),
    ]
    
    answers = inquirer.prompt(questions)
    
    if not answers or not answers.get('target'):
        print("\nMigration cancelled.")
        return None
    
    selected_name = answers['target']
    selected_config = enabled_targets[selected_name]
    
    return {
        'name': selected_name,
        'config': selected_config
    }


def configure_filters(config, target_config) -> Optional[Dict]:
    """
    Interactive filter configuration.
    
    Allows user to select which games to include based on various filters.
    
    Args:
        config: Config object from ludis.py
        target_config: Selected export target configuration
    
    Returns:
        Dictionary of filter settings, or None if cancelled
    """
    print("\n" + "=" * 60)
    print("CONFIGURE FILTERS")
    print("=" * 60)
    print("\nSelect which games to include in this migration:")
    
    # Get default filters from target config
    defaults = target_config.get('defaults', {})
    default_filters = defaults.get('filters', {})
    
    # Ask for quick selection mode
    quick_select = inquirer.list_input(
        message="Filter preset",
        choices=[
            ('Use defaults (from config.yaml)', 'defaults'),
            ('Select all filters', 'all'),
            ('Custom selection', 'custom'),
        ],
        default='defaults'
    )
    
    # Determine defaults based on quick selection
    if quick_select == 'all':
        # Select all filters
        preset_defaults = {
            'include_overrides': True,
            'include_favorites': True,
            'include_platform_best': True,
            'include_classic_titles': True,
            'include_all_time_favorites': True,
            'include_backlog': True,
            'include_goty_winner': True,
            'include_goty_nominee': True,
            'include_on_deck': True,
            'include_retro': True,
            'include_franchises': True,
        }
    elif quick_select == 'defaults':
        # Use config.yaml defaults
        preset_defaults = default_filters.copy()
        preset_defaults['include_overrides'] = True  # Always include overrides
    else:  # custom
        # Use config.yaml defaults as starting point
        preset_defaults = default_filters.copy()
        preset_defaults['include_overrides'] = True
    
    # Build filter options in the specified order
    filter_options = [
        ('include_overrides', 'Include Overrides (ManualInclude/ManualExclude)', preset_defaults.get('include_overrides', True)),
        ('include_favorites', 'Include Favorites (LaunchBox favorites)', preset_defaults.get('include_favorites', False)),
        ('include_platform_best', 'Include Platform Best (CUSTOM_The Best)', preset_defaults.get('include_platform_best', False)),
        ('include_classic_titles', 'Include Classic Console Titles (curated playlists)', preset_defaults.get('include_classic_titles', False)),
        ('include_all_time_favorites', 'Include All-Time Favorites (CUSTOM_All Time Favorites)', preset_defaults.get('include_all_time_favorites', False)),
        ('include_backlog', 'Include Backlog (CUSTOM_Backlog)', preset_defaults.get('include_backlog', False)),
        ('include_goty_winner', 'Include GOTY Winners (CUSTOM_GOTY Winner)', preset_defaults.get('include_goty_winner', False)),
        ('include_goty_nominee', 'Include GOTY Nominees (CUSTOM_GOTY Nominee)', preset_defaults.get('include_goty_nominee', False)),
        ('include_on_deck', 'Include On Deck (CUSTOM_On Deck)', preset_defaults.get('include_on_deck', False)),
        ('include_retro', 'Include Retro Collection (CUSTOM_Retro Collection)', preset_defaults.get('include_retro', False)),
        ('include_franchises', 'Include Franchises (any franchise)', preset_defaults.get('include_franchises', False)),
    ]
    
    # Create checkbox list
    print()
    questions = [
        inquirer.Checkbox('filters',
                         message="Select filters (Space to toggle, Enter to confirm)",
                         choices=[display for key, display, default in filter_options],
                         default=[display for key, display, default in filter_options if default],
                         ),
    ]
    
    answers = inquirer.prompt(questions)
    
    if not answers:
        print("\nFilter selection cancelled.")
        return None
    
    selected_filters = answers.get('filters', [])
    
    # Map display names back to filter keys
    display_to_key = {display: key for key, display, default in filter_options}
    
    # Build filter dictionary
    filters = {}
    for display in selected_filters:
        filter_key = display_to_key.get(display)
        if filter_key == 'include_overrides':
            # Special case: enable both manual include and exclude
            filters['force_manual_include'] = True
            filters['force_manual_exclude'] = True
        else:
            filters[filter_key] = True
    
    # Set all other filters to False
    all_filter_keys = [
        'force_manual_include', 'force_manual_exclude',
        'include_favorites', 'include_platform_best', 'include_classic_titles',
        'include_all_time_favorites', 'include_backlog', 'include_goty_winner',
        'include_goty_nominee', 'include_on_deck', 'include_retro', 'include_franchises'
    ]
    for key in all_filter_keys:
        if key not in filters:
            filters[key] = False
    
    # Show summary
    print("\n" + "-" * 60)
    print("FILTER SUMMARY")
    print("-" * 60)
    active_filters = [display for display in selected_filters]
    if active_filters:
        print("Active filters:")
        for f in active_filters:
            print(f"  ✓ {f}")
    else:
        print("No filters selected (all games will be included)")
    
    # Confirm
    confirm = inquirer.confirm(
        message="Proceed with these filters?",
        default=True
    )
    
    if not confirm:
        print("\nFilter selection cancelled.")
        return None
    
    return filters


def select_platforms(config, filters: Dict) -> Optional[List[Dict]]:
    """
    Interactive platform selection with filtered game counts.
    
    Shows platforms in format: "Platform, X (of Y) Games, A (of B) GB"
    where X/A are filtered counts and Y/B are totals.
    
    Args:
        config: Config object from ludis.py
        filters: Dictionary of filter settings from configure_filters()
    
    Returns:
        List of selected platform dictionaries, or None if cancelled
    """
    print("\n" + "=" * 60)
    print("PLATFORM SELECTION")
    print("=" * 60)
    
    # Initialize scanners
    scanner = InventoryScanner()
    mapper = PlatformMapper()
    
    # Scan inventory twice: once without filters (totals), once with filters
    print("\nScanning library...")
    print("  - Getting total counts...")
    all_platforms = scanner.get_platform_summary(filters=None)
    
    print("  - Applying filters...")
    filtered_platforms = scanner.get_platform_summary(filters=filters)
    
    # Create lookup for filtered counts
    filtered_lookup = {p['name']: p for p in filtered_platforms}
    
    # Build platform choices with filtered counts
    platform_choices = []
    hidden_count = 0
    unsupported_platforms = []
    
    for platform in all_platforms:
        platform_name = platform['name']
        total_games = platform['game_count']
        total_size = platform['total_size_bytes']
        total_size_str = platform['size_formatted']
        
        # Get filtered counts
        filtered_data = filtered_lookup.get(platform_name)
        if filtered_data:
            filtered_games = filtered_data['game_count']
            filtered_size = filtered_data['total_size_bytes']
            filtered_size_str = filtered_data['size_formatted']
        else:
            # No games match filters - hide this platform
            hidden_count += 1
            continue
        
        # Check if platform is supported by ES-DE
        if not mapper.is_platform_supported(platform_name):
            unsupported_platforms.append(platform_name)
            # Still show it, but we'll warn later
        
        # Build display string
        if filtered_games == total_games:
            # All games included - simpler display
            display = f"{platform_name}, {total_games} Games, {total_size_str}"
        else:
            # Show filtered vs total
            display = f"{platform_name}, {filtered_games} (of {total_games}) Games, {filtered_size_str} (of {total_size_str})"
        
        platform_choices.append({
            'display': display,
            'name': platform_name,
            'filtered_games': filtered_games,
            'total_games': total_games,
            'filtered_size': filtered_size,
            'total_size': total_size,
            'filtered_size_str': filtered_size_str,
            'total_size_str': total_size_str,
            'games': filtered_data['games'],
        })
    
    # Show summary
    print(f"\n✓ Found {len(platform_choices)} platforms with games matching filters")
    if hidden_count > 0:
        print(f"  ({hidden_count} platforms hidden - no games match filters)")
    
    if not platform_choices:
        print("\n✗ No platforms have games matching your filters!")
        print("Try adjusting your filter selection.")
        input("\nPress Enter to continue...")
        return None
    
    # Show warnings for unsupported platforms
    if unsupported_platforms:
        print(f"\n⚠ Warning: {len(unsupported_platforms)} platform(s) not supported by ES-DE:")
        for p in unsupported_platforms[:3]:
            print(f"  - {p}")
        if len(unsupported_platforms) > 3:
            print(f"  ... and {len(unsupported_platforms) - 3} more")
        print("  These platforms will be skipped during migration.")
    
    # Create checkbox selection (all pre-selected)
    print("\nAll platforms pre-selected. Uncheck any you want to exclude:")
    print("(Space to toggle, Enter to confirm)\n")
    
    questions = [
        inquirer.Checkbox('platforms',
                         message="Select platforms",
                         choices=[p['display'] for p in platform_choices],
                         default=[p['display'] for p in platform_choices],  # Pre-select all
                         ),
    ]
    
    answers = inquirer.prompt(questions)
    
    if not answers or not answers.get('platforms'):
        print("\nNo platforms selected. Migration cancelled.")
        return None
    
    selected_displays = answers['platforms']
    
    # Map display strings back to platform data
    display_to_data = {p['display']: p for p in platform_choices}
    selected_platforms = [display_to_data[d] for d in selected_displays]
    
    # Calculate totals for selected platforms
    total_selected_games = sum(p['filtered_games'] for p in selected_platforms)
    total_selected_size = sum(p['filtered_size'] for p in selected_platforms)
    total_selected_size_str = scanner._format_size(total_selected_size)
    
    # Show selection summary
    print("\n" + "-" * 60)
    print("SELECTION SUMMARY")
    print("-" * 60)
    print(f"Selected: {len(selected_platforms)} platforms")
    print(f"Total games: {total_selected_games:,}")
    print(f"Total size: {total_selected_size_str}")
    
    # Confirm selection
    confirm = inquirer.confirm(
        message="Proceed with these platforms?",
        default=True
    )
    
    if not confirm:
        print("\nPlatform selection cancelled.")
        return None
    
    return selected_platforms


def assign_storage_locations(config, target: Dict, selected_platforms: List[Dict]) -> Optional[Dict[str, Dict]]:
    """
    Assign storage locations to selected platforms using defaults with override capability.
    
    Flow:
    1. Show platforms with their default storage assignments
    2. Let user select platforms they want to reassign
    3. For each reassigned platform, prompt for new storage location
    4. Show final summary and confirm
    
    Args:
        config: Config object
        target: Selected export target dictionary
        selected_platforms: List of platform dictionaries from select_platforms()
            Each dictionary contains:
            - 'name': platform name
            - 'filtered_games': number of games after filters
            - 'filtered_size': total size in bytes
    
    Returns:
        Dictionary mapping platform name to storage info:
        {
            "Nintendo Wii U": {
                "storage": "sd_card",  # or "internal_ssd" or "custom"
                "path": "/full/path/to/storage/location",
                "games": 52,
                "size": 91530598400
            }
        }
        Or None if cancelled
    """
    print("\n" + "=" * 60)
    print("ASSIGN STORAGE LOCATIONS")
    print("=" * 60)
    
    target_config = target['config']
    target_name = target['name']
    
    # Get platform storage defaults
    platform_defaults = target_config.get('platform_storage_defaults', {})
    
    if not platform_defaults:
        print("\n✗ Platform storage defaults not configured!")
        print("This shouldn't happen - please run 'Configure Platform Storage Defaults' first.")
        return None
    
    # Get storage location paths
    storage_locations = target_config.get('storage_locations', {})
    internal_ssd = storage_locations.get('internal_ssd', {})
    sd_card = storage_locations.get('sd_card', {})
    
    internal_path = internal_ssd.get('path', '')
    sd_path = sd_card.get('path', '')
    
    # Build initial storage assignments from defaults
    storage_assignments = {}
    
    for platform_info in selected_platforms:
        platform_name = platform_info['name']
        default_storage = platform_defaults.get(platform_name, 'custom')
        
        # Determine path based on storage type
        if default_storage == 'internal_ssd':
            storage_path = internal_path
        elif default_storage == 'sd_card':
            storage_path = sd_path
        else:  # custom
            storage_path = None
        
        storage_assignments[platform_name] = {
            'storage': default_storage,
            'path': storage_path,
            'games': platform_info['filtered_games'],
            'size': platform_info['filtered_size']
        }
    
    # Show current assignments
    print("\nDefault storage assignments:")
    print()
    
    # Group by storage location
    internal_platforms = []
    sd_platforms = []
    custom_platforms = []
    
    for platform_name in sorted(storage_assignments.keys()):
        assignment = storage_assignments[platform_name]
        storage = assignment['storage']
        games = assignment['games']
        
        if storage == 'internal_ssd':
            internal_platforms.append(platform_name)
            print(f"  [SSD] {platform_name} ({games:,} games)")
        elif storage == 'sd_card':
            sd_platforms.append(platform_name)
            print(f"  [SD ] {platform_name} ({games:,} games)")
        else:
            custom_platforms.append(platform_name)
            print(f"  [???] {platform_name} ({games:,} games) - needs custom path")
    
    # Summary
    print(f"\nInternal SSD: {len(internal_platforms)} platforms")
    print(f"SD Card: {len(sd_platforms)} platforms")
    if custom_platforms:
        print(f"Custom paths needed: {len(custom_platforms)} platforms")
    
    # Ask if user wants to change any assignments
    if not inquirer.confirm("\nChange any storage assignments?", default=False):
        # No changes, but still need to handle custom paths
        if custom_platforms:
            print("\n" + "=" * 60)
            print("CONFIGURE CUSTOM PATHS")
            print("=" * 60)
            
            for platform_name in custom_platforms:
                questions = [
                    inquirer.Text('path',
                                 message=f"Enter custom path for {platform_name}",
                                 validate=lambda _, x: len(x.strip()) > 0,
                                 )
                ]
                answer = inquirer.prompt(questions)
                if not answer:
                    print("\nCancelled.")
                    return None
                
                storage_assignments[platform_name]['path'] = answer['path'].strip()
        
        return storage_assignments
    
    # Let user select platforms to reassign
    print("\n" + "=" * 60)
    print("SELECT PLATFORMS TO REASSIGN")
    print("=" * 60)
    print("Use Space to select platforms you want to change, Enter to confirm")
    print()
    
    platform_choices = sorted(storage_assignments.keys())
    
    try:
        questions = [
            inquirer.Checkbox('platforms',
                             message="Select platforms to reassign",
                             choices=platform_choices,
                             default=[])
        ]
        
        answers = inquirer.prompt(questions)
        if not answers:
            print("\nCancelled.")
            return None
        
        platforms_to_reassign = answers['platforms']
    except Exception as e:
        print(f"\n✗ Error during platform selection: {e}")
        return None
    
    if not platforms_to_reassign:
        # User didn't select any, just handle custom paths if needed
        if custom_platforms:
            print("\n" + "=" * 60)
            print("CONFIGURE CUSTOM PATHS")
            print("=" * 60)
            
            for platform_name in custom_platforms:
                questions = [
                    inquirer.Text('path',
                                 message=f"Enter custom path for {platform_name}",
                                 validate=lambda _, x: len(x.strip()) > 0,
                                 )
                ]
                answer = inquirer.prompt(questions)
                if not answer:
                    print("\nCancelled.")
                    return None
                
                storage_assignments[platform_name]['path'] = answer['path'].strip()
        
        return storage_assignments
    
    # Reassign selected platforms
    print("\n" + "=" * 60)
    print("REASSIGN STORAGE LOCATIONS")
    print("=" * 60)
    
    for platform_name in platforms_to_reassign:
        current_storage = storage_assignments[platform_name]['storage']
        current_label = {
            'internal_ssd': 'Internal SSD',
            'sd_card': 'SD Card',
            'custom': 'Custom Path'
        }.get(current_storage, 'Unknown')
        
        print(f"\n{platform_name}")
        print(f"  Current: {current_label}")
        
        # Prompt for new storage location
        storage_choices = [
            ('Internal SSD', 'internal_ssd'),
            ('SD Card', 'sd_card'),
            ('Custom Path...', 'custom')
        ]
        
        questions = [
            inquirer.List('storage',
                         message="Select new storage location",
                         choices=storage_choices,
                         )
        ]
        
        answer = inquirer.prompt(questions)
        if not answer:
            print("\nCancelled.")
            return None
        
        new_storage = answer['storage']
        
        # Update assignment
        storage_assignments[platform_name]['storage'] = new_storage
        
        if new_storage == 'internal_ssd':
            storage_assignments[platform_name]['path'] = internal_path
        elif new_storage == 'sd_card':
            storage_assignments[platform_name]['path'] = sd_path
        else:  # custom
            questions = [
                inquirer.Text('path',
                             message=f"Enter custom path for {platform_name}",
                             validate=lambda _, x: len(x.strip()) > 0,
                             )
            ]
            answer = inquirer.prompt(questions)
            if not answer:
                print("\nCancelled.")
                return None
            
            storage_assignments[platform_name]['path'] = answer['path'].strip()
    
    # Final summary
    print("\n" + "=" * 60)
    print("FINAL STORAGE ASSIGNMENTS")
    print("=" * 60)
    
    # Recalculate groups
    internal_platforms = []
    sd_platforms = []
    custom_platforms = []
    
    internal_games = 0
    sd_games = 0
    custom_games = 0
    
    for platform_name in sorted(storage_assignments.keys()):
        assignment = storage_assignments[platform_name]
        storage = assignment['storage']
        games = assignment['games']
        
        if storage == 'internal_ssd':
            internal_platforms.append(platform_name)
            internal_games += games
            print(f"  [SSD] {platform_name} ({games:,} games)")
        elif storage == 'sd_card':
            sd_platforms.append(platform_name)
            sd_games += games
            print(f"  [SD ] {platform_name} ({games:,} games)")
        else:
            custom_platforms.append(platform_name)
            custom_games += games
            custom_path = assignment['path']
            print(f"  [CUS] {platform_name} ({games:,} games) → {custom_path}")
    
    print(f"\nInternal SSD: {len(internal_platforms)} platforms, {internal_games:,} games")
    print(f"SD Card: {len(sd_platforms)} platforms, {sd_games:,} games")
    if custom_platforms:
        print(f"Custom paths: {len(custom_platforms)} platforms, {custom_games:,} games")
    
    # Confirm
    if not inquirer.confirm("\nProceed with these storage assignments?", default=True):
        print("\nCancelled.")
        return None
    
    return storage_assignments


def check_previous_configuration(config, target_name: str) -> Optional[Dict]:
    """
    Check if there are previous migration configurations for this target.
    
    Args:
        config: Config object
        target_name: Name of the export target
    
    Returns:
        Most recent configuration dict, or None if no history exists
    """
    migration_history = config.get('migration_history', {})
    configurations = migration_history.get('configurations', [])
    
    # Filter configurations for this target
    target_configs = [c for c in configurations if c.get('export_target') == target_name]
    
    if not target_configs:
        return None
    
    # Return most recent
    return target_configs[0]


def offer_previous_configuration(config, target_name: str, previous_config: Dict) -> bool:
    """
    Offer user the choice to use previous configuration or create new.
    
    Args:
        config: Config object
        target_name: Name of the export target
        previous_config: Most recent configuration
    
    Returns:
        True if user wants to use previous config, False if create new
    """
    from datetime import datetime
    
    print("\n" + "=" * 60)
    print("PREVIOUS CONFIGURATION FOUND")
    print("=" * 60)
    
    timestamp = previous_config.get('timestamp', 'Unknown')
    try:
        dt = datetime.fromisoformat(timestamp)
        date_str = dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        date_str = timestamp
    
    print(f"\nLast migration for {target_name}:")
    print(f"  Date: {date_str}")
    print(f"  Platforms: {previous_config.get('platform_count', 0)}")
    print(f"  Total games: {previous_config.get('total_games', 0):,}")
    print(f"  Total size: {previous_config.get('total_size_formatted', 'Unknown')}")
    
    # Show filter summary
    filters = previous_config.get('filters', {})
    enabled_filters = [k.replace('include_', '').replace('_', ' ').title() 
                      for k, v in filters.items() if v and k != 'custom_fields']
    if enabled_filters:
        print(f"  Filters: {', '.join(enabled_filters)}")
    
    print()
    
    choices = [
        ('Use this configuration (with optional modifications)', 'use'),
        ('Create new configuration', 'new'),
    ]
    
    questions = [
        inquirer.List('choice',
                     message="What would you like to do?",
                     choices=choices,
                     )
    ]
    
    answer = inquirer.prompt(questions)
    if not answer:
        return False
    
    return answer['choice'] == 'use'


def use_previous_configuration_workflow(config, target: Dict, previous_config: Dict) -> Optional[Dict]:
    """
    Load previous configuration and allow user to modify it.
    
    Args:
        config: Config object
        target: Export target dictionary
        previous_config: Previous configuration to load
    
    Returns:
        Updated configuration dict, or None if cancelled
    """
    print("\n" + "=" * 60)
    print("REVIEW PREVIOUS CONFIGURATION")
    print("=" * 60)
    
    # Ask if user wants to modify anything
    print("\nYou can use this configuration as-is or modify specific parts:")
    print("  - Filters")
    print("  - Platform selection")
    print("  - Storage assignments")
    
    if not inquirer.confirm("\nMake any changes to this configuration?", default=False):
        # Use as-is
        return previous_config
    
    # Allow modifications
    print("\nWhat would you like to modify?")
    print("(Note: Changing earlier steps will require re-doing later steps)")
    
    # Load previous values
    filters = previous_config.get('filters', {})
    platforms = previous_config.get('platforms', [])
    storage_assignments = previous_config.get('storage_assignments', {})
    
    # Build modification choices showing cascade relationship
    modification_choices = [
        ('Filters → Platform selection → Storage assignments', 'all'),
        ('Platform selection → Storage assignments', 'platforms_and_storage'),
        ('Storage assignments only', 'storage_only'),
        ('Done - use current configuration', 'done'),
    ]
    
    questions = [
        inquirer.List('modify',
                     message="Select modification scope",
                     choices=modification_choices,
                     )
    ]
    
    answer = inquirer.prompt(questions)
    if not answer:
        return None
    
    choice = answer['modify']
    
    if choice == 'done':
        # Keep existing configuration
        pass
    elif choice == 'all':
        # Reconfigure everything starting from filters
        new_filters = configure_filters(config, target['config'])
        if not new_filters:
            print("\n✗ Filter configuration cancelled")
            return None
        filters = new_filters
        
        new_platforms = select_platforms(config, filters)
        if not new_platforms:
            print("\n✗ Platform selection cancelled")
            return None
        platforms = new_platforms
        
        new_storage = assign_storage_locations(config, target, platforms)
        if not new_storage:
            print("\n✗ Storage assignment cancelled")
            return None
        storage_assignments = new_storage
        
    elif choice == 'platforms_and_storage':
        # Reconfigure platforms and storage (keep existing filters)
        if not filters:
            print("\n✗ No existing filters found - please start with 'Filters → Platform selection → Storage'")
            return None
        
        new_platforms = select_platforms(config, filters)
        if not new_platforms:
            print("\n✗ Platform selection cancelled")
            return None
        platforms = new_platforms
        
        new_storage = assign_storage_locations(config, target, platforms)
        if not new_storage:
            print("\n✗ Storage assignment cancelled")
            return None
        storage_assignments = new_storage
        
    elif choice == 'storage_only':
        # Reconfigure storage only (keep existing filters and platforms)
        if not filters or not platforms:
            missing = []
            if not filters:
                missing.append('filters')
            if not platforms:
                missing.append('platforms')
            print(f"\n✗ Missing {' and '.join(missing)} - please start with an earlier step")
            return None
        
        new_storage = assign_storage_locations(config, target, platforms)
        if not new_storage:
            print("\n✗ Storage assignment cancelled")
            return None
        storage_assignments = new_storage
    
    # Validate we have everything
    if not filters or not platforms or not storage_assignments:
        print("\n✗ Incomplete configuration")
        return None
    
    return {
        'filters': filters,
        'platforms': platforms,
        'storage_assignments': storage_assignments,
    }


def save_migration_configuration(config, target_name: str, migration_config: Dict):
    """
    Save migration configuration to config.yaml migration_history.
    
    Keeps last 5 configurations per target.
    
    Args:
        config: Config object
        target_name: Name of the export target
        migration_config: Configuration dictionary with filters, platforms, storage_assignments
    """
    from datetime import datetime
    import yaml
    
    config_file = PROJECT_ROOT / 'config.yaml'
    
    # Load current config
    with open(config_file, 'r') as f:
        config_data = yaml.safe_load(f)
    
    # Initialize migration_history if needed
    if 'migration_history' not in config_data:
        config_data['migration_history'] = {
            'configurations': []
        }
    
    # Calculate totals
    platforms = migration_config.get('platforms', [])
    storage_assignments = migration_config.get('storage_assignments', {})
    
    # Calculate totals from storage_assignments (which always has the counts)
    # platforms might be a list of strings (from saved config) or dicts (from new config)
    total_games = sum(assignment.get('games', 0) for assignment in storage_assignments.values())
    total_size = sum(assignment.get('size', 0) for assignment in storage_assignments.values())
    
    # Format size
    def format_size(bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    # Build platform list - handle both dict and string formats
    if not platforms:
        platform_names = []
    elif isinstance(platforms[0], dict):
        # New configuration - platforms are dicts
        platform_names = [p['name'] for p in platforms]
    else:
        # Reused configuration - platforms are already strings
        platform_names = platforms
    
    # Build configuration record
    config_record = {
        'timestamp': datetime.now().isoformat(),
        'export_target': target_name,
        'platform_count': len(platform_names),
        'total_games': total_games,
        'total_size_bytes': total_size,
        'total_size_formatted': format_size(total_size),
        'filters': migration_config.get('filters', {}),
        'platforms': platform_names,
        'storage_assignments': storage_assignments,
    }
    
    # Add to history
    configurations = config_data['migration_history']['configurations']
    
    # Filter to keep only this target's configs
    other_target_configs = [c for c in configurations if c.get('export_target') != target_name]
    this_target_configs = [c for c in configurations if c.get('export_target') == target_name]
    
    # Add new config at the beginning
    this_target_configs.insert(0, config_record)
    
    # Keep last 5 for this target
    this_target_configs = this_target_configs[:5]
    
    # Combine back
    config_data['migration_history']['configurations'] = this_target_configs + other_target_configs
    config_data['migration_history']['last_migration'] = datetime.now().isoformat()
    
    # Save
    with open(config_file, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)


def generate_platform_script(platform_name: str, platform_data: Dict, operation: str, scripts_dir: Path):
    """Generate individual platform migration script."""
    esde_folder = platform_data['esde_folder']
    games = platform_data['games']
    
    script_name = f"migrate_{esde_folder}.py"
    script_path = scripts_dir / script_name
    
    # Format size helper
    def format_size(bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    total_size_str = format_size(platform_data['total_size'])
    
    lines = []
    lines.append("#!/usr/bin/env python3")
    lines.append(f"# Auto-generated migration script for {platform_name}")
    lines.append(f"# {platform_data['game_count']} games, {total_size_str}")
    lines.append(f"# Operation: {operation}")
    lines.append("")
    lines.append("import os")
    lines.append("import shutil")
    lines.append("from pathlib import Path")
    lines.append("")
    lines.append("PLATFORM_NAME = " + repr(platform_name))
    lines.append("ESDE_FOLDER = " + repr(esde_folder))
    lines.append("OPERATION = " + repr(operation))
    lines.append("")
    lines.append("GAMES = [")
    
    for game in games:
        lines.append("    {")
        lines.append(f"        'title': {repr(game['title'])},")
        lines.append(f"        'filename': {repr(game['filename'])},")
        lines.append(f"        'source_relative': {repr(game['source_relative'])},")  # Use relative path
        lines.append(f"        'dest': {repr(game['dest'])},")
        lines.append(f"        'size': {game['size']},")
        lines.append("    },")
    
    lines.append("]")
    lines.append("")
    lines.append("def migrate(nas_base_path, dry_run=False, overwrite=False):")
    lines.append("    \"\"\"Execute migration for this platform.\"\"\"")
    lines.append("    print(f'\\nMigrating {PLATFORM_NAME}...')")
    lines.append("    print(f'  {len(GAMES)} games')")
    lines.append("    ")
    lines.append("    success_count = 0")
    lines.append("    skip_count = 0")
    lines.append("    error_count = 0")
    lines.append("    ")
    lines.append("    nas_base = Path(nas_base_path)")
    lines.append("    ")
    lines.append("    for game in GAMES:")
    lines.append("        source = nas_base / game['source_relative']")
    lines.append("        dest = Path(game['dest'])")
    lines.append("        ")
    lines.append("        # Check if source exists")
    lines.append("        if not source.exists():")
    lines.append("            print(f\"  ✗ Missing: {game['title']}\")")
    lines.append("            error_count += 1")
    lines.append("            continue")
    lines.append("        ")
    lines.append("        # Check if dest exists")
    lines.append("        if dest.exists() and not overwrite:")
    lines.append("            skip_count += 1")
    lines.append("            continue")
    lines.append("        ")
    lines.append("        if dry_run:")
    lines.append("            print(f\"  [DRY RUN] Would {OPERATION}: {game['title']}\")")
    lines.append("            success_count += 1")
    lines.append("        else:")
    lines.append("            try:")
    lines.append("                # Create destination directory")
    lines.append("                dest.parent.mkdir(parents=True, exist_ok=True)")
    lines.append("                ")
    lines.append("                if OPERATION == 'copy':")
    lines.append("                    shutil.copy2(source, dest)")
    lines.append("                else:  # symlink")
    lines.append("                    if dest.exists():")
    lines.append("                        dest.unlink()")
    lines.append("                    dest.symlink_to(source)")
    lines.append("                ")
    lines.append("                success_count += 1")
    lines.append("            except Exception as e:")
    lines.append("                print(f\"  ✗ Error with {game['title']}: {e}\")")
    lines.append("                error_count += 1")
    lines.append("    ")
    lines.append("    return {")
    lines.append("        'platform': PLATFORM_NAME,")
    lines.append("        'success': success_count,")
    lines.append("        'skipped': skip_count,")
    lines.append("        'errors': error_count,")
    lines.append("        'total': len(GAMES)")
    lines.append("    }")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    lines.append("    # Can be run standalone")
    lines.append("    import sys")
    lines.append("    ")
    lines.append("    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h']:")
    lines.append("        print('Usage: {} <nas_base_path> [--dry-run] [--overwrite]'.format(sys.argv[0]))")
    lines.append("        print('  nas_base_path: Where your NAS is mounted (e.g., /mnt/nas, /media/nas)')")
    lines.append("        sys.exit(1)")
    lines.append("    ")
    lines.append("    nas_base_path = sys.argv[1]")
    lines.append("    dry_run = '--dry-run' in sys.argv")
    lines.append("    overwrite = '--overwrite' in sys.argv")
    lines.append("    result = migrate(nas_base_path, dry_run=dry_run, overwrite=overwrite)")
    lines.append("    print(f\"\\n✓ {result['platform']}: {result['success']}/{result['total']} games\")")
    
    with open(script_path, 'w') as f:
        f.write('\n'.join(lines))
    
    # Make executable
    script_path.chmod(0o755)
    
    return script_name


def generate_migration_runner(dist_dir: Path, target: Dict, file_list: Dict, operation: str, script_names: List[str]):
    """Generate the main ludis-migrate.py runner script."""
    from datetime import datetime
    
    target_name = target['name']
    platforms_data = file_list['platforms']
    
    runner_path = dist_dir / 'ludis-migrate.py'
    
    lines = []
    lines.append("#!/usr/bin/env python3")
    lines.append(f"# Ludis ROM Migration Runner for {target_name}")
    lines.append(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"# Operation: {operation}")
    lines.append("")
    lines.append("import sys")
    lines.append("from pathlib import Path")
    lines.append("")
    lines.append("# Add scripts directory to path")
    lines.append("sys.path.insert(0, str(Path(__file__).parent / 'scripts'))")
    lines.append("")
    lines.append("# Import platform migration modules")
    
    for script_name in script_names:
        module_name = script_name.replace('.py', '')
        lines.append(f"import {module_name}")
    
    lines.append("")
    lines.append("PLATFORMS = {")
    
    for platform_name, platform_data in sorted(platforms_data.items()):
        module_name = f"migrate_{platform_data['esde_folder']}"
        
        def format_size(bytes_val):
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if bytes_val < 1024.0:
                    return f"{bytes_val:.2f} {unit}"
                bytes_val /= 1024.0
            return f"{bytes_val:.2f} PB"
        
        size_str = format_size(platform_data['total_size'])
        
        lines.append(f"    {repr(platform_name)}: {{")
        lines.append(f"        'module': {module_name},")
        lines.append(f"        'games': {platform_data['game_count']},")
        lines.append(f"        'size': {repr(size_str)},")
        lines.append(f"        'esde_folder': {repr(platform_data['esde_folder'])},")
        lines.append("    },")
    
    lines.append("}")
    lines.append("")
    lines.append("def main():")
    lines.append("    print('=' * 60)")
    lines.append(f"    print('LUDIS ROM MIGRATION - {target_name.upper()}')")
    lines.append("    print('=' * 60)")
    lines.append("    print()")
    lines.append("    print(f'Available platforms: {len(PLATFORMS)}')")
    lines.append("    ")
    lines.append("    # Show platform list")
    lines.append("    print('\\nPlatforms:')")
    lines.append("    for name, info in sorted(PLATFORMS.items()):")
    lines.append("        print(f\"  - {name}: {info['games']} games, {info['size']}\")")
    lines.append("    ")
    lines.append("    # Simple menu")
    lines.append("    print('\\n' + '=' * 60)")
    lines.append("    print('OPTIONS')")
    lines.append("    print('=' * 60)")
    lines.append("    print('1. Migrate all platforms')")
    lines.append("    print('2. Select specific platforms (not yet implemented)')")
    lines.append("    print('3. Exit')")
    lines.append("    ")
    lines.append("    choice = input('\\nSelect option [1]: ').strip() or '1'")
    lines.append("    ")
    lines.append("    if choice == '3':")
    lines.append("        print('\\nExiting.')")
    lines.append("        return")
    lines.append("    ")
    lines.append("    if choice != '1':")
    lines.append("        print('\\n⚠ Option not yet implemented. Exiting.')")
    lines.append("        return")
    lines.append("    ")
    lines.append("    # Get migration options")
    lines.append("    print('\\n' + '=' * 60)")
    lines.append("    print('MIGRATION OPTIONS')")
    lines.append("    print('=' * 60)")
    lines.append("    ")
    lines.append("    # NAS base path")
    lines.append("    print('\\nWhere is your NAS/source library mounted on this device?')")
    lines.append("    print('Examples:')")
    lines.append("    print('  /mnt/nas')")
    lines.append("    print('  /media/nas/games/library')")
    lines.append("    print('  /run/media/USERNAME/DRIVE/games/library')")
    lines.append("    ")
    lines.append("    nas_base_path = input('\\nNAS mount path: ').strip()")
    lines.append("    ")
    lines.append("    if not nas_base_path:")
    lines.append("        print('\\n✗ NAS path is required')")
    lines.append("        return")
    lines.append("    ")
    lines.append("    nas_base = Path(nas_base_path)")
    lines.append("    if not nas_base.exists():")
    lines.append("        print(f'\\n⚠ Warning: Path does not exist: {nas_base_path}')")
    lines.append("        confirm = input('Continue anyway? (y/N): ').strip().lower()")
    lines.append("        if confirm != 'y':")
    lines.append("            print('\\nCancelled.')")
    lines.append("            return")
    lines.append("    ")
    lines.append("    dry_run_input = input('\\nDry run mode? (y/N): ').strip().lower()")
    lines.append("    dry_run = dry_run_input == 'y'")
    lines.append("    ")
    lines.append("    overwrite_input = input('Overwrite existing files? (y/N): ').strip().lower()")
    lines.append("    overwrite = overwrite_input == 'y'")
    lines.append("    ")
    lines.append("    if dry_run:")
    lines.append("        print('\\n⚠ DRY RUN MODE - No files will be copied')")
    lines.append("    ")
    lines.append("    # Confirm")
    lines.append("    confirm = input('\\nProceed? (Y/n): ').strip().lower()")
    lines.append("    if confirm == 'n':")
    lines.append("        print('\\nCancelled.')")
    lines.append("        return")
    lines.append("    ")
    lines.append("    # Execute migrations")
    lines.append("    print('\\n' + '=' * 60)")
    lines.append("    print('EXECUTING MIGRATION')")
    lines.append("    print('=' * 60)")
    lines.append("    ")
    lines.append("    results = []")
    lines.append("    ")
    lines.append("    for platform_name in sorted(PLATFORMS.keys()):")
    lines.append("        platform_info = PLATFORMS[platform_name]")
    lines.append("        module = platform_info['module']")
    lines.append("        ")
    lines.append("        try:")
    lines.append("            result = module.migrate(nas_base_path, dry_run=dry_run, overwrite=overwrite)")
    lines.append("            results.append(result)")
    lines.append("        except Exception as e:")
    lines.append("            print(f'\\n✗ Error migrating {platform_name}: {e}')")
    lines.append("            results.append({")
    lines.append("                'platform': platform_name,")
    lines.append("                'success': 0,")
    lines.append("                'skipped': 0,")
    lines.append("                'errors': platform_info['games'],")
    lines.append("                'total': platform_info['games']")
    lines.append("            })")
    lines.append("    ")
    lines.append("    # Show summary")
    lines.append("    print('\\n' + '=' * 60)")
    lines.append("    print('MIGRATION SUMMARY')")
    lines.append("    print('=' * 60)")
    lines.append("    ")
    lines.append("    total_success = sum(r['success'] for r in results)")
    lines.append("    total_skipped = sum(r['skipped'] for r in results)")
    lines.append("    total_errors = sum(r['errors'] for r in results)")
    lines.append("    total_games = sum(r['total'] for r in results)")
    lines.append("    ")
    lines.append("    print(f'\\nTotal games: {total_games:,}')")
    lines.append("    print(f'  Successful: {total_success:,}')")
    lines.append("    print(f'  Skipped: {total_skipped:,}')")
    lines.append("    print(f'  Errors: {total_errors:,}')")
    lines.append("    ")
    lines.append("    if dry_run:")
    lines.append("        print('\\n(This was a dry run - no files were actually copied)')")
    lines.append("    ")
    lines.append("    print('\\n✓ Migration complete!')")
    lines.append("")
    lines.append("if __name__ == '__main__':")
    lines.append("    main()")
    
    with open(runner_path, 'w') as f:
        f.write('\n'.join(lines))
    
    # Make executable
    runner_path.chmod(0o755)
    
    return runner_path


def generate_manifest(dist_dir: Path, target: Dict, migration_config: Dict, file_list: Dict, operation: str, timestamp: str):
    """Generate migration manifest JSON file."""
    import json
    
    manifest = {
        'timestamp': timestamp,
        'target': target['name'],
        'operation': operation,
        'filters': migration_config['filters'],
        'platforms': {},
        'windows_games': file_list['windows_games'],
        'totals': {
            'platforms': len(file_list['platforms']),
            'games': sum(p['game_count'] for p in file_list['platforms'].values()),
            'size_bytes': sum(p['total_size'] for p in file_list['platforms'].values()),
        }
    }
    
    # Add platform details
    for platform_name, platform_data in file_list['platforms'].items():
        manifest['platforms'][platform_name] = {
            'esde_folder': platform_data['esde_folder'],
            'storage_path': platform_data['storage_path'],
            'game_count': platform_data['game_count'],
            'size_bytes': platform_data['total_size'],
            'games': [
                {
                    'title': game['title'],
                    'filename': game['filename'],
                    'source_relative': game['source_relative'],
                    'dest': game['dest'],
                    'size': game['size']
                }
                for game in platform_data['games']
            ]
        }
    
    manifest_path = dist_dir / 'manifest.json'
    
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    return manifest_path


def generate_gamelists(dist_dir: Path, file_list: Dict):
    """Generate ES-DE gamelist.xml files for each platform."""
    gamelists_dir = dist_dir / 'gamelists'
    gamelists_dir.mkdir(exist_ok=True)
    
    count = 0
    
    for platform_name, platform_data in file_list['platforms'].items():
        esde_folder = platform_data['esde_folder']
        
        platform_dir = gamelists_dir / esde_folder
        platform_dir.mkdir(exist_ok=True)
        
        gamelist_path = platform_dir / 'gamelist.xml'
        
        # Generate XML
        lines = []
        lines.append('<?xml version="1.0"?>')
        lines.append('<gameList>')
        
        for game in platform_data['games']:
            filename = game['filename']
            title = game['title']
            developer = game.get('developer', '')
            publisher = game.get('publisher', '')
            genre = game.get('genre', '')
            release_date = game.get('release_date', '')
            rating = game.get('rating', '')
            
            # Skip if we don't have minimum data
            if not filename or not title:
                continue
            
            # XML escape function
            def xml_escape(text):
                if not text:
                    return ''
                return (str(text)
                    .replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;')
                    .replace('"', '&quot;')
                    .replace("'", '&apos;'))
            
            lines.append('  <game>')
            lines.append(f'    <path>./{xml_escape(filename)}</path>')
            lines.append(f'    <name>{xml_escape(title)}</name>')
            if developer:
                lines.append(f'    <developer>{xml_escape(developer)}</developer>')
            if publisher:
                lines.append(f'    <publisher>{xml_escape(publisher)}</publisher>')
            if genre:
                lines.append(f'    <genre>{xml_escape(genre)}</genre>')
            if release_date:
                lines.append(f'    <releasedate>{xml_escape(release_date)}</releasedate>')
            if rating:
                try:
                    # Convert 0-5 rating to 0-1 for ES-DE
                    rating_float = float(rating) / 5.0
                    lines.append(f'    <rating>{rating_float:.2f}</rating>')
                except:
                    pass
            lines.append('  </game>')
        
        lines.append('</gameList>')
        
        with open(gamelist_path, 'w') as f:
            f.write('\n'.join(lines))
        
        count += 1
    
    return count


def generate_windows_install_list(dist_dir: Path, windows_games: List[str], timestamp: str):
    """Generate Windows games install list."""
    if not windows_games:
        return None
    
    install_list_path = dist_dir / 'install_list_windows.txt'
    
    lines = []
    lines.append("# Windows Games Install List")
    lines.append(f"# Generated: {timestamp}")
    lines.append(f"# Total: {len(windows_games)} games")
    lines.append("")
    lines.append("# These games need to be manually installed/configured")
    lines.append("# (Cloud launchers, pirated games, etc.)")
    lines.append("")
    
    for game_title in sorted(windows_games):
        lines.append(game_title)
    
    with open(install_list_path, 'w') as f:
        f.write('\n'.join(lines))
    
    return install_list_path


def validate_migration(file_list: Dict) -> Dict:
    """
    Calculate storage requirements for migration.
    
    Note: Source file validation happens on the target device during migration,
    not during script generation. This is because source files may not be
    accessible from the machine generating the scripts.
    
    Args:
        file_list: File list from build_file_list()
    
    Returns:
        Validation report dictionary with storage statistics
    """
    print("\n" + "=" * 60)
    print("STORAGE REQUIREMENTS")
    print("=" * 60)
    
    platforms_data = file_list['platforms']
    
    # Calculate storage requirements by destination path
    storage_requirements = {}
    
    for platform_name, platform_data in platforms_data.items():
        for game in platform_data['games']:
            storage_path = platform_data['storage_path']
            if storage_path not in storage_requirements:
                storage_requirements[storage_path] = {
                    'size': 0,
                    'games': 0,
                    'platforms': set()
                }
            
            storage_requirements[storage_path]['size'] += game['size']
            storage_requirements[storage_path]['games'] += 1
            storage_requirements[storage_path]['platforms'].add(platform_name)
    
    # Report storage requirements
    def format_size(bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    for storage_path, requirements in sorted(storage_requirements.items()):
        size_str = format_size(requirements['size'])
        game_count = requirements['games']
        platform_count = len(requirements['platforms'])
        print(f"\n  {storage_path}")
        print(f"    {game_count:,} games across {platform_count} platforms")
        print(f"    Total size: {size_str}")
    
    print("\nNote: Source file validation will occur on the target device during migration.")
    
    return {
        'storage_requirements': storage_requirements
    }


def build_file_list(config, target: Dict, migration_config: Dict) -> Dict:
    """
    Build comprehensive file list for migration.
    
    Queries master_inventory.csv for selected platforms and builds
    source -> destination mappings.
    
    Args:
        config: Config object
        target: Export target dictionary
        migration_config: Migration configuration with filters, platforms, storage
    
    Returns:
        Dictionary with platform data and Windows games list:
        {
            'platforms': {
                'Nintendo 64': {
                    'games': [...],
                    'esde_folder': 'n64',
                    'storage_path': '/path/to/storage',
                    'game_count': 125,
                    'total_size': 2500000000
                }
            },
            'windows_games': ['Game Title 1', 'Game Title 2']
        }
    """
    print("\n" + "=" * 60)
    print("BUILDING FILE LIST")
    print("=" * 60)
    
    master_inv = PROJECT_ROOT / 'LB_Exports' / 'master_inventory.csv'
    scanner = InventoryScanner(master_inv)
    mapper = PlatformMapper()
    
    storage_assignments = migration_config['storage_assignments']
    filters = migration_config['filters']
    
    platforms_data = {}
    windows_games = []
    
    print("\nProcessing platforms...")
    
    # Read CSV once and group games by platform
    import csv
    from pathlib import Path as PathLib
    
    # First pass: read CSV and collect games by platform
    platform_games_map = {platform_name: [] for platform_name in storage_assignments.keys()}
    
    print("  Reading master inventory...")
    with open(master_inv, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            platform = row.get('Platform', '').strip()
            
            # Skip if not one of our selected platforms
            if platform not in storage_assignments:
                continue
            
            # Apply filters
            if not scanner._should_include_game(row, filters):
                continue
            
            # Store the full row for this platform
            platform_games_map[platform].append(row)
    
    # Second pass: process each platform
    for platform_name, assignment in storage_assignments.items():
        rows = platform_games_map[platform_name]
        
        if not rows:
            continue
        
        # Get ES-DE folder name
        esde_folder = mapper.lb_to_esde(platform_name)
        
        if not esde_folder:
            print(f"  ⚠ Skipping {platform_name} (not supported by ES-DE)")
            continue
        
        # Special handling for Windows - just collect titles
        if platform_name == 'Windows':
            windows_games = [row.get('Title', 'Unknown') for row in rows]
            print(f"  ✓ Windows: {len(windows_games)} games (install list only)")
            continue
        
        storage_path = assignment['path']
        
        # Build game list with source -> destination mappings
        game_list = []
        total_size = 0
        
        for row in rows:
            # Get source path (relative from NAS base)
            source_relative = row.get('NASPath', '').strip()
            if not source_relative:
                continue
            
            filename = PathLib(source_relative).name
            dest_path = f"{storage_path}/{esde_folder}/{filename}"
            
            file_size = 0
            try:
                file_size = int(row.get('FileSize', 0)) if row.get('FileSize') else 0
            except (ValueError, TypeError):
                pass
            
            game_list.append({
                'title': row.get('Title', 'Unknown'),
                'filename': filename,
                'source_relative': source_relative,  # Relative path - will be resolved on target device
                'dest': dest_path,
                'size': file_size,
                'developer': row.get('Developer', ''),
                'publisher': row.get('Publisher', ''),
                'genre': row.get('Genre', ''),
                'release_date': row.get('ReleaseDate', ''),
                'rating': row.get('CommunityStarRating', ''),
            })
            
            total_size += file_size
        
        if not game_list:
            continue
        
        platforms_data[platform_name] = {
            'games': game_list,
            'esde_folder': esde_folder,
            'storage_path': storage_path,
            'game_count': len(game_list),
            'total_size': total_size
        }
        
        print(f"  ✓ {platform_name}: {len(game_list)} games")
    
    print(f"\n✓ Processed {len(platforms_data)} platforms")
    if windows_games:
        print(f"✓ Found {len(windows_games)} Windows games for install list")
    
    return {
        'platforms': platforms_data,
        'windows_games': windows_games
    }


def run_interactive(config):
    """
    Run the interactive migration script builder.
    
    This is the main entry point called from ludis.py menu.
    
    Args:
        config: Config object from ludis.py
    """
    # Step 2.2: Export Target Selection
    target = select_export_target(config)
    
    if not target:
        # User cancelled or no targets available
        return
    
    print(f"\n✓ Selected target: {target['name']}")
    
    # Validation: Check if platform storage defaults are configured
    if 'platform_storage_defaults' not in target['config']:
        print("\n" + "=" * 60)
        print("✗ PLATFORM STORAGE DEFAULTS NOT CONFIGURED")
        print("=" * 60)
        print("\nYou must configure platform storage defaults before creating a migration.")
        print("\nPlease select 'Configure Platform Storage Defaults' from the main menu.")
        input("\nPress Enter to continue...")
        return
    
    # Phase 3: Check for previous configurations
    previous_config = check_previous_configuration(config, target['name'])
    
    if previous_config:
        use_previous = offer_previous_configuration(config, target['name'], previous_config)
        if use_previous:
            # User chose to use/modify previous configuration
            result = use_previous_configuration_workflow(config, target, previous_config)
            if result:
                # Configuration selected, save and generate script
                save_migration_configuration(config, target['name'], result)
                print(f"\n✓ Configuration saved to migration history")
                # TODO: Generate script here
                print("\n" + "=" * 60)
                print("NEXT: SCRIPT GENERATION")
                print("=" * 60)
                print("\nComing soon: Generating migration script...")
                input("\nPress Enter to continue...")
            return
    
    # Step 2.3a: Configure Filters (new configuration)
    filters = configure_filters(config, target['config'])
    
    if not filters:
        # User cancelled filter selection
        return
    
    print(f"\n✓ Filters configured")
    
    # Step 2.3b: Platform Selection (with filtered counts)
    platforms = select_platforms(config, filters)
    
    if not platforms:
        # User cancelled platform selection
        return
    
    print(f"\n✓ Selected {len(platforms)} platforms")
    
    # Step 2.4: Storage Location Assignment
    storage_assignments = assign_storage_locations(config, target, platforms)
    
    if not storage_assignments:
        # User cancelled storage assignment
        return
    
    print(f"\n✓ Storage locations assigned")
    
    # Phase 3: Save configuration to migration_history
    migration_config = {
        'filters': filters,
        'platforms': platforms,
        'storage_assignments': storage_assignments,
    }
    
    save_migration_configuration(config, target['name'], migration_config)
    print(f"\n✓ Configuration saved to migration history")
    
    # Phase 4 & 5: Script Generation & Validation
    from datetime import datetime
    
    # Step 4.1: Build file list
    file_list = build_file_list(config, target, migration_config)
    
    if not file_list['platforms'] and not file_list['windows_games']:
        print("\n✗ No games found to migrate!")
        input("\nPress Enter to continue...")
        return
    
    # Step 5.1: Pre-flight validation
    validation_report = validate_migration(file_list)
    
    # Step 5.2: Show summary report
    print("\n" + "=" * 60)
    print("MIGRATION SUMMARY")
    print("=" * 60)
    
    print(f"\nExport Target: {target['name']}")
    
    # Get default operation mode
    default_operation = target['config'].get('defaults', {}).get('operation', 'copy')
    
    # Prompt for operation mode
    operation_choices = [
        (f"Copy files (create independent copies - default)", 'copy'),
        ('Symlink files (requires network access to source)', 'symlink'),
    ]
    
    questions = [
        inquirer.List('operation',
                     message="Select operation mode",
                     choices=operation_choices,
                     default=default_operation
                     )
    ]
    
    answer = inquirer.prompt(questions)
    if not answer:
        print("\nCancelled.")
        input("\nPress Enter to continue...")
        return
    
    operation = answer['operation']
    print(f"\nOperation: {operation}")
    
    # Calculate totals
    total_platforms = len(file_list['platforms'])
    total_games = sum(p['game_count'] for p in file_list['platforms'].values())
    total_size = sum(p['total_size'] for p in file_list['platforms'].values())
    
    def format_size(bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.2f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.2f} PB"
    
    print(f"\nPlatforms: {total_platforms}")
    print(f"Total Games: {total_games:,}")
    print(f"Total Size: {format_size(total_size)}")
    
    # Show storage breakdown
    storage_breakdown = {}
    for platform_name, platform_data in file_list['platforms'].items():
        storage_path = platform_data['storage_path']
        if storage_path not in storage_breakdown:
            storage_breakdown[storage_path] = {'games': 0, 'size': 0}
        storage_breakdown[storage_path]['games'] += platform_data['game_count']
        storage_breakdown[storage_path]['size'] += platform_data['total_size']
    
    print("\nStorage Breakdown:")
    for storage_path, stats in sorted(storage_breakdown.items()):
        print(f"  {storage_path}")
        print(f"    {stats['games']:,} games, {format_size(stats['size'])}")
    
    if file_list['windows_games']:
        print(f"\n  Windows (manual install): {len(file_list['windows_games'])} games")
        print(f"    See: install_list_windows.txt")
    
    # Show active filters
    active_filters = [k.replace('include_', '').replace('force_', '').replace('_', ' ').title() 
                     for k, v in filters.items() if v and k != 'custom_fields']
    if active_filters:
        print("\nActive Filters:")
        for f in active_filters:
            print(f"  - {f}")
    
    print(f"\n✓ Ready to generate migration package!")
    
    # Confirm before generating
    if not inquirer.confirm("\nGenerate migration scripts?", default=True):
        print("\nCancelled.")
        input("\nPress Enter to continue...")
        return
    
    # Step 5.3: Generate distribution package
    print("\n" + "=" * 60)
    print("GENERATING MIGRATION PACKAGE")
    print("=" * 60)
    
    # Create distribution directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dist_dir_name = f"dist_{target['name']}_{timestamp}"
    dist_dir = PROJECT_ROOT / 'migrations' / dist_dir_name
    
    dist_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir = dist_dir / 'scripts'
    scripts_dir.mkdir(exist_ok=True)
    
    # Create __init__.py for scripts directory
    (scripts_dir / '__init__.py').write_text('')
    
    print(f"\nCreating: {dist_dir_name}/")
    
    # Generate per-platform scripts
    print("\nGenerating platform scripts...")
    script_names = []
    
    for platform_name, platform_data in sorted(file_list['platforms'].items()):
        script_name = generate_platform_script(platform_name, platform_data, operation, scripts_dir)
        script_names.append(script_name)
        print(f"  ✓ {script_name}")
    
    # Generate main migration runner
    print("\nGenerating migration runner...")
    runner_path = generate_migration_runner(dist_dir, target, file_list, operation, script_names)
    print(f"  ✓ ludis-migrate.py")
    
    # Generate manifest
    print("\nGenerating manifest...")
    manifest_path = generate_manifest(dist_dir, target, migration_config, file_list, operation, timestamp)
    print(f"  ✓ manifest.json")
    
    # Generate gamelists
    print("\nGenerating ES-DE gamelists...")
    gamelist_count = generate_gamelists(dist_dir, file_list)
    print(f"  ✓ {gamelist_count} gamelist files")
    
    # Generate Windows install list
    if file_list['windows_games']:
        print("\nGenerating Windows install list...")
        windows_list_path = generate_windows_install_list(dist_dir, file_list['windows_games'], timestamp)
        print(f"  ✓ install_list_windows.txt ({len(file_list['windows_games'])} games)")
    
    # Show success message
    print("\n" + "=" * 60)
    print("✓ MIGRATION PACKAGE GENERATED")
    print("=" * 60)
    
    print(f"\nLocation: {dist_dir}")
    print(f"\nGenerated files:")
    print(f"  - ludis-migrate.py (main runner)")
    print(f"  - manifest.json (complete migration record)")
    print(f"  - scripts/ ({len(script_names)} platform scripts)")
    print(f"  - gamelists/ ({gamelist_count} ES-DE gamelist files)")
    if file_list['windows_games']:
        print(f"  - install_list_windows.txt ({len(file_list['windows_games'])} games)")
    
    print(f"\nTo execute the migration:")
    print(f"  1. Copy the entire '{dist_dir_name}' folder to your target device")
    print(f"  2. Run: python3 ludis-migrate.py")
    print(f"  3. Follow the interactive prompts")
    
    input("\nPress Enter to continue...")


def configure_storage_defaults(config):
    """
    Configure default storage locations for platforms per export target.
    
    This is a one-time setup (or reconfiguration) that determines which
    platforms go to Internal SSD vs SD Card vs Custom Path by default.
    
    Flow:
    1. Select export target
    2. Get all platforms from inventory
    3. Configure storage paths (if needed)
    4. Select platforms for Internal SSD
    5. Select platforms for SD Card (from remaining)
    6. Show remaining platforms (will need custom paths during migration)
    7. Save configuration to config.yaml
    
    Args:
        config: Config object
    """
    print("\n" + "=" * 60)
    print("CONFIGURE PLATFORM STORAGE DEFAULTS")
    print("=" * 60)
    
    # Step 1: Select export target
    target = select_export_target(config)
    if not target:
        return
    
    target_name = target['name']
    target_config = target['config']
    
    print(f"\n✓ Configuring defaults for: {target_name}")
    
    # Step 2: Get all platforms from inventory
    print("\nScanning all platforms in your library...")
    
    master_inv = PROJECT_ROOT / 'LB_Exports' / 'master_inventory.csv'
    if not master_inv.exists():
        print(f"\n✗ Master inventory not found!")
        print(f"   Expected: {master_inv}")
        print("\nPlease run the pipeline first to generate master_inventory.csv")
        return
    
    scanner = InventoryScanner(master_inv)
    
    # Get all platforms (no filters, just get everything)
    all_platforms = []
    # Use utf-8-sig to automatically handle BOM if present
    with open(master_inv, 'r', encoding='utf-8-sig') as f:
        import csv
        reader = csv.DictReader(f)
        platforms_seen = set()
        for row in reader:
            platform = row.get('Platform', '').strip()
            if platform and platform not in platforms_seen:
                platforms_seen.add(platform)
                all_platforms.append(platform)
    
    all_platforms.sort()
    
    print(f"✓ Found {len(all_platforms)} platforms\n")
    
    # Step 3: Configure storage paths (if needed)
    storage_locations = target_config.get('storage_locations', {})
    internal_ssd = storage_locations.get('internal_ssd', {})
    sd_card = storage_locations.get('sd_card', {})
    
    internal_path = internal_ssd.get('path', '')
    sd_path = sd_card.get('path', '')
    
    needs_path_config = not internal_path or not sd_path
    
    if needs_path_config:
        print("\n" + "=" * 60)
        print("CONFIGURE STORAGE PATHS")
        print("=" * 60)
        print(f"\nYou need to configure storage paths for {target_name}.")
        print("These are the base paths where ROMs will be stored on your device.\n")
        
        if not internal_path:
            print("⚠ Internal SSD path not configured")
        if not sd_path:
            print("⚠ SD Card path not configured")
        
        print("\nExamples:")
        print("  Internal SSD: /home/deck/Emulation/roms")
        print("  SD Card: /run/media/mmcblk0p1/Emulation/roms")
        
        # Prompt for Internal SSD path
        if not internal_path:
            questions = [
                inquirer.Text('path',
                             message="Enter Internal SSD base path (where ROMs will be stored)",
                             validate=lambda _, x: len(x.strip()) > 0,
                             )
            ]
            answer = inquirer.prompt(questions)
            if not answer:
                print("\nCancelled.")
                return
            internal_path = answer['path'].strip()
        
        # Prompt for SD Card path
        if not sd_path:
            questions = [
                inquirer.Text('path',
                             message="Enter SD Card base path (where ROMs will be stored)",
                             validate=lambda _, x: len(x.strip()) > 0,
                             )
            ]
            answer = inquirer.prompt(questions)
            if not answer:
                print("\nCancelled.")
                return
            sd_path = answer['path'].strip()
        
        # Save paths to config.yaml
        import yaml
        config_file = PROJECT_ROOT / 'config.yaml'
        
        with open(config_file, 'r') as f:
            config_data = yaml.safe_load(f)
        
        if 'export_targets' not in config_data:
            config_data['export_targets'] = {}
        if target_name not in config_data['export_targets']:
            config_data['export_targets'][target_name] = {}
        if 'storage_locations' not in config_data['export_targets'][target_name]:
            config_data['export_targets'][target_name]['storage_locations'] = {}
        
        config_data['export_targets'][target_name]['storage_locations']['internal_ssd'] = {
            'path': internal_path,
            'label': 'Internal SSD'
        }
        config_data['export_targets'][target_name]['storage_locations']['sd_card'] = {
            'path': sd_path,
            'label': 'SD Card'
        }
        
        with open(config_file, 'w') as f:
            yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
        
        print(f"\n✓ Storage paths saved to config.yaml")
    
    print(f"\nStorage paths configured:")
    print(f"  Internal SSD: {internal_path}")
    print(f"  SD Card: {sd_path}")
    
    # Check if we want to update existing paths
    if not needs_path_config:
        if inquirer.confirm("\nUpdate these paths?", default=False):
            print("\n" + "=" * 60)
            print("UPDATE STORAGE PATHS")
            print("=" * 60)
            
            # Prompt for new Internal SSD path
            questions = [
                inquirer.Text('path',
                             message="Enter new Internal SSD base path",
                             default=internal_path,
                             validate=lambda _, x: len(x.strip()) > 0,
                             )
            ]
            answer = inquirer.prompt(questions)
            if not answer:
                print("\nCancelled.")
                return
            internal_path = answer['path'].strip()
            
            # Prompt for new SD Card path
            questions = [
                inquirer.Text('path',
                             message="Enter new SD Card base path",
                             default=sd_path,
                             validate=lambda _, x: len(x.strip()) > 0,
                             )
            ]
            answer = inquirer.prompt(questions)
            if not answer:
                print("\nCancelled.")
                return
            sd_path = answer['path'].strip()
            
            # Save updated paths to config.yaml
            import yaml
            config_file = PROJECT_ROOT / 'config.yaml'
            
            with open(config_file, 'r') as f:
                config_data = yaml.safe_load(f)
            
            config_data['export_targets'][target_name]['storage_locations']['internal_ssd']['path'] = internal_path
            config_data['export_targets'][target_name]['storage_locations']['sd_card']['path'] = sd_path
            
            with open(config_file, 'w') as f:
                yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
            
            print(f"\n✓ Storage paths updated in config.yaml")
            print(f"  Internal SSD: {internal_path}")
            print(f"  SD Card: {sd_path}")
    
    # Step 4: Select platforms for Internal SSD
    print("\n" + "=" * 60)
    print("STEP 1: SELECT PLATFORMS FOR INTERNAL SSD")
    print("=" * 60)
    print("Use Space to select/deselect, Enter to confirm")
    print()
    
    # Validate we have platforms
    if not all_platforms:
        print("\n✗ No platforms found in master inventory!")
        print("This shouldn't happen. Please check your master_inventory.csv")
        return
    
    try:
        questions = [
            inquirer.Checkbox('platforms',
                             message="Select platforms for Internal SSD",
                             choices=all_platforms,
                             default=[])
        ]
        
        answers = inquirer.prompt(questions)
        if not answers:
            print("\nCancelled.")
            return
        
        internal_platforms = answers['platforms']
    except Exception as e:
        print(f"\n✗ Error during platform selection: {e}")
        print(f"\nPlatforms available: {len(all_platforms)}")
        print(f"First few platforms: {all_platforms[:5] if len(all_platforms) >= 5 else all_platforms}")
        return
    
    # Step 5: Select platforms for SD Card (from remaining)
    remaining_platforms = [p for p in all_platforms if p not in internal_platforms]
    
    if remaining_platforms:
        print("\n" + "=" * 60)
        print("STEP 2: SELECT PLATFORMS FOR SD CARD")
        print("=" * 60)
        print("Use Space to select/deselect, Enter to confirm")
        print()
        
        try:
            questions = [
                inquirer.Checkbox('platforms',
                                 message="Select platforms for SD Card",
                                 choices=remaining_platforms,
                                 default=[])
            ]
            
            answers = inquirer.prompt(questions)
            if not answers:
                print("\nCancelled.")
                return
            
            sd_platforms = answers['platforms']
        except Exception as e:
            print(f"\n✗ Error during platform selection: {e}")
            print(f"\nRemaining platforms: {len(remaining_platforms)}")
            print(f"First few platforms: {remaining_platforms[:5] if len(remaining_platforms) >= 5 else remaining_platforms}")
            return
    else:
        sd_platforms = []
    
    # Step 6: Show remaining platforms (will need custom paths)
    custom_platforms = [p for p in remaining_platforms if p not in sd_platforms]
    
    print("\n" + "=" * 60)
    print("CONFIGURATION SUMMARY")
    print("=" * 60)
    
    print(f"\nInternal SSD: {len(internal_platforms)} platforms")
    for p in sorted(internal_platforms):
        print(f"  - {p}")
    
    print(f"\nSD Card: {len(sd_platforms)} platforms")
    for p in sorted(sd_platforms):
        print(f"  - {p}")
    
    if custom_platforms:
        print(f"\nCustom path (configured during migration): {len(custom_platforms)} platforms")
        for p in sorted(custom_platforms):
            print(f"  - {p}")
    
    # Step 7: Confirm and save
    if not inquirer.confirm("\nSave this configuration?", default=True):
        print("\nCancelled.")
        return
    
    # Build the configuration dictionary
    platform_storage_defaults = {}
    
    for platform in internal_platforms:
        platform_storage_defaults[platform] = "internal_ssd"
    
    for platform in sd_platforms:
        platform_storage_defaults[platform] = "sd_card"
    
    for platform in custom_platforms:
        platform_storage_defaults[platform] = "custom"
    
    # Save to config.yaml
    import yaml
    
    config_file = PROJECT_ROOT / 'config.yaml'
    
    # Load existing config
    with open(config_file, 'r') as f:
        config_data = yaml.safe_load(f)
    
    # Update the configuration
    if 'export_targets' not in config_data:
        config_data['export_targets'] = {}
    
    if target_name not in config_data['export_targets']:
        config_data['export_targets'][target_name] = {}
    
    config_data['export_targets'][target_name]['platform_storage_defaults'] = platform_storage_defaults
    
    # Write back to config.yaml
    with open(config_file, 'w') as f:
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n✓ Defaults saved to config.yaml for {target_name}")
    print(f"\n✓ Configuration complete!")
    print(f"\nThe 'Create Migration Script' option is now available in the main menu.")
    print(f"You can reconfigure these defaults anytime from the menu.")


def main():
    """Test the migration builder"""
    print("This module should be run through ludis.py")
    print("Run: python3 ludis.py")


if __name__ == "__main__":
    main()

