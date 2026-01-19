# Terminal Status Check Commands

**Use these simple commands to check where you are, even if terminal text is spaced out:**

---

## Check Current Location

```bash
pwd
```
**Should show**: `/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way`

---

## Check if Homebrew is Installing/Installed

```bash
which brew
```
**If installed**: Shows a path like `/opt/homebrew/bin/brew`  
**If not installed**: No output

```bash
brew --version
```
**If installed**: Shows version number  
**If not installed**: "command not found"

---

## Check if GitKraken CLI is Installed

```bash
gk --version
```
**If installed**: Shows version  
**If not installed**: "command not found"

---

## Check GitHub Token

```bash
echo $GITHUB_TOKEN
```
**If set**: Shows token (starts with `ghp_`)  
**If not set**: No output

---

## Current Status (Based on Our Work)

- **GitHub Token**: ✅ Already added to `~/.zshrc`  
- **Homebrew**: ⏳ Installing (waiting for password)  
- **GitKraken CLI**: ⏳ Waiting for Homebrew to finish

---

*Created: January 17, 2026, 17:58 PST*
