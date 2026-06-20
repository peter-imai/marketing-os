# Phase 1: ICP Discovery — Subagent Research Prompt

> **When to load:** Phase 1 of market research. Sent to an Opus subagent along with the Phase 0 engagement brief.
> **Purpose:** Build a quantified Ideal Customer Profile with evidence from multiple sources.

---

You are conducting deep market research to build an Ideal Customer Profile (ICP) for a B2B company. You have access to web search — use it extensively. Every claim must cite its source.

## Context

You will receive an engagement brief with what the operator already knows about this company's buyers. Use it as a starting point, not a constraint. Validate, extend, and challenge it with evidence.

## Research Instructions

Gather data from these sources in this order:

### Tier 1: Company Website
- Product pages: technical requirements, integration capabilities, what the product actually does
- Case studies: customer company sizes, industries, use cases, outcomes
- Customer logos/testimonials: research these companies on LinkedIn and Crunchbase
- Pricing pages: minimum deal sizes, package tiers, what each tier implies about buyer size
- Partner ecosystem: technology requirements, complementary tools
- Job postings: what roles they're hiring for reveals who they sell to

### Tier 2: Third-Party Sources
- G2 and Capterra reviews: company sizes and industries of reviewers, what they praise/complain about
- LinkedIn: company page, employee posts about customers, leadership posts about target market
- Crunchbase: funding, employee count, growth signals of the company AND its customers
- Press releases (PRNewswire, BusinessWire): customer wins, partnership announcements
- Industry analyst mentions (Gartner, Forrester, IDC): market categorization, competitive quadrants

### Tier 3: Technology Footprint
- BuiltWith or similar: technology stack patterns of known customers
- Integration marketplace: what tools their product connects to (reveals buyer tech stack)
- API documentation: technical sophistication required to implement

## Required ICP Components

For each component, provide specific numbers with evidence — not vague language.

### Company Size Parameters
- Annual revenue range (with evidence for the range)
- Employee count range (with evidence)
- Department sizes for target users
- Growth rate patterns of best-fit customers
- Minimum budget requirements

### Industry Details
- Primary industry verticals with estimated split (e.g., "40% healthcare, 25% financial services...")
- Sub-industries with specific use cases per sub-industry
- Regulatory requirements that drive buying (if applicable)
- Industry-specific pain points that make this product relevant

### Technical Requirements
- Required technology stack components (what must already be in place)
- Integration requirements (what they need to connect to)
- Data volume / scale indicators
- Security and compliance certifications needed
- IT team size and expertise needed to implement

### Budget and Purchase Authority
- Typical contract values (or range)
- Who holds the budget (title/role)
- Purchase approval process (single decision-maker vs. committee)
- Implementation budget beyond license cost
- ROI expectations and typical timeframe

### Team Structure
- Which departments are involved (users vs. buyers vs. influencers)
- Key stakeholder roles in the buying process
- Minimum team sizes for the product to make sense
- Reporting relationships that matter

### Use Case Specifics
- Primary problems solved (top 3-5)
- Business processes the product replaces or enhances
- Implementation complexity (self-serve vs. guided vs. professional services)
- Time to value (how long before they see results)
- Success metrics (what "working" looks like)

### Geographical Focus
- Primary markets (countries/regions)
- Language and localization requirements
- Regulatory considerations by geography

### Disqualifying Signals
- What makes a company NOT a fit? Be specific.
- Too small (below what threshold?)
- Too large (above what threshold?)
- Wrong tech stack (what's incompatible?)
- Wrong stage (too early? too mature?)
- Industry exclusions (who should they NOT target?)

## Source Confidence Framework

Rate every major claim:

| Confidence | Criteria | Usage |
|------------|----------|-------|
| **High** | Multiple credible sources agree, recent data (<12 months), direct evidence | Claim with full confidence |
| **Medium** | Single credible source, older data (12-24 months), or inferred from related evidence | Claim with qualification |
| **Low** | Unverified, single weak source, >24 months old, or extrapolated | Do not claim — flag for validation |

## Output Format

Structure your output as:

1. **Executive Summary** — 2-3 paragraphs describing the ideal customer in narrative form
2. **Detailed ICP Components** — Each section above with specific data points, sources, and confidence ratings
3. **Disqualifying Signals** — Clear "do not target" criteria
4. **Confidence and Gaps** — What we know solidly (high confidence), what's inferred (medium), and what we couldn't find (gaps that need client validation)

Use specific numbers. "Companies with 200-2000 employees in healthcare and financial services, using Salesforce and at least one BI tool, with $5M-$100M annual revenue" — not "mid-market companies in regulated industries."
