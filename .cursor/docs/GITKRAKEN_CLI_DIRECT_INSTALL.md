# GitKraken CLI Direct Install Instructions
**Date:** January 10, 2026

---

## YOUR MAC: Apple M4 Max (Apple Silicon)

✅ **You need: Apple Silicon / ARM64 version**

---

## EASIEST METHOD: Manual Download

Since Homebrew installation got complicated, let's do it manually:

### **Step 1: Download**

1. Visit: **https://github.com/gitkraken/gk-cli/releases**
2. Look for the latest release
3. Download the file that says:
   - `gk_Darwin_arm64.tar.gz` OR
   - `gk-macos-arm64.tar.gz` OR
   - Any file with "Darwin" or "macos" and "arm64"

### **Step 2: Extract**

After downloading, double-click the `.tar.gz` file to extract it (or use terminal)

### **Step 3: Install**

Once extracted, you'll have a `gk` file. Then run these commands in terminal:

```bash
# Make it executable
chmod +x ~/Downloads/gk

# Move it to a system directory
sudo mv ~/Downloads/gk /usr/local/bin/gk

# Verify it works
gk --version
```

### **Step 4: Authenticate**

```bash
gk auth login
```

---

**Go to https://github.com/gitkraken/gk-cli/releases and download the ARM64 version!**
