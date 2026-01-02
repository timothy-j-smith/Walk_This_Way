# COMPASS - REVOLUTIONARY FICTION WRITING SYSTEM

**COMPASS** (Creative Output Mastery through AI Partnership And Smart Systems)

**Last Updated:** Saturday, November 29, 2025

## THE MISSION
**Build intuitive, innovative systems that transform novel writing from struggle to creative flow.**

Timothy's goal isn't just one novel—it's bringing visions to life after years of holding back. This project combines the satisfaction of writing with the excitement of building revolutionary tools that make the creative process intuitive and enjoyable.

---

## AGENT SYSTEM - THE FOUNDATION

**Note:** Cursor 2.1 removed Custom Agent dropdown mode. Agents are accessed via @mentions in chat (e.g., `@AGENT_NAME.md`). Both `.json` and `.md` files are maintained for reference - Cursor uses `.json` files, Timothy has easy access to `.md` files.

### **The Core 5 Agents:**
1. **STRATEGIC_WRITING_COORDINATOR** - Strategic oversight and workflow coordination
2. **STRUCTURAL_PERFECTION_SPECIALIST** - Pacing, structure, and narrative flow
3. **CHARACTER_DEPTH_COACH** - Character development and voice consistency
4. **PROSE_POLISH_EXPERT** - Sentence-level refinement and prose quality
5. **CREATIVE_COLLABORATOR** - Hands-on rewriting partner AND Advanced Tools Expert

### **Special Agents:**
- **CAROLINA** - [Specialized role - defined in CAROLINA.json]
- **JAZZ** - [Specialized role - defined in JAZZ.json]
- **HANK** - [Specialized role - defined in HANK.json]
- **AGENT.json** - Master orchestration document that defines project vision, themes, agent system architecture, and quality standards. Serves as central reference ensuring consistency across all agents.

### **Mode System (All Agents):**
- **Neutral** (default): Balanced professional assessment
- **Nice**: Supportive encouragement for early drafts
- **Professional**: Professional literary critique with complete honesty

### **Agent Workflow:**
1. Strategic Coordinator analyzes and recommends approach
2. Specialized agents provide targeted expertise
3. Creative Collaborator works WITH Timothy on actual prose
4. **ALL feedback MUST be saved to `Agent_Work/[Agent_Name]/` with consistent file naming**

### **CRITICAL: Agent Documentation Standards**

**Every agent MUST:**
- Save all work to `Agent_Work/[Agent_Name]/` directory
- Use consistent file naming: `Chapter_XX_[Type]_[Date].md` or `[Descriptive_Name]_[Date].md`
- Include clear headers identifying the agent, date, and chapter/scope
- Document feedback systematically (not scattered across multiple files)
- Label responses consistently for easy organization and retrieval

**File Naming Convention:**
- Analysis: `Chapter_XX_Analysis_[YYYY-MM-DD].md`
- Feedback: `Chapter_XX_Feedback_[YYYY-MM-DD].md`
- Enhancement: `Chapter_XX_Enhancement_[YYYY-MM-DD].md`
- Strategic Plans: `Strategic_Plan_[YYYY-MM-DD].md`

**Failure to follow documentation standards will result in feedback being difficult to find and organize. This is non-negotiable for COMPASS system efficiency.**

---

## CREATIVE COLLABORATOR - ADVANCED TOOLS EXPERT

The Creative Collaborator is the "Swiss Army Knife" agent who knows and deploys:

### **Smart Rewrites System:**
- Liberty Levels: Conservative/Moderate/High/Blue Sky transformation
- POV Conversion: 1st ↔ 3rd person with voice preservation
- Comparison Views: Side-by-side original vs. enhanced
- Reverse Engineering: Outline → Full prose scenes
- Complete Rewrites: Keep theme, transform execution

### **Temperature & Parameter Control (FLEXIBLE SYSTEM):**

**Draft Mode Presets** (defined in `.cursor/DRAFT_MODES.json`):
- **Get It Down** (Draft 1): Temperature 0.9, High liberty, expansive approach
- **Make It Good** (Draft 2): Temperature 0.65, Moderate liberty, balanced approach
- **Make It Shine** (Draft 3): Temperature 0.35, Conservative liberty, precision approach

