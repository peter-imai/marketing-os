# Data Writeup / Presentation Doc — Format Playbook

For data-driven internal documents shared with colleagues or clients: pilot results, audit findings, analysis summaries. Working documents — the reader needs enough to make decisions, not a narrative journey through your methodology.

**Voice stack at this point:** Voice base (loaded) → client kernel (loaded) → THIS playbook.

---

## Document Architecture

**Results first. Process second.** The reader wants to know what happened before how it happened. Don't build toward the conclusion — lead with it.

Section order by reader priority:

1. **Opening** — what you did, what happened, your honest assessment. Three sentences max.
2. **Results table** — the data IS the headline. Put the table in the first section, not the fourth.
3. **Segment breakdown** — if the data breaks down meaningfully (by type, tier, vertical). Table preferred.
4. **The process** — how you got there. ONLY AFTER the reader knows the punchline. Calibrate technical depth to the audience.
5. **Edge cases** — anything the results alone don't capture (recovery opportunities, unresolved categories, surprises).
6. **Scale implications** — what the results mean at full scale (projected numbers, costs, time estimates).
7. **Client decisions** — frame as THEIR decisions, not your recommendations. "[Client] owns the answer."
8. **Next steps** — numbered, brief, action-oriented.
9. **Reference** — source materials at the bottom.

Cut any section that doesn't earn its place. This order is a priority hierarchy, not a checklist.

---

## Opening Formula

The opening is the most consequential structural choice. Pattern:

> I built [thing] and ran [scope] against it. The goal was [goal]. I think [honest assessment] — but want your thoughts.

Rules:
- First person, action verb, past tense ("I built," "We ran," "I analyzed")
- Scope stated concretely (1,000 records, 3 weeks, 50 accounts)
- Honest assessment including uncertainty or caveats
- Invitation for input — genuine, not performative

**Do NOT** open with background context. Open with what's new — the thing you did and what you found.

---

## Section Headers

Specific to THIS document, not generic category labels.

| Do | Don't |
|----|-------|
| "Red Recovery" | "Analysis" |
| "Yellow at Scale" | "Implications" |
| "Decisions for [Client]" | "Recommendations" |
| "Cost at 96K" | "Financial Summary" |
| "By record type" | "Detailed Breakdown" |
| "The Process" | "Methodology" |

The test: could this header appear in any report? If yes, make it specific to this one.

---

## Data Presentation

- **Tables for structured data.** Results, breakdowns, costs, comparisons.
- **Prose for interpretation.** What the numbers mean, why they matter, what to do.
- **Don't mix** — a table with embedded interpretation or prose restating table values wastes the reader's time.
- **Real examples inline** — show the data, don't just describe it.
- **Ranges for estimates, points for actuals:** "30-38% recoverable" vs. "61.8% green"
- **Label projection basis:** "I estimate 30-38% — based on the composition (95 wrong LinkedIn, 69 wrong domain, 46 no identifiers)"

---

## Length Budget

**Target: 1-2 pages for a pilot/audit writeup. 2-3 pages maximum for comprehensive analyses.**

If you're exceeding the target:
- Cut edge case narratives to one sentence each
- Move technical process detail to a reference appendix
- Condense projection math to results only (show the formula, not every step)
- Ask: "Does the reader need this to make their decision?"

---

## Tone Calibration

- **Assessment, not pitch.** "I think the approach is solid — but want your thoughts" not "the results validate our approach."
- **Gap acknowledgment.** "I didn't run this in the pilot" — state what you didn't do without apology.
- **Ownership boundaries.** "We can flag them, but [client] owns the answer" — clear on whose decision it is.
- **Confidence proportional to evidence.** Ranges where uncertain. Precise where measured. Never hedge what you know, never assert what you don't.
- **Close with substance, not filler.** End on the next concrete action, not "ready to move forward when you are."

---

## Composition Method (Two-Pass)

**Pass 1 — Structure lock.** Before writing any body content:
1. Write the opening line (action + result + assessment).
2. List section headers in reader-priority order (results before process).
3. Set target length (pages/words).
4. Verify: does the opening lead with what happened? Are results before methodology?

**Pass 2 — Draft.** Fill in each section. For each section:
- Does this earn its place? If not, cut it.
- Is the header specific to THIS content?
- Am I showing what I found, or explaining context the reader already knows?
- Am I within the length budget?
