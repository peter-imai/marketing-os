---
type: system
governance: core-ref
scope: system
description: "Classification backbone — the type vocabulary, field schema, and governance fields for governed documents"
status: operator-reviewed
---

# Document Frontmatter Convention

Every persistent document in a governed location declares **what it is** via a `type` field in YAML frontmatter. The type determines the document's folder home, how fast it goes stale, and what structure (if any) it must have.

Why it matters: a typed document has a *shape*, and a shape is what lets knowledge **stack** instead of pile up. Unstructured notes accumulate; structured documents compound. Frontmatter is that contract.

Governed locations: `workspaces/`, `_system/`, `blueprints/`, `resources/`, `tools/`. (Skills and commands have their own frontmatter schema — see Tier C.)

---

## The Schema

A YAML block at the very top of the document, before any markdown:

```yaml
---
type: core
description: "Acme identity — who we are, who we serve, how we create value, what we do"
governance: core-ref
scope: workspace
status: operator-reviewed
workspace: acme
created: 12
last-updated: 40
updated-by: joint
convention: _system/workspace-folder-convention.md
---
```

### Field Reference

| Field | Required | Purpose |
|-------|----------|---------|
| `type` | Yes | Classification. Determines folder home, staleness threshold, structural requirements. |
| `description` | Yes | One-line summary (~80 chars). Lets the agent scan metadata without reading the body. |
| `status` | Yes | Maturity — how much latitude the agent has with the content (see vocab below). |
| `governance` | If applicable | Role in governance (`core-ref` = listed in a `core.md`). Enables reverse lookups. |
| `scope` | Recommended | Which scope level: `system`, `workspace`, `engagement`. |
| `created` | Yes | Session number when first created. Never changes. |
| `last-updated` | Yes | Session number of the last *meaningful* update. |
| `updated-by` | Yes | Who made the last meaningful update: `operator`, `agent`, `joint`. Trust signal. |
| `workspace` | If workspace-specific | Slug matching a directory in `workspaces/`. |
| `convention` | For Tier A | Which doc defines this type's required sections. Enables structural verification. |
| `related` | Optional | Links to related docs — a discovery safety net if folder placement isn't perfect. |

### What "meaningfully updated" means

`last-updated` tracks substantive changes, not mechanical ones.

- **Counts:** rewriting a section on new intelligence, adding a hypothesis, integrating research.
- **Doesn't count:** fixing a typo, reformatting a table, adding frontmatter itself.

When in doubt, update it — a false positive is less harmful than a false negative.

---

## Type Vocabulary

**Principle: type classifies function, not location.** Most types have a natural folder home because function and location align. But some (like `index`) are defined by what the document *does* — an index at the root of any folder is still an index. When function and location conflict, function wins.

### Tier A — Structured (have required sections)

These have a `convention` field pointing to the doc that defines their required sections, so structure can be verified, not just classified.

| Type | Home | Staleness | Required Sections |
|------|------|-----------|-------------------|
| `core` | `{scope}/core.md` | 40 sessions | Who we are, Who we serve, How we create value, What we do |
| `operating-lens` | `{scope}/operating-lens.md` | 5 sessions | What's happening now, Active direction, Watches |
| `voice-kernel` | `{workspace}/context/voice-kernel.md` | 40 sessions | Per `blueprints/voice-kernel-template.md` |
| `decision` | `_system/decisions/` | write-once | Decision, Rationale, Alternatives, What Would Make Us Revisit |

### Tier B — Typed (folder home + purpose, no mandatory sections)

The system validates placement (type ↔ folder), not internal structure.

| Type | Home | Routing Test |
|------|------|-------------|
| `context` | `{workspace}/context/` | Situational, market, or product context that orients the agent |
| `artifact` | `{workspace}/artifacts/` | A durable doc that cements a conclusion, state, or deliverable |
| `research` | `{workspace}/research/` | Exploration that informed a decision |
| `operations` | `{workspace}/operations/` | How we run things — working docs, SOPs, staging areas |
| `blueprint` | `blueprints/` | A reusable method for a recurring operation |
| `workflow` | `blueprints/workflows/` | The operational map of a recurring activity — the loop, its economics, what compounds |
| `framework` | `frameworks/` | Teaches how to *think* about a class of problem |
| `system` | `_system/` | Defines what the system IS — architecture, rules, principles |
| `resource` | `resources/` | Knowledge from outside the system — practitioner research, domain catalogs |
| `criteria` | `blueprints/criteria/` | A binary evaluation rubric — locked after validation |
| `tool-profile` | `tools/[name]/profile.md` | Operational knowledge about an external tool — capabilities, costs, gotchas |
| `index` | `{folder}/index.md` | A catalog or navigation doc pointing to the content it indexes |
| `marketing-pattern` | `blueprints/marketing-patterns/` | A named, attributed, cross-channel marketing method (see below) |
| `campaign` | `workspaces/{workspace}/campaigns/` | A channel-bound, time-bound execution with setup → run → end phases |

