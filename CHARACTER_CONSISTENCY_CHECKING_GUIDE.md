# Character Consistency Checking: Git Hooks & AI Solutions
**Date:** January 17, 2026  
**Time:** 19:50 PST  
**Project:** Walk This Way Novel  
**Purpose:** How to check character consistency before committing (e.g., warning if you write "Nick loved disco")

---

## ⚠️ WHAT GITKRAKEN PRO CANNOT DO

### **GitKraken Pro Limitations:**

**GitKraken Pro Desktop can:**
- ✅ Generate AI commit messages
- ✅ Stage, commit, and push files
- ✅ Visualize git history and branches
- ✅ Manage branches and merges

**GitKraken Pro Desktop cannot:**
- ❌ Track character details automatically
- ❌ Check prose for character consistency
- ❌ Warn about contradictions (e.g., "Nick loved disco" when Nick loves Aerosmith)
- ❌ Read Story Bible to validate character details

**Bottom Line:** GitKraken is a git tool, not a writing consistency checker. You'll need additional systems for character consistency checking.

---

## ✅ WHAT YOU CAN DO: THREE SOLUTIONS

You have **three ways** to check character consistency before committing:

1. **AI Assistant Check** (Before you commit, ask me)
2. **Git Pre-Commit Hook** (Automatic check before commit)
3. **Existing Systems** (Story Bible + Character Depth Coach)

---

## 🤖 SOLUTION 1: AI ASSISTANT CHECK (EASIEST)

### **Ask Me Before Committing:**

**Before you commit, ask me:**
```
"Check this chapter for character consistency - does it match the Story Bible?"
```

**I can:**
- ✅ Read your Story Bible (`Story_Bible/character-bible.md`)
- ✅ Check your prose for character details
- ✅ Warn if Nick is described as "loving disco" (he loves Aerosmith!)
- ✅ Check for timeline inconsistencies
- ✅ Verify character traits match Story Bible

**Workflow:**
```
1. Write chapter in Cursor
   ↓
2. Ask me: "Check character consistency for Nick in this chapter"
   ↓
3. I compare against Story Bible and warn if issues found
   ↓
4. Fix issues if needed
   ↓
5. Commit to git (via GitKraken or GUI)
```

**Why This Works:**
- ✅ No setup required - I'm already here
- ✅ I have access to your Story Bible
- ✅ I can read and analyze your prose
- ✅ I can catch contradictions before you commit

**Example Check:**
```
You: "I wrote that Nick loved disco - does that match his character?"

Me: "❌ WARNING: Nick's favorite band is Aerosmith (rock), not disco.
     According to Story Bible:
     - Nick: 'Favorite Band: Aerosmith !!'
     - Musical Style: 'Raw, passionate, emotional, loud, Aerosmith-influenced rock'
     - Disco contradicts his character (working-class rocker)
     Suggestion: Change to 'Nick loved Aerosmith' or remove disco reference."
```

---

## 🔧 SOLUTION 2: GIT PRE-COMMIT HOOK (AUTOMATED)

### **Automatic Check Before Every Commit:**

**A pre-commit hook runs automatically** before every `git commit`. It can:
- ✅ Scan staged files for character inconsistencies
- ✅ Check against Story Bible
- ✅ Warn or block commit if issues found

**How It Works:**
```bash
# Pre-commit hook runs before git commit
git add .
git commit -m "..."    # Hook runs here, checks files, warns if issues
```

