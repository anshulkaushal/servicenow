# Solution: Headers Showing as Plain Text in Confluence

## Problem
When you paste the converted content, headers show as literal text:
```
h2. 4. Integration Details
```
Instead of being rendered as an actual heading.

## Root Cause
You're pasting into Confluence's **Rich Text Editor**, which doesn't understand Storage Format syntax (`h1.`, `h2.`, etc.). You need to paste into the **Markup/Storage Format view**.

## Solution: Use Markup View

### Step-by-Step:

1. **Open your converted file** (e.g., `PROJECT_SUMMARY_CONFLUENCE.txt`)
2. **Copy all content** (Ctrl+A, Ctrl+C)

3. **In Confluence:**
   - Click **Edit** on your page
   - Look for the **"..." menu** (three dots) in the editor toolbar
     - It might be in the top-right corner
     - Or in a toolbar menu
   - Click it and select one of these options:
     - **"Markup"**
     - **"Storage Format"**
     - **"Wiki Markup"**
     - **"View Source"** (some versions)

4. **You should now see a code/markup editor** (not the visual editor)

5. **Paste your content** (Ctrl+V) into this markup editor

6. **Click "Save"** or "Update"

7. **Headers should now render correctly!**

## Visual Guide

```
Confluence Editor
┌─────────────────────────────────────┐
│ [Edit] [Format] [...] ← Click here │
│                                     │
│ Rich Text Editor (WRONG)           │
│ h2. Header ← Shows as plain text   │
└─────────────────────────────────────┘

After clicking "..." → "Markup":
┌─────────────────────────────────────┐
│ [Save] [Cancel]                     │
│                                     │
│ Markup Editor (CORRECT)             │
│ h2. Header ← Will render correctly  │
└─────────────────────────────────────┘
```

## If You Can't Find Markup View

Some Confluence versions hide this option. Try:

1. **Check Confluence version:**
   - Go to your profile → About
   - Note the version

2. **Alternative methods:**
   - Try **Ctrl+Shift+M** (some versions)
   - Look for **"</>"** icon (code/markup button)
   - Check if there's a **"Switch to Markup"** option

3. **Contact your Confluence admin:**
   - They may need to enable Storage Format editing
   - Or provide access to the markup editor

## Alternative Solution: Manual Formatting

If Markup view isn't available or doesn't work:

1. **Use the original Markdown files** (`.md` files, not converted)
2. **Paste into Confluence Rich Text Editor**
3. **For each header:**
   - Select the header text
   - Use the formatting dropdown (usually shows "Paragraph")
   - Select "Heading 1", "Heading 2", etc.
   - Or use keyboard shortcuts:
     - **Ctrl+1** = Heading 1
     - **Ctrl+2** = Heading 2
     - **Ctrl+3** = Heading 3
     - etc.

## Quick Test

To verify Markup view works:

1. Create a test page
2. Click Edit → "..." → "Markup"
3. Paste this:
   ```
   h1. Test Header
   This is normal text.
   h2. Test Subheader
   More text here.
   ```
4. Click Save
5. If you see formatted headings, Markup view works!
6. If you still see "h1. Test Header" as plain text, Markup view isn't working

## Still Not Working?

1. **Check Confluence permissions** - you may need edit rights
2. **Try a different browser** - some browsers have issues
3. **Clear browser cache** - old cached editor might be interfering
4. **Check Confluence version** - older versions may not support Storage Format
5. **Use the manual formatting method** (Alternative Solution above)

## Summary

**The key is:** Storage Format (`h1.`, `h2.`) only works in **Markup/Storage Format view**, not in the Rich Text Editor. Always paste in Markup view!

