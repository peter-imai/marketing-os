---
step: 4
title: "Review — self-audit against voice rubric + correction capture"
next: 05-deliver.md
reads:
  - blueprints/criteria/voice.md
  - clients/[client]/measure/voice/index.md (if exists)
writes:
  - clients/[client]/measure/voice/index.md (score log entry)
  - clients/[client]/context/voice-kernel.md (if corrections warrant update)
  - Playbook file (if corrections warrant update)
---

# Step 4: Review

**Goal:** Score the draft against the voice rubric, report results, capture any operator corrections, and route corrections to their permanent homes. This step is both quality assurance (self-audit) and learning infrastructure (feedback loop).

---

## Rules

- **Every draft gets scored.** Not optional, not just for experiments. This is the system's quality telemetry.
- **Scores are logged persistently.** They go to `clients/[client]/measure/voice/index.md`. If this file doesn't exist, create it (see below).
- **Operator corrections are ground truth.** No graduation threshold. If the operator says the voice is wrong, that's a fact.
- **Route corrections immediately.** Don't defer to `/done`. The correction should improve the NEXT composition in this session.

---

## Instructions

### 1. Self-Audit

Read `blueprints/criteria/voice.md`. Score the draft against all 8 criteria (1-5 scale). For each criterion:

- State the score
- Cite the specific passage that earned it
- If below 4, state what would fix it

Present as a compact table:

```
| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C1 Consequence-first | 4 | Opens with "66% campaign-ready" — action clause before consequence |
| C2 Peer register | 4 | Peer throughout, one over-explanation in tier breakdown |
| ... | ... | ... |
| **Total** | **32** | |
```

### 2. Flag Actionable Gaps

For any criterion scoring below 4:

- Name the criterion
- State the specific weakness
- Propose the fix: "This is a [kernel / playbook / composition method] issue. Fix: [specific change]."

The operator decides whether to act on each gap now or defer.

### 3. Operator Review Gate

**MANDATORY.** The operator reviews the draft AND the scores. They may:

- **Accept the draft** — move to delivery
- **Request revisions** — specific changes. Make them, re-score the changed sections.
- **Override a score** — "That C2 is a 3, not a 4." Accept the override and update.
- **Correct the voice** — "This doesn't sound like me because [X]." This triggers correction capture.

### 4. Correction Capture

If the operator made corrections during the review (or during Step 3 composition):

**a. Identify the delta.** What did the operator change? What was the original? What's the pattern — is this a one-off fix or a recurring voice issue?

**b. Propose routing.** Each correction routes to its most useful destination:

| Correction Type | Routes To | Example |
|----------------|-----------|---------|
| Editorial judgment (register, posture, energy) | Voice kernel — Decision Rules or Editorial Posture | "Don't diagnose the reader's problems" |
| Structural pattern (section order, opening formula) | Format playbook | "Results before process in data writeups" |
| Language constraint (word/phrase ban) | Voice base — Language Constraints | "Never use 'optimize'" |
| Format convention (email greeting, sign-off, header style) | Format playbook | "Subject line: 'Call wrap - [date]'" |
| Quality standard (length discipline, specificity bar) | Voice rubric — criterion definition | "C8 needs explicit word budget" |

**c. Present the proposal.** "Based on your corrections, I'd update [destination] with [specific change]. Apply it?"

**d. Apply immediately.** On operator confirmation, edit the target file. No graduation threshold. The correction should be in place before the next `/compose` run.

**e. Log the correction.** In the operator review response, note: "Voice [kernel/playbook/rubric] updated with [N] corrections."

### 5. Log Scores

Add a row to the client's Score Trajectory at `clients/[client]/measure/voice/index.md`.

**If the file doesn't exist:** Create it with this header structure:

```markdown
# Voice Evaluation — Score Trajectory

**Rubric:** `blueprints/criteria/voice.md`
**Voice kernel:** `clients/[client]/context/voice-kernel.md`

---

## Score Trajectory

| Run | Date | Format | Config | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | Total | Notes |
|-----|------|--------|--------|----|----|----|----|----|----|----|----|-------|-------|
```

**Log entry format:**

| Run | Date | Format | Config | C1-C8 | Total | Notes |
|-----|------|--------|--------|-------|-------|-------|
| Sequential number | Today's date | email/doc/persuasive | What voice files were loaded | Per-criterion scores | Sum | Brief note — what was the piece, any corrections applied |

---

## Success Criteria

- [ ] All 8 criteria scored with per-criterion reasoning
- [ ] Gaps flagged with proposed fixes
- [ ] Operator reviewed draft and scores
- [ ] Any corrections captured and routed (if applicable)
- [ ] Scores logged to measurement file

---

## Next

Proceed to `05-deliver.md`.
