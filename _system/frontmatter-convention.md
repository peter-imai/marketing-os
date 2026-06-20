---
type: system
governance: core-ref
scope: system
description: "Classification backbone — type vocabulary, field schema, governance fields, enforcement layers"
status: operator-reviewed
created: 195
last-updated: 666
updated-by: joint
---

# Document Frontmatter Convention

**Version:** v1.2 | **Created:** 2026-02-28 | **Status:** Active

## Revision Log

| Version | Date | What Changed | Trigger |
|---------|------|-------------|---------|
| v0.1 | 2026-02-28 | Initial design — schema, taxonomy, rollout tiers, consumer specs | Session 195 — T-11, Decision 060 |
| v0.2 | 2026-03-03 | Added `composition-brief` type, `intent-status` field. Composition workflow enforcement. | Session 210 — CF-35 composition failure diagnosis |
| v1.0 | 2026-04-03 | **Major revision.** Unified type vocabulary (17 canonical types in 3 tiers). Frontmatter becomes the classification backbone — every governed file declares its type, type maps to folder, system enforces the match. Supersedes D099 as primary classification authority. Ad-hoc type remap table. Tier A structured types get verifiable section requirements. | Session 515 — T-321, Decision 113 |
| v1.1 | 2026-04-05 | Added `governance` and `scope` fields. Moved from `blueprints/` to `_system/` — this is a system-level standard, not a reusable method. Added to core.md Core Documents. | Session 544 — T-340 |
| v1.2 | 2026-04-05 | Added `index` type. Principle shift: type classifies function, not location. Indexes live at the root of the folder they catalog regardless of that folder's primary type. Tier C exempt list tightened — "Backlogs" blanket exemption replaced with specific files (backlog.md, task-notes.md). | Session 551 — T-361, Decision 123 |
| v1.3 | 2026-04-05 | Added `log` type. Logs are structured context streams (not human-readable history) — companion files to a parent doc that record meaningful changes for downstream agent consumption. New `parent` field declares which doc a log records changes to. First specimen: `_system/core-log.md`. | Session 552 — T-380 |
| v1.4 | 2026-04-05 | **Added `marketing-pattern` type** (Tier B with required sections — first new type since `log`). Added the **atomic vs. domain framework** sub-classification within the `framework` type. Added **Marketing Pattern Required Sections** subsection (13 sections including Forces and Stamps). **Refined the methodology routing rule** per D124 (discipline-specific stays in practice area doc; named, attributed, cross-cutting methods earn their own marketing-pattern). **Stamps** introduced as the bidirectional-link compounding mechanism for marketing-patterns — see `frameworks/desire-paths.md`. **Forces** introduced as a structural concept — required section in marketing-pattern, required for new frameworks (existing frameworks: backlog retrofit T-384). New build rule cross-referenced: "Articulate Forces at Creation, Not Retrofitted" (`_system/build-rules.md`). | Session 553 — D124 |
| v1.5 | 2026-04-22 | **Added `campaign` type** (Tier B with required sections). Channel-bound, time-bound marketing executions with setup → run → end phases. Flat `.md` per campaign at `clients/{client}/campaigns/` (direct) or `clients/{client}/engagements/{eng}/campaigns/` (agency). Required frontmatter: `type`, `channel`, `status`, `started`/`ended` when applicable. Optional `motion`, `parent-pattern`, `data-sources`, `engagement`. 9 required body sections (Intent, Audience, Setup Checklist, Active Protocol, Live System State, Build Log, Learnings, Pattern Candidates, Open/Activation Checklist) + 3 optional (Traps & Escapes, Corrections, Meta). **Campaign vs. Operations boundary** articulated: `campaign` = time-bound with start/end; `operations` = ongoing running state. **`parent-pattern`** field extended from `operations`/`artifact` to `campaign` (bidirectional stamp link). **Rejected as types**: `experiment` (nests inside campaign), `initiative` (shape-emergent by definition, stays folder-only). **Pattern Candidates promotion rule**: default ≥2 runs confirm before promotion; N=1 escape hatch requires operator approval at `/done`. | Session 666 — D150 |

## Purpose

Frontmatter is the system's **classification backbone** — and, as of the S570 reframe, also its **stacking contract**. Every persistent governed document declares what it is via a `type` field from a controlled vocabulary. Each type maps to a folder. The system enforces the match. But classification is the floor, not the ceiling: the deeper mechanism is that **having a `type` means having a shape, and having a shape is what makes a document stackable**.

Frontmatter answers four questions:
- **What is this?** (`type`, `description`) — classification and routing
- **How fresh is this?** (`last-updated`, `created`) — temporal awareness
- **How much should I trust it?** (`status`, `updated-by`) — confidence calibration
- **What governs its structure?** (`convention`) — structural verification for Tier A types

### The Stacking Contract

Frontmatter isn't just classification — it's the mechanism that lets knowledge compound. Unstructured knowledge piles up; **structured knowledge stacks**. The `type` field is the stacking eligibility signal. The required-sections shape declared per type is the contract. Every typed artifact (`tool-profile`, `voice-kernel`, `workflow`, `marketing-pattern`, `criteria`, `skill`, `agent`, `framework`, and the rest) is a stackable component. Every stackable component follows the same three-verb lifecycle:

- **Set it up** — create the artifact per its type's convention (use the designated skill: `/connect-tool`, `/build-skill`, `/new-project`, etc.)
- **Wire it up** — catalog it into the system (index entries, cross-references, consumer wiring, auth manifest updates). Wire-up is what makes the component visible to the rest of the system.
- **Learn it up** — accumulate deeper knowledge, corrections, specializations from use over time. Learn-up is what makes the component compound.

All three verbs are required. Skip set-up and you have orphaned notes. Skip wire-up and you have hidden competence. Skip learn-up and you have dead capability. **This is why frontmatter matters** — it's not classification for its own sake, it's the contract that makes compounding possible.

