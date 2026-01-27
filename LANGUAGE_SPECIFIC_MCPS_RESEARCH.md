# LANGUAGE-SPECIFIC MCPS RESEARCH
## For Workflow Orchestrator MCP - January 24, 2026

**Purpose:** Research MCPs for Python, JSON, JavaScript, Markdown, and other languages/LLMs before building the Orchestrator

---

## EXECUTIVE SUMMARY

**Key Finding:** Language-specific MCPs are **limited** - most MCPs focus on integration/orchestration rather than direct language tooling.

**Strategy:** Build Workflow Orchestrator to **wrap CLI tools** and **orchestrate existing MCPs** rather than waiting for language-specific MCPs.

---

## PART I: AVAILABLE LANGUAGE-SPECIFIC MCPS

### ✅ Python MCPs

#### 1. **Pandoc MCP** ⭐⭐⭐⭐⭐ (YOU HAVE THIS!)
- **Package:** `mcp-pandoc` (via uvx)
- **Status:** ✅ Installed in your config
- **Capabilities:**
  - Document conversion (Markdown → DOCX, PDF, HTML, etc.)
  - Python-based (uses uvx)
  - Handles multiple formats
- **Use Case:** Converting novel drafts to different formats
- **Verdict:** ✅ **KEEP** - Already installed and useful

#### 2. **Python Execution MCPs** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No dedicated Python execution/linting MCPs found
- **Gap:** No MCP for:
  - Python code execution
  - Linting (pylint, flake8)
  - Formatting (black, autopep8)
  - Package management (pip, poetry)
- **Recommendation:** Build custom Python MCP or wrap CLI tools

#### 3. **Custom Python MCPs** (You Have These!)
- **COMPASS Writing Guides MCP** - Python-based ✅
- **Dennis Lehane MCP** - Python-based ✅
- **Style Emulation MCP** - Python-based ✅
- **Cognee MCP** - Python-based ✅
- **UltraRAG** - Python-based ✅
- **RAGentA** - Python-based ✅

**Verdict:** You're already using Python extensively for custom MCPs!

---

### ✅ JSON MCPs

#### 1. **JSON Validation/Manipulation** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No dedicated JSON MCPs found
- **Gap:** No MCP for:
  - JSON validation
  - JSON formatting/pretty-printing
  - JSON schema validation
  - JSON transformation
- **Recommendation:** 
  - Use Filesystem MCP to read/write JSON
  - Wrap `jq` CLI tool in custom MCP
  - Use Python MCP (when built) for JSON manipulation

#### 2. **JSON in Existing MCPs** ✅
- **Filesystem MCP** - Can read/write JSON files ✅
- **All MCPs** - Use JSON for configuration ✅
- **Your Config Files** - Already JSON-based ✅

**Verdict:** JSON handling is embedded in existing MCPs, but no dedicated JSON MCP exists.

---

### ✅ JavaScript/TypeScript MCPs

#### 1. **Node.js MCP Infrastructure** ⭐⭐⭐⭐⭐
- **Status:** ✅ **EXTENSIVE** - Most MCPs are Node.js-based
- **Examples:**
  - Sequential Thinking MCP (Node.js)
  - GitHub MCP (Node.js)
  - DuckDuckGo Search MCP (Node.js)
  - Firecrawl MCP (Node.js)
  - Vectara MCP (Node.js)
  - Most npm-installed MCPs (Node.js)
- **Capabilities:** 
  - JavaScript execution (via Node.js)
  - npm package management
  - TypeScript support (if configured)
- **Verdict:** ✅ **STRONG** - JavaScript ecosystem is well-supported

#### 2. **JavaScript-Specific Tools** ⚠️
- **Status:** ⚠️ **LIMITED** - No dedicated JS linting/formatting MCPs
- **Gap:** No MCP for:
  - ESLint
  - Prettier
  - TypeScript compilation
  - npm/yarn package management
- **Recommendation:** Wrap CLI tools or use Node.js MCP infrastructure

---

### ✅ Markdown MCPs

#### 1. **Pandoc MCP** ⭐⭐⭐⭐⭐ (YOU HAVE THIS!)
- **Package:** `mcp-pandoc` (via uvx)
- **Status:** ✅ Installed in your config
- **Capabilities:**
  - Markdown → DOCX, PDF, HTML, EPUB, etc.
  - Markdown validation
  - Format conversion
