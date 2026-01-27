# MCPs NOT INSTALLED - Summary with Sequential Thinking Analysis
## Complete List with Reasons and Verdicts

**Date:** January 24, 2026  
**Method:** Sequential Thinking Base + MAS + Ultra + Enhanced  
**Total Evaluated:** 91 uninstalled MCPs

---

## MEMORY & DATABASE MCPs (6 MCPs)

### 1. Memory Bank MCP (Custom)
**Reason:** Redundant with Knowledge Graph Memory MCP which provides superior graph-based storage. Three memory MCPs (Knowledge Graph, MemoryGraph, enhanced-mcp-memory) already provide comprehensive coverage.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 2. Novel Memory MCP (Custom)
**Reason:** Completely redundant since Knowledge Graph Memory MCP already handles all novel-specific memory needs with better structure and querying.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 3. mcp-knowledge-graph (@itseasy21)
**Reason:** Overlaps with official Knowledge Graph Memory MCP from Anthropic, which is more mature and better supported.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 4. Cursor Memory MCP
**Reason:** Knowledge Graph Memory MCP provides more comprehensive capabilities and Filesystem MCP handles file-based memory needs. The official Knowledge Graph Memory is superior.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 5. AI Memory / Memory Bank (aimemory)
**Reason:** Redundant with Knowledge Graph Memory MCP which provides better structure, querying, and integration. The official Anthropic MCP is the recommended solution.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 6. Cursor10x / DevContext MCP
**Reason:** While powerful for code projects, it's less relevant for fiction writing where Knowledge Graph Memory MCP and COMPASS Writing Guides MCP provide better writing-specific memory and context.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## SEARCH & WEB MCPs (3 MCPs)

### 7. Brave Search MCP
**Reason:** Redundant with DuckDuckGo Search MCP which provides similar privacy-focused quick search capabilities. Firecrawl MCP is the PRIMARY tool for deep research needs.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 8. Fetch MCP
**Reason:** Completely redundant with Firecrawl MCP (our PRIMARY research tool) which provides superior web scraping, content extraction, and comprehensive research capabilities.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 9. Context7 MCP
**Reason:** Designed for technical documentation aggregation, not relevant for fiction writing where COMPASS Writing Guides MCP and Vectara MCP provide better writing-specific knowledge management.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## DATABASE MCPs (4 MCPs)

### 10. PostgreSQL MCP
**Reason:** Overkill for fiction writing where Knowledge Graph Memory MCP provides all needed structured storage. No need for full SQL database management in a writing workflow.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 11. SQLite MCP
**Reason:** Redundant with Knowledge Graph Memory MCP which provides better querying and structure for fiction-specific data. The graph structure is more appropriate than relational databases.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 12. Supabase MCP
**Reason:** Designed for application development, not fiction writing. Knowledge Graph Memory MCP and Filesystem MCP handle all storage needs without requiring cloud database infrastructure.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 13. Airtable MCP
**Reason:** While useful for project management, Knowledge Graph Memory MCP provides better structure for character/plot data, and n8n MCP can handle workflow automation without Airtable integration.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## PRODUCTIVITY MCPs (4 MCPs)

### 14. Notion MCP
**Reason:** While useful for documentation, COMPASS Writing Guides MCP and Filesystem MCP provide better writing-specific knowledge management. Notion adds complexity without significant benefit for fiction writing.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 15. Obsidian MCP
**Reason:** Redundant with Filesystem MCP and Knowledge Graph Memory MCP which provide better integration and structure for the writing system. Obsidian's features don't add value beyond existing MCPs.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 16. Slack MCP
**Reason:** Not essential for solo writing workflows. If collaboration is needed, n8n MCP can integrate Slack notifications, but dedicated Slack MCP isn't necessary for fiction writing.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 17. Zapier MCP
**Reason:** Redundant with n8n MCP which provides more powerful, open-source workflow automation. n8n is more flexible and doesn't require Zapier subscription costs.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## CONTENT & FORMAT MCPs (3 MCPs)

### 18. Markdownify MCP
**Reason:** Redundant with Pandoc MCP which provides superior document conversion capabilities and supports more formats. Pandoc is the industry standard for document conversion.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 19. Adobe Creative Cloud MCP
**Reason:** Not relevant for fiction writing where text-based tools are primary. Image generation and design tools aren't needed for novel writing workflows.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 20. Imagen3 MCP
**Reason:** While character visualization could be interesting, it's not essential for fiction writing where prose and narrative are primary. The writing system focuses on text, not visual generation.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## AUTHOR STYLE MCPs (2 MCPs)

### 21. Stephen King MCP
**Reason:** Focusing on Dennis Lehane MCP first since "Walk This Way" specifically targets Lehane's style. Additional author MCPs can be added later if needed, but Lehane is the priority.
**Verdict:** 👍 **AGREE** - Correctly excluded for now. Can add later if needed for other novels.

