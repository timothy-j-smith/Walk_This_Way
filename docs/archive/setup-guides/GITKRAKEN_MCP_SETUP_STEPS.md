# GitKraken MCP Setup Steps
**Date:** January 10, 2026

---

## INSTALLATION STEPS

### **Step 1: Install GitKraken CLI**

**Option A: Via Homebrew (Easiest)**
```bash
brew install gitkraken-cli
```

**Option B: Manual Download**
1. Visit: https://www.gitkraken.com/cli
2. Download for macOS
3. Follow installation instructions

---

### **Step 2: Verify Installation**

```bash
gk --version
```

Should show GitKraken CLI version.

---

### **Step 3: Authenticate**

```bash
gk auth login
```

This will:
- Open browser for authentication
- Link CLI to your GitKraken Pro account
- Complete authentication

---

### **Step 4: Set Organization (If Needed)**

```bash
gk organization set <ORG_NAME>
```

(Only if you have a GitKraken organization)

---

### **Step 5: Add to MCP Config**

Once CLI is installed and authenticated, we'll add GitKraken MCP to your configuration files.

---

## AFTER SETUP

**MCP Configuration Will Include:**
```json
"gitkraken": {
  "command": "gk",
  "args": ["mcp"]
}
```

**Then:**
- Restart Cursor
- Test by asking AI about git history

---

**Follow these steps and let me know when you've completed authentication!**