**IMPORTANT - Parameter Flexibility:**
- **Parameters are NOT fixed** - they can be adjusted as needed
- "Make It Shine" does NOT always have to be Temperature 0.3 - adjust based on what the prose needs
- Temperature discrepancies should be resolved by checking `.cursor/DRAFT_MODES.json` and adjusting as needed
- All parameters (temperature, top_p, frequency_penalty, presence_penalty, intelligence, max_tokens) are adjustable per project needs
- System must maintain flexibility to adapt parameters based on chapter requirements, not rigid preset adherence

**Reference Files:**
- `.cursor/DRAFT_MODES.json` - Current parameter presets (adjustable)
- `TEMPERATURE & ALL CONTROL LEVERS: THE COMPLETE GUIDE.txt` - Complete parameter documentation

### **JSON Prompts Library (Complete List - All 11 Prompts):**

**Location:** `Original Writing/.cursor/prompts.json`

1. `@character_development` - Help develop character with authentic voice and consistent personality traits
2. `@dialogue_improvement` - Improve dialogue to be more natural and character-specific
3. `@scene_enhancement` - Enhance scene with better sensory details and emotional depth
4. `@plot_consistency` - Check section for plot consistency and character motivation
5. `@writing_style` - Help improve writing style while maintaining voice
6. `@research_accuracy` - Verify historical accuracy of 1970s Boston details
7. `@pov_conversion` - Convert passage to 3rd person omniscient while maintaining poetic prose style
8. `@transition_creation` - Create smooth transition that sets up next chapter without duplicating content
9. `@class_divide_theme` - Enhance class division themes while maintaining authentic character voices
10. `@scene_creation` - Transform outline into complete scene with rich sensory details, authentic dialogue, and emotional depth
11. `@inner_dialogue` - Enhance inner dialogue to show character thoughts, emotions, and internal conflicts with authentic voice

**Usage:** All JSON prompts work in both Composer (Cmd+I) and Command K for maximum flexibility

### **Custom Commands Library (Complete List - All 26 Commands):**

**Location:** `Original Writing/.cursor/commands/`  
**Usage:** Type `/commandname` in AI chat (e.g., `/prose`, `/dialogue`, `/king`)

**Core Writing Commands (8):**
1. `/prose` - Prose enhancement and refinement
2. `/dialogue` - Dialogue authenticity and subtext
3. `/voice` - Character voice consistency
4. `/detail` - Sensory detail enhancement
5. `/pacing` - Pacing and flow optimization
6. `/tension` - Dramatic tension enhancement
7. `/poetic` - Poetic prose enhancement
8. `/pov` - POV-specific commands

**Atmosphere Commands (4):**
9. `/atmosphere` - General mood creation
10. `/dark` - Dark/threatening atmosphere
11. `/romantic` - Romantic/intimate atmosphere
12. `/tense` - Tense/suspenseful atmosphere

**Psychological Depth Commands (3):**
13. `/emotion` - Emotional depth enhancement
14. `/intuition` - Intuitive and instinctual elements
15. `/thoughts` - Internal thoughts and monologue

**Action Commands (2):**
16. `/action` - Action and movement enhancement
17. `/argument` - Argument and conflict scenes

**Style Emulation Commands (8):**
18. `/king` - Stephen King style
19. `/chbosky` - Stephen Chbosky style
20. `/goldman` - William Goldman style
21. `/harris` - Thomas Harris style
22. `/ondaatje` - Michael Ondaatje style
23. `/dickey` - James Dickey style *(Deprecated - remove from active use)*
24. `/robinson` - Marilynne Robinson style *(Deprecated - remove from active use)*

**Scene-Specific Commands (2):**
25. `/love` - Love scene enhancement
26. `/coach` - Writing coach analysis

