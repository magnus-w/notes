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
| **append** (or **a**) | `todo a 3 "additional text"` — Append text to task #3 |
| **prepend** (or **p**) | `todo p 3 "text at start"` — Prepend text to task #3 |
| **replace** | `todo replace 3 "New task text"` — Replace entire task #3 |
| **edit** | `todo edit 3` — Open task #3 in `$EDITOR` |
| **prioritize** | `todo prioritize 3 A` — Set task #3 to priority A (A-Z, where A is highest) |
| **deprioritize** | `todo deprioritize 3` — Remove priority from task #3 |

## Filtering & Search

| Command | Usage |
|---------|-------|
| **lf** | `todo lf pattern` — List task IDs matching pattern |
| **listfile** | `todo listfile "filename"` — List tasks from a specific file |
| **listcon** | `todo listcon` — List all contexts (@-prefixed tags) |
| **listproj** | `todo listproj` — List all projects (+prefixed tags) |

## Other

| Command | Usage |
|---------|-------|
| **help** | `todo help` — Show all commands |
| **report** | `todo report` — Show task statistics |
| **shorthelp** | `todo shorthelp` — Brief command summary |
| **version** | `todo version` — Show version |

## To edit an existing task specifically:

```bash
todo edit 3        # Opens task #3 in your default editor
```

Or without opening an editor:

```bash
todo replace 3 "New task text"    # Replace entire task
todo a 3 " +newproject @newtag"   # Append to task #3
```

## List tasks with IDs:

```bash
todo ls
```

This shows all tasks with their IDs, so you can reference them in commands.
