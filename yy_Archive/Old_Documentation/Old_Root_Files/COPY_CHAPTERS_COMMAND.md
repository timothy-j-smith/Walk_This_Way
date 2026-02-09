# Copy Chapters Command

## Quick Command to Copy All 34 Chapters

Use this terminal command to create a draft copy of all your approved chapters:

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing" && mkdir -p Draft_Copy && cp -r Approved_Chapters/* Draft_Copy/
```

## What This Command Does:
1. `cd` - Navigate to your Original Writing directory
2. `mkdir -p Draft_Copy` - Create a Draft_Copy folder (if it doesn't exist)
3. `cp -r Approved_Chapters/* Draft_Copy/` - Copy all contents from Approved_Chapters to Draft_Copy

## Alternative Commands:

### Copy with timestamp:
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing" && mkdir -p "Draft_Copy_$(date +%Y%m%d_%H%M)" && cp -r Approved_Chapters/* "Draft_Copy_$(date +%Y%m%d_%H%M)/"
```

### Copy specific act only:
```bash
# Copy only Act I
cp -r Approved_Chapters/Act_I/ Draft_Copy/

# Copy only Act II
cp -r Approved_Chapters/Act_II/ Draft_Copy/

# Copy only Act III
cp -r Approved_Chapters/Act_III/ Draft_Copy/
```

### Copy with confirmation:
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing" && mkdir -p Draft_Copy && cp -rv Approved_Chapters/* Draft_Copy/
```
(The `-v` flag shows what files are being copied)

## Usage:
1. Open Terminal
2. Copy and paste the command above
3. Press Enter
4. Your draft copy will be created in the Draft_Copy folder

---
*Created: $(date)*