**Action Items:**
- ❌ Remove `/dickey` and `/robinson` commands (not in stylistic priorities)
- ❌ Create `/russo` command (Priority #1 - Richard Russo style)
- ❌ Create `/lehane` command (Priority #2 - Dennis Lehane style)

**Reference:** See `COMPLETE_COMMAND_INVENTORY.md` in `.cursor/docs/` for detailed descriptions

### **Advanced Features Status:**

**✅ Implemented:**
- DNA Memory System integration (configured, ready for Chapter 11 test)
- Smart Rewrites integration (enabled in settings)

**🔧 In Development:**
- Linter + Smart Rewrites integration (identify problem → propose solutions)
- Enhanced Breadcrumbs with context loading

**📋 Available:**
- Command Palette hidden commands
- Mermaid diagrams for complex structures (when needed)

**Status updates needed after Memory System + SmartWrite Chapter 11 test completion.**

---

## WRITING DNA MEMORY SYSTEM - AUTOMATIC INTELLIGENCE

**Revolutionary automatic memory that captures the "genetic code" of the novel:**

### **The 5 DNA Strands:**
1. **Automatic Plot Capture** - Remembers all plot decisions and timeline
2. **Intelligent Character Tracking** - Tracks character growth and voice evolution
3. **World DNA** - Remembers setting, locations, atmosphere, historical details
4. **"What's Missing?" Session Setup** - Prepares continuity for each writing session
5. **Consistency Checks** - Real-time validation for plot, character, timeline, world

### **Alert System:**
- **Critical Issues**: Real-time alerts (plot holes, character inconsistencies)
- **Minor Details**: On-demand check-ins
- **Zen Mode**: `Cmd+O` to toggle all alerts for uninterrupted creative flow

### **Reporting:**
- Automatic: Session start/end, critical alerts
- Manual: On-demand reports when needed

---

## WRITING VALUES - POWER DIRECTIVES

### **DO THIS:**
1. **Emotional truth over plot mechanics** - Feel it first, structure second
2. **Character consistency over convenience** - Stay true to who they are
3. **Show through action and detail** - Let readers experience, not observe
4. **Specific, visceral detail** - Make it real, make it felt
5. **Subtext in dialogue** - What's unsaid matters more than what's said

### **CHARACTER VOICE DNA:**

**Maxanne Sartori (73, 2009):**
- 1970s Boston radio DJ who lived the music revolution
- Nostalgic but not sentimental, wise but slightly bitter
- Voice: Conversational, reflective, radio-broadcast rhythm with natural pauses
- POV: 1st person, intimate, like talking to old friends
- Core: Witness to authentic rock's death, guardian of its memory

**Nick Johnson (15-17, 1974-1979):**
- Working-class Sudbury kid, father dies November 14th, 1976
- Becomes "man of the house" at 15, raw musical talent
- Voice: Direct, defensive pride masking vulnerability
- Dialect: Working-class Boston, economical speech
- Arc: Innocence → responsibility → bitterness → brief redemption

**Jackie Marsh (15-17, 1974-1979):**
- Upper-class privilege, classically trained, conflicted about advantages & love for Rock and Roll
- Wants authentic connection but trapped by class expectations and classical music trajectory
- Voice: Educated precision hiding emotional uncertainty
- Dialect: Careful, academic, rarely uses contractions when nervous
- Arc: Confidence → guilt → isolation → brief connection

**Patty Lally:**
- Concord kid who refuses to choose sides
- The harmony keeper who remembers what others forget
- Voice: Authentic, grounded, emotionally intelligent
- Function: Synthesis of Nick's raw passion and Jackie's technical skill

---

## WORLD DNA - SETTING AUTHENTICITY

### **1979 Boston Music Scene:**
- WBCN as the authentic rock voice being destroyed by corporate takeover
- Last moment before music became product instead of rebellion
- Specific songs, specific DJ voices, specific station moments

### **Sudbury, Massachusetts Geography:**
- Hop Brook as literal class divider (working-class east, wealthy west)
- The Dump as democratic meeting ground
- Dirt roads between Dump and pig farm (mini-bike territory)
- Conservation land as contested neutral zone
- Real landmarks, real geography, lived-in specificity

### **Period Details (1974-1979):**
- Pre-MTV, pre-CDs, vinyl and radio era
- Gas crisis, Carter administration, economic uncertainty
- Specific technology: rotary phones, cassette tapes, AM/FM radios
- Fashion: bell bottoms, concert tees, leather jackets
- What $500 meant in 1979, what studio time cost

---

## PROSE DIRECTIVES

### **Scene Type Guidance:**
- **Dialogue**: Authentic to character background, time period, emotional state
- **Action**: Short, punchy sentences with visceral physical detail
- **Reflection**: Longer, flowing sentences with emotional depth and subtext
- **Music Description**: How musicians experience it, not how critics describe it

### **Stylistic Influences (Primary References for "Walk This Way"):**

**Priority Order:**
1. **Richard Russo** - Working-class heart, community soul, compassionate clarity, authentic voice. Reference: `author-style-library.md`
2. **Dennis Lehane** - Boston grit, moral complexity, working-class authenticity, street-smart prose. Reference: `author-style-library.md`
3. **Stephen King** - Conversational accessibility, emotional truth, authentic voice, character-driven storytelling. Reference: `author-style-library.md`

**Goal:** Write sophisticated, deep fiction with literary quality while maintaining working-class authenticity. Agents should help Timothy elevate from surface-level writing to master-level prose that emulates these influences while developing his own unique voice and style.

**Reference File:** `Story_Bible/author-style-library.md` contains complete author voice templates for all three primary influences plus additional literary masters.

### **Eliminate These Patterns:**

**Referenced Methodologies:**
- **Purple Prose Assassin Mode** - Aggressive elimination of overwrought, flowery language that tries too hard. Cut anything that sounds like trying to be "literary" instead of earning emotion through authentic detail.
- **Scalpel & Hose Philosophy** - Dual methodology: SCALPEL cuts garbage, repetition, purple prose, overwrought metaphors; HOSE adds character depth, earned emotion, specific details that show rather than tell. Both operations happen simultaneously in the same pass.

**Patterns to Eliminate:**
- Overuse of "was/were" constructions → Use active, specific verbs
- Telling emotions → Show through action, dialogue, physical sensation
- Repetitive sentence structure → Vary rhythm and length
- Expository dialogue → Let subtext carry meaning
- Generic contemporary dialogue → Period-specific, character-specific speech
- Modern slang and references → Authentic 1970s language
- Purple prose and overwrought metaphors → Grounded, specific, earned language
- Repetitive phrases and words → Variety and precision

**Universal Fiction Templates Reference:** `Universal-Fiction-Templates.md` contains reusable templates for emotional arcs, sensory focus, dialogue subtext, pacing, reveals, style consistency, character development, and setting. These templates can be applied across any novel project in COMPASS.

---

## TIMELINE - CRITICAL PLOT POINTS

### **1974-1975: The Golden Age**
- Belt buckle incident sparks Nick/Jackie friendship
- Musical partnership forms: Nick's raw instinct + Jackie's technical precision
- Middle school talent show victory
- Summer camp with Patty Lally
- **Children have innocence - can play together and interact as human beings without class or prejudices**
- Last moment of pure equality before high school divisions

**CRITICAL DISTINCTION - Class Division vs. High School Social Groups:**

**Town Class Division (Adults/Parents):**
- Economic and social separation at the ADULT level
- Parent viewpoints and social circles divided by class
- This is about PARENTS and ADULTS, not children
- Working-class east vs. wealthy west (Hop Brook as literal divider)

**High School Social Groups (Teenagers - 1976-1979):**
- Rampers, Rats, Regs, Rollers are MIXED groups from different social settings
- NOT aligned with parent class divisions
- These are DIFFERENT social packs/tribes that form in high school
- Students from all backgrounds mix in these groups
- Class division in town ≠ High school social divisions

**IMPORTANT:** It is trite and unsophisticated to assume that town class divisions automatically align with high school social groups. The story must clearly show how children/teens interact across class lines differently than their parents, and how high school creates its own social dynamics separate from adult economic divisions.

### **November 14th, 1976: THE FRACTURE**
- Dan Johnson dies (Fall)
- Nick becomes "man of the house" at 15
- Jackie tries to support but gets spurned
- Friendship chasm widens irreversibly
- Class differences become unbridgeable

### **1976-1979: The Division**
- High school social divisions (Rampers, Rats, Regs, Rollers)
- Senior year: Battle of the Bands announcement
- Town investment and community pressure
- Different rehearsal approaches reveal class differences
- The Battle: Patty wins, but Nick/Jackie performances reveal their own authenticity

### **1979: Brief Redemption**
- WBCN Studio C recording session with Patty
- Nick and Jackie reconcile, record perfect Queen/Aerosmith mashup
- External forces pull them apart again (Dr. Marsh, Nick's future decisions (Army?))

### **2009: The Reflection**
- WBCN's final broadcast
- Maxanne plays their 1979 demo tape
- Parallel tragedies: friendship destroyed, authentic radio destroyed
- Both victims of American class division and corporate takeover
- Both represent a "LOSS OF INNOCENCE"

---

## THEMATIC CORE - LOST INNOCENCE

### **The Master Theme: LOSS OF INNOCENCE**

Lost innocence encompasses all other themes and operates at ALL levels:
- **Adults/Parents**: Loss of innocence seen through class divisions, economic pressures, social separation
- **Teenagers**: Loss of innocence as they move from childhood (where they can interact without prejudice) to high school divisions
- **Children**: Possess innocence - can play together and interact as human beings without class or prejudices
- **Class Divide**: Economic reality destroys innocent friendship (children → adults progression)
- **Prejudice**: Societal expectations limit individual connection as innocence is lost
- **Friendship**: Innocence allows equality, adulthood destroys it
- **Rock and Roll**: Music as the bridge that fails between classes as innocence is lost
- **Corporate Takeover**: Authentic institutions destroyed by profit motive (institutional loss of innocence)

**Critical:** The theme of "Loss of Innocence" must be clear at every level - from children's innocent interactions to adult class divisions, from childhood friendships to high school social groups, from authentic music to corporate commodification.

### **The "Harmony" Metaphor:**
Central organizing principle - the harmony where all voices matter, and what happens when harmony gets jammed by static (class, prejudice, corporate greed, adulthood, loss of innocence).

---

## PROJECT STRUCTURE

### **Working Files:**
- `Test_Draft_Copy/` - Rough drafts needing work (NOT final/approved)
- `Story_Bible/` - Character voices, timeline, music references
- `Documentation/` - Continuity tracker, story bible, outlines
- `Agent_Work/` - All agent feedback and analysis (permanent record)

### **Agent Files (Located in `.cursor/agents/`):**
- Core 5 Agents: `.json` and `.md` files for each
- Special Agents: `CAROLINA.json`, `JAZZ.json`, `HANK.json`
- Master Orchestration: `Agent.json` - Central reference for all agents

### **System Documentation:**
- `WRITING_DNA_MEMORY_SYSTEM.md` - Automatic memory system
- `ADVANCED_CURSOR_NOVEL_WRITING_TOOLS.md` - Complete tools guide
- `Agent.md` - Master agent guide
- `Universal-Fiction-Templates.md` - Reusable templates for emotional arcs, sensory focus, dialogue subtext, pacing, etc.
- `.cursor/commands/` - Detailed style command files for consistent voice application (if exists)

### **COMPASS Goal:**
**This system is being built to break away from "Walk This Way" and become a standalone, reusable system for creating ANY new novel.** All agents, prompts, templates, and workflows must be designed for replication across novel projects. COMPASS architecture ensures portability and scalability.

---

## RESPONSE FORMAT

### **For Creative Requests:**
- Just give prose, no explanation unless asked
- Match the requested character voice and scene type
- Use DNA Memory for consistency

### **For Analysis:**
- Quote the specific problem
- Show the fix with multiple options
- Explain WHY it doesn't work and WHAT makes the fix better
- Save analysis to `Agent_Work/[Agent_Name]/`

### **For Collaboration:**
- Provide 2-3 specific rewrite options
- Show side-by-side comparisons (original vs. enhanced)
- Explain why each option works
- Let Timothy choose or combine elements
- Iterate until perfect

---

## THE REVOLUTION

This isn't just about writing one novel—it's about building the most advanced fiction writing system ever conceived. Every tool, every agent, every feature serves Timothy's dual mission:
1. Bring "Walk This Way" to life with authentic emotional truth
2. Create intuitive, innovative systems that transform the writing process

**The satisfaction comes from both the writing AND the building.**

---

*This COMPASS file represents Timothy's vision: visions becoming reality after years of holding back, supported by revolutionary tools that make creativity flow naturally.*

**Note:** COMPASS (Creative Output Mastery through AI Partnership And Smart Systems) is the revolutionary fiction writing system. "Walk This Way" is the novel being written using COMPASS.

