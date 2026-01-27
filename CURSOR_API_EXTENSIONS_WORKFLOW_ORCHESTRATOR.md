# CURSOR API/CLI, EXTENSIONS & WORKFLOW ORCHESTRATOR MCP
## Complete Research & Implementation Plan - January 24, 2026

---

## PART I: CURSOR API/CLI RESEARCH

### ✅ Cursor API Capabilities

**Based on Documentation & Research:**

1. **Model Context Protocol (MCP) - Primary API**
   - **Location:** `.cursor/config/mcp.json` (project-specific) or `~/.cursor/mcp.json` (global)
   - **Transport Types:** stdio (local commands) and SSE (remote URLs)
   - **Access:** Settings > Features > MCP > Add New MCP Server
   - **Status:** ✅ You're using this extensively (27 MCPs configured)

2. **Command Palette API**
   - **Access:** `⌘K` (Mac) or `Ctrl+K` (Windows)`
   - **All Commands:** `Cursor: Show All Commands`
   - **Status:** ✅ Available - can be automated via scripts

3. **Shell Commands Configuration**
   - **Purpose:** Execute custom shell scripts from Cursor
   - **Location:** Cursor Settings > Shell Commands
   - **Status:** ✅ Available - enables CLI automation

4. **Agent Modes & Subagents**
   - **Purpose:** Run multiple agents in parallel
   - **Access:** Via Agent system
   - **Status:** ✅ You have this configured

5. **Terminal Integration**
   - **Purpose:** Direct terminal access from Cursor
   - **Status:** ✅ Available - you're using this

6. **Browser Integration**
   - **Purpose:** Web browsing from Cursor
   - **Status:** ✅ Available

### ⚠️ CLI Command (Unverified)

**Potential CLI:**
- May exist: `cursor` command in terminal
- **Action:** Test `cursor --help` in terminal
- **If exists:** Could enable full automation

**Recommendation:** Test if `cursor` CLI exists, could unlock powerful automation

---

## PART II: BEST EXTENSIONS FOR YOUR USE CASE

### Your Use Cases:
1. **Fiction Writing** (10 independent novels)
2. **Creative Brainstorming** (blue-sky thinking)
3. **Innovation/Product Management** (work projects)

---

### 🏆 TOP EXTENSIONS FOR FICTION WRITING

#### 1. **Markdown Extensions** ⭐⭐⭐⭐⭐

**Recommended:**
- **Markdown All in One** - Comprehensive markdown support
- **Markdown Preview Enhanced** - Rich preview with diagrams
- **Markdownlint** - Linting for markdown files
- **Paste Image** - Easy image insertion in markdown

**Why:** You write in markdown, these enhance the experience

---

#### 2. **Writing & Editing Extensions** ⭐⭐⭐⭐⭐

**Recommended:**
- **Grammarly** - Grammar and style checking (you have Grammarly API MCP!)
- **ProWritingAid** - Advanced writing analysis
- **Word Count** - Track word count per file/project
- **Better Comments** - Enhanced comment highlighting
- **Todo Tree** - Track TODO items in your writing

**Why:** Professional writing support

---

#### 3. **Organization & Navigation** ⭐⭐⭐⭐⭐

**Recommended:**
- **File Utils** - Advanced file operations
- **Path Intellisense** - Autocomplete file paths
- **Bookmarks** - Mark important locations
- **Bracket Pair Colorizer** - Better code/writing navigation
- **Indent Rainbow** - Visual indentation guide

**Why:** Navigate large novel projects efficiently

---

#### 4. **Git & Version Control** ⭐⭐⭐⭐⭐

**Recommended:**
- **GitLens** - Enhanced Git capabilities
- **Git Graph** - Visual Git history
- **Git History** - File history viewer

**Why:** You use Git/GitKraken extensively

---

#### 5. **Productivity** ⭐⭐⭐⭐

**Recommended:**
- **Todo+** - Enhanced TODO management
- **Project Manager** - Manage multiple projects
- **Pomodoro Timer** - Focus sessions
- **Time Tracker** - Track writing time

**Why:** Productivity for long writing sessions

---

### 🧠 TOP EXTENSIONS FOR CREATIVE BRAINSTORMING

#### 1. **Mind Mapping & Visualization** ⭐⭐⭐⭐⭐

**Recommended:**
- **Mermaid Preview** - Create diagrams in markdown
- **Draw.io Integration** - Visual diagrams
- **PlantUML** - UML diagrams
- **Markmap** - Mind maps from markdown

**Why:** Visualize creative connections

---

#### 2. **Note-Taking & Knowledge Management** ⭐⭐⭐⭐⭐

**Recommended:**
- **Foam** - Personal knowledge management
- **Obsidian** - Knowledge base (if compatible)
- **Notion** - Note-taking integration
- **Zettelkasten** - Note linking system

**Why:** Capture and connect creative ideas

---

#### 3. **Research & Reference** ⭐⭐⭐⭐

**Recommended:**
- **Citations** - Reference management
- **Research** - Research note-taking
- **Web Clipper** - Save web content

**Why:** Research for creative projects

---

### 💼 TOP EXTENSIONS FOR INNOVATION/PRODUCT MANAGEMENT

#### 1. **Project Management** ⭐⭐⭐⭐⭐

**Recommended:**
- **Jira** - Issue tracking integration
- **Linear** - Project management
- **Trello** - Kanban boards
- **Asana** - Task management

**Why:** Manage innovation projects

---

#### 2. **Documentation** ⭐⭐⭐⭐⭐

**Recommended:**
- **Markdown PDF** - Export to PDF
- **Docs View** - Documentation viewer
- **API Documentation Generator** - Auto-generate docs

**Why:** Document innovation work

---

#### 3. **Data & Analysis** ⭐⭐⭐⭐

**Recommended:**
- **CSV Viewer** - Data analysis
- **JSON Tools** - JSON manipulation
- **YAML** - YAML support

**Why:** Analyze product data

---

## PART III: WORKFLOW ORCHESTRATOR CUSTOM MCP

### 🎯 Core Concept

**Purpose:** Automatically orchestrate your 27 MCPs based on context, task, and workflow phase.

---

### 📋 Architecture Overview

```
┌─────────────────────────────────────────────────┐
│     Cursor Workflow Orchestrator MCP            │
├─────────────────────────────────────────────────┤
│                                                  │
│  1. Context Analyzer                            │
│     - Analyzes current task/question            │
│     - Identifies writing phase                  │
│     - Determines required capabilities          │
│                                                  │
│  2. MCP Recommender                              │
│     - Recommends MCPs based on context          │
│     - Suggests optimal MCP combinations         │
│     - Provides reasoning for recommendations    │
│                                                  │
│  3. Interactive Checklist                        │
│     - Shows recommended MCPs with checkboxes   │
│     - Allows user approval/modification         │
│     - Tracks user preferences                   │
│                                                  │
│  4. Dynamic Enable/Disable                      │
│     - Enables selected MCPs automatically      │
│     - Disables unused MCPs                     │
│     - Updates mcp.json dynamically              │
│                                                  │
│  5. Workflow Execution                          │
│     - Chains MCPs in optimal sequence          │
│     - Manages state across MCP calls            │
│     - Handles errors and retries                │
│                                                  │
│  6. Performance Monitor                         │
│     - Tracks MCP usage                          │
│     - Measures effectiveness                   │
│     - Learns from patterns                     │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

