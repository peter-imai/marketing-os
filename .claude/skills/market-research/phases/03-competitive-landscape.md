# Phase 3: Competitive Landscape — Hybrid Phase Guide

> **When to load:** Phase 3 of market research. This phase has three components:
> - **3A** (subagent): Named competitor profiles — send the subagent prompt section to an Opus subagent
> - **3B** (main context): Do-nothing competitor analysis — strategic work in main context
> - **3C** (main context): Trigger events — strategic work in main context
>
> **Purpose:** Map the competitive landscape including named competitors, the do-nothing segment, and trigger events that create buying urgency.

---

## Component 3A: Named Competitor Profiles — Subagent Prompt

*Send everything below this line through "End of 3A Prompt" to the Opus subagent, along with Phase 0-2 outputs.*

---

You are conducting competitive intelligence research for a B2B company. You have access to web search — use it extensively. Your goal is to build honest, evidence-based profiles of the significant competitors in this market.

### Context

You will receive:
1. An engagement brief with what the operator knows about competitors
2. An ICP analysis showing who the target buyer is
3. Market context showing where the market sits

Use all three to identify and research the competitors that matter for THIS company targeting THESE buyers.

### Competitor Identification

Identify 3-7 significant competitors based on:
- Companies mentioned in the engagement brief
- Companies appearing in G2/Capterra comparisons for this category
- Companies appearing in analyst quadrants (Gartner, Forrester)
- Companies targeting the same ICP segments
- Companies frequently mentioned in "vs." searches

Don't over-include. A competitor that targets enterprise when the client targets mid-market isn't significant. Focus on real ICP overlap.

### For Each Competitor, Research:

**Product Reality (not marketing claims)**
- What does their product actually do? Focus on capabilities, not positioning.
- Where are they strong? What do customers praise in reviews?
- Where are they weak? What do customers complain about?
- What's their technology approach? (Architecture, deployment model, integrations)

**Market Position**
- Company size (employees, funding, revenue if public)
- How long have they been in market?
- What's their growth trajectory? (Hiring patterns, funding rounds, expansion signals)
- What market segments do they dominate vs. where are they weak?

**Switching Friction**
- How hard is it to leave them? (Data lock-in, integration depth, contract terms)
- What does migration look like? (Time, cost, risk)
- What's the emotional switching cost? (Retraining, relationship disruption, organizational change)

**Customer Sentiment**
- What do G2/Capterra/TrustRadius reviews say? (Quote specific reviews)
- What do Reddit, forums, and support communities say?
- What are the recurring complaints?
- What are the recurring praises?

**Pricing and Packaging**
- What's their pricing model? (Per seat, per usage, platform fee)
- How do they compare to the client on price?
- What's included at each tier?
- Are there hidden costs (implementation, training, integrations)?

### Source Confidence Framework

Rate every major claim:

| Confidence | Criteria | Usage |
|------------|----------|-------|
| **High** | Multiple credible sources agree, recent data (<12 months), direct evidence | Claim with full confidence |
| **Medium** | Single credible source, older data (12-24 months), or inferred | Claim with qualification |
| **Low** | Unverified, single weak source, >24 months old, or extrapolated | Do not claim — flag for validation |

### Output Format

For each competitor:
```
## [Competitor Name]

**Overview:** [2-3 sentence summary of who they are and what they do]

**Strengths:** [What they do well, with evidence]

**Weaknesses:** [Where they fall short, with evidence from reviews/forums]

**Switching Friction:** [How hard it is to leave, and why]

**Customer Sentiment:** [Summary of what users actually say, with specific quotes]

**Pricing:** [How they price relative to the client]

**Displacement Opportunity:** [Where and why a buyer would switch FROM this competitor TO the client]

**Confidence:** [High/Medium/Low for each major claim above]
```

After all competitor profiles, include:
- **Competitive Matrix** — Quick-reference table: Competitor | Primary Strength | Primary Weakness | Switching Friction (H/M/L) | Displacement Angle
- **Confidence Summary** — What's solid, what's inferred, what couldn't be found

---

*End of 3A Prompt*

---

## Component 3B: Do-Nothing Competitor Analysis — Main Context Guide

This section runs in main context because it requires strategic thinking, not just research. The "do-nothing competitor" is the segment using manual workarounds, spreadsheets, incumbent tools repurposed, or simply ignoring the problem. This is often 50-70% of the addressable market.

Synthesize from ALL prior research (Phases 0-2 + 3A competitor raw output) to answer:

1. **What workarounds do prospects currently use?** Name them specifically. "Excel spreadsheets updated weekly by a junior analyst" is useful. "Manual processes" is not.

2. **Why does inertia persist?** Reasons people DON'T buy:
   - Not broken enough (the current pain is tolerable)
   - Fear of user revolt (the team won't adopt a new tool)
   - Budget competition (other priorities win the budget)
   - Complexity perception (seems harder than it is)
   - Lack of trigger (nothing forced a decision)
   - Switching cost from current workaround (ironically, even manual processes have switching costs)

3. **What's the true cost of doing nothing?** Quantify where possible:
   - Time cost (hours per week/month on manual processes)
   - Risk cost (what bad things happen without the solution)
   - Opportunity cost (what they can't do while stuck in manual mode)
   - Hidden costs (errors, missed insights, slow decisions)

4. **Who represents this segment?** In terms of the ICP — which companies look like good fits but aren't currently using ANY solution in this category?

---

## Component 3C: Trigger Events — Main Context Guide

What events break buyer inertia and create actual buying urgency? Synthesize from all prior research.

### Tier 1: Force Action
Events that REQUIRE a response — the buyer has no choice but to act.
- Examples: security breach, regulatory deadline, insurance renewal requirement, audit finding, system failure
- For each: What does it look like? How do you detect it? How urgent does it make the buyer? What messaging angle does it open?

### Tier 2: Create Openness
Events that make the buyer WILLING to consider change — not forced, but receptive.
- Examples: new leadership (new VP/CTO wants to put their stamp), peer incident (competitor got breached), vendor review cycle, budget season, strategic planning period
- For each: Same questions as Tier 1.

### Tier 3: Background Pressure
Events that create slow-building discomfort — alone they don't trigger buying, but they accumulate.
- Examples: board questions about the topic, volume growth making manual processes painful, team complaints, industry conference attendance, hiring difficulties in the function
- For each: Same questions as Tier 1.

---

## Synthesis Output

Combine 3A, 3B, and 3C into `competitive-landscape.md`:

1. **Named Competitors** — Processed from 3A raw research. Each competitor in 1-2 paragraphs: who they are, where they're strong, where they're vulnerable, and the displacement angle.

2. **Do-Nothing Competitor** — The full 3B analysis.

3. **Trigger Events** — The full 3C analysis, organized by tier.

4. **Quick-Reference Matrix:**

| Competitor | Primary Pain They Solve | Switching Friction | Opportunity | Top Trigger Events | Lead Message Angle |
|------------|------------------------|-------------------|-------------|-------------------|-------------------|
| [Name] | ... | H/M/L | ... | ... | ... |
| Do-Nothing | ... | M (inertia) | ... | ... | ... |

5. **Source Confidence Summary** — Across all three components.
