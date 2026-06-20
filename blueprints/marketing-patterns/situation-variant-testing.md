---
type: marketing-pattern
description: "Matrix testing for outbound message-market fit. Operationally-defined situations x message framings x volume per cell, with personalization withheld until the angle is validated."
attribution: "[Your source — practitioner name, firm, or engagement where you learned this]"
disciplines: [outbound-gtm, cold-email, linkedin-outbound, direct-mail, paid-creative]
status: specimen
---

<!--
  SPECIMEN PATTERN
  This is an example pattern card showing what a complete marketing pattern looks like.
  It's adapted from a real production pattern. Use it as your template when capturing
  methods from practitioners you learn from. Replace the content with your own method,
  but keep all 13 sections — each one is load-bearing.
-->

# Situation x Variant Testing

**Attributed to:** [Practitioner name / firm]. Adapt this attribution to the real source where you learned this method. Every pattern has a lineage — name it.

---

## Intent

Reduce uncertainty about which message angles land with which buyer realities, before spending real money on personalization or scale.

## Context

Apply this pattern when:

- You're running structured outbound to a defined market and don't yet know which angles work
- You have enough addressable list (~5,000+ contacts) to support matrix testing without exhausting the TAM
- You can push volume through test cells and measure replies (or equivalent conversion signal) per cell
- You can articulate at least 2-3 candidate "situations" — operationally-defined buyer realities that would call for different messaging
- You can articulate at least 4-5 candidate "framings" — fundamentally different angles/positions the same product can be sold from

The pattern applies across channels where you can push volume through test cells: cold email is the canonical case, but the structure works unchanged for LinkedIn outbound, cold calling scripts, direct mail, and paid ad creative. What changes across channels is the specific decision thresholds — but the cell structure, the situation definition, and the personalization-last principle hold.

**When NOT to apply:**
- Small TAM where cell-volume requirements would burn through the entire list (under ~1,000 contacts per situation)
- Single dominant situation where there's only one operationally meaningful buyer reality (degenerates into normal A/B variant testing)
- You already have a validated angle from a prior engagement and the marginal value of testing alternatives is low
- High-touch channels where each contact requires significant per-prospect effort (deep ABM, founder-led enterprise sales)

## Problem

The fuzzy question this pattern makes answerable: **Which message frames actually resonate with which buyer realities, and which ones are just our hypotheses about what should work?**

