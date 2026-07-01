---
type: system
governance: core-ref
scope: system
description: "The light workspace convention — what every workspace gets from day one (core.md identity + operating-lens.md now-state + backlog + context), and how it grows through real work via the Extension Catalog."
status: operator-reviewed
created: 1
last-updated: 1
updated-by: joint
---

# Workspace Convention

Every workspace — a client, a project, an area of your work — needs a home. Without a convention, each one drifts into its own shape and you lose orientation the moment you come back to it. This convention defines the **minimum base** a workspace gets on day one. It is deliberately thin. You do not build the whole structure up front. You start from real work, and the structure fills as the work earns it.

The mental model: a workspace is an **operations command center** for one slice of your work. Marketing is operations — the same thing, not a subset — so the depth that ships in this kit leans marketing, but the structure holds any repeatable work.

---

## The base — four things

```
[workspace-name]/
├── core.md            # Durable identity — who this is, who it serves, how it creates value
├── operating-lens.md  # Current state — what's happening now, what to watch
├── backlog.md         # The operating backlog — what needs to happen
└── context/           # Workspace-specific knowledge, accumulated through use
```

That's it. Two short docs, a backlog, and an empty `context/` folder. Everything else is an **extension** — added when the work justifies it, never before (see the Extension Catalog).

### `core.md` — durable identity

The slow-changing foundation. Who this workspace is, who it serves, how it creates value, what it does. Seeded by a short interview at setup and edited rarely — when the business itself changes, not every session.

`core.md` answers *"what is this?"* It does **not** carry the day-to-day. It is the thing a fresh session reads to know the ground it's standing on.

### `operating-lens.md` — current state + watches

The volatile layer. What's happening right now, where attention should go, what to flag. This is the session lens — read it at startup to know where you left off; update it at shutdown when the state moved.

The split between `core.md` and `operating-lens.md` is the point. Identity is stable; state churns. Jamming them into one doc means the stable foundation gets buried under session-by-session churn, and the doc bloats until no one trusts it. Keeping them separate lets `core.md` stay a clean foundation and `operating-lens.md` stay a current, honest read of now.

### `backlog.md` — the operating backlog

What needs to happen for this workspace — tasks, open questions, blocked items. Wired into startup (ambient awareness of open work) and shutdown (update statuses, capture what surfaced). Write items as session briefs: enough that a fresh session could pick one up and execute it cold.

### `context/`

Workspace-specific knowledge as it accumulates — voice notes, what's worked, reference material, research outputs. Starts empty. Grows only with use. The routing test for anything you're about to file: *"is this reusable across workspaces, or is it about this one?"* Reusable graduates up to the shared tier (`.claude/skills/`, `blueprints/`, `tools/`, `resources/`); workspace-specific stays here.

---

## How the structure fills itself

The base is light on purpose. You are not meant to fill it before you do real work. The structure populates **through the work**, routed at `/done`, narrated as it happens:

1. **Every home ships empty with a one-line charter** ("what goes here") — so there's always an obvious destination, and nothing is ever required up front.
2. **`/done` is the capture engine.** It routes what surfaced this session into the right home using the reusable-vs-this-workspace test.
3. **The system narrates the capture** — *"Filed your voice correction to `context/`. That list-cleaning thing — second time now; one more and we codify it as a reusable workflow."* You learn where things live by watching your own work get filed, not from a structure lecture.

> **The principle:** Homes exist empty from day one. Only `core.md` gets filled at setup. Everything else fills through real work, routed by `/done`, narrated as it happens. Structure stops being a setup form and becomes a filing system that populates itself.

---

## Templates

### `core.md` template (identity — seeded at setup)

```markdown
---
type: core
description: "[Workspace] identity — who we are, who we serve, how we create value"
status: operator-reviewed
scope: workspace
created: [session]
last-updated: [session]
updated-by: joint
---

# Core — [Workspace Name]

## Who we are
[One or two sentences. What this business/practice/area is.]

## Who we serve
[The people or companies on the other end of the work. Situational, not a demographic abstraction — "someone who is [situation] and needs [outcome]."]

## How we create value
[What you actually do for them, and why it matters. Plain language.]

## What we do
[The concrete activities — the work that repeats. This is what the system will help you operate.]
```

Keep it short. `core.md` is identity, not a strategy treatise. If a section wants to grow into research and positions, that's a sign it belongs in a `context/` doc that `core.md` points to — not in `core.md` itself.

### `operating-lens.md` template (now-state — updated as you work)

