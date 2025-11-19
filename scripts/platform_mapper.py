#!/usr/bin/env python3
"""
Platform Mapper - Maps LaunchBox platform names to ES-DE platform folders
========================================================================

This module handles the mapping between LaunchBox platform names and
ES-DE (EmulationStation Desktop Edition) platform folder names.

ES-DE uses specific folder names for each platform, which may differ from
LaunchBox's platform naming conventions.

Usage:
    from scripts.platform_mapper import PlatformMapper
    
    mapper = PlatformMapper()
    esde_folder = mapper.lb_to_esde("Nintendo Wii U")  # Returns "wiiu"
    lb_name = mapper.esde_to_lb("wiiu")                # Returns "Nintendo Wii U"
"""

import json
from pathlib import Path
from typing import Dict, Optional, List

# Project root is parent of scripts/ directory
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
ESDE_PLATFORMS_JSON = SCRIPT_DIR / "platforms-esde.json"


class PlatformMapper:
    """Maps between LaunchBox platform names and ES-DE folder names"""
    
    def __init__(self):
        """Initialize the platform mapper by loading ES-DE platform definitions"""
        self.esde_platforms = {}  # ES-DE name -> platform data
        self.lb_to_esde_map = {}  # LaunchBox name -> ES-DE folder
        self.esde_to_lb_map = {}  # ES-DE folder -> LaunchBox name
        
        self._load_esde_platforms()
        self._build_mappings()
    
    def _load_esde_platforms(self):
        """Load ES-DE platform definitions from JSON file"""
        if not ESDE_PLATFORMS_JSON.exists():
            raise FileNotFoundError(
                f"ES-DE platforms file not found: {ESDE_PLATFORMS_JSON}"
            )
        
        with open(ESDE_PLATFORMS_JSON, 'r', encoding='utf-8') as f:
            self.esde_platforms = json.load(f)
        
        print(f"✓ Loaded {len(self.esde_platforms)} ES-DE platform definitions")
    
    def _build_mappings(self):
        """
        Build bidirectional mappings between LaunchBox and ES-DE platform names.
        
        This uses manual mappings for known platforms and attempts fuzzy matching
        for others based on name similarity.
        """
        # Manual mappings: LaunchBox name -> ES-DE name (from platforms-esde.json keys)
        # These are platforms we know exist in both systems
        manual_mappings = {
            # Nintendo
            "Nintendo Entertainment System": "NES",
            "Super Nintendo Entertainment System": "SNES",
            "Nintendo 64": "Nintendo 64",
            "Nintendo GameCube": "GameCube",
            "Nintendo Wii": "Wii",
            "Nintendo Wii U": "Wii U",
            "Nintendo Switch": "Switch",
            "Nintendo Game Boy": "Game Boy",
            "Nintendo Game Boy Color": "Game Boy Color",
            "Nintendo Game Boy Advance": "Game Boy Advance",
            "Nintendo DS": "Nintendo DS",
            "Nintendo 3DS": "Nintendo 3DS",
            "Nintendo Virtual Boy": "Virtual Boy",
            "Nintendo Pokemon Mini": "PokéMini",
            "Nintendo Famicom Disk System": "FDS",
            "Nintendo Satellaview": "Satellaview",
            
            # Sega
            "Sega Genesis": "Genesis",
            "Sega Master System": "Master System",
            "Sega CD": "Sega CD",
            "Sega 32X": "Sega 32X",
            "Sega Saturn": "Saturn",
            "Sega Dreamcast": "Dreamcast",
            "Sega Game Gear": "Game Gear",
            "Sega SG-1000": "SG-1000",
            
            # Sony
            "Sony Playstation": "PlayStation",
            "Sony Playstation 2": "PlayStation 2",
            "Sony Playstation 3": "PlayStation 3",
            "Sony PSP": "PSP",
            "Sony Playstation Vita": "PS Vita",
            
            # Microsoft
            "Microsoft Xbox": "Xbox",
            "Microsoft Xbox 360": "Xbox 360",
            
            # NEC
            "NEC TurboGrafx-16": "TG-16",
            "NEC TurboGrafx-CD": "TG-CD",
            "PC Engine SuperGrafx": "SuperGrafx",
            
            # SNK
            "SNK Neo Geo AES": "Neo Geo",
            "SNK Neo Geo CD": "Neo Geo CD",
            "SNK Neo Geo Pocket Color": "Neo Geo Pocket Color",
            
            # Atari
            "Atari 2600": "Atari 2600",
            "Atari 5200": "Atari 5200",
            "Atari 7800": "Atari 7800",
            "Atari Jaguar": "Atari Jaguar",
            "Atari Lynx": "Atari Lynx",
            "Atari ST": "Atari ST",
            
            # Other Consoles
            "3DO Interactive Multiplayer": "3DO",
            "ColecoVision": "ColecoVision",
            "Mattel Intellivision": "Intellivision",
            "Magnavox Odyssey 2": "Odyssey 2",
            "Fairchild Channel F": "Channel F",
            "GCE Vectrex": "Vectrex",
            "Watara Supervision": "SuperVision",
            "Amstrad GX4000": "GX4000",
            
            # Computers
            "Commodore Amiga CD32": "AmigaCD32",
            "MS-DOS": "DOS",
            "Windows": "Windows",
            
            # Arcade
            "Arcade": "Arcade",
        }
        
        # Build LaunchBox -> ES-DE folder mapping
        for lb_name, esde_name in manual_mappings.items():
            if esde_name in self.esde_platforms:
                esde_folder = self.esde_platforms[esde_name]["folder"]
                self.lb_to_esde_map[lb_name] = esde_folder
                
                # Build reverse mapping (ES-DE folder -> LaunchBox name)
                # If multiple LB platforms map to same ES-DE folder, keep first
                if esde_folder not in self.esde_to_lb_map:
                    self.esde_to_lb_map[esde_folder] = lb_name
        
        print(f"✓ Built mappings for {len(self.lb_to_esde_map)} platforms")
    
    def lb_to_esde(self, lb_platform_name: str) -> Optional[str]:
        """
        Convert LaunchBox platform name to ES-DE folder name.
        
        Args:
            lb_platform_name: LaunchBox platform name (e.g., "Nintendo Wii U")
        
        Returns:
            ES-DE folder name (e.g., "wiiu") or None if not mapped
        """
        return self.lb_to_esde_map.get(lb_platform_name)
    
    def esde_to_lb(self, esde_folder: str) -> Optional[str]:
        """
        Convert ES-DE folder name to LaunchBox platform name.
        
        Args:
            esde_folder: ES-DE folder name (e.g., "wiiu")
        
        Returns:
            LaunchBox platform name (e.g., "Nintendo Wii U") or None if not mapped
        """
        return self.esde_to_lb_map.get(esde_folder)
    
    def get_esde_info(self, esde_name: str) -> Optional[Dict]:
        """
        Get full ES-DE platform information.
        
        Args:
            esde_name: ES-DE platform name (key from platforms-esde.json)
        
        Returns:
            Dictionary with 'folder' and 'description' keys, or None if not found
        """
        return self.esde_platforms.get(esde_name)
    
    def is_platform_supported(self, lb_platform_name: str) -> bool:
        """
        Check if a LaunchBox platform is supported by ES-DE.
        
        Args:
            lb_platform_name: LaunchBox platform name
        
        Returns:
            True if platform can be mapped to ES-DE, False otherwise
        """
        return lb_platform_name in self.lb_to_esde_map
    
    def get_supported_platforms(self) -> List[str]:
        """
        Get list of all supported LaunchBox platform names.
        
        Returns:
            List of LaunchBox platform names that can be mapped to ES-DE
        """
        return sorted(self.lb_to_esde_map.keys())
    
    def get_unsupported_platforms(self, lb_platforms: List[str]) -> List[str]:
        """
        Filter list of LaunchBox platforms to find unsupported ones.
        
        Args:
            lb_platforms: List of LaunchBox platform names
        
        Returns:
            List of platform names that are not supported by ES-DE
        """
        return [p for p in lb_platforms if not self.is_platform_supported(p)]
    
    def get_mapping_summary(self) -> Dict[str, int]:
        """
        Get summary statistics about platform mappings.
        
        Returns:
            Dictionary with counts of mapped platforms and ES-DE platforms
        """
        return {
            "total_esde_platforms": len(self.esde_platforms),
            "total_mapped_platforms": len(self.lb_to_esde_map),
            "total_esde_folders": len(self.esde_to_lb_map),
        }


