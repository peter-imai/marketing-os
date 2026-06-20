# /debrief — Meeting Debrief Skill

Process a meeting transcript into actionable intelligence through interactive discussion with the operator. The standard for all clients, all transcripts, without exception.

**Why this exists:** A solo agent processing a transcript produces adequate summaries but misses nuance. Five minutes of interactive processing while the conversation is still warm captures context, subtext, and operator judgment that no amount of post-hoc analysis can replicate.

**Invocation:** `/debrief` or `/debrief path/to/transcript.md`

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Read: `clients/*/meetings/transcripts/**` | Transcript access |
| Files | Write: `clients/*/meetings/**`, `clients/*/backlog.md`, `clients/*/core.md`, `clients/*/engagement-strategy.md`, `clients/*/marketing-strategy.md` | Update routing targets |
| Files | Write: `_system/backlog.md` | System-level backlog updates |
| MCP | `mcp__google-workspace__manage_task` | Route action items with external deadlines to Google Tasks |
| MCP | `mcp__google-workspace__list_task_lists` | Find operator's default task list |
No Bash commands, no network access, no subagents required.

---

## Subagent Strategy

All operations are sequential and interactive. No subagent strategy needed.

---

## Source Material

This skill produces internal intelligence and routing, not external-facing content. Convention 6 (Source Material Identification) does not apply.

---

## Steps

### Step 1: Intake

Accept the transcript. Three paths, one interface:

1. **File path as argument** — `/debrief clients/[client-name]/meetings/transcripts/2026-03-20.md`. Read the file.
2. **File path provided after invocation** — `/debrief` then operator provides a path. Read the file.
3. **Pasted text** — operator pastes transcript content directly into the conversation.

The skill's job starts when it has transcript text. How the transcript was acquired (Granola, Fireflies, Gemini Notes, manual copy) is not this skill's concern.

If a file path is provided, confirm the file exists before proceeding. If it doesn't exist, tell the operator and wait for a corrected path.

### Step 2: Context Detection

Determine which client this debrief is for. Try in order:

1. **Active client command** — if a client command was run earlier in this session, use that client. The strategy context is already loaded.
2. **File path inference** — if the transcript path is `clients/[name]/meetings/transcripts/...`, extract the client name.
3. **Transcript content** — scan the transcript for obvious client/company identifiers.
4. **Ask the operator** — if none of the above resolves it: "Which client is this meeting for?"

Once the client is identified, set the routing targets:
- **Client directory:** `clients/[client]/` (or `clients/[client]/engagements/[engagement]/` if applicable)
- **Backlog:** `[client-dir]/backlog.md`
- **Core:** `[client-dir]/core.md`
- **Strategy docs:** `[client-dir]/engagement-strategy.md`, `[client-dir]/marketing-strategy.md`
- **Meeting log:** `[client-dir]/meetings/log.md` (if it exists)

Not all routing targets will exist for every client (especially first run). That's fine — route to what exists, skip what doesn't, note what's missing.

### Step 3: Strategy Loading

If client strategy context **is not already loaded** in this session (i.e., no client command was run):

1. Check if `engagement-strategy.md` and `marketing-strategy.md` exist for this client.
2. If they exist, read and execute the procedure at `.claude/helpers.md#Load-Client-Strategy-Context` with the appropriate paths.
3. If they don't exist (new client, first run), proceed without. The debrief protocol works without strategy context — routing is less targeted, but signal analysis and update capture still function.

If strategy context **is already loaded**, skip this step entirely.

### Step 4: Preference Loading

Check if `[client-dir]/meetings/debrief-preferences.md` exists.

- **If it exists:** Read it. Apply the preferences to how you handle the remaining steps (emphasis areas, email behavior, special context to load, routing patterns).
- **If it doesn't exist:** Use defaults. Flag that this is a first run for this client — Step 10 will capture preferences after the debrief.

### Step 5: Signal Analysis

Read the full transcript. Not a skim — absorb the conversation dynamics.

Present 5-8 signal bullets to the operator. Each signal should have conviction: "The most important thing from this meeting is..." not "The meeting covered..."

Signal categories to look for:
- **Strategic shifts** — priorities changing, timeline moving, scope expanding/contracting
- **Decisions made** — what was agreed to, explicitly or implicitly
- **Relationship dynamics** — collaboration model changing, new stakeholders, energy shifts
- **Business context** — deals, revenue, team changes, external factors
- **Positioning signals** — how the client frames the product, naming choices, competitive references
- **Gaps or tensions** — what wasn't said, what was contradicted, what's unresolved
- **Commitments** — who promised what to whom, with or without deadlines

Take positions. "I think the biggest signal here is X because..." is better than a neutral list.

### Step 6: Operator Discussion

**This step is mandatory. Do not skip it.**

Ask: "What did I get right? What did I miss? What stood out to you sitting in that conversation?"

The operator was in the room. They heard tone, saw body language, felt the energy. Their read corrects yours. Wait for their input before proceeding.

After the operator responds, integrate their corrections and additions into your understanding. This combined read — your analysis plus the operator's lived experience — is the intelligence that drives the remaining steps.

### Step 7: Update Identification

Together with the operator, identify all updates across these categories:

**a. Backlog — new items.** Tasks surfaced by the conversation. Propose with priority. Operator approves before anything is added.