- **Use Case:** Converting novel drafts, documentation
- **Verdict:** ✅ **KEEP** - Already installed and perfect for your use case

#### 2. **Markdown Processing** ⚠️
- **Status:** ⚠️ **LIMITED** - No dedicated Markdown processing MCPs
- **Gap:** No MCP for:
  - Markdown linting (markdownlint)
  - Markdown formatting
  - Markdown table generation
  - Markdown TOC generation
- **Recommendation:** 
  - Use Pandoc MCP (you have it!)
  - Wrap markdownlint CLI tool
  - Use Filesystem MCP for Markdown file operations

---

### ✅ Other Languages

#### 1. **Go** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No Go-specific MCPs
- **Recommendation:** Wrap `go` CLI tools if needed

#### 2. **Rust** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No Rust-specific MCPs
- **Recommendation:** Wrap `cargo` CLI tools if needed

#### 3. **Shell/Bash** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No shell-specific MCPs
- **Note:** Most MCPs execute shell commands internally
- **Recommendation:** Use Toolbox MCP or wrap shell scripts

---

## PART II: LLM-SPECIFIC MCPS

### ✅ LLM Integration MCPs

#### 1. **Zen Orchestrator MCP** ⭐⭐⭐⭐⭐ (YOU HAVE THIS!)
- **Status:** ✅ Installed in your config
- **Capabilities:**
  - Routes tasks to optimal AI models (GPT-4, Gemini Pro, O3)
  - Multi-model orchestration
  - Model selection based on task
- **Verdict:** ✅ **KEEP** - Perfect for LLM orchestration

#### 2. **Anthropic/Claude MCPs** ⭐⭐⭐⭐⭐
- **Sequential Thinking MCP** - Official Anthropic ✅
- **Knowledge Graph Memory MCP** - Official Anthropic ✅
- **Filesystem MCP** - Official Anthropic ✅
- **GitHub MCP** - Official Anthropic ✅
- **DuckDuckGo Search MCP** - Official Anthropic ✅
- **Status:** ✅ You have all 5 official Anthropic MCPs

#### 3. **OpenAI MCPs** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No dedicated OpenAI MCPs found
- **Note:** Zen Orchestrator can route to OpenAI models
- **Recommendation:** Use Zen Orchestrator for OpenAI access

#### 4. **Google/Gemini MCPs** ⚠️
- **Status:** ⚠️ **NOT FOUND** - No dedicated Gemini MCPs found
- **Note:** Zen Orchestrator can route to Gemini models
- **Recommendation:** Use Zen Orchestrator for Gemini access

---

## PART III: RECOMMENDATIONS FOR ORCHESTRATOR

### 🎯 Strategy: Wrap CLI Tools + Orchestrate Existing MCPs

**Instead of waiting for language-specific MCPs, build Orchestrator to:**

1. **Wrap CLI Tools:**
   - Python: `pylint`, `black`, `pytest`
   - JSON: `jq`, `jsonlint`
   - JavaScript: `eslint`, `prettier`, `npm`
   - Markdown: `markdownlint`, `pandoc` (you have this!)
   - Shell: Direct shell command execution

2. **Orchestrate Existing MCPs:**
   - Use Filesystem MCP for file operations
   - Use Pandoc MCP for Markdown conversion
   - Use Zen Orchestrator for LLM routing
   - Chain MCPs for complex workflows

3. **Build Custom Language MCPs (If Needed):**
   - Python Execution MCP
   - JSON Validation MCP
   - Markdown Processing MCP

---

### 📋 Recommended MCPs to Add

#### High Priority (For Orchestrator):

1. **Toolbox MCP** ⭐⭐⭐⭐⭐
   - **Purpose:** Command execution, API integration, file operations
   - **Why:** Enables wrapping CLI tools
   - **Status:** ⚠️ **NOT INSTALLED** - Should add
   - **Action:** Add to mcp.json

2. **Keep Existing Language MCPs:**
   - ✅ Pandoc MCP (Markdown conversion)
   - ✅ Zen Orchestrator (LLM routing)
   - ✅ Filesystem MCP (File operations)
   - ✅ All Python-based custom MCPs