### 🔧 MCP Tools (Functions)

#### 1. **analyze_context**
- **Purpose:** Analyze current task/question
- **Input:** User query, current file, writing phase
- **Output:** Context analysis, required capabilities
- **Example:** "User is editing Chapter 4, needs character consistency check"

#### 2. **recommend_mcps**
- **Purpose:** Recommend MCPs based on context
- **Input:** Context analysis
- **Output:** List of recommended MCPs with reasoning
- **Example:** "For character consistency: Knowledge Graph Memory, Character Depth Coach, Dennis Lehane MCP"

#### 3. **show_checklist**
- **Purpose:** Display interactive checklist
- **Input:** Recommended MCPs
- **Output:** Checklist UI with checkboxes
- **Example:** 
  ```
  ☑ Knowledge Graph Memory MCP (Recommended: Character consistency)
  ☑ Character Depth Coach MCP (Recommended: Character analysis)
  ☐ Firecrawl MCP (Optional: Research if needed)
  ☐ Sequential Thinking MCP (Optional: Complex reasoning)
  ```

#### 4. **enable_mcps**
- **Purpose:** Enable selected MCPs
- **Input:** List of MCP names to enable
- **Output:** Updated mcp.json with enabled MCPs
- **Action:** Sets `"disabled": false` for selected MCPs

