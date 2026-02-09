# MCP ENCYCLOPEDIA
## Complete Reference for All 66 Model Context Protocol Servers
**Version:** 1.0  
**Last Updated:** February 8, 2026  
**Maintained By:** Timothy + Claude  
**Workspace:** Walk This Way  

---

## README: How to Use This Encyclopedia

### Quick Reference
- **Total MCPs Configured:** 66
- **Currently Enabled:** 20 (lean writing toolkit)
- **Currently Disabled:** 46 (installed, ready to enable)
- **Custom-Built MCPs:** 8 (built specifically for this project)

### How MCPs Work in Cursor
Each **enabled** MCP launches as a persistent background process when Cursor starts. It stays running in memory, waiting for the AI agent to call its tools. **Disabled** MCPs are configured but not running -- zero resource cost. You can toggle any MCP between enabled/disabled by changing `"disabled": false` to `"disabled": true` in `.cursor/config/mcp.json`.

### Performance Guidelines
- **MacBook Air (16GB):** Keep 15-25 MCPs enabled for smooth operation
- **Mac Studio:** Can handle 30-40+ enabled MCPs comfortably
- Each enabled MCP consumes ~25-130MB RAM and a small amount of CPU
- Restart Cursor after changing MCP config to apply changes

### How to Add a New MCP
1. Add the entry to `.cursor/config/mcp.json` inside the `"mcpServers"` object
2. Set `"disabled": false` to enable immediately, or `"disabled": true` to install without running
3. If the MCP requires API keys, add them to `~/.zshrc` as environment variables
4. Restart Cursor to load the new MCP
5. **Update this Encyclopedia** -- add a new entry in the appropriate category

### How to Remove an MCP
1. Set `"disabled": true` in `.cursor/config/mcp.json` (recommended) OR delete the entry entirely
2. Restart Cursor
3. Update the status in this Encyclopedia

### How to Check MCP Health
- **Cursor Settings > MCP** shows status indicators (green = running, red = errored)
- Use Cursor Command `/mcp-lookup [name]` for quick info on any MCP
- This Encyclopedia is the comprehensive reference

### Entry Format
Each MCP entry includes:
- **Status:** Current enabled/disabled state
- **Type:** Official / Community / Custom-Built
- **API Required:** What keys are needed (if any)
- **Prerequisites:** What needs to be installed first
- **Description:** Detailed explanation of what the MCP does and how it's used
- **Use Case Example:** A concrete example of how Timothy uses this MCP
- **Installation Config:** The exact JSON config entry

---

## TABLE OF CONTENTS

