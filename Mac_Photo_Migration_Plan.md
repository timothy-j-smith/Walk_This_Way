# Photo Migration Plan — Crucial 4 TB SSD

**Owner:** Timothy J. Smith  
**Created:** August 22, 2026  
**Hardware:** Mac Studio (primary), MacBook Air, iPhone  
**Target drive:** Crucial X10 Pro — `Crucial Photos` (4 TB, APFS, not encrypted)  
**Future backup drive:** LaCie 2 TB (Time Machine — configure after LaCie is wiped)

**Purpose of this document:** Explain where Apple Photos actually live, what “main” vs “backup” means, and give step-by-step instructions for Timothy or the next Cursor agent to move ~80,000 photos/videos off the Mac Studio internal disk and onto the Crucial SSD without breaking iCloud sync.

---

## Part 1 — Where Are Your Photos Right Now? (Plain English)

### 1.1 The three places photos can exist

| Location | What it is | Your situation |
| --- | --- | --- |
| **iPhone** | Camera + local cache | New photos start here |
| **iCloud Photos** | Apple’s cloud sync (you have **2 TB** iCloud storage) | Likely holds **full-size originals** for everything synced |
| **Mac Studio** | `~/Pictures/Photos Library.photoslibrary` (~**41 GB** today) | A **local copy or optimized version** — not necessarily all 80,000 originals at full size |

### 1.2 iCloud Photos ON — how it actually works

When **Settings → Apple ID → iCloud → Photos → Sync this Mac** is **ON**:

1. **iCloud is the hub.** Apple treats iCloud as the sync master for your library.
2. **Each device chooses how much to keep locally:**
   - **Download Originals to this Mac** → full library on internal disk (uses lots of space).
   - **Optimize Mac Storage** → Mac keeps smaller versions; full originals stay in iCloud and download only when needed.
3. **Your Mac Studio library (~41 GB)** is almost certainly **not** all 80,000 originals at full resolution — unless you explicitly chose “Download Originals.”

**Bottom line:** With iCloud Photos on, **originals live in iCloud** (within your 2 TB plan). The Mac holds a **working copy**, which can be slim or fat depending on one checkbox.

### 1.3 “Main” vs “backup” — stop the confusion

| Term | Meaning | What Timothy wants |
| --- | --- | --- |
| **Main / live library** | Where day-to-day Photos app edits, albums, and iPhone sync happen | Probably **keep iCloud Photos** for family/iPhone workflow |
| **Archive / cold storage** | Full originals on Crucial, off the Mac internal disk | **Crucial 4 TB** — work photos, exports, old drive imports, things **not** in shared iCloud |
| **Backup** | Second copy if something fails | **LaCie Time Machine** (Mac files) + optionally a **full export** on Crucial |

**Crucial is NOT a Time Machine replacement.** It is **photo housing / archive**. Time Machine on LaCie backs up the **Mac**, not your entire iCloud account.

### 1.4 Recommended strategy for Timothy (hybrid — simplest)

Do **not** try to move all 80,000 iCloud photos to Crucial as the only master in one step. That fights Apple’s design.

Instead:

1. **Mac Studio:** Turn on **Optimize Mac Storage** → frees internal disk; iCloud keeps originals.
2. **Crucial:** Be the **archive** for:
   - Work photos **removed** from shared Apple Photos
   - Photos from old drives (**Other-Archives**)
   - Full **exports** of anything you want guaranteed on physical media
3. **Optional later:** A **second Photos library file** on Crucial for a completely separate collection (no iCloud).
4. **LaCie (later):** Time Machine for Mac Studio — includes the Photos library *file* on Mac, not a substitute for iCloud.

---

## Part 2 — Before You Move Anything (Checklist)

### 2.1 Verify current iCloud Photos settings (Mac Studio)

1. Open **System Settings**.
2. Click your **Apple ID** name at top.
3. Click **iCloud**.
4. Click **Photos** (or **See All** → Photos).
5. Note whether **Sync this Mac** is ON.
6. Open **Photos** app → **Settings** (Cmd+,) → **General**:
   - If **“Download Originals to this Mac”** is selected → this is why space is used. Switch to **Optimize Mac Storage**.
   - If already optimized → Mac is lean; iCloud holds full originals.

### 2.2 Verify iPhone settings

