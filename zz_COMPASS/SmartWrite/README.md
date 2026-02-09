# SMARTWRITE SYSTEM
**Location:** `SmartWrite/`  
**Purpose:** All Smart Rewrites System enhancements, organized by date and chapter

---

## 📁 FOLDER STRUCTURE

```
SmartWrite/
├── README.md (this file)
├── Requests/          # Author-initiated SmartWrite requests
│   └── [YYYY-MM-DD]_Request_Template.md
├── Results/           # All SmartWrite enhancement results
│   ├── [YYYY-MM-DD]_Chapter_XX_[Title]/
│   │   ├── Enhancement_Report.md
│   │   ├── Selected_Options.md (author choices)
│   │   └── Iterations/ (if re-run)
│   └── [YYYY-MM-DD]_Chapters_XX-YY/ (multiple chapters)
└── Archive/           # Completed/approved enhancements
```

---

## 🚀 HOW TO INITIATE SMARTWRITE

### **Method 1: Simple Chat Request (Easiest)**

Just tell me (HANK) in chat:

```
"SmartWrite Chapter 6, Moderate liberty"
"SmartWrite Chapter 11, passages 1-3, Conservative"
"SmartWrite Chapters 4-6, High liberty"
```

**That's it!** No code, no scripts, no forms to fill out.

---

### **Method 2: Request Template (For Complex Requests)**

If you want to be more specific, create a file in `SmartWrite/Requests/`:

**File:** `SmartWrite/Requests/2025-11-29_Chapter_06_Request.md`

```markdown
# SmartWrite Request
**Date:** 2025-11-29
**Chapter(s):** Chapter 6 "Jackie's World"
**Liberty Level:** Moderate
**Specific Passages:** 
- Opening breakfast scene (paragraphs 1-2)
- Dr. Marsh reveal (paragraphs 5-6)
- Piano moment (paragraph 8)
- Final reflection (last paragraph)

**Focus Areas:**
- Voice DNA consistency
- Subtext reinforcement (class divide)
- Remove purple prose

**Mode:** Neutral
```

Then just say: "Process the SmartWrite request in Requests folder"

---

### **Method 3: Inline Request (While Editing)**

While you're reading a chapter, just highlight text and say:

```
"SmartWrite this passage, Moderate liberty"
"Enhance this section with SmartWrite, Conservative"
```

I'll process it immediately and save to `SmartWrite/Results/`

---

## 📊 HOW I SELECT PASSAGES

**When you say "SmartWrite Chapter X":**

1. **I read the entire chapter**
2. **I identify key moments:**
   - Opening scenes (first impressions)
   - Emotional beats (conflict, revelation, resolution)
   - Character voice moments (dialogue, internal monologue)
   - Thematic moments (class divide, friendship, music)
   - Transitions (scene changes, time shifts)
3. **I prioritize passages that:**
   - Need voice calibration
   - Could strengthen subtext
   - Have purple prose to cut
   - Need more specific detail
   - Are thematically important

**You can override:** Just tell me which passages you want!

---

## 📁 FILE ORGANIZATION

### **Single Chapter:**
```
SmartWrite/Results/2025-11-29_Chapter_06_Jackies_World/
├── Enhancement_Report.md (all options)
├── Selected_Options.md (your choices)
└── Iterations/
    └── 2025-11-29_Iteration_02.md (if re-run)
```

### **Multiple Chapters:**
```
SmartWrite/Results/2025-11-29_Chapters_04-06/
├── Chapter_04_Enhancement_Report.md
├── Chapter_05_Enhancement_Report.md
├── Chapter_06_Enhancement_Report.md
└── Selected_Options_All_Chapters.md
```

### **Partial Chapter:**
```
SmartWrite/Results/2025-11-29_Chapter_06_Passages_1-3/
├── Enhancement_Report.md
└── Selected_Options.md
```

---

## 🔄 ITERATION WORKFLOW

**If you want to re-run SmartWrite:**

1. **Tell me:** "Re-run SmartWrite on Chapter 6, try High liberty this time"
2. **I create:** New iteration file in `Iterations/` folder
3. **You compare:** Original vs. Iteration 1 vs. Iteration 2
4. **You select:** Best elements from each

**All iterations are saved** so you can always go back!

---

## ✅ AUTHOR CHOICES

**After I provide enhancements, you can:**

1. **Select options:** Tell me which ones you like
2. **Combine elements:** "Use Option 1 from Passage 1, Option 2 from Passage 2"
3. **Request changes:** "Make Option 1 less formal"
4. **Apply to chapter:** I'll update the actual chapter file

**Your choices are saved in `Selected_Options.md`** for reference!

---

## 🎯 LIBERTY LEVELS

- **Conservative:** Polish only, minimal changes
- **Moderate:** Balanced revision (default)
- **High:** Dramatic transformation
- **Blue Sky:** Exploratory (clearly labeled)

**Just tell me which one you want!**

---

## 💡 EXAMPLES

### **Example 1: Full Chapter**
```
You: "SmartWrite Chapter 6, Moderate"
Me: Creates SmartWrite/Results/2025-11-29_Chapter_06_Jackies_World/Enhancement_Report.md
```

### **Example 2: Specific Passages**
```
You: "SmartWrite Chapter 11, just the cafeteria scene, Conservative"
Me: Creates SmartWrite/Results/2025-11-29_Chapter_11_Cafeteria_Scene/Enhancement_Report.md
```

### **Example 3: Multiple Chapters**
```
You: "SmartWrite Chapters 4-6, Moderate liberty"
Me: Creates SmartWrite/Results/2025-11-29_Chapters_04-06/ with separate reports
```

### **Example 4: Re-run with Different Liberty**
```
You: "Re-run SmartWrite Chapter 6, try High liberty this time"
Me: Creates SmartWrite/Results/2025-11-29_Chapter_06_Jackies_World/Iterations/2025-11-29_Iteration_02.md
```

---

## 🎉 NO CODE REQUIRED!

**Everything is done through:**
- Simple chat commands
- Optional markdown templates
- Automatic file organization

**You just talk to me, and I handle everything!**

---

**Last Updated:** November 29, 2025  
**System Status:** ✅ Active and Ready

