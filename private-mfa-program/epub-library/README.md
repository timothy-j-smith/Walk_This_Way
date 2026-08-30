# Master EPUB Library — Private MFA Study Only

**Not for publication. Not for distributing your work.**

This folder holds **other people's novels** that you legally own (purchased EPUBs) so the `ebook` MCP can read them during MFA exercises — reverse engineering, compare/contrast, emulation setup.

Your Walk This Way prose stays in `Draft_06/` as plain `.txt` files. Use Cursor **Read** for that. You do **not** need to convert your novel to EPUB.

---

## Folder layout

```
epub-library/
├── masters/              # Novels you own — craft masters for study
│   ├── dickey/
│   ├── ondaatje/
│   ├── king/
│   ├── lehane/
│   ├── robinson/
│   └── other/
└── _inbox/               # Unsorted purchases — move into masters/{author}/
```

---

## What EPUB means here

EPUB is the **file format** ebooks come in when you buy them (Kindle, Kobo, Apple Books, etc.). The `ebook` MCP opens those files on your Mac so the agent can pull passages for private study.

It is **not** a publishing tool. Nothing here uploads, sells, or distributes your writing.

---

## Example use

Drop `English_Patient.epub` into `masters/ondaatje/`, then in chat:

- "Use **ebook** — read the opening of the Ondaatje EPUB for RE setup"
- "Use **ebook** — compare how Ondaatje handles time jumps vs my Ch 15 in Draft_06"

For **your** chapters, the agent reads `Draft_06/Chapter_15_Landslide.txt` directly — no EPUB involved.

---

## Git

Purchased ebooks are gitignored (`*.epub`, etc.). Only this README and empty folders are tracked.
