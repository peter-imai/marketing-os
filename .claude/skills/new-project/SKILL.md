---
name: new-project
description: "Add a new project or client to Marketing OS. Interactive setup — creates the light workspace base (core.md identity + operating-lens.md + backlog + context) and a slash command. No foundation-doc homework — the workspace fills through real work.\nTRIGGER when: operator mentions a new client, new project, new engagement, or onboarding someone new; work references a workspace that doesn't exist yet.\nDO NOT TRIGGER when: working within an existing project, or operator is just discussing a potential client without committing."
---

# New Project

Add a project or client to Marketing OS. Interactive elicitation → scaffold the **light base** + slash command.

The base is deliberately thin: `core.md` (identity) + `operating-lens.md` (now-state) + `backlog.md` + an empty `context/`. You do **not** front-load positioning, ICP, market context, and personas — that knowledge accumulates in `context/` as real work surfaces it, routed by `/done`. Convention: `_system/client-folder-convention.md`.

**Input:** Operator answers to a short interview.
**Output:** Workspace at `projects/[name]/` (light base) + slash command at `.claude/commands/[name].md`.

**References:**
- [templates/command-template.md](templates/command-template.md) — template for the project's slash command
- `_system/client-folder-convention.md` — the light base + the `core.md` / `operating-lens.md` templates

**Subagent strategy:** All operations are sequential — no subagent strategy needed.

---

## Step 1: Elicit

Ask conversationally — 1-2 questions at a time, respond, continue. This is the same light identity interview `/start` runs; it seeds `core.md`.

1. **"What's the name of this project?"**
   - Derive the kebab-case folder/command name. Convert spaces/capitals silently ("Acme Corp" → `acme-corp`).

**What the work is** (seeds `core.md`):
2. **"In a sentence or two — what is [name]?"** (Who you are.)
3. **"Who's it for — who does it serve?"** (Push for the situational version: "someone who is [situation] and needs [outcome].")
4. **"What do you do for them, and why does it matter?"** (How you create value.)
5. **"What's the work that repeats here?"** (The activities the system will help operate.)

**What to start on** (seeds the first backlog item + `operating-lens.md`):
6. **"What do you want to tackle first?"** Offer options — they may not know what's possible:
   - **Content** — LinkedIn, newsletter, YouTube, blog
   - **Outbound** — cold email, list building, prospecting
   - **Meeting intelligence** — drop a transcript, get structured outputs
   - **A specific piece of work** — a draft, a brief, a cleanup
   - **Something else** — tell me what's on your plate

**Optional extensions** (only if they come up):
7. **"Will this involve data work — list building, enrichment, CSV imports?"**
   - If yes → scaffold the data workspace (`_sources/`, `_enrichment/`, `_working/`, `_output/`, `scripts/`, `data-state.md`, `data-story.md`). Convention: `_system/data-workspace-convention.md`.
   - If no/unsure → skip. It scaffolds on first touch if data appears later.

8. **"Is this a client where you'll manage a relationship — stakeholders, how you show up?"**
   - This is a *judgment flag*, not a doc to create now. If yes, note it in `operating-lens.md` Watches ("relationship to navigate — stakeholder reads accumulate in `context/` as you meet them") and add `context/` as the home. Don't pre-build an engagement-strategy doc — it earns its place once there are real people and dynamics to record.

**Present the scaffold plan:**

> Here's what I'll create for **[name]** — the light base. It fills as you work; nothing is required up front:
>
> ```
> projects/[name]/
> ├── core.md             ← identity, seeded from what you told me
> ├── operating-lens.md   ← now-state; what you're starting on
> ├── backlog.md          ← first task: [from Q6]
> └── context/            ← empty; workspace knowledge lands here as you work
> ```
>
> [If data work, add:
> ```
> ├── _sources/  _enrichment/  _working/  _output/  scripts/
> ├── data-state.md       ← data project manifest
> └── data-story.md       ← decisions, learnings, strategic arc
> ```
> ]
>
> Plus a `/[name]` command so you can drop into sessions.

**Wait for operator approval before creating anything.**

---

## Step 2: Scaffold

Create files in this order, populated from Step 1.

### 2a. Folder + empty homes

Create `projects/[name]/context/`. Add a one-line charter so the home is obvious: a `context/README.md` containing *"Workspace-specific knowledge accumulates here as you work — voice notes, what's worked, reference material. Routed by `/done`."*

### 2b. Data workspace (only if Q7 = yes)

Create `_sources/`, `_enrichment/`, `_working/`, `_output/`, `scripts/`. Write `data-state.md` and `data-story.md` from the templates in `_system/data-workspace-convention.md` (§ State Doc Template, § Data Story → Template). Populate the Goal from Q2/Q6; leave tables/logs empty — they fill as work begins.