#### 5. **disable_mcps**
- **Purpose:** Disable unused MCPs
- **Input:** List of MCP names to disable
- **Output:** Updated mcp.json with disabled MCPs
- **Action:** Sets `"disabled": true` for selected MCPs

#### 6. **execute_workflow**
- **Purpose:** Execute MCP workflow
- **Input:** List of enabled MCPs, workflow steps
- **Output:** Workflow results
- **Action:** Chains MCP calls in sequence

#### 7. **monitor_performance**
- **Purpose:** Track MCP usage and effectiveness
- **Input:** MCP usage logs
- **Output:** Performance metrics, recommendations
- **Action:** Learns which MCPs work best for which tasks

---

### 📝 Implementation Details

#### MCP Configuration File Management

**Location:** `.cursor/config/mcp.json`

**Strategy:**
1. **Default State:** All MCPs start with `"disabled": true` (except essential ones)
2. **On Task Start:** 
   - User asks question or starts task
   - Workflow Orchestrator analyzes context
   - Recommends MCPs
   - Shows checklist
   - User approves/modifies
   - Enables selected MCPs
3. **On Task Complete:**
   - Optionally disables MCPs
   - Logs usage for learning

**Example mcp.json Structure:**
```json
{
  "mcpServers": {
    "walk-this-way-files": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "..."],
      "disabled": false  // Essential, always enabled
    },
    "knowledge-graph-memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"],
      "disabled": true  // Disabled by default
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {"FIRECRAWL_API_KEY": "env:FIRECRAWL_API_KEY"},
      "disabled": true  // Disabled by default
    }
    // ... all other MCPs with "disabled": true by default
  }
}
```

---

### 🎨 Interactive Checklist System (Your Original Vision!)

#### Checklist Format (Exactly As You Described)

