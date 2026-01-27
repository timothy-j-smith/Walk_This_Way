# CURSOR WORKFLOW ORCHESTRATOR MCP
## Intelligent MCP Management & Workflow Orchestration

**Status:** ✅ Ready for Testing  
**Created:** January 24, 2026  
**Purpose:** Automatically manage and orchestrate your 27 MCPs based on context

---

## 🎯 WHAT IT DOES

The Workflow Orchestrator MCP intelligently:
1. **Analyzes your tasks** to understand what you need
2. **Recommends MCPs** based on context (character, plot, style, research, code)
3. **Shows interactive checklist** with reasoning for each recommendation
4. **Enables/disables MCPs** automatically based on your approval
5. **Learns from usage** to improve recommendations over time

---

## 🚀 INSTALLATION

### Step 1: Install Dependencies

**⚠️ IMPORTANT: MCP requires Python 3.10+**

**Check Python version:**
```bash
python3 --version
```

**If Python < 3.10, install Python 3.10+:**
```bash
# Option 1: Homebrew (Recommended)
brew install python@3.10

# Option 2: Download from python.org
# https://www.python.org/downloads/
```

**Then run setup:**
```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/CURSOR_WORKFLOW_ORCHESTRATOR_MCP"

# Run setup script (automatically handles Python version)
./setup.sh
```

**Or manually:**
```bash
# Use Python 3.10+ (adjust command if needed)
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install mcp
chmod +x server.py
```

### Step 2: Add to Cursor Config

Add to `.cursor/config/mcp.json`:

```json
{
  "mcpServers": {
    "cursor-workflow-orchestrator": {
      "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/CURSOR_WORKFLOW_ORCHESTRATOR_MCP/venv/bin/python",
      "args": [
        "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/CURSOR_WORKFLOW_ORCHESTRATOR_MCP/server.py"
      ],
      "disabled": false
    }
  }
}
```

### Step 3: Restart Cursor

Restart Cursor completely for the MCP to load.

---

## 📋 AVAILABLE TOOLS

### 1. `analyze_context`
Analyzes your task/question to determine required capabilities.

**Example:**
```
Use cursor-workflow-orchestrator to analyze: "Check character consistency in Chapter 4"
```

**Returns:** Context analysis with task type, writing phase, required capabilities

---

### 2. `recommend_mcps`
Recommends MCPs based on context analysis.

**Example:**
```
Use cursor-workflow-orchestrator to recommend MCPs for character consistency check
```

**Returns:** Essential, recommended, and optional MCPs with reasoning

---

### 3. `show_checklist`
Displays interactive checklist of recommended MCPs.

**Example:**
```
Use cursor-workflow-orchestrator to show checklist for: "Check character consistency"
```

**Returns:** Markdown checklist with checkboxes and reasoning

---

### 4. `enable_mcps`
Enables selected MCPs automatically.

**Example:**
```
Use cursor-workflow-orchestrator to enable: ["knowledge-graph-memory", "dennis-lehane-style"]
```

**Returns:** Success status and list of enabled MCPs

---

### 5. `disable_mcps`
Disables MCPs automatically.

**Example:**
```
Use cursor-workflow-orchestrator to disable: ["firecrawl", "duckduckgo-search"]
```

**Returns:** Success status and list of disabled MCPs

---

### 6. `list_available_mcps`
Lists all available MCPs with their status.

**Example:**
```
Use cursor-workflow-orchestrator to list all available MCPs
```

**Returns:** Complete list of all 27+ MCPs with enabled/disabled status

---

### 7. `get_mcp_status`
Gets current status of all MCPs.

**Example:**
```
Use cursor-workflow-orchestrator to get MCP status
```

**Returns:** Summary of enabled vs disabled MCPs

---

## 🎨 EXAMPLE WORKFLOW

### Scenario: Character Consistency Check

**Step 1: Analyze Task**
```
Use cursor-workflow-orchestrator to analyze: "Check if Nick's character is consistent in Chapter 4"
```

**Step 2: Get Recommendations**
```
Use cursor-workflow-orchestrator to recommend MCPs based on that analysis
```

**Step 3: Show Checklist**
```
Use cursor-workflow-orchestrator to show checklist for character consistency check
```

**Step 4: Enable MCPs**
```
Use cursor-workflow-orchestrator to enable: ["knowledge-graph-memory", "dennis-lehane-style", "compass-writing-guides"]
```

**Step 5: Restart Cursor** (for changes to take effect)

**Step 6: Proceed with Task** (using enabled MCPs)

---

## 🧠 INTELLIGENT RECOMMENDATIONS

The Orchestrator analyzes:

- **Task Type:**
  - Character → Knowledge Graph Memory, Character Depth Coach, Dennis Lehane
  - Plot → Sequential Thinking, AI Writers Workshop
  - Style → Dennis Lehane, Style Emulation, COMPASS Guides
  - Research → Firecrawl, DuckDuckGo, Vectara
  - Code → Toolbox, Filesystem

- **Writing Phase:**
  - Drafting → Creative MCPs (Sequential Thinking, AI Writers Workshop)
  - Editing → Analysis MCPs (Character Depth Coach, Prose Polish)
  - Polishing → Style MCPs (Dennis Lehane, Style Emulation)

- **File Context:**
  - Chapter files → Character/plot MCPs
  - Story Bible → Research MCPs
  - Agent Work → Analysis MCPs

---

## 📊 LEARNING SYSTEM

The Orchestrator logs all usage to:
`.cursor/logs/orchestrator-usage.jsonl`

**Tracks:**
- Which MCPs are used for which tasks
- Success rate of recommendations
- User modifications to recommendations
- Performance metrics

**Future Enhancement:**
- Learn optimal MCP combinations
- Improve recommendation accuracy
- Reduce unnecessary activations

---

## 🔧 TECHNICAL DETAILS

**Language:** Python 3  
**Dependencies:** mcp (MCP SDK)  
**Pattern:** Follows COMPASS Writing Guides MCP structure  
**Data:** Reads/writes `.cursor/config/mcp.json`  
**Logs:** `.cursor/logs/orchestrator-usage.jsonl`

---

## ✅ STATUS

- ✅ Toolbox MCP added to config
- ✅ Orchestrator MCP server created
- ⚠️ Needs: Virtual environment setup
- ⚠️ Needs: Add to mcp.json
- ⚠️ Needs: Testing

---

**Next Steps:**
1. Set up virtual environment
2. Install dependencies
3. Add to mcp.json
4. Test with real workflows