### 2c. Write `core.md` (identity)

Use the `core.md` template in `_system/client-folder-convention.md`:

```markdown
---
type: core
description: "[Name] identity — who we are, who we serve, how we create value"
status: operator-reviewed
client: [name]
governance: core-ref
scope: workspace
created: [session]
last-updated: [session]
updated-by: joint
convention: _system/client-folder-convention.md
---

# Core — [Name]

## Who we are
[From Q2]

## Who we serve
[From Q3 — situational]

## How we create value
[From Q4]

## What we do
[From Q5 — the work that repeats]
```

Keep it short. If an answer was thin, take it and move on — `core.md` sharpens through use. The operator owns this doc; suggest changes, don't rewrite without approval. (Agency-pattern engagement → `scope: engagement`.)

### 2d. Write `operating-lens.md` (now-state)

Use the `operating-lens.md` template in `_system/client-folder-convention.md`:

```markdown
---
type: operating-lens
description: "[Name] current state — what's happening now, what to watch"
status: operator-reviewed
client: [name]
governance: core-ref
scope: workspace
created: [session]
last-updated: [session]
updated-by: joint
convention: _system/client-folder-convention.md
---

# Operating Lens — [Name]

## What's happening now
[From Q6 — what they're starting on]

## Active direction
- [From Q6]

## Watches
- [If Q8 = yes: "relationship to navigate — stakeholder reads accumulate in context/ as you meet them." Else leave empty.]
```

### 2e. Write `backlog.md`

```markdown
# [Name] Backlog

| # | Task | Status | Added |
|---|------|--------|-------|
| 1 | [First task from Q6 — be specific, not just "content"] | ready | [today's date] |

---

*Task counter: 1.*
```

### 2f. Write `auth.yaml`

```yaml
# [Name] — Client Auth Manifest
# Convention: see _system/tool-integration-convention.md § Auth Scoping.
# Secrets: projects/[name]/.env (gitignored). This file declares WHAT — .env holds values.

env_file: .env  # relative to this directory

# tools:
#   example-tool:
#     env_vars: [EXAMPLE_API_KEY]
```

Scaffolded empty — tools get added via `/connect-tool`.

### 2g. Self-critique the identity docs before wiring

`core.md` frames everything downstream — a misread here gets embedded everywhere. **Run `.claude/helpers.md#Self-Critique-Gate`** on `core.md` + `operating-lens.md`. The bar: does `core.md` capture who they are in *their* words (specific, not generic "we help businesses grow")? Is "who we serve" situational, not a demographic abstraction? Is `operating-lens.md` the actual now-state? Then present both back for a quick confirm — *"Here's how I captured you — does this land? Anything off?"* — and adjust before generating the command.

---

## Step 3: Wire

### 3a. Generate the slash command

Read [templates/command-template.md](templates/command-template.md). Generate `.claude/commands/[name].md` filled with:
- Project name + file paths (`projects/[name]/...`)
- Startup that reads `core.md` (identity) + `operating-lens.md` (now-state) + `backlog.md`
- Activity routing seeded from Q6 + 2-3 generic activities

### 3b. Update CLAUDE.md routing table

Add a row:

```
| [Name] project work | Use `/[name]` command. Routes by activity, loads context on demand. |
```

Match existing entry format. Use "client work" if the operator framed it as a client.

### 3c. Present summary

- List what was created.
- **"Run `/[name]` to start your first session — it'll invite you into a first piece of work."**
- **"The workspace fills as you go. Run `/teach-me` if you want the core concepts walked through."**

---

## After Completion

The project is set up when all are true:
- [ ] `projects/[name]/` exists with: `core.md`, `operating-lens.md`, `backlog.md`, `context/` (+ charter), `auth.yaml`
- [ ] If data work: `_sources/`, `_enrichment/`, `_working/`, `_output/`, `scripts/`, `data-state.md`, `data-story.md`
- [ ] `.claude/commands/[name].md` exists and follows the template
- [ ] CLAUDE.md routing table has a `/[name]` row
- [ ] Operator has seen the summary and knows the next step

---

## Error Handling

- **Name collision:** Check if `projects/[name]/` exists before creating. If it does — rename, merge, or abort.
- **Vague answers:** Thin answers are fine. Take what you get; `core.md` is `operator-reviewed` but allowed to start light and sharpen through use. Don't pad with "To be developed" sections — a short honest `core.md` beats a long hedged one.
- **CLAUDE.md routing table not found:** If the format changed, tell the operator the line to add manually rather than risk a bad edit.

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Write: `projects/**` | Create workspace + light base |
| Files | Write: `.claude/commands/**` | Create the project slash command |
| Files | Edit: `CLAUDE.md` | Add routing table entry |

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
