# SPELL CHECKER GUIDE - Quick Fix for Underlined Words

**Created**: January 17, 2026, 09:30 PST  
**Purpose**: How to quickly add character names, place names, and novel-specific words to your spell checker

---

## 🎯 THE PROBLEM

Spell checker is underlining correct words like:
- Character names: Nick, Jackie, Patty, Maxanne, Grace, Dan, etc.
- Place names: Sudbury, Hop Brook, Cavicchio, etc.
- Novel-specific terms: Aerosmith, Queen, Fleetwood Mac, etc.

**You don't want to right-click each one individually!**

---

## ✅ THE SOLUTION: `.cspell.json` FILE

**Location**: `.cspell.json` in your project root

**Current words in your dictionary**:
- Sudowrite
- Maxanne
- WBCN
- Chbosky
- Dickey
- Goldman

---

## 📝 HOW TO ADD WORDS (Two Methods)

### **METHOD 1: Quick Add via Right-Click** (For 1-2 words)

1. Right-click on the underlined word
2. Choose **"Add 'WordName' to Workspace Dictionary"** or **"Add to Dictionary"**
3. Word is automatically added to `.cspell.json`

**This is fast for individual words, but slow if you have many!**

---

### **METHOD 2: Bulk Add to `.cspell.json`** (For Many Words)

**Your `.cspell.json` file looks like this**:

```json
{
  "version": "0.2",
  "language": "en",
  "dictionaries": ["en", "en-US"],
  "dictionaryDefinitions": [],
  "ignorePaths": [
    "**/node_modules/**",
    "**/.git/**",
    "**/dist/**",
    "**/build/**"
  ],
  "ignoreRegExpList": [],
  "allowCompoundWords": true,
  "words": [
    "Sudowrite",
    "Maxanne",
    "WBCN",
    "Chbosky",
    "Dickey",
    "Goldman"
  ]
}
```

**To add more words, just add them to the `"words"` array**:

```json
{
  "version": "0.2",
  "language": "en",
  "dictionaries": ["en", "en-US"],
  "dictionaryDefinitions": [],
  "ignorePaths": [
    "**/node_modules/**",
    "**/.git/**",
    "**/dist/**",
    "**/build/**"
  ],
  "ignoreRegExpList": [],
  "allowCompoundWords": true,
  "words": [
    "Sudowrite",
    "Maxanne",
    "WBCN",
    "Chbosky",
    "Dickey",
    "Goldman",
    
    // NOVEL CHARACTERS
    "Nick",
    "Jackie",
    "Patty",
    "Grace",
    "Dan",
    "Johnson",
    "Marsh",
    "Sartori",
    "Lally",
    "Wentworth",
    
    // PLACE NAMES
    "Sudbury",
    "Cavicchio",
    
    // BAND NAMES & MUSIC TERMS
    "Aerosmith",
    "Queen",
    "Fleetwood",
    "Mac",
    
    // NOVEL-SPECIFIC TERMS
    "Rampers",
    "Rats",
    "Regs",
    "Rollers",
    "Juilliard"
  ]
}
```

**Just add words to the `"words"` array, one per line, with quotes and commas.**

---

## 🎯 RECOMMENDED WORDS TO ADD (From Your Novel)

Based on your blueprint, here are words you'll likely need:

### **Character Names**
- Nick
- Jackie
- Patty
- Grace
- Dan
- Johnson
- Marsh
- Sartori
- Lally
- Wentworth

### **Place Names**
- Sudbury
- Hop Brook (or "Hopbrook" - check your usage)
- Cavicchio

### **Band Names**
- Aerosmith
- Queen
- Fleetwood (as in Fleetwood Mac - check if it's one word or two)

### **Novel-Specific Terms**
- Rampers
- Rats
- Regs
- Rollers
- Juilliard

---

## 🚀 QUICK STEPS

1. **Open `.cspell.json`** (in your project root)
2. **Find the `"words"` array** (starts around line 14)
3. **Add words** after the existing ones, each on its own line with quotes and commas
4. **Save the file**
5. **The spell checker will update automatically** - red underlines will disappear!

---

## 💡 TIP: Keep Adding as You Write

**As you write Draft 2**:
- If a word is underlined, add it to `.cspell.json`
- Either right-click → "Add to Dictionary" (quick)
- Or manually add to `.cspell.json` (if you have several to add at once)

---

## ❓ FAQ

**Q: Does this work for both spell checkers?**  
A: Yes! The `.cspell.json` file works with Code Spell Checker extension, which is your primary spell checker.

**Q: Will words added here work in all my files?**  
A: Yes! Once added to `.cspell.json`, the word is accepted everywhere in your project.

**Q: Do I need to restart Cursor?**  
A: No, just save the file. The spell checker updates automatically.

**Q: Can I add words in bulk?**  
A: Yes! Just add multiple words to the `"words"` array, one per line.

---

**This is much faster than right-clicking each word individually!**

**DISCO! 🎸**

---

*Created: January 17, 2026, 09:30 PST*
