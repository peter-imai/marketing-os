---
name: llm-research
description: Deep multi-LLM research — desktop-first workflow with Claude Code orchestration
version: 1.4
---

# LLM Research

Deep strategic research using multiple LLMs. Claude Code orchestrates the thinking — prompt drafting, feedback synthesis, cross-pollination routing, final synthesis. The operator runs the models in their desktop apps (Claude Desktop, ChatGPT, Gemini) where subscriptions cover usage and deep research/extended thinking modes are available natively.

## Permissions

- **Write:** Creates research folder and files.
- **Read:** Reads response files and reference materials.
- **No Bash/API required.** Models run in desktop apps, not via API dispatch.

## Workflow

### Step 1: Orient

Draft an intent — 2-3 sentences that answer: **What do we want to learn, and why does it matter right now?**

Not "review our JTBD framework" — that's a method. The intent is the decision this research will inform.

Examples:
- "We want to know what makes brokers want to spend time on this platform every day — not the business model, just the experience."
- "We want to find the holes in our positioning before we launch."

Ask or infer: any sensitivities to anonymize (company names, pricing, competitive details).

Present the intent to the operator.

**GATE: Operator approves intent or adds color.**

### Step 2: Draft Critique Prompt + Scaffold

Based on the approved intent:

1. Redraft the intent (incorporating operator color).
2. Draft a **short** critique prompt. Read `model-profiles.md` (in this skill directory) for per-model awareness.
3. Scan `failure-catalog.md` as a post-draft safety net.

**CRITICAL — Two-message architecture.** The critique prompt is Paste 1. The full context + research questions are Paste 2 (drafted in Step 4, sent after critique discussion). These MUST be separate messages in the desktop app conversation. The failure catalog documents why: models skip critique and jump to research when the full context is included alongside the critique request. Critique instructions buried at the end of a substantive prompt get ignored across all three models.

**Critique prompt structure (Paste 1):**

The critique prompt should be **short** — under ~300 words. Its job is to get the model **evaluating the research frame itself** BEFORE it has the full context to anchor on. The output we want is a verdict on whether this is the right question to point a deep research pass at — not a critique that drifts toward partial answers. Structure:

1. **Front-loaded single-job instruction (FIRST — primacy position).** Open with a direct statement: *"Right now, I am only asking you to do one thing: critique the research frame I'm about to describe."* Explicit guards: *"Don't research it. Don't answer it. Don't draft a polished replacement frame ready to run."* Tell them the full context comes in the next message. This goes BEFORE the avatar so it's the hardest line to forget. Models default to helpfulness and will start solving unless the constraint is in primacy.
2. **Avatar** — who they are for this exercise (2-3 sentences, specific with economic context).
3. **Situation** — brief orientation, NOT a full briefing (3-5 sentences max — just enough to understand the domain and what's being attempted).
4. **The frame to critique** — state the operator's current frame as numbered assumptions or framings. This is the **attack surface**. **Resist the urge to bullet-list attack angles** ("does X cut at the joint? does Y smuggle bias?") — those duplicate the surface and constrain where the model looks. The numbered assumptions give them the targets; let them find their own angles. Operator-validated: stripping prescribed angles trusts the model to cook.
5. **Restated meta-question (closing).** Re-state the single job in different words. The load-bearing line: *"Tell us whether this is the highest-leverage question to point a deep research pass at right now, asked the right way, at the right level."* Pair with: *"Don't start the research; tell us whether this is the research worth running."* Invite cynicism and extended thinking. Restating in primacy + recency positions makes the meta-frame inescapable.
6. End with: **"Let me know when you're ready for the full context and research questions."** — signals Paste 2 is coming.

**What does NOT go in Paste 1:**
- Detailed data schemas, field lists, or table structures
- Full module inventories or content specifications
- Historical data about production pipelines
- Anything that gives the model enough to start "solving" instead of critiquing

All of that goes in Paste 2 (Step 4) alongside the research questions, after the critique discussion has sharpened the framing.

**Create the research folder and scaffold files:**

```
workspaces/[workspace]/research/YYYY-MM-DD-[topic]/
├── 00-critique.md        # Critique prompt only (Paste 1 — short, framing-focused)
├── 00-context.md         # Full context + research questions (Paste 2 — populated in Step 4)
├── 01-feedback.md        # Per-model critique feedback + discussion notes (populated in Step 3-4)
├── 02-claude-desktop.md  # ## Research
├── 02-chatgpt.md         # ## Research
├── 02-gemini.md          # ## Research
├── 03-synthesis.md       # Final synthesis (populated in Step 6)
```

Write the critique prompt to `00-critique.md`. Create `00-context.md` with a placeholder (populated in Step 4). Create the three model files with `## Research` header and paste instructions in HTML comments. Create `01-feedback.md` with per-model section headers (`## Claude`, `## ChatGPT`, `## Gemini`). Create `03-synthesis.md` with a placeholder header.

Present the critique prompt in the conversation for the operator to copy and paste.

**GATE: Operator approves or edits the critique prompt.**

Tell the operator: "Copy this to all three desktop apps. Enable deep research / extended thinking. When critiques come back, paste them here in the conversation."

### Step 3: Discuss Critiques

The operator pastes LLM critiques directly into the conversation — not into files. Critiques are transient input for discussion, not artifacts to store.

Read all critiques. Then run an **interleaved discussion** — organized by theme, not by model:

1. Identify the main critique themes across all three models. Group related points.
2. For each theme, present what each model said (verbatim quotes, not summaries) and where they agree or diverge.
3. After presenting each theme, **ask the operator for their take.** Do they agree? Is the model missing context? Is this a real gap or a misunderstanding?
4. This is a conversation, not a presentation. Surface a theme, discuss it, move to the next. The operator's input on each point shapes the per-model responses in Step 4.

The goal: by the end, you and the operator have worked through every major critique point together. The operator has given their position. You understand what each model needs to hear.

**GATE: All major critique themes discussed. Operator confirms they've said what they need to say.**

### Step 4: Draft Full Context + Research Questions (Paste 2) + Per-Model Feedback

The critique conversation has refined the framing. Now build Paste 2 — the full context and research questions.

**This is where the heavy context goes.** Everything that was deliberately excluded from the critique prompt (Paste 1) — detailed data schemas, table structures, module inventories, production pipeline details, constraints — goes here. The models now have the critique discussion as their lens; this context will be processed through that sharpened framing rather than overwhelming it.

1. **Draft the full context package** — all the detailed information the models need to do the research. Data reality, current structures, constraints, specifications. Write to `00-context.md`.

2. **Draft the research questions** — informed by the critique discussion. Open questions — "what do you see?" not "is this right?" Most important questions first. Nothing that steers. Scan `failure-catalog.md` as a post-draft safety net.

3. **Draft per-model feedback** — individual responses for each model that:
   - Address that model's specific critique points with the operator's clarifications
   - Include the full context package (or reference it if too long — "here's the full context I mentioned")
   - Include the research questions
   - Tell the model to proceed with the research using the clarified framing

Write to `01-feedback.md` with per-model headers:

```markdown
# Feedback + Research Questions

## Claude
[Critique feedback + full context + research questions for Claude Desktop]

## ChatGPT
[Critique feedback + full context + research questions for ChatGPT]

## Gemini
[Critique feedback + full context + research questions for Gemini]
```

Present `01-feedback.md` to the operator for review.

**GATE: Operator approves.**

Tell the operator: "Copy each model's section from `01-feedback.md` and paste it into the corresponding desktop app. They'll do their deep research. Paste the results into the model files (`02-claude-desktop.md`, `02-chatgpt.md`, `02-gemini.md`) under `## Research`."

### Step 5: Process Research

Wait for operator to confirm research results are pasted into the model files (`02-claude-desktop.md`, `02-chatgpt.md`, `02-gemini.md`).

Read all three research results. Present key findings from each — don't dump full text.

Then assess cross-pollination value. Read the cross-pollination guide in `model-profiles.md`. Recommend specific routing if warranted:

- "Gemini had a sharp take on X that Claude missed. I'd send Gemini's analysis to Claude with this framing: [copy block]."
- "All three converged on Y — no cross-pollination needed there."
- "Claude and ChatGPT disagree on Z. Worth sending both perspectives to Gemini for a tiebreaker."

If the operator wants cross-pollination: draft the prompts, operator executes in desktop apps, pastes responses into model files (`02-*`) under `## Cross-Pollination`.

#### The amplification round (generative passes — propose it by DEFAULT, don't wait to be asked)

On a *generation* pass, cross-pollination isn't tie-breaking — it's where a large share of the best output is born. After the first generation round, **proactively propose a directed amplification round** that points the models at each other with three distinct mandates (mix as fits the material):

- **Pressure-test** — each model attacks the *other's* load-bearing claims: kill the seductive-but-wrong, reconcile or reject the tensions. **Front-load this as the FIRST job in the prompt** (and tell the model to do it before generating anything new) — otherwise it skips the disciplined critique for the fun of generating.
- **Go wider** — "here's a whole *class* you didn't explore — go deep there," plus "name a class *neither* of you touched and generate into it." This is where the net-new ideas come from.
- **Go deeper** — expand / explain / size the strongest ideas. Usually best run *after* selection narrows the set (deepening all of them is waste; deepening the chosen few is gold).

Match mandates to model character — **asymmetric, not identical jobs**: the strong reconciler/builder (e.g. Claude) carries go-wider + reconciliation; the scalpel (e.g. Gemini) carries the pressure-test / kill-list. Bidirectional cross-poll (vs. the default Gemini→Claude-only) is justified when *both* models produced distinct divergent material worth both attacking and extending. Anti-anchor the go-wider: ask each model to name the unexplored class *itself first*, then offer your candidate directions as additional seeds.

**Why this is a default, not an option:** in practice this move surfaced a whole set of high-value items a single round missed — and historically it only happened when the operator manually intervened. Propose it so it doesn't depend on that.

**GATE: Operator decides on cross-pollination and confirms when complete.**

### Step 6: Synthesize

Write `03-synthesis.md` — the final artifact. This is not a summary of what three models said. It's a strategic synthesis that:

- Integrates the strongest thinking from all models
- Incorporates the operator's judgment (from Steps 3-5)
- Resolves contradictions with a clear position
- Identifies what's actionable vs. what needs more thinking

**Quality checks before presenting synthesis:**
- Does every identified contradiction get resolved with a clear position (not "both have a point")?
- Does the synthesis name specific operator judgments from Steps 3-5?

Present the synthesis to the operator.

### Step 7: Capture Learnings

After the research is complete:

1. **Prompt learnings** — Did the critiques reveal prompt design gaps? If a new failure mode emerged, add it to `failure-catalog.md`.
2. **Model behavior** — Did any model surprise you? Update `model-profiles.md` observation log.
3. **Failure patterns** — Anything go wrong? Check `failure-catalog.md` — if the pattern is new, add it.

Write a brief note at the bottom of `03-synthesis.md` summarizing learnings captured. Present to operator for confirmation before updating shared files.

**DONE.**

## Notes

- **Desktop apps maintain conversation state.** Each phase continues the chat in that app — the operator doesn't need to re-paste history.
- **All three models typically earn their keep** for strategic research. The divergence is the point.
- **Cross-pollination is directional, not symmetric.** Gemini's cynicism sharpens Claude's thoroughness. Claude's depth gives Gemini something to react to. ChatGPT is the wild card. See model-profiles.md for routing logic.

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