Canonical home for the full stacking framework: pending at `frameworks/stacking.md` (T-405, atomic framework per D124, forces to be drafted from source material). Captured: `_system/core-log.md` 2026-04-06 S570 Shift entry. Related patterns: `resources/operator-patterns.md` Pattern #29 (Design for Stacking — umbrella) + Pattern #30 (Tool Fluency — specific instance) + OP74 curriculum entry (Wire up tool references).

### What Frontmatter Is NOT

Frontmatter is not a tagging system, a search index, or a knowledge graph. It is machine-readable metadata that classifies documents, calibrates the agent's confidence, and declares the shape that makes a document stackable. The system's routing (CLAUDE.md, commands, directory structure) handles discoverability. Frontmatter handles classification, trust, enforcement, and the stacking contract.

---

## The Schema

YAML frontmatter block at the top of the document, before any markdown content.

```yaml
---
type: core
description: "System-level governance — intention, core documents, active direction, watches"
governance: core-ref
scope: client
status: operator-reviewed
client: acme
created: 152
last-updated: 515
updated-by: joint
convention: _system/core-convention.md
related:
  - clients/acme/engagement-strategy.md
  - clients/acme/marketing-strategy.md
---
```

### Field Reference

| Field | Required | Type | Purpose |
|-------|----------|------|---------|
| `type` | Yes | Enum (see vocabulary) | Document classification. Determines folder home, staleness threshold, and structural requirements. |
| `description` | Yes | String (~80 chars) | One-line summary of document's purpose. Enables metadata-only scanning without reading the body. |
| `governance` | If applicable | Enum (see vocabulary) | Role in the governance hierarchy. Enables bidirectional linking — the doc knows its governance role, not just core.md knowing it points here. |
| `scope` | Recommended | Enum (see vocabulary) | Which scope level this document belongs to. Usually derivable from path but declared for explicit queryability. |
| `status` | Yes | Enum (see taxonomy) | Maturity level. Determines how much latitude the agent has with the content. |
| `client` | If client-specific | Enum (see taxonomy) | Which client this belongs to. Enables cross-client queries. |
| `created` | Yes | Session number | When the document was first created. Never changes. |
| `last-updated` | Yes | Session number | When the document was last *meaningfully* updated. Not every touch counts — adding a line to a table isn't an update. Rewriting a section based on new intelligence is. |
| `updated-by` | Yes | Enum (see taxonomy) | Who made the last meaningful update. Trust signal — agent-updated docs may need operator validation. |
| `convention` | Required for Tier A | Path string | Which blueprint governs this document's structure. When present, enables structural verification — the audit can check that required sections exist. |
| `related` | Optional | Array of paths | Links to related documents. Discovery safety net — even if folder placement isn't perfect, linked docs are findable. Agent follows links when loading a file for additional context. `/audit` checks for broken links. |
| `intent-status` | If composition workflow | Enum: `draft`, `approved` | Whether the document intent has been operator-reviewed. Writer checks for `approved` before composing. |
| `parent` | Required for `log` type | Path string | The doc this log records changes to. Enables reverse lookup ("which log records changes to this doc?") and parent-log pairing verification by `/audit`. |

### What "Meaningfully Updated" Means

The `last-updated` field tracks substantive changes, not mechanical ones.

**Counts as an update:** Rewriting a strategy section based on new intelligence. Adding a new hypothesis. Updating the engagement thesis after a stakeholder change. Integrating research findings.

**Does NOT count:** Fixing a typo. Reformatting a table. Adding frontmatter itself. Routine session-log-style updates to "Recent Sessions" sections.

The agent uses judgment. When in doubt, update the field — a false positive is less harmful than a false negative.

---

## Unified Type Vocabulary

**This is the authoritative classification for all persistent documents in the system.** 22 canonical types in three tiers. New values require a deliberate decision — they're added here first, then used in documents.

**Principle: type classifies function, not location.** Most types have a natural folder home because function and location align. But some types (like `index`) are defined by what the document *does*, not where it lives — an index at the root of any governed folder is still an index. When function and location conflict, function wins.

### Tier A — Structured Types

These types have **defined section templates**. The agent can validate structure, not just classify. Each has a `convention` field pointing to the blueprint that defines its required sections.

| Type | Home | Staleness | Convention | Required Sections |
|------|------|-----------|------------|-------------------|
| `core` | `{scope}/core.md` | 5 sessions | `_system/core-convention.md` | Intention, Core Documents, Active Direction, Watches |
| `engagement-strategy` | `{client}/engagement-strategy.md` | 15 sessions | `_system/client-context-architecture.md` | Per convention |
| `marketing-strategy` | `{client}/marketing-strategy.md` | 15 sessions | `_system/client-context-architecture.md` | Per convention |
| `data-state` | `{scope}/data/**/data-state.md` | 10 sessions | `_system/data-workspace-convention.md` | Index, pipeline status |
| `data-story` | `{scope}/data/**/data-story.md` | 10 sessions | `_system/data-workspace-convention.md` | Strategic frame, standing decisions, log |
| `voice-kernel` | `{client}/context/voice-kernel.md` | 40 sessions | `blueprints/voice-kernel-template.md` | Per template |
| `decision` | `_system/decisions/` | N/A (write-once) | — | Decision, Rationale, Alternatives Considered, What Would Make Us Revisit |

**Tier A enforcement:** When the `convention` field is present, `/audit` can verify that the required sections exist. This is the "structured vs. typed" distinction — `convention` is the marker.

### Tier B — Typed

These types have a **folder home and a purpose**, but no mandatory internal structure. The system validates placement (type ↔ folder), not sections.

