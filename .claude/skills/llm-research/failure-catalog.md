# Prompt Failure Catalog

**Loaded by:** Step 2 as a post-draft safety net — scan the active checklist, fix any that apply.
**Updated by:** Step 7 when a research session surfaces a new failure mode.
**Purpose:** Lean quality gate. Only items that caught real problems in real sessions.

---

## Active Checklist

### Composition Framing

- [ ] **Format labels trigger template-matching.** "Write a landing page" produces sales page templates regardless of voice direction. "Write the argument that makes someone sign up" produces argument-first composition. When composition keeps failing, change the format label — the frame triggers the pattern, not the prompt details.

Scan after drafting. Fix any that apply.

### Prompt Design

- [ ] **No hints or examples that anchor the answer.** Parenthetical examples and candidate answers turn the model into a yes-man. Force it to derive, not confirm.
- [ ] **Context orients without prescribing.** Every context element should pass: "Does the model need this to understand the situation, or am I steering?" Includes: no internal system jargon ("session frames," "intelligence docs"), no stakeholder details (names, titles, interpersonal reads), nothing that implies what the answer should be.
- [ ] **Scope naming matches full intent.** If the research covers a full process, name the full scope — not just the most salient component. "Ideation factory" anchored models on idea generation when the intent was the full creative pipeline.
- [ ] **Design thinking before taxonomy.** If the research is about a product/UX problem, the prompt must start from human scenarios (who, what just happened, time pressure, audience, emotional state) — NOT report types, feature lists, engine architectures, or product menus. Taxonomy is a conclusion, not a starting point. Models will eagerly classify and architect if you let them — the prompt must force them to stay in the user's moment first.
- [ ] **Deep research vs extended thinking — pick deliberately.** Deep research returns citation-heavy reports. Extended thinking returns opinionated judgment. Design problems, strategic framing, and "what should we do" questions need thinking mode. "What exists in the market" and "what do competitors offer" need research mode. Sending a design question to deep research produces a well-sourced answer to the wrong question.
- [ ] **Origination passes: resist the scaffold-and-quota instinct.** On a *generative* round, the tempting "improvements" are buckets/categories to fill and a volume quota ("give me 25+ ideas across these 5 buckets"). Both anchor: buckets pre-decide where the model looks (it fills your matrix instead of finding the class you *didn't* name), and a count optimizes for *obvious* high-volume ideas — the opposite of originality density. Prefer instead: **one floor-calibration example** (the altitude you mean, kept deliberately mediocre so it doesn't seed the good ideas), **a stopping rule** ("keep going until you're scraping past the obvious") not a count, and **minimal suppression** (one "diverge, don't converge" line, not a stack of don't-do-X's — suppression burns generative budget). And **don't phrase the goal as your hypothesis** ("make them *want* to act" forecloses the remove-the-decision / default-on / opt-out class). Validated: asked to critique an origination prompt, Gemini pushed scaffold+quota (its over-structuring profile), Claude pushed calibration-example + de-suppression + the smuggled-hypothesis catch — for origination, Claude's was right; Gemini's would have produced balanced-but-generic output.
- [ ] **Withhold the answer when testing whether a doc *communicates* X.** If the goal is to verify a document conveys something (not to teach it), do NOT pre-state it — ask the reader to tell you, in their own words, what the doc says. Their answer is the test. Validated: withholding a key conceptual separation turned one question into a clean before/after on a mid-session edit — adversarial readers who misread it pre-edit read it correctly post-edit.
- [ ] **Verify load-bearing facts against live sources before building the context package.** Numbers and system-state claims lifted from internal docs can be stale — and a model can only reason from what you hand it, so a stale fact becomes the model's biggest "insight" (it recommends building the thing that already exists). Before drafting Paste 2, spot-check the decisive figures (audience size, what's built, current metrics) against the canonical/live source, not the convenience doc. Validated: a context package carried a stale audience number and "pipeline not built" (when sends were in fact already running) off a stale internal doc — so both models' headline recommendation was to build something already in production.

