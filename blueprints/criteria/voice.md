---
type: criteria-rubric
description: "8-criterion voice evaluation rubric for composition — continuous self-audit instrument for /compose"
spectrum-position: self-audit
consumers:
  - "/compose skill (self-audit step after drafting)"
  - "Voice kernel tuning (correction feedback loop)"
  - "Format playbook development"
status: working-draft
convention: blueprints/frontmatter-convention.md
---

# Voice Evaluation Rubric

**Purpose:** Evaluate whether composed output sounds like the operator wrote it — not whether the content is strategically correct, structurally complete, or factually accurate. This rubric measures voice quality: editorial judgment, register, specificity, and discipline.

**Input:** Any composed external content (landing page section, email, data writeup, meeting summary, LinkedIn post, newsletter section).

**Output:** Score from 8-40 + per-criterion breakdown with reasoning. The pattern of scores identifies which voice components need adjustment.

**When to use:** After every `/compose` draft, before operator review. The agent runs the self-audit and reports scores with reasoning. The operator can override any score. Corrections feed back into the voice kernel.

---

## Pre-Score Gate

Check before scoring. If this fails, fix it before evaluating voice quality.

**Client sensitivity.** Does any passage frame client work in a way that could make a client uncomfortable? Are real client details properly anonymized — conceptually, not just by changing numbers?

- **Pass:** Safe to proceed with voice scoring.
- **Fail:** Fix the sensitivity issue first. Voice quality is irrelevant if the content damages a relationship.

---

## Criteria

Score each criterion 1-5. Definitions are grounded in the voice kernel (`workspaces/[workspace]/context/voice-kernel.md`) and voice base (`_system/voice-base.md`). Reference the kernel's decision rules and transformation examples for calibration.

### 1. Consequence-First Opening

*Anchor: Decision Rule 1 — "Lead with consequence, not principle."*

Does the piece open with what matters (result, impact, outcome) rather than context, principle, or setup?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Opens with pure context, background, or principle. Reader waits 3+ sentences to learn why this matters. | "In marketing, systems thinking has become increasingly important..." |
| 2 | Opens with context but the second sentence contains a consequence. Setup-heavy but not purely abstract. | "We ran the pilot last week. The results validated our approach — 66% of records are campaign-ready." |
| 3 | First paragraph leads with consequence but wraps it in setup or qualification. The payoff is there — it's not leading. | "After working with multiple clients, I noticed that email response data actually feeds content ideation." |
| 4 | First sentence contains a consequence, with a clause of setup attached. Close to leading with impact. | "I built a cleanup pipeline and ran our 1,000-row test set against it — 66% green, ready for campaigns." |
| 5 | First sentence IS the consequence. No warmup, no qualification. | "66% of the CRM is campaign-ready. Here's how we got there." |

**Format note:** For meeting recaps and reply emails, score from the first *substantive* line (after greeting), not the literal first sentence.

### 2. Peer Register