1. **Settings → [Your Name] → iCloud → Photos**.
2. **Sync this iPhone** — usually ON.
3. **Optimize iPhone Storage** vs **Download and Keep Originals** — same idea as Mac.

### 2.3 Confirm Crucial is ready

- Volume name: **Crucial Photos**
- Format: **APFS** (not encrypted)
- Folders already created:

```
/Volumes/Crucial Photos/Photos/
├── Work-Private/
├── From-Apple-Photos-Archive/
├── Other-Archives/
└── Incoming-Sort-Here/
```

### 2.4 Check free space

- Crucial: ~4 TB free
- Estimate: 80,000 photos/videos might be **500 GB – 2 TB+** depending on video. Crucial is large enough, but run a test export first.

---

## Part 3 — Free Mac Studio Space (Do This First)

### 3.1 Enable Optimize Mac Storage

1. **Photos** app → **Settings** → **General**.
2. Select **Optimize Mac Storage**.
3. Wait. macOS removes full-size local copies over time (hours to days). iCloud originals stay safe.
4. **Do not** disable iCloud Photos unless you know exactly why.

### 3.2 Confirm space recovery

1. **Apple menu → System Settings → General → Storage**.
2. Watch **Photos** size shrink over time.
3. Internal `Photos Library.photoslibrary` may stay ~ tens of GB (database + previews) — that is normal.

**Expected outcome:** Mac Studio stops being the “warehouse” for full originals; iCloud remains source of truth for synced library.

---

## Part 4 — What Goes on Crucial (Three Workflows)

### Workflow A — Work / private photos (leave shared iCloud)

**Use folder:** `Photos/Work-Private/`

1. Open **Photos** on Mac Studio.
2. Select work photos (Smart Album or manual selection).
3. **File → Export → Export Unmodified Original** (keeps full quality + metadata).
4. Save to: `/Volumes/Crucial Photos/Photos/Work-Private/`
5. Verify export opened correctly (spot-check 5–10 files).
6. **Then** delete from Photos app (moves to Recently Deleted for 30 days — confirm before emptying).
7. Deletion removes them from **shared iCloud library** — kids’ devices will lose access. **That is the goal** for work-only items.

### Workflow B — Archive exports from Apple Photos (backup copy, stay in iCloud)

**Use folder:** `Photos/From-Apple-Photos-Archive/`

1. Select photos (year album, entire library subset, etc.).
2. **File → Export → Export Unmodified Original**.
3. Save to dated subfolder, e.g. `From-Apple-Photos-Archive/2026-export-batch-01/`.
4. **Do not delete** from Photos if you want them to remain in iCloud.

**This is a physical backup layer** — not the live library.

### Workflow C — Photos from old drives / not in iCloud

**Use folder:** `Photos/Other-Archives/`

1. Copy folders from LaCie, old NAS exports, etc. into subfolders by source.
2. No Photos app required — Finder drag-and-drop is fine.
3. Optionally import into a **separate Photos library** on Crucial later (Part 6).

---

## Part 5 — Moving 80,000 Items (Phased Plan)

**Do not export all 80,000 at once on day one.** Phase it.

### Phase 1 — Test batch (50–100 items)

1. Create album **“Crucial Test Export”** in Photos.
2. Add 50 photos + 5 videos (mixed years, HEIC, JPG, MOV).
3. Export Unmodified Original → `Incoming-Sort-Here/test-batch/`.
4. Verify file count matches, videos play, dates intact.
5. Check Crucial eject/reconnect — files still there.

### Phase 2 — Work-private pull (priority)

1. Identify all work-related photos in shared library.
2. Export → `Work-Private/` by project or year.
3. Delete from Photos only after export verified.
4. Document count in a text file: `Work-Private/EXPORT-LOG.txt`.

### Phase 3 — Year-by-year archive (optional backup on Crucial)

1. In Photos sidebar, sort **Media Types** or create Smart Albums by year.
2. Export one year at a time → `From-Apple-Photos-Archive/YYYY/`.
3. Log each year: date, count, size in `EXPORT-LOG.txt`.
4. **Keep in iCloud** — this is archive copy only.

### Phase 4 — Old external / NAS photos

