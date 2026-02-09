# COMPASS Enhancement Research Guide
## Synthesizing research → COMPASS ingredients (techniques, nuggets, experiments)
**Date:** January 26, 2026  
**Location:** `zz_COMPASS/Archive/` — out of the way, available for reference, avoids duplicating work  
**Template:** `JAZZ_CHAT_ANALYSIS.md` (project root)

---

## WHAT THIS IS FOR

**Input:** Your research — chats with agents (e.g. JAZZ), Cursor/Claude discovery sessions, notes, docs. *Not* MCP candidates (those use `MCP_EVALUATION_GUIDE.md`).

**Output:** COMPASS enhancement ingredients:
- **Techniques to implement** — e.g. XML tags, context pinning, chain-of-thought (JAZZ-style)
- **Nuggets to document** — concepts worth capturing (e.g. code-to-fiction mapping, AI-helping-AI)
- **Experiments to try** — things to test (e.g. temperature, extended thinking)
- **What’s already covered** — by your current MCP stack, so you don’t duplicate

**Purpose:** Surface Cursor/Claude “secret sauce” and workflow improvements that make COMPASS better — not new MCPs.

---

## WHAT TO DO NEXT (every time you have research to synthesize)

### 1. Add your research

- **In this chat (or any chat):** Paste the research, or `@` the file(s), or attach.  
- **New chat:** Same — paste or `@` the research. Optionally `@` this guide and `@JAZZ_CHAT_ANALYSIS.md` so the template is in context.

### 2. Type a short instruction — no special MCP command needed

You do **not** need to “initiate” or “prompt” the Sequential Thinking MCP by name. Cursor Claude will use structured analysis (and Sequential Thinking if it’s enabled) when it’s useful. You just need a clear ask.

**Use either of these (or your own words):**

- **Short:**  
  *“Analyze this research and make recommendations for COMPASS — what should be applied?”*

- **Full (for consistency):**  
  *“Analyze this research and make recommendations for COMPASS. Use this guide and JAZZ_CHAT_ANALYSIS as the template. Output: (1) techniques to implement, (2) nuggets to document, (3) experiments to try, (4) what’s already covered by MCPs so we don’t duplicate.”*

If you want a single repeatable line, use the **Full** line above and paste it whenever you start a synthesis.

### 3. What happens

Cursor Claude will:

- Use this guide and the JAZZ analysis as the format.
- Treat your research like the JAZZ chat: identify features/ideas, categorize by value (Critical / High-Value / Experimental / Already covered).
- Produce: techniques to implement, nuggets to document, experiments to try, and “already covered by MCPs.”
- Use Sequential Thinking MCP when it helps for multi-step reasoning — no extra step required from you.

---

## OPTIONAL: saved prompt/command

You don’t *need* a formal command. Typing something like *“Analyze this research and make recommendations for COMPASS”* is enough.

If you want a **repeatable prompt**:

- Save the **Full** instruction above in a file (e.g. `zz_COMPASS/Archive/ENHANCEMENT_RESEARCH_PROMPT.txt` or a Cursor rule).
- When you have new research: paste that prompt, then paste or `@` the research. Same effect, less to remember.

**No need to “invoke” an MCP** — just ask for the analysis in natural language.

---

## SYNTHESIS OUTPUT FORMAT (JAZZ-style)

When you ask for analysis, the output should follow the JAZZ template:

1. **Executive summary** — Steps used, verdict (e.g. “X techniques to implement, Y nuggets to document, Z experiments”).
2. **Chat/source summary** — What the research was about, who was involved, main themes.
3. **Critical / high-value items** — Each with: What it is, status vs your system, why it matters, how to implement, verdict (Implement / Document / Test).
4. **What NOT to add** — Already covered by MCPs or existing COMPASS pieces.
5. **Consensus and priority order** — What to do first, second, etc.

Reference: open `JAZZ_CHAT_ANALYSIS.md` for the exact structure and tone.

---

## WHEN TO USE THIS vs MCP EVALUATION

| You have… | Use… |
|-----------|------|
| Chats, agent sessions, Cursor/Claude discovery, notes, “secret sauce” research | **This guide** — COMPASS Enhancement Research |
| New MCPs or tools to add/replace in the stack | **MCP_EVALUATION_GUIDE.md** — Step 0 (COMPASS capability) + Augment/Replace/Reject |

MCP stack is in a good place; this guide is for **enhancement research synthesis**, not MCP hunting.

---

## ARCHIVE: DON’T DUPLICATE

This folder (`zz_COMPASS/Archive/`) is for:

- This guide.
- Completed synthesis outputs (e.g. “Research X – COMPASS synthesis”) so you can refer back and avoid redoing the same research or conclusions.

Store finished syntheses here when they’re done — and skim before starting new research to avoid repeating work.

---

*Last updated: January 26, 2026*
