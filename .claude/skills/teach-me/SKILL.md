---
name: teach-me
description: "Self-paced walk through the core concepts that make Marketing OS click. Interactive, skippable, resumable — teaches one concept at a time from the concept registry. Use when the operator wants to understand how the system works, or says 'teach me', 'walk me through the concepts', 'how does this work'."
disable-model-invocation: true
---

# Teach Me

An interactive, self-paced walk through the core concepts. The operator drives — they can go through all of them, pick one, or stop anytime. Never lecture; teach one concept, check in, move on.

**Source of truth:** `curriculum/concepts.md` (the registry — definitions and triggers live there, not here). This skill is just the *walk*.
**Progress state:** `_system/onboard-log.md` — mark a concept Introduced once you've taught it, so `/done` micro-teaching doesn't re-teach it.

---

## Procedure

### 1. Load state

Read `curriculum/concepts.md` (the concepts) and `_system/onboard-log.md` (what's already been introduced). If `onboard-log.md` doesn't exist, that's fine — treat all concepts as un-introduced.

### 2. Orient the operator

Tell them briefly what this is and let them steer:

> "There are [N] core concepts that make this system click. I can walk you through them one at a time — you can stop whenever, and we'll pick up where we left off next time. Want the ones you haven't seen yet, all of them, or is there a specific one you're curious about?"

Show the list with status, e.g.:

> 1. The loop — close every session with `/done` ✓ (seen)
> 2. The backlog is your brain — *not yet*
> 3. Quality gates — how to talk to the system — *not yet*
> …

Default to the un-introduced ones in order. Honor any pick.

### 3. Teach one concept

For each concept the operator agrees to, compose a short spoken-style teach (~30–60 seconds of reading) from the registry entry:

- **Name it** plainly.
- **Explain** it in your own words (don't paste the file — talk).
- **Give the example** (use the registry's, or a better one drawn from *this* operator's actual work if you know it).
- **Say when it matters** — the trigger, framed as "you'll feel this when…".

Then **check in** before moving on:

> "Make sense? Want to go deeper on this one, or move to the next?"

If they want depth, point to `curriculum/playbook.md` for the full treatment, or expand inline. One concept at a time — never dump all of them at once.

### 4. Mark progress

After teaching a concept, update `_system/onboard-log.md`: mark that concept **Introduced** (this session, today's date). This is what keeps `/done` from re-teaching it. If the operator clearly *got* it (asked a sharp question, connected it to their work), you can note it reinforced too — but introduced is the minimum.

### 5. Close

When they stop (whether after one concept or all six):

> "That's where we'll pick up next time — run `/teach-me` whenever. The full how-it-works doc is `curriculum/playbook.md`, and `/system` is your reference hub anytime you're unsure where something lives."

If all core concepts (1–3) are now introduced *and* reinforced, note that they're through the essentials.

---

## Notes

- **Resumable by design.** State lives in `onboard-log.md`, not here. A fresh session reads it and knows exactly what's left.
- **Pull, not push.** This is the operator *choosing* to learn. The complement is `/done` micro-teaching, which drips one concept per session automatically. Same registry, same progress log — they never double-teach.
- **Don't gate real work on this.** `/teach-me` is optional and self-paced. The system is fully usable without finishing it.
