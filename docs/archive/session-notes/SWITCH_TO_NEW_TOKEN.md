# Switch to New Token - Step by Step
**Created:** January 22, 2026  
**Purpose:** Use your new "Personal GITHUB Token" (no expiration) instead of old one

---

## 🎯 WHAT YOU HAVE

**Two tokens:**
1. ✅ **"Personal GITHUB Token"** - NEW, no expiration (the one you want!)
2. ⚠️ **"Walk this Way"** - OLD, expires Feb 5, 2026 (currently being used)

**You need to switch from the old token to the new one!**

---

## ✅ STEP 1: Test Your New Token

**Your new token:** `ghp_gm1IKUYz8f1CJKtLqYhmX4nTZETZMM3WXUQN`

**I'll test it to make sure it works with your personal account!**

---

## 🔧 STEP 2: Use New Token in Terminal

**In Terminal, run:**

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
git push origin main
```

**When prompted:**
- **Username:** `timothy-j-smith`
- **Password:** `ghp_gm1IKUYz8f1CJKtLqYhmX4nTZETZMM3WXUQN`

**This will save the NEW token to your Mac Keychain, replacing the old one!**

---

## 🔧 STEP 3: Update GitKraken Pro

1. **Open GitKraken Pro**
2. **File → Preferences → Authentication**
3. **Remove the old GitHub connection** (if there is one)
4. **Add new connection:**
   - Username: `timothy-j-smith`
   - Token: `ghp_gm1IKUYz8f1CJKtLqYhmX4nTZETZMM3WXUQN`
5. **Save**

---

## 🗑️ STEP 4: Delete Old Token (Optional)

**Once the new token is working, you can delete the old one:**

1. **On GitHub tokens page**, find "Walk this Way" token
2. **Click the red "Delete" button**
3. **Confirm deletion**

**This cleans up old tokens you don't need anymore.**

---

## ✅ VERIFY IT'S WORKING

**After switching to new token:**

```bash
git push origin main
```

**Should work without asking for password (token is saved in Keychain)!**

---

## 🎯 SUMMARY

1. ✅ **New token created** - "Personal GITHUB Token" (no expiration)
2. ✅ **Use new token** - In Terminal and GitKraken Pro
3. ✅ **Old token can be deleted** - Once new one is working
4. ✅ **No more expiration worries** - New token never expires!

---

**Your new token is ready! Let's switch to it now!** 🎉

---

*Created to help switch to new token*  
*January 22, 2026*
