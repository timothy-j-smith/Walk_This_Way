# Cursor AI: Latest Features & Capabilities (October 2025)

## 🔥 NEWEST CUTTING-EDGE FEATURES

### 1. Plan Mode (Released October 2025)
Plan Mode is Cursor's newest major feature that allows agents to write detailed plans before starting complex tasks, significantly extending how long agents can run. When you prompt Agent to create a plan, Cursor researches your codebase to find relevant files, reviews documentation, and asks clarifying questions. It then creates a Markdown file with file paths and code references that you can edit directly. This addresses the major problem of AI agents generating code hastily without overall architecture planning.

**How to use:** Press Shift + Tab in the agent input to start planning mode. Cursor will automatically suggest plan mode when you describe complex tasks.

### 2. Browser Controls (September 2025)
Agents can now take screenshots, improve UI, and debug client issues using browser capabilities. This enables Cursor to interact with live web applications, test changes in real-time, and debug visual issues—bringing it closer to end-to-end application development.

### 3. Hooks System (Beta - September 2025)
Hooks allow you to observe, control, and extend the Agent loop using custom scripts. You can use Hooks to audit Agent usage, block commands, or redact secrets from context at runtime. Supported lifecycle events include beforeShellExecution, beforeMCPExecution, beforeReadFile, afterFileEdit, and stop.

GitButler was one of the first to implement Hooks, using afterFileEdit and stop hooks to automate version control, with each AI session beginning on a new branch and ending with an AI-generated commit message.

**Power user applications:**
- Block dangerous commands (rm -rf operations)
- Automatically run formatters after code edits
- Redact API keys and secrets before they reach the model
- Create audit trails of all agent actions
- Enforce testing requirements

### 4. Team Rules (September 2025)
Teams can now define and share global rules from the dashboard that will be applied to all projects. Team rules also work with Bugbot, ensuring behavior is consistent across repos. This is crucial for maintaining coding standards across large engineering organizations.

### 5. Agent Autocomplete
When writing prompts, autocomplete suggestions appear based on recent changes. Tab to accept suggestions and attach files to context. This speeds up prompt writing significantly for repetitive tasks.

## MAJOR FEATURES FROM 2025

### Bugbot - Automated PR Code Review (Mid-2025)
Bugbot is a debugging assistant integrated with GitHub that watches code changes and flags potential errors automatically. It's offered as an extra-priced add-on at approximately $40 per person per month.

Bugbot optimizes for detecting the hardest logic bugs with a low false positive rate. During its extensive beta period, Bugbot reviewed over one million pull requests and flagged 1.5 million potential issues. Developers resolved over 50% of the bugs that Bugbot identified, suggesting genuinely actionable feedback.

**Key capabilities:**
- Analyzes PR diffs and leaves comments with explanations and fix suggestions
- Runs automatically on each PR update or manually when triggered
- Supports .cursor/BUGBOT.md files for project-specific context
- "Fix in Cursor" button that jumps directly to the problematic code with pre-filled prompts

### Background Agents (Released June 2025)
Background Agents run in a remote environment provisioned by Cursor, allowing developers to create agents that clone a GitHub repository, work on a separate branch, and push changes asynchronously.

Background agents auto-run all terminal commands (unlike foreground agents which require approval), but this introduces data exfiltration risks through potential prompt injection attacks.

Background agents can be started from Slack or the web app, allowing an agent to take a first pass at a task. Each agent has a unique shareable link for viewing progress and code changes.

**Advanced capabilities:**
- Run in isolated Ubuntu-based machines with internet access and ability to install packages
- Support custom Dockerfiles for machine setup with specific compiler versions and system-level dependencies
- Can be monitored from menubar, web app, mobile, or any browser

### Slack Integration (June 2025)
You can launch Background Agents directly from Slack by mentioning @Cursor. Agents read the entire thread, understand context, and create PRs in GitHub.

Commands include: @Cursor [repo=org/repo] to target specific repositories, @Cursor [branch=dev] to specify branches, and @Cursor [model=o3] to choose AI models.

### Linear Integration (August 2025)
You can now start Background Agents directly from Linear, delegating tasks to Cursor without leaving your issue tracker. The integration allows you to assign issues directly to Cursor agents the same way you assign issues to teammates, with agents updating progress back in Linear.