1. Copy to `Other-Archives/` with source name in folder.
2. Deduplicate later (don't rush).

### Phase 5 — Reconcile

1. Compare iCloud storage usage (Settings → Apple ID → iCloud).
2. Compare Crucial used space (Finder → Get Info).
3. Decide if a **second Photos library on Crucial** is needed (Part 6).

---

## Part 6 — Optional: Make Crucial a True Photos “Home” (Advanced)

Only do this if Timothy wants a **non-iCloud** library as primary for a subset.

### 6.1 Create new library on Crucial

1. Quit Photos.
2. Hold **Option** → open Photos.
3. **Create New…**
4. Name: `Crucial Archive.photoslibrary`
5. Location: `/Volumes/Crucial Photos/Photos/`
6. **Do not** enable iCloud Photos for this library.

### 6.2 Switch between libraries

- Hold **Option** when opening Photos → choose **Crucial Archive** or **System Photo Library**.

### 6.3 When to use this

- Large body of photos **never** going back to iCloud.
- Work archive completely separate from family library.

**This is housing, not backup.** Still export or Time Machine the `.photoslibrary` bundle.

---

## Part 7 — Backup Strategy (Full Picture)

| Layer | What | Protects against |
| --- | --- | --- |
| **iCloud Photos (2 TB)** | Live sync + cloud originals | Phone lost, one Mac dies |
| **Crucial 4 TB** | Physical archive + work exports | iCloud account issues, selective local control |
| **LaCie 2 TB Time Machine** | Mac Studio snapshot | Mac failure, accidental deletes on Mac |
| **Second copy (future)** | Duplicate Crucial to another disk OR Backblaze | Drive failure, fire/theft |

**Gap to know:** Time Machine does **not** replace iCloud and does **not** automatically backup everything in iCloud if “Optimize Mac Storage” is on. **Crucial year-export archives** close that gap for photos Timothy cares most about.

---

## Part 8 — Instructions for the Next Cursor Agent

If Timothy asks an agent to continue this work:

1. **Read this file first.**
2. **Never erase Crucial or LaCie** without explicit confirmation.
3. **Check mount:** `diskutil info "Crucial Photos"` and `ls "/Volumes/Crucial Photos/Photos/"`.
4. **Check Mac library size:** `du -sh ~/Pictures/Photos\ Library.photoslibrary`.
5. **Check iCloud optimize state:** Photos → Settings → General (user must confirm in UI).
6. **Exports:** Always use **Export Unmodified Original**, not “Export Photos.”
7. **Deletes from Photos:** Only after export verified; warn about shared iCloud deletion.
8. **Do not enable encryption** on Crucial unless Timothy explicitly asks.
9. **LaCie:** Reserved for Time Machine after manual backup of existing LaCie data — do not repurpose without confirmation.
10. **Log progress** in `/Volumes/Crucial Photos/Photos/EXPORT-LOG.txt` (create if missing).

---

## Part 9 — Quick Reference Commands (Terminal)

```bash
# Is Crucial connected?
diskutil info "Crucial Photos"

# Mac Photos library size
du -sh ~/Pictures/Photos\ Library.photoslibrary

# List archive folders
ls -la "/Volumes/Crucial Photos/Photos/"

# Open Crucial in Finder
open "/Volumes/Crucial Photos"
```

---

## Part 10 — Decision Summary (Timothy’s Answers)

| Question | Answer |
| --- | --- |
| Where are originals today? | Most likely **iCloud** (with 2 TB plan), not fully on Mac Studio |
| What is Mac Studio holding? | ~41 GB library — optimized/partial local copy |
| Should Crucial replace iCloud? | **No** — use Crucial as **archive + work storage** |
| Should Crucial be encrypted? | **No** (decided Aug 22, 2026) |
| How to free Mac space? | **Optimize Mac Storage** in Photos |
| Is Crucial a backup? | **Archive / housing**; export copies are backup; LaCie TM backs up Mac |
| First physical action? | Optimize Mac Storage → test export 50 photos → work-private export |

---

## Part 11 — When Crucial Is Plugged In

Copy this guide to the drive so it travels with the archive:

```bash
cp "~/Library/Mobile Documents/com~apple~CloudDocs/Cursor/03_Novels/Walk This Way/Mac_Photo_Migration_Plan.md" "/Volumes/Crucial Photos/Photos/"
```

*(Adjust path if file was moved.)*

---

*End of plan. Start with Part 3 (Optimize Mac Storage), then Part 5 Phase 1 (test export).*