| Type | Home | Staleness | Routing Test |
|------|------|-----------|-------------|
| `context` | `{client}/context/` | 30 sessions | "Situational, market, or product context that orients the agent — never operational docs" |
| `artifact` | `{client}/artifacts/` | N/A (durable) | "Durable doc that cements a conclusion, state, or deliverable" |
| `research` | `{client}/research/` | N/A (archival) | "Exploration that informed a decision" |
| `operations` | `{client}/operations/` | 20 sessions | "How we run things — working docs, SOPs, staging areas" |
| `blueprint` | `blueprints/` | 40 sessions | "Reusable method for recurring operations" |
| `workflow` | `blueprints/workflows/` | 40 sessions | "Operational map of a recurring activity — the loop, its economics, what compounds. Not a build method (→ blueprint), not execution steps (→ skill), not theory (→ framework)" |
| `framework` | `frameworks/` | 40 sessions | "Teaches how to THINK about a class of problem" |
| `system` | `_system/` | 20 sessions | "Defines what the system IS — architecture, rules, principles" |
| `resource` | `resources/` | N/A | "Knowledge from OUTSIDE the system — practitioner research, domain catalogs" |
| `transcript` | `resources/transcripts/` | N/A (archival) | "Ingested external transcript — video, podcast, meeting recording" |
| `criteria` | `blueprints/criteria/` | N/A (locked) | "Binary evaluation rubric — locked after validation" |
| `tool-profile` | `tools/[name]/profile.md` | 20 sessions | "Operational knowledge about an external tool — capabilities, costs, gotchas, usage examples. Knowledge, not code." |
| `index` | `{governed-folder}/index.md` or `{folder}/*-index.md` | N/A | "Catalog or navigation doc pointing to content it indexes — not content itself. Top-of-domain orientation file. Lives at the root of the folder it catalogs regardless of that folder's primary type." |
| `log` | `{parent-folder}/{parent-name}-log.md` | N/A | "Companion file to a parent doc — structured stream of meaningful changes (decisions, shifts, signals, dead ends, snapshots) recorded for downstream agent consumption. Reverse-chronological. Not a human-readable history doc. Lives next to its parent. Declares parent via `parent` field." |
| `marketing-pattern` | `blueprints/marketing-patterns/` | 60 sessions | "A named, attributed, opinionated, reusable marketing method captured as a pattern card. Cross-cutting across channels and engagements. Includes Forces (the tensions the pattern resolves) and Stamps (executions that link back to the pattern). For discipline-specific or single-channel tactics, use the practice area doc in `resources/marketing/` instead. See D124 for the routing rule." |
| `campaign` | `clients/{client}/campaigns/` (direct) or `clients/{client}/engagements/{eng}/campaigns/` (agency) | N/A (time-bound — campaigns end) | "A channel-bound, time-bound marketing execution with setup → run → end phases. Flat `.md` file per campaign. Required `channel:` field; optional `motion:` (outbound / nurture / broadcast / re-engagement) for sub-shape selection. Required Build Log section captures session-by-session activity — the mechanism that stops info-loss across sessions. Required Live System State section captures non-file state (external IDs, field IDs, schedules) required to re-enter the work. May declare `parent-pattern:` to stamp back to a marketing-pattern. Distinct from `operations`: `campaign` has a start and end; `operations` is ongoing running state. See Campaign Required Sections below." |

#### Framework Sub-Classification: Atomic vs. Domain

Frameworks come in two altitudes within the same `framework` type:

- **Domain frameworks** teach how to think about a *problem space* — Quality Engine, Voice Engineering, Experimentation (future), Statistics (future). Anchored to a specific discipline. Typically longer, often procedural, often with multi-dimensional structure.
- **Atomic frameworks** teach how to think about a *cross-cutting structural move* — Forces, Desire Paths, Intention (future), Pattern Language (future). Irreducible (cannot be decomposed further into smaller thinking tools) and applicable across any domain. Typically shorter, more conceptual, focused on a single primitive.

Both are `type: framework`, both live in `frameworks/`. The split is taxonomic — it helps route new thinking tools to the right altitude. The two altitudes serve different roles: domain frameworks are *consulted* when you're working in their domain; atomic frameworks are *applied* whenever the structural move they describe is needed.

The distinction is body-level, not enforced at the type level. There is no `framework-class` field. The classification surfaces in the framework's intent paragraph and in cross-references from this convention. As more atomic frameworks earn their keep (Forces, Desire Paths shipping in this same revision are the first deliberate specimens), this section may upgrade to a structural enforcement mechanism.

### Tier C — Exempt

These document categories have their **own lifecycle management** and are NOT frontmattered. Do not add frontmatter to these.

| Category | Location | Why Exempt |
|----------|----------|------------|
| `_inputs` files | `{client}/_inputs/` | Staging area — deleted after processing |
| Skill files (SKILL.md) | `.claude/skills/` | Own frontmatter schema (not missing — different) |
| Command files | `.claude/commands/` | Own frontmatter schema (allowed-tools, description, model) |
| Meeting transcripts | `{client}/meetings/transcripts/` | Ephemeral — processed by `/debrief` |
| `backlog.md`, `task-notes.md` | `{scope}/` | Working tables, mechanical maintenance via `/done`. Note: `*-index.md` is NOT exempt — it's `type: index`. |
| Session log | `_system/session-log.md` | Append-only, structure IS the metadata |

### Blueprints Anti-Patterns

These should NEVER go in `blueprints/` (root): client-specific docs (→ `clients/`), thinking tools (→ `frameworks/`), external knowledge (→ `resources/`), durable conclusion docs (→ `artifacts/`), strategy/voice docs (→ `context/`), evaluation data (→ `measure/`).

**Marketing methodology routing (D124, refines D112):**

D112 sent all marketing methodology to discipline practice area docs. D124 refines this for the specific case of attributed cross-channel methods:

- **Discipline-specific tactics** (single-channel mechanics, platform-specific patterns, channel-bound techniques) → discipline's practice area doc in `resources/marketing/` (e.g., `cold-email.md`, `outbound-gtm.md`). This is D112's rule, still load-bearing for the majority of marketing knowledge.
- **Named, attributed, opinionated, cross-cutting methods** (a real practitioner method that works across multiple channels with explicit forces, opinions, and procedure) → `blueprints/marketing-patterns/` as a `marketing-pattern`. The pattern lives once; practice area docs reference it from a Discovery Methods section.