**Display in Cursor Chat:**
```
┌─────────────────────────────────────────────────────┐
│  MCP Activation Recommendations                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Based on your task: "Check character consistency" │
│                                                      │
│  ☑ Knowledge Graph Memory MCP                      │
│    └─ Reason: Stores character data and relationships│
│                                                      │
│  ☑ Character Depth Coach MCP                       │
│    └─ Reason: Analyzes character consistency        │
│                                                      │
│  ☑ Dennis Lehane MCP                                │
│    └─ Reason: Style consistency check                          │
│                                                      │
│  ☐ Firecrawl MCP                                    │
│    └─ Reason: Optional - research if needed         │
│                                                      │
│  ☐ Sequential Thinking MCP                          │
│    └─ Reason: Optional - complex reasoning          │
│                                                      │
│  [Approve Selected] [Add More] [Modify] [Cancel]   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**How It Works (Your Original Concept):**
1. **All MCPs start disabled** (except essential: filesystem)
2. **You ask a question** → "Check character consistency in Chapter 4"
3. **Cursor Claude analyzes** → Identifies needed capabilities
4. **Shows checklist** → Recommended MCPs with checkboxes
5. **You approve/modify** → Check/uncheck boxes, add more if needed
6. **MCPs activate** → Selected MCPs enabled automatically
7. **Task proceeds** → Uses enabled MCPs for the task

#### User Interaction Flow

1. **User asks question or starts task**
2. **Workflow Orchestrator analyzes:**
   - Current file/chapter
   - Writing phase (drafting/editing/polishing)
   - Task type (character/plot/research/style)
   - Required capabilities
3. **Generates recommendations:**
   - Essential MCPs (pre-checked)
   - Recommended MCPs (pre-checked)
   - Optional MCPs (unchecked)
4. **Shows checklist:**
   - User can check/uncheck
   - User can add additional MCPs
   - User can see reasoning for each
5. **User approves:**
   - Workflow Orchestrator enables selected MCPs
   - Updates mcp.json
   - Restarts MCP connections (if needed)
6. **Task execution:**
   - Uses enabled MCPs
   - Chains them in optimal sequence
7. **Task complete:**
   - Optionally disables MCPs
   - Logs usage for learning

---

### 🧠 Intelligent Recommendation Engine

#### Context Analysis

**Factors Considered:**
1. **Current File:**
   - Chapter file → Character/plot MCPs
   - Story Bible → Research MCPs
   - Agent Work → Analysis MCPs

2. **Writing Phase:**
   - Drafting → Creative MCPs (Sequential Thinking, AI Writers Workshop)
   - Editing → Analysis MCPs (Character Depth Coach, Prose Polish)
   - Polishing → Style MCPs (Dennis Lehane, Style Emulation)

3. **Task Type:**
   - Character → Knowledge Graph Memory, Character Depth Coach
   - Plot → Sequential Thinking, Firecrawl (research)
   - Style → Dennis Lehane, Style Emulation
   - Research → Firecrawl, DuckDuckGo, Vectara

4. **Question Keywords:**
   - "character" → Character MCPs
   - "research" → Research MCPs
   - "style" → Style MCPs
   - "plot" → Plot/Structure MCPs

#### Recommendation Logic

```python
def recommend_mcps(context):
    recommendations = {
        "essential": [],
        "recommended": [],
        "optional": []
    }
    
    # Character-related tasks
    if "character" in context.task.lower():
        recommendations["essential"].append("knowledge-graph-memory")
        recommendations["essential"].append("character-depth-coach")
        recommendations["recommended"].append("dennis-lehane-style")
    
    # Research tasks
    if "research" in context.task.lower() or "fact" in context.task.lower():
        recommendations["essential"].append("firecrawl")
        recommendations["recommended"].append("duckduckgo-search")
        recommendations["recommended"].append("vectara")
    
    # Style tasks
    if "style" in context.task.lower() or "voice" in context.task.lower():
        recommendations["essential"].append("dennis-lehane-style")
        recommendations["essential"].append("style-emulation")
        recommendations["recommended"].append("compass-writing-guides")
    
    # Complex reasoning
    if context.complexity == "high":
        recommendations["recommended"].append("sequential-thinking")
        recommendations["recommended"].append("sequential-thinking-ultra")
    
    return recommendations