**What You Can Check:**
- Character name + trait combinations (e.g., "Nick loved disco" = ERROR)
- Timeline inconsistencies (e.g., Dan's death date)
- Location mismatches (e.g., wrong street names)
- Character trait contradictions (e.g., Maxanne's age, Jackie's family)

**Example Hook Check:**
```
You try to commit chapter with: "Nick loved disco"

Hook detects:
- File: Draft_1/Act_II/Chapter_15.txt
- Line 42: "Nick loved disco"
- Story Bible says: Nick's favorite band is Aerosmith
- ❌ ERROR: Character consistency violation
- Commit blocked until you fix or approve
```

---

## 📋 SOLUTION 3: USE YOUR EXISTING SYSTEMS

### **You Already Have Character Tracking!**

**Your Existing Systems:**

1. **Story Bible** (`Story_Bible/character-bible.md`)
   - Source of truth for character details
   - Nick's favorite band: Aerosmith
   - Jackie's favorite band: Queen

2. **Character Depth Coach** (Agent)
   - Checks character consistency
   - Can analyze chapters for character issues
   - Provides feedback before you commit

3. **Writing DNA Memory System**
   - Tracks character development
   - Remembers character details
   - Can be queried for consistency

**How to Use Before Committing:**
```
1. Write chapter in Cursor
   ↓
2. Ask Character Depth Coach: "Check this chapter for Nick's character consistency"
   ↓
3. Coach analyzes and flags issues
   ↓
4. Fix issues if needed
   ↓
5. Commit to git
```

---

## 🎯 RECOMMENDED WORKFLOW

### **Best Approach: AI Assistant Check Before Committing**

**Daily Writing Session:**
```
1. Write chapter in Cursor
   ↓
2. Save file (Cmd+S)
   ↓
3. Ask me: "Check character consistency for [character] in this chapter"
   ↓
4. I check against Story Bible and warn if issues
   ↓
5. Fix issues if needed
   ↓
6. Stage changes in GitKraken Desktop
   ↓
7. AI commit message (GitKraken Pro)
   ↓
8. Commit and push
```

**Why This Works Best:**
- ✅ No setup required - I'm already available
- ✅ I can read Story Bible and your prose
- ✅ I catch issues before you commit
- ✅ You can ask anytime: "Does this match Nick's character?"

---

## 💡 PRACTICAL EXAMPLES

### **Example 1: Character Trait Check**

**Before Committing:**
```
You: "I wrote 'Nick loved disco' - does that match his character?"

Me: "❌ WARNING: Nick's favorite band is Aerosmith (rock), not disco.
     Story Bible: 'Favorite Band: Aerosmith !!'
     Musical Style: 'Raw, passionate, emotional, loud, Aerosmith-influenced rock'
     Disco contradicts his character (working-class rocker who loves Aerosmith).
     Suggestion: Change to 'Nick loved Aerosmith' or 'Nick hated disco'."
```

**After Fix:**
```
You: "I changed it to 'Nick loved Aerosmith' - is that correct?"

Me: "✅ CORRECT: Matches Story Bible perfectly.
     Nick's favorite band: Aerosmith
     Musical style: Aerosmith-influenced rock
     You're good to commit!"
```

### **Example 2: Timeline Check**

**Before Committing:**
```
You: "I wrote Dan died in 1977 - is that correct?"

Me: "⚠️ INCONSISTENCY: Story Bible shows two dates:
     - Character Bible: 'Died in construction accident, November 14, 1976'
     - Continuity Tracker: 'Death: 1977 (heart attack)'
     Need to confirm correct date before committing.
     Which is correct: 1976 or 1977?"
```

### **Example 3: Location Check**

**Before Committing:**
```
You: "I wrote Nick lived on Elm Street - is that correct?"

Me: "❌ WARNING: Story Bible shows:
     - Character Bible: 'Dutton Road (wrong side of Hop Brook)'
     - Continuity Tracker: 'Street: Dutton Road (later reference says Elm Street - NEEDS CONSISTENCY CHECK)'
     Dutton Road is correct. Elm Street needs correction."
```

---

## 🔧 ADVANCED: GIT PRE-COMMIT HOOK SETUP

### **If You Want Automatic Checking:**

**I can create a pre-commit hook** that automatically checks for:
- Character name + trait mismatches (e.g., "Nick loved disco")
- Timeline inconsistencies
- Location mismatches
- Story Bible contradictions

**How It Works:**
```bash
# Hook runs before every commit
git add .
git commit -m "..."    # Hook checks files, warns if issues
```

**What It Checks:**
- Scans staged files for character inconsistencies
- Compares against Story Bible
- Warns or blocks commit if issues found

**Would you like me to:**
- ✅ Create a pre-commit hook script?
- ✅ Set it up for character consistency checking?
- ✅ Configure it to check against Story Bible?

**Note:** This requires some setup, but gives you automatic checking before every commit.

---

## 📚 SUMMARY: WHAT CAN CHECK CHARACTER CONSISTENCY

### **What Cannot:**
- ❌ GitKraken Pro Desktop (git tool, not writing checker)
- ❌ Git itself (version control, not content checker)

### **What Can:**
- ✅ **AI Assistants (Me/Claude)** - Can check against Story Bible before commit
- ✅ **Character Depth Coach** - Agent that checks character consistency
- ✅ **Git Pre-Commit Hooks** - Automatic checking before commit
- ✅ **Story Bible** - Source of truth (but needs to be checked against)

---

## 🎯 RECOMMENDATION

**For Now: Use AI Assistant Check**
- ✅ No setup required
- ✅ I can check before you commit
- ✅ I have access to Story Bible
- ✅ I can analyze your prose

**Just ask me:** "Check character consistency for [character] in this chapter"

**For Later: Consider Git Pre-Commit Hook**
- ⏳ Requires setup
- ✅ Automatic checking before every commit
- ✅ No need to remember to ask
- ✅ Catches issues automatically

---

**Bottom Line:** GitKraken Pro cannot check character consistency automatically. But you can:
1. **Ask me before committing** (easiest, no setup)
2. **Use Character Depth Coach** (existing agent system)
3. **Set up git pre-commit hook** (automatic, requires setup)

**The easiest solution: Just ask me before you commit!**

---

*Last Updated: January 17, 2026 19:50 PST*
