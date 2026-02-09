# Knowledge Graph Visualizer
## Auto-Generate Mermaid Diagram from Knowledge Graph Memory

**Command:** `/knowledge-graph-visualize` or `/kg-viz` or `/graph`

**Action:** Reads the entire Knowledge Graph Memory and generates a visual Mermaid diagram showing all entities, relationships, and narrative structure.

**Usage:** Type `/knowledge-graph-visualize` in Cursor Chat.

---

## Instructions for AI

When this command is invoked, execute the following pipeline:

### Step 1: Read the Knowledge Graph

Use the **Knowledge Graph Memory MCP** (`user-memory`) tool `read_graph` to retrieve all entities and relations.

### Step 2: Categorize Entities by Type

Group entities into Mermaid subgraphs by their `entityType`:
- **character** -> `subgraph Characters`
- **location** -> `subgraph Locations`
- **event** -> `subgraph Key_Events`
- **plot_thread** -> `subgraph Plot_Threads`
- **theme** -> `subgraph Themes`
- **craft_note** -> `subgraph Craft_Notes`
- **world_rule** -> `subgraph World_Rules`
- **research** -> `subgraph Research`
- Any other type -> `subgraph Other`

### Step 3: Build Mermaid Syntax

For each entity, create a node:
```
NodeID["Entity Name<br/>First observation (truncated to 40 chars)"]
```

For each relation, create an edge:
```
FromNodeID -->|relationType| ToNodeID
```

Apply color coding by entity type:
- Characters: `fill:#e74c3c,color:#fff` (red)
- Locations: `fill:#1abc9c,color:#fff` (teal)
- Events: `fill:#3498db,color:#fff` (blue)
- Plot Threads: `fill:#9b59b6,color:#fff` (purple)
- Themes: `fill:#f39c12,color:#fff` (orange)
- Craft Notes: `fill:#2ecc71,color:#fff` (green)

### Step 4: Generate the Diagram

Use the **Mermaid MCP** (`user-mcp-mermaid`) tool `generate_mermaid_diagram` with:
- `theme`: "dark"
- `outputType`: "file"

### Step 5: Report to User

After generating, display:
- Total entities count by type
- Total relations count
- The generated Mermaid diagram image
- Any entities with zero relations (orphans) flagged for review

---

## Variations

### Filter by Type
```
/kg-viz characters    -- Only show character entities and their relations
/kg-viz locations     -- Only show location entities and their relations
/kg-viz events        -- Only show event entities and their relations
/kg-viz themes        -- Only show themes and what embodies/opposes them
/kg-viz plot          -- Only show plot threads and driving characters
```

### Output Formats
```
/kg-viz full          -- Complete graph (default)
/kg-viz simple        -- Characters + relations only (no observations)
/kg-viz timeline      -- Events ordered chronologically (if dates available)
```

---

## Example Output

For a novel with 10 characters, 6 locations, 8 events, 3 themes:
- Generates a Mermaid `graph TD` diagram
- Characters in red, locations in teal, events in blue, themes in orange
- Arrows show relationships: "kills", "lives_in", "occurs_at", "embodies"
- Saved as PNG file for visual reference

---

**Status:** Ready to Use
**Requires:** Knowledge Graph Memory MCP + Mermaid MCP (both installed)
**Usage:** Type `/knowledge-graph-visualize` in Cursor Chat