```

---

### 📊 Learning & Optimization

#### Usage Tracking

**Track:**
- Which MCPs are used for which tasks
- Success rate of recommendations
- User modifications to recommendations
- Performance metrics (speed, accuracy)

**Learn:**
- Which MCP combinations work best
- User preferences over time
- Task patterns and optimal MCP sets

**Optimize:**
- Improve recommendation accuracy
- Reduce unnecessary MCP activations
- Speed up workflow execution

---

## PART IV: AUTOMATED MCP ENABLE/DISABLE SYSTEM

### ✅ CONFIRMED: This System Was Discussed!

**Found in your codebase:** `MCP_ORCHESTRATION_STRATEGY.md` (January 17, 2026)

**You discussed exactly this system:**
1. **All MCPs start disabled** (except essential ones like filesystem)
2. **Task-specific MCP configurations** - Different blends for different tasks
3. **Smart defaults** - Essential MCPs always on, others toggleable
4. **Profile-based switching** - Writing mode, Commit mode, Planning mode, Research mode

**Your Original Vision (Now Enhanced):**
1. **All MCPs start disabled** (except essential ones)
2. **Cursor Claude analyzes the task/question**
3. **Recommends MCPs to activate** (with reasoning)
4. **Shows interactive checklist** (with checkboxes)
5. **User approves/modifies** (can add/remove recommendations)
6. **MCPs are enabled/disabled dynamically** (updates mcp.json)
7. **Workflow executes** (with enabled MCPs)
8. **Learning system** (tracks what works best)

### 🔧 Implementation Strategy

#### Step 1: Default Configuration

**Modify `.cursor/config/mcp.json`:**
- Set all non-essential MCPs to `"disabled": true`
- Keep only essential MCPs enabled:
  - `walk-this-way-files` (always needed)
  - `github` (if using Git)
  - `gitkraken` (if using GitKraken)

#### Step 2: Workflow Orchestrator MCP

**Build MCP with these tools:**
1. `analyze_task` - Analyzes user question/task
2. `recommend_mcps` - Recommends MCPs based on analysis
3. `show_checklist` - Displays interactive checklist
4. `enable_mcps` - Enables selected MCPs
5. `disable_mcps` - Disables unused MCPs
6. `update_mcp_config` - Updates mcp.json file

#### Step 3: Integration with Cursor

**How it works:**
1. User asks question in Cursor chat
2. Workflow Orchestrator MCP analyzes question
3. Recommends MCPs
4. Shows checklist in chat (markdown format with checkboxes)
5. User responds with selections
6. MCPs are enabled/disabled
7. Cursor reloads MCP configuration
8. Task proceeds with enabled MCPs

---

### 📝 Example Workflow

**User:** "I need to check if Nick's character is consistent in Chapter 4"

**Workflow Orchestrator Analysis:**
- Task: Character consistency check
- File: Chapter 4
- Required: Character data, analysis tools

**Recommendations:**
```
┌─────────────────────────────────────────────────┐
│ MCP Activation Recommendations                  │
├─────────────────────────────────────────────────┤
│ Task: Character consistency check              │
│                                                  │
│ ☑ Knowledge Graph Memory MCP                   │
│   └─ Stores character data and relationships   │
│                                                  │
│ ☑ Character Depth Coach MCP                    │
│   └─ Analyzes character consistency            │
│                                                  │
│ ☑ Dennis Lehane MCP                             │
│   └─ Style consistency check                    │
│                                                  │
│ ☐ Firecrawl MCP                                │
│   └─ Optional - research if needed             │
│                                                  │
│ Type: "approve" or modify selections           │
└─────────────────────────────────────────────────┘
```

**User:** "approve"

**Workflow Orchestrator:**
1. Enables: Knowledge Graph Memory, Character Depth Coach, Dennis Lehane
2. Updates mcp.json
3. Notifies Cursor to reload MCPs
4. Proceeds with character consistency check

---

## PART V: IMPLEMENTATION PLAN

### Phase 1: Research & Design (Week 1)
- [x] Research Cursor API/CLI capabilities
- [x] Identify best extensions
- [x] Design Workflow Orchestrator architecture
- [ ] Verify MCP enable/disable automation approach

### Phase 2: Build Workflow Orchestrator MCP (Week 2-3)
- [ ] Create MCP server structure
- [ ] Implement context analyzer
- [ ] Implement recommendation engine
- [ ] Implement checklist system
- [ ] Implement enable/disable functionality
- [ ] Test with your 27 MCPs

### Phase 3: Integration & Testing (Week 4)
- [ ] Integrate with Cursor
- [ ] Test workflow scenarios
- [ ] Optimize recommendations
- [ ] Add learning/optimization

### Phase 4: Extension Installation (Week 1-2)
- [ ] Install markdown extensions
- [ ] Install writing extensions
- [ ] Install organization extensions
- [ ] Install creative brainstorming extensions
- [ ] Install product management extensions

---

## 🎯 NEXT STEPS

1. **Test Cursor CLI** - Check if `cursor` command exists
2. **Install Top Extensions** - Start with markdown and writing extensions
3. **Build Workflow Orchestrator MCP** - Begin implementation
4. **Modify mcp.json** - Set non-essential MCPs to disabled by default
5. **Test Workflow** - Try the automated enable/disable system

---

**Created:** January 24, 2026  
**Status:** Ready for implementation  
**Priority:** High - This is your path to Super Agent status
