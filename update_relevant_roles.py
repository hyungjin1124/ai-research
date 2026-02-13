#!/usr/bin/env python3
"""
Script to populate relevant_roles in insight-synthesis files based on AGENTS.md routing.

This script:
1. Parses AGENTS.md to build a reverse mapping: file_path -> [roles]
2. For each insight-synthesis .md file, updates the relevant_roles field
3. Preserves all other frontmatter and body content exactly
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict


def parse_agents_md(agents_path: str) -> Dict[str, List[str]]:
    """
    Parse AGENTS.md and build a reverse mapping: file_path -> [roles]

    Returns:
        Dict[file_path] -> List[role_names]
    """
    file_to_roles = defaultdict(set)

    with open(agents_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all agent roles and their sources
    # Pattern: ### {role_name}
    # Followed by primary_sources and secondary_sources sections

    role_pattern = r'### (\w+)\n'
    roles = re.findall(role_pattern, content)

    # For each role, find its primary_sources and secondary_sources
    for role in roles:
        # Skip if it's a heading like "역할 정의" or other non-agent sections
        if role not in ['frontend_agent', 'backend_agent', 'architecture_agent', 'planning_agent',
                        'pm_agent', 'qa_agent', 'data_agent', 'sales_agent']:
            continue

        # Find the section for this role
        role_section_pattern = rf'### {role}\n(.*?)(?=### |\Z)'
        match = re.search(role_section_pattern, content, re.DOTALL)

        if not match:
            continue

        section_text = match.group(1)

        # Extract file paths from backtick-quoted strings
        # Pattern: `path/to/file.md`
        file_pattern = r'`([Ii]nsights/[^`]+?\.md)`'
        files = re.findall(file_pattern, section_text)

        for file_path in files:
            # Normalize path (remove leading "Insights/" for consistency check later)
            # But keep the full path as extracted
            file_to_roles[file_path].add(role)

    # Convert sets to sorted lists
    result = {path: sorted(list(roles)) for path, roles in file_to_roles.items()}
    return result


def read_frontmatter_and_body(file_path: str) -> tuple:
    """
    Read a markdown file and split frontmatter from body.

    Returns:
        (frontmatter_dict, body_content_str)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file starts with ---
    if not content.startswith('---'):
        return {}, content

    # Find the closing --- delimiter
    lines = content.split('\n')
    closing_index = -1

    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            closing_index = i
            break

    if closing_index == -1:
        return {}, content

    # Extract frontmatter and body
    frontmatter_text = '\n'.join(lines[1:closing_index])
    body_text = '\n'.join(lines[closing_index + 1:])

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {file_path}: {e}")
        return {}, content

    return frontmatter, body_text


def write_frontmatter_and_body(file_path: str, frontmatter: dict, body: str):
    """
    Write frontmatter and body back to a markdown file.

    Uses yaml.dump with specific settings to preserve formatting.
    """
    # Dump frontmatter with specific settings
    frontmatter_text = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=1000
    )

    # Remove trailing newline from yaml.dump (it adds one)
    frontmatter_text = frontmatter_text.rstrip('\n')

    # Combine frontmatter and body
    content = f"---\n{frontmatter_text}\n---\n{body}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def is_template_file(file_path: str) -> bool:
    """Check if file is a template file."""
    return '_TEMPLATE' in file_path


def find_all_insight_files(insights_dir: str) -> List[str]:
    """Find all insight .md files (excluding _TEMPLATE files)."""
    insights_path = Path(insights_dir)

    md_files = []
    for md_file in insights_path.rglob('*.md'):
        if not is_template_file(str(md_file)):
            md_files.append(str(md_file))

    return sorted(md_files)


def normalize_path(path: str) -> str:
    """Normalize path for comparison (handle case sensitivity, backslashes, etc.)."""
    # Convert backslashes to forward slashes
    normalized = path.replace('\\', '/')
    # Make it case-insensitive for comparison
    return normalized.lower()


def main():
    repo_root = os.environ.get('VAULT_ROOT', os.path.dirname(os.path.abspath(__file__)))
    agents_file = os.path.join(repo_root, 'AGENTS.md')
    insights_dir = os.path.join(repo_root, 'Insights')

    # Step 1: Parse AGENTS.md
    print("Step 1: Parsing AGENTS.md...")
    file_to_roles = parse_agents_md(agents_file)

    print(f"\nReverse Mapping (File -> Roles):\n")
    print("=" * 100)
    for file_path in sorted(file_to_roles.keys()):
        roles = file_to_roles[file_path]
        print(f"{file_path}")
        print(f"  Roles: {', '.join(roles)}")
    print("=" * 100)

    # Step 2: Find all insight files
    print("\n\nStep 2: Finding all insight files...")
    insight_files = find_all_insight_files(insights_dir)
    print(f"Found {len(insight_files)} insight files")

    # Step 3: Process each insight file
    print("\n\nStep 3: Processing insight files...")
    print("=" * 100)

    updated_count = 0
    skipped_count = 0

    for insight_file in insight_files:
        # Get relative path from insights_dir
        rel_path = os.path.relpath(insight_file, repo_root)

        # Read the file
        frontmatter, body = read_frontmatter_and_body(insight_file)

        # Skip if not an insight-synthesis file
        if frontmatter.get('type') != 'insight-synthesis':
            print(f"SKIP: {rel_path} (not insight-synthesis)")
            skipped_count += 1
            continue

        # Find matching roles
        normalized_rel_path = normalize_path(rel_path)
        matching_roles = []

        # Try to find exact match or normalized match
        for agents_path, roles in file_to_roles.items():
            normalized_agents_path = normalize_path(agents_path)
            if normalized_agents_path == normalized_rel_path or normalized_agents_path.endswith(normalized_rel_path):
                matching_roles = roles
                break

        # Update relevant_roles
        old_roles = frontmatter.get('relevant_roles', [])
        frontmatter['relevant_roles'] = matching_roles

        # Write back
        write_frontmatter_and_body(insight_file, frontmatter, body)

        status = "UPDATE" if matching_roles else "EMPTY"
        print(f"{status}: {rel_path}")
        if matching_roles:
            print(f"       -> relevant_roles: {matching_roles}")

        updated_count += 1

    print("=" * 100)
    print(f"\nSummary:")
    print(f"  Updated: {updated_count}")
    print(f"  Skipped: {skipped_count}")


if __name__ == '__main__':
    main()
