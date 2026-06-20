---
name: market-research
description: "Multi-phase market research: ICP, market context, competitive landscape, buyer personas, and strategic synthesis. Run at engagement start to build the research foundation."
disable-model-invocation: true
---

# Market Research

Multi-phase market research workflow. Builds deep understanding of a client's market, buyers, competitors, and targeting opportunities. Each phase builds on the last. Teaching checkpoints between phases ensure the operator learns and reacts before the next phase runs.

**Input:** A client to research. The operator must know enough about the client to answer the Phase 0 interview.
**Output:** `market-research.md` (primary synthesis) plus detailed deliverables (`icp.md`, `competitive-landscape.md`, `buyer-personas.md`) in the client's context directory.

**References:**
- [phases/00-engagement-brief.md](phases/00-engagement-brief.md) — Phase 0 interview framework
- [phases/01-icp-research.md](phases/01-icp-research.md) — Phase 1 subagent prompt
- [phases/02-market-context.md](phases/02-market-context.md) — Phase 2 subagent prompt
- [phases/03-competitive-landscape.md](phases/03-competitive-landscape.md) — Phase 3 hybrid guide
- [phases/04-buyer-personas.md](phases/04-buyer-personas.md) — Phase 4 subagent prompt
- [phases/05-customer-evidence.md](phases/05-customer-evidence.md) — Phase 5 subagent prompt (optional)
- [phases/06-niche-data-sources.md](phases/06-niche-data-sources.md) — Phase 6 subagent prompt (optional)
- [templates/synthesis-template.md](templates/synthesis-template.md) — Phase 4.5 output structure
- [templates/output-convention.md](templates/output-convention.md) — File placement and naming

---

## Step 0: Setup

1. Read [templates/output-convention.md](templates/output-convention.md).
2. Determine the client context directory:
   - Check if `clients/[name]/engagements/` exists. If yes, ask the operator which engagement.
   - Otherwise use `clients/[name]/context/`.
   - If the client directory doesn't exist, create it.
3. Create `_inputs/research/` inside the context directory.
4. Confirm with the operator: "Starting market research for [client]. Output goes to [path]. Ready to begin with the engagement brief?"

**Wait for operator confirmation before proceeding.**

---

## Step 1: Phase 0 — Engagement Brief

Read [phases/00-engagement-brief.md](phases/00-engagement-brief.md).

Conduct the interview in main context. Use the framework conversationally — follow threads, skip what the operator can't answer, probe where answers are interesting. If the operator has intake from the client team, read it first and use the interview to fill gaps.

After the interview, synthesize into the format specified in the phase file. Write to `[context-dir]/_inputs/research/00-engagement-brief.md`.

**Teaching checkpoint (brief):**
Present a summary: "Here's what I'm taking into the research. [Key points]. Anything I'm missing or getting wrong?"

**Wait for operator confirmation before proceeding.**

---

## Step 2: Phase 1 — ICP Discovery

Read [phases/01-icp-research.md](phases/01-icp-research.md).

Launch an Opus subagent with the Task tool:
- **Prompt:** The full content of `phases/01-icp-research.md`, preceded by: "Here is the engagement brief for context:" followed by the full content of `00-engagement-brief.md`.
- **Model:** opus
- **Subagent type:** general-purpose

The subagent will use WebSearch to research the ICP. When it returns:

1. Save the raw output to `[context-dir]/_inputs/research/01-icp-raw.md`.
2. Process the raw output into `[context-dir]/icp.md` — clean up, add structure, remove redundancy, but preserve all data and sources.

**Teaching checkpoint:**
1. Present the 3-5 most important findings: "Here's what stands out about who buys this..."
2. Flag any surprises vs. Phase 0 assumptions: "You said [X] — the research shows [Y]."
3. Present source confidence summary: what's solid, what's qualified, what's missing.
4. Ask: "Does this match what you're seeing? Anything to add or challenge?"

Annotate `icp.md` with operator reactions. Carry forward to next phase.

**Wait for operator input before proceeding.**

---

## Step 3: Phase 2 — Market Context

Read [phases/02-market-context.md](phases/02-market-context.md).

Launch an Opus subagent with the Task tool:
- **Prompt:** The full content of `phases/02-market-context.md`, preceded by the Phase 0 engagement brief and the processed Phase 1 ICP output.
- **Model:** opus
- **Subagent type:** general-purpose

