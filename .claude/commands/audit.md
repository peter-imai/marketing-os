System health audit — diagnostic report on how well the system is holding together.

This is a diagnostic — you report findings, you don't fix them. The operator reviews the report and decides what to act on.

---

## Step 0: Graduation Check

Read `_system/onboard-log.md`.

**If the file doesn't exist or status is `graduated`:** Skip to Step 1.

**If status is `in-progress`:**

Check all core concepts (1-3) in the onboard log table:

| # | Concept | What to verify |
|---|---------|---------------|
| 1 | The loop | Multiple `/done` runs across multiple sessions (check session log) |
| 2 | How to work | Operator has interacted with the backlog in 2+ sessions |
| 3 | Quality gates | Operator has corrected or edited system output |

For each concept, check the onboard log: is it both **introduced** AND **reinforced**?

### If all core concepts are introduced + reinforced:

Present the evidence from the onboard log milestones:

> "You've covered the core concepts:
> 1. **The loop** — [evidence from milestones]
> 2. **How to work** — [evidence]
> 3. **Quality gates** — [evidence]
>
> Ready to graduate? This transitions you from onboarding to maintenance mode. The system keeps working the same way — you just stop getting teaching moments at shutdown."

**On operator confirmation:**

1. Update `_system/onboard-log.md`:
   - Set `**Status:**` to `graduated`
   - Set `**Graduated:**` to `Session [N], [today's date]`
2. Add milestone: `- [Session N] Graduated via /audit`
3. Confirm: "Graduated. `/done` onboarding step is now inactive. Run `/system` anytime for a quick diagnostic."

### If core concepts are not complete:

List which concepts are missing introduction or reinforcement.

> "Not quite ready — [concept name(s)] haven't been fully covered yet. Keep using the system normally and `/done` will continue teaching at shutdown. Run `/audit` again when you think you're ready."

**Then continue to the diagnostic** — it runs regardless of onboarding status.

---

## Step 1: Load Reference Standards

Read these files. They are the standards you check against.

- `_system/marketing-principles.md`
- CLAUDE.md (already loaded — review the Workflow Practices and Core Principles sections)

Hold these in mind for all subsequent checks.

## Step 2: Run Diagnostics

For each area below, read the specified files, run the specified checks, and record findings.

Tag each finding:
- **Compliant** — meets the standard
- **Drifted** — was compliant, has degraded or partially fails
- **Gap** — standard exists but was never met

---

### Area 1: CLAUDE.md Health

**Read:** `CLAUDE.md`

**Check:**
- **Growth:** Has CLAUDE.md grown since install? Count sections and routing table entries. Flag if routing table has entries that don't correspond to actual commands/skills, or if new sections have been added that belong in a command instead.
- **Universality:** Does every section serve ALL sessions, not just specific activities? Activity-specific instructions belong in commands, not CLAUDE.md.
- **Routing coverage:** Does the routing table cover the main entry points? (architect, done, system, audit, client commands, compose, debrief, llm-research). Are there commands or skills missing from the table?
- **Primitive Selection table:** Is it present? Does it accurately reflect the current primitives in the system?
- **Accumulated cruft:** Are there routing rules or workflow practices that were added but aren't actually being followed or enforced?

---

### Area 2: `/done` Prescription Compliance

**Read:** `.claude/commands/done.md`

**Check each maintenance step:** Is it prescriptive ("update X in file Y with Z") or descriptive ("X should stay current")?

For each step:
1. Quote the instruction
2. Classify: prescriptive or descriptive
3. If descriptive, note what a prescriptive version would say

The standard: every step must tell a literal assistant exactly what to do, what file to write to, and what content to produce.

---

### Area 3: Blueprint Currency

**Read:** Every file in `blueprints/`

**For each blueprint, check:** Does it reference files, conventions, folder structures, or commands that still exist and work as described? The blueprints shipped with the kit — the risk isn't that they're poorly written, it's that the system has evolved and the blueprints haven't kept up.

