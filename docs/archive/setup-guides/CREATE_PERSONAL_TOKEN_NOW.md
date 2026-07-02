# CREATE PERSONAL GITHUB TOKEN - STEP BY STEP
**Created:** January 22, 2026  
**URGENT:** Need to create token from PERSONAL account (not work!)

---

## ⚠️ TOKEN STATUS

**Your tokens:**
- ❌ Token 1 (10/8/25): **EXPIRED** - No longer works
- ❌ Token 2 (1/6/26): **EXPIRED** - No longer works  
- ❌ Token 3 (recent): **WORK ACCOUNT** - Wrong account!

**You need a NEW token from your PERSONAL account!**

---

## ✅ CREATE PERSONAL TOKEN - STEP BY STEP

### **Step 1: Make Sure You're on Personal Account**

1. **Open browser** (Safari or Chrome)
2. **Go to:** https://github.com
3. **Check top right corner:**
   - Should show: `timothy-j-smith` (your PERSONAL account)
   - NOT: `tsmit1_nike` (work account)
4. **If you see work account:**
   - Click your profile picture (top right)
   - Click "Sign out"
   - Sign back in with your PERSONAL account (`timothy-j-smith`)

---

### **Step 2: Create the Token**

1. **While logged into PERSONAL account**, go to:
   ```
   https://github.com/settings/tokens
   ```

2. **Click:** "Generate new token" → "Generate new token (classic)"

3. **Fill in the form:**
   - **Note:** `Walk This Way Personal - NEVER EXPIRES`
   - **Expiration:** Select **"No expiration"** (so it never expires!)
   - **Scopes:** Check ONLY:
     - ✅ `repo` (Full control of private repositories)
   - **DO NOT check other boxes** (you don't need them)

4. **Scroll down and click:** "Generate token" (green button)

5. **IMPORTANT:** Copy the token immediately!
   - It starts with `ghp_`
   - You'll only see it once!
   - **Write it down somewhere safe!**

---

### **Step 3: Test the Token**

**Once you have your new personal token, tell me and I'll test it!**

Or test it yourself:
```bash
curl -s -H "Authorization: token YOUR_NEW_TOKEN" https://api.github.com/user
```

**Should show:**
- `"login": "timothy-j-smith"` (your PERSONAL account)
- NOT `"tsmit1_nike"` (work account)

---

### **Step 4: Use the Token**

**In Terminal:**
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
git push origin main
```

**When prompted:**
- **Username:** `timothy-j-smith`
- **Password:** Paste your NEW personal token

**It will save to Keychain automatically!**

---

### **Step 5: Update GitKraken Pro**

1. **Open GitKraken Pro**
2. **File → Preferences → Authentication**
3. **Remove any existing GitHub connections**
4. **Add new connection:**
   - Username: `timothy-j-smith`
   - Token: Your NEW personal token
5. **Save**

---

## 💡 ABOUT TOKEN EXPIRATION

**Tokens can expire if:**
- ✅ You set an expiration date when creating them
- ✅ You delete them manually
- ✅ GitHub revokes them for security

**To prevent expiration:**
- ✅ **Always choose "No expiration"** when creating tokens
- ✅ **Don't delete tokens** unless you're replacing them
- ✅ **Keep tokens safe** - don't share them

**Your old tokens expired because:**
- They were probably set to expire after 90 days or similar
- That's why they stopped working

---

## ✅ SUMMARY

1. **Log into PERSONAL GitHub** (`timothy-j-smith`)
2. **Create new token** with "No expiration"
3. **Copy token** (you'll only see it once!)
4. **Test it** (should show personal account)
5. **Use it** in Terminal and GitKraken Pro
6. **Done!** It will never expire

---

**Once you create the token, share it with me and I'll help you set it up!** 🎯

---

*Created to help you create the right token*  
*January 22, 2026*
