# Quick Start: Upload Markdown to Confluence

## 🎯 EASIEST METHOD: Convert to Word Format (Recommended!)

**Want to avoid all the formatting issues?** Convert to Word format instead!

```bash
# Install requirements (one time)
pip install python-docx markdown

# Convert all files to Word
python convert_all_to_word.py
```

Then simply **drag and drop** the `.docx` files into Confluence! See `README_WORD_CONVERTER.md` for details.

---

## ⚡ Alternative: Markdown to Confluence Format (3 Steps)

### Step 1: Convert Markdown to Confluence Format

```bash
# Convert a single file
python markdown_to_confluence.py PROJECT_SUMMARY.md

# Or convert all files at once
python convert_all_to_confluence.py
```

This creates `*_CONFLUENCE.txt` files ready for Confluence.

### Step 2: Copy Content
- Open the `*_CONFLUENCE.txt` file (e.g., `PROJECT_SUMMARY_CONFLUENCE.txt`)
- Select All (Ctrl+A / Cmd+A)
- Copy (Ctrl+C / Cmd+C)

### Step 3: Paste in Confluence (CRITICAL - Read Carefully!)

**You MUST paste in Markup/Storage Format view, NOT Rich Text Editor!**

1. Go to your Confluence page
2. Click **Edit**
3. **IMPORTANT:** Click the **"..." menu** (three dots) in the editor toolbar
4. Select **"Markup"** or **"Storage Format"** or **"Wiki Markup"**
   - This switches to the markup editor where Storage Format works
5. **Paste your content** (Ctrl+V) into the markup editor
6. Click **Save**

**Why?** The Rich Text Editor doesn't understand `h1.`, `h2.` syntax. You need the Markup view!

---

## 🎯 That's It!

The content should now display with proper formatting (headings, panels, tables, etc.).

---

## 📋 What Files to Use

### ✅ Use These (Standard Markdown - Edit These)
- `PROJECT_SUMMARY.md`
- `TOOL_ANALYSIS_AND_ALERTING.md`
- `ARCHITECTURE_DESIGN.md`
- `IMPLEMENTATION_ROADMAP.md`

### ✅ Converted Files (Copy These to Confluence)
- `PROJECT_SUMMARY_CONFLUENCE.txt` ← After running converter
- `TOOL_ANALYSIS_AND_ALERTING_CONFLUENCE.txt` ← After running converter
- `ARCHITECTURE_DESIGN_CONFLUENCE.txt` ← After running converter
- `IMPLEMENTATION_ROADMAP_CONFLUENCE.txt` ← After running converter

---

## ❌ If Headers Show as Plain Text (Like "h2. Header")

**This happens when you paste into Rich Text Editor instead of Markup view!**

### Fix:
1. In Confluence editor, click the **"..." menu** (three dots)
2. Select **"Markup"** or **"Storage Format"** or **"Wiki Markup"**
3. **Delete the content** that's showing as plain text
4. **Paste the content again** in the Markup view
5. Click **Save**

### Alternative: Manual Formatting
If Markup view doesn't work:
1. Use the **original `.md` files** (not converted)
2. Paste into Confluence Rich Text Editor
3. Select each header line
4. Use the formatting toolbar to set as Heading 1, Heading 2, etc.
5. Or use keyboard shortcuts: **Ctrl+1** for H1, **Ctrl+2** for H2, etc.

---

## 🔧 If Python Converter Doesn't Work

1. Make sure Python 3.6+ is installed: `python --version`
2. Try `python3` instead of `python`
3. See `HOW_TO_UPLOAD_TO_CONFLUENCE.md` for detailed troubleshooting

---

## 📝 Need More Help?

- **Detailed Instructions:** See `HOW_TO_UPLOAD_TO_CONFLUENCE.md`
- **Converter Docs:** See `README_CONVERTER.md`