Outbound campaign design without this pattern operates on instinct: a senior practitioner picks the angle they think will land, writes one variant well, sends it broadly, and learns one thing (it worked, or it didn't). The learning is binary, the comparison frame is missing, and there's no mechanism to discover that the angle that worked best wasn't the one the practitioner picked. Personalization typically gets layered on top to compensate for uncertainty about the angle — which is expensive and doesn't fix the angle problem.

The pattern reframes the question. Instead of "is my angle right?" it asks "which combinations of buyer realities and message frames produce reads I can act on?" Matrix structure forces explicit comparison; volume per cell makes the read trustworthy; the personalization-last rule stops the practitioner from saving a losing angle with expensive labor.

## Forces

The competing values this pattern's solution resolves. Each force pulls in a specific direction; the pattern's procedure is readable as a resolution of the tensions.

**Force 1: Enough signal to trust the read, as few emails as possible spent getting it.**

Pull one way: statistical rigor would demand thousands of emails per cell before you call a winner. Pull the other way: you have a finite list, finite time, and every email spent learning is an email not spent scaling something that already works. The ~500-per-cell floor is a specific resolution — above 500, the signal is trustable for decision-making (not journal-grade, but trustable enough to pick a winner and scale); below 500, you're reading noise. 500 isn't statistically ideal; it's the floor where the trade stops hurting more than it helps.

**Force 2: Cost of applying personalization vs. cost of finding the angle without it.**

Personalization is expensive per email — research time, custom signals, AI generation cost, per-prospect effort. Finding the winning angle is cheap per email — same template, volume, let the data pick. If you invert the order (personalize first, find angle second), you spend the expensive resource on angles that haven't been validated. The tension is real because practitioners under pressure feel like personalization is the work; the pattern says the angle is the work and personalization is the amplifier you apply afterward on what already works.

**Force 3: What counts as a segment worth testing separately.**

Business intuition pushes toward more segments (industry, company size, region, title, technology stack) because finer targeting feels more sophisticated. But testing a "segment" separately only pays off if the copy you'd actually write is different for that group. If two "segments" get the same email, you're not running two tests — you're running one test with extra filtering overhead. The epistemic commitment ("a situation is something that changes the copy") resolves this: the segmentation cost is only justified when the segment forces copy divergence. This force is what stops the matrix from exploding into ungovernable cell counts.

## Core Opinions

The epistemic commitments — the specific definitional moves that separate this pattern from generic outbound advice.

**1. A situation is something that changes the copy.** If the difference between two groups doesn't force a different email, it's not a situation — it's a filter variable, an enrichment signal, or a demographic. Demographics ("manufacturing companies with 100-500 employees") are not situations. Operational realities ("3-person IT team giving out local admin because they can't manage anything else") are situations because they force a specific email you wouldn't write to anyone else.

**2. Volume beats intuition, with a specific floor.** ~500 emails per cell is the minimum signal threshold for decision-making. The number itself isn't precious — it's a forcing function that says "be honest about what you actually know." Below 500, you're tempted to read noise as signal.

**3. Title tier is a language split, not a separate axis.** The same problem needs different language depending on who receives it (a manager cares about operational pain; a director cares about strategic positioning). Treating title as a full axis would explode the matrix. The resolution: it's a sub-split inside each variant, weighted to the actual title distribution in the data.

**4. Decision thresholds are baked into the method.** 1 positive reply per 100 emails sent = "scale it." 1:200 = "maybe, in harder verticals." These aren't industry benchmarks — they're action triggers built into the pattern so you can decide on ambiguous results without stalling.

**5. Personalization is the last layer, not the first.** You don't try to save a losing angle with better research. You find the angle first via volume, then add AI/custom signals on top of what already works. This inverts the sequence most practitioners default to under pressure.

## Procedure

The mechanical steps. Specific numbers, specific decisions.

1. **Define situation buckets per vertical.** Group prospects by their operational reality, not demographics. Each situation must pass the test: "Describe what's different about this group in one sentence; does that sentence change the email?" Yes = situation. No = filter variable.

2. **Write 4-5 framings per situation.** Each framing positions the same product through a fundamentally different buyer motivation: compliance pressure, liability/risk, revenue opportunity, competitive differentiation, operational efficiency. These are not A/B tests on wording — they're different reasons-to-care.

3. **Split each framing by title tier as a language sub-axis.** Same problem, different register for staff vs. directors. Distribution reflects actual title mix in your data, not a clean 50/50.

4. **Send ~500 emails per cell.** Math: 3 situations x 5 framings = 15 cells x 500 = 7,500 emails per vertical test. Below 500/cell you're reading noise; below 200 you have nothing. Adjust upward for hard verticals.

5. **Evaluate winners against thresholds.** Primary metric: positive reply rate. **Scale threshold:** 1:100 positive reply for trigger-based situations; 1:200 for evergreen situations. **Kill threshold:** below 1:200 after 200 sends. Track by framing x situation x title tier — the intersection tells you what works for whom.

6. **Scale winners. Then layer personalization.** Variants that clear the scale threshold get more volume. Only after identifying winning angles do you add AI personalization, deeper research, or per-prospect customization. Personalization on a losing angle is wasted effort.

7. **Calibrate thresholds for vertical hardness.** In hard verticals (cybersecurity, enterprise, highly regulated industries), all thresholds adjust downward. A 1% positive reply rate that's marginal in a friendly vertical may be excellent in a hard one. The pattern's structure stays; the numbers shift.

## What It Produces

When you apply this pattern, you walk away with:

- **A test matrix** — structured plan of situations x framings x title splits with cell-volume targets
- **A per-cell measurement model** — framing x situation x title tier as the unit of analysis, not just "variant performance"
- **A scaling decision** — which cells get more volume, justified by data not instinct
- **A personalization roadmap** — which winning angles deserve AI/custom signals layered on, in priority order
- **Transferable learning** — once you know "problem framing X beats problem framing Y for situation Z," that's an asset you carry to the next engagement
- **Honest quantification of vertical difficulty** — running the matrix in a hard vertical reveals the actual achievable reply rates, which calibrates expectations for everyone

## Known Variants & Limits

**Adaptations practitioners use:**

- **Small TAM:** Reduce to 200-300 per cell, accept noisier signal. Below 200/cell the pattern degenerates — you're hoping rather than learning.
- **Single dominant situation:** Skip situation bucketing; test more framings against the one situation instead.
- **Known winning angle from another engagement:** Start with the known winner as one brick, test fewer alternatives, save volume for scaling.
- **TAM too small for full matrix:** The pattern doesn't fit. Use a different testing approach (A/B at higher volume per cell, or n-of-1 deep personalization for tier-1 accounts).
- **Vertical-specific calibration:** Hard verticals require lower thresholds. The pattern's structure holds; the numbers shift.

**Where the pattern breaks:**

- **High-touch channels (founder-led ABM, six-figure deals).** Per-contact cost is so high that 500 contacts through 15 cells is economically irrational. Reach for deep research instead.
- **Markets with no observable situations.** If you can't articulate buyer realities that change the copy, the pattern can't run. Fix the upstream segmentation work first.
- **Channels without per-contact reply signal.** If you can't measure positive replies (or equivalent) at the cell level, the decision thresholds don't fire.
- **Engagements where speed-to-pipeline matters more than learning.** If you need revenue this week and learning compounds over months, the pattern is the wrong shape.

## What It Is NOT

- **Not a copywriting framework.** The pattern tells you which variants to test, not how to write them.
- **Not a positioning method.** It assumes you already have hypotheses worth testing — it doesn't help you generate them.
- **Not an A/B testing methodology.** A/B is one axis, two cells, statistical purity. This is matrix testing, pragmatic decision thresholds, operational feasibility.
- **Not a campaign playbook.** It's cross-campaign — applied to any structured outbound.
- **Not channel-specific.** The structure works across channels. The channel determines the volume math and threshold calibration; the structure is invariant.
- **Not a substitute for qualitative discovery.** It surfaces what works at scale. It doesn't tell you why a cell won — you still need conversations and interviews.
- **Not a one-time exercise.** A test produces winners; winners become hypotheses for the next test.

## Related Patterns

**Ancestors (older methods this descends from):**
- **Bucket testing** (classical email marketing) — closest ancestor. This pattern is a more opinionated descendant with explicit forces and a tighter cell structure.
- **Multivariate testing** (web optimization) — same matrix idea, different substrate.
- **Quasi-experimental design** (social sciences) — shared DNA: matrix structure, controlled volume, pragmatic thresholds.

**Cousins (similar goal, different mechanism):**
- **Multi-armed bandit / contextual bandit testing** — same goal (identify winners) but with algorithmic reallocation instead of fixed cells. This pattern is the human-operated version.
- **Lean Startup build-measure-learn** — same philosophy but at a different altitude. Lean Startup is a mindset; this pattern is a concrete procedure within it.

**Parents (upstream methods this pattern consumes):**
- **Situation mining / buyer research** — whatever upstream discovery method produces your situation catalog, this pattern's matrix operates on its output. Mine first, test second.

## Known Uses / Stamps

Bidirectional links to executions of this pattern. Each stamp records the engagement, calibration choices, and a link to the execution artifact. This section starts empty and accumulates over time -- it's the compounding mechanism.

*(No stamps yet. When you execute this pattern, add a one-line entry here: engagement name, calibration notes, link to your execution artifact.)*

## Provenance

This specimen pattern is adapted from a real production pattern used in outbound GTM work. The method was originally developed for matrix-testing cold email angles across multiple buyer situations, then generalized as a cross-channel testing methodology.

When you capture your own patterns, use this Provenance section to document where the material came from -- which practitioner, which engagement, which source material. Source integrity matters because the Forces section must trace to real practitioner experience, not general knowledge.

---

*Specimen pattern included with the Marketing OS starter kit. Replace the attribution and provenance with your own sources when you adapt this for real use. The structure (all 13 sections) is the constant; the content is yours to build.*
