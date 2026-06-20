---
type: workflow
description: "A background agent that watches a source on a schedule, analyzes new material against a declared baseline, and drops findings into the backlog as operator-gated proposals."
status: operator-reviewed
created: 2026-04-11
last-updated: 2026-04-11
updated-by: joint
---

# Background Agent

The pattern for "how do you make the system iterate on itself, on a topic, or on a corpus, over time." Also called the agentic loop. Same five-step shape under every instance — what changes is the capture source and the baseline.

---

## Pattern

A background agent watches some part of the world on a schedule, reasons about what's new or drifting, and drops its findings into the backlog as a proposal — the operator decides what actually lands. The capture step is mechanical so the agent never has to remember to be invoked. The analysis step compares new material against a *declared* baseline — an existing ICP doc, the previous report, the current landing page, a pattern library — so the output is deltas, not summaries. The gating step is where the operator stays in the loop, and it's what separates a self-annealing system from a report-generation bot. What compounds: every pass sharpens the baseline that the next pass compares against. Foundational docs ratchet toward reality instead of rotting.

---

## The Loop

```
  Capture  →  Trigger  →  Analyze  →  Backlog  →  Operator
 (hook on    (time or   (deltas vs.  (item +      (gate
  source)     count       baseline)   report)      findings)
              threshold)
     ▲                                                │
     └────────────────────────────────────────────────┘
            baseline sharpens during operator review
```

### 1. Capture

A hook stores new material from the source on its own. Sales call transcripts, prompt history, YouTube transcripts from a channel you watch, Slack threads, whatever the source is. Source-specific. Mechanical. Never asks permission.

- **Input:** The source system (call recording API, prompt archive, video feed, export folder, webhook)
- **Output:** Files in a known capture folder (e.g., `_sources/`, `data/transcripts/`)
- **What it produces:** A growing pile of raw material, timestamped, readable by the analysis step

**Scaffolding:** A `SessionStart` hook or external cron. The capture should be cheap — it runs often, grabs new material, writes it down, exits. Don't put intelligence in the capture step; that's the analysis step's job.

### 2. Trigger

A threshold fires the analysis agent. The trigger is mechanical, not aspirational.

- **Input:** State from the last run (timestamp, item count) + current state (items since last run, time elapsed)
- **Output:** A decision — fire the analysis pipeline, or wait
- **What it produces:** A running analysis job when the threshold is met. Nothing otherwise.

**Four trigger mechanisms:**

| Mechanism | When to use | Example |
|---|---|---|
| **Time-based** | Steady-flow sources (daily calls, constant stream) | Every 7 days — cheap date check on `SessionStart`, fires once a week |
| **Count-based** | Bursty sources (occasional high-volume input) | Every 500 new items — measured against a state file |
| **Hybrid** | Volume unpredictable | Fire when EITHER 7 days elapsed OR 500 items accumulated |
| **Event-based** | Discrete high-value events | Fire when a new YouTube video drops, when a call finishes processing |

**Separation from capture is load-bearing.** Two separate hooks — capture runs cheap every session, trigger runs only when there's enough delta to be worth a full analysis pass. Folding them together makes the capture step expensive and the analysis step too frequent.

**Scaffolding:** A second `SessionStart` hook does the threshold check and, if met, spawns the analysis pipeline in the background using `claude -p --bare --model claude-opus-4-6 --allowedTools Read,Write --no-session-persistence`. The `--bare` flag prevents hook recursion. A lockfile (atomic `mkdir` on a `.analysis-lock` directory) prevents double-runs when two sessions start close together.

**Tuning.** Too aggressive = thin noise in every report. Too rare = overwhelming reports. The first couple of runs tell you what the right cadence is. Start longer and shorten if findings are too dense to review in one pass.

### 3. Analyze against a baseline

The analysis agent doesn't summarize the new material. It compares the new material against a declared prior — the existing ICP doc, the previous version of the corpus, the current landing page copy, whatever document represents the current state of the question. The comparison is what makes the output worth reading: here's what's new vs. what you already know.

- **Input:** The new material (since the last run) + a pointer to the declared baseline + an instruction to surface deltas, not summaries
- **Output:** A structured report — each finding has a category, a one-line description, evidence, and a proposed disposition
- **What it produces:** A report saved to a versioned location (`reports/R{n}.md`) so runs can be compared over time

