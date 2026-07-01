System reference hub for Marketing OS. The operator's persistent reference point — introduced during setup, reinforced at every teaching moment.

**Route based on invocation:**
- `/system` (no args) → Quick Diagnostic
- `/system practices` → Best Practices
- `/system audit` → route to `/audit`

---

## Quick Diagnostic (Default)

Read the following files in parallel, then present a concise system snapshot:

1. `_system/onboard-log.md` (if it exists)
2. `_system/session-log.md` (last 5 entries)
3. `_system/backlog.md` (Focus Queue section only, if it exists)

### Format the Snapshot

**If onboard log exists and status is `in-progress`:**

```
SYSTEM STATUS

  Onboarding: [N] of 5 concepts introduced, [M] reinforced
  Next concept: [name] — [one-line description of what triggers it]

  Sessions: [count from milestones]
  Last /done: [date from session log]

  [If Focus Queue has items:]
  Next up: [focus queue item]
```

For each concept, show status with a simple indicator:
- Introduced + Reinforced → learned
- Introduced only → introduced (needs reinforcement)
- Not introduced → upcoming

**If onboard log exists and status is `graduated`:**

```
SYSTEM STATUS

  Status: Graduated (Session [N])
  Last audit: [date from session log, or "none"]
  Last /done: [date from session log]

  [If Focus Queue has items:]
  Next up: [focus queue item]

  Run /system practices for operational reference.
  Run /audit for system health check.
```

**If no onboard log exists:**

```
SYSTEM STATUS

  Sessions: [count from session log]
  Last audit: [date, or "none — consider running /audit"]
  Last /done: [date]

  [If Focus Queue has items:]
  Next up: [focus queue item]
```

**Must load fast.** Read a few state files, format a snapshot, done. No analysis, no recommendations beyond what's shown above.

---

## Best Practices

Present core practices for operating the system. If the operator is still onboarding (status = `in-progress`), frame as a curriculum with concept status markers. Post-graduation, present as an operational reference.

**Core practices to cover:**

1. **Context management.** Context is a finite resource. `/clear` between unrelated tasks. Subagents for heavy research. Break points at phase boundaries.
2. **`/done` is mandatory.** Routes knowledge, updates backlogs, commits to git. Skip it and the session's work evaporates.
3. **Correction specificity.** "The voice is wrong" is less useful than "this sounds like a template — more casual, fewer hedge words." Specific corrections train the system.
4. **Quality gates.** Vibe checks (taste) + hard codes (structural). You need both. Vibe checks catch drift the system can't measure.
5. **Primitive selection.** Skills are expensive (context budget). Helpers are free. CLAUDE.md rules fire every turn. Use the right primitive for the right job.
6. **Research before execution.** Build context first. Read before writing. Plan before building.

**During onboarding:** Note which concepts the operator has encountered (check onboard log). "You've seen this" vs. "Coming up."

**Post-graduation:** Just the practices, organized for quick scanning.

---

## Audit

> "For a system health check, start a fresh session and run `/audit`. It checks onboarding graduation and system health."

Do not attempt to run `/audit` from within this session — it needs its own clean context.

---

## Design Notes

- This command is a **reference hub**, not a workflow. No multi-step process, no checkpoints, no file creation.
- The quick diagnostic must stay under 5 seconds. If it's slow, something is wrong with the file reads.
- During onboarding, every response should end with: "Run `/system` anytime." This command is the safety net.
- Post-graduation, this becomes the "how do I..." entry point.
