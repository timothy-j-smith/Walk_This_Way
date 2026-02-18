# STEPHEN KING MCP — "The Writer's Toolbox"

**Status:** PRIVATE & CONFIDENTIAL — Design Document  
**Date Created:** February 12, 2026  
**Last Updated:** February 18, 2026  
**Version:** Pre-Build Design v1.0  

---

## PRIVATE & CONFIDENTIAL

- For Timothy and Claude's internal use only
- NOT shared publicly
- NOT in public repositories
- Keep local/private

---

## PURPOSE

A Private & Confidential Stephen King Style Emulation + Craft Education Engine. Built as a companion to Timothy's A.B.S.H. writing system (Architecture, Brick, Scalpel, Hose). Designed to educate, collaborate, and provide honest professional feedback through the lens of Stephen King's craft philosophy.

**This MCP is fundamentally different from the Dennis Lehane MCP:**

| Dennis Lehane MCP | Stephen King MCP |
|---|---|
| Literary analysis of technique (reference) | Craft philosophy as educational engine (tool) |
| "How does HE create that effect?" | "How do YOU become a better writer?" |
| 4 tools, single mode | 3 tools, 3 modes, 3 liberty levels |
| Project-specific (Walk This Way) | Universal (all projects, all novels) |

---

## SOURCES

- Stephen King: *On Writing: A Memoir of the Craft*
- writing_guides.json: King philosophy (lines 18-86), King quotes (lines 759-793), Scalpel & Hose Philosophy (lines 829-970)
- king.md: Style command reference
- Professional book reviews and critical author analysis
- Timothy's A.B.S.H. system developed through months of experimentation

**Disclaimer:** NOT plagiarism — style analysis and craft education only. Fair use for educational purposes.

---

## THE 3-3-3 ARCHITECTURE

Everything is organized in threes: 3 Tools, 3 Modes, 3 Liberty Levels.

### 3 Tools (What the MCP Can Do)

| Tool | Function | Maps to A.B.S.H. |
|---|---|---|
| **king_imagine** | Situations, stakes, fear, planning — the idea phase | **A** (Architecture) |
| **king_craft** | Voice, pacing, telepathy, building — the writing phase | **B** (Brick) |
| **king_revise** | Cutting and adding — the editing phase | **S + H** (Scalpel & Hose) |

**Teaching is woven into every tool.** No separate TEACH tool — King's principles surface naturally in context, right when needed. Any tool explains "why" when asked.

### 3 Modes (What You Want to Do)

Ordered by input size: idea < draft < manuscript.

| Mode | What It Does | Default Liberty Level |
|---|---|---|
| **1. CREATE** | Idea → story. Build from a seed: an image, a sentence, an outline | Nice |
| **2. TRANSFORM** | Draft → better draft. The convenience store. Quick, targeted improvement | Neutral |
| **3. EDIT** | Chapters → mastery. The full treatment. Deep editing + education | Professional |

### 3 Liberty Levels (How Feedback Is Delivered)

| Level | When to Use | What It Sounds Like |
|---|---|---|
| **NICE** | Early ideas, first drafts, fragile moments | "This has real energy. The core idea is compelling. Here's what could make it even stronger..." |
| **NEUTRAL** | Middle drafts, working sessions, honest check-ins | "This works because X. This doesn't work because Y. Here's what to change." |
| **PROFESSIONAL** | Final drafts, pre-submission, when you need the real number | "This is at a 5/10. Paragraphs 2-4 fail because the pacing drags. Here's the revision plan." |

**Critical Rule: NICE ≠ DISHONEST.** All levels are honest. The difference is delivery, not truth.

A 4/10 scene at each level:

- **Nice:** "The core situation here is strong — a father confronting his son's silence. The emotion is real. The dialogue needs to earn that emotion more specifically. Here are three concrete ways to deepen it..."
- **Neutral:** "The situation works. The dialogue doesn't. It's telling us what the characters feel instead of showing. Revision focus: cut expository lines, add one specific physical detail per exchange."
- **Professional:** "This scene is at 4/10. The father's motivation isn't established before the confrontation, so the emotion is unearned. Three specific failures: [list]. Revision plan: [plan]."

---

## SMART DEFAULTS

Each mode has a natural default liberty level. You can just say "King Create" and the default kicks in. Override anytime by specifying the level.

| Mode | Default Level | Why |
|---|---|---|
| Create | Nice | Early ideas need protection. Fuel the rocket. |
| Transform | Neutral | Quick fixes need honest balance. |
| Edit | Professional | Deep review should be rigorous. You're here because you're ready. |

