# GitKraken CLI Troubleshooting
**Date:** January 10, 2026

---

## CURRENT STATUS

✅ **GitKraken Desktop is installed** (found in `/Applications/`)
❌ **GitKraken CLI (`gk` command) is not yet accessible**

---

## IMPORTANT: CLI vs Desktop App

**GitKraken Desktop App** ≠ **GitKraken CLI**

The desktop app (GitKraken.app) is separate from the CLI tool (`gk`). The CLI needs to be installed separately.

---

## INSTALLATION OPTIONS

### **Option 1: Download Binary Directly**

1. Visit: https://www.gitkraken.com/cli
2. Download the macOS binary
3. Move it to a location in your PATH:
   ```bash
   # After downloading to ~/Downloads/gk
   chmod +x ~/Downloads/gk
   sudo mv ~/Downloads/gk /usr/local/bin/gk
   ```
4. Verify:
   ```bash
   gk --version
   ```

### **Option 2: Install Homebrew (Then Use Homebrew)**

If you want to use Homebrew (package manager for macOS):

```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install GitKraken CLI
brew install gitkraken-cli
```

---

## WHERE ARE YOU STUCK?

**Please tell me:**
1. What did you try? (download, install, etc.)
2. What error message do you see?
3. Did you download a file? If so, where is it?

Once I know where you're stuck, I can help you complete the setup!

---

**Common Issues:**
- Downloaded binary but didn't move it to PATH
- Need to make binary executable (`chmod +x`)
- Need to authenticate after installation (`gk auth login`)
