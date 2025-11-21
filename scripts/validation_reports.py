#!/usr/bin/env python3
"""
Validation Reports Generator
=============================

Generates validation reports after master inventory build to help users
identify potential issues like multi-disc games, duplicate regions, etc.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict
from typing import List, Dict, Tuple

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def detect_multi_disc(title: str, filename: str) -> Tuple[bool, str]:
    """
    Detect if a game is part of a multi-disc set.
    
    Returns:
        (is_multi_disc, disc_pattern)
    """
    # Patterns for disc indicators
    disc_patterns = [
        r'\(Disc\s+\d+\)',
        r'\(Disk\s+\d+\)',
        r'\(CD\s+\d+\)',
        r'\(DVD\s+\d+\)',
        r'Disc\s+\d+',
        r'Disk\s+\d+',
        r'CD\s+\d+',
        r'DVD\s+\d+',
    ]
    
    combined = f"{title} {filename}"
    
    for pattern in disc_patterns:
        if re.search(pattern, combined, re.IGNORECASE):
            return (True, "MULTI_DISC")
    
    return (False, "")


def detect_bin_cue_pair(filename: str) -> bool:
    """Check if filename is a .bin or .cue file (likely paired)."""
    return filename.lower().endswith(('.bin', '.cue'))


def detect_region_variant(title: str) -> List[str]:
    """
    Extract region indicators from title.
    
    Returns list of regions found (USA, Europe, Japan, etc.)
    """
    regions = []
    region_patterns = {
        'USA': r'\(USA\)',
        'Europe': r'\(Europe\)',
        'Japan': r'\(Japan\)',
        'World': r'\(World\)',
        'Korea': r'\(Korea\)',
        'Asia': r'\(Asia\)',
    }
    
    for region_name, pattern in region_patterns.items():
        if re.search(pattern, title, re.IGNORECASE):
            regions.append(region_name)
    
    return regions


def normalize_title_for_grouping(title: str) -> str:
    """
    Normalize title for grouping similar games.
    Removes region indicators, disc numbers, etc.
    """
    # Remove common patterns
    normalized = title
    
    # Remove disc/cd/dvd indicators
    normalized = re.sub(r'\s*\(Dis[ck]\s+\d+\)', '', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\s*Dis[ck]\s+\d+', '', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\s*\(CD\s+\d+\)', '', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\s*\(DVD\s+\d+\)', '', normalized, flags=re.IGNORECASE)
    
    # Remove region indicators
    normalized = re.sub(r'\s*\([^)]*(?:USA|Europe|Japan|World|Korea|Asia)[^)]*\)', '', normalized, flags=re.IGNORECASE)
    
    # Remove version indicators
    normalized = re.sub(r'\s*\(v\d+\.?\d*\)', '', normalized, flags=re.IGNORECASE)
    normalized = re.sub(r'\s*\(Rev\s+\w+\)', '', normalized, flags=re.IGNORECASE)
    
    # Trim whitespace
    normalized = normalized.strip()
    
    return normalized


def generate_multi_file_report(inventory_path: Path, output_path: Path):
    """
    Analyze master inventory for potential multi-file games.
    
    Outputs a CSV with potential issues for manual review.
    """
    if not inventory_path.exists():
        print(f"⚠ Warning: {inventory_path} not found. Skipping multi-file report.")
        return None
    
    # Group games by normalized title and platform
    game_groups = defaultdict(list)
    
    with open(inventory_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            platform = row.get('Platform', '').strip()
            title = row.get('Title', '').strip()
            filename = row.get('Filename', '').strip()
            
            if not title or not platform:
                continue
            
            normalized_title = normalize_title_for_grouping(title)
            key = f"{platform}::{normalized_title}"
            
            game_groups[key].append({
                'platform': platform,
                'title': title,
                'filename': filename,
                'lbid': row.get('LBID', ''),
                'naspath': row.get('NASPath', ''),
            })
    
    # Analyze groups for potential issues
    issues = []
    
    for key, games in game_groups.items():
        if len(games) < 2:
            continue  # Single game, no issue
        
        platform = games[0]['platform']
        filenames = [g['filename'] for g in games]
        titles = [g['title'] for g in games]
        
        # Detect issue type
        issue_type = "UNKNOWN"
        suggestion = ""
        
        # Check for multi-disc
        has_disc_indicators = any(detect_multi_disc(g['title'], g['filename'])[0] for g in games)
        if has_disc_indicators:
            issue_type = "MULTI_DISC"
            suggestion = "Keep only Disc 1 (optional)"
        
        # Check for .bin/.cue pairs
        elif any(detect_bin_cue_pair(g['filename']) for g in games):
            if len(games) == 2 and any(f.endswith('.bin') for f in filenames) and any(f.endswith('.cue') for f in filenames):
                issue_type = "BIN_CUE_PAIR"
                suggestion = "Both files needed - no action required"
        
        # Check for region variants
        else:
            regions = []
            for g in games:
                regions.extend(detect_region_variant(g['title']))
            if regions:
                issue_type = "DIFFERENT_REGIONS"
                suggestion = f"Choose preferred region (found: {', '.join(set(regions))})"
        
        # Add issue
        issues.append({
            'Platform': platform,
            'TitleGroup': normalize_title_for_grouping(games[0]['title']),
            'FileCount': len(games),
            'Files': '; '.join(filenames[:5]),  # Limit to 5 for readability
            'Titles': '; '.join(titles[:5]),
            'Suggestion': suggestion,
            'IssueType': issue_type,
        })
    
    # Write report
    if issues:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        header = ['Platform', 'TitleGroup', 'FileCount', 'Files', 'Titles', 'IssueType', 'Suggestion']
        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=header, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(sorted(issues, key=lambda x: (x['Platform'], x['TitleGroup'])))
        
        print(f"✓ Generated multi-file game report: {output_path}")
        print(f"  Found {len(issues)} potential multi-file game groups")
        return output_path
    else:
        print("✓ No potential multi-file game issues detected")
        return None


def generate_all_validation_reports(config):
    """
    Generate all validation reports after master inventory build.
    
    Args:
        config: Config object from ludis.py
    """
    print("\n" + "=" * 60)
    print("GENERATING VALIDATION REPORTS")
    print("=" * 60)
    
    inventory_path = PROJECT_ROOT / config.paths.output_directory / "master_inventory.csv"
    validation_dir = PROJECT_ROOT / config.paths.output_directory / "validation"
    
    # Generate multi-file game report
    print("\n1. Analyzing for potential multi-file games...")
    multi_file_report = validation_dir / "potential_multi_file_games.csv"
    generate_multi_file_report(inventory_path, multi_file_report)
    
    print("\n" + "=" * 60)
    print("✓ VALIDATION REPORTS COMPLETE")
    print("=" * 60)
    print("\nReview these reports before continuing:")
    if multi_file_report and multi_file_report.exists():
        print(f"  • {multi_file_report}")
    print("\nUse ManualInclude/ManualExclude to control what gets migrated.")


if __name__ == "__main__":
    # Test standalone
    inventory = PROJECT_ROOT / "LB_Exports" / "master_inventory.csv"
    output = PROJECT_ROOT / "LB_Exports" / "validation" / "potential_multi_file_games.csv"
    
    generate_multi_file_report(inventory, output)

