---
name: llm-research
description: Deep multi-LLM research — desktop-first workflow with Claude Code orchestration
version: 1.3
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

**CRITICAL — Two-message architecture.** The critique prompt is Paste 1. The full context + research questions are Paste 2 (drafted in Step 4, sent after critique discussion). These MUST be separate messages in the desktop app conversation. The failure catalog documents why: models skip critique and jump to research when the full context is included alongside the critique request.

**Critique prompt structure (Paste 1):**

The critique prompt should be **short** — under ~300 words. Its job is to get the model thinking critically about the framing BEFORE it has the full context to anchor on. Structure:

1. **Avatar** — who they are for this exercise (2-3 sentences, specific with economic context)
2. **Situation** — brief orientation, NOT a full briefing (3-5 sentences max)
3. **The framing we want critiqued** — our current approach/assumptions (keep it tight)
4. **Critique request as the PRIMARY and FINAL action** — what to push back on, what to look for
5. End with: **"Let me know when you're ready for the full context and research questions."**

**What does NOT go in Paste 1:**
- Detailed data schemas, field lists, or table structures
- Full module inventories or content specifications
- Historical data about production pipelines
- Anything that gives the model enough to start "solving" instead of critiquing

All of that goes in Paste 2 (Step 4).

**Create the research folder and scaffold files:**

```
clients/[client]/research/YYYY-MM-DD-[topic]/
├── 00-critique.md        # Critique prompt only (Paste 1)
├── 00-context.md         # Full context + research questions (Paste 2 — Step 4)
├── 01-feedback.md        # Per-model critique feedback + discussion notes
├── 02-claude-desktop.md  # ## Research
├── 02-chatgpt.md         # ## Research
├── 02-gemini.md          # ## Research
├── 03-synthesis.md       # Final synthesis (Step 6)
```

Write the critique prompt to `00-critique.md`. Create remaining files with headers and paste instructions.

Present the critique prompt for the operator to copy.

**GATE: Operator approves or edits the critique prompt.**

Tell the operator: "Copy this to all three desktop apps. Enable deep research / extended thinking. When critiques come back, paste them here."

### Step 3: Discuss Critiques

The operator pastes LLM critiques directly into the conversation — not into files.

Read all critiques. Then run an **interleaved discussion** — organized by theme, not by model:

1. Identify the main critique themes across all three models. Group related points.
2. For each theme, present what each model said (verbatim quotes, not summaries) and where they agree or diverge.
3. After presenting each theme, **ask the operator for their take.** Do they agree? Missing context? Real gap or misunderstanding?
4. This is a conversation, not a presentation. Surface a theme, discuss it, move to the next.

**GATE: All major critique themes discussed. Operator confirms.**

### Step 4: Draft Full Context + Research Questions (Paste 2) + Per-Model Feedback

The critique conversation has refined the framing. Now build Paste 2.

**This is where the heavy context goes.** Everything excluded from the critique prompt — data schemas, specifications, constraints — goes here.

1. **Draft the full context package.** Write to `00-context.md`.
2. **Draft research questions** — informed by the critique discussion. Open questions — "what do you see?" not "is this right?" Most important first.
3. **Draft per-model feedback** — individual responses addressing that model's critique points + full context + research questions.

Write to `01-feedback.md` with per-model headers:

```markdown
# Feedback + Research Questions

## Claude
[Critique feedback + full context + research questions]

## ChatGPT
[Critique feedback + full context + research questions]

## Gemini
[Critique feedback + full context + research questions]
```

**GATE: Operator approves.**

Tell the operator to paste each model's section into the corresponding desktop app.

### Step 5: Process Research

Wait for operator to confirm research results are in the model files.

Read all three. Present key findings — don't dump full text.

Then assess cross-pollination value. Read the cross-pollination guide in `model-profiles.md`. Recommend specific routing if warranted:

- "Gemini had a sharp take on X that Claude missed — send it to Claude with this framing."
- "All three converged on Y — no cross-pollination needed."
- "Claude and ChatGPT disagree on Z — send both to Gemini for a tiebreaker."

**GATE: Operator decides on cross-pollination and confirms when complete.**

### Step 6: Synthesize

Write `03-synthesis.md` — the final artifact. Not a summary of three models. A strategic synthesis that:

- Integrates the strongest thinking from all models
- Incorporates the operator's judgment
- Resolves contradictions with a clear position
- Identifies what's actionable vs. what needs more thinking

Present to operator.

### Step 7: Capture Learnings

1. **Prompt learnings** — Did critiques reveal prompt design gaps? Add to `failure-catalog.md`.
2. **Model behavior** — Surprises? Update `model-profiles.md` observation log.
3. **Failure patterns** — Check `failure-catalog.md` for new patterns.

Write a note at the bottom of `03-synthesis.md` summarizing captured learnings.

**DONE.**

## Notes

- **Desktop apps maintain conversation state.** Each phase continues the chat — no re-pasting.
- **All three models typically earn their keep** for strategic research. The divergence is the point.
- **Cross-pollination is directional, not symmetric.** See model-profiles.md for routing logic.
