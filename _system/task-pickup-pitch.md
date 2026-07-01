---
type: system
governance: core-ref
scope: system
description: "Before picking up a task, the agent aligns on three things — the task, the deliverable, the keystone references — and waits for the go. The forcing function for active grounding at session start."
status: operator-reviewed
created: 1
last-updated: 1
updated-by: joint
---

# Task-Pickup Pitch

## What this is

Before picking up a task, the agent **aligns on it first** — like an intern who shows they understand the work before they're trusted to run with it. It does not "pick up the task and build some stuff." It names what this is, what it's delivering, and the few references the work hinges on — and it waits for the go.

You (the operator) read the pitch, push back if it's thin, and green-light. **You are the enforcement.** This protocol just makes sure the alignment happens before the swing.

## Why it exists

Two failure modes, one root — context arrives *passive* instead of *reasoned-from*:

- **Skip-and-fabricate** — the agent dives in without pulling what it needs, makes things up, doesn't ground the work in anything you've built.
- **Drown-and-obey** — the agent reads a wall of front-loaded context, then mechanically executes the written task, losing its own judgment. (A heavy session dilutes the instruction; a light session plus one clear instruction gets followed with consistency.)

The pitch fixes both by making grounding **active** (the agent reasons about what the task needs) and **light** (it pulls a few keystone references on cue, not a wall up front).

## A new session is usually a new task

Default to pitching at the **top of a session** — that's when a new task almost always arrives. Startup loads nothing eagerly; the pitch is the first move. Within a session, pitch again whenever a genuinely new task is handed over.

**Don't pitch on:** a continuation of a task already aligned this session, a status question, or plain conversation. Those aren't new tasks.

## The three legs

Align on three things, then wait. Lead with the task — if the framing is wrong, the rest is wasted.

1. **The task** — what is this *really* about, in the agent's own words, reconstructed from its brief and the direction — not the title parroted back, the underlying *why*. And: is it framed right? If the agent reads it as stale, mis-aimed, or solving the wrong thing, it says so here and how it'd re-aim it.

2. **The deliverable** — the concrete output, and what *good* looks like. Stated plainly enough that "done" is checkable. This is the leg that keeps the work pointed at the result you actually want, not a plausible-looking artifact.

3. **The keystone references** — the few docs or sources the work genuinely hinges on, *why each bears on it*, and what's deliberately **not** being pulled. Naming the keystones drags the load decision into the open, where a *miss* gets caught before execution. "I might need to search for X" is fair — the menu is the known-good set, not a cage.

**Then wait** for the go before building.

## Loop only as needed — converge, don't grind

Size scales with ambiguity. **Don't gate on "is this substantial enough"** — that judgment is exactly what the agent gets wrong. Instead: always align on new-task pickup, and let the alignment *shrink*.

- **Dead-clear task → one line, one round.** "This is X, deliverable is Y, pulling Z — go." You rubber-stamp and it rolls. Even one line forces a ground-check.
- **Murky task → loop the three legs** with you until they're pinned. But the loop *converges* — it's alignment, not interrogation. If the agent catches itself re-asking settled things, it stops.

Failing safe toward grounding is the point — bounded by: one round when it's clear.

## A note on register (so this doesn't become the disease it's curing)

A pitch that mechanically fills all three legs without thought is a **failed pitch**, even though it has every part. The point isn't the form — it's that the agent actually reasoned about what this task is, what it produces, and what it hinges on. A performed ritual is worse than none: it looks like grounding and isn't. This is reasoning-to-think-with, not law to obey.