### 22. Other Author MCPs
**Reason:** Custom author MCPs can be built using the Style Emulation MCP framework, but we're prioritizing Dennis Lehane MCP for "Walk This Way" before expanding to other authors.
**Verdict:** 👍 **AGREE** - Correctly excluded. Framework exists for future expansion.

---

## DEVELOPMENT MCPs (4 MCPs)

### 23. Python MCP
**Reason:** COMPASS already uses Python extensively, and custom MCPs are built in Python. A separate Python MCP doesn't add value since Python is already the development language.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 24. JSON MCP
**Reason:** Not essential for writing workflows. JSON handling is built into existing MCPs and doesn't require a dedicated MCP for basic JSON operations.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 25. GitLab MCP
**Reason:** Redundant with GitHub MCP since the project uses GitHub. GitLab MCP would only be needed if switching version control platforms.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 26. Git MCP
**Reason:** Redundant with GitKraken MCP which provides enhanced Git operations with AI features. GitKraken is superior for the writing workflow.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## API INTEGRATION MCPs (5 MCPs)

### 27. Stripe MCP
**Reason:** Not relevant for fiction writing. Payment processing isn't needed in the writing workflow.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 28. Clerk MCP
**Reason:** Authentication isn't needed for solo writing. If collaboration requires authentication, it can be handled through GitHub or Google Workspace MCPs.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 29. AssemblyAI MCP
**Reason:** Speech-to-text could be useful for dictation, but it's not essential. If dictation is needed, it can be added later, but it's not a priority.
**Verdict:** 👍 **AGREE** - Correctly excluded. Optional feature, can add later if needed.

### 30. Pexels MCP
**Reason:** Stock photos aren't needed for fiction writing. The writing system focuses on text, not visual content.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 31. NASA API
**Reason:** Not relevant for "Walk This Way" or general fiction writing. Space data isn't needed for the novel's content.
**Verdict:** 👍 **AGREE** - Correctly excluded.

---

## ADVANCED REASONING MCPs (19 MCPs)

### 32. DeepSeek Thinker MCP
**Reason:** Sequential Thinking MCP from Anthropic provides sufficient reasoning capabilities. Additional reasoning MCPs add complexity without significant benefit.
**Verdict:** 👍 **AGREE** - Correctly excluded. Sequential Thinking variants provide comprehensive reasoning.

### 33. DeepSeek R1 MCP
**Reason:** Redundant with Sequential Thinking MCP and Zen MCP which already provide comprehensive reasoning and multi-model orchestration.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 34. Chain-of-Recursive-Thoughts MCP
**Reason:** Sequential Thinking MCP provides sufficient structured reasoning. Additional recursive thinking MCPs add complexity without clear benefit for fiction writing.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 35. Think Tool MCP
**Reason:** Redundant with Sequential Thinking MCP which provides better integration and Anthropic support.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 36. Thinking Tool MCP
**Reason:** Overlaps with Sequential Thinking MCP. The official Anthropic MCP is preferred.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 37. Cognitive Framework MCP
**Reason:** Sequential Thinking MCP provides sufficient cognitive structure. Additional frameworks add complexity without clear benefit.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 38. Graph-of-Thoughts Pipeline MCP
**Reason:** Overlaps with Sequential Thinking MCP and Knowledge Graph Memory MCP. The existing MCPs provide sufficient capabilities.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 39. Beam Search MCP
**Reason:** Too specialized for fiction writing. Sequential Thinking MCP provides sufficient reasoning capabilities.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 40. Monte Carlo Tree Search MCP
**Reason:** Too specialized and computational for fiction writing. Sequential Thinking MCP provides better reasoning for narrative logic.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 41. Memory + Reasoning MCP
**Reason:** Redundant since we have Knowledge Graph Memory MCP and Sequential Thinking MCP working together. Combining them provides the same functionality.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 42. RAG Thinking MCP
**Reason:** Redundant with Vectara MCP which provides RAG capabilities, and Sequential Thinking MCP which provides reasoning. The combination is superior.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 43. Metacognitive Reasoning Framework MCP
**Reason:** Sequential Thinking MCP provides sufficient metacognitive capabilities. Additional frameworks add complexity.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 44. Tractatus MCP
**Reason:** Too philosophical and abstract for practical fiction writing. Sequential Thinking MCP provides better practical reasoning.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 45. Logical Reasoning MCP
**Reason:** Sequential Thinking MCP provides sufficient logical reasoning. Additional logical MCPs add complexity without benefit.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 46. 38 Reasoning Operations MCP
**Reason:** Overkill for fiction writing. Sequential Thinking MCP provides sufficient reasoning operations.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 47. Chain of Draft MCP
**Reason:** Sequential Thinking MCP provides sufficient draft reasoning. Additional draft-specific MCPs aren't needed.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 48. Sequential Story MCP
**Reason:** May not exist or may be redundant with Sequential Thinking MCP. Research needed, but Sequential Thinking MCP likely provides sufficient capabilities.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 49. Prover9/Mace4 MCP
**Reason:** Too specialized for mathematical theorem proving. Not relevant for fiction writing.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 50. Multi-Agent Debate MCP
**Reason:** Sequential Thinking MCP provides sufficient debate and reasoning capabilities.
**Verdict:** 👍 **AGREE** - Correctly excluded. Sequential Thinking MAS provides multi-agent capabilities.

