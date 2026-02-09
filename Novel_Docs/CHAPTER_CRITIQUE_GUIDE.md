# Chapter Critique Guide - All MCPs

**Chapter:** Camp Winnipesaukee (Lehane-filtered version)  
**Date:** January 24, 2026  
**Status:** Ready for Multi-MCP Critique

---

## 🎯 AVAILABLE CRITIQUE MCPs

### 1. **PROFESSIONAL_EDITOR_MCP** ⚠️ TRIAL VERSION
**Status:** ✅ Created and configured  
**Purpose:** Professional editorial evaluation with grading (A+ to F)

**How to Use:**
```
@professional-editor evaluate_manuscript text="[paste chapter]" title="Chapter: Camp Winnipesaukee"
```

**What It Provides:**
- Overall grade (A+ to F) with score
- Category scores: Structure, Prose, Character, Dialogue, Pacing, Theme
- Strengths (what's working)
- Issues (what needs work)
- Priority recommendations

**Evaluation Criteria:**
- Structure: Scene purpose, opening hook, resolution
- Prose: Verb strength, filter words, show vs tell, specificity
- Character: Voice distinction, motivations, internal state
- Dialogue: Naturalness, subtext, character-specific speech
- Pacing: Sentence variety, tension markers, rhythm
- Theme: Presence, integration, subtlety

---

### 2. **FICTION_REVERSE_ENGINEERING_MCP**
**Status:** ✅ Installed and configured  
**Purpose:** Mathematical analysis comparing to bestseller formulas

**How to Use:**
```
@fiction-reverse-engineering analyze_pacing text="[paste chapter]"
@fiction-reverse-engineering compare_to_bestseller your_text="[paste chapter]" bestseller_title="Mystic River" detailed=true
```

**What It Provides:**
- Pacing analysis (tension curves, reveal frequency)
- Dialogue pattern analysis
- Structure comparison to bestsellers
- Mathematical metrics (sentence length, dialogue percentage)

---

### 3. **DENNIS_LEHANE_MCP**
**Status:** ✅ Installed and configured  
**Purpose:** Style-specific critique based on Lehane techniques

**How to Use:**
```
@dennis-lehane-style compare_to_lehane_style text="[paste chapter]" focus="dialogue"
```

**What It Provides:**
- Comparison to Lehane's style techniques
- Loss of innocence theme analysis
- Silence/unspoken themes check
- Boston grit authenticity
- Visceral description evaluation

---

## 📋 RECOMMENDED CRITIQUE WORKFLOW

### **Step 1: Professional Editor Evaluation**
Get overall grade and comprehensive feedback:
```
@professional-editor evaluate_manuscript text="[chapter]" title="Camp Winnipesaukee"
```

### **Step 2: Fiction Reverse Engineering Analysis**
Get mathematical pacing and structure analysis:
```
@fiction-reverse-engineering analyze_pacing text="[chapter]"
```

### **Step 3: Style-Specific Critique**
Get Lehane-style evaluation:
```
@dennis-lehane-style compare_to_lehane_style text="[chapter]"
```

### **Step 4: Compare Results**
Review all three critiques and identify:
- Common issues across all MCPs (priority fixes)
- Conflicting feedback (needs judgment)
- Areas of strength (preserve these)

---

## ⚠️ IMPORTANT NOTES

1. **Restart Cursor Required:** The new PROFESSIONAL_EDITOR_MCP needs Cursor to be restarted to load.

2. **Trial MCP:** PROFESSIONAL_EDITOR_MCP is marked as TRIAL - we'll evaluate and refine based on results.

3. **Combined Approach:** Use all three MCPs for comprehensive critique:
   - Professional Editor = Overall quality assessment
   - Fiction Reverse Engineering = Objective metrics
   - Dennis Lehane = Style-specific feedback

---

## 🚀 NEXT STEPS

1. **Restart Cursor** to load PROFESSIONAL_EDITOR_MCP
2. **Run Professional Editor evaluation** first (overall assessment)
3. **Run Fiction Reverse Engineering** (objective metrics)
4. **Run Dennis Lehane comparison** (style-specific)
5. **Review all three** and create action plan

---

**Created:** January 24, 2026  
**Status:** Ready for Use
