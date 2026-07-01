# Model Profiles

**Loaded by:** Step 2 when drafting prompts and Step 5 when recommending cross-pollination.
**Updated by:** Step 7 when model behavior observations warrant changes.
**Purpose:** Lightweight reference for model strengths and per-task recommendations. Grows with experience.

---

## Profiles

| Model | Character | Strengths | Watch For |
|-------|-----------|-----------|-----------|
| **Claude Desktop** | The A-student. Exhaustive, thorough, follows best practices. Can be naive — "book smart." But once given direction (e.g., Gemini's cynical lens), becomes excellent at deep research. | Deep analysis, evidence quality, honest about gaps, thoroughness, comprehensive coverage. Best as a second-pass deep diver — give it a sharper lens, let it go deep. | Can follow best practices that read like a textbook rather than real-world strategy. Naive until directed. Hedges when a strong opinion would be more useful. |
| **Gemini** | The scalpel. Sharp, cynical, cutting. Less volume, more edge. | Structured strategic synthesis, sharp interpretation, seeing angles others miss, breaking complex artifacts into evaluable components. Good web access for market analysis. | Can be too organized — frameworks without substance. May structure critique so neatly that sharp edges get smoothed. But when it cuts, it cuts well. |
| **ChatGPT** | The wild card. Can be sharp like Gemini or miss the mark. Unpredictable but worth having for divergence. | Breadth, deep research capability, creative reframing, volume of alternative perspectives. Can be cynical and sharp OR comprehensive and thorough. | Can be superficially agreeable without anti-sycophancy framing. Volume of feedback can dilute signal. Less predictable than the other two. |

---

## Cross-Pollination Guide

Cross-pollination is directional, not symmetric. The value depends on matching the right feedback to the right model's character.

### Primary Pattern: Gemini → Claude

The highest-value cross-pollination route. Gemini's cynicism and sharp framing direct Claude's thoroughness. Claude is the A-student who does excellent deep research once pointed in a more cynical direction. Route Gemini's sharpest observations to Claude with framing like: "Consider this perspective and go deep on it."

### Secondary Patterns

| Route | When | Why |
|-------|------|-----|
| **Claude → Gemini** | Claude produced depth that Gemini skipped | Gemini can react to Claude's comprehensive analysis and find the gaps in it |
| **Gemini → ChatGPT** | Need creative alternatives to Gemini's sharp critique | ChatGPT can take Gemini's edge and explore adjacent solutions |
| **ChatGPT → Claude** | ChatGPT surfaced something surprising | Claude can investigate it thoroughly |
| **Both → third model** | Two models agree but neither challenged it | Route the agreement to the third with explicit instruction to challenge |

### Cross-Pollination Prompt Design

**Lead with evaluation, not integration.** The receiving model must have permission to challenge, reshape, or replace the routed idea — otherwise cross-pollination degrades into forced adoption. Frame as: "Here's a concept to evaluate — does it hold up? Would you modify it, or propose something better that serves the same purpose?" Not: "Here are strong findings to incorporate." The difference matters: Claude Desktop revised both ChatGPT concepts significantly (4 channel stages → 2 operating modes, System-first → Demo-first, added Audience-first) because the prompt gave it room to think critically.

### When Cross-Pollination Adds Value

- A model raised something strong but couldn't go deep enough — route to Claude for investigation.
- Two models agree on a diagnosis but neither challenged it — route to the third as a devil's advocate.
- A model's framing revealed a dimension the others missed — route that framing, not just the conclusion.
- Claude was naive on something Gemini saw clearly — route Gemini's take to sharpen Claude's next pass.

### When Cross-Pollination Adds Noise

- Feedback is already comprehensive and convergent — more rounds won't add signal.
- The gap is about engagement context only the operator has, not analysis depth.
- The operator has enough to act on and more rounds delay action.

---

