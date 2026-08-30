# Add an Author

One professor. One anchor novel. Flat with everyone else. No numbered rank.

## When to add

Timothy names a book that felt like it came from his hand, or a scene type the working set cannot teach. The Dean does not add authors to look complete.

## Steps

1. Pick the **anchor novel** (one book, not a career)
2. Create `faculty/[lastname]-[short-novel-slug].md` — lowercase, dashes
3. Use the seven-section envelope if they join the working set. Use the short roster envelope otherwise
4. Add a line to [faculty/README.md](../faculty/README.md) under Roster (or Working set if Timothy promotes them)
5. Add them to the open novel's `prose-dna.md` only if that book will summon them
6. Optional lab: add a JSON + engine entry. See [add-mcp.md](add-mcp.md) author-engines section
7. Principles and fair-use excerpts only. No wholesale reprint

## Working-set envelope (seven sections)

1. When to call
2. Who they are
3. Voice signature
4. What they teach
5. Characteristic techniques
6. How they coach
7. When they hand off

## Roster envelope (short)

- When to call
- Anchor novel
- Craft DNA (five to eight bullets)
- Pitfalls
- One tutoring question
- Handoff

## Engine (optional)

Python: `/Users/timothy/mcp-servers/author-engines-venv/bin/python`

Server: `zz_COMPASS/MCP_Implementations/AUTHOR_ENGINES/author_server.py --author [slug]`

JSON: `AUTHOR_ENGINES/data/[slug].json`

The skill file is the identity. The engine is the lab. Do not create a second personality in the JSON.

## Do not add

Tartt. Russo. Whitehead. Do not restore Russo as a numbered first influence.