**The distinction is scope:** discipline-bound stays with the discipline; cross-cutting earns its own pattern card. The signal a method has crossed the threshold: you can describe it without naming a specific channel and the description still makes sense.

---

## Type Lifecycle

The type vocabulary defines **what** each type is. This section defines **how** each type operates — how instances come into existence, what makes them good, and how they flow back into sessions that need them.

| Dimension | Question | Example (well-wired) |
|-----------|----------|---------------------|
| **Creation** | What prompts the system to create an instance? | `core` → `/new-project` scaffolds one automatically |
| **Structure** | What sections or shape make a good instance? | `core` → core-convention defines required sections |
| **Read path** | How does it get loaded into sessions that need it? | `core` → every command reads it at startup |
| **Write path** | What maintains the instance over time? | `engagement-strategy` → `/done` and `/debrief` route updates |

When adding a new type, define all four dimensions. A dimension can be "operator-initiated" or "on demand" — but it must be a deliberate design choice, not an omission.

### Tier A Lifecycle

| Type | Creation | Structure | Read Path | Write Path |
|------|----------|-----------|-----------|------------|
| `core` | `/new-project` | core-convention.md | Command startup | `/done` (suggests), operator approves |
| `engagement-strategy` | `/new-project` | client-context-architecture.md | Command startup (helper) | `/done`, `/debrief` |
| `marketing-strategy` | `/new-project` | client-context-architecture.md | Command startup (helper) | `/done`, `/debrief` |
| `data-state` | Convention guides when data work starts | data-workspace-convention.md | Command startup (data activity) | `/done` |
| `data-story` | Convention guides when data work starts | data-workspace-convention.md | On demand | `/done` |
| `voice-kernel` | `/new-project` | voice-kernel-template.md | `/compose` (layered: base → client) | `/done`, feedback loop |
| `decision` | `/architect` when design decisions made | Required sections in type definition | On demand; `/architect` revisit scans | `/architect` |

### Tier B Lifecycle

