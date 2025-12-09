#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch converter: Convert all Markdown files to Confluence format

This script automatically converts all standard Markdown documentation files
to Confluence Storage Format.

Usage:
    python convert_all_to_confluence.py
"""

import os
import subprocess
import sys
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except (AttributeError, TypeError):
        pass  # Already wrapped or not applicable

# List of Markdown files to convert
MARKDOWN_FILES = [
    'PROJECT_SUMMARY.md',
    'TOOL_ANALYSIS_AND_ALERTING.md',
    'ARCHITECTURE_DESIGN.md',
    'IMPLEMENTATION_ROADMAP.md',
    'PROJECT_DOCUMENTATION.md',
    'REQUIREMENTS_DOCUMENT.md',
]


def convert_file(input_file, output_file=None):
    """Convert a single file using the converter script"""
    script_path = 'markdown_to_confluence.py'
    
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found!")
        return False
    
    if output_file:
        cmd = [sys.executable, script_path, input_file, output_file]
    else:
        cmd = [sys.executable, script_path, input_file]
    
    try:
        # Set UTF-8 encoding for subprocess output
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print(f"Error converting {input_file}:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    print("=" * 60)
    print("Markdown to Confluence Batch Converter")
    print("=" * 60)
    print()
    
    converted = 0
    failed = 0
    
    for md_file in MARKDOWN_FILES:
        if os.path.exists(md_file):
            print(f"Converting {md_file}...")
            if convert_file(md_file):
                converted += 1
                print()
            else:
                failed += 1
                print()
        else:
            print(f"[SKIP] Skipping {md_file} (file not found)")
            print()
    
    print("=" * 60)
    print(f"Conversion complete!")
    print(f"  [OK] Successfully converted: {converted} files")
    if failed > 0:
        print(f"  [ERROR] Failed: {failed} files")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Find the *_CONFLUENCE.txt files in this directory")
    print("2. Open each file and copy the content")
    print("3. In Confluence, click Edit on your page")
    print("4. Press Ctrl+Shift+V to paste as plain text")
    print("5. Click Save")


if __name__ == '__main__':
    main()