When the subagent returns:

1. Save raw output to `[context-dir]/_inputs/research/02-market-context-raw.md`.
2. Hold the processed market context — it will be incorporated into the Phase 4.5 synthesis rather than a standalone deliverable.

**Teaching checkpoint:**
1. Present the market narrative in condensed form: "Here's what's happening in this market right now..."
2. Surface the 3-5 things that matter most for GTM decisions.
3. Flag any time-sensitive opportunities or threats.
4. Ask: "Does this match what you're seeing in conversations with the client?"

Annotate with operator reactions. Carry forward.

**Wait for operator input before proceeding.**

---

## Step 4: Phase 3 — Competitive Landscape

Read [phases/03-competitive-landscape.md](phases/03-competitive-landscape.md).

This phase has three components:

### Step 4A: Named Competitor Profiles (Subagent)

Launch an Opus subagent with the Task tool:
- **Prompt:** The "Component 3A" section from the phase file (everything between "Send everything below this line" and "End of 3A Prompt"), preceded by Phase 0-2 outputs.
- **Model:** opus
- **Subagent type:** general-purpose

Save raw output to `[context-dir]/_inputs/research/03-competitive-raw.md`.

### Step 4B: Do-Nothing Competitor (Main Context)

While waiting for or after the subagent returns, work through Component 3B in main context. Use all prior research plus the 3A raw output to analyze the do-nothing segment. Follow the guide in the phase file.

### Step 4C: Trigger Events (Main Context)

Work through Component 3C in main context. Identify and tier the trigger events following the guide in the phase file.

### Synthesis

Combine 3A, 3B, and 3C into `[context-dir]/competitive-landscape.md` using the synthesis format in the phase file. Include the quick-reference matrix.

**Teaching checkpoint (important — most strategically loaded phase):**
1. "[N] named competitors, plus the do-nothing segment. Here's the landscape..."
2. Present each competitor in 2-3 sentences with the key displacement angle.
3. "The do-nothing competitor is [description]. Here's why they stay..."
4. "These are the trigger events that create real urgency: [top 3]"
5. Ask: "Which of these competitors do the client's customers most commonly switch from?"

Annotate with operator reactions. Carry forward.

**Wait for operator input before proceeding.**

---

## Step 5: Phase 4 — Buyer Personas

Read [phases/04-buyer-personas.md](phases/04-buyer-personas.md).

Launch an Opus subagent with the Task tool:
- **Prompt:** The full content of `phases/04-buyer-personas.md`, preceded by ALL prior phase outputs (engagement brief, ICP, market context, competitive landscape).
- **Model:** opus
- **Subagent type:** general-purpose

When the subagent returns:

1. Save raw output to `[context-dir]/_inputs/research/04-personas-raw.md`.
2. Process into `[context-dir]/buyer-personas.md` — clean up, ensure each persona connects to competitive reality and trigger events.

**Teaching checkpoint:**
1. Present each persona as a brief narrative: "Meet [Name], the [Title]..."
2. "Here's what matters about each for how we reach them..."
3. Flag which persona is highest priority and why.
4. Ask: "Do these match real people you've encountered? Which is the primary decision-maker vs. influencer vs. blocker?"

Annotate with operator reactions.

**Wait for operator input before proceeding.**

---

## Step 6: Phase 4.5 — Research Synthesis

Read [templates/synthesis-template.md](templates/synthesis-template.md).

This runs entirely in main context. Synthesize ALL research (Phases 0-4) into `[context-dir]/market-research.md` following the template structure:

1. Executive Summary (3-5 paragraphs)
2. ICP Summary (condensed from Phase 1)
3. Market Dynamics (condensed from Phase 2)
4. Competitive Reality (condensed from Phase 3 — named competitors, do-nothing, triggers)
5. Buyer Profiles (condensed from Phase 4)
6. Strategic Implications (5-8 items — this is where the value is)
7. Source Confidence Summary
8. Open Questions

**Writing standards:**
- This is a SYNTHESIS, not a stapling. Connect findings across phases.
- Strategic Implications must compare against Phase 0 baseline assumptions.
- Source confidence becomes a messaging guardrail for all downstream work.
- Someone should be able to read this in 5 minutes and understand the full picture.

**Teaching checkpoint (final):**
1. Present strategic implications one by one.
2. "Here's what surprised me vs. what we assumed in Phase 0..."
3. "Here are the open questions I think we need to resolve with the client..."
4. Operator final review.

