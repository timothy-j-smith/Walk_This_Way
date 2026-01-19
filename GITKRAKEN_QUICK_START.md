# GitKraken CLI - Quick Start Guide
**Date:** January 17, 2026  
**Time:** 19:03 PST  
**Purpose:** Correct commands to try GitKraken's hidden features

---

## ⚠️ COMMON ERRORS & FIXES

### Error 1: "please add at least 1 repository path/url to the workspace"

**Problem:** Workspace creation requires repository paths.

**Solution:**
```bash
# Must provide repository path with --add-repos flag
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
gk workspace create "Walk_This_Way_Test" --add-repos "$(pwd)"
```

**What `$(pwd)` does:**  
Returns current directory path. Equivalent to manually typing the full path.

---

### Error 2: "no repository found in directory"

**Problem:** `gk ai commit` must be run from within a git repository directory.

**Solution:**
```bash
# First, navigate to your git repository:
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"

# Stage your changes:
git add .

# Then run AI commit:
gk ai commit
```

**Important:**  
- `gk ai commit` reads your **staged changes** (files you've added with `git add`)
- Must be in directory with `.git` folder
- If you're in home directory (`~`), navigate to project first

---

## ✅ CORRECT COMMANDS TO TRY

### 1. Create a Workspace (Correct Way)

```bash
# Navigate to your project:
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"

# Create workspace with current directory:
gk workspace create "Walk_This_Way_Test" --add-repos "$(pwd)"

# Verify it was created:
gk workspace list
```

---

### 2. Try AI Commit (Correct Way)

```bash
# Navigate to your git repository:
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"

# Make a small change to a file (edit and save)

# Stage your changes:
git add .

# Now AI can analyze and generate commit message:
gk ai commit
```

---

### 3. View Commit Graph

```bash
# Navigate to your git repository:
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"

# View graph in terminal:
gk graph

# Or launch GitKraken Desktop:
gk graph --gitkraken
```

---

### 4. Start a Work Item

```bash
# Navigate to your git repository:
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"

# Start a work item:
gk work start "Test_Work_Item"

# Make some changes...
git add .
gk ai commit

# End the work item:
gk work end "Test_Work_Item"
```

---

## 🎯 WHY THESE COMMANDS FAILED

1. **Workspace creation:** Requires `--add-repos` flag with repository path(s)
2. **AI commit:** Must be in git repository directory (not home directory)
3. **AI commit:** Must stage changes first with `git add .`

---

## 💡 PRO TIP: Check Current Directory

If you're not sure where you are:

```bash
# Show current directory:
pwd

# Check if you're in a git repository:
git rev-parse --show-toplevel 2>/dev/null && echo "✅ In git repo" || echo "❌ Not in git repo"
```

---

## 📝 FILE HEADER FORMAT (For Future Reference)

All files I create should include:
```markdown
# Title
**Date:** January 17, 2026  
**Time:** 19:03 PST  
**Purpose:** Description
```

**Getting current time:**
```bash
date "+%Y-%m-%d %H:%M %Z"
```

---

**Last Updated:** January 17, 2026 19:03 PST
