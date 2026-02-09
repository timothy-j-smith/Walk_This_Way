# Populate Knowledge Graph with MCP Encyclopedia Data

Load all 66 MCPs from the Encyclopedia into the Knowledge Graph Memory as structured entities and relations.

## Instructions

1. Read the MCP Encyclopedia at `.cursor/docs/MCP_ENCYCLOPEDIA.md`
2. For each MCP entry, create a Knowledge Graph entity using the `knowledge-graph-memory` MCP's `create_entities` tool:

### Entity Format
Each MCP becomes an entity with these observations:
- `type: MCP Server`
- `status: [Enabled/Disabled]`
- `mcp_type: [Official/Community/Custom-Built]`
- `api_required: [None/key name]`
- `category: [category from encyclopedia]`
- `description: [first sentence of description]`

### Relations Format
Create relations between MCPs:
- `compass-intelligence` → `uses` → `knowledge-graph-memory`
- `compass-intelligence` → `feeds` → `mermaid` (if available)
- `sequential-thinking` → `variant_of_family` → `sequential-thinking-enhanced`
- `sequential-thinking` → `variant_of_family` → `sequential-thinking-mas`
- `sequential-thinking` → `variant_of_family` → `sequential-thinking-rust`
- `sequential-thinking` → `variant_of_family` → `sequential-thinking-ultra`
- `firecrawl` → `complements` → `duckduckgo-search`
- `style-emulation` → `related_to` → `dennis-lehane-style`
- `professional-editor` → `related_to` → `fiction-reverse-engineering`
- `walk-this-way-files` → `same_type_as` → `tim-cursor-experiment-files`
- `github` → `related_to` → `gitkraken`

3. After creating all entities and relations, report the total count.

## Run this command to populate the Knowledge Graph
This only needs to be run once. After that, the data is persistent in the KG.