**Wait for operator sign-off before proceeding.**

---

## Step 7: Optional Phases

After Phase 4.5 sign-off, present the operator with a choice:

"Core research is complete. Two optional phases are available:

**Phase 5: Customer Evidence Discovery** — Finds where social proof, case studies, and reviews exist online. Useful when you need social proof for messaging or the client has thin third-party validation.

**Phase 6: Niche Data Sources** — Identifies 3-5 high-signal data sources for targeting and list building. Useful when the engagement needs outbound targeting infrastructure.

Run either, both, or neither?"

**Wait for operator decision.**

### If Phase 5: Customer Evidence

Read [phases/05-customer-evidence.md](phases/05-customer-evidence.md).

Launch a Sonnet subagent:
- **Prompt:** The full content of the phase file, with the company name and any industry-specific review platforms identified in Phase 2.
- **Model:** sonnet
- **Subagent type:** general-purpose

Save raw to `[context-dir]/_inputs/research/05-evidence-raw.md`. Process into `[context-dir]/customer-evidence.md`.

Brief checkpoint: "Found [N] case studies, [N] review platforms, [N] social proof sources. Notable gaps: [gaps]. Anything else to look for?"

### If Phase 6: Niche Data Sources

Read [phases/06-niche-data-sources.md](phases/06-niche-data-sources.md).

Launch a Sonnet subagent:
- **Prompt:** The full content of the phase file, preceded by Phase 1 ICP and Phase 3 competitive landscape outputs.
- **Model:** sonnet
- **Subagent type:** general-purpose

Save raw to `[context-dir]/_inputs/research/06-sources-raw.md`. Process into `[context-dir]/targeting-sources.md`.

Brief checkpoint: "Identified [N] high-signal data sources. Here's what each gives us: [summary]. These complement each other because [reason]."

---

## Error Handling

**Subagent returns thin results:** If a subagent's output is notably thin (few sources, low confidence across the board, major gaps), flag it to the operator: "Phase [N] research came back thin — [specific issue]. Options: (1) re-run with more specific search terms, (2) proceed with what we have and flag gaps, (3) operator provides supplemental information." Do not silently proceed with low-quality research.

**Operator doesn't know answers in Phase 0:** This is expected for some questions. Mark unknown areas as "Key Questions to Investigate" in the engagement brief. These become explicit research targets for subsequent phases.

**Client directory structure unclear:** If you can't determine whether the client uses simple or multi-engagement structure, ask the operator. Don't guess.

**Phase outputs contradict each other:** Surface the contradiction to the operator at the next teaching checkpoint. "Phase 1 suggested [X] but Phase 3 found [Y]. Which aligns with what you're seeing?" Contradictions are valuable signals, not errors.

**Context window pressure:** Each subagent runs in its own context. The main context accumulates phase outputs. If context is getting long after Phase 3, offer the operator a break point: "Good break point. We can continue in this session or start fresh with Phase 4 — all research is saved to files."

---

## After Completion

Present to the operator:

1. **Summary of what was produced:**
   - `market-research.md` — primary synthesis (loaded every session)
   - `icp.md` — detailed ICP
   - `competitive-landscape.md` — competitors, do-nothing, triggers
   - `buyer-personas.md` — buyer personas
   - Plus any optional phase outputs
   - Raw research in `_inputs/research/`

2. **Recommended next steps:**
   - Share strategic implications with the client team for validation
   - Resolve open questions listed in the synthesis
   - The market research deliverables are now available for downstream skills (positioning, messaging, campaign design)

3. **Quality note:** This research is a foundation, not a final answer. It should be updated when significant new information arrives — a client call that reveals new competitors, a market event that shifts dynamics, or validation that changes assumptions. The skill supports re-running individual phases (see [roadmap.md](roadmap.md) for incremental update mode plans).

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Tools | `WebSearch` | Research queries in Phases 1-6 (via Opus and Sonnet subagents) |
| Tools | `Task` | Launch subagents for parallel research phases |
| Files | Write: `clients/*/context/**` | Research deliverables (icp.md, competitive-landscape.md, buyer-personas.md, market-research.md) |
| Files | Write: `clients/*/context/_inputs/research/**` | Raw subagent outputs |
| Files | Write: `clients/*/engagements/*/context/**` | Alternate path for multi-engagement clients |

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
