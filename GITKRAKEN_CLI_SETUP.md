# GitKraken CLI Setup Guide

**Created**: January 17, 2026, 09:30 PST  
**Purpose**: Instructions for installing GitKraken CLI for MCP setup

---

## 🎯 TWO METHODS TO INSTALL

### METHOD 1: Via GitKraken App (Easiest - No Homebrew Needed)

**If you already have GitKraken app installed:**

1. **Open GitKraken application**
2. **Go to**: GitKraken → Preferences (or `Cmd + ,`)
3. **Click**: "CLI" tab in left sidebar
4. **Click**: "Enable CLI" button
5. **Follow instructions**: GitKraken will show you the exact command to add to your PATH

**After enabling:**
- Close and reopen your terminal
- Test with: `gk --version`
- If it works, you're done! ✅

---

### METHOD 2: Via Homebrew (If Method 1 Doesn't Work)

**First, install Homebrew** (if not already installed):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

This will:
- Ask for your password (for sudo access)
- Install Homebrew (takes 5–10 minutes)
- Show you commands to add to your PATH

**After Homebrew is installed:**

```bash
brew install --cask gitkraken-cli
```

**Test installation:**
```bash
gk --version
```

---

## ✅ VERIFICATION

After installation, verify it works:

```bash
gk --version
```

You should see something like:
```
gk version 1.x.x
```

---

## 🔧 IF IT DOESN'T WORK

**Check your PATH:**

```bash
echo $PATH
```

Make sure the GitKraken CLI path is included. GitKraken will show you the exact path when you enable CLI in the app.

**Restart your terminal** after adding to PATH.

---

## 📝 NEXT STEPS (After GitKraken CLI is Installed)

1. **Enable MCP server** in `.cursor/config/mcp.json`:
   ```json
   "gitkraken": {
     "disabled": false
   }
   ```

2. **Restart Cursor completely** (Quit and reopen)

3. **Test with Claude**: "Show me recent git commits"

---

## 💡 RECOMMENDATION

**Try Method 1 first** (via GitKraken app) - it's simpler and doesn't require Homebrew.

**Use Method 2** only if:
- You don't have GitKraken app installed
- Method 1 doesn't work for you
- You want to use Homebrew anyway

---

*Created: January 17, 2026, 09:30 PST*
