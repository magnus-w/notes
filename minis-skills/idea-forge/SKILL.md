---
name: idea-forge
version: 1.0.0
description: Adaptive six-stage interview for developing a raw creative idea (story, product, essay, strategy, research question, or any concept) into a fully formed one. Trigger when the user says "Idea Forge", "develop this idea", "run the six-stage framework", or asks for a structured back-and-forth to develop/interrogate/stress-test a concept. Works like Save the Cat or the Scientific Method but domain-agnostic and interview-driven: one question at a time, next question adapts to the previous answer, with recap checkpoints between stages.
---

# Idea Forge

A domain-agnostic idea-development framework, run as an adaptive interview: one question at a
time, each answer shapes the next question. Six stages, each with its own function and question
bank. Works for stories, products, essays, strategy, research questions — any raw concept.

## Core Principles

- **One question at a time.** Never dump a full list. Wait for the answer before asking the next.
- **Adapt, don't script.** Question banks below are seeds, not a fixed script. Pick the one that
  follows naturally from what the user just said; skip questions already answered implicitly;
  invent a sharper follow-up when the user's answer reveals something the bank didn't anticipate.
- **Checkpoint between stages.** After each stage, give a 2-4 sentence recap of what's been
  established, then ask permission to move on ("Ready to move to [next stage], or want to dig
  more here?"). This is the "checkpoint" behavior the user asked for.
- **Bounce, don't just record.** Don't act as a passive stenographer. Push back gently when an
  answer is vague, contradicts an earlier answer, or avoids the hard part. Offer a sharper
  reframing if useful. This is the "bouncing board" behavior.
- **Short turns.** Ask, wait, react in 1-3 sentences + next question. Save synthesis for
  checkpoints and the final document.
- **No forced order rigidity.** If the user's answer to a Stage 2 question actually resolves a
  Stage 4 question, acknowledge it and don't re-ask it later.

## The Six Stages

1. **Provocation** — surface the itch. What triggered this, and why now?
2. **Divergence** — widen without filtering. What are ALL the directions this could go?
3. **Framing** — commit. What's actually in scope, what's deliberately out?
4. **Complication** — pressure-test. What resists, breaks, or surprises when you push on it?
5. **Confrontation** — reality-check. Does it survive contact with an audience/critic/reality?
6. **Synthesis** — land it. What's the final shape, and what changed in your understanding?

## Workflow

1. **Trigger & orient.** When invoked, briefly state you'll run the six-stage interview, one
   question at a time, with a recap before each new stage. Ask what the raw idea/topic is if not
   already given.
2. **Run Stage 1 (Provocation).** Ask ONE opening question from the bank below (or a better one
   the seed idea suggests). React briefly, then ask the natural follow-up.
3. **Progress through stages 2-6** the same way — one question, react, follow up as needed
   (typically 2-4 exchanges per stage, more if the user is engaged and the material is rich).
4. **Checkpoint after each stage**: recap in 2-4 sentences what's now established, note any
   tension or open thread, ask if they want to continue or linger.
5. **After Stage 6**, offer to write up the full session as a structured markdown summary
   (stage-by-stage: question threads + answers + the emerging shape of the idea). Only write the
   file if the user confirms and gives/approves a location (default to
   `/var/minis/shared/notes/projects/` unless told otherwise).
6. **Mid-session exits are fine.** If the user wants to stop early, offer a checkpoint recap of
   everything so far rather than forcing completion.

## Question Bank (seeds — adapt freely)

### 1. Provocation
- What sparked this? A specific moment, a frustration, something you saw or read?
- If you didn't develop this idea at all, what would you regret not exploring?
- Who is this itch really for — you, a specific audience, a problem you keep seeing?
- What's the one-sentence version, even if it's rough?

### 2. Divergence
- If there were no constraints — budget, time, format, skill — what are three wildly different
  directions this could take?
- What's the version of this idea you're afraid is too weird/big/simple to say out loud?
- What existing thing (film, product, essay, business) is this in conversation with — and how
  does it differ?
- If you had to make this idea unrecognizable from its current form but keep its core, what
  would you change?

### 3. Framing
- Of everything you just named, what are you actually committing to right now?
- What's explicitly NOT this idea — what would dilute or derail it if you tried to include it?
- Who is this for, specifically? Who is it deliberately not for?
- What constraint (length, budget, medium, deadline, audience) is real and non-negotiable?
- In one sentence: what does this idea promise the audience/user/reader?

### 4. Complication
- What's the biggest thing standing in the way of this working?
- Where does your own interest/energy dip when you imagine developing this further?
- What would someone who dislikes this idea say is wrong with it?
- What happens to the idea if you remove its most obvious/expected element?
- What's the hardest true thing you know about this that you haven't dealt with yet?

### 5. Confrontation
- If you showed this to the toughest honest critic you know, what would they flag first?
- What's the most likely way this fails in the real world (gets ignored, misunderstood,
  outcompeted, falls apart under its own logic)?
- What evidence, reaction, or test would actually change your mind about this idea?
- Has anything you've said in this conversation contradicted something you said earlier? (ask
  yourself this as the agent, and raise it if so)

### 6. Synthesis
- Say the idea now in one sentence — how is it different from the one you opened with?
- What's the very next concrete step, and when will you take it?
- What did developing this just now change about how you understand it?
- What are you now confident about, and what are you consciously leaving unresolved?

## Output Format (if user requests a written summary)

```markdown
# [Idea Title] — Idea Forge Session

## 1. Provocation
[synthesized answer/thread, not raw Q&A transcript]

## 2. Divergence
...

## 3. Framing
...

## 4. Complication
...

## 5. Confrontation
...

## 6. Synthesis
- Final one-line statement of the idea:
- Next concrete step:
- Open/unresolved threads:
```

Keep each section to a tight paragraph or bullet list — synthesized, not a verbatim transcript.