### Interaction Architecture

- [ ] **Critique-first is a separate turn.** Placing critique instructions at the end of a substantive prompt gets ignored across all three models. If critique-first matters, it's a separate message. **Enforced in SKILL.md Step 2 (v1.3):** Paste 1 must be short (~300 words) with critique as the primary action. Full context goes in Paste 2 (Step 4).
- [ ] **Artifact separated from critique request.** All three models skip critique and jump to research when the full artifact is included alongside. Two-paste workflow: Paste 1 = short framing + critique request (no data dumps). Paste 2 = full context + research questions, sent AFTER critique discussion. **Enforced in SKILL.md Step 2 (v1.3):** explicit "What does NOT go in Paste 1" checklist.
- [ ] **Generative passes: the gate is clarifying-questions-first, not critique-first.** For a *generation* pass (not evaluative research), Paste 1's job flips from "critique my frame" to "ask your sharpest clarifying questions before you generate anything." Same two-message discipline + hard primacy guard ("don't generate yet"); different job. Validated: both models asked, neither jumped to output. *(Pairs with the Step 5 "amplification round" — pressure-test / go-wider / go-deeper — which is where most of the best generative output is actually born.)*

### Cross-Pollination (Step 5)

- [ ] **Lead with evaluation, not integration.** "Evaluate these concepts — do they hold up?" preserves the receiving model's critical judgment. "Incorporate these strong findings" kills it.
- [ ] **Pressure-test prompts must be neutral, never leading.** A strongly-worded "attack / kill this" makes models capitulate (sycophancy) — the critique degrades into agreement with your framing and is worthless. Frame as "evaluate on the merits; defend what's strong as readily as you cut what's weak," with an explicit anti-capitulation guard ("don't fold to my framing — models do this and it's useless to me"). Validated: operator caught a kill-framed amplification prompt before it ran; reframed neutral, and the model then pushed back on the operator's own assumption (the signal we wanted).
- [ ] **Calibrate cynic-role critiques: steelman-first + confidence-rating.** Even a neutral "critique this" makes models *manufacture* objections to play the role. Before trusting a critique, force a calibration pass: (1) steelman the thing first — where is it genuinely right?; (2) rate confidence on each objection (high/med/low) and separate "would bet on it" from "raised because asked." ~Half the round-1 objections collapsed under this in testing. This is the antidote to performed skepticism — run it as a default pass on any evaluative critique.

### Synthesis / Interpretation

- [ ] **Convergence is not validation — watch for correlated error.** Two or three models landing on the same conclusion can be corroboration OR shared-prior pattern-matching (e.g., all reading "two-sided marketplace cold-start" off surface cues without the domain facts). When models converge, ask whether they share a prior that could be wrong *together*; hold the ground truth yourself rather than treat a unison chorus as proof. The agent's job is to be the sensor for correlated error, not to amplify it. Observed: both models converged round-1 on a *false* keystone that the operator's domain facts dismantled.
- [ ] **A "resolved / high-confidence" call is a hypothesis until domain ground-truth checks it — hold *all* resolved calls loosely.** A synthesis marks some calls "resolved" or "high confidence" — that's the model's confidence in its own *reasoning*, not evidence the call is *right* (and it applies to a single confident call, not just cross-model convergence). Before a "resolved" call drives a build, name its **load-bearing premise** and check that premise against domain ground-truth the model didn't have. Surface the premise for the operator to check — don't inherit the confidence label. Validated: two "high-confidence" synthesis calls were reversed on operator domain knowledge — both load-bearing premises turned out false once grounded in how the domain actually works.

### Scaffold

- [ ] **No `claude.md` filename in research folders.** macOS is case-insensitive — Claude Code auto-loads it as project instructions. Use `claude-desktop.md`.

---