### Model Context Protocol (MCP) Support
MCP is an open protocol that standardizes how applications provide context and tools to LLMs. MCP servers can be written in any language that can print to stdout or serve an HTTP endpoint.

Cursor supports one-click MCP installation from a curated collection, OAuth authentication for secure access, and both project-specific (.cursor/mcp.json) and global (~/.cursor/mcp.json) configurations.

**Popular MCP servers include:**
- Sequential Thinking (structured problem-solving)
- Puppeteer (browser automation)
- Google Drive, Notion, GitHub, Slack, Sentry, Postgres
- DuckDuckGo Web Search

## LESSER-KNOWN & ADVANCED FEATURES

### Features Most Power Users Don't Know About

**Shareable Deeplinks** - Generate shareable deeplinks for reusable prompts, useful for setup instructions in documentation, team resources, and sharing workflows.

**Slash Commands & Custom Commands** - You can create reusable prompts stored in .cursor/commands/[command].md. Run them by typing / in the Agent input and selecting from the dropdown. Teams use these for running linters, fixing compile errors, and creating PRs with conventional commits.

**Sandboxed Terminal Execution** - Commands now execute in a secure, sandboxed environment. Non-allowlisted commands automatically run in a sandbox with read/write access to your workspace and no internet access.

**Memories Feature (Beta)** - Memories stores and references facts from previous AI chats, creating a persistent knowledge base for each project. This eliminates the need to repeat project specifics or coding conventions.

### Advanced Context Management
- @Files, @Folders, @Code, @Docs, @Web, and @Git mentions give Cursor precise context
- .cursorrules file provides persistent instructions about coding style and project-specific context
- Notepads for documenting architecture decisions and reusable templates
- @Web searches the web and includes PDFs in context

### Tab Model Improvements
A new Tab completion model rolled out in 2025 with smarter refactors, better context, and noticeably faster performance. The Tab model can now suggest changes across multiple files, excelling at refactors, edit chains, and jumping between related code.

### Jupyter Notebook Support
Agents can now implement changes in Jupyter Notebooks, creating and editing multiple cells directly (Sonnet models only).

### GitHub PR Agent Integration
Agents can be used directly inside GitHub pull requests. Tag @Cursor and the Agent will read the prompt, apply the fix, and push a commit.

### Compact Mode
Compact mode hides tool icons, collapses diffs by default, and auto-hides input when idle—useful for long sessions with many tool calls.

### Advanced Agent Steering
Sending messages while Cursor is working now steers the agent better. ⌥+Enter queues messages, ⌘+Enter interrupts immediately to send messages.

## TECHNICAL ARCHITECTURE & SECRET CAPABILITIES

### Proprietary Models
Cursor has developed its own custom "Tab" autocomplete model that predicts your next actions, and a codebase embedding model that gives Agent deep understanding and recall. Cursor's development of its own models signals a strategic shift toward independence from third-party providers, with expectations for significant 2026 investment in proprietary models optimized for coding tasks.

### Model Support
Cursor supports multiple frontier models: GPT-5, Claude Sonnet 4.5, Claude Opus 4.1, Gemini 2.5 Pro, and Grok Code. Claude 3.7 Sonnet is the most popular model as of April 2025, followed by Gemini 2.5 Pro, while o3 is the fastest-growing model.

### Advanced Codebase Understanding
Recent improvements for large codebases include: Read file now reads full files when appropriate with 2MB cap removed; List can explore full directory trees in one call; Grep has improved matching with less noise; and Codebase Search has better ranking and indexing.

## WHAT'S IN DEVELOPMENT / ROADMAP

### Confirmed 2026 Direction
Based on funding announcements and development patterns, here's what's likely coming:

**Deeper Enterprise Integrations** - Expect deeper integrations with JIRA for enterprise teams, GitHub Issues for open-source projects, and DevOps pipelines for continuous deployment.

**Voice and Conversational Control** - As agents become more capable, voice control seems inevitable—imagine describing a feature verbally while commuting, then arriving to review the agent's implementation.

