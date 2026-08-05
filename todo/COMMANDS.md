# todo.txt CLI Commands

## Core Commands

| Command | Usage |
|---------|-------|
| **add** | `todo add "Buy milk @shopping"` — Add a new task |
| **ls** | `todo ls` — List all tasks |
| **list** | `todo list` — List all tasks (same as ls) |
| **listpri** | `todo listpri [A-Z]` — Show tasks with a specific priority |
| **do** | `todo do 3` — Mark task #3 as done |
| **done** | `todo done 3` — Mark task #3 as done (same as do) |
| **rm** | `todo rm 3` — Delete task #3 |
| **del** | `todo del 3` — Delete task #3 (same as rm) |
| **append** | `todo append 3 "additional text"` — Append text to task #3 |
| **prepend** | `todo prepend 3 "text at start"` — Prepend text to task #3 |
| **replace** | `todo replace 3 "New task text"` — Replace entire task #3 |
| **pri** | `todo pri 3 A` — Set task #3 to priority A (A-Z, where A is highest) |
| **depri** | `todo depri 3` — Remove priority from task #3 |

## Filtering & Search

| Command | Usage |
|---------|-------|
| **listcon** | `todo listcon` — List all contexts (@-prefixed tags) |
| **listproj** | `todo listproj` — List all projects (+prefixed tags) |
| **listall** | `todo listall [TERM]` — List all including archived tasks |
| **listfile** | `todo listfile [FILE] [TERM]` — List tasks from a specific file |

## Other

| Command | Usage |
|---------|-------|
| **help** | `todo help` — Show detailed help |
| **shorthelp** | `todo shorthelp` — Brief command summary |
| **report** | `todo report` — Show task statistics |
| **archive** | `todo archive` — Move done tasks to done.txt |

## To edit an existing task:

```bash
todo replace 3 "New task text"    # Replace entire task
todo append 3 " +newproject @newtag"   # Append to task #3
todo prepend 3 "URGENT: "              # Prepend to task #3
```

**Note:** There is no interactive `edit` command that opens an editor. Use `replace`, `append`, or `prepend` instead, or edit `todo.txt` directly.

## Sync your changes

After editing with the `todo` CLI, run:

```bash
todoc
```

This commits task changes separately, then syncs the whole repo:
- Commits `todo/` as `"todo: update <timestamp>"`
- Commits everything else as `"notes: sync <timestamp>"`
- Pulls and pushes to remote
