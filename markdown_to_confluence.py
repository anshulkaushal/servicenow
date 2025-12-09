#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown to Confluence Storage Format Converter

This script converts standard Markdown files to Confluence Storage Format
so they can be pasted directly into Confluence pages.

Usage:
    python markdown_to_confluence.py input.md output_confluence.txt
    python markdown_to_confluence.py PROJECT_SUMMARY.md PROJECT_SUMMARY_CONFLUENCE.txt
"""

import re
import sys
import os
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except (AttributeError, TypeError):
        pass  # Already wrapped or not applicable


def convert_headers(text):
    """Convert Markdown headers to Confluence headers"""
    lines = text.split('\n')
    result = []
    
    for line in lines:
        original_line = line
        stripped = line.lstrip()
        
        # Process from h6 to h1 (most specific first) to avoid conflicts
        # Match headers with required space after #
        if stripped.startswith('###### '):
            # h6: ###### Header -> h6. Header
            header_text = stripped[7:].strip()  # Remove '###### '
            # Remove trailing # if present
            header_text = header_text.rstrip('#').strip()
            result.append(f'h6. {header_text}')
        elif stripped.startswith('##### '):
            # h5: ##### Header -> h5. Header
            header_text = stripped[6:].strip()  # Remove '##### '
            header_text = header_text.rstrip('#').strip()
            result.append(f'h5. {header_text}')
        elif stripped.startswith('#### '):
            # h4: #### Header -> h4. Header
            header_text = stripped[5:].strip()  # Remove '#### '
            header_text = header_text.rstrip('#').strip()
            result.append(f'h4. {header_text}')
        elif stripped.startswith('### '):
            # h3: ### Header -> h3. Header
            header_text = stripped[4:].strip()  # Remove '### '
            header_text = header_text.rstrip('#').strip()
            result.append(f'h3. {header_text}')
        elif stripped.startswith('## '):
            # h2: ## Header -> h2. Header
            header_text = stripped[3:].strip()  # Remove '## '
            header_text = header_text.rstrip('#').strip()
            result.append(f'h2. {header_text}')
        elif stripped.startswith('# '):
            # h1: # Header -> h1. Header
            header_text = stripped[2:].strip()  # Remove '# '
            header_text = header_text.rstrip('#').strip()
            result.append(f'h1. {header_text}')
        else:
            # Not a header, keep as-is
            result.append(original_line)
    
    return '\n'.join(result)


def convert_bold(text):
    """Convert Markdown bold to Confluence bold"""
    # **text** -> *text*
    text = re.sub(r'\*\*(.+?)\*\*', r'*\1*', text)
    return text


def convert_italic(text):
    """Convert Markdown italic to Confluence italic"""
    # *text* (not bold) -> _text_
    # Need to be careful not to convert bold markers
    # This is a simple approach - may need refinement
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'_\1_', text)
    return text


def convert_code_blocks(text):
    """Convert Markdown code blocks to Confluence code blocks"""
    # ```language\ncode\n``` -> {code:language=...}\ncode\n{code}
    def replace_code_block(match):
        language = match.group(1) or 'text'
        code = match.group(2)
        return f'{{code:language={language}|collapse=false}}\n{code}\n{{code}}'
    
    text = re.sub(
        r'```(\w+)?\n(.*?)```',
        replace_code_block,
        text,
        flags=re.DOTALL
    )
    return text


def convert_inline_code(text):
    """Convert inline code to Confluence format"""
    # `code` -> {{code}}
    text = re.sub(r'`([^`]+)`', r'{{\1}}', text)
    return text


def convert_lists(text):
    """Convert Markdown lists to Confluence lists"""
    lines = text.split('\n')
    result = []
    in_list = False
    
    for line in lines:
        # Unordered lists: - item or * item -> * item
        if re.match(r'^[\-\*] ', line):
            if not in_list:
                in_list = True
            # Convert - to *
            line = re.sub(r'^[\-\*] ', '* ', line)
        # Ordered lists: 1. item -> # item
        elif re.match(r'^\d+\. ', line):
            if not in_list:
                in_list = True
            line = re.sub(r'^\d+\. ', '# ', line)
        else:
            if in_list and line.strip() == '':
                in_list = False
            elif in_list and not line.startswith(' ') and not line.startswith('\t'):
                in_list = False
        
        result.append(line)
    
    return '\n'.join(result)


def convert_tables(text):
    """Convert Markdown tables to Confluence tables"""
    lines = text.split('\n')
    result = []
    in_table = False
    
    for i, line in enumerate(lines):
        # Check if this is a table line
        if '|' in line and not line.strip().startswith('|---'):
            if not in_table:
                in_table = True
            
            # Convert table format
            # Markdown: | Header | -> Confluence: || Header ||
            # Remove alignment markers like |:---:|
            if i > 0 and lines[i-1].strip().startswith('|---'):
                continue  # Skip separator lines
            
            # Convert | to ||
            line = re.sub(r'\|', '||', line)
            # Remove leading/trailing || if needed
            line = line.strip()
            if line.startswith('||'):
                line = line[2:]  # Remove leading ||
            if line.endswith('||'):
                line = line[:-2]  # Remove trailing ||
            line = '||' + line + '||'
        else:
            if in_table:
                in_table = False
            # Skip separator lines
            if line.strip().startswith('|---'):
                continue
        
        result.append(line)
    
    return '\n'.join(result)


def convert_links(text):
    """Convert Markdown links to Confluence links"""
    # [text](url) -> [text|url]
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'[\1|\2]', text)
    return text


def convert_checkboxes(text):
    """Convert Markdown checkboxes to Confluence checkboxes"""
    # - [ ] -> ( )
    text = re.sub(r'^- \[ \]', r'* ( )', text, flags=re.MULTILINE)
    # - [x] -> (/) 
    text = re.sub(r'^- \[[xX]\]', r'* (/)', text, flags=re.MULTILINE)
    return text


def convert_horizontal_rules(text):
    """Convert horizontal rules"""
    # --- -> ----
    text = re.sub(r'^---$', '----', text, flags=re.MULTILINE)
    return text


def convert_blockquotes(text):
    """Convert blockquotes"""
    # > text -> {quote}text{quote}
    lines = text.split('\n')
    result = []
    in_quote = False
    
    for line in lines:
        if line.startswith('> '):
            if not in_quote:
                result.append('{quote}')
                in_quote = True
            result.append(line[2:])  # Remove '> '
        else:
            if in_quote:
                result.append('{quote}')
                in_quote = False
            result.append(line)
    
    if in_quote:
        result.append('{quote}')
    
    return '\n'.join(result)


def convert_markdown_to_confluence(markdown_text):
    """Main conversion function"""
    text = markdown_text
    
    # Order matters - do code blocks before inline code
    text = convert_code_blocks(text)
    text = convert_blockquotes(text)
    text = convert_checkboxes(text)
    text = convert_headers(text)
    text = convert_bold(text)
    text = convert_italic(text)
    text = convert_inline_code(text)
    text = convert_lists(text)
    text = convert_tables(text)
    text = convert_links(text)
    text = convert_horizontal_rules(text)
    
    return text


def main():
    if len(sys.argv) < 2:
        print("Usage: python markdown_to_confluence.py <input.md> [output.txt]")
        print("\nExample:")
        print("  python markdown_to_confluence.py PROJECT_SUMMARY.md")
        print("  python markdown_to_confluence.py PROJECT_SUMMARY.md output.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    
    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convert
    confluence_content = convert_markdown_to_confluence(markdown_content)
    
    # Determine output file
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Auto-generate output filename
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}_CONFLUENCE.txt"
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(confluence_content)
    
    # Use ASCII-safe characters for Windows compatibility
    print(f"[OK] Converted '{input_file}' to '{output_file}'")
    print(f"[OK] You can now copy the content from '{output_file}' and paste it into Confluence")
    print(f"\nTo paste in Confluence:")
    print(f"  1. Open '{output_file}'")
    print(f"  2. Copy all content (Ctrl+A, Ctrl+C)")
    print(f"  3. In Confluence, click Edit")
    print(f"  4. Press Ctrl+Shift+V to paste as plain text")
    print(f"  5. Click Save")


if __name__ == '__main__':
    main()