```markdown
---
type: operating-lens
description: "[Workspace] current state — what's happening now, what to watch"
status: operator-reviewed
scope: workspace
cap-lines: 40
created: [session]
last-updated: [session]
updated-by: joint
---

# Operating Lens — [Workspace Name]

## What's happening now
[The current focus. What you're in the middle of. Where you left off last session.]

## Active direction
[The 2-5 things that have momentum right now. Each one short.]

## Watches
[Things to keep an eye on and flag if they move — a pending decision, a slipping commitment, a deadline, a risk.]
```

`operating-lens.md` is where state lives, so it's the doc most prone to bloat. Keep Active Direction to a handful of short bullets and Watches to what's genuinely live. When it gets long, that's the signal to drain finished items — the backlog and git history are the record, not this doc.

---

## Naming conventions

| Item | Convention | Example |
|------|-----------|---------|
| Workspace folder | kebab-case | `acme`, `personal-brand` |
| Context docs | descriptive, kebab-case | `voice-kernel.md`, `what-works.md` |
| Meeting notes | date-prefix + title | `2026-01-15 - Kickoff Call.md` |
| Root-level docs | fixed names | `core.md`, `operating-lens.md`, `backlog.md` |
| Function folders | short kebab-case | `content`, `data`, `campaigns` |

**General rules:**
- No numbered prefixes on folders (no `00 -`, `01 -`). Alphabetical is fine.
- No spaces in folder names. Spaces in meeting-note titles are fine — the date prefix handles sorting.
- No version suffixes. Edit in place — `positioning-v2.md` is how you end up with three versions and no clarity on which is current.

---

## Extension Catalog

Extensions get added when the work justifies them — not before. Each row documents what triggers the addition.

| Extension | Add when | Notes |
|-----------|----------|-------|
| `context/voice-kernel.md` | The system needs to write in your voice | Voice corrections accumulate here; `/compose` reads it |
| `meetings/` + `meetings/log.md` | Meeting transcripts start flowing | `log.md` is rolling synthesis; individual files are per-meeting records |
| `content/` | Content production work begins | Subfolders emerge from the content types you actually produce |
| `data/` | Data work starts (audiences, enrichment, exports) | `_system/data-workspace-convention.md` governs it |
| `campaigns/` | A marketing campaign kicks off | One folder per campaign |
| `operations/` | Recurring processes or working docs need a home | SOPs, staging areas, frequently-changing working docs |
| `scripts/` | Custom automation is built | Include a venv if Python |
| Additional `context/` docs | As the workspace grows | Voice guide, audience profiles, platform guides — per file placement conventions |

The catalog documents what's *available*. It does not mean build it all. An empty folder is noise.

---

## Lifecycle rules

| Item | Retention | Notes |
|------|-----------|-------|
| `core.md` | Permanent, edited rarely | Changes when the business changes, not per session |
| `operating-lens.md` | Permanent, updated in place | State churns; drain finished items, don't append history |
| `context/` docs | Permanent, updated in place | Knowledge evolves — edit, don't fork |
| `backlog.md` | Permanent, actively maintained | Done items clear periodically; git is the permanent record |
| Function folders (added later) | Per their own conventions | Designed at point of need |

---

## Multiple workspaces

If you work with one company, you don't need a per-workspace command — `/start` *is* your entry. Open with `/start`, close with `/done`. The single workspace lives at the system root.

When you take on a second company or a genuinely separate area of work, run `/new-project`. It scaffolds a new workspace with this light base and (if useful) a `/[workspace]` command so you can drop straight into it. You add structure only when the second workspace earns it — same rule as everything else.

---

## Anti-patterns

- **Pre-building function folders** — don't create `content/`, `data/`, `operations/` until work actually starts there. Empty folders are noise.
- **Front-loading foundation docs** — you do not write positioning, ICP, market context, and buyer personas before the system can help. You start from real work. That knowledge accumulates in `context/` as the work surfaces it — routed by `/done`, not produced as setup homework.
- **Jamming identity and state into one doc** — `core.md` is identity, `operating-lens.md` is now-state. Merging them buries the stable foundation under churn and bloats the doc until it's untrusted.
- **Numbered folder prefixes** — manual sort ordering that doesn't scale.
- **Version suffixes on docs** — edit in place.
- **Letting `operating-lens.md` grow without draining** — when Active Direction and Watches sprawl, the doc stops being a current read and starts being a graveyard. Drain finished items; the backlog and git carry the history.
