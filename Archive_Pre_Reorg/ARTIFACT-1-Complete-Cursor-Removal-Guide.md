# ARTIFACT 1: COMPLETE CURSOR REMOVAL GUIDE
## Mac Studio System Cleanup - Exact Commands & Procedures

---

**Version:** 1.0  
**Created:** December 2024  
**Purpose:** Complete removal of all Cursor files, scripts, and configurations from Mac Studio  
**Target:** Clean system ready for new creative writing tools

---

## ⚠️ **PRE-REMOVAL BACKUP PROCEDURE**

### Step 1: Backup Your Writing Files
```bash
# Create backup directory
mkdir -p ~/Desktop/Cursor-Writing-System-Backup/$(date +%Y-%m-%d)

# Copy entire writing project
cp -r "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing" ~/Desktop/Cursor-Writing-System-Backup/$(date +%Y-%m-%d)/

# Verify backup
ls -la ~/Desktop/Cursor-Writing-System-Backup/$(date +%Y-%m-%d)/
```

### Step 2: Export Valuable Configurations
```bash
# Create config backup directory
mkdir -p ~/Desktop/Cursor-Writing-System-Backup/$(date +%Y-%m-%d)/configurations

# Copy .cursorrules (your writing style guide)
cp "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing/.cursorrules" ~/Desktop/Cursor-Writing-System-Backup/$(date +%Y-%m-%d)/configurations/

# Copy Universal Templates
cp "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Original Writing/Universal-Fiction-Templates.md" ~/Desktop/Cursor-Writing-System-Backup/$(date +%Y-%m-%d)/configurations/
```

---

## 🗑️ **COMPLETE CURSOR REMOVAL PROCESS**

### Phase 1: Remove Cursor Application
```bash
# Remove main Cursor application
sudo rm -rf /Applications/Cursor.app

# Verify removal
ls -la /Applications/ | grep -i cursor
```

### Phase 2: Remove User Data Directories
```bash
# Remove Cursor user support files
rm -rf ~/Library/Application\ Support/Cursor

# Remove Cursor caches
rm -rf ~/Library/Caches/Cursor

# Remove Cursor preferences
rm -rf ~/Library/Preferences/com.cursor.*

# Remove Cursor logs
rm -rf ~/Library/Logs/Cursor

# Remove Cursor saved application state
rm -rf ~/Library/Saved\ Application\ State/com.cursor.*

# Verify removal
ls -la ~/Library/Application\ Support/ | grep -i cursor
ls -la ~/Library/Caches/ | grep -i cursor
ls -la ~/Library/Preferences/ | grep -i cursor
```

### Phase 3: Remove VS Code Integration (Cursor uses VS Code settings)
```bash
# Remove VS Code user data (Cursor shares these)
rm -rf ~/.vscode

# Remove VS Code application support
rm -rf ~/Library/Application\ Support/Code

# Remove VS Code caches
rm -rf ~/Library/Caches/Code

# Remove VS Code preferences
rm -rf ~/Library/Preferences/com.microsoft.VSCode.*

# Verify removal
ls -la ~/ | grep -i vscode
ls -la ~/Library/Application\ Support/ | grep -i code
```

### Phase 4: Remove Configuration Files
```bash
# Remove keybindings
rm -f ~/Library/Application\ Support/Cursor/User/keybindings.json

# Remove settings
rm -f ~/Library/Application\ Support/Cursor/User/settings.json

# Remove any remaining cursor configs
find ~ -name "*cursor*" -type f 2>/dev/null
find ~ -name "*cursor*" -type d 2>/dev/null

# Remove any remaining VS Code configs
find ~ -name "*vscode*" -type f 2>/dev/null
find ~ -name "*vscode*" -type d 2>/dev/null
```

### Phase 5: Remove System-Level Cursor Files
```bash
# Check for system-level Cursor files
sudo find /System -name "*cursor*" 2>/dev/null
sudo find /usr -name "*cursor*" 2>/dev/null
sudo find /opt -name "*cursor*" 2>/dev/null

# Remove any found system files (be very careful)
# Only remove if you're certain they're Cursor-related
```

### Phase 6: Clean Launch Services Database
```bash
# Rebuild launch services database
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user

# Verify no Cursor entries remain
launchctl list | grep -i cursor
```

### Phase 7: Remove Cursor from System Preferences
```bash
# Remove from login items (if any)
# This must be done manually:
# System Preferences > Users & Groups > Login Items
# Remove any Cursor entries

# Remove from extensions (if any)
# This must be done manually:
# System Preferences > Extensions
# Remove any Cursor extensions
```

---

## 🔍 **VERIFICATION PROCEDURES**

### Step 1: Verify Application Removal
```bash
# Check Applications folder
ls -la /Applications/ | grep -i cursor

# Check if Cursor still launches
which cursor
```

### Step 2: Verify User Data Removal
```bash
# Check user directories
ls -la ~/Library/Application\ Support/ | grep -i cursor
ls -la ~/Library/Caches/ | grep -i cursor
ls -la ~/Library/Preferences/ | grep -i cursor
```

### Step 3: Verify Configuration Removal
```bash
# Check for remaining config files
find ~ -name "*cursor*" 2>/dev/null
find ~ -name "*vscode*" 2>/dev/null
```

### Step 4: Verify System Cleanup
```bash
# Check system processes
ps aux | grep -i cursor

# Check system files
sudo find /System -name "*cursor*" 2>/dev/null
```

---

## 🧹 **FINAL CLEANUP COMMANDS**

### Clear System Caches
```bash
# Clear system caches
sudo rm -rf /Library/Caches/*
sudo rm -rf ~/Library/Caches/*

# Clear user caches
rm -rf ~/Library/Caches/com.apple.helpd
rm -rf ~/Library/Caches/com.apple.nsurlsessiond
```

### Rebuild System Databases
```bash
# Rebuild spotlight index
sudo mdutil -E /

# Rebuild launch services
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -kill -r -domain local -domain system -domain user
```

### Restart System
```bash
# Restart Mac Studio
sudo reboot
```

---

## ✅ **POST-REMOVAL VERIFICATION CHECKLIST**

- [ ] Cursor application removed from /Applications/
- [ ] No Cursor processes running
- [ ] User data directories removed
- [ ] Configuration files removed
- [ ] VS Code integration removed
- [ ] System caches cleared
- [ ] Launch services rebuilt
- [ ] System restarted
- [ ] Backup files safely stored
- [ ] No remaining Cursor references in system

---

## 🚨 **IMPORTANT NOTES**

1. **Backup First:** Always backup your writing files before starting
2. **Run as Admin:** Some commands require sudo privileges
3. **Verify Each Step:** Check output of each command
4. **Restart Required:** System restart is necessary for complete cleanup
5. **Manual Steps:** Some System Preferences items must be removed manually

---

## 📞 **RECOVERY PROCEDURES**

If something goes wrong:
1. Restore from Time Machine backup
2. Reinstall macOS if necessary
3. Your writing files are safe in iCloud Drive
4. Your backup directory contains all valuable configurations

---

**END OF ARTIFACT 1**
