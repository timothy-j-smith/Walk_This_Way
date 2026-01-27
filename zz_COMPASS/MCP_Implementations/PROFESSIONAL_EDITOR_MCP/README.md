# Professional Editor MCP - TRIAL VERSION

**Status:** ⚠️ TRIAL MCP - First version for evaluation and refinement  
**Purpose:** Professional editorial evaluation and critique for fiction writing  
**Based on:** Publishing industry standards used by major houses

---

## 🎯 WHAT THIS MCP DOES

Provides **honest, constructive critique** based on professional editorial standards. Evaluates your fiction writing across six key areas and provides:

- **Overall Grade** (A+ to F) with score
- **Category-by-category evaluation** (Structure, Prose, Character, Dialogue, Pacing, Theme)
- **Areas of Strength** - What's working well
- **Areas for Improvement** - What needs work
- **Priority Recommendations** - What to fix first

---

## 📋 EVALUATION CRITERIA

### **Structure**
- Scene purpose and necessity
- Opening hook effectiveness
- Resolution/cliffhanger quality
- Scene advancement of plot/character

### **Prose**
- Verb strength and variety
- Filter word usage
- Show vs. tell balance
- Specificity vs. generic language
- Sentence rhythm and variety

### **Character**
- Distinct character voices
- Clear motivations
- Authentic reactions
- Internal state access
- Physical reactions (showing emotion)

### **Dialogue**
- Naturalness and authenticity
- Subtext presence
- Character-specific speech
- Balance with narrative
- Action beats vs. tags

### **Pacing**
- Sentence variety and rhythm
- Tension markers
- Scene length appropriateness
- Dynamic vs. static pacing

### **Theme**
- Thematic presence
- Natural integration (not preachy)
- Depth without heavy-handedness

---

## 🎓 GRADING SCALE

- **A+ (95-100):** Publication-ready. Minor polish needed.
- **A (90-94):** Strong work. Professional quality with minor issues.
- **B+ (85-89):** Good work. Needs revision but has strong foundation.
- **B (80-84):** Solid work. Multiple areas need improvement.
- **C+ (75-79):** Needs significant revision. Core issues present.
- **C (70-74):** Major revision required. Fundamental problems.
- **D (60-69):** Extensive revision needed. Multiple critical failures.
- **F (0-59):** Not ready. Requires complete rewrite or fundamental rethinking.

---

## 🚀 USAGE

### **Basic Evaluation:**
```
@professional-editor evaluate_manuscript text="[your chapter text]"
```

### **With Title:**
```
@professional-editor evaluate_manuscript text="[your chapter]" title="Chapter 10: Camp Winnipesaukee"
```

### **Focus on Specific Areas:**
```
@professional-editor evaluate_manuscript text="[your chapter]" focus_areas=["prose", "dialogue"]
```

---

## ⚠️ TRIAL MCP NOTES

This is a **first version** for evaluation. We will:
- Test effectiveness
- Gather feedback
- Refine evaluation criteria
- Adjust grading scales
- Add features based on needs

**Your feedback is essential for improvement!**

---

## 📁 FILES

- `server.py` - Main MCP server
- `README.md` - This file
- `requirements.txt` - Python dependencies
- `data/evaluations/` - Saved evaluation reports (JSON)

---

## 🔧 SETUP

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add to `.cursor/config/mcp.json`:
   ```json
   "professional-editor": {
     "command": "python",
     "args": [
       "/path/to/PROFESSIONAL_EDITOR_MCP/server.py"
     ],
     "disabled": false
   }
   ```

3. Restart Cursor to load MCP

---

## 📝 EVALUATION OUTPUT

Each evaluation includes:
- Overall grade and score
- Category scores
- Strengths (what's working)
- Issues (what needs work)
- Priority recommendations
- Saved JSON report for reference

---

**Created:** January 24, 2026  
**Version:** 1.0 (Trial)  
**Status:** Active - Awaiting Evaluation
