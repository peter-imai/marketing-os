---
name: new-project
description: "Add a new project or client to Marketing OS. Interactive setup — creates folder, foundation docs, and slash command.\nTRIGGER when: operator mentions a new client, new project, new engagement, or onboarding someone new; work references a client that doesn't have a workspace yet.\nDO NOT TRIGGER when: working within an existing project, or operator is just discussing a potential client without committing."
---

# New Project

Add a project or client to Marketing OS. Interactive elicitation → scaffold folder + foundation docs + slash command.

**Input:** Operator answers to 5 questions.
**Output:** Complete project workspace at `projects/[name]/` + slash command at `.claude/commands/[name].md`.

**References:**
- [templates/command-template.md](templates/command-template.md) — template for generating the project's slash command

**Subagent strategy:** All operations are sequential — no subagent strategy needed.

---

## Step 1: Elicit

Ask these questions conversationally. Don't dump all 5 at once — ask 1-2 at a time, respond to what the operator says, then continue. Adapt the phrasing to the conversation flow.

1. **"What's the name of this project?"**
   - Derive the kebab-case folder name and command name from the answer.
   - If the name has spaces or capitals, convert silently (e.g., "Acme Corp" → `acme-corp`).

2. **"What does [name] do? One sentence."**
   - This seeds the positioning doc and intelligence file.

3. **"Who's it for, and why you over the alternatives?"**
   - This seeds the positioning doc. "Alternatives" includes doing nothing / status quo.
   - If the operator doesn't know yet, that's fine — write "To be developed" in the positioning doc.

4. **"Is this B2B, B2C, or internal?"**
   - This is a routing flag for future foundation work. B2B → ICP doc will be relevant later. B2C → skip ICP, personas are the targeting. Internal → neither applies.

5. **"What do you want to tackle first?"**
   Offer options — the operator may not know what's possible:
   - **Content** — LinkedIn, newsletter, YouTube, blog
   - **Outbound** — cold email, list building, prospecting
   - **Strategy** — positioning deep-dive, market research, competitive analysis
   - **Meeting intelligence** — drop a transcript, get structured outputs
   - **Something else** — tell me what's on your plate

   The answer seeds the first backlog item.

6. **"Will this involve working with data — list building, enrichment, CSV imports, that kind of thing?"**
   - If yes → scaffold data project structure (`_sources/`, `_enrichment/`, `_working/`, `_output/`, `scripts/`, `data-state.md`). Convention: `_system/data-workspace-convention.md`.
   - If no or unsure → skip. The fallback convention (CLAUDE.md routing) will scaffold on first touch if data files appear later.

**After all questions answered:**

