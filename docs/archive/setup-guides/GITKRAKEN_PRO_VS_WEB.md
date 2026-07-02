# GitKraken Pro vs GitKraken.dev - Where to Find Preferences
**Created:** January 22, 2026  
**Problem:** Can't find File/Preferences menu

---

## 🎯 THE DIFFERENCE

### **GitKraken.dev (Web Interface)**
- ✅ What you're looking at in the screenshot
- ✅ Web-based (runs in browser)
- ❌ **NO File/Preferences menu** (web apps don't have these)
- ✅ Has "Settings" in left sidebar instead

### **GitKraken Pro (Desktop App)**
- ✅ Desktop application (installed on your Mac)
- ✅ **HAS File/Preferences menu** (traditional desktop app)
- ✅ This is where you configure authentication

---

## 🔍 WHERE TO FIND PREFERENCES IN DESKTOP APP

### **GitKraken Pro (Desktop Application):**

**On Mac:**
1. **Open GitKraken Pro** (the desktop app, not the web)
2. **Top menu bar:** Click "GitKraken" (next to Apple logo)
3. **Click:** "Preferences" (or press `Cmd+,`)
4. **Left sidebar:** Click "Authentication"
5. **GitHub section:** Add your token here

**Or:**
- **File menu:** Some versions have "File" → "Preferences"
- **Keyboard shortcut:** `Cmd+,` (Command + Comma)

---

## 🌐 IF YOU'RE USING GITKRAKEN.DEV (WEB)

**The web version uses different settings:**

1. **Click your profile icon** (top right)
2. **Click:** "Settings" or "Account Settings"
3. **Look for:** "Integrations" or "GitHub"
4. **Connect GitHub account** there

**But for tokens, you might need to use the desktop app!**

---

## ✅ EASIER WAY: Use Terminal First

**Since terminal didn't prompt you, let's test if it's working:**

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
git push origin main
```

**If it works without asking:**
- ✅ Token is already saved in Mac Keychain
- ✅ GitKraken Pro should use it automatically
- ✅ You might be all set!

**If it asks for username/password:**
- Enter: `timothy-j-smith`
- Password: Your new token (no expiration)

---

## 🎯 QUICK CHECK: Which GitKraken Are You Using?

**Desktop App (GitKraken Pro):**
- ✅ Has menu bar at top (File, Edit, View, etc.)
- ✅ Has "GitKraken" menu (next to Apple logo)
- ✅ Can access Preferences via `Cmd+,`

**Web App (GitKraken.dev):**
- ✅ Runs in browser
- ✅ No menu bar
- ✅ Has "Settings" in left sidebar

---

## ✅ SUMMARY

1. **If using desktop app:** `Cmd+,` or GitKraken menu → Preferences
2. **If using web app:** Profile icon → Settings → Integrations
3. **Test terminal first:** `git push` - if it works, you're done!
4. **Token might already be saved** in Mac Keychain

---

**Let's test if your token is already working in terminal first!** 🎯

---

*Created to help find Preferences*  
*January 22, 2026*