### Currently Enabled MCPs (20)
- [A. Core Writing Intelligence](#a-core-writing-intelligence)
  - Compass Intelligence MCP
  - Compass Writing Guides MCP
  - Dennis Lehane Style MCP
  - Style Emulation MCP
  - Professional Editor MCP
  - Fiction Reverse Engineering MCP
  - WalkThisWay Characters MCP
- [B. Reasoning & Thinking (The 5 Brothers)](#b-reasoning--thinking-the-5-brothers)
  - Sequential Thinking (Base)
  - Sequential Thinking Enhanced
  - Sequential Thinking MAS
  - Sequential Thinking Rust
  - Sequential Thinking Ultra
- [C. Memory & Knowledge](#c-memory--knowledge)
  - Knowledge Graph Memory MCP
- [D. File Access](#d-file-access)
  - Walk This Way Files
  - Tim Cursor Experiment Files
- [E. Search & Web](#e-search--web)
  - DuckDuckGo Search MCP
  - Firecrawl MCP
  - Fetch MCP
- [F. Version Control](#f-version-control)
  - GitHub MCP
  - GitKraken MCP

### Currently Disabled MCPs (46)
- [G. Advanced Memory](#g-advanced-memory-disabled)
- [H. Search & Research](#h-search--research-disabled)
- [I. Media & Creative](#i-media--creative-disabled)
- [J. Data & Databases](#j-data--databases-disabled)
- [K. Automation & Workflow](#k-automation--workflow-disabled)
- [L. Development Tools](#l-development-tools-disabled)
- [M. Communication & Collaboration](#m-communication--collaboration-disabled)
- [N. AI & Reasoning](#n-ai--reasoning-disabled)
- [O. Orchestration](#o-orchestration-disabled)

---

## ENABLED MCPs (20)

---

### A. Core Writing Intelligence

---

#### Compass Intelligence MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built  
**API Required:** None  
**Prerequisites:** Python 3.11, mcp package  

Compass Intelligence MCP is the "brain" of the Compass Writing Ecosystem, combining Knowledge Graph visualization, structured text extraction, and prompt engineering pattern management into a single powerful server. It transforms the Knowledge Graph Memory's JSON data into visual Mermaid diagrams with color-coded nodes (characters in blue, locations in green, events in orange, themes in purple), enabling you to see your novel's entire web of relationships at a glance. The extraction tools use XML-tagged prompts with Chain of Thought reasoning to systematically pull characters, locations, events, themes, and plot threads from chapter text, feeding structured data into the Knowledge Graph. The prompt engineering library stores and manages reusable patterns (XML tags, CoT steps, context pinning, few-shot examples) that improve extraction quality over time. This MCP is the intermediary between your chapter text, Claude's analytical capabilities, the Knowledge Graph, and Mermaid visualization -- the pipeline that makes your novel's structure visible and queryable.

**Use Case Example:** After writing a new chapter, run `/chapter-to-kg` which uses Compass Intelligence to extract all characters, locations, and events mentioned, then automatically updates the Knowledge Graph and generates an updated Mermaid diagram showing how the new chapter connects to the rest of the novel.

**Installation:**
```json
"compass-intelligence": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/COMPASS_INTELLIGENCE_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/COMPASS_INTELLIGENCE_MCP/server.py"
  ],
  "disabled": false
}
```

---

#### Compass Writing Guides MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built  
**API Required:** None  
**Prerequisites:** Python 3.11, mcp package  

Compass Writing Guides MCP provides structured craft guidance for fiction writing, offering tools for analyzing narrative structure, pacing, dialogue, and prose quality. It contains writing guides based on proven fiction craft principles -- from story structure (three-act, hero's journey, in medias res) to scene-level techniques (dialogue attribution, showing vs. telling, sensory detail). The guides are specifically calibrated for the type of literary fiction Timothy writes -- character-driven narratives with complex timelines, working-class settings, and thematic depth. Unlike generic writing advice, these guides understand the specific challenges of "Walk This Way" -- maintaining two timelines, balancing multiple POVs, and weaving themes of class, loss, and music through every scene.

**Use Case Example:** When you're struggling with a scene transition between Maxanne's 2009 narration and the 1970s flashback, ask Claude to consult the Writing Guides MCP for techniques on seamless timeline transitions, and it will provide specific craft strategies with examples.

**Installation:**
```json
"compass-writing-guides": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/COMPASS_Writing_Guides_MCP/server.py"
  ],
  "disabled": false
}
```

---

#### Dennis Lehane Style MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built (Private & Confidential)  
**API Required:** None  
**Prerequisites:** Python 3.11, mcp package  

Dennis Lehane Style MCP provides deep analysis of Dennis Lehane's prose style, narrative techniques, and storytelling patterns specifically designed to inform and elevate Timothy's writing in "Walk This Way." Lehane's mastery of working-class Boston settings, male friendship dynamics, grief narratives, and unflinching emotional honesty directly parallels the themes and world of "Walk This Way" -- Nick and Jackie's story echoes the intense male bonds in "Mystic River" and "Gone, Baby, Gone." The MCP analyzes Lehane's specific techniques: his use of compressed dialogue that reveals character through what's NOT said, his ability to make blue-collar settings feel simultaneously specific and universal, his technique of using physical objects (like Nick's belt buckle from Spencer's) as emotional anchors, and his masterful handling of time jumps between past trauma and present reckoning. This is not about copying Lehane's style but about understanding the craft principles that make his working-class narratives so powerful and applying those principles to Timothy's unique voice.

**Use Case Example:** When writing Nick's confrontation with Jackie about the class divide, ask Claude to analyze the scene through the Lehane MCP lens -- it will evaluate whether the dialogue has Lehane's quality of revealing character through subtext, whether the physical setting grounds the emotional conflict, and whether the scene balances toughness with vulnerability the way Lehane does.

**Installation:**
```json
"dennis-lehane-style": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/DENNIS_LEHANE_MCP/server.py"
  ],
  "disabled": false
}
```

---

#### Style Emulation MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built  
**API Required:** Anthropic API Key  
**Prerequisites:** Python 3.11, mcp package, anthropic package  

Style Emulation MCP is the broader style analysis engine that can analyze and emulate the prose style of any author, not just Dennis Lehane. It breaks down an author's writing into measurable components -- sentence length distribution, vocabulary complexity, dialogue-to-narrative ratio, use of figurative language, pacing patterns, POV techniques -- and then provides tools to either match that style or blend elements from multiple authors. For "Walk This Way," this is invaluable when Timothy wants to calibrate different narrative voices: Maxanne's 2009 retrospective voice might channel the reflective quality of Joan Didion, while Nick's 1970s sections might carry the raw energy of early Bruce Springsteen interviews or the working-class grit of Richard Price. The MCP learns style preferences over time, building a profile of Timothy's own emerging voice and flagging when prose drifts too far from established patterns.

**Use Case Example:** After drafting a chapter, run it through the Style Emulation MCP to get a "style report" showing sentence length variation, dialogue density, and emotional tone -- then compare it against the established style profile for "Walk This Way" to ensure consistency across chapters.

**Installation:**
```json
"style-emulation": {
  "command": "/Users/timothy/mcp-servers/style-emulation-mcp/venv/bin/python",
  "args": ["-m", "style_emulation.server"],
  "env": {
    "PYTHONPATH": "/Users/timothy/mcp-servers/style-emulation-mcp/src",
    "ANTHROPIC_API_KEY": "env:ANTHROPIC_API_KEY"
  },
  "disabled": false
}
```

---

#### Professional Editor MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built  
**API Required:** None  
**Prerequisites:** Python 3.11, mcp package  

Professional Editor MCP provides the kind of rigorous, honest editorial feedback that a high-level literary editor would give -- not cheerleading, but constructive criticism focused on making the prose stronger. It evaluates manuscripts at multiple levels: line editing (word choice, sentence rhythm, clarity), copy editing (consistency, grammar, punctuation), developmental editing (structure, pacing, character arcs, thematic coherence), and proofing. The editor persona is calibrated to be direct and specific -- instead of saying "this scene needs work," it will say "Nick's dialogue in lines 45-60 loses his working-class voice; he's using vocabulary that sounds like Jackie, not like a kid from the Natick projects." This MCP is critical for maintaining quality across a long novel where it's easy for character voices to blur, pacing to sag, or thematic threads to get lost. It also flags common fiction pitfalls: over-reliance on adverbs, telling instead of showing, head-hopping between POVs, and dialogue attribution issues.

**Use Case Example:** Before finalizing a chapter, run it through the Professional Editor MCP for a full editorial report. It returns specific, actionable feedback organized by category (voice consistency, pacing, dialogue quality, thematic resonance) with line-number references and suggested revisions.

**Installation:**
```json
"professional-editor": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/PROFESSIONAL_EDITOR_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/PROFESSIONAL_EDITOR_MCP/server.py"
  ],
  "disabled": false
}
```

---

#### Fiction Reverse Engineering MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built  
**API Required:** None  
**Prerequisites:** Python 3.11, MCP package  

Fiction Reverse Engineering MCP takes published fiction and deconstructs it into its component craft elements -- revealing how great novels achieve their effects so Timothy can learn from and apply those techniques. Feed it a chapter from "Mystic River" and it will map out Lehane's scene structure (how he builds tension, where he places revelations, how he transitions between viewpoints), his dialogue techniques (subtext, rhythm, class-specific speech patterns), his use of setting as emotional mirror, and his pacing decisions. This is "reverse engineering for writers" -- understanding the machinery beneath the surface of great fiction. For "Walk This Way," this MCP helps Timothy study how other novelists have handled the specific challenges his book faces: dual timelines (like "The Kite Runner"), working-class male friendship (like "Mystic River"), music as cultural identity (like "High Fidelity"), and grief narratives (like "A Little Life").

**Use Case Example:** Before writing the Battle of the Bands scene, feed the MCP a comparable climactic scene from a published novel and ask it to reverse-engineer the pacing, tension-building, and emotional payoff techniques -- then apply those structural principles to your own scene.

**Installation:**
```json
"fiction-reverse-engineering": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/FICTION_REVERSE_ENGINEERING_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/FICTION_REVERSE_ENGINEERING_MCP/server.py"
  ],
  "disabled": false
}
```

---

#### WalkThisWay Characters MCP
**Status:** ✅ Enabled  
**Type:** Custom-Built  
**API Required:** None  
**Prerequisites:** Python 3.11, MCP package  

WalkThisWay Characters MCP is a dedicated character database and consistency engine specifically for the "Walk This Way" novel. It stores detailed profiles for every character -- not just names and physical descriptions, but voice patterns, speech rhythms, vocabulary range, emotional triggers, relationship dynamics, and character arc trajectories. Nick Johnson has a specific way of talking (shorter sentences, working-class Boston slang, avoids emotional vulnerability through humor), and this MCP ensures that voice stays consistent whether you're writing Chapter 1 or Chapter 34. It tracks character states across the timeline -- Nick at 15 (grieving, angry, discovering music) vs. Nick at 17 (more confident, channeling grief into guitar) vs. adult Nick -- and flags inconsistencies. The MCP also maintains relationship matrices showing how every character pair interacts, what they know about each other, and what secrets exist between them.

**Use Case Example:** Before writing a scene between Nick and Jackie, query the Characters MCP: "What does Nick know about Jackie's classical training at this point in the timeline? What's their emotional temperature after the last scene they shared?" The MCP returns precise answers based on the story's internal state.

**Installation:**
```json
"walkthisway-characters": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/WalkThisWay_Character_MCP/server.py"
  ],
  "disabled": false
}
```

---

### B. Reasoning & Thinking (The 5 Brothers)

---

#### Sequential Thinking (Base) - Brother #1
**Status:** ✅ Enabled  
**Type:** Official Anthropic  
**API Required:** None  
**Prerequisites:** None  

Sequential Thinking MCP forces transparent, step-by-step reasoning that makes implicit logic explicit -- perfect for systematic plot and character analysis. When analyzing complex plot decisions like "Should Nick confront Jackie about the class divide at the Battle of the Bands?" it breaks down the reasoning chain, identifies assumptions (Nick's working-class pride, Jackie's guilt about privilege, the weight of their friendship), validates each step, and reveals potential plot holes before they become problems. This MCP is essential for debugging narrative logic in "Walk This Way," ensuring character motivations are consistent and maintaining the structural integrity of the dual timeline structure. It transforms intuitive "feel" into explicit, teachable reasoning processes. **Use this Brother for:** Simple logic checks, basic step-by-step analysis, timeline verification.

**Use Case Example:** "Walk me through step-by-step whether it makes narrative sense for Maxanne to reveal Dan's cause of death in Chapter 3 or hold it until Chapter 12."

**Installation:**
```json
"sequential-thinking": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
  "disabled": false
}
```

---

#### Sequential Thinking Enhanced - Brother #2
**Status:** ✅ Enabled  
**Type:** Community (VitalyMalakanov)  
**API Required:** None  
**Prerequisites:** Python venv at /Users/timothy/mcp-servers/sequential-thinking-enhanced/  

Enhanced Sequential Thinking adds 19 different thinking modes (linear, creative, evaluative, etc.), real-time agentic feedback, tool recommendations, and explicit future state planning, offering granular control over reasoning style and flow. The system learns which thinking modes work best for different writing tasks -- creative mode for plot brainstorming, evaluative mode for consistency checking, linear mode for timeline verification. For "Walk This Way," this means you can switch between creative exploration (developing the friendship between Nick and Jackie) and critical evaluation (ensuring their voices remain distinct and authentic) seamlessly. **Use this Brother for:** Mode-specific thinking -- when you need creative brainstorming vs. critical evaluation vs. linear analysis.

**Use Case Example:** "Switch to creative mode and brainstorm 5 alternative ways the Battle of the Bands could end, then switch to evaluative mode and rank them by thematic resonance."

**Installation:**
```json
"sequential-thinking-enhanced": {
  "command": "/Users/timothy/mcp-servers/sequential-thinking-enhanced/venv/bin/enhanced-sequential-thinking-server",
  "disabled": false
}
```

---

#### Sequential Thinking MAS (Multi-Agent System) - Brother #3
**Status:** ✅ Enabled  
**Type:** Community  
**API Required:** Anthropic API Key  
**Prerequisites:** Python venv at /Users/timothy/mcp-servers/sequential-thinking-mas/  

Sequential Thinking MAS uses multiple specialized agents (Factual, Emotional, Critical, Optimistic, Creative, Synthesis) coordinated via a complexity analyzer that routes tasks intelligently. For "Walk This Way," plot decisions are analyzed from multiple perspectives simultaneously -- the Factual agent verifies timeline consistency, the Emotional agent evaluates emotional authenticity, the Critical agent identifies potential plot holes, the Optimistic agent explores positive outcomes, the Creative agent generates alternative narrative paths, and the Synthesis agent combines all perspectives into comprehensive recommendations. The system learns which agent combinations work best for different types of narrative problems. **Use this Brother for:** Complex decisions requiring multiple perspectives -- character arc choices, thematic conflicts, plot structure debates.

**Use Case Example:** "Should Nick forgive Jackie for choosing classical music over their band? Analyze from all agent perspectives -- factual (what happened), emotional (how both feel), critical (plot holes), creative (alternative resolutions)."

**Installation:**
```json
"sequential-thinking-mas": {
  "command": "/Users/timothy/mcp-servers/sequential-thinking-mas/venv/bin/mcp-server-mas-sequential-thinking",
  "env": {
    "LLM_PROVIDER": "anthropic",
    "ANTHROPIC_API_KEY": "env:ANTHROPIC_API_KEY"
  },
  "disabled": false
}
```

---

#### Sequential Thinking Ultra - Brother #4
**Status:** ✅ Enabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** Node.js, built at /Users/timothy/mcp-servers/sequential-thinking-ultra/  

Sequential Thinking Ultra adds bias detection (identifying 5 major cognitive biases), real-time quality metrics (consistency, completeness, practicality), resource-budgeting (fast/thorough modes), improved flow control, dynamic branching, and query rewriting capabilities. The bias detection is particularly powerful -- it identifies when plot decisions are influenced by confirmation bias (assuming Nick must be angry at Jackie because of class differences, when the story shows their friendship is more complex), availability heuristic (overemphasizing recent plot elements), or other cognitive biases. The quality metrics provide confidence scores for reasoning chains, helping identify when plot logic is solid vs. when it needs more work. **Use this Brother for:** Bias detection, quality scoring, when you need confidence levels on narrative decisions.

**Use Case Example:** "Analyze Nick's decision to quit school and pursue music -- check for cognitive biases in my reasoning and give me confidence scores on whether this character choice is authentic."

**Installation:**
```json
"sequential-thinking-ultra": {
  "command": "node",
  "args": ["/Users/timothy/mcp-servers/sequential-thinking-ultra/dist/index.js"],
  "env": {
    "ULTRA_THINK_AUTO_LABEL": "true",
    "ULTRA_THINK_QUALITY": "true",
    "ULTRA_THINK_META": "true",
    "ULTRA_THINK_BUDGET": "true",
    "ENABLE_QUERY_REWRITING": "true",
    "DEFAULT_BUDGET_MODE": "balanced"
  },
  "disabled": false
}
```

---

#### Sequential Thinking Rust - Brother #5
**Status:** ✅ Enabled  
**Type:** Community (Performance Variant)  
**API Required:** None  
**Prerequisites:** Rust binary at /Users/timothy/.cargo/bin/  

The Rust-based implementation provides significant speedups, memory efficiency, and concurrent processing while maintaining full compliance with MCP specs. If you're running Sequential Thinking across multiple analysis tasks simultaneously or processing large manuscripts (75,000-90,000 words), the Rust version provides faster feedback loops. The performance gains become valuable when combined with other Sequential Thinking features, allowing analysis without lag. **Use this Brother for:** Performance-critical tasks, large-scale analysis, when speed matters.

**Use Case Example:** When running a full-novel consistency check across all 34 chapters simultaneously, the Rust version handles the workload without the latency of the Python-based variants.

**Installation:**
```json
"sequential-thinking-rust": {
  "command": "/Users/timothy/.cargo/bin/sequential-thinking-server",
  "disabled": false
}
```

---

### C. Memory & Knowledge

---

#### Knowledge Graph Memory MCP
**Status:** ✅ Enabled  
**Type:** Official Anthropic  
**API Required:** None  
**Prerequisites:** None  

Knowledge Graph Memory MCP is the foundation of the persistent memory system, storing characters, relationships, plot threads, and world-building details in a structured graph format with entities, relations, and observations. It enables complex queries like "What are Nick Johnson's unresolved conflicts with Jackie Marsh?" or "Who knows about the belt buckle that Nick purchased from Spencer's in the Natick Mall?" that would be impossible with simple file storage. The graph structure automatically maintains temporal relationships, so when Chapter 1 takes place in 1979 (when Dan is already dead), the system correctly tracks that Dan died November 14, 1976 when Nick was 15. This MCP is irreplaceable for maintaining consistency and prevents the plot holes and character inconsistencies that plague complex narratives with dual timeline structures. It also feeds into the Compass Intelligence pipeline for Mermaid visualization.

**Use Case Example:** After introducing a new character or plot element, add it to the Knowledge Graph: "Create entity 'Maxanne Sartori' with observations: 'Radio DJ at WBCN', 'Narrator of the 2009 frame story', 'Witnessed the 1970s Boston rock scene firsthand'." Then query it later: "What does Maxanne know about Nick and Dan's relationship?"

**Installation:**
```json
"knowledge-graph-memory": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-memory"],
  "disabled": false
}
```

---

### D. File Access

---

#### Walk This Way Files
**Status:** ✅ Enabled  
**Type:** Official Anthropic (Filesystem)  
**API Required:** None  
**Prerequisites:** None  

Filesystem MCP scoped to the Walk This Way workspace, providing the AI agent with direct read/write access to all novel files, drafts, documentation, COMPASS implementations, and project resources. This is the foundation that enables every other MCP to work -- without file access, the agent can't read your chapters, update your drafts, or access your Story Bible. The scope is limited to this specific workspace directory for security, ensuring the agent can't accidentally access files outside the project.

**Use Case Example:** "Read Chapter 12 from Draft_1 and compare it with the Active_Draft_2 version, highlighting what changed."

**Installation:**
```json
"walk-this-way-files": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way"
  ],
  "disabled": false
}
```

---

#### Tim Cursor Experiment Files
**Status:** ✅ Enabled  
**Type:** Official Anthropic (Filesystem)  
**API Required:** None  
**Prerequisites:** None  

Filesystem MCP scoped to the Tim Cursor Experiment workspace, providing access to Timothy's second workspace where Cursor tooling experiments, MCP research, and technical documentation live. This cross-workspace access is essential for referencing MCP setup notes, comparing configurations, and accessing research that informs the Walk This Way project's technical infrastructure.

**Use Case Example:** "Check the Tim Cursor Experiment workspace for any MCP configuration notes I saved there last week about the Sequential Thinking setup."

**Installation:**
```json
"tim-cursor-experiment-files": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/Tim Cursor Experiment"
  ],
  "disabled": false
}
```

---

### E. Search & Web

---

#### DuckDuckGo Search MCP
**Status:** ✅ Enabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

DuckDuckGo Search MCP provides quick, privacy-respecting web searches without requiring an API key. It's the "quick reference lookup" tool for when you need a fast fact-check during active writing without interrupting creative flow. Need to verify that WBCN was actually on 104.1 FM in 1979? That the Natick Mall had a Spencer's Gifts in the late 1970s? That the Battle of the Bands format you're describing is historically plausible? DuckDuckGo handles these in seconds. It complements Firecrawl, which is for deep research dossiers -- DuckDuckGo is for rapid fact-checking.

**Use Case Example:** "Quick search: What bands played at the Rat in Kenmore Square in 1979?" -- gets you a fast answer without leaving Cursor.

**Installation:**
```json
"duckduckgo-search": {
  "command": "npx",
  "args": ["-y", "duckduckgo-mcp-server"],
  "disabled": false
}
```

---

#### Firecrawl MCP
**Status:** ✅ Enabled  
**Type:** Community  
**API Required:** Firecrawl API Key (FIRECRAWL_API_KEY)  
**Prerequisites:** API key in ~/.zshrc  

Firecrawl MCP is the PRIMARY deep research tool -- it doesn't just search, it scrapes full web pages, extracts article content, and compiles comprehensive research dossiers. When you need to research the 1970s Boston punk scene for "Walk This Way," Firecrawl can crawl entire websites about WBCN radio history, extract detailed articles about the Rat club in Kenmore Square, and compile everything into structured research documents. It handles JavaScript-rendered pages, bypasses paywalls where possible, and returns clean markdown content. The difference between Firecrawl and DuckDuckGo is depth -- DuckDuckGo gets you a quick answer, Firecrawl gets you a 20-page research dossier.

**Use Case Example:** "Firecrawl the WBCN Wikipedia page and any related articles about Boston rock radio in the 1970s -- I need a comprehensive research document on the station's history, key DJs, and the role it played in breaking new bands."

**Installation:**
```json
"firecrawl": {
  "command": "npx",
  "args": ["-y", "firecrawl-mcp"],
  "env": {
    "FIRECRAWL_API_KEY": "env:FIRECRAWL_API_KEY"
  },
  "disabled": false
}
```

---

#### Fetch MCP
**Status:** ✅ Enabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

Fetch MCP provides basic HTTP fetching capabilities -- it can retrieve any URL and return its content as clean, readable text. It's simpler than Firecrawl (no JavaScript rendering, no crawling multiple pages) but faster and more reliable for straightforward page retrieval. Useful for grabbing specific web pages, API responses, or documents when you know exactly what URL you need. Think of it as "wget for the AI" -- give it a URL, get back the content.

**Use Case Example:** "Fetch the lyrics for 'Rock and Roll All Nite' by KISS from this specific URL so I can reference the song that's playing in the Chapter 5 scene."

**Installation:**
```json
"fetch": {
  "command": "npx",
  "args": ["-y", "@mcpflow.io/mcp-fetch"],
  "disabled": false
}
```

---

### F. Version Control

---

#### GitHub MCP
**Status:** ✅ Enabled  
**Type:** Official Anthropic  
**API Required:** GitHub Personal Access Token (GITHUB_TOKEN)  
**Prerequisites:** Token in ~/.zshrc (no-expiration, personal account timothy-j-smith)  

GitHub MCP provides full repository management capabilities -- creating/managing repos, branches, pull requests, issues, and file operations directly through the AI agent. For "Walk This Way," this means the agent can commit your work, create branches for experimental chapters, manage issues for plot holes or TODOs, and push changes to your remote repository without you leaving the editor. It uses your personal GitHub token (timothy-j-smith account) and is completely separate from any work accounts.

**Use Case Example:** "Commit the current chapter changes with message 'Chapter 12 revision: added Maxanne flashback scene' and push to main."

**Installation:**
```json
"github": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-github", "--token", "env:GITHUB_TOKEN"],
  "disabled": false
}
```

---

#### GitKraken MCP
**Status:** ✅ Enabled  
**Type:** Official GitKraken  
**API Required:** None (uses GitKraken CLI)  
**Prerequisites:** GitKraken CLI (`gk`) installed  

GitKraken MCP provides enhanced Git operations through GitKraken's powerful CLI, offering visual diff capabilities, advanced merge conflict resolution, and repository analytics beyond what the standard GitHub MCP provides. It's particularly useful for comparing chapter versions, visualizing the commit history of your novel's evolution, and handling complex branch operations. GitKraken's merge tools are superior to basic git for resolving conflicts when you're working on the same chapter from both your MacBook Air and Mac Studio.

**Use Case Example:** "Show me a visual diff of Chapter 8 between the current version and last week's commit, highlighting exactly what changed in Nick's dialogue."

**Installation:**
```json
"gitkraken": {
  "command": "gk",
  "args": ["mcp"],
  "disabled": false
}
```

---

## DISABLED MCPs (46)

*These MCPs are installed and configured but not currently running. Enable any of them by changing `"disabled": true` to `"disabled": false` in `.cursor/config/mcp.json` and restarting Cursor.*

---

### G. Advanced Memory (Disabled)

---

#### Enhanced MCP Memory
**Status:** ⬚ Disabled  
**Type:** Community (cbunting99)  
**API Required:** None  
**Prerequisites:** Python venv at /Users/timothy/mcp-servers/enhanced-mcp-memory/  

Enhanced MCP Memory adds memory persistence, workflow learning, and style pattern detection on top of basic memory capabilities. It learns your writing patterns and workflow preferences over time, automatically detecting when you're repeating themes or developing similar character arcs. For "Walk This Way," it would detect patterns like how you develop working-class characters and how you handle dual timelines, then consolidate these patterns to help maintain consistency. Currently disabled because Knowledge Graph Memory covers the core memory needs, and this adds overhead for features not yet critical to the writing workflow.

**Enable when:** You want the AI to learn and remember your workflow patterns across sessions.

```json
"enhanced-mcp-memory": {
  "command": "/Users/timothy/mcp-servers/enhanced-mcp-memory/venv/bin/enhanced-mcp-memory",
  "disabled": true
}
```

---

#### Supermemory MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** OpenMemory API Key (OPENMEMORY_API_KEY)  
**Prerequisites:** API key  

Supermemory provides a lightweight, universal memory layer that can store and retrieve any type of information. It's simpler than Knowledge Graph Memory (no graph structure) but faster for basic key-value style memory. Useful as a supplementary memory system for quick notes and session-specific context that doesn't need full graph relationships.

**Enable when:** You need a fast, simple memory store alongside the Knowledge Graph.

```json
"supermemory": {
  "command": "npx",
  "args": ["-y", "@supercorp/memory-mcp"],
  "disabled": true
}
```

---

#### OpenMemory MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** OpenMemory API Key (OPENMEMORY_API_KEY)  
**Prerequisites:** API key  

OpenMemory provides cloud-based persistent memory that syncs across devices and sessions. Unlike local memory MCPs, your memories are stored in the cloud and accessible from any machine. This could be valuable for syncing novel context between your MacBook Air and Mac Studio.

**Enable when:** You need cloud-synced memory across both machines.

```json
"openmemory": {
  "command": "npx",
  "args": ["-y", "@openmemory/mcp-server"],
  "env": {
    "OPENMEMORY_API_KEY": "env:OPENMEMORY_API_KEY"
  },
  "disabled": true
}
```

---

#### Scanadi AI Memory
**Status:** ⬚ Disabled  
**Type:** Community (GitHub source)  
**API Required:** PostgreSQL URI  
**Prerequisites:** PostgreSQL database, pgvector extension, built from source at /Users/timothy/mcp-servers/scanadi-memory/  

Scanadi AI Memory uses PostgreSQL with pgvector for semantic search, intelligent caching, graph relationships, and sophisticated memory decay algorithms. Memories automatically age -- older plot details move to archived states while current threads stay active. Requires a running PostgreSQL instance, which is why it's disabled.

**Enable when:** You have PostgreSQL set up and want enterprise-grade memory with semantic search and memory aging.

```json
"scanadi-ai-memory": {
  "command": "node",
  "args": ["/Users/timothy/mcp-servers/scanadi-memory/repo/dist/cli.js"],
  "env": {
    "POSTGRES_URL": "env:POSTGRES_URI"
  },
  "disabled": true
}
```

---

#### Vectara MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Vectara API Key + Corpus Key  
**Prerequisites:** API keys  

Vectara provides enterprise-grade semantic search and RAG (Retrieval-Augmented Generation) capabilities. Upload your entire manuscript and Vectara indexes it for semantic queries -- ask "find all scenes where Nick feels inadequate about his social class" and it finds them even if those exact words aren't used. Powerful for finding thematic connections across a long novel.

**Enable when:** You want semantic search across your full manuscript and have Vectara API keys.

```json
"vectara": {
  "command": "/Users/timothy/mcp-servers/vectara-mcp/venv/bin/vectara-mcp",
  "args": ["--transport", "stdio"],
  "env": {
    "VECTARA_API_KEY": "env:VECTARA_API_KEY",
    "VECTARA_CORPUS_KEY": "env:VECTARA_CORPUS_KEY"
  },
  "disabled": true
}
```

---

#### Cognee Connections
**Status:** ⬚ Disabled  
**Type:** Community (Graph-RAG)  
**API Required:** OpenAI API Key  
**Prerequisites:** Python venv, OpenAI key  

Cognee uses Graph-RAG to discover hidden connections across manuscripts -- relationships between characters, themes, and plot elements that you might not consciously recognize. It builds a knowledge graph from your text and then surfaces unexpected connections.

**Enable when:** You want AI-discovered connections across your manuscripts.

```json
"cognee-connections": {
  "command": "/Users/timothy/mcp-servers/cognee-mcp/repo/cognee-mcp/.venv/bin/cognee-mcp",
  "env": {
    "LLM_API_KEY": "env:OPENAI_API_KEY",
    "ENABLE_BACKEND_ACCESS_CONTROL": "false"
  },
  "disabled": true
}
```

---

### H. Search & Research (Disabled)

---

#### Brave Search MCP
**Status:** ⬚ Disabled  
**Type:** Official Brave  
**API Required:** Brave API Key (BRAVE_API_KEY)  
**Prerequisites:** API key  

Brave Search provides privacy-focused web search with its own independent index (not Google's). It offers structured search results with snippets, and supports both web and news searches. Currently disabled because DuckDuckGo covers the quick-search needs without requiring an API key.

**Enable when:** You want an alternative to DuckDuckGo with potentially better results for specific queries.

```json
"brave-search": {
  "command": "npx",
  "args": ["-y", "@brave/brave-search-mcp-server"],
  "env": {
    "BRAVE_API_KEY": "env:BRAVE_API_KEY"
  },
  "disabled": true
}
```

---

#### Exa MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Exa API Key (EXA_API_KEY)  
**Prerequisites:** API key  

Exa is an AI-native search engine that understands semantic meaning, not just keywords. Ask "novels that handle dual timelines between past trauma and present reckoning" and it finds relevant results even if those exact phrases don't appear. Better than traditional search for conceptual/thematic research.

**Enable when:** You need semantic/conceptual web searches beyond keyword matching.

```json
"exa": {
  "command": "npx",
  "args": ["-y", "exa-mcp-server"],
  "env": {
    "EXA_API_KEY": "env:EXA_API_KEY"
  },
  "disabled": true
}
```

---

#### Perplexity MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Perplexity API Key (PERPLEXITY_API_KEY)  
**Prerequisites:** API key  

Perplexity provides AI-powered search that returns synthesized answers with citations, not just links. Ask a complex research question and get a well-written summary with sources. Excellent for historical research where you need a comprehensive answer, not a list of links.

**Enable when:** You want AI-synthesized research answers with citations for historical accuracy.

```json
"perplexity": {
  "command": "npx",
  "args": ["-y", "@jschuller/perplexity-mcp"],
  "env": {
    "PERPLEXITY_API_KEY": "env:PERPLEXITY_API_KEY"
  },
  "disabled": true
}
```

---

#### Open Library MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

Open Library MCP connects to the Internet Archive's Open Library, providing access to book metadata, author information, and in some cases full text of public domain works. Useful for researching published novels, finding comparable titles, and accessing reference materials.

**Enable when:** You need to research published books, find comp titles, or access book metadata.

```json
"open-library": {
  "command": "npx",
  "args": ["-y", "@8enSmith/mcp-open-library"],
  "disabled": true
}
```

---

#### Puppeteer MCP
**Status:** ⬚ Disabled  
**Type:** Official Anthropic  
**API Required:** None  
**Prerequisites:** None  

Puppeteer provides full browser automation -- it can navigate to websites, click buttons, fill forms, take screenshots, and extract content from JavaScript-heavy pages that Firecrawl might not handle. Think of it as a robot that can browse the web like a human.

**Enable when:** You need to interact with web pages that require JavaScript or login, or want screenshots of websites.

```json
"puppeteer": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-puppeteer"],
  "disabled": true
}
```

---

#### Context7 MCP
**Status:** ⬚ Disabled  
**Type:** Community (Upstash)  
**API Required:** None  
**Prerequisites:** None  

Context7 provides up-to-date documentation and code examples for libraries and frameworks. It pulls the latest docs directly, ensuring you're never working with outdated information. More relevant for coding projects than fiction writing.

**Enable when:** You're doing technical/coding work and need current documentation.

```json
"context7": {
  "command": "npx",
  "args": ["-y", "@upstash/context7-mcp"],
  "disabled": true
}
```

---

#### Goodreads Scraper
**Status:** ⬚ Disabled  
**Type:** Community (via Apify)  
**API Required:** Apify API Token (APIFY_API_TOKEN)  
**Prerequisites:** API token  

Uses Apify's web scraping platform to extract book data from Goodreads -- reviews, ratings, comparable titles, genre classifications, and reader demographics. Invaluable for market research and understanding your comp titles.

**Enable when:** You want to research comparable books, read aggregated reviews, or do market analysis.

```json
"goodreads-scraper": {
  "command": "npx",
  "args": ["-y", "apify-mcp@latest"],
  "env": {
    "APIFY_API_TOKEN": "env:APIFY_API_TOKEN"
  },
  "disabled": true
}
```

---

### I. Media & Creative (Disabled)

---

#### Adobe Express MCP
**Status:** ⬚ Disabled  
**Type:** Official Adobe  
**API Required:** None  
**Prerequisites:** None  

Adobe Express MCP provides AI-powered design capabilities -- creating images, social media graphics, marketing materials, and visual content. For a novelist, this could generate book cover concepts, character mood boards, setting reference images, or social media promotional graphics.

**Enable when:** You need to create visual assets for your book (cover concepts, mood boards, promo graphics).

```json
"adobe-express": {
  "command": "npx",
  "args": ["-y", "@adobe/express-developer-mcp@latest", "--yes"],
  "disabled": true
}
```

---

#### EverArt MCP
**Status:** ⬚ Disabled  
**Type:** Official Anthropic  
**API Required:** None  
**Prerequisites:** None  

EverArt provides AI image generation capabilities through the MCP protocol. Create character portraits, setting illustrations, scene mood images, or any visual content to support your writing process. Different from Adobe Express in that it's focused on AI art generation rather than design tools.

**Enable when:** You want AI-generated images for characters, settings, or scenes.

```json
"everart": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-everart"],
  "disabled": true
}
```

---

#### Imagen3 (Google)
**Status:** ⬚ Disabled  
**Type:** Community (GitHub source)  
**API Required:** Gemini API Key (GEMINI_API_KEY)  
**Prerequisites:** Built from source at /Users/timothy/mcp-servers/imagen3-mcp/  

Google's Imagen3 image generation model accessed through MCP. Produces high-quality, photorealistic images. Could generate reference images for settings (1970s Boston streets, the Rat club interior, WBCN studios) or character visualizations.

**Enable when:** You want Google's image generation for photorealistic reference images.

```json
"imagen3": {
  "command": "node",
  "args": ["/Users/timothy/mcp-servers/imagen3-mcp/repo/build/index.js"],
  "env": {
    "GEMINI_API_KEY": "env:GEMINI_API_KEY"
  },
  "disabled": true
}
```

---

#### MiniMax MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** MiniMax API Key + Host  
**Prerequisites:** API keys  

MiniMax provides AI-powered video and audio generation. Could generate ambient audio for writing sessions (1970s Boston street sounds, punk rock club atmosphere) or promotional video content.

**Enable when:** You want AI-generated audio/video content.

```json
"minimax": {
  "command": "npx",
  "args": ["-y", "minimax-mcp-js"],
  "env": {
    "MINIMAX_API_KEY": "env:MINIMAX_API_KEY",
    "MINIMAX_API_HOST": "env:MINIMAX_API_HOST"
  },
  "disabled": true
}
```

---

#### Blender MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** Blender installed, Python venv at /Users/timothy/mcp-servers/blender-mcp/  

Blender MCP connects the AI agent to Blender, the open-source 3D modeling software. Could create 3D visualizations of settings, character models, or scene layouts. Requires Blender to be installed and running.

**Enable when:** You want 3D visualization of settings or scenes and have Blender installed.

```json
"blender": {
  "command": "/Users/timothy/mcp-servers/blender-mcp/venv/bin/blender-mcp",
  "disabled": true
}
```

---

#### FFMCP (FFmpeg)
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** FFmpeg installed  

FFMCP wraps FFmpeg for audio/video processing through MCP. Convert audio formats, extract clips, process video, and manipulate media files. Useful if you're working with audio recordings, podcast content, or video research materials.

**Enable when:** You need to process audio or video files.

```json
"ffmcp": {
  "command": "npx",
  "args": ["-y", "ffmcp"],
  "disabled": true
}
```

---

#### AssemblyAI MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** AssemblyAI API Key (ASSEMBLYAI_API_KEY)  
**Prerequisites:** API key  

AssemblyAI provides speech-to-text transcription with high accuracy, speaker diarization (identifying who's speaking), and sentiment analysis. Could transcribe interviews, research recordings, or your own spoken notes/brainstorming sessions into text.

**Enable when:** You have audio recordings to transcribe or want to dictate chapters.

```json
"assemblyai": {
  "command": "npx",
  "args": ["-y", "assembly-ai-mcp@latest"],
  "env": {
    "ASSEMBLYAI_API_KEY": "env:ASSEMBLYAI_API_KEY"
  },
  "disabled": true
}
```

---

### J. Data & Databases (Disabled)

---

#### SQLite MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

SQLite provides a local, file-based relational database accessible through MCP. Store structured data (character databases, scene indexes, timeline events) in SQL tables that can be queried with powerful SQL statements. More structured than Knowledge Graph for tabular data.

**Enable when:** You want relational database queries for structured novel data (timeline tables, character attributes, scene indexes).

```json
"sqlite": {
  "command": "npx",
  "args": ["-y", "mcp-sqlite", "/Users/timothy/mcp-servers/databases/local.db"],
  "disabled": true
}
```

---

#### PostgreSQL MCP
**Status:** ⬚ Disabled  
**Type:** Official Anthropic  
**API Required:** PostgreSQL URI  
**Prerequisites:** Running PostgreSQL instance  

Full PostgreSQL database access through MCP. Enterprise-grade relational database for when SQLite isn't sufficient. Required by some advanced MCPs (like Scanadi AI Memory).

**Enable when:** You have PostgreSQL running and need full relational database capabilities.

```json
"postgresql": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-postgres", "env:POSTGRES_URI"],
  "disabled": true
}
```

---

#### Airtable MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Airtable API Key (AIRTABLE_API_KEY)  
**Prerequisites:** Airtable account + API key  

Airtable provides a spreadsheet-database hybrid with a rich API. Could be used for tracking characters, scene logs, revision notes, or project management in a visual, collaborative format that syncs with Airtable's web interface.

**Enable when:** You use Airtable for project management or want a visual database interface.

```json
"airtable": {
  "command": "npx",
  "args": ["-y", "airtable-mcp-server"],
  "env": {
    "AIRTABLE_API_KEY": "env:AIRTABLE_API_KEY"
  },
  "disabled": true
}
```

---

#### Supabase MCP
**Status:** ⬚ Disabled  
**Type:** Official Supabase  
**API Required:** Supabase Access Token  
**Prerequisites:** Supabase account  

Supabase provides a full backend-as-a-service (PostgreSQL database, authentication, storage, real-time subscriptions) through MCP. Overkill for fiction writing but could power a web-based dashboard or collaborative writing environment.

**Enable when:** You're building web-based tools or dashboards that need a backend.

```json
"supabase": {
  "command": "npx",
  "args": ["-y", "@supabase/mcp-server-supabase@latest", "--access-token", "env:SUPABASE_ACCESS_TOKEN"],
  "disabled": true
}
```

---

### K. Automation & Workflow (Disabled)

---

#### N8N Workflow MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** N8N API Key + Base URL  
**Prerequisites:** Running N8N instance  

N8N is a workflow automation platform (like Zapier but self-hosted). Through MCP, you can create automated workflows -- e.g., "when a chapter is committed to GitHub, automatically run it through the Professional Editor MCP and save the report." Requires a running N8N instance.

**Enable when:** You want automated writing workflows and have N8N set up.

```json
"n8n-workflow": {
  "command": "npx",
  "args": ["-y", "n8n-nodes-mcp"],
  "env": {
    "N8N_API_KEY": "env:N8N_API_KEY",
    "N8N_BASE_URL": "env:N8N_BASE_URL"
  },
  "disabled": true
}
```

---

#### Apache Airflow MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Airflow credentials  
**Prerequisites:** Running Airflow instance, Python venv at /Users/timothy/mcp-servers/airflow-mcp/  

Apache Airflow is an enterprise workflow orchestration platform for scheduling and monitoring complex data pipelines. More powerful than N8N but also more complex. Could orchestrate multi-step writing analysis pipelines.

**Enable when:** You need enterprise-grade workflow orchestration.

```json
"apache-airflow": {
  "command": "/Users/timothy/mcp-servers/airflow-mcp/venv/bin/mcp-server-apache-airflow",
  "env": {
    "AIRFLOW_BASE_URL": "env:AIRFLOW_BASE_URL",
    "AIRFLOW_USERNAME": "env:AIRFLOW_USERNAME",
    "AIRFLOW_PASSWORD": "env:AIRFLOW_PASSWORD"
  },
  "disabled": true
}
```

---

#### Label Studio MCP
**Status:** ⬚ Disabled  
**Type:** Community (GitHub source)  
**API Required:** Label Studio URL + API Key  
**Prerequisites:** Running Label Studio instance, Python venv  

Label Studio is a data labeling platform. Through MCP, you could create annotation projects for your manuscript -- labeling scenes by emotion, tagging character appearances, classifying dialogue types. Useful for systematic manuscript analysis.

**Enable when:** You want structured annotation/labeling of your manuscript for analysis.

```json
"label-studio": {
  "command": "/Users/timothy/mcp-servers/label-studio-mcp/venv_dir/bin/mcp-label-studio",
  "env": {
    "LABEL_STUDIO_URL": "env:LABEL_STUDIO_URL",
    "LABEL_STUDIO_API_KEY": "env:LABEL_STUDIO_API_KEY"
  },
  "disabled": true
}
```

---

### L. Development Tools (Disabled)

---

#### Docker MCP
**Status:** ⬚ Disabled  
**Type:** Official Docker  
**API Required:** None  
**Prerequisites:** Docker Desktop installed  

Docker MCP manages containers through the AI agent -- creating, starting, stopping, and monitoring Docker containers. Useful for running self-hosted services (databases, N8N, Label Studio) in isolated containers.

**Enable when:** You use Docker for running services.

```json
"docker": {
  "command": "npx",
  "args": ["-y", "@docker/mcp-server-docker"],
  "disabled": true
}
```

---

#### Jupyter Notebook MCP
**Status:** ⬚ Disabled  
**Type:** Community (PyPI)  
**API Required:** None  
**Prerequisites:** Python venv at /Users/timothy/mcp-servers/jupyter-mcp/  

Jupyter Notebook MCP enables creating and running Jupyter notebooks through MCP. Could be used for data analysis of your manuscript (word frequency, dialogue analysis, pacing charts), generating visualizations, or running Python analysis scripts.

**Enable when:** You want data analysis or visualizations of your manuscript in notebook format.

```json
"jupyter-notebook": {
  "command": "/Users/timothy/mcp-servers/jupyter-mcp/venv/bin/jupyter-mcp-server",
  "disabled": true
}
```

---

#### Toolbox MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

Toolbox is a meta-MCP that provides access to a curated collection of useful tools -- text processing, data manipulation, format conversion, and utility functions. It's a Swiss Army knife of small tools bundled together.

**Enable when:** You need miscellaneous utility tools and don't want to install separate MCPs for each.

```json
"toolbox": {
  "command": "uvx",
  "args": ["--prerelease=allow", "mcp-toolbox[all]@latest", "stdio"],
  "disabled": true
}
```

---

#### Vizro Dashboards MCP
**Status:** ⬚ Disabled  
**Type:** Community (PyPI)  
**API Required:** None  
**Prerequisites:** Python venv at /Users/timothy/mcp-servers/vizro-mcp/  

Vizro creates interactive data dashboards using Python. Could visualize manuscript analytics (word counts over time, character appearance frequency, scene pacing graphs) as beautiful, interactive web dashboards.

**Enable when:** You want interactive data visualization dashboards for manuscript analytics.

```json
"vizro-dashboards": {
  "command": "/Users/timothy/mcp-servers/vizro-mcp/venv/bin/vizro-mcp",
  "disabled": true
}
```

---

#### YepCode MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** YepCode API Key  
**Prerequisites:** API key  

YepCode provides a serverless code execution platform -- run code snippets in multiple languages without local setup. Could execute analysis scripts, data transformations, or custom tools on-demand.

**Enable when:** You need to run code snippets in the cloud without local setup.

```json
"yepcode": {
  "command": "npx",
  "args": ["-y", "yepcode-mcp@latest"],
  "env": {
    "YEPCODE_API_KEY": "env:YEPCODE_API_KEY"
  },
  "disabled": true
}
```

---

### M. Communication & Collaboration (Disabled)

---

#### Slack MCP
**Status:** ⬚ Disabled  
**Type:** Official Anthropic  
**API Required:** Slack Bot Token + Team ID  
**Prerequisites:** Slack workspace, bot token  

Slack MCP enables the AI agent to read and send Slack messages, manage channels, and interact with your Slack workspace. Could be used for notifications ("Chapter 12 analysis complete!"), collaboration with beta readers, or integrating writing workflow updates.

**Enable when:** You want AI-Slack integration for notifications or collaboration.

```json
"slack": {
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-slack"],
  "env": {
    "SLACK_BOT_TOKEN": "env:SLACK_BOT_TOKEN",
    "SLACK_TEAM_ID": "env:SLACK_TEAM_ID"
  },
  "disabled": true
}
```

---

#### Linear MCP
**Status:** ⬚ Disabled  
**Type:** Official Linear  
**API Required:** None (OAuth-based)  
**Prerequisites:** Linear account  

Linear is a project management tool. Through MCP, you can create issues, track tasks, manage sprints, and organize your writing workflow. Could track chapter revisions, plot hole fixes, and editing tasks in a structured project management system.

**Enable when:** You want structured project management for your writing workflow.

```json
"linear": {
  "command": "npx",
  "args": ["-y", "mcp-remote", "https://mcp.linear.app/mcp"],
  "disabled": true
}
```

---

#### Figma MCP
**Status:** ⬚ Disabled  
**Type:** Official Figma  
**API Required:** Figma Access Token  
**Prerequisites:** Figma account  

Figma is a design tool. Through MCP, the AI agent can access Figma files, read design specs, and interact with your designs. Could be used for book cover design collaboration, visual storyboarding, or scene layout planning.

**Enable when:** You use Figma for visual design work.

```json
"figma": {
  "command": "npx",
  "args": ["-y", "figma-developer-mcp"],
  "env": {
    "FIGMA_ACCESS_TOKEN": "env:FIGMA_ACCESS_TOKEN"
  },
  "disabled": true
}
```

---

#### Google Workspace MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Google OAuth Client ID + Secret  
**Prerequisites:** Google Cloud project, OAuth credentials  

Google Workspace MCP provides access to Google Drive, Docs, Sheets, and other Google services. Could sync your novel with Google Docs for sharing with editors/beta readers, or use Sheets for structured data.

**Enable when:** You want AI access to your Google Drive/Docs/Sheets.

```json
"google-workspace": {
  "command": "uvx",
  "args": ["workspace-mcp"],
  "env": {
    "GOOGLE_OAUTH_CLIENT_ID": "env:GOOGLE_OAUTH_CLIENT_ID",
    "GOOGLE_OAUTH_CLIENT_SECRET": "env:GOOGLE_OAUTH_CLIENT_SECRET"
  },
  "disabled": true
}
```

---

#### Agent Hub MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

Agent Hub is a universal AI agent coordination platform -- it enables different AI assistants (Claude, Cursor, Qwen, Gemini) to share knowledge and collaborate across projects. Think of it as a shared memory/communication bus between AI agents. Useful if you're running multiple AI tools across machines, but not essential for single-agent workflows.

**Enable when:** You want multiple AI agents to share context and collaborate.

```json
"agent-hub": {
  "command": "npx",
  "args": ["-y", "agent-hub-mcp"],
  "disabled": true
}
```

---

### N. AI & Reasoning (Disabled)

---

#### DeepSeek Thinker MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** DeepSeek API Key  
**Prerequisites:** API key  

DeepSeek Thinker provides access to DeepSeek's reasoning model through MCP. It's an alternative reasoning engine to Sequential Thinking -- useful for getting a "second opinion" on complex narrative decisions from a different AI model.

**Enable when:** You want DeepSeek's reasoning capabilities as an alternative perspective.

```json
"deepseek-thinker": {
  "command": "npx",
  "args": ["-y", "deepseek-thinker-mcp"],
  "env": {
    "API_KEY": "env:DEEPSEEK_API_KEY",
    "BASE_URL": "https://api.deepseek.com"
  },
  "disabled": true
}
```

---

#### Chain of Draft MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** None  

Chain of Draft implements a "drafting" approach to reasoning -- instead of one long chain of thought, it generates multiple short drafts and iteratively refines them. This can produce more creative and varied results for brainstorming tasks where you want multiple options explored quickly.

**Enable when:** You want iterative draft-based reasoning for creative brainstorming.

```json
"chain-of-draft": {
  "command": "npx",
  "args": ["-y", "mcp-chain-of-draft-server"],
  "disabled": true
}
```

---

#### Winston AI MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** Winston AI API Key  
**Prerequisites:** API key  

Winston AI detects AI-generated content and provides originality scores. Run your chapters through it to ensure your prose doesn't inadvertently sound AI-generated, or check that your revisions maintain a human voice. Important for ensuring your novel reads as authentically human-written.

**Enable when:** You want to check your prose for AI-detection and ensure it reads as human-written.

```json
"winston-ai": {
  "command": "npx",
  "args": ["-y", "winston-ai-mcp@latest"],
  "env": {
    "WINSTON_AI_API_KEY": "env:WINSTON_AI_API_KEY"
  },
  "disabled": true
}
```

---

### O. Orchestration (Disabled)

---

#### Zen Orchestrator MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** OpenAI + Google + Anthropic API Keys  
**Prerequisites:** Python venv at /Users/timothy/mcp-servers/zen-mcp-server/, multiple API keys  

Zen MCP provides multi-model orchestration -- it routes tasks to the optimal AI model (GPT-4 for dialogue, Gemini for analysis, Claude for reasoning) based on task type. This is the "multi-model brain" that can leverage different AI strengths for different aspects of writing. Requires multiple API keys to be set up.

**Enable when:** You want to leverage multiple AI models (GPT-4, Gemini, Claude) for different tasks.

```json
"zen-orchestrator": {
  "command": "/Users/timothy/mcp-servers/zen-mcp-server/venv/bin/python",
  "args": ["/Users/timothy/mcp-servers/zen-mcp-server/server.py"],
  "env": {
    "OPENAI_API_KEY": "env:OPENAI_API_KEY",
    "GOOGLE_API_KEY": "env:GOOGLE_API_KEY",
    "ANTHROPIC_API_KEY": "env:ANTHROPIC_API_KEY"
  },
  "disabled": true
}
```

---

#### Cursor Workflow Orchestrator MCP
**Status:** ⬚ Disabled  
**Type:** Custom-Built  
**API Required:** None  
**Prerequisites:** Python 3.11, mcp package  

Cursor Workflow Orchestrator manages complex multi-step writing workflows within Cursor -- coordinating between multiple MCPs to execute pipelines like "read chapter > analyze with editor > check continuity > update knowledge graph > generate report." It's the workflow automation layer for the COMPASS ecosystem.

**Enable when:** You want automated multi-MCP writing pipelines.

```json
"cursor-workflow-orchestrator": {
  "command": "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/CURSOR_WORKFLOW_ORCHESTRATOR_MCP/venv/bin/python",
  "args": [
    "/Users/timothy/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/zz_COMPASS/MCP_Implementations/CURSOR_WORKFLOW_ORCHESTRATOR_MCP/server.py"
  ],
  "disabled": true
}
```

---

### P. Document & Conversion (Disabled)

---

#### Pandoc MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** Pandoc installed  

Pandoc is the "universal document converter" -- it converts between dozens of document formats (Markdown to DOCX, DOCX to PDF, HTML to ePub, etc.). Essential when you need to deliver your manuscript in different formats for editors, agents, or publishers.

**Enable when:** You need to convert manuscripts between formats (Markdown -> DOCX, DOCX -> PDF, etc.).

```json
"pandoc": {
  "command": "uvx",
  "args": ["mcp-pandoc"],
  "disabled": true
}
```

---

#### eBook MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** ePub Library Path  
**Prerequisites:** Python 3.12+ (not currently available)  

eBook MCP provides tools for reading, analyzing, and managing ePub files. Could analyze published ePubs for structure and formatting, or help format your manuscript as an ePub for digital distribution. Currently blocked by Python version requirement (needs 3.12+).

**Enable when:** You have Python 3.12+ and need ePub file management.

```json
"ebook": {
  "command": "python",
  "args": ["-m", "ebook_mcp"],
  "env": {
    "EPUB_LIBRARY_PATH": "env:EPUB_LIBRARY_PATH"
  },
  "disabled": true
}
```

---

### Q. Authentication & SaaS (Disabled)

---

#### Clerk MCP
**Status:** ⬚ Disabled  
**Type:** Official Clerk  
**API Required:** Clerk Secret Key  
**Prerequisites:** Clerk account  

Clerk provides user authentication and management. Only relevant if you're building a web application that needs user login/signup functionality -- not directly related to fiction writing.

**Enable when:** You're building a web app that needs authentication.

```json
"clerk": {
  "command": "npx",
  "args": ["-y", "@clerk/clerk-mcp@latest"],
  "env": {
    "CLERK_SECRET_KEY": "env:CLERK_SECRET_KEY"
  },
  "disabled": true
}
```

---

#### Anki Flashcards MCP
**Status:** ⬚ Disabled  
**Type:** Community  
**API Required:** None  
**Prerequisites:** Anki desktop app + AnkiConnect plugin  

Anki MCP creates spaced-repetition flashcards for memorizing character details, timeline facts, and plot points. Using cognitive science principles, it helps you internalize your novel's world so you can write from deep familiarity rather than constantly referencing notes.

**Enable when:** You want spaced-repetition flashcards for memorizing novel details.

```json
"anki-flashcards": {
  "command": "/Users/timothy/mcp-servers/anki-mcp/venv/bin/mcp-ankiconnect",
  "disabled": true
}
```

---

## GLOSSARY: Key Terms

### What is an MCP?
**MCP (Model Context Protocol)** is a standard created by Anthropic that allows AI assistants (like Claude in Cursor) to use external tools. Think of it like USB ports on your computer -- MCP is the universal standard that lets the AI plug into different tools (search engines, databases, file systems, custom analysis tools) without needing custom integrations for each one. Each "MCP Server" is a small program that provides specific capabilities to the AI.

### What is an API?
**API (Application Programming Interface)** is a way for software to talk to other software. When an MCP needs an API key, it means that MCP connects to an external service (like Firecrawl's web scraping service, or Brave's search engine) and that service requires a password-like "key" to verify you're authorized to use it. API keys are typically free for basic usage with paid tiers for heavy use.

### What is an API Key?
An **API Key** is a unique string of characters (like `sk-abc123...`) that acts as your password to access an external service. You get one by signing up on the service's website. API keys are stored in your `~/.zshrc` file as environment variables so MCPs can access them without the keys being hardcoded in any config files.

### Enabled vs Disabled
- **Enabled** (`"disabled": false`): The MCP launches when Cursor starts and runs as a background process, ready to be called. Uses RAM and CPU.
- **Disabled** (`"disabled": true`): The MCP is configured but NOT running. Zero resource cost. Flip to enabled anytime.

---

## API KEY REFERENCE

This section lists every API key needed across all 66 MCPs, how to get each one, and which MCPs use it.

### Currently Needed (for Enabled MCPs)

| API Key | Environment Variable | Used By | How to Get It | Cost |
|---|---|---|---|---|
| **GitHub Personal Token** | `GITHUB_TOKEN` | github | github.com/settings/tokens > Generate new token (classic) > Select scopes: repo, gist | Free |
| **Anthropic API Key** | `ANTHROPIC_API_KEY` | sequential-thinking-mas, style-emulation | console.anthropic.com > API Keys > Create Key | Pay-per-use (~$3/M input tokens) |
| **Firecrawl API Key** | `FIRECRAWL_API_KEY` | firecrawl | firecrawl.dev > Sign up > Dashboard > API Keys | Free tier: 500 pages/month |

### Needed When You Enable Disabled MCPs

| API Key | Environment Variable | Used By | How to Get It | Cost |
|---|---|---|---|---|
| **Brave Search Key** | `BRAVE_API_KEY` | brave-search | brave.com/search/api > Get API Key | Free tier: 2,000 queries/month |
| **Exa API Key** | `EXA_API_KEY` | exa | exa.ai > Sign up > API Keys | Free tier available |
| **Perplexity API Key** | `PERPLEXITY_API_KEY` | perplexity | perplexity.ai/settings/api > Generate | Pay-per-use |
| **OpenAI API Key** | `OPENAI_API_KEY` | zen-orchestrator, cognee-connections | platform.openai.com > API Keys | Pay-per-use |
| **Google API Key** | `GOOGLE_API_KEY` | zen-orchestrator | console.cloud.google.com > APIs & Services > Credentials | Free tier available |
| **Gemini API Key** | `GEMINI_API_KEY` | imagen3 | aistudio.google.com > Get API Key | Free tier: 60 requests/min |
| **DeepSeek API Key** | `DEEPSEEK_API_KEY` | deepseek-thinker | platform.deepseek.com > API Keys | Pay-per-use (very cheap) |
| **Airtable API Key** | `AIRTABLE_API_KEY` | airtable | airtable.com/account > API section | Free with Airtable account |
| **AssemblyAI API Key** | `ASSEMBLYAI_API_KEY` | assemblyai | assemblyai.com > Dashboard > API Key | Free tier: 100 hours |
| **Apify API Token** | `APIFY_API_TOKEN` | goodreads-scraper | apify.com > Settings > Integrations > API Token | Free tier: $5/month credits |
| **Figma Access Token** | `FIGMA_ACCESS_TOKEN` | figma | figma.com/developers > Personal Access Tokens | Free with Figma account |
| **Slack Bot Token** | `SLACK_BOT_TOKEN` | slack | api.slack.com/apps > Create App > OAuth | Free |
| **Slack Team ID** | `SLACK_TEAM_ID` | slack | Your Slack workspace URL contains it | Free |
| **Supabase Access Token** | `SUPABASE_ACCESS_TOKEN` | supabase | supabase.com > Dashboard > Settings > API | Free tier available |
| **Vectara API Key** | `VECTARA_API_KEY` | vectara | vectara.com > Console > API Keys | Free tier available |
| **Vectara Corpus Key** | `VECTARA_CORPUS_KEY` | vectara | vectara.com > Console > Corpus > Settings | Free tier available |
| **OpenMemory API Key** | `OPENMEMORY_API_KEY` | openmemory, supermemory | openmemory.ai > Dashboard > API | Free tier available |
| **MiniMax API Key** | `MINIMAX_API_KEY` | minimax | minimax.chat > Developer > API Keys | Free tier available |
| **Winston AI API Key** | `WINSTON_AI_API_KEY` | winston-ai | winston.ai > Dashboard > API | Paid plans |
| **Clerk Secret Key** | `CLERK_SECRET_KEY` | clerk | clerk.com > Dashboard > API Keys | Free tier available |
| **YepCode API Key** | `YEPCODE_API_KEY` | yepcode | yepcode.io > Settings > API Keys | Free tier available |
| **PostgreSQL URI** | `POSTGRES_URI` | postgresql, scanadi-ai-memory | Self-hosted or cloud (e.g., Supabase, Railway) | Varies |
| **N8N Credentials** | `N8N_API_KEY`, `N8N_BASE_URL` | n8n-workflow | Self-hosted N8N instance | Self-hosted: free |
| **Airflow Credentials** | `AIRFLOW_BASE_URL`, etc. | apache-airflow | Self-hosted Airflow instance | Self-hosted: free |
| **Label Studio Credentials** | `LABEL_STUDIO_URL`, etc. | label-studio | Self-hosted Label Studio | Self-hosted: free |
| **Google OAuth** | `GOOGLE_OAUTH_CLIENT_ID`, etc. | google-workspace | console.cloud.google.com > OAuth consent | Free |

### How to Add an API Key

1. Get the key from the service's website (see "How to Get It" column above)
2. Open your terminal and edit `~/.zshrc`:
   ```bash
   nano ~/.zshrc
   ```
3. Add the key as an environment variable:
   ```bash
   export FIRECRAWL_API_KEY="fc-your-actual-key-here"
   ```
4. Save and reload:
   ```bash
   source ~/.zshrc
   ```
5. Restart Cursor for MCPs to pick up the new key

### Security Notes
- **NEVER** commit API keys to git. Keys are stored in `~/.zshrc` (your home directory), not in the workspace.
- MCP configs reference keys as `"env:VARIABLE_NAME"` -- this tells the MCP to read the key from your environment, not from the config file.
- Your **GITHUB_TOKEN** is for your **personal** account (timothy-j-smith) only. Your Nike work token is stored separately as `GITHUB_NIKE_TOKEN` and is NOT used by any MCP or git operation.
- Rotate API keys periodically. If a key is compromised, regenerate it on the service's website and update `~/.zshrc`.

---

## CHANGE LOG

| Date | Change | By |
|---|---|---|
| Feb 8, 2026 | Initial Encyclopedia created with all 66 MCPs | Timothy + Claude |
| Feb 8, 2026 | Trimmed from 46 to 20 enabled MCPs for MacBook Air performance | Timothy + Claude |
| Feb 8, 2026 | Swapped Sequential Thinking Brothers #4 and #5 (Ultra=#4, Rust=#5) | Timothy + Claude |
| Feb 8, 2026 | Added Glossary (MCP, API, API Key definitions) and API Key Reference section | Timothy + Claude |

---

*This Encyclopedia is the single source of truth for all MCP configurations. Update it whenever MCPs are added, removed, or their status changes.*
