---
name: new-reminder
version: 1.0.0
description: Create a new reminder in the "Taskbar" Reminders list. Trigger when the user says "New Reminder", "new reminder", or asks to add/create a reminder without specifying a list. Always targets the Taskbar list.
---

# New Reminder

Creates a reminder in the **Taskbar** list via `apple-reminders create`.

Note: Reminders app "sections/columns" (e.g. "Inbox") are a UI-only grouping with no public API — cannot be set programmatically. Only list, title, due date/time, priority, notes are settable. Do not attempt to target a section.

## Workflow

1. Ask the user for:
   - **Title** (required)
   - **Due date** (optional)
   - **Due time** (optional, only relevant if a date was given)
2. Title is the only required field — if the user gives just a title, create it immediately with no due date, don't force date/time questions.
3. If a date is given without a time, default to 09:00.
4. If the user gives relative dates ("tomorrow", "friday"), resolve to an actual date using current time context.
5. Run:
   ```
   apple-reminders create --title "<title>" --list "Taskbar" --due <YYYY-MM-DDTHH:MM> --compact
   ```
   Omit `--due` entirely if no date was given.
6. Confirm briefly what was created (title, list, due date/time if set).
