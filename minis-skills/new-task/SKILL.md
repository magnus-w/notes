---
name: new-task
version: 1.0.0
description: Create a new task in the "In the Loop" Notion board (Root Club workspace) via the ntn CLI. Trigger when the user says "New Task" or "new task". Different from "New Reminder" skill (which targets Apple Reminders Taskbar list) — this one targets Notion.
---

# New Task

Creates a page in the Notion **"In the Loop" database** via the `ntn` CLI (public API).

Note: "In the Loop" is the name of BOTH the database itself AND one of the Status select options inside it. Don't confuse the two.

- Data source ID: `dc298401-4be2-48b7-bdde-041d36c1385e` (database titled "In the Loop", lives under the "Home" page in Root Club workspace)
- Title property is called **Task** (not "Name").

## Fields

- **Title** (required) — page title
- **Status** (select) — default to `In the Loop` if user doesn't specify. Other options exist (Inbox, For the Loop, Feedback Loop, Testing, Released, Veckans Glosa) — if user names one, use it.
- **Project** (select, optional) — ask only if not given, don't block on it
- **Due** (date, optional)
- **Energy** (select, optional) — one of: Creative, Admin, Prep

## Workflow

1. Ask the user for: Title, Status (offer "In the Loop" as default), and optionally Project / Due / Energy.
2. Only Title is strictly required — Status defaults to "In the Loop" if unspecified. If the user gives just a title, create immediately without Status/Project/Due/Energy questions, using the default Status.
3. Resolve relative dates ("tomorrow", "friday") to actual dates using current time context.
4. Build the request body and create the page:
   ```
   ntn api /v1/pages -d '{
     "parent": {"data_source_id": "dc298401-4be2-48b7-bdde-041d36c1385e"},
     "properties": {
       "Task": {"title": [{"text": {"content": "<title>"}}]},
       "Status": {"select": {"name": "<status>"}}
     }
   }'
   ```
   Add optional properties only if provided:
   - `"Project": {"select": {"name": "<project>"}}`
   - `"Due": {"date": {"start": "<YYYY-MM-DD>"}}`
   - `"Energy": {"select": {"name": "<energy>"}}`

   Write the JSON body to a temp file first if it contains special characters, then pass with `-d @/tmp/file.json` to avoid shell quoting issues.
5. Confirm briefly what was created (title, status, and any other fields set).
