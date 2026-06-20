Ending this Marketing OS session.

**Context will be cleared after this runs. Everything that matters must be written to files.**

---

## Artifact Routing Rules

Before executing updates, classify everything that surfaced this session. Each item has ONE correct home:

| What Surfaced | Where It Goes | NOT Here |
|---------------|---------------|----------|
| **Design decision** (we chose X over Y) | Decision doc (`_system/decisions/`) | Memory |
| **Convention** (how to name/structure things) | Decision doc or system docs | Memory |
| **Task** (something that needs doing) | Backlog (system or client) | — |
| **System gap** (system couldn't handle X) | Backlog as a task (or explicitly parked) | — |
| **Method** (how to do a recurring thing) | Blueprint (`blueprints/`) | Memory |
| **Operational activity with a loop** (recurring multi-step process) | Workflow (`blueprints/workflows/`) — required sections: Pattern, Loop, Economics | Blueprint (workflows are more specific) |
| **Learning about client** | Strategy docs or context files | Memory |
| **Learning about how to operate the system** | Memory (if truly operational) | — |
| **Marketing domain knowledge** (tool, technique, insight, methodology) | Marketing expertise index (`resources/marketing/`) | Memory |

**Key rules:**
- Memory is for **operational knowledge** that helps the agent work. Not for conventions, methods, or client details — those have proper homes.
- System gaps must become **backlog tasks** — don't just note them.
- If you're unsure, ask: "Will anyone act on this based on where I'm putting it?" If no, it's in the wrong place.

---

## 1. Reflect

Briefly state what the session's goal was, what was accomplished, and what didn't get done.

Then identify **one** practitioner insight — a convention that was applied, a pattern that emerged, or a tool behavior worth understanding. State it in one sentence, then name the principle behind it. Format:

> **Insight:** [One sentence describing what was learned about how we build.]
> **Principle:** [The convention or architecture principle it connects to.]

Examples:
- **Insight:** Subagents reading decision docs kept the main context clean for synthesis work. **Principle:** Protect the main context window — fill it with what you're working ON, not what you needed to look up.
- **Insight:** Loading strategy docs first gave them outsized influence on activity context loading. **Principle:** Load order is a design variable.

This gets included in the git commit message (Step 6) so it accumulates in version history.

If nothing genuinely new surfaced this session, say so — don't force it.

## 2. Capture Decisions

For each decision made this session:
- If not already logged, log to `_system/decisions/YYYY-MM-DD-NNN-[topic].md`
- Use the standard format: Decision, Rationale, Alternatives Considered, What Would Make Us Revisit
- **Revisit trigger wiring:** If any revisit trigger is time-based or threshold-based, add a corresponding entry to the backlog. Prose-only triggers are unmonitored; wired triggers get caught.

## 3. Route Everything That Surfaced

Walk through the artifact routing table above. For each item that surfaced (decisions, conventions, tasks, gaps, methods, client learnings, operational learnings), apply the routing rules and write it to the correct destination.

For knowledge routing, reference `.claude/helpers.md#Route-Knowledge-To-Destination`. For new backlog items, follow `.claude/helpers.md#Capture-Backlog-Item`.

Specifically check:
- **Unresolved questions** → Add to backlog as a task, or to the relevant design doc. Do NOT leave them only in conversation.
- **Methods discovered or refined** → Create or update the relevant blueprint in `blueprints/`.
- **Workflow tribal knowledge** → Did this session involve a recurring multi-step operational activity? Check `blueprints/workflows/` for an existing doc. If one exists, route tribal knowledge (gotchas, timing, costs, edge cases) there. If none exists and this activity has been done before, propose creating one.
- **Marketing knowledge** → Did this session produce marketing knowledge that applies beyond one client? Update `resources/marketing/index.md` — the relevant domain entry.
- **Engagement playbook patterns** → Did this session produce engagement work that would be done again for the next client? Capture observations.
- **New system artifacts** → Wire new artifacts: name their read mechanism + update mechanism. Update startup sequences of affected commands. Unwired components don't exist to the system.
- **System failures** → Did the system violate its own principles this session? Log what happened, which principle was violated, what should have prevented it, and what was done.

## 3b. Content Idea Capture

**Check:** Did content ideas surface this session — a topic worth a video, a client moment worth capturing, a competitive angle, a trending concept?

If something surfaced, capture it. Format:
```
- [YYYY-MM-DD] Idea description. Where it surfaced. (Source: client session / conversation / etc.)
```

If nothing surfaced, move on. Don't manufacture ideas.

## 3c. Messaging Candidates Capture

**Check:** Did sharp positioning or messaging language surface this session? A vivid metaphor, a reframe that landed, a line the operator said that stopped the conversation.

If yes, capture it with the context of what it addresses and where it came from.

If nothing sharp surfaced, move on. Don't manufacture candidates.

## 3d. Tool Learning Capture

**Scope:** Sessions that used tools (API clients, SaaS platforms, processing scripts) or made tool selection decisions. Skip for sessions that didn't interact with tooling.

**Check:** Did this session reveal something real about a tool? A capability confirmed or denied, a cost number, a gotcha, a performance characteristic, a comparison.

If yes, route the learning:
- **Selection-relevant** (when to use, cost changes, comparison evidence) → update `tools/index.md`
- **Operational depth** (throughput numbers, failure modes, gotchas, quality data) → update `tools/[name]/profile.md`

If a tool has no `profile.md` yet, create one. Capture operational knowledge from real usage only.

## 3e. Quality Experiment Check

**Scope:** Sessions that invoked a deliverable-producing skill (`/compose`, `/debrief`, `/llm-research`).

**Check `_system/quality-engine-map.md`** (if it exists) for the skill(s) used this session:

1. **Was a "Ready to Try" experiment active?** Log your observation: what the experiment was and what you observed. The operator decides: keep / modify / drop.
2. **Did the operator correct output quality?** Capture what was wrong and what criterion would have caught it.

If no skill was used or no quality signal surfaced, move on.

## 3f. Onboarding Check

**Gate:** Read `_system/onboard-log.md`. If the file doesn't exist or status is `graduated`, skip this step entirely.

**If status is `in-progress`:**

This step teaches one concept per shutdown — never more. Your job is to name what they just experienced, not lecture.

### Trigger Detection

Two-phase check. **Phase 1:** Find the first un-introduced concept whose first exposure trigger fired. **Phase 2:** If none, find the first un-reinforced concept whose reinforcement trigger fired. One concept max.

| # | Concept | First Exposure Trigger | Reinforcement Trigger |
|---|---------|----------------------|----------------------|
| 1 | The loop | This is a `/done` run | Session count ≥ 2 |
| 2 | How to work | Operator captured/referenced a backlog item | Backlog interaction in 2+ sessions |
| 3 | Quality gates | Operator corrected system output | Session count ≥ 5 |
| 4 | Cross-loop compounding | 2+ client directories exist with context | Intelligence flowed between capabilities |
| 5 | System hygiene | Session count ≥ 8 | First `/audit` run |

**Fallback:** If core concepts (1-3) haven't been introduced by session ~5, deliver with general framing.

### Teaching

Compose a brief message (30-60 seconds) that names the concept, connects to this session's work, explains why it matters, and points to `/system`.

### Update the Onboard Log

Mark concepts as Introduced/Reinforced. Check graduation readiness (core concepts 1-3 both introduced AND reinforced → nudge toward `/audit`).

Hold the teaching message — deliver it in the wrap-up (Step 7).

---

## 4. Execute Updates

### Always (every session type):

- **Update system backlog:** Add new items, update statuses. `_system/backlog.md`. Detailed design notes → `_system/task-notes.md`.
- **Backlog maintenance:** Mark completed cluster tasks `[x]` with date. If all tasks in a cluster are done, move cluster to Done section. Move done standalone tasks to Done section. Unblock items whose blockers are done. **Done section rotation:** Keep 20 most recent, clear older.
- **Cross-reference update:** For each task completed, check whether other items reference it (by ID, as blocker, or dependency). Update their status. Note next sequenced step in active cluster — surfaces in wrap-up.
- **File growth check:** Flag if exceeded: `_system/backlog.md` > 200 lines, `_system/system-philosophy.md` > 450 lines, any strategy doc > 100 lines. Trim before committing.
- **Update client backlog (if operating session):** Mark completed tasks, update statuses, add new items. Move completed to Done table with date.

### Architecture sessions additionally:

- **Update system architecture:** If the architecture narrative doc is present (`_system/system-philosophy.md`), update it — component inventory, folder tree, conventions. If concepts/principles changed, update narrative sections.

### Operating sessions additionally:

- **Update frontmatter on Tier 1 docs:** For strategy docs you *meaningfully updated*, set `last-updated` and `updated-by`. Do NOT update frontmatter on docs you only read.
- **Consider core.md updates:** Did active direction shift? Are watches still current? Did new documents become important enough to add to Core Documents?
- **Update data state (if data work):** If the session involved data work, update the relevant `data-state.md`.
- **Update contact registry (if people work):** If meeting debriefs or emails revealed new contacts, add to `contacts.yaml`.

## 4b. Coherency Agent

Runs every `/done`. No gate — state coherency matters even when no task was completed.

**Mechanism:** Spawn a subagent with this job:

**Input:**
1. The active scope's `core.md` (if it exists — skip Lens 1 if no core.md).
2. The Step 1 reflection (what happened this session).
3. `git diff --name-only` output (what files changed).
4. The active backlog.

**Lens 1 — State Coherency** (requires `core.md`):
- For each file listed in Core Documents: was it touched, or should it have been? Flag staleness.
- **Reverse governance check:** For files modified this session that have `governance: core-ref` in frontmatter, verify they appear in core.md's Core Documents. Flag any doc that declares itself core-ref but isn't listed.
- Does the Intention still match reality?
- Did any Watch trigger?
- Is `core.md` over 30 lines? Flag as structural issue.

**Lens 2 — Direction Coherency** (the bulletproof backlog):
- Scan ALL remaining tasks:
  - **Staleness:** Description references state that no longer exists
  - **Redundancy:** Session work already accomplished what a remaining task describes
  - **Sequence:** Within clusters, is the order still right?
  - **Cross-references:** Any task mentioning a completed task — does the reference still make sense?
  - **Alignment:** Do remaining tasks still serve the declared Active Direction? (Skip if no core.md.)

**Output** — "Coherent." or Flags + recommendations:

| Flag type | What it produces | What happens next |
|-----------|-----------------|-------------------|
| **Backlog fix** | Crisp one-liner per fix. Numbered list. | Surfaces in wrap-up. Operator approves. |
| **State flag** | Informational one-liner. | Surfaces in wrap-up. Operator decides. |
| **Watch trigger** | One-liner with evidence. | Awareness only. |
| **core.md suggestion** | Question, never auto-applied. | Operator answers. Agent updates only on yes. |

**Rules:** Err toward flagging. Never modify backlog or core.md without explicit operator approval.

## 4c. Doc Log Entries

Read and execute the procedure at `.claude/helpers.md#Check-For-Doc-Logs` with:
- **Touched files list:** `git diff --name-only` output
- **Session number:** current session
- **Trigger source:** `session`

The helper handles detection, drafting, and approval. In the wrap-up, reflect any applied entries in the routed section.

## 5. Update Session Log

Append one line to `_system/session-log.md`:

Format: `| YYYY-MM-DD | Session NNN | command-type | one-line summary |`

**Do not skip this step.** The cadence hook depends on it.

## 6. Commit

After all file updates are complete:
1. `git add` the files that were created or modified
2. `git commit` with format:
```
Session N: [What was accomplished]

[2-3 lines of detail if needed]

Practitioner insight: [The one-sentence insight from Step 1, if one was identified]
```

## 7. Wrap Up

All work is done. Deliver one summary using this format:

```
================================================================
SESSION {N} · {COMMAND} · COMPLETE
================================================================

  {Plain language summary — what we did and what it produced.
   2-4 lines. Concrete nouns, no filler.}

─── routed ────────────────────────────────
  {What → destination}
  {What → destination}

─── observations ──────────────────────────
  {Quality experiment results, corrections, anything the operator should know}

─── coherency ─────────────────────────────
  {Proposals — numbered, one-liner each}
  Should I apply these? Yes / no / yes except N?

  {Informational flags — state staleness, watch triggers. No prompt needed.}

─── logical next steps ────────────────────
  {Cluster sequence: next task in the active cluster}
  {Unblocked tasks}

─── onboarding ────────────────────────────
  {Teaching moment from Step 3f}

────────────────────────────────────────────
  /exit
```

**Rules:**
- **Skip sections with nothing to report.** Only include sections with content.
- The arrow IS the explanation. No filler about routing taxonomy.
- Coherency can have both proposals (with yes/no prompt) and informational flags. Proposals first.
- Logical next steps only appears when there's signal (cluster sequence or unblocked tasks).
- `/exit` is always the last thing they see.
