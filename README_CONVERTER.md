# Markdown to Confluence Converter

## Overview

This converter allows you to use standard Markdown files and automatically convert them to Confluence Storage Format for easy upload to Confluence.

## Quick Start

### Option 1: Convert a Single File

```bash
python markdown_to_confluence.py PROJECT_SUMMARY.md
```

This creates `PROJECT_SUMMARY_CONFLUENCE.txt` that you can copy-paste into Confluence.

### Option 2: Convert All Files at Once

```bash
python convert_all_to_confluence.py
```

This automatically converts all documentation files:
- `PROJECT_SUMMARY.md` → `PROJECT_SUMMARY_CONFLUENCE.txt`
- `TOOL_ANALYSIS_AND_ALERTING.md` → `TOOL_ANALYSIS_AND_ALERTING_CONFLUENCE.txt`
- `ARCHITECTURE_DESIGN.md` → `ARCHITECTURE_DESIGN_CONFLUENCE.txt`
- `IMPLEMENTATION_ROADMAP.md` → `IMPLEMENTATION_ROADMAP_CONFLUENCE.txt`
- And more...

## Requirements

- Python 3.6 or higher
- No additional packages required (uses only standard library)

## Usage

### Single File Conversion

```bash
# Basic usage (auto-generates output filename)
python markdown_to_confluence.py input.md

# Specify output file
python markdown_to_confluence.py input.md output.txt
```

### Batch Conversion

```bash
# Convert all documentation files
python convert_all_to_confluence.py
```

## What Gets Converted

| Markdown | Confluence Format |
|----------|-------------------|
| `# Header` | `h1. Header` |
| `## Header` | `h2. Header` |
| `**bold**` | `*bold*` |
| `` `code` `` | `{{code}}` |
| ` ```language` | `{code:language=...}` |
| `- [ ]` | `( )` |
| `- [x]` | `(/)` |
| `\|Header\|` | `\|\|Header\|\|` |
| `[text](url)` | `[text\|url]` |

## How to Use Converted Files

1. **Run the converter:**
   ```bash
   python markdown_to_confluence.py PROJECT_SUMMARY.md
   ```

2. **Open the output file:**
   - Open `PROJECT_SUMMARY_CONFLUENCE.txt` (or your output file)

3. **Copy the content:**
   - Select All (Ctrl+A / Cmd+A)
   - Copy (Ctrl+C / Cmd+C)

4. **Paste into Confluence:**
   - Go to your Confluence page
   - Click **Edit**
   - Press **Ctrl+Shift+V** (Windows) or **Cmd+Shift+V** (Mac)
   - This pastes as plain text and Confluence will render the formatting
   - Click **Save**

## Alternative: Paste in Markup View

If Ctrl+Shift+V doesn't work:

1. In Confluence editor, click the **"..." menu** (three dots)
2. Select **"Markup"** or **"Storage Format"**
3. Paste the content there
4. Click **Save**

## Troubleshooting

### Issue: Python not found
**Solution:** Make sure Python 3 is installed and in your PATH.

### Issue: File encoding errors
**Solution:** The script uses UTF-8 encoding. If you have encoding issues, ensure your Markdown files are saved as UTF-8.

### Issue: Tables not converting correctly
**Solution:** Make sure your Markdown tables have proper formatting with pipes (`|`).

### Issue: Code blocks not working
**Solution:** Ensure code blocks use triple backticks with optional language identifier:
````markdown
```python
code here
```
````

## Examples

### Convert Project Summary
```bash
python markdown_to_confluence.py PROJECT_SUMMARY.md PROJECT_SUMMARY_CONFLUENCE.txt
```

### Convert Architecture Design
```bash
python markdown_to_confluence.py ARCHITECTURE_DESIGN.md ARCHITECTURE_DESIGN_CONFLUENCE.txt
```

### Convert All Files
```bash
python convert_all_to_confluence.py
```

## Workflow Recommendation

1. **Edit Markdown files** (use standard Markdown syntax)
2. **Convert to Confluence format** when ready to publish
3. **Copy-paste into Confluence** using Ctrl+Shift+V
4. **Review and adjust** formatting in Confluence if needed

## Notes

- The converter preserves most Markdown formatting
- Some complex formatting may need manual adjustment
- Always review the converted content in Confluence
- Keep your original Markdown files as source of truth

## Support

If you encounter issues:
1. Check that your Markdown syntax is correct
2. Verify Python version (3.6+)
3. Review the conversion output for any obvious issues
4. Some edge cases may require manual adjustment