Flag any broken reference (file path that doesn't exist, convention that's changed, command that's been renamed).

---

### Area 4: System Architecture Currency

**Read:** `_system/system-architecture.md`

**Check in both directions:**
1. **Listed but missing:** For each entry in the Component Inventory and Folder Structure, verify the file exists. Flag entries pointing to files that don't exist.
2. **Existing but unlisted:** Glob for significant files in key directories (`blueprints/`, `_system/`, `.claude/commands/`, `.claude/skills/`, `resources/`) and flag any that are missing from the inventory.
3. **Conventions table:** Is each convention still accurate? Does the enforcement mechanism match reality?

---

### Area 5: Backlog Hygiene

**Read:** `_system/backlog.md`

**Check:**
- Items marked `blocked` where the blocker is resolved or done — flag for unblocking
- Items marked `ready` with unresolved dependencies — flag the inconsistency
- Items with no activity across many sessions — should they be parked or cut?
- Done items still in the active table that should be in the Done section
- Priority labels that no longer reflect reality
- Backlog size: is it growing out of control or well-managed?

**Also check:** The workspace operating backlog(s) — the root `backlog.md` (single-company) and any `projects/[name]/backlog.md` (multi-workspace). Run the same checks on each.

---

### Area 6: Workspace Docs — Identity + Now-State

The kit's base is a two-doc split (`_system/client-folder-convention.md`): `core.md` = durable identity, `operating-lens.md` = current state + watches. Check both, per workspace.

**Find the workspaces:** the root (single-company setup) and each `projects/[name]/` that has a corresponding `/[name]` command.

**For each workspace:**

1. **`core.md` exists** and reads as identity (who we are / who we serve / how we create value / what we do) — not a state dump. It's slow-changing; no tight line cap, but flag it if it has accreted session-by-session churn that belongs in `operating-lens.md`.
2. **`operating-lens.md` exists** and reads as current state (what's happening now, active direction, watches). This is the volatile doc — it's where caps and re-bloat checks apply (see Area 10).
3. **Both are read at startup** by the workspace's command (root → `/start` Orient Mode; `projects/[name]/` → `/[name]`).

**The standard:** identity and state live in separate docs so the foundation stays clean and the now-state stays current. A workspace missing `operating-lens.md`, or with state jammed into `core.md`, is the drift this area catches.

---

### Area 7: Marketing Principles Adherence

**Read:** `_system/marketing-principles.md` (already loaded in Step 1 — review principle by principle)

**For each principle, follow this procedure:**
1. **Extract the test.** Find the principle's stated test, corollary, anti-pattern, or closing evaluative question. If it has one, copy it verbatim. If not, derive the simplest binary test from the principle's core claim.
2. **Select a target.** Identify 1-2 concrete artifacts, files, or system behaviors where that test applies. Choose things you've already read in Areas 1-6 where possible.
3. **Apply the test literally.** Don't interpret generously. Read the test as a strict auditor would. Does the artifact pass or fail?
4. **Record the finding** with the test you applied, the artifact you checked, and the evidence for your verdict.

**If a principle has no stated test and no testable criterion can be derived:** flag that as a finding itself. A principle you can't check is a principle you can't enforce.

**Do not skip principles because they seem obviously met.** Apply the test anyway. Assumed compliance is how drift starts.

---

### Area 8: Memory Currency

**Find and read** the memory index file. It lives at `~/.claude/projects/` under a path derived from this project's directory. Look for `MEMORY.md` in the memory folder.

**Check:**
- **Accuracy:** Is the information accurate to current system state? Cross-reference any file paths, convention names, or tool references against what actually exists.
- **Staleness:** Is anything referencing things that have been removed, renamed, or superseded?
- **Misrouted content:** Does it contain items that belong in proper homes instead? Conventions belong in `_system/decisions/` or `_system/system-architecture.md`. Methods belong in `blueprints/`. Tasks belong in backlogs. Only operational state (who the operator is, how they prefer to work, external references) belongs in memory.

---

### Area 9: Context Loading Order

**Read:** All files in `.claude/commands/`

**For each command that loads context files at startup:**
1. List the files loaded and their order
2. Check: does the order follow identity (`core.md`) → current state (`operating-lens.md`) → activity context (on demand)?
3. Flag any command that loads heavy context before establishing identity/framing
4. Flag any command that loads context outside its scope

---

### Area 10: Context Budget

**Read:** All files in `.claude/commands/`

**For each command that loads files at startup (Read directives in startup/orientation steps):**

1. List every file the command reads at startup (not on-demand/reference reads)
2. Measure each file's approximate token cost: character count / 4 (label as approximate)
3. Add CLAUDE.md + skill descriptions (~2% of context window) as baseline auto-loaded cost
4. Sum the total startup context load for that command

**Check against budgets:**
- **Per-command startup reads:** Flag any command exceeding ~10K tokens (~650 lines combined)
- **Individual file growth:** Flag `_system/backlog.md` > 200 lines, `_system/system-architecture.md` > 450 lines, `operating-lens.md` > 40 lines (the now-state doc is the re-bloat risk — `core.md` identity is slow-changing and not capped the same way)
- **Skill count:** Count skills in `.claude/skills/`. For each, check whether `disable-model-invocation: true` is set. Flag skills that load at startup but are only invoked manually — these waste description budget
- **Backlog Done section:** Count entries. Flag if > 20 (should be rotated)

**Why this matters:** Context budget degrades silently. A command that loaded 8K tokens at install might load 20K after a few months of growth. The system gets slower, reasoning gets worse, and nothing warns you. This check catches it.

**Mechanical cap + register check.** Run the checker — it reads the `cap-lines` frontmatter on auto-loaded files, sums the aggregate token budget (~10K target), and scans for hedging language and session-stamp narrative that signals re-bloat:

```bash
python3 tools/hygiene/check-state-caps.py
```

The same script runs at SessionStart via `cadence-check.sh` and reports only when something is over budget. **If you keep a `backlog-index.md`:** confirm it is a status digest (open tasks, priorities, counters) — NOT a running session journal. A `Last synced: S{n}` paragraph accreting each session is the re-bloat failure mode where the index that should save context starts costing it.

---

### Area 11: System Coherence

This area runs AFTER areas 1-10. You've now read the system. Step back and assess it as a whole.

**Answer each of these questions. Ground every claim in specific findings from areas 1-10.**

1. **Tensions:** Are any principles in tension with each other in practice? Are any findings pulling in opposite directions? Name the tension and which side the system is currently favoring.

2. **Investment balance:** Where is the system over-built relative to actual use? Where is it under-built? Check: how many blueprints have been used in real work vs. created and never triggered?

3. **Pattern clustering:** Do your findings cluster around a theme? If 3+ areas show drift in the same direction, name the pattern.

4. **Dead weight:** Are there artifacts, conventions, or capabilities that exist but have never been used in real work? For each, state whether it should be pruned or is waiting for a concrete trigger.

5. **Highest-risk gap:** State the single most important thing this system is getting wrong right now. This is not a compliment opportunity — if you can't identify one, you haven't looked hard enough.

---

## Step 3: Write Report

Write all findings to `_system/system-health.md`. Overwrite any previous report.

**Structure the report as follows:**

- **Header:** "System Health Report" with run date and a 1-2 sentence headline summary
- **Graduation status:** Current onboarding status (or "Graduated, Session N")
- **Areas 1-10:** Each area gets a heading, a status tag (compliant / drifted / gap), and the findings
- **Area 11:** System Coherence — the five meta-assessment answers
- **Proposed Actions table:** At the end, a table with columns: #, Finding (what's wrong), Proposed Task (what to do), Priority (P1/P2/P3)

**Do NOT write proposed tasks to the backlog.** The audit is non-destructive. The operator reviews the report and decides what gets added.

## Step 4: Present Summary

After writing the report, present the operator with:
1. The headline (1-2 sentences)
2. Count of findings per status (compliant / drifted / gap)
3. The Area 11 highest-risk gap
4. The proposed actions table

The operator decides next steps.
