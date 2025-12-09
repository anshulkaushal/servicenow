# Troubleshooting Header Issues in Confluence

## Issue: Headers Not Rendering in Confluence

If headers are showing as plain text instead of formatted headings in Confluence, try these solutions:

## Solution 1: Verify Paste Method

**Correct Method:**
1. Copy the converted content from `*_CONFLUENCE.txt` file
2. In Confluence, click **Edit**
3. Press **Ctrl+Shift+V** (paste as plain text)
4. Click **Save**

**Wrong Method:**
- Don't use regular paste (Ctrl+V) - this may paste as formatted text
- Don't paste from Word or other rich text editors

## Solution 2: Use Markup View

1. In Confluence editor, click the **"..." menu** (three dots)
2. Select **"Markup"** or **"Storage Format"**
3. Paste the content directly there
4. Click **Save**

## Solution 3: Verify Header Format

Headers should look like this in the converted file:
```
h1. Main Title
h2. Section Title
h3. Subsection Title
```

**NOT like this:**
```
# Main Title
## Section Title
```

## Solution 4: Manual Header Creation

If automatic conversion isn't working:

1. In Confluence editor, type your header text
2. Select the text
3. Use the formatting toolbar to set heading level
4. Or use keyboard shortcuts:
   - Ctrl+1 for H1
   - Ctrl+2 for H2
   - Ctrl+3 for H3
   - etc.

## Solution 5: Check Confluence Version

Some older Confluence versions may have issues with Storage Format. Try:
- Updating Confluence
- Using the Rich Text Editor instead
- Contacting your Confluence administrator

## Solution 6: Alternative - Use Rich Text Format

If Storage Format isn't working, you can:
1. Copy from the original `.md` file
2. Paste into a Markdown-to-HTML converter online
3. Copy the HTML
4. In Confluence, use "Insert" → "Markup" → "HTML"

## Testing Your Conversion

Run this to test if headers are converting correctly:

```bash
python test_header_conversion.py
```

If all tests pass, the conversion is working. The issue is likely with how you're pasting into Confluence.

## Common Issues

### Issue: Headers show as `h1. Text` instead of formatted
**Cause:** Not using plain text paste
**Fix:** Use Ctrl+Shift+V or paste in Markup view

### Issue: Some headers convert, others don't
**Cause:** Headers without space after `#` (like `#Header`)
**Fix:** Ensure all headers have space: `# Header` not `#Header`

### Issue: Headers with numbers not working
**Cause:** Usually a paste issue
**Fix:** Try Solution 2 (Markup view)

## Still Having Issues?

1. Check the converted file - do headers look like `h1.`, `h2.`, etc.?
2. Try pasting just one header to test
3. Check Confluence permissions - you may need edit rights
4. Try a different browser
5. Clear browser cache

## Quick Test

1. Create a simple test file `test.md`:
   ```markdown
   # Test Header
   ## Test Subheader
   ```

2. Convert it:
   ```bash
   python markdown_to_confluence.py test.md test_output.txt
   ```

3. Check `test_output.txt` - should show:
   ```
   h1. Test Header
   h2. Test Subheader
   ```

4. If it shows correctly, paste into Confluence using Ctrl+Shift+V