#### Medium Priority:

3. **Custom Python Execution MCP** ⭐⭐⭐⭐
   - **Purpose:** Execute Python code, lint, format
   - **Why:** Direct Python support
   - **Status:** ⚠️ **NEEDS BUILDING** - Custom MCP
   - **Action:** Build as part of Orchestrator

4. **Custom JSON Validation MCP** ⭐⭐⭐
   - **Purpose:** Validate, format, transform JSON
   - **Why:** JSON is everywhere in configs
   - **Status:** ⚠️ **NEEDS BUILDING** - Custom MCP
   - **Action:** Build as part of Orchestrator

---

## PART IV: INTEGRATION WITH ORCHESTRATOR

### How Language MCPs Fit Into Orchestrator

**Workflow Orchestrator MCP will:**

1. **Detect Language:**
   - Analyze file extension (.py, .js, .json, .md)
   - Detect task type (linting, formatting, execution)
   - Recommend appropriate MCPs/tools

2. **Route to Language Tools:**
   - Python task → Python Execution MCP (when built) or CLI wrapper
   - JSON task → JSON Validation MCP (when built) or jq wrapper
   - Markdown task → Pandoc MCP (you have it!)
   - JavaScript task → Node.js execution or CLI wrapper

3. **Chain Language MCPs:**
   - Markdown → Pandoc → DOCX conversion
   - Python → Lint → Format → Execute
   - JSON → Validate → Transform → Write

4. **Enable/Disable Based on Task:**
   - Writing task → Enable Pandoc, Markdown tools
   - Code task → Enable Python, JavaScript tools
   - Config task → Enable JSON tools

---

## PART V: ACTION PLAN

### Before Building Orchestrator:

1. **Add Toolbox MCP** ⭐⭐⭐⭐⭐
   - Enables CLI tool wrapping
   - Critical for language support
   - **Action:** Add to mcp.json

2. **Keep Existing Language MCPs:**
   - ✅ Pandoc MCP (Markdown)
   - ✅ Zen Orchestrator (LLM)
   - ✅ Filesystem MCP (All files)
   - ✅ All Python custom MCPs

### During Orchestrator Build:

3. **Build Language Tool Wrappers:**
   - Python execution wrapper
   - JSON validation wrapper
   - Markdown linting wrapper
   - JavaScript execution wrapper

4. **Integrate with Existing MCPs:**
   - Chain Pandoc for Markdown
   - Use Filesystem for file ops
   - Route to Zen for LLM tasks

### After Orchestrator Build:

5. **Build Custom Language MCPs (If Needed):**
   - Only if CLI wrappers insufficient
   - Focus on most-used languages first
   - Python and JSON are highest priority

---

## FINAL RECOMMENDATIONS

### ✅ Add to mcp.json:

```json
{
  "toolbox": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-toolbox"],
    "disabled": false
  }
}
```

### ✅ Keep Existing:

- Pandoc MCP (Markdown conversion)
- Zen Orchestrator (LLM routing)
- Filesystem MCP (File operations)
- All Python-based custom MCPs

### ⚠️ Build as Part of Orchestrator:

- Python execution wrapper
- JSON validation wrapper
- Language detection logic
- CLI tool integration

---

## SUMMARY

**Language-Specific MCPs Status:**
- ✅ **Markdown:** Pandoc MCP (you have it!)
- ✅ **LLM:** Zen Orchestrator (you have it!)
- ✅ **JavaScript:** Node.js infrastructure (extensive)
- ⚠️ **Python:** Custom MCPs exist, but no execution MCP
- ⚠️ **JSON:** No dedicated MCP, but can use Filesystem
- ⚠️ **Other Languages:** Limited or none

**Strategy:**
1. Add Toolbox MCP for CLI tool wrapping
2. Build Orchestrator with language detection
3. Wrap CLI tools for Python, JSON, JavaScript
4. Chain existing MCPs (Pandoc, Filesystem, Zen)
5. Build custom language MCPs only if needed

**Verdict:** You're well-positioned! Add Toolbox MCP, then build Orchestrator with language tool wrappers.

---

**Created:** January 24, 2026  
**Next Step:** Add Toolbox MCP, then build Workflow Orchestrator with language support
