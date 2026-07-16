# Workflow

How a piece moves from idea to finished draft with Riley, Tessa, and Dusty — and what you, the editor, do at each step.

### Starting a New Project

1. **You** copy the `/projects/project/` folder and rename it to your project name (or just tell Riley about the piece and let her set it up).
2. **You** write the brief — fill in `/projects/[project]/briefs/_TEMPLATE-editor-brief.md` (copied from `/projects/project/briefs/_TEMPLATE-editor-brief.md`). Cover the story, the format (feature, interview, opinion, profile), audience, language, what source material already exists, and your deadlines. Rough notes are fine — Riley will come back with clarifying questions.
3. **You** open the Claude desktop app, select Cowork and add this folder ("content") by clicking the folder icon with plus sign. Then you add the brief document you just wrote by clicking the plus sign to the left of the folder icon with the plus.
3. **You** message: "Riley, new brief ready: @projects/[project]/briefs/[project]-editor-brief.md"
4. **Riley** researches the subject, transcribes or summarizes any interviews, files all of that source material in `/projects/[project]/research/`, and writes a research brief in `/projects/[project]/briefs/`.

### Reviewing the Research Brief

There's no formal sign-off gate here — the research brief is Riley confirming she understood the assignment and surfacing what she found, not a document that blocks progress. Skim it, correct anything that's off, and answer any open questions she's flagged. If you want to go deeper on a source than the brief summarizes, the full material is in `/projects/[project]/research/`.

### Approving a Pitch — a real decision point

Tessa reads Riley's research brief and writes **three pitches** (Hook + Pitch, each entering the material from a different angle) to `/projects/[project]/pitches/`. This is where your input matters most:

- Read all three, ask questions, and pick one — or ask Tessa to combine elements from more than one.
- Tessa will revise the selected pitch based on your feedback before moving on.

### Approving the Outline

Once a pitch is picked, Tessa writes a structured outline to `/projects/[project]/outlines/`. The outline now also spells out any fact boxes or sidebars (what each one covers), any standalone testimony sections if the piece has multiple sources, and where the piece is headed for its headline and closing line — not just the narrative beats. Approve this before Tessa starts drafting; it's cheaper to adjust structure here than after a full draft exists.

### Reviewing the Draft

Tessa writes the full piece to `/projects/[project]/content/`. Give feedback the way you would with any writer — line notes, cuts, questions — and Tessa edits in place. Length and language should already be set from the editor brief; flag it if either needs to change mid-project.

### Design

Once the piece is close to final, Tessa writes design prompts to `/projects/[project]/design/`. Dusty builds the layout, hero image, and any supporting graphics there. Same as content — give feedback and expect iteration.

### Directory Structure

```
/projects/[project]/briefs/     — Editor brief, research brief (templates live here too)
/projects/[project]/research/   — Source material: interviews, recordings, documents
/projects/[project]/pitches/    — Tessa's Hook + Pitch directions
/projects/[project]/outlines/   — Approved pitch, structured into an outline
/projects/[project]/content/    — Written piece and edits
/projects/[project]/design/     — Design prompts and Dusty's design artifacts
/projects/project/              — Empty template: copy this whole folder to start a new project
```

### The Team

- **Riley** — research and analysis, your entry point for a new project (`/system/research-agent.md`)
- **Tessa** — writing, from pitch through finished piece (`/system/content-agent.md`)
- **Dusty** — layout, imagery, and design (`/system/designer-agent.md`)

### Key Skills

- **Feature Research** — how Riley researches a subject before writing the research brief
- **Content Writing** — voice, structure, and the house style Tessa writes in
- **Concept Development** — how Tessa builds pitches from Riley's research
- **Unexpected Methodology** — shared creative-technique reference
- **Visual Design Principles** — Dusty's design craft reference

### Status Updates

Ask Riley or Tessa for a status update any time — what's confirmed, what's still open, what stage a project is at, and who it's waiting on.
