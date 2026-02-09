# MCP Lookup

Look up any MCP from our Encyclopedia. The user will provide an MCP name or keyword.

## Instructions

1. Read the MCP Encyclopedia at `.cursor/docs/MCP_ENCYCLOPEDIA.md`
2. Search for the MCP name or keyword the user provided: `$input`
3. Return the full entry including:
   - Status (Enabled/Disabled)
   - Type (Official/Community/Custom-Built)
   - API Required
   - Prerequisites
   - Full description
   - Use Case Example
   - Installation config JSON
   - "Enable when" note (if disabled)
4. If the search term is vague, return all matching entries
5. If the user asks "list all" or "show categories", return the Table of Contents with enabled/disabled counts

## Special Queries
- `$input` = "enabled" → List all 20 enabled MCPs with one-line descriptions
- `$input` = "disabled" → List all 46 disabled MCPs with one-line descriptions  
- `$input` = "custom" → List all custom-built MCPs
- `$input` = "search" → List all search/research MCPs
- `$input` = "memory" → List all memory-related MCPs
- `$input` = "brothers" → List all 5 Sequential Thinking variants
- `$input` = "api" → List all MCPs that require API keys
- `$input` = "no-api" → List all MCPs that don't require API keys
