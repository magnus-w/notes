# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A personal Markdown notes repo, not an application. There is no build, no test suite,
and no linter — don't look for one or invent one. Content is a mix of Swedish and
English; match the language of the file you're editing.

The repo is cloned on more than one machine (this Mac and `linux`, a GCP VM on the
tailnet), which is why the sync machinery below exists.

## Sync: `todoc`

`todoc` is the only way this repo is meant to be committed and pushed. It is a shell
function defined in `shell/todo.sh`, sourced from `~/.zshrc` (Mac) and `~/.bashrc`
(linux) — the rc files each contain one line pointing here.

It commits in two stages: `todo/` first as `todo: update <stamp>`, then everything
else as `notes: sync <stamp>`, so task churn doesn't bury real note edits in the log.
Then `git pull --rebase --autostash` and push, aborting the rebase and leaving the
repo untouched if anything conflicts.

**The second stage runs `git add -A` over the whole repo.** Anything you leave in the
working tree gets committed on the user's next sync, under a commit message that
says nothing about it. Write scratch files to the session scratchpad, not here.

`todo/*.txt` is union-merged via `.gitattributes` so tasks added on both machines
concatenate rather than conflict. Consequence: the same task can appear twice if it's
edited on both sides. Don't "fix" the union merge — it's deliberate.

## How the todo.txt config resolves

Worth knowing before changing anything under `shell/`, because the chain crosses
files that live outside the repo:

```
~/.zshrc | ~/.bashrc      one line, sources the next file
  └─ shell/todo.sh        derives NOTES_REPO from its own path, exports
                          TODOTXT_CFG_FILE, defines the todo alias and todoc()
       └─ shell/todo.cfg  derives the repo root from $TODOTXT_CFG_FILE,
                          sets TODO_DIR=<repo>/todo
            └─ todo/      todo.txt, done.txt, report.txt
```

Both files self-locate rather than hardcoding a path, so the repo can sit at a
different location on each machine. Keep it that way. `shell/todo.sh` must stay
valid in **both** bash and zsh — it's sourced by both, and branches on
`$ZSH_VERSION` for repo-root detection and completion setup.

Editing `shell/` changes the user's live shell on both machines after a pull. Treat
it with more care than a note.

## Layout

- `inbox/` — unsorted notes; the default landing place for something new.
- `projects/` — per-project notes (`skriv/` writing, `tex/`, `diplomat/`,
  `booknotes/`).
- `templates/` — HTML/PDF conversion tooling, plus `template.html`.
- `shell/` — dotfile sources, described above.
- `todo/` — todo.txt data files.

## Commands

```bash
python3 templates/convert.py <file.md> [out.html]   # self-contained HTML; needs pandoc
.claude/skills/books-notes/books-notes-export.sh list           # Apple Books highlights
.claude/skills/books-notes/books-notes-export.sh export <id>
```

`convert.py` reads optional YAML frontmatter (`title`, `subtitle`, `from`, `date`),
falling back to the first `#` heading and today's date. It shells out to pandoc for
the markdown→HTML fragment, then builds a TOC from the h2/h3 elements and inlines
everything into `templates/template.html`.

`md2pdf` is on `PATH` but lives outside the repo (`~/.config/md-templates/md2pdf.sh`)
and is interactive — it prompts for paths, so it can't be driven non-interactively.

## Two traps

**`templates/ReadMe.md` does not describe this repo.** It documents a separate Claude
desktop "Cowork" workspace with a research/writing/design agent team (Riley, Tessa,
Dusty) and references `/system/*.md` and `/projects/project/` — neither path exists
here. It's kept as reference material. Don't follow it as this repo's workflow or try
to resolve its paths.

**The `books-notes` skill is Mac-only.** It reads local Apple Books SQLite databases
under `~/Library/Containers/com.apple.iBooksX/`, needs Full Disk Access for the
terminal, and cannot run on the linux VM. Say so up front rather than failing
partway. See `.claude/skills/books-notes/SKILL.md` for the extraction rules — notably
that `location` is a spine index and must never be presented as a page number.