### The Full Grid (9 Possible Combinations)

| | Nice | Neutral | Professional |
|---|---|---|---|
| **King Create** | **King Create Nice** *(default)* | King Create Neutral | King Create Professional |
| **King Transform** | King Transform Nice | **King Transform Neutral** *(default)* | King Transform Professional |
| **King Edit** | King Edit Nice | King Edit Neutral | **King Edit Professional** *(default)* |

---

## NAMING CONVENTION

**King [Mode] [Level]**

- **King** first — the MCP identity (WHO)
- **Mode** second — what you're doing (WHAT)
- **Level** third — how you want feedback (HOW)

Examples:
- `King Create Nice` — nurturing an early idea
- `King Transform Neutral` — balanced quick polish
- `King Edit Professional` — full rigorous review
- `King Create Professional` — rigorous planning, no hand-holding
- `King Edit Nice` — deep review with encouragement first

Or just talk naturally — the agent figures out the routing:
- "I have an idea about a father and son" → King Create (Nice implied)
- "Tighten up this paragraph" → King Transform (Neutral implied)
- "Review these three chapters" → King Edit (Professional implied)

---

## THE 3 SCENARIOS (Natural Workflows)

Scenarios are not tools or modes — they're patterns of how the tools get used together.

### Scenario 1: CREATE — "I have an idea. Help me build it."

- Smallest input (an image, a sentence, a seed)
- Biggest transformation (idea becomes story)
- Uses: king_imagine → king_craft → king_revise (full A.B.S.H. journey)
- Example: "A Black cowboy rides his horse down the city streets of Portland, Oregon in 1993."
- The Phantom Cowboy origin story — a single image that becomes a novel

### Scenario 2: TRANSFORM — "I have a draft. Make it better, quick."

- Medium input (a paragraph, a scene, a short story)
- Medium transformation (your prose, sharpened)
- Uses: king_revise in Transform mode
- The convenience store — in, out, better
- Example: "Rewrite this paragraph like King would"

### Scenario 3: EDIT — "I have chapters. Give me everything."

- Largest input (chapters, a whole story, a novel)
- Deepest engagement (full teaching + editing)
- Uses: king_revise in Edit mode with Learn depth
- Full `<<agent notes>>`, revision report, before/after diff
- High time investment, highest learning payoff

---

## INLINE NOTES SYSTEM

A dialogue between writer and editor that lives inside the text itself.

### The Notation

- `<<Agent note: explanation of why this change was made>>` — editorial commentary
- `((Author note: my thoughts, reactions, ideas))` — author responses

### The Diff View

- **Green text** = new/improved prose (additions and replacements)
- **Red text** = old prose being cut or replaced
- Author hits "Keep" on changes they accept

### The Revision Report

A summary at the end of Edit mode, grouping changes by principle:
- What was changed and why
- Grouped by category (pacing, voice, telepathy, etc.)
- Available on request — skipped when not wanted

---

## AGENT GUIDELINES

Behavioral rules encoded in the MCP data so ANY agent consulting it interacts consistently.

### Honesty Protocol

- **Never rate above what the prose earns.** A 4 is a 4. Say it directly. Then say how to make it a 6.
- **No flattery.** Encouragement is fine. Lying is not.
- "This scene has real potential and here's what needs to change" = honest.
- "This is Pulitzer material" when it's a first draft = dishonest.
- **The Phantom Cowboy Lesson:** Timothy was told a draft was 8.5-9/10 (Pulitzer-quality) by an AI agent. Beta readers rated it 2/10. He invested real money, time, and emotional energy based on false feedback. This MCP exists in part to prevent that from ever happening again. Honest feedback protects the author.

### A.B.S.H. Process Awareness

The author works in Architecture, Brick, Scalpel, Hose cycles:
- **A** (Architecture): Planning, ideation, story structure
- **B** (Brick): Building paragraph by paragraph, chapter by chapter
- **S** (Scalpel): Cutting purple prose, killing darlings, eliminating noise
- **H** (Hose): Flushing with truth, meaning, specificity, earned emotion

Respect this process. Don't reorganize the author's workflow.

### Neurodiversity-Informed Interaction

The author has dyslexia, ADHD, and ASD:
- He learns by **DOING**, not by reading theory first
- **Visual learning** is primary — diff views, before/after comparisons
- **In-context teaching** over separate lectures — show changes, explain them in place
- **Concrete and specific** over abstract — "this adverb weakens this verb" not "adverbs are generally considered weak"
- **No homework assignments** — learning happens naturally through the writing process
- He sees the movie first, then reads the book (visual-first processing)
- Keep explanations brief and tied to specific examples

