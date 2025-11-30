# CUSTOM AGENT LIMIT STRATEGY

**Cursor Only Allows 5 Custom Agents in Dropdown - Here's How to Handle 9 Agents**

---

## 🎯 THE PROBLEM:

- ✅ You have **9 agents** set up
- ❌ Cursor dropdown only allows **5 custom agents**
- ⚠️ Need to prioritize which 5 go in dropdown
- ✅ Other 4 can still be accessed via @ mentions

---

## 📋 RECOMMENDED: TOP 5 FOR DROPDOWN

### **Priority 1: Most Frequently Used**

1. **CREATIVE_COLLABORATOR**
   - Hands-on rewriting partner
   - Most used for actual prose work
   - Advanced Tools Expert
   - **USE:** Daily writing and rewriting

2. **STRATEGIC_WRITING_COORDINATOR**
   - Workflow orchestrator
   - Coordinates other agents
   - Strategic oversight
   - **USE:** Chapter analysis, workflow planning

3. **JAZZ**
   - Creative Thought Partner
   - Discovery and exploration
   - Hidden superpowers
   - **USE:** Tool discovery, technical questions, experimentation

4. **HANK**
   - COMPASS Super Agent
   - Technical architect
   - Strategic partner
   - **USE:** System architecture, technical troubleshooting

5. **CAROLINA**
   - Technical Systems Expert
   - Patient teacher
   - Git/MCP expert
   - **USE:** Technical setup, Git issues, MCP configuration

---

## 📋 ACCESS VIA @ MENTIONS (Other 4 Agents)

These agents are still fully functional via @ mentions:

### **Specialized Writing Agents:**

1. **CHARACTER_DEPTH_COACH**
   ```
   @.cursor/agents/CHARACTER_DEPTH_COACH.json
   ```
   - Character development and voice consistency
   - Use when: Character work needed, voice issues

2. **PROSE_POLISH_EXPERT**
   ```
   @.cursor/agents/PROSE_POLISH_EXPERT.json
   ```
   - Sentence-level refinement
   - Use when: Prose polish needed, word choice issues

3. **STRUCTURAL_PERFECTION_SPECIALIST**
   ```
   @.cursor/agents/STRUCTURAL_PERFECTION_SPECIALIST.json
   ```
   - Pacing and structure
   - Use when: Structural analysis needed, pacing issues

4. **Agent (Master Orchestration)**
   ```
   @.cursor/agents/Agent.json
   ```
   - Master reference document
   - Use when: Need project vision, themes, character info
   - **Note:** Other agents reference this automatically

---

## 🎯 DECISION MATRIX

### **Use Dropdown For:**
- ✅ Daily writing work (Creative Collaborator)
- ✅ Workflow coordination (Strategic Coordinator)
- ✅ Tool discovery (JAZZ)
- ✅ Technical issues (HANK, CAROLINA)
- ✅ Quick access to most-used agents

### **Use @ Mentions For:**
- ✅ Specialized analysis (Character, Prose, Structural)
- ✅ One-time deep dives
- ✅ When you need specific expertise
- ✅ Combining multiple agents in one chat

---

## 🔧 RECOMMENDED WORKFLOW

### **Daily Writing:**
1. **Start with Strategic Coordinator** (dropdown)
   - Analyze chapter, recommend approach
2. **Switch to Creative Collaborator** (dropdown)
   - Do actual rewriting work
3. **If stuck, use JAZZ** (dropdown)
   - Explore solutions, find hidden features

### **Specialized Work:**
1. **Use @ mentions** for specialized agents:
   ```
   @.cursor/agents/CHARACTER_DEPTH_COACH.json
   Analyze Chapter 5 for character consistency
   ```

### **Technical Issues:**
1. **Use HANK or CAROLINA** (dropdown)
   - System architecture (HANK)
   - Git/MCP setup (CAROLINA)

---

## 📝 ALTERNATIVE: ROTATE AGENTS

**Option:** Rotate which 5 are in dropdown based on current needs

**Week 1 (Writing Phase):**
- Creative Collaborator
- Strategic Coordinator
- Character Coach
- Prose Expert
- Structural Specialist

**Week 2 (Discovery Phase):**
- JAZZ
- HANK
- CAROLINA
- Creative Collaborator
- Strategic Coordinator

**Note:** This requires updating Settings, but gives flexibility

---

## ✅ RECOMMENDED SETUP

### **Top 5 in Dropdown (Recommended):**

1. **Creative Collaborator** - Daily writing
2. **Strategic Coordinator** - Workflow
3. **JAZZ** - Discovery & exploration
4. **HANK** - Technical architect
5. **CAROLINA** - Technical systems

### **Access Others Via @ Mentions:**
- Character Coach: `@.cursor/agents/CHARACTER_DEPTH_COACH.json`
- Prose Expert: `@.cursor/agents/PROSE_POLISH_EXPERT.json`
- Structural Specialist: `@.cursor/agents/STRUCTURAL_PERFECTION_SPECIALIST.json`
- Agent (Master): `@.cursor/agents/Agent.json` (auto-referenced by others)

---

## 🎯 QUICK REFERENCE

### **Dropdown Agents (5):**
- Creative Collaborator
- Strategic Coordinator
- JAZZ
- HANK
- CAROLINA

### **@ Mention Agents (4):**
- Character Coach
- Prose Expert
- Structural Specialist
- Agent (Master)

---

## 💡 KEY INSIGHT

**The dropdown is for convenience, not limitation.**

- ✅ All 9 agents are fully functional
- ✅ Dropdown = Quick access to most-used
- ✅ @ Mentions = Access to specialized agents
- ✅ Both methods work equally well

**You're not losing functionality - you're just organizing access!**

---

**Last Updated:** November 1, 2025
**Status:** Strategy for handling 5-agent limit while maintaining access to all 9 agents