**b. Backlog — existing item updates.** Cross-reference the transcript against open backlog items. Flag: reprioritization, scope changes, blockers removed, new constraints, nuance additions. This is equally important as new items.

**c. Intelligence updates.** New information about people, preferences, concerns, dynamics, market context. What did we learn about the client, their customers, or their market?

**d. Strategy doc updates.** Anything that changes the engagement approach or marketing strategy. If a signal changes how we think about the relationship or the market approach, flag it.

**e. Growth hypotheses.** Market signals, new audiences, channel opportunities, activation ideas. Route to `growth-hypotheses.md` if one exists for this client.

**f. Action items.** Distinguish two types:
- *Internal work* (no hard external deadline) → backlog items (captured in a/b above)
- *External commitments* (deadline, promised to another human) → Google Tasks (Step 8 routes these)

**g. Structural gaps.** Things the meeting revealed that the system can't handle yet — important context with no natural home. Flag for system backlog.

Present all proposed updates to the operator. Wait for confirmation or corrections before executing.

### Step 8: Execution

Execute all confirmed updates:

1. **File updates** — backlog additions/modifications, intelligence updates, strategy doc updates, growth hypotheses, meeting log entry. Make the changes. Don't just list them.

2. **Google Tasks** — for action items with external deadlines, read and execute the procedure at `.claude/helpers.md#Route-Action-Items-To-Tasks`.

3. **Knowledge routing** — if reusable knowledge surfaced (marketing domain insight, practitioner convention, architecture pattern), read and execute the procedure at `.claude/helpers.md#Route-Knowledge-To-Destination`.

### Step 8b: Core.md Check

Check if `core.md` exists for the active scope (engagement, client, or system level).

**If it exists:** Read it. Compare against what this meeting revealed:
- Did the meeting surface a new concern or risk? → Suggest adding to Watches or Primary concern: "This meeting surfaced [X]. Should I add it to core.md?"
- Did the meeting resolve an existing concern? → Suggest replacing: "Core.md lists [concern] as the primary worry, but this meeting seemed to address it. Replace with [new concern], or remove?"
- Did the meeting shift what's happening or what success looks like? → Suggest updating Intention: "It sounds like the engagement has shifted from [X] to [Y]. Update core.md?"

**If it doesn't exist:** Note the gap in the summary. Don't create one — that's an operator action.

**Write protection:** Suggest changes, present them, wait for explicit approval. Never write to core.md without the operator saying yes.

### Step 9: Summary + Email Suggestion

**Summary:** Present what was changed and where. List every file updated, every backlog item added/modified, every Google Task created. The operator spot-checks — not a line-by-line review, a sanity check that important things landed in the right places.

**Email suggestion:** Check whether this meeting warrants client communication:
- If preferences exist (Step 4) and specify email behavior, follow them.
- If no preferences: use judgment. If the meeting produced commitments, deliverable handoffs, or open questions for the client, suggest: "This looks like it needs a follow-up email. Use `/compose` to draft it — it'll auto-select email format with recipients from this debrief."
- The email is a suggestion, not an automatic trigger. The operator invokes `/compose` separately if they want it.

### Step 10: Preference Capture (First Run Per Client)

**Only runs if no `debrief-preferences.md` exists for this client.** On subsequent runs, skip this step entirely.

After the debrief completes, propose defaults based on what you just observed:

> "First debrief for [client]. Here's what I'd default to for future runs based on what just happened:"

Propose recommendations across these dimensions:
- **Email follow-up:** Always suggest / skip unless asked / ask each time *(infer from whether this meeting warranted one)*
- **Emphasis:** Action items vs. strategic analysis vs. balanced *(infer from what the operator focused on in Step 6)*
- **Standard routing targets:** List the docs that were updated — propose those as the default routing set
- **Special context:** Any domain-specific docs that should load for this client's debriefs
- **Anything else the debrief revealed** about how this client's meetings should be processed

Ask: "Anything to change or add?"

On confirmation, write `[client-dir]/meetings/debrief-preferences.md`:

```yaml
---
client: [client name]
created: [session number]
last-updated: [session number]
---
```

Then the operator's confirmed preferences as prose bullets.

---

## Quality Gates

1. **Step 6 must happen.** The operator's read is mandatory. If the operator says "just process it" or "skip the discussion," push back once: "The interactive step is what makes debriefs valuable — 5 minutes of your read produces dramatically better intelligence than solo processing. Still want to skip?" If they insist, proceed, but note in the summary that the operator read was skipped.

2. **Updates require confirmation.** Never execute file updates without the operator confirming the proposed changes (Step 7). The operator's taste and judgment determine what gets captured.

3. **Existing items matter as much as new items.** The debrief should update the system's understanding of existing work, not just append new tasks. If you proposed only new items and no updates to existing ones, check yourself — conversations almost always add nuance to work already in progress.

4. **Signals, not summaries.** Step 5 produces your read on what matters, not a restatement of what happened. If your signal bullets could be generated by any summarization tool, they're too shallow.

---

## Done State

The debrief is complete when:
- [ ] Transcript has been fully read and analyzed
- [ ] Operator has provided their read (Step 6)
- [ ] All updates have been confirmed and executed
- [ ] Action items with deadlines have been routed to Google Tasks (if any)
- [ ] Core.md checked for concern updates (if it exists for this scope)
- [ ] Summary has been presented and operator has confirmed
- [ ] Preferences have been captured (first run) or loaded (subsequent runs)

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
