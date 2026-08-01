---
name: "books-notes"
description: "Extract highlights and notes from one or more Apple Books via the local Books SQLite databases and save them as a markdown file in projects/booknotes/ in the notes repo. Use when Magnus asks for his Apple Books highlights, Books notes, or to pull notes from a specific book. Runs only via Claude Code on Magnus's MacBook, not on The Well."
---

## Apple Books Notes skill

Extracts highlights and notes from Magnus's Apple Books library and saves them as a markdown file in `projects/booknotes/` in the notes repo (`/Users/magnus/GitHub/notes`). A file can contain more than one book if he selects several. Mirrors the structure of the kindle-notes skill, adapted for a different data source: there is no Apple Books web page, so this reads two local SQLite databases directly instead of scraping a browser page.

### Prerequisites

- This skill runs only via Claude Code on Magnus's MacBook, in Terminal.app, with local filesystem access. It cannot run on The Well (the remote GCP VM) — the database paths referenced below only exist on the Mac itself. If invoked from a context without that access, say so up front rather than attempting it and failing partway through.
- Terminal.app needs Full Disk Access, granted once in System Settings → Privacy & Security → Full Disk Access. Without it, the first database read fails with a permissions error rather than any interactive prompt. If a query fails this way, tell Magnus to check that setting rather than retrying blindly.
- Ask Magnus to open Books.app briefly before running this, if he's read on iPhone or iPad recently — this triggers an iCloud sync check for annotations made on other devices. There's no external signal that the sync has finished, so treat this as a rough wait (on the order of 30 seconds) rather than something to verify.
- Data lives in two local SQLite databases:
  - `~/Library/Containers/com.apple.iBooksX/Data/Documents/BKLibrary/BKLibrary*.sqlite` — book metadata (asset ID, title, author).
  - `~/Library/Containers/com.apple.iBooksX/Data/Documents/AEAnnotation/AEAnnotation*.sqlite` — the highlights and notes themselves, linked to books by asset ID.
- Covers EPUB annotations only. PDF annotations in Apple Books are stored in a different structure and are not covered by this skill.
- Use the helper script kept alongside this skill, at `.claude/skills/books-notes/books-notes-export.sh` (relative to the repo root), rather than writing raw SQL inline each time — it locates the current database files and returns clean JSON. Always invoke it by that path; it is not on `PATH`.

### Invocation

When Magnus invokes this skill without naming a book, present a short menu:
1. Choose from a list of his annotated books
2. Name the book(s) directly

If he names one or more books in the same message that invokes the skill, skip the menu and go straight to fetching those.

For "choose from a list": run `.claude/skills/books-notes/books-notes-export.sh list` and show the results numbered (title, author, highlight count) so he can reply with which one(s).

For "name the book(s)": run `.claude/skills/books-notes/books-notes-export.sh list`, match against the titles returned, and confirm the match if there's ambiguity (e.g. multiple editions or a partial title match).

### Process (per book)

1. Get the book's `asset_id` from the `list` output.
2. Run `.claude/skills/books-notes/books-notes-export.sh export <asset_id>` to get all highlights and notes for that book, already ordered by physical location.
3. For each entry in the returned JSON: `text` is the highlighted passage, `note` is any attached note (often null), `chapter` is the chapter name, `location` is the spine index used for ordering, `cfi` is the raw EPUB CFI string (a fallback reference, not needed for normal output).
4. Group the highlights by chapter, keeping the order returned. Two quirks to expect:
   - `chapter` is null for many highlights even when other highlights in the same chapter have it — Books doesn't record it consistently. Fill a missing `chapter` from another highlight sharing the same `location`.
   - If a `location` has no chapter name anywhere, derive it from the offset between `location` and chapter number — but only when that offset is identical for every chapter in the book. Otherwise fall back to a `Location {location}` heading.
   - Never display a raw `location` as if it were a page or Kindle-style position. It is a spine index, and `ZPLABSOLUTEPHYSICALLOCATION` is 0 for most books.
5. Build the book's markdown:
   - Single book: `# {Book Title} — {Author}` at the top, then `## {Chapter}` per chapter.
   - Multiple books: `## {Book Title} — {Author}` per book, then `### {Chapter}` per chapter.
   - Under the title, one italic metadata line: `_{N} highlights from Apple Books._` Don't include highlight dates anywhere in the file — position in the book is the only ordering Magnus wants.
   - One block per highlight:
     ```
     > {text}

     **Note:** {note}
     ```
     (omit the `**Note:**` line entirely when `note` is null or empty; collapse any internal newlines/runs of whitespace in `text` and `note` to single spaces so the blockquote stays one paragraph)

### Output

- Save into `/Users/magnus/GitHub/notes/projects/booknotes/` (i.e. `projects/booknotes/` relative to the repo root). Create the folder if it doesn't exist.
- Filename for a single book: `{Book Title}.md` — the book title exactly as it appears in the `list` output, minus any characters that can't go in a filename (`/` and `:` become ` - `). Don't add the author, a date, or a slug.
- If multiple books were selected: one file with each book as its own `##` section in the order selected, saved as `{Book Title 1} & {Book Title 2}.md` (join additional titles with `&` too; if this gets unwieldy for 3+ books, use `Apple Books Notes {YYYY-MM-DD}.md` instead and list the books in a one-line intro at the top of the file).
- Tell Magnus the full path of the file that was written.

### Notes

- No write operations are performed on the Books databases — this is a one-way, read-only export.
- If Magnus asks to re-run this for a book he's already exported, regenerate and overwrite/re-save rather than diffing against the previous file. If he's added highlights since the last export, a fresh full extraction is simpler and more reliable than incremental tracking.
- If a book shows zero highlights in the `list` output despite Magnus expecting some, check whether Books.app has finished its iCloud sync before concluding the highlights don't exist.
