# Phase 4: Buyer Personas — Subagent Research Prompt

> **When to load:** Phase 4 of market research. Sent to an Opus subagent along with all Phase 0-3 outputs.
> **Purpose:** Build rich, named buyer personas grounded in all prior research. These should feel like real people, not demographic profiles.

---

You are building buyer personas for a B2B company. You have access to web search — use it extensively. Your goal is to create 2-4 personas that feel like real people a salesperson would recognize, grounded in the market research you've been given.

## Context

You will receive:
1. An engagement brief (what the operator knows about buyers)
2. ICP analysis (who the target company looks like)
3. Market context (what's happening in the market)
4. Competitive landscape (who competitors are, the do-nothing segment, trigger events)

Use ALL of this. Each persona exists within this competitive reality — they're not abstract demographics, they're people dealing with specific competitors, workarounds, and market pressures.

## Research Approach

### Professional Background Research
- Search LinkedIn for titles matching the roles identified in the ICP
- Look at career progression patterns — where do these people come from?
- Identify common previous employers, educational backgrounds, certifications
- Review content they post/share — what topics do they engage with?
- Check conference speaker lists in the relevant industry

### Behavioral Pattern Research
- Search G2/Capterra reviews filtered by role — how do these people evaluate software?
- Look at Reddit, industry forums — what questions do they ask? What language do they use?
- Check industry communities and Slack groups — what do they discuss?
- Review job postings for this role — what skills, tools, and responsibilities are listed?

## Persona Components (Focus on What Changes Messaging)

For each persona, provide:

### Identity
- A realistic name and title
- Company type and size within the ICP
- Years of experience range
- Reporting structure (who they report to, who reports to them)
- 2-3 sentence narrative snapshot: "Meet Sarah, the VP of Security at a 500-person healthcare company who inherited a patchwork of tools from her predecessor..."

### Current Situation (Critical)
What is this person doing TODAY about the problem the client solves?
- Using a competitor's product? Which one, and how do they feel about it?
- Using manual workarounds? What specifically? (Name the spreadsheets, the processes)
- Ignoring the problem? Why — and what would make them stop ignoring it?
- This must connect to the competitive landscape from Phase 3.

### Pain and Motivation
- **What keeps them up at night?** The actual fear — not the product benefit restated as a problem. "I'm terrified we'll have an incident and I'll be the one who didn't act" is different from "needs better security tools."
- **What would make them forward an email to a colleague?** This is the virality test. Content that gets forwarded reaches buyers you can't directly target.
- **What would make them take a meeting?** The specific trigger or proof point.
- **What do they want to be true?** The aspiration — not what the product does, but what their professional life looks like if the problem were solved.

### Decision Process
- How do they evaluate solutions? (Formal RFP? Informal research? Peer recommendation?)
- Who else is involved in the decision? (Technical evaluator? Finance? Legal? End users?)
- What proof do they need? (Case studies? ROI calculator? Free trial? Reference calls?)
- What kills a deal? (Price? Complexity? Security concerns? Bad references? Timeline?)
- How long does the buying process typically take?

### Language and Communication
- What words do they use to describe their problems? (Use THEIR language, not vendor language)
- Where do they get information? (Specific publications, communities, events, peers)
- What content format do they prefer? (Short-form vs. long-form? Technical vs. strategic?)
- When are they most receptive? (Budget season? After an incident? New role?)

### Trigger Event Mapping
Connect to Phase 3's trigger events:
- Which Tier 1 triggers affect this persona most?
- Which Tier 2 triggers create openness?
- Which Tier 3 pressures are they experiencing?

## What NOT to Include

Cut anything that produces generic filler without changing how you'd reach this person:
- Detailed "legacy goals" or "mentorship activities" (rarely actionable)
- Exhaustive skill inventories (the ICP covers technical requirements)
- "Professional Motivation Map" with vague career aspirations
- Content consumption habits at a granular level (unless specific and surprising)

If a section wouldn't change the email you write, the ad you target, or the content you create — cut it.

## Source Confidence Framework

Rate every major claim:

| Confidence | Criteria | Usage |
|------------|----------|-------|
| **High** | Multiple credible sources agree, recent data (<12 months), direct evidence | Claim with full confidence |
| **Medium** | Single credible source, older data (12-24 months), or inferred | Claim with qualification |
| **Low** | Unverified, single weak source, >24 months old, or extrapolated | Do not claim — flag for validation |

## Output Format

For each persona (2-4 total):

```
## [Name], the [Title]

**Snapshot:** [2-3 sentence narrative introducing this person as a real human]

### Current Situation
[What they're doing today about this problem. Connected to competitive landscape.]

### Pain and Motivation
[What keeps them up at night. What would make them act. What they aspire to.]

### Decision Process
[How they buy. Who's involved. What proof they need. What kills deals.]

### Language
[The words they use. Where they get information. When they're receptive.]

### Trigger Events
[Which triggers from Phase 3 affect this persona and how.]

**Confidence:** [Summary of what's solid vs. inferred for this persona]
```

After all personas:
- **Priority Ranking** — Which persona is the primary buyer (highest priority to reach)? Why?
- **Role Mapping** — For each persona: decision-maker, influencer, evaluator, or blocker?
- **Confidence Summary** — What we know solidly, what's inferred, what needs validation from the client
