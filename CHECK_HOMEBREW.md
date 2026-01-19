# Check Homebrew Installation Status

**If your terminal output is showing dashes/dots**, use these commands to check status:

---

## Step 1: Check if Homebrew Installed

Run this command:
```bash
which brew
```

**What you should see:**
- If Homebrew is installed: `/opt/homebrew/bin/brew` or `/usr/local/bin/brew`
- If not installed: (no output or error)

---

## Step 2: Test Homebrew

Run this command:
```bash
brew --version
```

**What you should see:**
- If installed: `Homebrew 4.x.x` (version number)
- If not installed: `command not found: brew`

---

## Step 3: If Homebrew is Installed, Install GitKraken CLI

Run this command:
```bash
brew install --cask gitkraken-cli
```

**Wait for it to finish** (may take a few minutes)

---

## Step 4: Verify GitKraken CLI

Run this command:
```bash
gk --version
```

**What you should see:**
- If installed: Version number like `gk version 1.x.x`
- If not installed: `command not found: gk`

---

## If Homebrew Installation is Still Running

**In your terminal where Homebrew is installing:**
- **Wait** - It takes 5-10 minutes
- **Look for** messages like "Installation successful!" or "Next steps:"
- **Don't close the terminal** until it's done

---

*Created: January 17, 2026, 17:58 PST*
