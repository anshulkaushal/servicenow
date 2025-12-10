#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch converter: Convert all Markdown files to Word format

This script automatically converts all standard Markdown documentation files
to Word (.docx) format for easy upload to Confluence.

Requirements:
    pip install python-docx markdown

Usage:
    python convert_all_to_word.py
"""

import os
import sys
import io

# Don't wrap stdout here - let each module handle its own encoding
# This prevents conflicts when importing other modules

# List of Markdown files to convert
MARKDOWN_FILES = [
    'PROJECT_SUMMARY.md',
    'TOOL_ANALYSIS_AND_ALERTING.md',
    'ARCHITECTURE_DESIGN.md',
    'IMPLEMENTATION_ROADMAP.md',
    'PROJECT_DOCUMENTATION.md',
    'REQUIREMENTS_DOCUMENT.md',
]


def convert_file(input_file):
    """Convert a single file using the converter script"""
    script_path = 'markdown_to_word.py'
    
    if not os.path.exists(script_path):
        try:
            print(f"Error: {script_path} not found!", file=sys.stderr)
        except:
            pass
        return False
    
    # Generate output filename
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.docx"
    
    # Import and use the converter directly
    try:
        # Temporarily suppress stdout from the converter
        import contextlib
        from io import StringIO
        
        with contextlib.redirect_stdout(StringIO()):
            from markdown_to_word import convert_markdown_to_word
            convert_markdown_to_word(input_file, output_file)
        
        # Print success message to our stdout
        try:
            print(f"  [OK] Created {output_file}")
        except (ValueError, OSError):
            # If stdout is closed, try to restore it
            sys.stdout = sys.__stdout__
            print(f"  [OK] Created {output_file}")
        return True
    except ImportError as e:
        try:
            print(f"Error: Could not import converter: {e}", file=sys.stderr)
        except:
            pass
        return False
    except Exception as e:
        try:
            print(f"Error converting {input_file}: {e}", file=sys.stderr)
        except:
            pass
        return False


def safe_print(*args, **kwargs):
    """Safely print, handling closed stdout"""
    try:
        print(*args, **kwargs)
    except (ValueError, OSError):
        # Restore stdout if it was closed
        sys.stdout = sys.__stdout__
        print(*args, **kwargs)


def main():
    # Check for required packages
    try:
        import docx
        import markdown
    except ImportError:
        safe_print("Error: Required packages not installed!")
        safe_print("Please install them with:")
        safe_print("  pip install python-docx markdown")
        safe_print()
        sys.exit(1)
    
    safe_print("=" * 60)
    safe_print("Markdown to Word Batch Converter")
    safe_print("=" * 60)
    safe_print()
    
    converted = 0
    failed = 0
    skipped = 0
    
    for md_file in MARKDOWN_FILES:
        if os.path.exists(md_file):
            safe_print(f"Converting {md_file}...")
            try:
                if convert_file(md_file):
                    converted += 1
                else:
                    failed += 1
            except Exception as e:
                try:
                    print(f"Error: {e}", file=sys.stderr)
                except:
                    pass
                failed += 1
            safe_print()
        else:
            safe_print(f"[SKIP] Skipping {md_file} (file not found)")
            skipped += 1
            safe_print()
    
    safe_print("=" * 60)
    safe_print(f"Conversion complete!")
    safe_print(f"  [OK] Successfully converted: {converted} files")
    if failed > 0:
        safe_print(f"  [ERROR] Failed: {failed} files")
    if skipped > 0:
        safe_print(f"  [SKIP] Skipped: {skipped} files")
    safe_print("=" * 60)
    safe_print()
    safe_print("Next steps:")
    safe_print("1. Review the .docx files in this directory")
    safe_print("2. In Confluence, click 'Create' → 'Import Word Document'")
    safe_print("3. Or drag and drop the .docx files into Confluence")
    safe_print("4. Confluence will automatically convert them")


if __name__ == '__main__':
    main()

