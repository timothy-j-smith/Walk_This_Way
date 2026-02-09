# CHAPTER ANALYSIS & KNOWLEDGE GRAPH EXTRACTION TEMPLATE
## XML-Tagged Structured Extraction for Novel Intelligence Pipeline
**Version:** 1.0
**Status:** Ready
**Integration:** Knowledge Graph Memory MCP + Mermaid MCP

---

## WHAT THIS DOES

**Extracts structured intelligence from any chapter** using XML-tagged prompting, then feeds it into the Knowledge Graph Memory for persistent storage and Mermaid visualization.

This template uses four prompt engineering techniques:
1. **XML Tags** - Structure the extraction into clear categories
2. **Chain of Thought** - Reason through each extraction step by step
3. **Context Pinning** - Pin character DNA and plot DNA as reference context
4. **Few-Shot Examples** - Provide extraction examples to guide quality

---

## THE EXTRACTION FRAMEWORK

### How to Use

Copy this framework into a chat when analyzing any chapter. Replace `[CHAPTER_CONTENT]` with the actual text or file reference.

---

### Extraction Prompt

```
<system_context>
You are a literary intelligence extraction system. Your job is to read a chapter 
and extract every narratively significant element into structured categories.
Be thorough but precise. Only extract what is ACTUALLY in the text — do not infer 
or fabricate. Use Chain of Thought to reason through each category.
</system_context>

<reference_context>
Pin the following for cross-reference during extraction:
- Story_Bible/ (character DNA, plot DNA, world DNA)
- Previous Knowledge Graph entities (call read_graph first)
</reference_context>

<input>
[CHAPTER_CONTENT]
</input>

<extraction_instructions>

STEP 1: CHARACTER EXTRACTION
<character_extraction>
For EACH character who appears, speaks, is referenced, or influences action:

<character>
  <name>[Full name as used in story]</name>
  <entity_type>character</entity_type>
  <role>[protagonist | antagonist | supporting | mentioned | referenced]</role>
  <chapter_status>[new_introduction | recurring | background]</chapter_status>
  <physical_details>[Any physical description given in THIS chapter]</physical_details>
  <emotional_state>[Emotional arc in this chapter]</emotional_state>
  <key_actions>[What they DO in this chapter]</key_actions>
  <key_dialogue>[Most significant line(s) of dialogue, quoted]</key_dialogue>
  <relationships_shown>
    <relation>
      <with>[Other character name]</with>
      <type>[loves | fears | respects | hates | mentors | etc.]</type>
      <evidence>[Quote or reference from text]</evidence>
    </relation>
  </relationships_shown>
  <observations>
    - [Observation 1: trait, behavior, or detail]
    - [Observation 2: ...]
    - [Observation 3: ...]
  </observations>
</character>
</character_extraction>

STEP 2: LOCATION EXTRACTION
<location_extraction>
For EACH location, setting, or place referenced:

<location>
  <name>[Location name]</name>
  <entity_type>location</entity_type>
  <chapter_status>[new | recurring]</chapter_status>
  <physical_description>[Sensory details: sight, sound, smell, texture]</physical_description>
  <atmosphere>[Emotional/tonal quality of this place]</atmosphere>
  <narrative_function>[Why this location matters to the story]</narrative_function>
  <characters_present>[Who is here]</characters_present>
  <observations>
    - [Observation 1]
    - [Observation 2]
  </observations>
</location>
</location_extraction>

STEP 3: EVENT EXTRACTION
<event_extraction>
For EACH significant plot beat, action, or turning point:

<event>
  <name>[Short descriptive name]</name>
  <entity_type>event</entity_type>
  <description>[What happens, in 2-3 sentences]</description>
  <characters_involved>[Who participates]</characters_involved>
  <location>[Where it occurs]</location>
  <chapter_position>[opening | rising_action | midpoint | climax | falling_action | closing]</chapter_position>
  <consequences>[What this sets up or causes]</consequences>
  <observations>
    - [Observation 1]
    - [Observation 2]
  </observations>
</event>
</event_extraction>

STEP 4: THEME EXTRACTION
<theme_extraction>
For EACH theme expressed, introduced, or developed:

<theme>
  <name>[Theme name]</name>
  <entity_type>theme</entity_type>
  <how_expressed>[How the theme manifests in this chapter]</how_expressed>
  <characters_connected>[Who embodies or opposes this theme]</characters_connected>
  <development_stage>[introduced | developing | challenged | deepened | resolved]</development_stage>
  <observations>
    - [Observation 1]
    - [Observation 2]
  </observations>
</theme>
</theme_extraction>

STEP 5: PLOT THREAD EXTRACTION
<plot_thread_extraction>
For EACH plot thread that is advanced, introduced, or referenced:

<plot_thread>
  <name>[Thread name]</name>
  <entity_type>plot_thread</entity_type>
  <status>[introduced | advanced | complicated | paused | resolved]</status>
  <description>[How this thread moves in this chapter]</description>
  <connected_characters>[Who drives this thread]</connected_characters>
  <observations>
    - [Observation 1]
    - [Observation 2]
  </observations>
</plot_thread>
</plot_thread_extraction>

STEP 6: CRAFT OBSERVATION
<craft_extraction>
For NOTABLE prose techniques, structural choices, or stylistic decisions:

<craft_note>
  <name>[Technique name]</name>
  <entity_type>craft_note</entity_type>
  <technique>[What the author does]</technique>
  <example>[Brief quote or reference]</example>
  <effect>[What this achieves for the reader]</effect>
  <observations>
    - [Observation 1]
    - [Observation 2]
  </observations>
</craft_note>
</craft_extraction>

</extraction_instructions>

<output_format>
After extraction, provide:
1. SUMMARY: Total counts by category
2. KNOWLEDGE GRAPH ACTIONS: List of create_entities, add_observations, create_relations calls needed
3. NEW RELATIONS: All relationships discovered, in format: FROM -->|relation_type| TO
4. CONFLICTS: Any contradictions with existing Knowledge Graph data
</output_format>
```

