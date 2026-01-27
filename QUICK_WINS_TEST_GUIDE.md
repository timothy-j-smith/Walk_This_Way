# QUICK WINS TEST GUIDE
## Step-by-Step Testing Instructions
**Date:** January 24, 2026

---

## 🧪 TEST 1: SESSION START SCRIPT

### Step 1: Run the Script
In your terminal, run:
```bash
./.cursor/scripts/session-start.sh
```

### Step 2: Follow the Checklist
The script will guide you through:
1. **Context Pinning** - It will remind you to pin:
   - `Story_Bible/character-bible.md`
   - `.cursor/rules/walk-this-way-writing-directives.md`
   - Your current chapter (if you have one open)

2. **Quick Access** - It will show you where guides are located

3. **Templates** - It will remind you about the template library

### Step 3: Pin Files (In Cursor)
1. Open Cursor
2. In the sidebar, find `Story_Bible/character-bible.md`
3. Right-click → "Pin to Context"
4. Repeat for `.cursor/rules/walk-this-way-writing-directives.md`
5. If you have a chapter open, pin that too

**Expected Result:** Script runs, reminds you, you pin files manually

---

## 🧪 TEST 2: XML TAGS TEMPLATE

### Step 1: Open Template Library
Open: `.cursor/rules/quick-wins-templates.md`

### Step 2: Copy Basic Scene Rewrite Template
Copy this template:
```
<goal></goal>
<tone></tone>
<constraint></constraint>
Write the scene.
```

### Step 3: Fill in the Brackets
Example:
```
<goal>Reveal Nick's anger about his father's death</goal>
<tone>Raw, defensive, masking vulnerability</tone>
<constraint>No exposition, show through action and dialogue</constraint>
Write the scene.
```

### Step 4: Paste into Cursor
1. Open Cursor Chat (or Agent, or Cmd+K)
2. Paste your filled-in template
3. Add your scene text or request

**Expected Result:** Better structured prompt, clearer output

---

## 🧪 TEST 3: ROLE PROMPTING TEMPLATE

### Step 1: Copy Role Template
From `quick-wins-templates.md`, copy:
```
You are a developmental editor specializing in [genre].
You focus on story structure, pacing, plot architecture, and narrative flow.
You identify structural weaknesses and provide strategic revision recommendations.

[Your question/request]
```

### Step 2: Fill in the Brackets
Example:
```
You are a developmental editor specializing in literary fiction.
You focus on story structure, pacing, plot architecture, and narrative flow.
You identify structural weaknesses and provide strategic revision recommendations.

Analyze Chapter 5's pacing and structure.
```

### Step 3: Paste into Cursor
Paste into Chat, Agent, or Cmd+K

**Expected Result:** Specialized feedback focused on structure and pacing

---

## 🧪 TEST 4: POWER COMBO (All Techniques)

### Step 1: Copy Power Combo Template
From `quick-wins-templates.md`, copy "Combo 1: Role + XML + Chain of Thought"

### Step 2: Fill in All Brackets
Example:
```
You are a line editor specializing in working-class authenticity.

<thinking>
- What does Nick want in this scene?
- What's the subtext?
- What are the consequences?
</thinking>

<scene>
<goal>Show Nick's defensive pride</goal>
<tone>Raw, masking vulnerability</tone>
<constraint>No exposition, show through action</constraint>
</scene>

Analyze and provide fixes.
```

### Step 3: Paste into Cursor
Paste into Chat, Agent, or Cmd+K

**Expected Result:** Deep analysis with structured output

---

## ✅ SUCCESS CRITERIA

### Session Start Script:
- ✅ Script runs without errors
- ✅ Reminds you to pin files
- ✅ Shows guide locations
- ✅ You successfully pin files in Cursor

### XML Tags Template:
- ✅ Template copied easily
- ✅ Filled in with your details
- ✅ Pasted into Cursor
- ✅ Output is better structured

### Role Prompting:
- ✅ Role template copied
- ✅ Filled in with genre/details
- ✅ Pasted into Cursor
- ✅ Feedback is specialized

### Power Combo:
- ✅ All techniques combined
- ✅ Filled in with details
- ✅ Pasted into Cursor
- ✅ Output is comprehensive

---

## 🎯 NEXT STEPS AFTER TESTING

### If Everything Works:
1. ✅ Use session start script every writing session
2. ✅ Build your example library (create `.cursor/examples/` directory)
3. ✅ Use templates regularly
4. ✅ Progress from simple to Power Combos

### If Something Doesn't Work:
- Check script permissions: `chmod +x .cursor/scripts/session-start.sh`
- Verify template file exists: `.cursor/rules/quick-wins-templates.md`
- Check file paths are correct
- Ask for help!

---

**Ready to test?** Start with Test 1 (Session Start Script) - it's the easiest!