7. **Check for multi-project context.** If this appears to be a client engagement (not the operator's own business), ask: **"Is this a client where you need to manage the relationship — stakeholders, how you show up, that kind of thing?"**
   - If yes → create `engagement-strategy.md`
   - If no or if this is the operator's own business → skip it

8. **"What does success look like for this right now, and what's your biggest worry?"**
   - This seeds `core.md` (the Intention section). Map the answers:
     - "What's happening" → derive from Q2 + Q5 context
     - "Success right now" → their answer to the first part
     - "Primary concern" → their answer to the worry part. If they don't have one, leave as "To be identified."
     - "Time horizon" → infer from context, or ask: "Are you thinking this week, this month, or this quarter?"

**Present the scaffold plan:**

> Here's what I'll create for **[name]**:
>
> ```
> projects/[name]/
> ├── context/
> │   └── positioning.md        ← seeded from what you told me
> ├── artifacts/                 ← for durable deliverables
> ├── core.md                   ← what matters right now (from Q8)
> ├── marketing-strategy.md     ← stub — you'll build this out
> └── backlog.md                ← first task: [from Q5]
> ```
>
> [If data work:
> ```
> ├── _sources/                  ← immutable original imports
> ├── _enrichment/               ← enrichment pass outputs
> ├── _working/                  ← intermediates, merges, logs
> ├── _output/                   ← final deliverables
> ├── scripts/                   ← enrichment/cleaning scripts
> ├── data-state.md              ← data project manifest (inventory lens)
> └── data-story.md              ← decisions, learnings, strategic arc (meaning lens)
> ```
> ]
>
> ```
> ├── auth.yaml                  ← tool auth manifest (declares env var names)
> ```
>
> Plus a `/[name]` command so you can start sessions.
> [If multi-project: Plus `engagement-strategy.md` for relationship management.]

**Wait for operator approval before creating anything.**

---

## Step 2: Scaffold

Create files in this order. Use the operator's answers from Step 1 to populate content.

### 2a. Create the folder structure

Create `projects/[name]/context/` and `projects/[name]/artifacts/`.

### 2b. Create data project structure (only if Q6 = yes)

Create these folders and the two companion docs:
- `projects/[name]/_sources/`
- `projects/[name]/_enrichment/`
- `projects/[name]/_working/`
- `projects/[name]/_output/`
- `projects/[name]/scripts/`

Write `data-state.md` using the template from `_system/data-workspace-convention.md` § State Doc Template. Populate the Project section with what we know from elicitation (goal from Q2/Q5, entity types if mentioned). Leave tables empty — they'll fill as work begins.

Write `data-story.md` using the template from `_system/data-workspace-convention.md` § Data Story → Template. Populate the Strategic Frame: Goal from Q2/Q5 (the business outcome, not pipeline mechanics), Arc set to "sourcing" (initial phase). Leave Standing Decisions empty and Log empty — they'll accumulate as work begins.

### 2c. Write `context/positioning.md`

```markdown
---
type: context
description: "Positioning seed — what [name] does, who it's for, why them"
status: working-notes
client: [name]
governance: core-ref
scope: client
created: [current session number or date]
last-updated: [current session number or date]
updated-by: joint
convention: _system/client-context-architecture.md
---

# Positioning: [Name]

## What [Name] Does

[Answer from Q2 — one sentence]

## Who It's For

[Answer from Q3 — the audience and their situation]

## Why [Name] Over Alternatives

[Answer from Q3 — the differentiator. If operator didn't have a clear answer, write: "To be developed. Run `/positioning` for facilitated Dunford discovery."]

## Competitive Alternatives

[If mentioned in Q3, list them. Otherwise: "Not yet mapped. Foundation doc sequence: positioning → ICP (if B2B) → market context → buyer personas. See `_system/client-context-architecture.md`."]

---

*Seed positioning from `/new-project` setup. For full positioning discovery, run `/positioning` (Dunford methodology).*
*For market research (ICP, buyer personas, market context), see Crawford research prompts at `resources/jordan-crawford/market-research/`.*
```

### 2d. Write `marketing-strategy.md`

```markdown
---
type: strategy
description: "Marketing strategy — what we believe about [name]'s market and what we're doing about it"
status: working-notes
client: [name]
governance: core-ref
scope: client
created: [current session number or date]
last-updated: [current session number or date]
updated-by: agent
convention: _system/client-context-architecture.md
---

# Marketing Strategy: [Name]

## Strategic Thesis

[Leave blank with note: "To be developed. What do you believe about this market and why you'll win?"]

## How We See the Product

[Seed from Q2 if there's enough to work with. Otherwise: "To be developed."]

## Audience

[Seed from Q3 + Q4. Note B2B/B2C flag. If B2B: "ICP and buyer personas to be developed via Crawford research prompts." If B2C: "Buyer personas to be developed."]

## What's First

[From Q5 — what the operator wants to tackle first and any initial thinking about approach.]

---

*Strategy stub from `/new-project` setup. Build this out through operating sessions with `/[name]`.*
```

### 2e. Write `backlog.md`

```markdown
# [Name] Backlog

| # | Task | Status | Added |
|---|------|--------|-------|
| 1 | [First task derived from Q5 — be specific, not just "content"] | ready | [today's date] |

---

*Task counter: 1.*
```

### 2f. Write `core.md`

```markdown
---
type: core
description: "[Name] — intention, core documents, active direction, watches"
governance: core-ref
scope: client
convention: _system/core-convention.md
---

# Core — [Name]

## Intention

**What's happening:** [From Q2 + Q5 — what the engagement is doing right now]
**Success right now:** [From Q8 — what "this is working" looks like]
**Primary concern:** [From Q8 — the biggest worry. If none stated: "To be identified."]
**Time horizon:** [From Q8 — this week / this month / this quarter]

## Core Documents

- `context/positioning.md` — positioning seed
- `marketing-strategy.md` — strategy stub
- `backlog.md` — live task status
[If data work: - `data-story.md` — data narrative (decisions, learnings, strategic arc)]

## Active Direction

- [From Q5 — what the operator wants to tackle first]

## Watches

- [Leave empty or seed one from Q8 concern if it maps to something observable]
```

Convention: `_system/core-convention.md`. 30-line hard cap. The operator owns this document — the agent suggests changes but never writes without approval. For agency-pattern engagements (Q7 = yes), set `scope: engagement` instead of `scope: client`.

### 2g. Write `auth.yaml`

```yaml
# [Name] — Client Auth Manifest
# Convention: C1. See _system/tool-integration-convention.md § Auth Scoping.
# Secrets: projects/[name]/.env (gitignored). This file declares WHAT — .env holds values.

env_file: .env  # relative to this directory

# tools:
#   example-tool:
#     env_vars: [EXAMPLE_API_KEY]
```

Scaffolded empty — tools get added via `/connect-tool` or manually. The commented `tools:` section shows the expected shape.

### 2h. Write `engagement-strategy.md` (only if Q7 = yes)

```markdown
---
type: strategy
description: "Engagement strategy — relationship layer for [name]"
status: working-notes
client: [name]
governance: core-ref
scope: engagement
created: [current session number or date]
last-updated: [current session number or date]
updated-by: agent
convention: _system/client-context-architecture.md
---

# Engagement Strategy: [Name]

## Engagement Thesis

[Why we're working with this client. What the relationship is.]

## What Success Looks Like

[To be developed — from the client's perspective and from yours.]

## How We Show Up

[To be developed — tone, dynamics, what to protect, what to push.]

## The People

[To be developed — who's involved, what they care about.]

## Risks & Constraints

[To be developed.]

## Open Questions

[To be developed.]

---

*Stub from `/new-project` setup. Build this out through operating sessions — especially after first meetings.*
```

---

## Step 3: Wire

### 3a. Generate the slash command

Read [templates/command-template.md](templates/command-template.md). Generate `.claude/commands/[name].md` by filling in the template with:
- Project name
- File paths (`projects/[name]/...`)
- Activity routing table seeded from Q5 (the activity they chose + 2-3 generic activities)
- If engagement-strategy.md exists, include it in the startup loading sequence

### 3b. Update CLAUDE.md routing table

Add a new row to the routing table in `CLAUDE.md`:

```
| [Name] project work | Use `/[name]` command. Routes by activity, loads context on demand. |
```

Use the same format as your existing entries. If the operator said "client" during elicitation, use "client work" instead of "project work".

### 3c. Present summary

Tell the operator:
- What was created (list all files)
- **"Run `/[name]` to start your first session."**
- **"When you're ready for deeper positioning, run `/positioning`."**
- If B2B: **"For ICP and buyer personas, the system has Crawford research prompts at `resources/jordan-crawford/market-research/`."**

---

## After Completion

The project is set up when all of these are true:
- [ ] `projects/[name]/` exists with: `context/positioning.md`, `artifacts/`, `core.md`, `marketing-strategy.md`, `backlog.md`, `auth.yaml`
- [ ] If data work: `_sources/`, `_enrichment/`, `_working/`, `_output/`, `scripts/`, `data-state.md`, and `data-story.md` exist
- [ ] If multi-project: `engagement-strategy.md` exists at client root
- [ ] `.claude/commands/[name].md` exists and follows the command template
- [ ] CLAUDE.md routing table has a row for `/[name]`
- [ ] Operator has seen the summary and knows what to do next

---

## Error Handling

- **Name collision:** Before creating any files, check if `projects/[name]/` already exists. If it does, tell the operator and ask: rename, merge into existing, or abort.
- **Vague answers:** If the operator gives very thin answers (e.g., "I don't know yet" for positioning), that's fine. Write "To be developed" in the relevant sections. The docs are working-notes status — they're seeds, not doctrine.
- **CLAUDE.md routing table not found:** If the routing table format in CLAUDE.md has changed, tell the operator what line to add manually rather than risking a bad edit.

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Write: `projects/**` | Create project folder and foundation docs |
| Files | Write: `.claude/commands/**` | Create the project slash command |
| Files | Edit: `CLAUDE.md` | Add routing table entry |

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