**This is where you check the output and tune.** Tuning makes a big difference in two places: the *prompt* (V1 usually produces readable summaries instead of sharp deltas — that's the most common miss), and the *threshold* (too often = thin noise, too rare = overwhelming report). Plan for a couple of passes. The first review session tells you exactly what was missing.

### 4. Write findings as a backlog item

The pipeline appends a single backlog item that points at the report — title, link, "review and dispose." Not a direct edit to the foundational doc. A proposal sitting in the backlog, structured the same way every other task in the system is structured.

- **Input:** The analysis report from Step 3
- **Output:** A backlog item linked to the report
- **What it produces:** A visible, scannable proposal queue entry that surfaces in the next session start

**The backlog is the queue. The report is the artifact.** The split matters because the backlog stays scannable and the artifact is where the depth lives.

### 5. Operator gates application

Not code. A discipline. The operator opens the report inside a session, walks it finding by finding, decides what gets promoted into the foundational doc. The agent never mutates anything on its own.

- **Input:** The backlog item + the report
- **Output:** Updates to the baseline doc, new captures to other inboxes, items refined into actionable tasks — applied manually, one finding at a time
- **What it produces:** A sharper baseline for the next pass, plus whatever promotions (content ideas, curriculum entries, copy revisions) the operator pulled out of the findings

**This is where the loop earns its keep.** Skip this step and you have a report-generation bot, not a self-annealing system.

### Why the gating step matters more than the analysis step

If you let the agent push directly to the doc, two things break: (a) you stop learning, because the epiphanies happen during the *interaction*, not during the read; (b) the foundational doc starts drifting on autopilot and nobody notices when it goes wrong. The split between "do the work autonomously" and "apply the work manually" is the whole game. It's what makes the loop safe at team scale, and it's what makes the operator level up instead of decay.

### Why this actually closes the self-annealing loop

Self-annealing has been the theoretical promise of every AI-second-brain pitch for three years and it has mostly been bullshit. The thing that breaks it in practice is that the system has nowhere to land its findings — they evaporate in chat history. This pattern lands them in the same place every other piece of work lands (the backlog), in the same shape every other task has, gated by the same review move the operator already does. The compounding works because the mechanism is the same one already trusted.

---

## What It Unlocks

Five things that weren't possible before — not because the models couldn't do them, but because there was no place for the findings to land.

- **Foundational docs ratchet toward reality instead of rotting.** ICP, positioning, messaging — usually these drift away from what customers actually say the moment you ship them. With the loop, the gap between "what you thought your customer wanted" and "what they said on Tuesday's call" closes every week. Mechanically, with the operator's hand on the review step. The doc gets *sharper*, not just longer.

- **Your words come from real conversations, not imagined ones.** Landing page copy, cold email hooks, objection handlers — all of it can be pulled from transcripts where a prospect used that exact phrase. Writing becomes a promotion step, not a generation step.

- **Insight stops evaporating into chat history.** Every flash of understanding on a call, every time you figured out how to frame something live, every tricky articulation that happened on the fly — normally these evaporate the moment the call ends. The loop captures them and hands them back during the review session, where you decide which ones to lock in.

- **Operator behavior becomes coachable.** You can audit how you're actually operating — on calls, inside the tool, in the work — against what best practices look like on paper. The gap between "declared workflow" and "actual workflow" becomes visible. For solo operators that's interesting. For teams it's the whole game.

- **Content gets generated as a byproduct of work, not a tax on it.** Right now, making content means pausing the work to sit down and write. The loop flips this: the work itself is the source material, the agent surfaces what's content-worthy, and the operator just decides what to publish. The hardest thing to articulate about using these tools — the moment-to-moment nuances — is exactly what this pattern surfaces automatically.

The common thread: all five are versions of "the system is now paying attention to you, continuously, and bringing you findings at the moments you're ready to act on them." That's the capability that wasn't possible before — not because the models couldn't do it, but because there was no place for the findings to land.

---

## Where to Point It

Same shape every time. What changes is the capture source and the baseline.

| # | Capture source | Baseline | Threshold | What the agent surfaces |
|---|---|---|---|---|
| 1 | Sales call transcripts | Current ICP doc + objection-handling notes | Every 3 calls, or weekly | New prospect language missing from ICP, objections not matching current handlers, repeated jobs-to-be-done framings. The ICP doc gets *sharper*, not just longer. |
| 2 | Sales call transcripts | Current landing page copy + cold email sequences | Weekly | Where prospects' actual language diverges from the current messaging. The highest-leverage variant — copy comes out of real conversations instead of imagined ones. |
| 3 | YouTube channel transcripts | Current marketing knowledge doc | Per new video, or weekly batch | New framings, new tactics, new structural moves. Over months: a queryable, deduplicated, opinionated library instead of a folder of bookmarked videos. |
| 4 | Own Claude Code prompt history | Existing principles doc + content idea inbox | Every 7 days, or N prompts | Three passes — conceptual moves for the principles doc, teaching moments for the curriculum, and moments that would make content. The third pass is the sleeper — the way you actually use the tool is exactly the material that's hardest to articulate from the outside. |
| 5 | Teammate session log | Declared best-practices doc | Weekly | Gaps — "skill X not invoked where it would have helped, prompts skipping the planning step, agent executing without gating." Output is a coaching report filed to their backlog, not a finger wag. The highest-leverage variant for team-scale deployment. |

Each gets at a different leverage axis: foundational doc evolution, tactical messaging, external learning, self-observation for content, and team coaching. Pick one and the rest follow the same recipe.

---

## Non-Negotiables

- **Operator gates application.** No autonomous mutation. Ever. Even when the finding seems obvious. The cost of one bad auto-edit to a foundational doc is higher than the cost of one extra review pass.
- **Compare against a declared baseline, not against nothing.** Summaries of new material are noise. Deltas against an existing document are signal. The baseline is what makes the agent's output worth reading.
- **Land findings in the same shape as everything else.** Backlog item, structured artifact, frontmatter, the whole thing. If the loop's output lives in a parallel weird format, it doesn't compound.

---

## Pitfalls

- **Threshold too aggressive.** Running the analysis on every new input is noise. Wait until there's enough delta to be worth a review pass.
- **Baseline that drifts silently.** If the baseline doc isn't itself maintained, the agent's deltas become meaningless. The review pass is what keeps the baseline honest.
- **Letting the agent write to the foundational doc directly.** Will feel efficient. Will rot the doc within a month.
- **Pretty summaries instead of sharp deltas.** V1 analysis prompts almost always produce readable prose instead of deltas-against-baseline. Tune the prompt on the first run.
- **Skipping the review session.** Without the review move, this is a report generator, not a self-annealing system.

---

## Economics

Per-instance, approximate.

| Dimension | Cost |
|---|---|
| Build cost (one-time) | ~4-8 hours for a first instance — capture hook + trigger hook + analysis prompt + backlog write-back. Most of the time goes into the analysis prompt (tuning it from "summary" to "delta"). |
| Analysis run (automated) | ~10-15 min of Opus sub-agent time per window. Runs in background, no blocking. |
| Operator review (manual) | ~20-30 min per round to walk findings, react, and apply promotions. Non-negotiable — this is the gating step. |
| Weekly operator cost per instance | ~20-30 min/week (assuming weekly cadence). ~2 hours/month. |
| Weekly model cost per instance | ~$0.50-$2.00 (Opus analysis run, depending on window size) |

**Unit economics of the loop.** Each round costs ~50 min total (~20 automated + ~30 operator). It produces: baseline doc updates that get sharper with every pass, 2-5 promotable findings per run, and occasionally a new pattern or convention worth locking in.

**Break-even signal.** If a round produces zero findings and zero baseline updates, the cadence is too frequent or the corpus window is too small. Stretch the cadence. If every round produces an overwhelming wall of findings, the cadence is too rare. Tighten.

---

## Before You Build

Two things have to exist before the build starts. Neither is optional.

- **A single folder where source files land.** Whatever the capture source is — call transcripts, prompt history, YouTube transcripts, Slack exports — the simplest version is: point the hook at one folder where new files arrive, and let the hook read whatever's new since the last run. Don't build complicated ingest plumbing. One folder, one hook, one read path.
- **A baseline doc in a shape the agent can actually compare against.** The foundational doc (ICP, positioning, pattern library, whatever is being updated) needs to be *structured* — sections per dimension, not one paragraph of prose — or the deltas come back lossy. If the baseline is weak, the findings will be weak no matter how good the analysis prompt is. Fix the baseline first.

---

## Where to Start

Pick the use case with the *clearest baseline doc already*. If there's a current articulation of the ICP somewhere and sales calls are a steady-flow input, that's the lowest-friction first instance — everything needed (capture source, baseline doc, review cadence) already exists in the workflow. Build that one. Once it's running, the same pattern points at the next thing for free. That's the compounding side.