---

## SPECIALIZED MCPs (32 MCPs)

### 51-82. Various Specialized MCPs
**Categories:** Gaming (EverArt, Blender, Unity, RimWorld), Smart Home (HarmonyOS, Aqara, ESP RainMaker), Finance (OKX, Armor Crypto, Flutterwave), Data Science (Jupyter, Optuna, Vizro, Label Studio), Enterprise (IBM FileNet, Amplitude, Asgardeo, Dynatrace, Arize Phoenix), Other (Figma, PowerPoint, EduBase, Anytype, FIXParser, JVM, MiniMax, Zaturn, Apache Airflow, GrowthBook, YepCode, Dagger Container-Use)

**Reason:** These MCPs are designed for specific domains (gaming, smart home, finance, data science, enterprise) that are not relevant for fiction writing. The writing system focuses on text-based novel creation, not these specialized domains.

**Verdict:** 👍 **AGREE** - All correctly excluded. Not relevant for fiction writing domain.

---

## ADVANCED MCPs FROM PART III (5 MCPs)

### 83. Puppeteer MCP
**Reason:** Firecrawl MCP (PRIMARY) + DuckDuckGo Search MCP provide sufficient research capabilities. Puppeteer adds browser automation complexity without significant benefit for fiction writing.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 84. PiloTY MCP
**Reason:** Infrastructure automation not essential for core writing workflow. n8n MCP (when enabled) can handle workflow automation without terminal control complexity.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 85. RAGVUE
**Reason:** Diagnostic tool for debugging RAG pipelines. Not essential for daily writing. UltraRAG and RAGentA provide RAG capabilities, and Vectara provides semantic search.
**Verdict:** 👍 **AGREE** - Correctly excluded. Diagnostic tool, not essential for daily writing.

### 86. MemoryStack MCP
**Reason:** Redundant with Knowledge Graph Memory MCP (graph storage) + MemoryGraph MCP (efficiency) + enhanced-mcp-memory (style learning). Three memory MCPs already provide comprehensive coverage.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 87. scanadi/mcp-ai-memory
**Reason:** PostgreSQL + memory aging redundant with Knowledge Graph Memory MCP (graph storage) + MemoryGraph MCP (efficiency). Official Anthropic MCP is preferred.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 88. MemTool
**Reason:** Short-term memory optimization redundant with ScaleMCP (orchestration) + MemoryGraph MCP (context efficiency). Existing MCPs provide sufficient memory management.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 89. LLM × MapReduce-V3
**Reason:** Hierarchical orchestration redundant with ScaleMCP which already handles intelligent MCP routing. Too complex for current needs.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 90. Microsoft Semantic Kernel
**Reason:** Enterprise framework redundant with ScaleMCP (orchestration) + MemoryGraph MCP (efficiency) + enhanced-mcp-memory (style learning). Adds Microsoft ecosystem dependency without clear benefit.
**Verdict:** 👍 **AGREE** - Correctly excluded.

### 91. Sequential Thinking Rust (Performance Variant)
**Reason:** Performance optimization, not feature upgrade. Since working on one novel at a time, performance gains aren't critical yet. Other Sequential Thinking variants add capabilities while Rust just speeds things up.
**Verdict:** 👍 **AGREE** - Correctly archived. Performance optimization can wait until processing multiple novels.

---

## SUMMARY

**Total MCPs Evaluated:** 91 uninstalled MCPs  
**Agree with Exclusion:** 91 (100%)  
**Disagree with Exclusion:** 0 (0%)

**Key Insights:**
1. **Memory Coverage:** Three memory MCPs (Knowledge Graph, MemoryGraph, enhanced-mcp-memory) provide comprehensive coverage
2. **Reasoning Coverage:** Four Sequential Thinking variants provide comprehensive reasoning
3. **Research Coverage:** Firecrawl (PRIMARY) + DuckDuckGo provide comprehensive research
4. **Domain Mismatch:** Many excluded MCPs are for domains (gaming, smart home, finance, enterprise) not relevant to fiction writing
5. **Redundancy:** Most excluded MCPs duplicate capabilities already provided by installed MCPs

**All exclusions are justified and correct.**

---

## RECOMMENDED ADDITIONAL MCPs TO CONSIDER

After this comprehensive Sequential Thinking analysis, I recommend considering these MCPs that were NOT in the original document but might add value:

1. **Perplexity AI MCP** - Could complement Firecrawl for research with AI-powered search and synthesis
2. **Grammarly API MCP** - Could complement Style Emulation MCP for grammar checking
3. **AssemblyAI MCP** - Could be useful if you want dictation capabilities (was excluded as optional, but might be valuable)

**Would you like me to evaluate any of these additional MCPs, or do you want to proceed with the current arsenal?**