### Tier C — Exempt (no frontmatter)

These have their own lifecycle and are **not** frontmattered: `_inputs/` staging files, skill files (`.claude/skills/` — own schema), command files (`.claude/commands/` — own schema), meeting transcripts, `backlog.md` / `task-notes.md` (working tables), the session log (append-only). Note: `*-index.md` is *not* exempt — it's `type: index`.

**Adding a new type:** if something emerges that doesn't fit, add it here first (home, staleness, routing test, and how it gets created/maintained), then use it. Log the choice to `_system/decisions/`.

---

## Capturing a Marketing Pattern

A `marketing-pattern` is a named, attributed, opinionated method that works across multiple channels — distinct from a single-channel tactic (those live in the discipline's doc in `resources/marketing/`). The signal it's crossed the threshold: you can describe it without naming a specific channel and it still makes sense.

**A pattern card carries:** Attribution (who authored it), Intent (the move in one sentence), Context (when to apply), Problem (the uncertainty it reduces), **Forces** (the competing values the solution resolves), Core Opinions (definitional commitments that separate it from generic advice), Procedure (the mechanical how-to), What It Produces, Known Variants & Limits, What It Is NOT, and Known Uses (one line per execution, accumulated over time).

**Capture protocol** — when pulling a pattern from source material (a transcript, article, practitioner corpus):

1. Work from the command where the source is loaded (e.g. `/marketing-os`), not cold.
2. Load the source files into context first.
3. Draft **Forces first** — before procedure. Each force must trace to a specific sentence in the source.
4. Run the falsification test on each force: can you cite material pushing the opposite direction? If not, drop it.
5. Forces drafted from general knowledge are the failure mode — refuse them.

Then fill the remaining sections. Reference specimen: `blueprints/marketing-patterns/situation-variant-testing.md`.

---

## Field Vocabularies

**`status` — maturity:**

| Value | Means | Agent latitude |
|-------|-------|----------------|
| `working-notes` | Agent synthesis or early draft, not operator-validated | Low — treat as directional, flag assumptions |
| `operator-reviewed` | Operator has read and corrected it | Medium — treat as current unless contradicted |
| `doctrine` | Operator-ratified | High — treat as ground truth |

**`scope`:** `system` (applies across all workspaces) · `workspace` (one workspace) · `engagement` (one engagement within a workspace).

**`updated-by`:** `operator` (operator drove the change — higher trust) · `agent` (agent synthesized it — may need validation) · `joint` (collaborative).

**`governance`:** `core-ref` — the doc is listed in a `core.md` as a governing document. Enables the reverse lookup (the doc knows it's governed, not just `core.md` knowing it points there).

---

## Consumers & Maintenance

The convention is real because things read it:

- **Startup** parses `last-updated` on the workspace base (`core.md` + `operating-lens.md`), compares to the current session, and flags staleness; reads `status` / `updated-by` to calibrate confidence.
- **`/done`** updates `last-updated` + `updated-by` on docs it meaningfully changed, and checks new docs for valid frontmatter + correct placement.
- **`/audit`** periodically scans governed locations for missing frontmatter, type↔folder mismatches, and missing required sections.

New docs in governed locations get frontmatter at creation: `type`, `description`, `status` (usually `working-notes`), `created` + `last-updated` (current session), `updated-by`, plus `workspace` if workspace-specific and `convention` if Tier A.

---

## Anti-Patterns

| Anti-pattern | What goes wrong | Prevention |
|---|---|---|
| Mechanical timestamp updates | `last-updated` bumped on every touch — destroys the staleness signal | The "meaningfully updated" rule above |
| Stale frontmatter, current content | Content changes but frontmatter doesn't — false staleness alerts | `/done` maintenance |
| Frontmatter bloat | Fields with no consumer | Every field must have a named reader |
| Inventing enum values | A new `type` appears without being added to the vocabulary | Add it here first, then use it |
| Frontmattering Tier C docs | Overhead with no benefit | Tier C is explicitly exempt |
