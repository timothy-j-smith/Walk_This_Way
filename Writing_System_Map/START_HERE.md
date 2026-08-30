# Writing system map

Timothy J. Smith · 22 August 2026

One toolkit. Many novels. Walk This Way is a book, not a toolbox.

**To print from Cursor:** open this `.md` file → `Cmd+Shift+V` (Markdown preview) → `Cmd+P`.

**To print the PDF:** do not use Cursor. Use the Preview app that just opened, or Finder → this folder → `START_HERE.pdf` → double-click → File → Print.

---

## Tomorrow morning — three jobs only

You are not finishing a novel tomorrow. You are parking the toolbox so the drafts can get rewritten.

1. Read this paper. Do not open fifty MCP toggles first.
2. Confirm the three buckets below still match what you want.
3. When you open Cursor, ask for the daily set: about ten MCPs left on for a Draft_06 day. Everything else stays off.

**Do not tomorrow:** move folders, add new MCPs, rebuild the orchestrator, or start a ninth novel.

---

## The short version (keep this page on the desk)

1. **Three buckets.** (1) The book — this novel’s pages and Story Bible. (2) The toolkit — one copy of the writing machines (MCP Library + COMPASS). (3) This Mac — servers and keys that have to run here (`~/mcp-servers`). New novels point at the toolkit. They do not get a paste of the tools.

2. **Draft folders stay.** Git is the undo button for today’s work in Draft_06. Folders are the print copies: Draft_1, Active_Draft_2, Draft_04, frozen Draft_05. You keep them so you can open “that garage chapter from four” and print it. Do not flatten those folders into git history.

3. **Most MCPs are writing tools. Do not load them all at once.** About 75% of the 104 names in Walk This Way’s config are writing-related (craft, books, research, git). Use them by stage: daily line edit ~10; research adds a few; print adds Pandoc; Figma and Docker stay off.

4. **The orchestrator is a stale labeler, not the organizer.** Keep the idea. Do not use the current server to flip switches. It writes a flag Cursor often ignores. Rebuild it only after the three buckets exist.

---

## Why this print pack exists

You have several first drafts. Walk This Way and Senseless are two. On disk next to them: Helix, Island Spring, Luna Alpha, Scrambled Eggs, Streets of Dreams, The Last Champion Standing, The Phantom Cowboy, When The River Cries. The drafts got written. The rewrites wait while the tools get rebuilt. That loop will still be here in six months unless the toolbox lives in one place and each novel stays a novel.

You already named this job in `03_Novels/_PROCESS_AND_ORG.md` and then deferred it. This is that session, on paper.

---

## 1. Three buckets

One Cursor window can open more than one folder (multi-root workspace). Git stays separate for each repo.

1. Cursor window — one workspace, two (or three) folders
2. **A. The book** — Walk This Way (or Senseless, or the next novel)
3. **B. The toolkit** — MCP Library + COMPASS (one copy for every book)
4. **C. This Mac** — `~/mcp-servers`, `~/mcp-venvs`, `~/.cursor/skills`, API keys

| Thing | Bucket | Now |
| --- | --- | --- |
| Draft_06, Story_Bible, PARKING_LOT.md | Book | Already correct |
| Draft_1 through Draft_05 folders | Book | Keep. Print copies. |
| Character facts for this novel | Book | This novel only |
| zz_COMPASS MCP source inside Walk This Way | Toolkit | Duplicate. Move later, not tomorrow morning. |
| 104-server mcp.json inside the novel | Split later | Too big for a book repo |
| Google / Gmail / Calendar | This Mac + Cursor plugins | Life around writing. Not the book. |

You already started the split: `Walk_This_Way.code-workspace` opens the novel and MCP Library + COMPASS. The mess is extra copies of the toolbox still living inside the novel.

---

## 2. Draft folders — Walk This Way

Keep the folders. Add git as save-points inside the active draft only. You do not need to become a git expert for this.

1. `Draft_1/` — first attempt. Keep. Do not edit.
2. `Active_Draft_2/` — incomplete rewrite era. Keep as quarry. Awkward name; leave it.
3. No Draft_03 folder. Do not invent one to fill the number.
4. `Draft_04/` — quarry. You will hunt a chapter here. Do not edit.
5. `Draft_05/` — first complete book. Frozen. Keep forever as the readable full draft. Do not edit.
6. **`Draft_06/` — the only folder we edit. Git lives here going forward.**

| Job | Use |
| --- | --- |
| Print yesterday’s book / find a lost chapter | Open the draft folder. Paper copy. This is why the folders exist. |
| Undo a bad line-edit today | Git inside Draft_06. Commits are not named “Draft 4 garage chapter.” |

---

## 3. MCPs by stage — not all at once

Counted from Walk This Way’s mcp.json (104 names): 67 fiction craft, 4 git, 7 life-around-writing (Google, Slack, Airtable, n8n, Linear), 26 other (Figma, Docker, Airflow, Blender). About 75% writing-related. The problem is never having them. The problem is loading a hundred into one chat.

| Stage | How many on | Examples |
| --- | --- | --- |
| Daily line edit (now) | ~8–12 | This book’s files, characters, Ondaatje / Dickey / King, sequential-thinking, professional-editor |
| Look something up | +2–4 | Firecrawl, ebook, Gutenberg, Goodreads, Wikipedia |
| Craft / reverse-engineer | +2–4 | COMPASS guides, fiction reverse-engineering, style emulation |
| Print / export | +1 | Pandoc |
| Life around the desk | Cursor plugins | Google Calendar, Gmail, Drive — not inside the novel config |
| Parked | Off | Figma, Blender, Docker, Airflow, Jupyter, Netlify, Clerk |

Customize → MCPs is the real on/off. A `disabled` flag in the JSON file often does not stop Cursor from launching a server.

---

## 4. Orchestrator — honest

Cursor Workflow Orchestrator (January 2026) lives inside Walk This Way under zz_COMPASS. It keyword-matches (character / plot / style / research), is hardcoded to Nick / Jackie / Maxanne, writes disabled flags Cursor may ignore, and was built for 27 servers. Status came back empty on 22 Aug 2026.

- Safe to leave sitting there. It is not managing anything real.
- Do not click its enable/disable tools as your daily control.
- Do not rewrite it this week. Map first. Move COMPASS out. Then named kits (Daily / Research / Print / Parked).

---

## Order of work — do not skip ahead

1. Agree this map (done enough to print; confirm in the morning).
2. Name a daily Draft_06 set (~10). Leave the rest off in Customize.
3. Stop adding new MCPs until the toolkit repo is the one copy.
4. Move zz_COMPASS / MCP source into MCP Library + COMPASS (one pile). Separate sitting. Not with coffee and a chapter open.
5. Novel mcp.json becomes short. Toolkit and Mac hold the machines.
6. Then, if you still want it: orchestrator as named kits, not 104 toggles.

## Do not

- Flatten Draft_1–05 into git and delete the folders.
- Copy the toolkit into Senseless or the next book.
- Write another reorganization plan that sits in `.cursor/docs` and gets forgotten.
- Rebuild the orchestrator before step 5.
- Start a new novel until one rewrite is actually in motion. The tools will never feel finished if the test is “ready for eight books at once.”

---

## Where these files live

- This novel: `Walk This Way/Writing_System_Map/`
- Next to all the books: `03_Novels/Writing_System_Map/`

No folders were moved when this pack was made. 22 Aug 2026.