**Organization-Wide Knowledge Bases** - Memory systems will likely expand beyond project-level to organization-wide knowledge bases, building institutional knowledge that persists across projects and team members.

**Self-Correcting Test Loops** - An anticipated feature where AI can iteratively fix errors by running tests and refining code until all tests pass.

**Proprietary Model Development** - Expect significant investment in proprietary models optimized specifically for coding tasks, understanding Cursor's unique agent architecture and user patterns.

### Research Focus Areas
Cursor's "Problems for 2024-2025" roadmap details: Next Action Prediction for smoother code navigation; Perfect Edits with scaled computation for complex code changes; and Optimal Context with advanced retrieval and long-context processing.

## BUSINESS & COMPETITIVE POSITION

### Valuation & Funding
In June 2025, Anysphere raised $900 million at a $9.9 billion valuation, led by Thrive Capital, with participation from Andreessen Horowitz, Accel, and DST Global. The company's ARR has been doubling approximately every two months.

### Rejected Acquisition Offers
OpenAI reportedly explored a $3 billion acquisition attempt. Anysphere declined, choosing to scale independently and raise capital on its own terms.

### Market Position
Cursor is used by over half of the Fortune 500, including NVIDIA, Uber, and Adobe. Bloomberg dubbed Anysphere as "the fastest growing startup ever".

### Pricing Tiers
- **Free/Hobby:** Limited features
- **Pro:** $20/month - unlimited Tab and Auto usage plus monthly credit for model calls
- **Ultra:** $200/month - 20× more model usage and priority features
- **Team/Business:** Starting at $40/user/month - adds privacy mode and SSO
- **Enterprise:** Custom pricing - adds SCIM provisioning, priority support, dedicated account manager

**Add-ons:**
- Bugbot: ~$40/user/month
- Background Agents: Included in Pro+ plans

## SECURITY & PRIVACY

Cursor runs on SOC 2 Type II-compliant AWS infrastructure. With privacy mode enabled, models don't retain any code or chat prompts for training, and Cursor only holds code in memory for the duration of an AI request. Enterprise customers get privacy mode enforced by default.

**Important limitation:** Cursor doesn't offer self-hosting—you can't run it entirely within your own VPC.

## COMPETITIVE LANDSCAPE

**Main Competitors:**
- GitHub Copilot: First-party VS Code integration, simpler but less powerful
- Windsurf (Codeium): $15/month Pro plan, lighter-weight feel
- Claude Code: Command-line based, winning praise for AI quality
- Devin: More agentic but reportedly less stable

The pace of change in this crowded market makes it challenging for developers to know which AI assistants to adopt.

## RISKS & CHALLENGES

Key risks include: expensive model inference costs that could pressure margins; AI-generated code potentially introducing subtle bugs or vulnerabilities; security concerns around prompt injection attacks; intense competition from GitHub, Google, and other well-funded players; and the challenge of maintaining explosive growth indefinitely.

## COMMUNITY & ECOSYSTEM

**Active Community Resources:**
- Official Cursor Forum (forum.cursor.com)
- GitHub repository for wiki and issues
- Extensive third-party tutorials and guides
- Growing ecosystem of MCP servers and integrations
- Community-developed Cursor rules and prompts

## BOTTOM LINE: WHAT MAKES CURSOR UNIQUE

- **Native AI-First Architecture:** Unlike plugins, Cursor is built from the ground up for AI
- **Multi-File Agent Capabilities:** Can coordinate changes across entire codebases
- **Autonomous Background Execution:** True parallel AI development
- **Enterprise-Grade Security:** SOC 2 compliance with zero-retention privacy mode
- **Ecosystem Play:** MCP support, Slack/Linear integrations, team collaboration features
- **Proprietary Models:** Custom Tab and embedding models for better performance
- **Rapid Innovation Pace:** Weekly releases with major features every month

**The Secret Sauce:** Cursor's technical moat comes from codebase understanding through custom embedding models combined with AI research capabilities, not just layering AI on top of existing editors.

---

*This report represents the most comprehensive analysis of Cursor as of October 2025, covering everything from the latest Plan Mode and Browser Controls to the under-the-radar Hooks system and advanced MCP integrations. The platform is evolving from a smart editor into a complete autonomous development platform.*
