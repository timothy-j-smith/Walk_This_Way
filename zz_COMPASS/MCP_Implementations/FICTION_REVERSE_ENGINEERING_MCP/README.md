# FICTION REVERSE ENGINEERING MCP
## Extract Structural DNA from Bestsellers

**Status:** ✅ Ready for Setup  
**Created:** January 24, 2026  
**Purpose:** Learn from bestsellers through mathematical analysis

---

## ⚠️ CRITICAL PHILOSOPHY

**This MCP is a LEARNING TOOL, NOT A FORMULA**

- ✅ Use to understand patterns in bestsellers
- ✅ Learn pacing techniques mathematically
- ✅ Compare your work objectively
- ✅ Extract insights for improvement
- ❌ DO NOT copy formulas blindly
- ❌ DO NOT replace creative intuition
- ❌ DO NOT force writing into rigid patterns

**See `USAGE_GUIDELINES.md` for complete usage instructions.**

---

## 🚀 INSTALLATION

### Step 1: Install Dependencies

```bash
cd "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/FICTION_REVERSE_ENGINEERING_MCP"

# Create virtual environment (use Python 3.10+)
python3.10 -m venv venv
source venv/bin/activate

# Install MCP SDK
pip install --upgrade pip
pip install mcp

# Make server executable
chmod +x server.py
```

### Step 2: Add to Cursor Config

Add to `.cursor/config/mcp.json`:

```json
{
  "mcpServers": {
    "fiction-reverse-engineering": {
      "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/FICTION_REVERSE_ENGINEERING_MCP/venv/bin/python",
      "args": [
        "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/FICTION_REVERSE_ENGINEERING_MCP/server.py"
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

### 1. `reverse_engineer_novel`
Reverse engineer a bestselling novel to extract its structural formula.

**⚠️ Use for LEARNING, not copying**

**Example:**
```
Use fiction-reverse-engineering to reverse engineer "Mystic River" by Dennis Lehane
```

**Returns:** Structural analysis with extracted formula

---

### 2. `compare_to_bestseller`
Compare your writing to a reverse-engineered bestseller formula.

**⚠️ Use for DIAGNOSTIC analysis or REFINEMENT, not during creative drafting**

**Example:**
```
Use fiction-reverse-engineering to compare Chapter 4 to "Mystic River" formula
```

**Returns:** Detailed comparison with actionable suggestions

---

### 3. `analyze_pacing`
Analyze pacing mathematically - tension curves, reveal frequency.

**⚠️ Use for OBJECTIVE analysis during revision, not during creative flow**

**Example:**
```
Use fiction-reverse-engineering to analyze pacing in Chapter 4
```

**Returns:** Pacing analysis with metrics

---

### 4. `extract_dialogue_formula`
Extract dialogue patterns - rhythm, beat patterns, tag usage.

**⚠️ Learn patterns, then adapt to your voice**

**Example:**
```
Use fiction-reverse-engineering to extract dialogue formula from Chapter 4
```

**Returns:** Dialogue formula with examples

---

### 5. `find_chapter_formula`
Extract chapter-level formulas - structure, hooks, cliffhangers.

**⚠️ Understand patterns, maintain variety**

**Example:**
```
Use fiction-reverse-engineering to find chapter formula for Chapter 4
```

**Returns:** Chapter formula with patterns

---

### 6. `list_available_formulas`
List all reverse-engineered bestseller formulas available.

**Example:**
```
Use fiction-reverse-engineering to list available formulas
```

**Returns:** List of all saved formulas

---

## 🎯 WHEN TO USE

### ✅ APPROPRIATE:
- Learning from bestsellers
- Diagnostic analysis (something feels off)
- Revision phase (polishing)
- Quality assurance (final check)

### ❌ INAPPROPRIATE:
- During creative drafting
- For every decision
- To copy bestsellers
- Instead of your voice

**See `USAGE_GUIDELINES.md` for complete guidance.**

---

## 🔄 INTEGRATION

### Works With:
- **Structural Perfection Specialist** - Qualitative + Quantitative analysis
- **AI Writers Workshop MCP** - Narrative guidance + Pattern analysis
- **COMPASS Writing Guides** - Techniques + Formulas
- **Sequential Thinking MCPs** - Logic validation

### Workflow:
1. **Creative Drafting:** Use your intuition + Creative Collaborator
2. **Analysis:** Use Structural Perfection Specialist + Reverse Engineering MCP
3. **Revision:** Use all tools together
4. **Polish:** Use Reverse Engineering MCP for final verification

---

## 📊 EXAMPLE WORKFLOW

### Learning from Masters:

**Step 1: Reverse Engineer**
```
Use fiction-reverse-engineering to reverse engineer "Mystic River" by Dennis Lehane
```

**Step 2: Study Formula**
- Review extracted patterns
- Understand pacing structure
- Learn dialogue techniques

**Step 3: Apply Insights**
- Use insights to inform your writing
- Adapt patterns to your voice
- Don't copy formulas

---

### Diagnostic Analysis:

**Step 1: Identify Issue**
- Something feels off in Chapter 4

**Step 2: Compare**
```
Use fiction-reverse-engineering to compare Chapter 4 to "Mystic River" formula
```

**Step 3: Fix Issues**
- Review deviations
- Apply recommendations
- Maintain your voice

---

## 🛡️ SAFEGUARDS

### Built-in Warnings:
- Every tool response includes usage warnings
- Formulas include learning tool disclaimers
- Comparisons emphasize maintaining voice

### Usage Limits:
- Don't use for every chapter
- Don't use during creative flow
- Use for analysis and refinement
- Always prioritize your voice

---

## 📝 TECHNICAL DETAILS

**Language:** Python 3.10+  
**Dependencies:** mcp (MCP SDK)  
**Pattern:** Follows COMPASS Writing Guides MCP structure  
**Data:** Stores formulas in `data/formulas/`  
**Logs:** Analysis results saved as JSON

---

## ✅ STATUS

- ✅ Server created
- ✅ Usage guidelines created
- ⚠️ Needs: Virtual environment setup
- ⚠️ Needs: Add to mcp.json
- ⚠️ Needs: Testing

---

**Next Steps:**
1. Set up virtual environment
2. Install dependencies
3. Add to mcp.json
4. Test with real bestseller
5. Use appropriately (see guidelines)

---

**Remember:** This is a learning tool. Use to understand patterns, not to copy formulas. Maintain your unique voice.
