# AGENT TESTING & VERIFICATION GUIDE

**How to Verify Agents Are Set Up Properly and Know Their Job Descriptions**

---

## 🎯 QUICK TEST (30 Seconds)

### **Step 1: Start New Chat with Agent**
1. Open Cursor
2. Settings → Custom Agents → Select agent (e.g., "Creative Collaborator")
3. Start new chat (`Cmd+L` or `Cmd+I`)

### **Step 2: Ask This Question:**
```
What is your role and what files do you use?
```

### **Step 3: Check Response**
**✅ GOOD Response (Agent knows its job):**
- States its specific role clearly
- Lists files it uses (Test_Draft_Copy, Story_Bible, etc.)
- Mentions its process or capabilities
- References Agent.json or master orchestration

**❌ BAD Response (Agent doesn't know its job):**
- Generic AI assistant response
- Doesn't mention specific role
- Doesn't list files
- Seems confused about purpose

---

## 🔍 DETAILED VERIFICATION TESTS

### **TEST 1: Role Verification**

**Ask:**
```
What is your exact role in the Walk This Way project? What makes you different from the other agents?
```

**Expected Response Should Include:**
- Specific role name (e.g., "Strategic Writing Coordinator")
- Mission statement
- What it does vs. what it doesn't do
- How it differs from other agents

**Example Good Response:**
> "I'm the Strategic Writing Coordinator - your right hand man for 'Walk This Way.' I coordinate your specialized agents, track your progress, and ensure quality consistency across all chapters. Unlike the other agents who focus on specific areas (character, prose, structure), I take a macro-level strategic view and coordinate the workflow."

---

### **TEST 2: File Access Verification**

**Ask:**
```
What files and folders do you have access to? What is the correct folder for current drafts?
```

**Expected Response Should Include:**
- `Test_Draft_Copy/` (NOT Working_Chapters - that's outdated!)
- `Story_Bible/`
- `.cursor/agents/Agent.json`
- Other relevant files from its contextFiles list

**Example Good Response:**
> "I have access to:
> - Test_Draft_Copy/ (current drafts needing work)
> - Story_Bible/ (character voices, timeline, music references)
> - .cursor/agents/Agent.json (master orchestration)
> - .cursorrules (writing values and mission)
> - WRITING_DNA_MEMORY_SYSTEM.md (automatic memory system)"

**❌ RED FLAG:** If agent says "Working_Chapters" - that's outdated! Should say "Test_Draft_Copy"

---

### **TEST 3: Process Verification**

**Ask:**
```
Walk me through your process. How do you work with Timothy?
```

**Expected Response Should Include:**
- Step-by-step process
- How it saves work (Agent_Work folder)
- How it collaborates
- Mode system (Neutral/Nice/Professional)

**Example Good Response (Creative Collaborator):**
> "My process:
> 1. You share a passage that needs work
> 2. I analyze it and provide 2-3 rewrite options
> 3. You choose what works
> 4. I can deploy Smart Rewrites, JSON Prompts, DNA Memory integration
> 5. We iterate until it's perfect
> 
> I save my work to Agent_Work/Creative_Collaborator/"

---

### **TEST 4: Mode System Verification**

**Ask:**
```
What modes do you support? What's the difference between them?
```

**Expected Response Should Include:**
- Neutral (default) - balanced professional assessment
- Nice - supportive and encouraging
- Professional - brutal honesty, literary agent critique

**Example Good Response:**
> "I support three modes:
> - **Neutral** (default): Balanced professional assessment, identifies strengths and areas for improvement
> - **Nice**: Encouraging and supportive, ideal for early drafts
> - **Professional**: Professional literary agent critique - direct, honest, uncompromising. Identifies every weakness without sugar-coating, but also highlights what's genuinely well-written."

---

### **TEST 5: Master Orchestration Verification**

**Ask:**
```
What is the master theme of Walk This Way? What are the core themes?
```

**Expected Response Should Include:**
- Master Theme: Lost Innocence
- Core themes: Class Divide, Prejudice, Friendship, Rock and Roll, Corporate Takeover
- Character names (Nick, Jackie, Maxanne, Patty)
- Timeline (1974-1979, 2024)

**Example Good Response:**
> "The master theme is **Lost Innocence**, which encompasses:
> - Class Divide (Nick vs. Jackie's economic worlds)
> - Prejudice (societal expectations and limitations)
> - Friendship (how innocence allows connection, adulthood destroys it)
> - Rock and Roll (music as the bridge that fails between classes)
> - Corporate Takeover (WBCN's corporate destruction of authentic institutions)"

**❌ RED FLAG:** If agent doesn't know the themes, it's not loading Agent.json properly!

---

## 🚨 TROUBLESHOOTING

### **Problem: Agent gives generic response**

**Possible Causes:**
1. JSON file not loading
2. MCP not enabled
3. Agent not selected from Custom Agents dropdown
4. Invalid JSON syntax

**Fixes:**
1. Check JSON file exists in `.cursor/agents/`
2. Verify JSON is valid (no syntax errors)
3. Enable MCP in Custom Agent Settings
4. Restart Cursor
5. Try @ mention instead: `@.cursor/agents/[AGENT].json`

---

### **Problem: Agent references wrong folder (Working_Chapters)**

**Fix:**
- Update JSON file's `contextFiles` array
- Change `Working_Chapters/` → `Test_Draft_Copy/`
- Restart Cursor
- Test again

---

### **Problem: Agent doesn't know its role**

**Fixes:**
1. Check `systemPrompt` in JSON file is complete
2. Verify `description` field is filled
3. Check `whatIDo` and `whatIDontDo` arrays
4. Ensure JSON file is in `.cursor/agents/`
5. Restart Cursor

---

### **Problem: Agent can't access files**

**Fixes:**
1. Enable MCP in Custom Agent Settings
2. Check MCP config in `~/.cursor/mcp.json`
3. Verify file paths in `contextFiles` are correct
4. Use absolute paths if needed
5. Check Node.js is installed (for MCP)

---

## ✅ VERIFICATION CHECKLIST

Before using an agent, verify:

- [ ] Agent states its specific role clearly
- [ ] Agent lists correct files (Test_Draft_Copy, not Working_Chapters)
- [ ] Agent knows its process
- [ ] Agent knows mode system
- [ ] Agent knows master theme (Lost Innocence)
- [ ] Agent knows core themes (Class Divide, etc.)
- [ ] Agent knows character names (Nick, Jackie, Maxanne, Patty)
- [ ] Agent references Agent.json or master orchestration
- [ ] Agent mentions its save location (Agent_Work folder)

---

## 🎯 QUICK VERIFICATION PROMPT

**Copy/paste this into any agent chat:**

```
I want to verify you're set up correctly. Please tell me:
1. Your exact role and mission
2. The correct folder for current drafts (should be Test_Draft_Copy, NOT Working_Chapters)
3. The master theme of Walk This Way
4. Your process for working with me
5. Where you save your work
```

**If agent answers all 5 correctly: ✅ SET UP PROPERLY**

**If agent misses any: ❌ NEEDS FIXING**

---

## 📋 AGENT-SPECIFIC VERIFICATION

### **Creative Collaborator Should Know:**
- ✅ Hands-on rewriting partner
- ✅ Advanced Tools Expert (Smart Rewrites, JSON Prompts)
- ✅ Works WITH you on actual prose
- ✅ Provides 2-3 options for every passage
- ✅ Test_Draft_Copy/ folder

### **Strategic Coordinator Should Know:**
- ✅ Strategic oversight and workflow coordination
- ✅ Coordinates other agents
- ✅ Tracks progress across chapters
- ✅ Recommends optimal agent/prompt combinations
- ✅ Test_Draft_Copy/ folder

### **Character Coach Should Know:**
- ✅ Character development and voice consistency
- ✅ Character Voice DNA (Nick, Jackie, Maxanne)
- ✅ Emotional depth and authenticity
- ✅ 1970s Boston voice and setting
- ✅ Test_Draft_Copy/ folder

### **Prose Expert Should Know:**
- ✅ Prose polish and voice consistency
- ✅ Stephen King influence
- ✅ Show vs. tell techniques
- ✅ Word repetition reduction
- ✅ Test_Draft_Copy/ folder

### **Structural Specialist Should Know:**
- ✅ Pacing and story flow
- ✅ Thematic consistency
- ✅ Plot holes and inconsistencies
- ✅ Chapter transitions
- ✅ Test_Draft_Copy/ folder

---

## 🚀 RECOMMENDED TESTING WORKFLOW

1. **Start with Creative Collaborator** (most complex, tests everything)
2. **Run Quick Test** (30 seconds)
3. **Run Detailed Tests** (5 minutes)
4. **If passes, test other agents** (should be faster)
5. **If fails, troubleshoot** (check JSON, MCP, restart)

---

**Last Updated:** November 1, 2025
**Status:** Ready for testing!

