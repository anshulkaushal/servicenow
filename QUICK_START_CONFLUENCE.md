# Quick Start: Upload Markdown to Confluence

## ⚡ Fast Method (3 Steps)

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

### Step 3: Paste in Confluence
1. Go to your Confluence page
2. Click **Edit**
3. **IMPORTANT:** Press **Ctrl+Shift+V** (Windows) or **Cmd+Shift+V** (Mac)
   - This pastes as plain text and Confluence will render the formatting
4. Click **Save**

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

## ❌ If It's Still Showing as Plain Text

Try this:
1. In Confluence editor, click the **"..." menu** (three dots)
2. Select **"Markup"** or **"Storage Format"**
3. Paste the content there
4. Click **Save**

---

## 🔧 If Python Converter Doesn't Work

1. Make sure Python 3.6+ is installed: `python --version`
2. Try `python3` instead of `python`
3. See `HOW_TO_UPLOAD_TO_CONFLUENCE.md` for detailed troubleshooting

---

## 📝 Need More Help?

- **Detailed Instructions:** See `HOW_TO_UPLOAD_TO_CONFLUENCE.md`
- **Converter Docs:** See `README_CONVERTER.md`

