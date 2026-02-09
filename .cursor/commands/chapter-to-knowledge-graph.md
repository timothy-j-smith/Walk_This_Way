# Chapter to Knowledge Graph
## Extract Structured Data from Chapter and Write to Knowledge Graph

**Command:** `/chapter-to-kg` or `/extract-kg` or `/ingest`

**Action:** Analyzes a chapter file, extracts characters, locations, events, themes, and craft observations using XML-tagged structured extraction, then writes them into Knowledge Graph Memory.

**Usage:** Type `/chapter-to-kg <chapter file>` in Cursor Chat.

---

## Instructions for AI

When this command is invoked, execute the following pipeline:

### Step 1: Read the Chapter

Read the specified chapter file. If no file is specified, use the currently open file.

### Step 2: Structured Extraction with XML Tags

Analyze the chapter content and extract information into these XML-tagged categories. Think through each category carefully using Chain of Thought reasoning.

<extraction_template>

<characters>
For each character who APPEARS or is MENTIONED in this chapter:
- name: Full name as used in the story
- role: protagonist / antagonist / supporting / mentioned
- observations: Key traits, actions, dialogue patterns, emotional state in THIS chapter
- first_appearance: true/false (is this the first time they appear in the novel?)
- relationships_shown: Any relationships demonstrated in this chapter
</characters>

<locations>
For each location that appears in this chapter:
- name: Location name
- description: Physical details, atmosphere, sensory details
- significance: Why this location matters to the plot/theme
- first_appearance: true/false
</locations>

<events>
For each significant event or plot beat:
- name: Short descriptive name
- description: What happens
- characters_involved: Who participates
- location: Where it occurs
- consequences: What this event causes or sets up
- chapter_position: opening / rising / climax / falling / closing
</events>

<themes>
For each theme expressed or developed:
- name: Theme name
- how_expressed: How the theme manifests in this chapter
- characters_connected: Which characters embody or oppose this theme
- development: Is this theme introduced / developed / challenged / resolved?
</themes>

<craft_observations>
For notable craft techniques used:
- technique: What the author does (POV shift, time compression, dialogue style, etc.)
- example: A brief quote or reference
- effect: What this achieves for the reader
</craft_observations>

<plot_threads>
For each plot thread advanced or introduced:
- name: Thread name
- status: introduced / advanced / complicated / resolved
- connection: How it connects to the main plot
</plot_threads>

</extraction_template>

### Step 3: Check Existing Knowledge Graph

Use `read_graph` to see what entities already exist. For each extracted item:
- If the entity ALREADY EXISTS: use `add_observations` to add new observations
- If the entity is NEW: use `create_entities` to create it
- For all relationships found: use `create_relations` to add them

### Step 4: Write to Knowledge Graph

Execute the Knowledge Graph Memory MCP calls:

1. **create_entities** for all NEW characters, locations, events, themes, craft notes, plot threads
2. **add_observations** for EXISTING entities that have new information in this chapter
3. **create_relations** for all relationships discovered (use active voice: "lives_in", "kills", "loves", "occurs_at", "embodies", "drives", etc.)

### Step 5: Generate Updated Visualization

After writing, call `/knowledge-graph-visualize` to generate an updated Mermaid diagram showing the new state of the knowledge graph.

### Step 6: Report to User

Display a summary:
- New entities created (count by type)
- Existing entities updated (count)
- New relations added (count)
- The updated Mermaid diagram
- Any potential conflicts or duplicates flagged for review

---

## Variations

### Extract Only (Don't Write)
```
/chapter-to-kg --dry-run <file>    -- Show what WOULD be extracted, don't write
```

### Extract Specific Category
```
/chapter-to-kg --characters-only <file>   -- Only extract characters
/chapter-to-kg --events-only <file>       -- Only extract events
/chapter-to-kg --themes-only <file>       -- Only extract themes
```

### Batch Process
```
/chapter-to-kg --all-chapters    -- Process all chapters in Active_Draft_2/
```

---

## Example

**Input:** `/chapter-to-kg Active_Draft_2/Chapter_Camp_Winnipesaukee_1975.txt`

**AI Reads the chapter, then extracts:**
```xml
<characters>
  - Nick Johnson: protagonist, nervous energy, trying to prove himself
  - Jackie Marsh: supporting, skeptical but warming up
</characters>

<locations>
  - Camp Winnipesaukee: Summer camp setting, humid, pine trees, lake nearby
</locations>

<events>
  - Nick's First Performance: Nick plays guitar at camp talent show
    - Characters: Nick, camp audience
    - Location: Camp Winnipesaukee
    - Consequences: Sets up his musical ambition
</events>

<themes>
  - Coming of Age: Nick discovering music as identity
  - Belonging: Finding your tribe through shared passion
</themes>
```

**AI then writes to Knowledge Graph and generates updated Mermaid diagram.**

---

**Status:** Ready to Use
**Requires:** Knowledge Graph Memory MCP + Mermaid MCP (both installed)
**Usage:** Type `/chapter-to-kg <filename>` in Cursor Chat
