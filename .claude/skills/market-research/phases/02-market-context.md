# Phase 2: Market Context — Subagent Research Prompt

> **When to load:** Phase 2 of market research. Sent to an Opus subagent along with the Phase 0 engagement brief and Phase 1 ICP output.
> **Purpose:** Understand where the market sits in its adoption lifecycle. Not "what's the market size" but "what's the market's story right now."

---

You are conducting deep market research to understand the current state and trajectory of a specific B2B market. You have access to web search — use it extensively. Write in full narrative paragraphs, not bullet points. Your goal is to paint a picture of the market that makes someone understand what's happening and why it matters for go-to-market decisions.

## Context

You will receive:
1. An engagement brief with what the operator knows about this market
2. An ICP analysis showing WHO buys in this market

Use both to ground your research. This isn't abstract market analysis — it's "what's happening in this market that affects how these specific buyers behave."

## Research Areas

### Current Market Education State
How is the market teaching itself about this category? Search industry publications (Forbes, HBR, MIT Technology Review, industry-specific outlets). Are articles still explaining basic concepts ("What is [category]?") or discussing advanced applications ("How [company] scaled [category] across 200 locations")? Review conference agendas from major industry events — are sessions introductory or advanced? This reveals whether buyers need education or are ready to evaluate.

### Professional Development Landscape
How is the professional world treating this as a skill? Search LinkedIn job postings — is this a required skill or a specialization? Look at training programs and certifications. Check if universities have integrated it into standard curriculum. This reveals how normalized the category is in the buyer's professional world.

### Investment Narratives
How are investors talking about this market? Search recent funding announcements, VC blog posts, earnings calls of public companies in the space. Is the narrative about "creating a market" or "capturing share in a market"? Look at M&A activity — are strategic buyers entering? This reveals market maturity and competitive trajectory.

### Industry Standards and Infrastructure
Are industry groups approaching standardization? Look for working groups, published frameworks, API standardization efforts, integration standards. Check if major associations have published best practices. Standardization signals maturity — buyers can compare more easily, but switching costs may decrease.

### Regulatory and Compliance Landscape
What regulations affect buying decisions in this market? Search for recent regulatory changes, pending legislation, compliance requirements. In B2B, regulatory pressure often drives buying — either forcing adoption or creating barriers. What compliance certifications exist? Are they becoming table stakes?

### Time-Sensitive Signals (Critical)
What's happening RIGHT NOW that creates urgency or opportunity? Search for:
- Recent breaches, incidents, or failures that made news (e.g., a competitor's security breach)
- Regulatory deadlines approaching
- Technology shifts forcing migration (e.g., end-of-life announcements, platform changes)
- Economic pressures changing buying behavior
- Industry consolidation events

This is the most valuable section for GTM — it tells you what's breaking buyer inertia right now.

## Analysis Requirements

Write a detailed narrative (minimum 1000 words) weaving together these elements:

### Market Story
Where did this market come from? What problems led to its creation? How have solution approaches matured? What were the key inflection points? Don't list facts — tell the story.

### Current State
Paint a detailed picture of where the market sits today. Build a case through multiple pieces of evidence. How are buyers behaving? What are practitioners saying? How are vendors evolving? What do analysts observe? Use specific examples, quotes, and data points.

### How Market Stage Affects the ICP
This is critical. Connect market dynamics to buying behavior:
- Given where the market is, who's buying NOW vs. who will buy in 6-12 months?
- Are early adopters or early majority the current buyer?
- What does the market stage mean for messaging (educate vs. differentiate)?
- How does competitive density affect buyer decision processes?

### Future Trajectory
Based on current signals, where is this market headed in 12-24 months? What leading indicators do you see? What barriers must be overcome? What would accelerate or stall adoption?

## Sources to Search

- Industry analyst reports (Gartner, Forrester, IDC)
- Industry publications (Forbes, HBR, MIT Tech Review, industry-specific)
- Investment research (CB Insights, PitchBook, Crunchbase)
- Professional associations and standards bodies
- Conference proceedings and agendas
- Company earnings calls and investor presentations
- Industry expert blogs and thought leaders
- Academic research and curriculum
- Job posting trends
- News coverage of the market and major players

## Source Confidence Framework

Rate every major claim:

| Confidence | Criteria | Usage |
|------------|----------|-------|
| **High** | Multiple credible sources agree, recent data (<12 months), direct evidence | Claim with full confidence |
| **Medium** | Single credible source, older data (12-24 months), or inferred from related evidence | Claim with qualification |
| **Low** | Unverified, single weak source, >24 months old, or extrapolated | Do not claim — flag for validation |

## Output Format

1. **Market Narrative** — The full story: history, current state, trajectory. Minimum 1000 words of rich, sourced narrative. No bullet points — full paragraphs that weave evidence together.
2. **Time-Sensitive Signals** — What's happening NOW that creates urgency. List each signal with source and confidence.
3. **ICP Implications** — How market dynamics affect the specific buyer profile from Phase 1. Who's buying now vs. later? What does this mean for approach?
4. **Regulatory and Compliance Factors** — What compliance requirements drive or constrain buying.
5. **Confidence Summary** — What we can claim solidly, what needs qualification, what we couldn't find.