### Smart Defaults

- Default liberty levels per mode (Create→Nice, Transform→Neutral, Edit→Professional)
- Agent infers mode from natural language — author doesn't need to specify codes
- Override any default by adding the level: "King Create Professional"

---

## CREATIVE SETTINGS

Per-tool temperature and Top_P optimization for King's creative, vivid, surprising prose style.

| Tool / Context | Temperature | Top_P | Rationale |
|---|---|---|---|
| king_imagine (situations, ideas) | 0.95 | 0.95 | Maximum creative spark for brainstorming |
| king_craft (voice, building) | 0.92 | 0.95 | Diverse, authentic, surprising vocabulary |
| king_revise — Create mode | 0.92 | 0.93 | Creative building from ideas |
| king_revise — Transform mode | 0.88 | 0.90 | Balanced: insightful but grounded |
| king_revise — Edit mode | 0.80 | 0.85 | Precise surgical editing |
| Channel (King's voice) | 0.93 | 0.95 | King's vivid, conversational style |

---

## KING'S CRAFT KNOWLEDGE BASE

All knowledge stored in `king_analysis.json`. Accessed through the 3 tools as needed.

### The Writer's Toolbox (King's Central Metaphor)

Four shelves of mastery, bottom to top:

1. **Bottom Shelf (Foundation):** Vocabulary and grammar. Use the first word that comes to mind if it's appropriate. Don't try to decorate.
2. **Second Shelf (Style):** Active voice over passive. Death to adverbs. Specific verbs over modified weak ones. Conversational prose that doesn't perform.
3. **Third Shelf (Scene Craft):** Situation-based storytelling. Character revelation through action. The "closed door" first draft. Earning emotion through specificity.
4. **Top Shelf (Theme & Resonance):** "Themes are like bones in the body — you can't see them but they hold everything together." Themes emerge; they are never forced.

### King's Core Philosophy

Source: *On Writing: A Memoir of the Craft* + writing_guides.json lines 18-86

- **Story is king.** Character drives horror. Ordinary people in extraordinary situations. Accessible literary quality.
- **Character drives plot, not the other way around.** Never force characters to serve plot; let plot emerge from character.
- **Write with the door closed, rewrite with the door open.** First draft is for you. Subsequent drafts are for readers.
- **Kill your darlings.** Be willing to cut passages you love if they don't serve the story.
- **The road to hell is paved with adverbs.** Strong verbs are more effective than weak verbs with modifiers.
- **The passive voice is weak and circuitous.** Use active voice for clarity and impact.
- **Description begins in the writer's imagination, but should finish in the reader's.** Give enough detail, leave room for imagination.
- **Dialogue comes from listening.** Good dialogue comes from observing how people actually speak.
- **The scariest moment is always just before you start.** Fear diminishes once you begin. Start writing, even imperfectly.
- **Read a lot and write a lot.** Your voice emerges from writing. Steal techniques, not style.

### Situation-Over-Plot Philosophy

King doesn't plot. He puts characters in situations and lets them respond:
- "I want to put a group of characters in some sort of predicament and then watch them try to work themselves free."
- The test for any scene: Did you start with a situation and let characters respond? Or did you force characters into a plot point?

### Telepathy Engine

Writing is refined telepathy — the writer sends an image, the reader receives it:
- **Signal:** Specific detail, concrete imagery, active verbs, earned emotion
- **Noise:** Adverbs, passive voice, over-description, abstract philosophy, "literary" pretension
- Quality of writing = clarity of transmission

### Fear & Stakes (Ordinary to Extraordinary)

King's genius applied beyond horror:
- Fear of failure, fear of growing up, fear of losing what you love, fear of being ordinary, fear of being forgotten
- The mundane made profound through specific, concrete, earned detail
- Non-horror masterpieces: Stand By Me, Shawshank Redemption, 11/22/63, Hearts in Atlantis

### Voice Craft

- **Blue-collar authenticity:** Not caricature accent but worldview — directness, toughness masked as humor, pop culture as shared language
- **Period-specific voice:** Songs, brands, TV shows, slang ground characters in their era
- **Child/teen POV:** King writes young people with unmatched authenticity — their logic, fears, bravado, vulnerability

### Pacing Mastery

- **Page-turner technique:** The "one more page" effect
- **Sentence rhythm:** Short sentences for urgency. Long, rolling sentences for reflection.
- **Chapter architecture:** Cliffhanger endings, cold opens, the camera pull technique
- **The Patient Setup:** Slow, detailed, character-rich setup that makes the payoff devastating. King earns his climaxes.

### Revision Philosophy (Scalpel & Hose Meets King)

- **King's Formula:** 2nd draft = 1st draft minus 10%
- **SCALPEL (King's cuts):** Adverbs, passive voice, overwriting, "literary" pretension, telling-after-showing
- **HOSE (King's additions):** Specific sensory detail, character-specific fear made concrete, money sentences that earn their place, the ordinary detail that makes the extraordinary believable
- **Closed Door / Open Door:** Write freely first (for yourself). Revise with the reader in mind (for them). Fresh eyes between drafts.

### King's Hard Rules

1. Read a lot and write a lot — no shortcut, no substitute
2. Kill adverbs — strong verbs carry more image
3. Active voice — passive is weak and circuitous
4. 2nd draft = 1st draft minus 10%
5. Character drives plot — never the reverse
6. Write with the door closed, rewrite with the door open
7. Kill your darlings — if it doesn't serve the story, it dies
8. Description should finish in the reader's imagination
9. Themes are bones — invisible but holding everything together
10. The scariest moment is always just before you start
11. Dialogue comes from listening to how people actually speak

### King's Quotes (from writing_guides.json)

- "The scariest moment is always just before you start." — On beginning a writing project
- "Read a lot and write a lot." — On developing craft
- "The road to hell is paved with adverbs." — On prose style
- "Kill your darlings, kill your darlings, even when it breaks your egocentric little scribbler's heart, kill your darlings." — On revision
- "Description begins in the writer's imagination, but should finish in the reader's." — On description
- "Write with the door closed, rewrite with the door open." — On first drafts vs. revision
- "Character drives plot, not the other way around." — On character and plot

### King's Style Summary

- **Prose style:** Conversational, accessible, working/middle-class. No pretension. Vivid, often visceral metaphors grounded in physical/sensory.
- **Pacing:** Page-turner pacing. Knows when to speed up, slow down.
- **Narrative technique:** Third person omniscient OR limited, often multiple POVs. Patient setup, then accelerating tension.
- **Character voice:** Rich backstory. Natural, specific to character. Blue-collar authentic dialogue.
- **Themes:** Evil (supernatural and human), childhood trauma, small-town America, addiction and recovery, ordinary heroism.

---

## FILE STRUCTURE (Planned)

```
zz_COMPASS/MCP_Implementations/STEPHEN_KING_MCP/
├── STEPHEN_KING_MCP_DESIGN.md    ← This document
├── server.py                      ← MCP server with 3 tools
├── data/
│   └── king_analysis.json         ← Comprehensive King craft data
├── requirements.txt               ← Dependencies (mcp library)
└── README.md                      ← Private & Confidential setup guide
```

---

## OPEN QUESTIONS (Pre-Build)

1. **SmartRewrite Integration:** Timothy's existing SmartRewrite system has Liberty Levels (Conservative, Moderate, High) for how much prose changes. How does this relate to the King MCP's Liberty Levels (Nice, Neutral, Professional) which control feedback delivery? Same system? Different dimensions? Needs discussion.

2. **Rating Scale:** Should there be a defined 1-10 scale for consistent ratings across sessions? Proposed:
   - 1-3: Needs fundamental rework
   - 4-5: Foundation there, significant revision needed
   - 6-7: Solid draft, targeted improvements needed
   - 8-9: Publication-ready with minor polish
   - 10: Exceptional

3. **Integration with Other MCPs:** How the King MCP relates to Dennis Lehane MCP, COMPASS Writing Guides, Professional Editor, etc. (Expected: they coexist naturally, can be used together.)

---

## DESIGN HISTORY

This MCP was designed through extensive back-and-forth dialogue between Timothy and Claude, including consultation with the Sequential Thinking MCP. Key design decisions:

- Started at 9 tools, simplified to 3 based on Timothy's real workflow needs
- A.B.S.H. alignment discovered organically — Timothy's existing system maps directly to the tool structure
- Liberty Levels added based on Timothy's experience with The Phantom Cowboy (false praise from AI leading to real-world consequences)
- Smart defaults ensure the system works naturally without requiring code memorization
- Agent guidelines encoded in MCP data to ensure consistent behavior across different chat sessions

---

*PRIVATE & CONFIDENTIAL — For Timothy and Claude's Use Only*  
*Last Updated: February 18, 2026*
