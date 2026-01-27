# GitKraken Pro Token Setup - Complete Guide
**Created:** January 22, 2026  
**Purpose:** Set up GitHub token for GitKraken Pro

---

## ✅ WHAT I'VE DONE

1. ✅ **Configured Git credential helper** - Token will be saved to Mac Keychain
2. ✅ **Set up your repository** - Ready to use token

---

## 🔧 HOW TO USE YOUR TOKEN

### **Option 1: GitKraken Pro (Easiest)**

**GitKraken Pro should automatically use your token!**

1. **Open GitKraken Pro**
2. **Go to:** Preferences → Authentication
3. **Add GitHub account:**
   - Click "Connect to GitHub"
   - It will open browser for authentication
   - OR enter your token manually if prompted

**GitKraken Pro will save the token and use it automatically!**

---

### **Option 2: Terminal (First Time Setup)**

**The first time you push from Terminal, enter your token:**

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
git push origin main
```

**When prompted:**
- **Username:** `timothy-j-smith`
- **Password:** `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`

**It will save to your Mac Keychain, so you won't need to enter it again!**

---

## 🔍 CHECK YOUR TOKEN PERMISSIONS

**Your token might need the right permissions:**

1. **Go to:** https://github.com/settings/tokens
2. **Find your token** (or create a new one)
3. **Make sure it has:**
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (optional, for GitHub Actions)

**If your token doesn't have `repo` permission, create a new one!**

---

## 🎯 GITKRAKEN PRO SETUP

### **Method 1: Through GitKraken UI**

1. **Open GitKraken Pro**
2. **File → Preferences → Authentication**
3. **Click "Connect to GitHub"**
4. **Follow the prompts** (it will use your browser)

### **Method 2: Manual Token Entry**

1. **Open GitKraken Pro**
2. **File → Preferences → Authentication**
3. **Click "Add" next to GitHub**
4. **Enter:**
   - **Username:** `timothy-j-smith`
   - **Token:** `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`

---

## ✅ TEST IT

**In GitKraken Pro:**
1. Make a small change (or just try to push)
2. Click "Push" button
3. It should work without asking for password!

**In Terminal:**
```bash
git push origin main
```
Should work without asking (after first time).

---

## 💡 WHY THIS IS NEEDED

- **GitHub stopped accepting passwords** in 2021
- **Personal Access Tokens** are required
- **GitKraken Pro** needs the token to push/pull
- **Once set up, it works automatically!**

---

**Your token is configured! GitKraken Pro should work now.** 🎉

---

*Setup complete*  
*January 22, 2026*
