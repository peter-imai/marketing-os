# Blueprint: Client Context Architecture

**Version:** v1.0 | **Status:** Active

## Purpose

Every client needs foundational context before the system can do meaningful work. Without it, every session starts from zero.

This blueprint defines:
1. **What docs** every client produces (the canonical foundation)
2. **How each doc is generated** (three distinct methods)
3. **What order** they're produced in (the onboarding sequence)

---

## Architecture Overview

```
Foundation (produced during onboarding)
├── Positioning          — what you sell, why you're different
├── ICP                  — what companies to target (B2B only)
├── Market Context       — where your market sits on the adoption curve
├── Buyer Personas       — who buys, their pain, their language
└── Marketing Strategy   — how you reach those buyers

Conditional (produced if applicable)
└── Engagement Strategy  — relationship layer (multi-client only)
```

---

## Onboarding Routing

**Flag 1: B2B or B2C?**
- B2B → produce ICP (company-level targeting) + Buyer Personas
- B2C → produce Buyer Personas only (ICP is redundant)

**Flag 2: Single business or multiple clients?**
- Single business → skip Engagement Strategy
- Multiple clients → produce Engagement Strategy per client

---

## Foundation Docs

### 1. Positioning

**Purpose:** What you sell, who it's for, why you're different.

**Generation method:** Facilitated discovery (Dunford methodology). Operator-intensive — the agent facilitates, the operator makes the calls.

**Methodology source:** `resources/april-dunford/positioning-sop-scale-partners.md` — 7-step process based on April Dunford's "Obviously Awesome."

**Key sections:**
- **Best-fit customer** — Situational, not demographic. "Someone who is [situation] and needs [outcome]."
- **Competitive alternatives** — What the buyer does instead. Include "do nothing."
- **Unique capabilities** — What you can do that alternatives can't. Specific and provable.
- **Value themes** — Capabilities clustered into buyer-meaningful benefits. 2-4 themes.
- **Market frame** — What category you compete in, or the new one you're creating.
- **Product/service description** — What you sell, how it works, what it costs.

**Quality signal:** Someone unfamiliar reads it and can explain what makes it different in one sentence.

**Update triggers:** New product/service, competitive shift, audience pivot.

---

### 2. ICP (B2B Only)

**Purpose:** What companies to target — firmographic, technographic, behavioral profile.

**Generation method:** LLM research with web search. Feed your positioning, get back a data-driven company profile.

**Generation source:** `resources/jordan-crawford/market-research/01-client-icp.md` — Crawford ICP research prompt.

**Key sections:**
- Company size parameters (revenue, employees, growth)
- Industry verticals with specific use cases
- Technical requirements
- Budget and purchase authority
- Team structure and stakeholder roles
- Use case specifics

**Quality signal:** You could build a targeting list from it without additional interpretation.

**Update triggers:** Win/loss patterns change, new vertical success, pricing shift.

---

### 3. Market Context

**Purpose:** Where your market sits on the adoption curve — the story of how this space got here.

**Generation method:** LLM research with web search. Produces a narrative analysis grounded in evidence.

**Generation source:** `resources/jordan-crawford/market-research/02-market-context.md` — Crawford market context research prompt.

**Key sections:**
- Historical context — evolution, inflection points
- Current state analysis — buyer behavior, vendor evolution
- Adoption patterns — who's buying now vs. a year ago
- Future trajectory — signals, barriers, enablers

**Quality signal:** Reads as a coherent narrative, not a bullet-point summary. At least 1000 words.

**Update triggers:** Major market event, new competitor, adoption stage shift, annual refresh.

---

### 4. Buyer Personas

**Purpose:** Who buys — the humans making the purchase decision. Their pain, their language, their process.

**Generation method:** LLM research with web search. Data-driven personas from professional footprint analysis.

**Generation source:** `resources/jordan-crawford/market-research/03-buyer-persona.md` — Crawford buyer persona research prompt.

**Key sections per persona:**
- Professional snapshot — career, expertise
- Daily reality — responsibilities, KPIs, challenges
- Decision driver analysis — evaluation criteria, validation needs, ROI expectations
- Communication profile — channels, content preferences, trust building
- Professional motivation map — career drivers, impact goals

**Quality signal:** Each persona feels like a real person you could recognize professionally.

**Update triggers:** New buyer type, behavioral shift, win/loss data contradicts persona.

