# Dual Cursor Setup Management Guide 🎯

## Overview
This guide helps you manage two separate Cursor instances:
- **MAIN CURSOR**: Your stable, production workspace that you can't afford to break
- **EXPERIMENTAL CURSOR**: Your testing environment for learning new features safely

---

## 🔍 How to Identify Which Cursor You're In

### Quick Check Commands
Run these in your terminal to instantly know where you are:

```bash
# Quick identity check
echo "=== CURSOR INSTANCE CHECK ==="
echo "Git User: $(git config user.name)"
echo "Git Email: $(git config user.email)"
echo "Current Branch: $(git branch --show-current 2>/dev/null || echo 'No git repo')"
echo "Working Directory: $(pwd)"
```

### Visual Indicators You Should Set Up

#### 1. Window Title Method
**For Experimental Cursor workspaces:**
- Create `.vscode/settings.json` in your workspace:
```json
{
  "window.title": "🧪 EXPERIMENTAL - ${activeEditorShort}${separator}${rootName}",
  "workbench.colorTheme": "Default High Contrast"
}
```

**For Main Cursor workspaces:**
- Use standard titles and your preferred theme

#### 2. Terminal Prompt Method
Add to your shell profile (`.bashrc` or `.zshrc`):
```bash
# For experimental Cursor
export PS1="[🧪 EXP] $PS1"
```

---

## 🚀 How to Launch Specific Cursor Instances

### Method 1: Different Installation Locations
If you installed Cursor in different locations:
- **Main Cursor**: Default installation path
- **Experimental Cursor**: Custom path (if you chose one during installation)

### Method 2: Different Workspaces
- **Main Cursor**: Open your production projects
- **Experimental Cursor**: Open dedicated test/learning projects

### Method 3: Different Profiles (Recommended)
Create separate workspace folders:
```
~/CursorWorkspaces/
├── Main/           # For production work
└── Experimental/   # For testing and learning
```

---

## 🔧 Git Setup for Your Experimental Cursor

### Current Status
Your experimental Cursor currently has:
- Git User: "Cursor Agent"
- Git Email: "cursoragent@cursor.com"

### Recommended Configuration

#### Option A: Keep Separate Git Identities
```bash
# For Experimental Cursor (current setup is fine)
git config --global user.name "Experimental Cursor"
git config --global user.email "experimental.cursor@yourdomain.com"

# For Main Cursor (set this in your main instance)
git config --global user.name "Your Real Name"
git config --global user.email "your.real.email@domain.com"
```

#### Option B: Use Same Identity Everywhere
```bash
# Set the same in both instances
git config --global user.name "Your Real Name"
git config --global user.email "your.real.email@domain.com"
```

---

## 📚 Git vs GitHub Clarification

### Git vs GitHub - What's the Difference?

**Git** = Version control software (like Microsoft Word's track changes, but for code)
- Runs locally on your computer
- Tracks changes to your files
- Works offline

**GitHub** = Online hosting service for Git repositories
- Like Google Drive, but specifically for Git projects
- Stores your code online
- Enables collaboration

### Your Account Setup
You mentioned "GITBOT" - you likely mean **GitHub**:

1. **GitHub Account**: One account works for everything
   - Use the same GitHub account for both Cursor instances
   - Your login credentials remain the same

2. **Git Configuration**: Can be different per Cursor instance
   - This is just your name/email for commit messages
   - Doesn't affect your GitHub login

---

## 🖥️ Understanding Your Current Cursor Interface

### What You're Seeing (Modern Cursor Layout)

**Text Editor**: The main coding area where you write/edit files
**AI Chat**: Where you have conversations with AI (like this one)
**Composer**: Advanced AI feature for generating and editing code

### Why This Looks Different
Your experimental Cursor likely has:
- ✅ Updated interface design
- ✅ Latest features enabled
- ✅ Modern layout optimizations

Your main Cursor might have:
- Older version
- Different settings/preferences
- Disabled features for stability

---

## 🛠️ Setting Up Your Experimental Environment

### Step 1: Configure Git Properly
```bash
# Set up your identity (choose one approach from above)
git config --global user.name "Your Preferred Name"
git config --global user.email "your.email@domain.com"

# Verify the setup
git config --list | grep user
```

### Step 2: Create Workspace Markers
```bash
# In your experimental workspace
echo "EXPERIMENTAL_CURSOR_$(date +%Y%m%d)" > .cursor-instance

# Check it worked
cat .cursor-instance
```

### Step 3: Set Up GitHub Authentication
```bash
# Check if you're already authenticated with GitHub
gh auth status

# If not authenticated, login
gh auth login
```

---

## 🚦 Safe Experimentation Practices

### DO in Experimental Cursor:
- ✅ Test new AI features
- ✅ Try different themes/settings
- ✅ Experiment with extensions
- ✅ Practice Git commands
- ✅ Learn keyboard shortcuts

### DON'T in Experimental Cursor:
- ❌ Work on critical projects
- ❌ Test destructive commands without backups
- ❌ Share experimental branches to main repositories

---

## 🆘 Emergency Recovery

### If You Break Something:
1. **Don't panic** - you're in experimental mode for a reason
2. **Check which Cursor** you're in using the identity commands above
3. **Document what you did** - learning opportunity!
4. **Reset if needed** - experimental environments are meant to be rebuilt

### Font Size Issue You Experienced:
This likely happened because:
- Both Cursors were running simultaneously
- Settings were synced between instances
- You were in the same workspace/project

**Solution**: Always verify which instance you're in before making changes

---

## 📞 Who Am I?

I'm **Claude** (Anthropic's AI assistant), running as Cursor's AI backend. I can help you with:
- Code writing and debugging
- Git/GitHub workflows  
- Cursor feature explanations
- Learning programming concepts
- Project planning and architecture

---

## 🎯 Quick Start Checklist

- [ ] Run identity check command to confirm you're in experimental Cursor
- [ ] Configure Git with your preferred name/email
- [ ] Set up GitHub authentication (`gh auth login`)
- [ ] Create workspace marker file
- [ ] Test AI Chat, Composer, and Text Editor features
- [ ] Practice with a small test project
- [ ] Document what you learn for your main Cursor setup

---

## 🔄 Next Steps

1. **Verify your setup** using the commands in this guide
2. **Practice basic Git workflows** in this experimental environment
3. **Test Cursor's AI features** safely
4. **Once comfortable**, apply learnings to your main Cursor setup

Remember: The whole point of having two instances is to learn fearlessly in one while keeping the other stable!