*Anchor: Editorial Posture (Do/Don't pairs) + Decision Rule 3.*

Does the writing treat the reader as a technically competent peer, or does it lecture, explain basics, or diagnose the reader's problems?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Lectures down, explains concepts the audience already understands, or diagnoses the reader's problems. | "Your marketing is broken." "Let me explain how loops work." |
| 2 | Mostly explanatory, with peer moments. Over-explains in multiple spots. | Explains what a tool is to the team that uses it daily. |
| 3 | Peer most of the time but slips into teaching mode or hedging in spots. ~70-80% peer. | Mixed register — mostly peer, but 2-3 parenthetical explanations the audience doesn't need. |
| 4 | Consistent peer register with one minor slip. ~90%+ peer. | One unnecessary clarification in an otherwise clean peer-to-peer report. |
| 5 | Pure peer throughout. No condescension, no hedging, no unsolicited diagnosis. | Consistent register — every sentence assumes the reader is smart and time-poor. |

### 3. Anti-Pattern Clean

*Anchor: Language Constraints (Banned Words + Banned Patterns).*

Is the output free of banned words, banned patterns, and AI-isms?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Pervasive or systemic violations. Multiple banned words AND banned patterns. | "Unlock your potential to streamline and optimize..." — systemic. |
| 2 | 2-3 clear violations. | "Optimize" in one section, "leverage" in another. |
| 3 | Exactly 1 clear violation. Isolated slip, not systemic. | Single "optimize" in an otherwise clean piece. |
| 4 | Zero banned words or patterns, but one debatable near-miss. | Borderline marketing language, not on the banned list. |
| 5 | Clean. Zero banned words, zero banned patterns, zero AI-isms. | Could not point to a single violation or near-miss. |

### 4. Specificity Anchored

*Anchor: Decision Rule 4 — "Real specifics only" + Decision Rule 6 — "Plain language outcomes."*

Are claims grounded in real numbers, named tools, and concrete scenarios — or generic, vague, or fabricated?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Generic claims throughout. No real numbers, named tools, or concrete scenarios. | "Our solution provides comprehensive marketing automation capabilities." |
| 2 | Occasional specifics but most claims are vague. | Names one tool but everything else is "significant improvements." |
| 3 | Mix of specific and vague. Some sections grounded, others rely on generalizations. | Names tools but also says "dramatically improve your results." |
| 4 | Nearly every claim grounded. One or two soft claims that could be tighter. | All but one paragraph is fully specific. |
| 5 | Every claim grounded. Real numbers from real work, named tools, concrete scenarios. | "300+ sessions. 3 clients. One command replaces a weekly analyst task." |

**Hard rule:** If ANY specific number is fabricated, this criterion scores 1 regardless of other specifics.

### 5. No Template Activation

*Anchor: Decision Rule 2 — "Show, don't argue" + Banned Patterns.*

Does the piece feel structurally organic, or has the model fallen into a generic content pattern?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Pure template. The structure came from training data, not from this content. | Could swap the content for any topic and the structure wouldn't change. |
| 2 | Heavy template scaffolding. Content may be original but the architecture is generic. | "What we did / Results / Next steps" — status-update brief template. |
| 3 | Mix — some sections feel organic, others feel templated. | Headers are fresh but one section reads like a blog post template. |
| 4 | Structure mostly follows the argument's logic. One minor imported convention. | Recognizable closing pattern, but earned by the content. |
| 5 | Structure feels entirely organic to the content. | Could not identify which "template" this was based on — because it wasn't. |

### 6. Sharpness Calibrated

*Anchor: Decision Rule 7 — "When excited, more detail not volume" + Decision Rule 8 — "Acknowledge complexity honestly."*

Is the editorial confidence appropriate to the evidence?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Severely miscalibrated — everything hedged, or everything hyperbolic. | "This REVOLUTIONARY approach..." or "This might possibly help..." |
| 2 | Noticeably miscalibrated in multiple spots. | Two paragraphs overblown, one unnecessarily hedged. |
| 3 | Mostly calibrated but inconsistent. 1-2 spots where confidence doesn't match evidence. | Strong opening, but the middle section pads with "incredible" and "amazing." |
| 4 | Well-calibrated throughout with one minor slip. | One "approximately" where the number is actually precise. |
| 5 | Confidence matches evidence precisely throughout. Energy comes from specificity, not volume. | "It's not perfect, but it is self-auditing." |

### 7. First-Person Practitioner

*Anchor: Editorial Posture — "First-person practitioner showing real work" + Decision Rule 2.*

Does the writing have the energy of someone doing the work, or does it read as produced about the work?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Reads as produced FOR the operator, not BY them. No sense that the author did the work. | "The system enables users to..." — who is talking? |
| 2 | First-person framing but the energy is reporting, not demonstrating. | "We built a system that validates records" — first person but no demonstration. |
| 3 | First-person with some practitioner energy. Mixed — 50-50 demonstrating vs. documenting. | Some "look at this" moments, but other sections read as documentation. |
| 4 | Consistent practitioner energy with one section dipping into explanation mode. | 90% practitioner — one section reads as process documentation. |
| 5 | "Look at this thing" energy throughout. Shows the work, doesn't just describe it. | "I prepped for a client meeting in five minutes — not a demo, a real meeting." |

### 8. Omission Discipline

*Anchor: Decision Rule 5 — "Omit what doesn't earn its place."*

Is every paragraph necessary? Could sections be cut without losing meaning?

| Score | Definition | Signal |
|-------|-----------|--------|
| 1 | Multiple paragraphs could be deleted without losing meaning. | First two paragraphs are setup that could be deleted entirely. |
| 2 | Several sections feel loose. 2-3 paragraphs are filler or could be condensed. | Three paragraphs that each make a point already made elsewhere. |
| 3 | Mostly tight but 1-2 sections feel like filler. ~85-90% earned. | 90% earned, but one paragraph repeats a point already made. |
| 4 | Tight throughout. One sentence or clause that could be trimmed. | Almost perfectly dense — one sentence is slightly redundant. |
| 5 | Every paragraph earns its place. Could not cut a section without losing meaning. | Removing any paragraph would leave a visible gap. |

---

## Scoring

**Total:** Sum of all 8 criteria. Range: 8-40.

**Per-criterion reasoning is required.** Each score must include a brief explanation with specific passages cited.

The per-criterion breakdown matters more than the total. The pattern tells you what to adjust:

| Weak criteria | Likely adjustment target |
|--------------|--------------------------|
| 1 (Consequence-first) or 5 (Template activation) | Kernel Decision Rules 1-2. Consider two-pass workflow where Pass 1 locks opening and structure. |
| 2 (Peer register) or 7 (First-person practitioner) | Kernel Editorial Posture section. The do/don't pairs may need sharpening. |
| 3 (Anti-pattern clean) | Strengthen the voice base's Language Constraints or add format-level negative constraints. |
| 4 (Specificity anchored) | Often a content problem, not a voice problem. Check source material before blaming the kernel. |
| 6 (Sharpness calibrated) | Hardest to fix mechanically. May require operator correction examples. |
| 8 (Omission discipline) | Two-pass helps — review pass checks for cuttable paragraphs. Format playbook can set a word budget. |

---

## Calibration Examples

### High Score (Target: 36-40)

> Less experienced marketers with better systems are outproducing more talented people without them.
>
> I prepped for a client meeting in five minutes. Not a demo — a real meeting, real client, real stakes. The system loaded the client's strategy, open questions, what I committed to last time. I went in sharp. Meeting happened. Dropped the transcript. Three minutes later: intelligence doc updated, strategy doc updated, follow-up email drafted in my voice and pushed to Gmail.
>
> That's one meeting. I have 5-8 a week. And the debrief at meeting 10 catches strategic implications that meeting 1's debrief couldn't — because it has 9 meetings of accumulated context.

**Scores:** C1: 5, C2: 5, C3: 5, C4: 5, C5: 5, C6: 5, C7: 5, C8: 5. **Total: 40.**

### Low Score (Target: 8-14)

> In today's rapidly evolving marketing landscape, leveraging AI tools has become essential for businesses looking to optimize their marketing operations. Our comprehensive system transforms how marketing teams approach their daily workflows, unlocking new levels of productivity and streamlining complex processes.

**Scores:** C1: 1, C2: 1, C3: 1 (6 violations), C4: 1, C5: 1, C6: 1, C7: 1, C8: 1. **Total: 8.**

### Mid-Range Score (Target: 22-28)

> I run marketing for three clients simultaneously. Each one gets the same process — email campaigns, meeting debriefs, content production — but with their own context and voice loaded.
>
> The system helps ensure consistency across clients while maintaining the flexibility needed to adapt to each client's unique requirements. It's an incredibly powerful way to scale your marketing operations without sacrificing quality or personalization.
>
> Last week I ran 6 meetings across two clients. Each debrief took about 3 minutes. The follow-up emails drafted themselves in the right voice for each client.

**Scores:** C1: 3, C2: 3, C3: 3, C4: 3, C5: 3, C6: 3, C7: 3, C8: 3. **Total: 24.**