---

## FEW-SHOT EXAMPLES

### Example: Character Extraction

**Input text:** *"Nick leaned against the doorframe, his guitar case hanging from one hand like a question mark. Jackie looked up from her notebook, pen frozen mid-sentence. 'You're late,' she said, though they both knew there hadn't been a time set."*

**Extraction:**
```xml
<character>
  <name>Nick Johnson</name>
  <role>protagonist</role>
  <chapter_status>recurring</chapter_status>
  <physical_details>Leaning posture, carrying guitar case</physical_details>
  <emotional_state>Uncertain, tentative — guitar case "like a question mark"</emotional_state>
  <key_actions>Arrives at Jackie's location</key_actions>
  <key_dialogue>None in this passage</key_dialogue>
  <relationships_shown>
    <relation>
      <with>Jackie Marsh</with>
      <type>tentative_connection</type>
      <evidence>"they both knew there hadn't been a time set" — unspoken understanding</evidence>
    </relation>
  </relationships_shown>
  <observations>
    - Guitar is an extension of his identity — carries it everywhere
    - Body language shows uncertainty (leaning, not entering)
    - The simile "like a question mark" suggests he's seeking something from Jackie
  </observations>
</character>
```

### Example: Event Extraction

**Input text:** *"The first chord rang out across the lake, and every kid at Camp Winnipesaukee stopped what they were doing. Nick didn't notice. He was somewhere else entirely, fingers finding notes he didn't know he had."*

**Extraction:**
```xml
<event>
  <name>Nick's Breakthrough Performance at Camp</name>
  <description>Nick plays guitar at camp and enters a flow state, captivating the entire camp audience without realizing it. This is the moment music becomes more than a hobby.</description>
  <characters_involved>Nick Johnson, camp audience</characters_involved>
  <location>Camp Winnipesaukee</location>
  <chapter_position>climax</chapter_position>
  <consequences>Establishes Nick's natural musical talent; sets up his pursuit of music as identity</consequences>
  <observations>
    - "somewhere else entirely" — dissociative flow state, pure absorption
    - "fingers finding notes he didn't know he had" — talent exceeding conscious skill
    - The audience stops but Nick doesn't notice — he plays for himself, not them
  </observations>
</event>
```

---

## TIPS

1. **Be thorough** — Extract everything, even minor characters and background locations
2. **Quote the text** — Observations are stronger with direct textual evidence
3. **Use Chain of Thought** — Reason through WHY something matters, not just WHAT it is
4. **Check for conflicts** — Compare extractions against existing Knowledge Graph entries
5. **Pin context** — Always reference Story Bible DNA files for consistency checking

---

**Status:** Ready to Use
**Next Step:** Use with `/chapter-to-kg` command for automated Knowledge Graph population