---

### 5. Marketing Strategy

**Purpose:** How you reach buyers — execution brain. What you believe and what you're doing about it.

**Generation method:** Agent-elicited interview. Conversational synthesis of the operator's existing thinking.

**Key sections:**
- **Strategic thesis** — The core bet. Opinionated and specific.
- **How we see the product** — What we lead with, what we don't do.
- **Content strategy** — How content serves the business (depth varies by engagement).
- **How we see the market** — Competitive landscape and positioning stakes.
- **Audience strategy** — Who we're building for, segmented, prioritized.
- **Growth thesis** — How growth works. Discovery → engagement → conversion → retention.
- **What's working / What's not** — Performance reality.
- **Hypotheses** — Explicit, testable bets. "We believe if we do X, Y will happen."

**Quality signal:** Every section states a decision or position. No hedge-filled sections.

**Update triggers:** Performance data invalidates a position, scope change, quarterly review.

---

## Conditional Docs

### Engagement Strategy (Multi-Client Only)

**Purpose:** The relationship layer. "Who are these people, what do they want, how do I show up?"

**Generation method:** Agent-elicited interview.

**Key sections:**
- **Engagement thesis** — What the relationship IS.
- **What success looks like** — Per-stakeholder. Specific outcomes.
- **How we show up** — Tone, dynamics, dos and don'ts.
- **The people** — Individual profiles + dynamics.
- **Engagement structure** — Scope, compensation, cadence.
- **Risks & constraints** — What could go wrong.
- **Open questions** — Each tied to a decision it unlocks.

---

## Production Sequence

The dependency order IS the onboarding sequence:

```
1. Positioning              ← Operator-driven. Everything flows from this.
   ↓
2. ICP (if B2B)             ← Research, scoped by positioning.
   ↓
3. Market Context           ← Research, scoped by positioning + ICP.
   ↓
4. Buyer Personas           ← Research, scoped by ICP (B2B) or positioning (B2C).
   ↓
5. Marketing Strategy       ← Agent interview. Informed by all docs above.
   ↓
6. Engagement Strategy      ← Agent interview. Only if multi-client.
   (if multi-client)
```

**Post-onboarding:** Market context may revise positioning. Buyer personas may reveal new segments. The sequence is linear for production but forms a feedback loop once docs exist.

---

## File Placement

```
clients/[client-name]/
├── context/
│   ├── positioning.md
│   ├── icp.md              (B2B only)
│   ├── market-context.md
│   └── buyer-personas.md
├── marketing-strategy.md    (root — Tier 1 operational)
├── engagement-strategy.md   (conditional)
├── core.md                  (what matters right now — intention, watches, core documents)
└── backlog.md
```

Strategy docs at client root — loaded every session. Foundation docs in `context/` — loaded on demand.

---

## Frontmatter

All Tier 1 docs carry YAML frontmatter:

```yaml
---
type: [strategy | foundation | intelligence]
description: "One line"
status: [working-notes | operator-reviewed | doctrine]
client: [client-name]
created: [session number]
last-updated: [session number]
updated-by: [operator | agent | joint]
---
```

**Status progression:** Working Notes → Operator-Reviewed → Doctrine.

---

## Importing from External Systems

When migrating from an existing setup:

1. Create `_inputs/` staging folder in the client directory
2. Push raw docs from the old system into `_inputs/`
3. Triage: what maps to which canonical doc?
4. Build foundation docs from the relevant content
5. Clean `_inputs/` once processed (git preserves history)

The migration is a strategic review, not a copy-paste. Question every position. Validate currency.

---

## Anti-Patterns

| Anti-Pattern | What Goes Wrong | Prevention |
|---|---|---|
| **Agent-inferred strategy** | Agent synthesizes from session history without validation. Grounds itself in its own guesses. | Status tracking. Operator ratification is not optional. |
| **Strategy doc as data dump** | Metrics and schedules bloat the doc. Buries decisions. | Foundation vs. Context boundary. Weekly data belongs elsewhere. |
| **Static strategy** | Written once, never updated. Agent grounds on stale positions. | Enforcement hooks + update triggers + Hypotheses section. |
| **Template filling without conviction** | Sections filled because template demands it. Says nothing. | Every section states a decision. "TBD" beats hedging. |
| **Skipping positioning** | Everything downstream inherits vagueness. | Production sequence enforced — positioning is Step 1. |