| Type | Creation | Structure | Read Path | Write Path |
|------|----------|-----------|-----------|------------|
| `context` | Operator-initiated | — | Command startup (core set); on demand | `/done`, `/debrief`, `/ingest` |
| `artifact` | Session work | — | On demand | Session work |
| `research` | Session work | — | On demand | Session work |
| `operations` | Operator-initiated | — | Command startup (activity-matched) | `/done` |
| `blueprint` | `/architect` | — | On demand | `/architect` |
| `workflow` | Routing table; `/done` prompt | **Required** (see below) | Routing table; activity-matched | `/done`, session work |
| `framework` | `/architect`; surfaced when a thinking tool or structural primitive earns naming | **Forces section required for new frameworks** (D124). Existing frameworks: backlog retrofit per T-384. Atomic vs. domain sub-classification declared in body, not enforced. | On demand; consulted when domain matches (`Load-Marketing-Domain-Expertise` for marketing-anchored frameworks); cross-referenced from Design Lenses, build rules, and skills | `/architect` |
| `system` | `/architect` | Varies by doc | On demand or command startup | `/architect`, `/done` |
| `resource` | `/ingest`, research sessions | — | Helper: Load-Marketing-Domain-Expertise (4/5 commands) | `/done`, `/ingest` |
| `transcript` | `/transcript-acquisition`, `/ingest` | — | On demand after ingest | `/ingest` |
| `criteria` | Build-Criteria helper | quality-engine.md framework | On demand (skill/workflow consumers) | Quality work |
| `tool-profile` | `/connect-tool` | tool-integration-convention | On demand | `/done`, `/connect-tool` |
| `index` | Operator-initiated when a domain earns navigation | — (no required sections; discovery, not verification) | Referenced from CLAUDE.md routing table; on demand | `/done`, `/ingest`, content-routing sessions |
| `log` | Stamped alongside parent doc, OR retroactively when a parent earns a log (Snapshot entry preserves state at stamp moment) | **Required** (see below) | Explicit on demand (v1) — no auto-load. Loaded when an agent or operator asks for historical context for the parent doc, or when future consumers (T-369 system annealing, T-370 content ideation) read log streams as input. Auto-load deferred until consumers prove value. | `/done` Step 4c (session-driven entries when parent touched), `/debrief` Step 8c (meeting-driven entries), manual append. Detection unified via `Check-For-Doc-Logs` helper. |
| `marketing-pattern` | `/architect` (via this convention's routing); `/ingest benchmark` promoting practitioner techniques to pattern candidates; recognized in session work when a method earns naming. Per the build rule "Articulate Forces at Creation," forces MUST be drafted at creation time, not retrofitted. | **Required** (see Marketing Pattern Required Sections below) | Catalog at `blueprints/marketing-patterns/index.md`; cross-referenced from practice area docs in `resources/marketing/`; loaded on demand by problem class | `/done` (stamp routing on execution — when a session executes a pattern, route a stamp back to the pattern file); `/architect` (pattern refinement based on accumulated stamps); session work |
| `campaign` | Launching a marketing campaign. Current path: manual scaffold from channel template in `blueprints/campaign-templates/{channel}.md` (email first; others as they earn the slot). Future: `/campaign-start` skill walks the elicitation and scaffolds the file (backlog T-459). Required `channel:` field at creation selects the Setup Checklist template. | **Required** (see Campaign Required Sections below) | Client/engagement command surfaces `status: planning` and `status: running` campaigns at session start; `ended` and `archived` load on demand. Rollout of this read path across client commands is backlog T-463 — until it lands, read path is "agent reads `campaigns/` when a session touches campaign work." | `/done` sweeps active campaigns and prompts a Build Log entry when the session touched one. Hook to enforce this is backlog T-460 (F-65 family — instruction-only pre-hook). Pattern Candidates promotion: default ≥2 runs confirm; N=1 escape hatch requires operator approval at `/done`. |

### Workflow Required Sections

Workflows are Tier B but have required sections derived from the type definition ("the loop, its economics, what compounds"):

1. **Pattern** — What this workflow does, why it exists, what compounds across iterations. The systemic context in one paragraph.
2. **The Loop** — Visual cycle diagram + numbered steps. Each step: Input, Output, What it produces. Tribal knowledge (gotchas, rate limits, edge cases) goes inline with the relevant step.
3. **Economics** — What it costs per run (time, money, credits, tokens). Enables ROI reasoning and cost-aware sequencing.

Reference specimens: `blueprints/workflows/corpus-analysis-pipeline.md`, `blueprints/workflows/substack-scraping-pipeline.md`.

### Log Required Sections

Logs are companion files to a parent doc, structured for agent consumption rather than human reading. They record what changed in the parent doc and why — not as prose, as queryable entries.

**Required frontmatter:** `parent` field declaring which doc this log records changes to.

**Naming:** `{parent-name}-log.md`, same folder as parent. Examples: `_system/core.md` → `_system/core-log.md`. `clients/acme/engagement-strategy.md` → `clients/acme/engagement-strategy-log.md`.

**Structure:**

1. **Header** — one-paragraph orientation: what this log records, where new entries go (top), pointer to entry types and format. Keep under 5 lines.
2. **Insertion sentinel** — immediately after the `---` horizontal rule that separates the header from entries, place this comment on its own line: `<!-- log-insert -->`. New entries are inserted on the line immediately after the sentinel. The sentinel is invisible in rendered markdown but provides a deterministic anchor for `Check-For-Doc-Logs` to find — no markdown parsing required. Same pattern as the corpus pipeline's `<!-- corpus-review-insert -->` in `_system/backlog.md`.
3. **Entries** — reverse-chronological (newest first). Entries are separated by a blank line — never a `---` horizontal rule (the only `---` in the file is the one between the header and the first entry). Each entry uses this format:

```
### YYYY-MM-DD · S{N} · {Type}
**What:** One-line fact.
**Why:** Reasoning (often references operator feedback, practitioner input, or session work).
**Implication:** Forward hook — what this changes or enables downstream.
```

**Snapshot exception:** Snapshot entries (used for retroactive bootstrap when stamping a log onto an existing parent doc) MAY include a body block under **What** that captures the parent doc's state at the snapshot moment. Snapshot is the only type permitted this carve-out — its purpose is to preserve content that the parent doc will lose as it evolves. Routine entry types (`Decision`, `Hypothesis`, `Signal`, `Shift`, `Dead end`) keep What/Why/Implication as strict one-liners.

**Entry type enum** (6 values):

| Type | When to use |
|------|-------------|
| `Decision` | A choice was made between alternatives. The choice itself is the entry. |
| `Hypothesis` | We're trying X, don't know yet whether it works. Becomes a `Decision` or `Dead end` later. |
| `Signal` | An external observation changed our understanding (operator feedback, practitioner pattern, incident, data point). |
| `Shift` | A direction change at the meta level — we used to think X, now we think Y. |
| `Dead end` | Tried X, didn't work, here's why. Prevents re-attempting. |
| `Snapshot` | One-time bootstrap entry capturing parent doc state at a point in time. Used when retroactively stamping an existing parent doc. |

**Pruning:** None in v1. Logs grow unbounded. Revisit if a log exceeds ~150 lines.

Reference specimen: `_system/core-log.md`.

### Marketing Pattern Required Sections

Marketing patterns are Tier B but have required sections derived from the type definition (an attributed, opinionated, reusable method with named tensions and a record of its uses):

1. **Attribution** — Author, origin, date captured. Top of doc, frontmatter or header. Required because patterns are practitioner-authored, not system-synthesized — provenance is part of the artifact.
2. **Intent** — One sentence. The move the pattern makes. Functions like the intention section in core.md — orients the reader before any detail.
3. **Context** — When to apply. Scale requirements, preconditions, channel scope, what has to be true for the pattern to make sense.
4. **Problem** — The fuzzy question the pattern makes answerable. What uncertainty does it reduce?
5. **Forces** — The competing values the pattern's solution resolves. **Required at creation time, not retrofitted** — the build rule "Articulate Forces at Creation, Not Retrofitted" applies. Each force names a specific value that pulls one direction and a specific value that pulls the other; the pattern's procedure is readable as a resolution. Pattern forces may inherit from a parent framework's domain forces (declared via the `parent-framework` field — future T-383). Canonical treatment: `frameworks/forces.md`.
6. **Core Opinions** — Epistemic commitments — the specific definitional moves that separate this pattern from generic advice. ("A situation is something that changes the copy" is a definitional commitment, not a procedure step.)
7. **Procedure** — Mechanical steps. Specific numbers, specific decisions, specific thresholds. The "how to actually do it" layer.
8. **What It Produces** — Outputs that drop out of applying it. What you walk away holding.
9. **Known Variants & Limits** — How practitioners adapt. Where the pattern breaks. What scale it stops working at. The honesty layer.
10. **What It Is NOT** — Sharpens identity against adjacent patterns. The negative space is doing real work — it's how you tell siblings apart.
11. **Related Patterns** — Family. Ancestors, siblings, children (specializations). Cross-references to other marketing-patterns when they exist.
12. **Known Uses / Stamps** — Bidirectional links to executions of this pattern. Each stamp is one line: `[S{n}, {client}] {one-sentence calibration} → {link to execution artifact}`. Starts empty on creation; accumulates over time. **The compounding mechanism** for patterns — see `frameworks/desire-paths.md` for the canonical treatment of stamps as desire-path infrastructure.
13. **Provenance** — Where the captured material came from. Source documents, sessions, ingestion history.

**Required frontmatter on the marketing-pattern itself:**

- `type: marketing-pattern`
- `description` — one-line classifier
- `attribution` — author/origin (e.g., "Author Name / Their Organization")
- `disciplines` — array of disciplines/channels the pattern applies to (cross-cutting nature must be explicit)
- `parent-framework` — optional. When present, declares which framework the pattern inherits domain-level forces from (e.g., `parent-framework: frameworks/experimentation.md` once that framework exists). Formalized via T-383. Omit the field entirely until a parent framework exists; do not write `null`.

**Bidirectional stamp link — `parent-pattern` field on execution artifacts:**

When a session executes a marketing-pattern in client work, the execution artifact (typically `type: operations`, sometimes `type: artifact`, in a client/engagement folder) declares the pattern it inherits from via:

- `parent-pattern: blueprints/marketing-patterns/{slug}.md` — path to the canonical pattern card

This is the inbound half of the bidirectional stamp link defined in `frameworks/desire-paths.md`. The outbound half is the entry in the pattern's "Known Uses / Stamps" section pointing back at the execution artifact. **Both must exist for the link to count.** `/audit` Area 12 verifies bidirectionality (per T-387). `/done` routes new stamps when a session executes a pattern (per T-386). Stamp format convention is canonicalized in T-388. Until those tasks ship, both halves are maintained manually at `/done`.

The `parent-pattern` field is canonical across `operations` and `artifact` types — any execution artifact that applies a marketing-pattern declares it the same way. The convention is forward-looking on purpose: by establishing the field now, future patterns and execution artifacts have a stable schema to write against, and the audit infrastructure has a stable field to verify.

Reference specimen:
- Marketing pattern: `blueprints/marketing-patterns/situation-variant-testing.md`

### Pattern Capture Protocol

When deliberately capturing a marketing pattern from source material (transcript, article, practitioner corpus), follow the **pattern capture protocol** (S553):

1. Open the engagement command where the source material is most active (e.g., `/marketing-os` for MKT1) — do NOT attempt from cold `/architect`.
2. Explicitly load source files into context at session start.
3. Draft **Forces first** — before procedure, before opinions. Each force must trace to a specific sentence in the source.
4. Run the **falsification test** on each force: can you cite material that pushes the opposite direction? If no, drop it.
5. Forces drafted from general LLM knowledge are the failure mode — refuse them.

Then fill the remaining 12 sections of the method-card structure. See `blueprints/marketing-patterns/situation-variant-testing.md` as the reference specimen.

### Campaign Required Sections

Campaigns are Tier B but have required sections derived from the type definition (a channel-bound, time-bound execution with setup → run → end phases where session-to-session info loss is the failure mode the type exists to prevent):

**Required frontmatter on the campaign:**

- `type: campaign`
- `description` — one-line classifier
- `channel` — e.g. `email`, `ads`, `social`. Required. Drives Setup Checklist template selection at scaffold time.
- `status` — `planning | running | paused | ended | archived`. Required.
- `started: YYYY-MM-DD` — required once `status ≠ planning`
- `ended: YYYY-MM-DD` — required once `status = ended`

**Optional frontmatter:**

- `motion` — `outbound | nurture | broadcast | re-engagement` (or other channel-appropriate sub-shape). Optional. Used when a single channel carries multiple campaign shapes with different Setup Checklists (e.g., email cold-outbound vs. email nurture sequence). Promote to required if Setup Checklist templates consistently branch by motion.
- `parent-pattern: blueprints/marketing-patterns/{slug}.md` — when the campaign executes a named marketing-pattern. Bidirectional stamp — the pattern's Known Uses / Stamps section accumulates a back-reference. Same field as on `operations` and `artifact` types (D124).
- `data-sources: [path, ...]` — list of data-project references this campaign draws from. Campaigns do NOT own data — they reference it. A data project can feed N campaigns or zero.
- `engagement: {name}` — agency case (engagements live under `clients/{agency}/engagements/{eng}/campaigns/`).

**Required body sections, in order (this order serves fresh-campaign flow — planning → setup → run → learn → hand off):**

1. **Intent** — One paragraph. What this campaign is trying to do and for whom. Orients the reader in one breath.
2. **Audience** — Who this targets. Link(s) into `data/` for the list(s). No list duplication in the campaign doc.
3. **Setup Checklist** — Channel-specific pre-launch discipline. Email: domain/deliverability, list hygiene, schedule, send limits, tracking setup, reply routing. Ads: account, budget, pixel/conversion tracking, creative pipeline. Social: account, voice calibration, schedule, amplification plan. Populated from channel template at scaffold time (`blueprints/campaign-templates/{channel}.md`). First template ships with email; others as they earn the slot.
4. **Active Protocol** — Current execution plan. What's running now, next action, stop criterion. This is the "if I open this campaign today, what am I supposed to do" answer.
5. **Live System State** — **Mandatory.** Non-file state required to re-enter the work. External-system IDs (e.g., Instantly campaign IDs, Google Ads account IDs), domain/subdomain allocations, tool-level field IDs (e.g., Clay column field IDs), segment vocabulary, schedule JSON. **Update discipline:** when a Build Log entry records activity that changed external state, update Live System State in the same pass. The section lies if it goes stale; lying is worse than empty. API keys and secrets do NOT live here — those live in `_system/credentials/` per D131.
6. **Build Log** — **Mandatory. Never skip.** Dated session entries. Shape: `### S{n} — YYYY-MM-DD`, then bullets covering activity, outcomes, decisions. Written at `/done` when the session touched the campaign. **Enforcement mechanism is backlog T-460** — instruction-only pre-hook, decays under pressure; honest risk named here and in D150. Interim defense: `/done` Pattern #35 Step 8 fresh-eyes sweep.
7. **Learnings** — Campaign-local findings, operator-categorized. Most learnings stay here until they earn promotion to Pattern Candidates, then to a marketing-pattern or discipline doc. Not every learning is a pattern; don't force promotion.
8. **Pattern Candidates** — Seeds for promotion to `blueprints/marketing-patterns/` or to a discipline practice area doc in `resources/marketing/`. **Promotion rule (refines `frameworks/desire-paths.md`):** default — promote at ≥2 runs confirm the pattern. **Escape hatch — promote at N=1** when a candidate is clearly load-bearing: solves a named problem, not speculative, and the agent flags it at `/done` for **operator approval**. Operator-gated to prevent premature pattern-making while preventing the opposite failure (deferring a real pattern forever and making the operator re-invent it). Deferring a real pattern is a bigger failure than promoting one that later proves thin; the latter is correctable via pattern deprecation, the former burns operator attention every time the problem recurs.
9. **Open / Activation Checklist** — Next-session hand-off state. What's waiting, what's blocked, what a cold-context agent needs to re-enter fast. The "I picked this up after a week away" answer.

**Optional sections (add when evidence earns it):**

- **Traps & Escapes** — Failure modes encountered + fixes. Pattern-candidate seed.
- **Corrections Received** — Operator-voice corrections during campaign execution. Feeder for voice-kernel and discipline-doc updates.
- **Meta — How We Worked** — Agent tendencies + what worked procedurally. Feeder for `resources/operator-patterns.md` and `resources/agent-conventions.md`.

**Filename convention:** short human-readable slug, no date prefix. Dates live in frontmatter. Examples: `aen-man-variants.md`, `q2-launch-nurture.md`.

**Flat file default.** Flat `.md` per campaign. If a campaign grows assets that need their own files (copy variants in separate files, multi-asset creative), revisit the convention. D150 explicitly preserves the option to fork to folder-per-campaign once evidence earns it.

**Campaign vs. Operations boundary.** `campaign` = time-bound with start/end dates, channel-scoped, setup → run → end. `operations` = ongoing running state of client work (CRM infrastructure, BDM ops, audit checklists) without a defined end. A running-state doc that suddenly grows an end date has become a campaign; a campaign that ends and archives stays in `campaigns/` as `status: archived`.

---

## Ad-Hoc Type Remap Table

Existing files with non-canonical type values should be remapped to canonical types. The `description` field captures what the old type conveyed.

| Ad-hoc value | → Canonical type | Rationale |
|-------------|-----------------|-----------|
| `positioning-foundation`, `buyer-psychology`, `buyer-brief`, `competitive-intelligence`, `market-intelligence`, `targeting-reference`, `product-foundation`, `product-overview`, `product-design` | `context` | These describe content topic, not document function. They orient the agent. |
| `deliverable`, `concept-doc` | `artifact` | Durable docs that cement conclusions. |
| `analysis`, `brainstorm-output`, `synthesis`, `marketing-knowledge` | `research` | Explorations and syntheses. |
| `process`, `plan`, `launch-plan`, `process-plan`, `planning` | `operations` | How we run things at the client level. **Sub-case — quarterly plans:** files with `type: plan` representing a quarterly cadence plan live at `clients/{client}/quarterly-plans/{YYYY-QN}/`, overriding the default `operations/` location. Produced via `blueprints/workflows/plan-elicitation-method.md`. |
| `methodology` | `operations` (client-applied) OR `marketing-pattern` (cross-cutting attributed) | Client-applied execution plans (e.g., "outbound testing plan for a specific client") are `operations`. Named cross-channel attributed methods are `marketing-pattern`. |
| `criteria-rubric` | `criteria` | Evaluation rubric — near-match. |
| `convention`, `design-decision` | `decision` | Architectural choices. |
| `voice-infrastructure`, `voice-guide` | `context` | Voice-adjacent context (not the kernel itself). |
| `podcast`, `podcast-transcript`, `newsletter` | `transcript` | Ingested external content. |
| `composition-brief` | (exempt — Tier C) | Consumed during composition workflow, not maintained. `intent-status` field remains available on any doc when needed. |

**Remap process:** Change `type` to canonical value. Update `description` to capture what the old type conveyed. Verify file is in the correct folder for the new type. If not, flag for operator review.

---

## Controlled Vocabularies

### `governance` — Governance Role

| Value | What It Means | Consumer |
|-------|-------------|----------|
| `core-ref` | Listed in a scope's core.md as a governing document. core.md is authoritative (operator-controlled, write-protected); this field enables reverse lookups — the doc knows it's governed. | `/done` (reverse governance check in coherency agent), `/audit` Area 12 (bidirectional verification), `/new-project` (scaffolds on new docs), structural map (display), conformance detection (T-285). |

### `scope` — System Scope Level

| Value | What It Means |
|-------|-------------|
| `system` | System-wide — applies across all clients. Home: `_system/`, `blueprints/`, `frameworks/`, `resources/`, `tools/`. |
| `client` | Client-specific — applies to one client. Home: `clients/[name]/`. |
| `engagement` | Engagement-specific — applies to one engagement within a client. Home: `clients/[name]/engagements/[name]/`. |

### `status` — Document Maturity

| Value | What It Means | Agent Latitude |
|-------|-------------|---------------|
| `working-notes` | Agent synthesis or early draft. Not validated by operator. | Low — treat as directional, surface uncertainties, flag assumptions. |
| `operator-reviewed` | Operator has read and corrected. Represents validated positions. | Medium — treat as current unless new information contradicts it. |
| `doctrine` | Operator-ratified. This IS the strategy. Changes require deliberate revision. | High — treat as ground truth. Don't second-guess without strong evidence. |

### `client` — Client Identifier

Slug matching a directory in `clients/`. Example values: `acme`, `your-agency`, `personal`. Add a new value when you onboard a client; the slug must match the folder name in `clients/`.

### `updated-by` — Last Updater

| Value | What It Means |
|-------|-------------|
| `operator` | The operator made or directed the last substantive change. Higher trust. |
| `agent` | The agent synthesized or updated the content independently. May need operator validation. |
| `joint` | Collaborative session — operator was actively involved in shaping the update. |

---

## Rollout Tiers

### Tier 1 — Active Maintenance (MUST stay current)

Documents where staleness directly degrades every downstream decision. The agent updates `last-updated` and `updated-by` at `/done` whenever it meaningfully modifies these docs.

**Includes all Tier A types:** `core`, `engagement-strategy`, `marketing-strategy`, `data-state`, `data-story`, `voice-kernel`.

### Tier 2 — Creation Stamp

Documents that benefit from metadata for orientation but don't require ongoing freshness tracking. Frontmatter is added when created or on major revision. `last-updated` updated only on major revision.

**Includes all Tier B types:** `context`, `artifact`, `research`, `operations`, `blueprint`, `workflow`, `framework`, `system`, `resource`, `transcript`, `criteria`, `tool-profile`, `index`, `log`, `marketing-pattern`, `campaign`.

### Not Frontmattered

All Tier C categories: `_inputs`, skill files, command files, meeting transcripts, `backlog.md`/`task-notes.md`, session log. These either have their own frontmatter schema (skills, commands) or genuinely don't fit frontmatter (ephemeral staging, append-only logs, mechanical working tables). Note: `*-index.md` files are NOT exempt — they're `type: index`.

---

## Consumers

### Primary: `Load-Client-Strategy-Context` Helper

Parses frontmatter on every strategy doc loaded at session startup. Behavior:

1. Parse `last-updated` and compare to current session number.
2. If gap exceeds the type's staleness threshold → flag: `"⚠️ [Doc] last updated Session {N} ({gap} sessions ago). Review before relying on it."`
3. Parse `status` → calibrate agent confidence.
4. Parse `updated-by` → if `agent` and status isn't `doctrine`, note: `"Last update was agent-synthesized, not operator-validated."`

### Secondary: `/audit` Area 12 — Document Classification Compliance

Periodic scan across all governed locations. Checks:
- Files in governed locations have frontmatter with canonical `type` value
- Type ↔ folder match
- Tier A files have required sections per their convention
- Coverage percentage by folder

### Tertiary: `/done` Check 8 — Frontmatter Compliance

Every session, for files created or meaningfully modified: verify frontmatter exists with canonical type value and correct folder placement.

---

## Maintenance

### At Session Shutdown (`/done`)

For Tier 1 docs the agent meaningfully updated this session:

1. Update `last-updated` to the current session number.
2. Update `updated-by` to reflect who drove the change.
3. Do NOT update frontmatter on docs that were only read, not changed.

### When Creating New Documents

All new documents in governed locations (clients/, _system/, blueprints/, frameworks/, resources/) MUST include frontmatter with:
- `type` from the canonical vocabulary
- `description` (one line)
- `status` (usually `working-notes` for new docs)
- `created` and `last-updated` set to current session number
- `updated-by`
- `client` if client-specific
- `convention` if Tier A type

### When Adding a New Client

Add the client identifier to the `client` taxonomy table in this blueprint.

### When Adding a New Document Type

If a new type of document emerges that doesn't fit existing values, add it to the vocabulary above. Include: tier classification, folder home, staleness threshold, routing test, and all four lifecycle dimensions (creation, structure, read path, write path). This is a deliberate decision — log to `_system/decisions/`.

---

## Enforcement

Five layers (defense in depth):

| Layer | Mechanism | What It Catches |
|-------|-----------|----------------|
| Creation templates | `/new-project`, `/build-skill`, skill templates produce correct frontmatter | Missing frontmatter on new docs |
| Helper parsing | `Load-Client-Strategy-Context` flags stale/unreviewed docs | Staleness and trust gaps at session startup |
| `/done` check 8 | Frontmatter compliance on modified files | Missing or non-canonical type, folder mismatch |
| Convention reference | This blueprint is the authoritative schema | Inconsistent or invented field values |
| `/audit` Area 12 | Periodic full scan of governed locations | Coverage gaps, structural violations, remap candidates |

---

## Anti-Patterns

| Anti-Pattern | What Goes Wrong | Prevention |
|---|---|---|
| **Mechanical timestamp updates** | Agent updates `last-updated` on every doc it touched, even trivial changes. Destroys the staleness signal. | "Meaningfully updated" definition above. |
| **Stale frontmatter, current content** | Doc content gets updated but frontmatter doesn't. Creates false staleness alerts. | `/done` enforcement. |
| **Frontmatter bloat** | Adding fields that have no consumer. | Every field must have a named consumer. No speculative metadata. |
| **Two sources of truth** | Inline markdown metadata coexists with frontmatter fields. They drift apart. | Frontmatter IS the metadata. Remove redundant inline markers. |
| **Inventing enum values** | Agent creates a new `type` without updating the vocabulary. | Controlled vocabulary defined here. New values require updating this blueprint + decision record. |
| **Frontmattering Tier C docs** | Adding frontmatter to exempt categories (backlogs, transcripts, _inputs). Adds overhead without benefit. | Tier C is explicitly exempt. |

---

## Integration

- **`_system/system-map.md`** — Structural inventory organized by frontmatter type
- **`CLAUDE.md`** — File Placement section requires frontmatter on governed files
- **`_system/client-context-architecture.md`** — strategy doc frontmatter requirements
- **`.claude/helpers.md#Load-Client-Strategy-Context`** — primary consumer (parses frontmatter, flags staleness)
- **`.claude/commands/done.md`** — maintains Tier 1 frontmatter at shutdown
- **`.claude/hooks/done-enforcement.sh`** — check 8 (frontmatter compliance)
- **`.claude/commands/audit.md`** — Area 12 (document classification compliance)
- **Decision 060** — original rationale and design choices
- **Decision 113** — vocabulary unification and classification backbone

---

*v1.0 — 2026-04-03 (Session 515). Major revision: unified 17-type vocabulary from T-321 taxonomy failure. Frontmatter becomes classification backbone. Incorporates Jacob Deedle's taxonomy governance methodology (adopted D060), document taxonomy (D099), and routing gap analysis (D112). Deferred: wiki linking, tags (no consumer — revisit when one exists).*
