---
type: reference
description: "The concept registry — the single source of the core ideas the system teaches. Read by /teach-me (pull) and /done micro-teaching (push)."
status: draft
---

# Concepts

> **LLM-drafted, not operator-vetted.** This is a first-pass concept set. The concept *selection* is the operator's call — trim, add, or rewrite freely. Marked `status: draft` until reviewed.

The few ideas that make this system click. Most people who bounce off Claude Code do so because they're missing one of these — not because the tool is hard.

**This file is the single source.** Two surfaces teach from it:
- **`/teach-me`** (pull) — the operator walks these on demand, self-paced.
- **`/done` micro-teaching** (push) — drips one concept per session, triggered by what the operator just did.

Both mark progress in `_system/onboard-log.md` so a concept is never taught twice. Definitions and triggers live **here**; the surfaces just decide *when* to teach.

**For the deep version,** `curriculum/playbook.md` is the read-end-to-end "how to work" doc. This registry is the atomic version — one idea at a time.

Concepts 1–3 are **core** (graduation-gating: once introduced *and* reinforced, the operator is off training wheels). 4–6 deepen.

---

## 1. The loop — close every session with `/done`

**What it is:** A session's work only becomes permanent when you close with `/done`. It routes what you learned to its home, updates your "where you left off," and commits to git. Skip it and the session evaporates — next time you start from scratch.

**Example:** You spend an hour refining your cold-email angle. You close the laptop. Without `/done`, next week the system has no memory of it. With `/done`, you open `/start` and it says "here's the angle you landed on last time."

**When it matters:** Every single session. This is the one habit that, missed, breaks everything downstream.
- *First exposure trigger:* the operator runs `/done` for the first time.
- *Reinforcement:* by the 2nd session.

---

## 2. The backlog is your brain

**What it is:** You don't hold work in your head. You capture it to the backlog — a one-line task — and the system picks it up later. `/start` reads the backlog and tees up what's next. The backlog *is* the memory; you're free to forget.

**Example:** Mid-session you think "I should test a LinkedIn version of this." Instead of trying to remember, you say so — it lands in the backlog. Three sessions later, `/start` surfaces it: "you wanted to test a LinkedIn version."

**When it matters:** Any time something surfaces that you can't do right now. Capture it, move on.
- *First exposure trigger:* the operator captures or references a backlog item.
- *Reinforcement:* backlog interaction across 2+ sessions.

---

## 3. Quality gates — how to talk to the system

**What it is:** The system will hand you confident-sounding work whether or not it's good. Your job is to *not* take it at face value. The highest-leverage moves: make it **critique its own work**, **push back** when something's off, and **verify the artifact** (check the actual output, not the summary of it). You direct the quality; the system supplies the volume.

**Example:** It drafts an email. Instead of accepting it, you say "critique this and flag the weakest line." It finds the generic opener you'd have missed. One sentence of pushback, much better output.

**When it matters:** Every deliverable. The difference between 3x and 10x is almost entirely here.
- *First exposure trigger:* the operator corrects or pushes back on system output.
- *Reinforcement:* by the 5th session.

---

## 4. You direct it — pitch before the work

**What it is:** Before a real piece of work, the system should tell you what it thinks the task is, what it'll produce, and what it'll reference — *then wait for your go.* You're the driver. A 30-second alignment up front beats a confident wrong turn. When the system pitches, read it and correct the aim before it swings.

**Example:** You say "write the follow-up." It pitches: "I read this as a nudge to the people who opened but didn't reply — short, one new angle, pulling your last email for voice. Good?" You catch that it's actually for non-openers. Fixed before a word was written.

**When it matters:** The start of any non-trivial task. If the system dives in without pitching, that's your cue to slow it down.
- *First exposure trigger:* the system pitches a task, or the operator redirects a dive-in.
- *Reinforcement:* across 2+ sessions.

---

## 5. Cross-loop compounding

**What it is:** Context built in one workspace can feed another. What the system learns about your voice, your market, your patterns doesn't stay siloed — it compounds across everything you run. The more you work in it, the more each new piece starts from somewhere instead of zero.

**Example:** The voice the system learned drafting your emails shows up when you later write a landing page — you didn't re-teach it. A market insight from one client's research sharpens how you frame another's.

**When it matters:** Once you're running more than one workspace, or returning to related work weeks later.
- *First exposure trigger:* a second workspace/context exists, or intelligence flows between pieces.
- *Reinforcement:* observed compounding.

---

## 6. System hygiene — keep it healthy as it grows

**What it is:** A system that grows through use also accumulates cruft — stale notes, half-finished structure, drift. `/audit` is the periodic health check that catches it. You don't need it early; you need it once the system is big enough to hide problems from you.

**Example:** Six weeks in, you've got context docs that contradict each other. `/audit` surfaces the conflict so you reconcile it before it misleads a future session.

**When it matters:** Once the system has real accumulated state — roughly after the first handful of weeks.
- *First exposure trigger:* ~8 sessions in.
- *Reinforcement:* first `/audit` run.
