# Markdown to Word Converter

## Overview

This converter converts your Markdown documentation files to Word (.docx) format, which you can then upload directly to Confluence. Confluence has built-in support for importing Word documents and will automatically convert them.

## Quick Start

### Step 1: Install Requirements

```bash
pip install python-docx markdown
```

### Step 2: Convert Files

```bash
# Convert a single file
python markdown_to_word.py PROJECT_SUMMARY.md

# Or convert all files at once
python convert_all_to_word.py
```

This creates `.docx` files that you can upload to Confluence.

### Step 3: Upload to Confluence

1. **Method 1: Import Word Document**
   - In Confluence, click **"Create"** → **"Import Word Document"**
   - Select your `.docx` file
   - Confluence will convert it automatically

2. **Method 2: Drag and Drop**
   - Simply drag and drop the `.docx` file into Confluence
   - Confluence will prompt you to import it

3. **Method 3: Attach and Convert**
   - Attach the `.docx` file to a page
   - Confluence may offer to convert it to a page

## Advantages of Word Format

✅ **No formatting issues** - Word format is well-supported by Confluence  
✅ **Easy upload** - Just drag and drop or use import  
✅ **Automatic conversion** - Confluence handles the conversion  
✅ **Preserves formatting** - Headers, lists, tables all work  
✅ **No manual pasting** - Upload once and done  

## Files Created

After conversion, you'll have:
- `PROJECT_SUMMARY.docx`
- `TOOL_ANALYSIS_AND_ALERTING.docx`
- `ARCHITECTURE_DESIGN.docx`
- `IMPLEMENTATION_ROADMAP.docx`
- `PROJECT_DOCUMENTATION.docx`
- `REQUIREMENTS_DOCUMENT.docx`

## Usage Examples

### Convert Single File
```bash
python markdown_to_word.py PROJECT_SUMMARY.md
# Creates: PROJECT_SUMMARY.docx
```

### Convert with Custom Output Name
```bash
python markdown_to_word.py PROJECT_SUMMARY.md MyProject.docx
```

### Convert All Files
```bash
python convert_all_to_word.py
```

## What Gets Converted

| Markdown | Word Format |
|----------|-------------|
| `# Header` | Heading 1 |
| `## Header` | Heading 2 |
| `**bold**` | Bold text |
| `` `code` `` | Monospace font |
| `- List item` | Bullet list |
| `1. Item` | Numbered list |
| Tables | Word tables |
| Code blocks | Formatted code blocks |

## Troubleshooting

### Issue: "python-docx not installed"
**Solution:**
```bash
pip install python-docx markdown
```

### Issue: "markdown not installed"
**Solution:**
```bash
pip install markdown
```

### Issue: Word file looks wrong
**Solution:**
- Open the `.docx` file in Microsoft Word
- Review and adjust formatting if needed
- Save and upload to Confluence

### Issue: Confluence import fails
**Solution:**
- Make sure the file is a valid `.docx` file
- Try opening it in Word first to verify it's valid
- Check Confluence permissions
- Try a different browser

## Tips

1. **Review First:** Open the `.docx` file in Word before uploading to check formatting
2. **One at a Time:** Upload files one at a time for better control
3. **Backup:** Keep your original `.md` files as source of truth
4. **Update:** When you update `.md` files, re-run the converter

## Comparison: Word vs Storage Format

| Feature | Word Format | Storage Format |
|---------|-------------|----------------|
| Upload Method | Drag & drop | Copy-paste in Markup view |
| Ease of Use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Formatting | Automatic | Manual (Markup view) |
| Confluence Support | Built-in | Requires Markup view |
| Best For | Quick upload | Advanced users |

## Next Steps

1. Install requirements: `pip install python-docx markdown`
2. Convert files: `python convert_all_to_word.py`
3. Review `.docx` files in Word
4. Upload to Confluence using import feature
5. Done! 🎉