def main():
    """Test the platform mapper"""
    print("=" * 60)
    print("PLATFORM MAPPER TEST")
    print("=" * 60)
    
    mapper = PlatformMapper()
    
    print("\n" + "-" * 60)
    print("MAPPING SUMMARY")
    print("-" * 60)
    summary = mapper.get_mapping_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    print("\n" + "-" * 60)
    print("TEST MAPPINGS")
    print("-" * 60)
    
    test_platforms = [
        "Nintendo Wii U",
        "Sony Playstation 3",
        "NEC TurboGrafx-16",
        "Arcade",
        "Unknown Platform",  # Should fail
    ]
    
    for platform in test_platforms:
        esde_folder = mapper.lb_to_esde(platform)
        if esde_folder:
            print(f"✓ {platform:40} → {esde_folder}")
            # Test reverse lookup
            reverse = mapper.esde_to_lb(esde_folder)
            if reverse != platform:
                print(f"  ⚠ Reverse lookup mismatch: {esde_folder} → {reverse}")
        else:
            print(f"✗ {platform:40} → (not mapped)")
    
    print("\n" + "-" * 60)
    print("SUPPORTED PLATFORMS")
    print("-" * 60)
    supported = mapper.get_supported_platforms()
    print(f"Total: {len(supported)} platforms")
    for i, platform in enumerate(supported[:10], 1):
        esde_folder = mapper.lb_to_esde(platform)
        print(f"{i:2}. {platform:40} → {esde_folder}")
    if len(supported) > 10:
        print(f"... and {len(supported) - 10} more")


if __name__ == "__main__":
    main()

