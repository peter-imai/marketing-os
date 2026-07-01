---
name: build-skill
description: "Build a new Marketing OS skill from a blueprint, SOP, or workflow. Criteria-first process — define what good output looks like, build the skill, then prove it meets the standard.\nTRIGGER when: operator wants to create, build, or mechanize a new skill; has a documented process, blueprint, SOP, or workflow to convert; says 'this should be a skill' or 'let's make a skill for this'.\nDO NOT TRIGGER when: modifying an existing skill (edit directly), or operator is building without wanting the structured process."
argument-hint: [workflow-name]
---

# Build Skill

Build a new skill from a validated workflow. Two phases: build it right, then prove it's right.

**Input:** A workflow to convert — a blueprint, SOP, documented process, or well-understood manual workflow.
**Output:** A complete skill package at `.claude/skills/<skill-name>/` wired into the system.

**References:**
- [quality-checklist.md](quality-checklist.md) — review criteria for Phase 2 (13 structural + 6 output-quality)
- [skill-template.md](skill-template.md) — starting skeleton for new SKILL.md files (includes step-file scaffold, subagent strategy section, progressive disclosure tiers)
- `_system/skill-design-conventions.md` — full rationale behind the six skill design conventions (progressive disclosure, helpers, step-file sharding, subagent strategy, permission declaration, source material identification)
- `blueprints/criteria-development.md` — criteria development blueprint (pattern menu, tiering, meta-evaluation). Reference for Step 4.
- `.claude/helpers.md` — shared procedures available to all skills

---

## Phase 1: Build

### Step 1: Identify the Source

What workflow is becoming a skill?

- **From blueprint/SOP:** Read the source document. Note which parts are procedure (→ SKILL.md), which are reference material (→ supporting files), and which are context that the consuming command already handles (→ don't duplicate).
- **From undocumented workflow:** Write out the steps first. If you can't articulate the procedure clearly, it's not ready to be a skill — capture it as a blueprint and iterate manually.

State what you're building and where the source material lives. **Wait for operator confirmation before proceeding.**

---

### Step 2: Assess Readiness

Answer these questions honestly:

1. **How many times has this workflow been executed?** More reps = more confidence the steps are right.
2. **Are the steps stable?** If the procedure changes every time, it's still a blueprint, not a skill.
3. **Are quality gates defined?** If you don't know what "good output" looks like, Step 4 will build quality gates from your failure modes — but you need at least observed failure modes to work from.
4. **Are failure modes known?** If you haven't hit errors yet, you haven't run it enough — but this doesn't block building. Step 4 can generate plausible failures analytically.

Present the assessment to the operator. If maturity is low, flag the risk: "This workflow has [N] manual executions. The skill will likely need iteration after the first few runs." **The operator decides whether to proceed** — don't hard-block.

---

### Step 3: Design the Package

**First, assess complexity.** Read the complexity tiers in [skill-template.md](skill-template.md) § Complexity Assessment. Determine which tier this skill falls into:
- **Simple** (≤3 short steps, no subagents) → L1 only, everything in SKILL.md
- **Medium** (4+ steps, or subagent coordination) → L1 + L2 step files
- **Complex** (multiple phases, deep reference, templates) → All three levels

**Then decide what goes where:**

| Content Type | Where It Lives | Examples |
|-------------|---------------|----------|
| Orchestration + quality gates | SKILL.md (L1, <5K tokens) | Step routing, decision points, error handling, subagent strategy |
| Detailed workflow logic | Step files (L2) | Phase instructions, subagent prompts, complex procedures |
| Output scaffolds, deep reference | Templates/resources (L3) | Output templates, prompt libraries, rubrics, examples |
| Shared procedures | `.claude/helpers.md` | Knowledge routing, backlog capture, strategy loading |
| Client/session context | Consuming command | Positioning docs, strategy files, client state |

**For skills that produce deliverables:** Build a context map — which sources does each generation/composition step need, and what happens if they're missing?

| Generation Step | Source | Type | When Loaded | Fallback if Missing |
|----------------|--------|------|-------------|---------------------|
| [step name] | [path or description] | static / dynamic / generated | [at this step] | [degradation path] |

**Source types:** Static = file at a known path (e.g., `context/icp.md`). Dynamic = operator-provided per invocation (e.g., prospect data). Generated = produced by a prior step or API call (e.g., enrichment results from Step 1).

This makes context precision AND degradation design explicit at design time. Every generation step names its sources. Reference material defers until the step that needs it. Fallback column catches brittleness before the skill is built.

**List every file you plan to create** with a one-line purpose for each. For medium/complex skills, include the step-file directory structure. **Wait for operator approval of the package design before building.**

**Rules:**
- SKILL.md stays under 5K tokens (~300-350 lines). If it's longer, move workflow detail to L2 step files.
- Every supporting file must be referenced from SKILL.md (or from the step file that uses it) at the point where it's needed.
- Don't duplicate context that consuming commands already load.
- Don't duplicate procedures that exist in `.claude/helpers.md` — reference them.
- For sharded skills, include the step-file scaffold from [skill-template.md](skill-template.md) § Step-File Scaffold.

---

### Step 4: Design the Quality Loop

**This step applies to skills that produce deliverables, content, or analytical output.** For pure utility skills (e.g. a data-fetch or file-processing skill), note "N/A — utility skill" and skip to Step 5.

Before building the skill, define what good output looks like. Criteria come first — they're a design tool, not a review gate.

1. **What does this skill produce, and what job does that output do?** One sentence, job-focused. Not what the output IS — what it DOES for the person who receives it. (See `blueprints/criteria-development.md` Phase 1A for examples.)

2. **What are the top 3 ways that output fails?** Pull from observed failure modes if the workflow has been run manually. If not, generate 3 plausible failures by running a hypothetical invocation through the workflow analytically — "If someone used this skill with [realistic input], what would go wrong?" Consider both output failures (what goes wrong with the finished artifact) and input failures (what happens when source material is incomplete or low-quality — these often cause the output failures).

3. **Draft 2-3 binary criteria that catch those failures.** Each criterion is a yes/no question an evaluator can answer without subjective judgment. For pattern inspiration, reference the pattern menu in `blueprints/criteria-development.md` Phase 2 (name-swap test, outcome test, negative-space, etc.) — skip Phases 3-4 (tiering and meta-evaluation are for deeper scored iteration, not skill self-audit). Keep it to 2-3 criteria.

4. **Write the criteria file.** Save to `blueprints/criteria/[artifact-type].md` using the Build-Criteria helper format. Frontmatter: `type: criteria-rubric`, `spectrum-position`, `consumers` (list this skill). The criteria file is the single source of truth — criteria don't dissolve into skill prose. They're standalone, lockable, auditable artifacts. (Decision 091.)

5. **Decide how the skill consumes the criteria.** At the generation step, the skill will Read the criteria file. Two consumption patterns:
   - **Self-audit** — the agent loads criteria, scores its own output, revises failures before presenting. Best when the agent generates without intermediate operator interaction.
   - **Operator review** — present the criteria alongside the output for operator evaluation. Best when operator taste is the primary quality mechanism.

   Note: behavioral writing instructions in the skill ("write concisely," "lead with insight," "avoid jargon") are INSTRUCTIONS, not criteria. Instructions stay in the skill. Criteria are binary evaluation rubrics that live in `blueprints/criteria/`.

Present the job statement, failure modes, and draft criteria to the operator. **Wait for approval before proceeding.** The operator's taste governs the criteria — the agent proposes, the operator decides what "good" means.

---

### Step 5: Determine Frontmatter

Walk through each field and decide:

| Field | Decision to Make |
|-------|-----------------|
| `name` | Lowercase, hyphenated. What would the operator type after `/`? |
| `description` | What it does + when to use it. Write for the operator scanning the `/` menu. |
| `argument-hint` | What arguments does it take? Omit if none. |
| `disable-model-invocation` | **Default to `true` for any skill that modifies files, calls APIs, or runs multi-step workflows.** Only leave as default (false) for reference/knowledge skills or simple utilities. |
| `context: fork` | Does the skill need operator interaction mid-workflow? If yes: don't fork. If it's heavy processing with no interaction: fork. |
| `allowed-tools` | Does the skill need tool restrictions? Usually no — only restrict for safety reasons. |

Present frontmatter decisions to operator.

---

### Step 6: Build SKILL.md

Read [skill-template.md](skill-template.md) for the starting skeleton.

**Writing rules:**
- **Prescribe, don't describe.** Every step tells the agent exactly what to do. "Create a new section" not "sections should be created." If a step could be interpreted two ways, it's not prescriptive enough.
- **Actionable quality gates.** Every operator checkpoint must present a concrete intermediate artifact — a draft, an analysis, a design — not a description of what will be produced. The operator reacts to work they can see, not plans they can't evaluate. Write: "Present [specific artifact] to operator. **Wait for operator decision before proceeding.**"
- **Anchor generation to prior approvals.** Generation/composition instructions must reference the specific operator-approved output from a prior step — not the artifact type generically. "Compose a brief matching the job statement, failure modes, and criteria the operator approved in Step 4" — not "Write a content brief."
- **Inline what the agent needs.** Bash commands, file paths, format specifications — put them in the step where they're used, not in a reference section the agent has to go find.
- **Degradation paths.** In the Error Handling section, for each external dependency (context docs, APIs, tools), state what happens when it's missing. At minimum, one fallback path for the skill's primary dependency. "If Gmail MCP is unavailable, compose the email as `artifacts/YYYY-MM-DD-topic-email.md` instead." Not just an error message — a degradation path.
- **Reference quality criteria.** For skills with a quality loop (Step 4): at the generation step, include a Read instruction for the criteria file produced in Step 4 (`blueprints/criteria/[name].md`). For self-audit skills, the agent reads criteria, scores output, and revises before presenting. For operator-reviewed skills, present criteria alongside output. Behavioral writing instructions ("write concisely," "avoid jargon") stay inline — these are instructions, not criteria.
- **Clear done state.** The last section defines what "finished" looks like — what files exist, what's been updated, what to present to the operator.

---

### Step 7: Build Supporting Files

For each supporting file listed in your package design (Step 3):

1. **State its purpose** in the first line or a brief header — what is this file and when does the agent load it?
2. **Write the content.** Reference material should be complete enough that the agent doesn't need to look elsewhere.
3. **Verify the reference link** in SKILL.md points to this file and says when to load it.

No orphaned files — every file in the skill directory must be referenced from SKILL.md.

**Convention: Create `roadmap.md`.** Every skill gets a `roadmap.md` companion file for V2+ ideas and future enhancements. This captures ideas that surface during build or use but aren't in scope for the current version. Ideas stay local in `roadmap.md` until they're mature enough to promote to the system backlog (`_system/backlog.md`) as a task. Seed it with anything that came up during Steps 1-6 that was deferred.

---

### Step 8: Wire Into the System

1. **Update consuming commands.** Which commands route to this workflow? Update their routing tables to reference the skill by name (e.g. the CLAUDE.md routing table gets a row pointing at the new skill).
2. **Blueprint migration.** If this skill migrates a blueprint, add a note to the blueprint: "Migrated to `.claude/skills/<name>/` — skill is the active workflow. Blueprint retained as design history."
3. **Backlog.** Mark the skill-building task as done. Check if completing this skill unblocks other tasks.

---

## Phase 2: Review

**Do not ship the skill without completing this phase.**

Read [quality-checklist.md](quality-checklist.md). Evaluate the skill you just built against every criterion.

**Section A (Structural Quality):** All 13 criteria apply to every skill.
**Section B (Output Quality):** 6 criteria apply only to deliverable-producing skills. Mark N/A for utility skills.

For each criterion, assess:
- **Pass** — meets the standard, no changes needed
- **Needs work** — state the specific issue

Fix all "needs work" items. Then present the full review to the operator with your assessment for each criterion.

---

## Error Handling

- **Skill name conflict:** Before creating the skill directory, check if `.claude/skills/<name>/` already exists. If it does, inform the operator and ask whether to overwrite, rename, or abort.
- **Source workflow too immature:** If Step 2 assessment reveals low maturity (few reps, unstable steps, no quality gates), recommend the operator capture the workflow as a blueprint first and iterate manually before promoting to a skill. Don't build a skill from a workflow that's still being figured out.
- **Consuming command has no routing table:** If Step 8 identifies a consuming command that doesn't have a routing table or skill-awareness section, flag it to the operator. Create a backlog task to add skill routing to that command rather than blocking the skill build.

---

## After Both Phases

1. **Summarize** what was built: skill name, file count, what it does, which commands consume it.
2. **Recommend testing.** The operator should run the skill on a real task before considering it validated. A skill isn't proven until it's been invoked and produced good output.

---

## Permissions

This skill uses only Read, Edit, and Write tools within the project directory. No Bash commands, network access, or MCP tools required.

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Write: `.claude/skills/**` | Create new skill packages |
| Files | Edit: `.claude/commands/**` | Update consuming command routing tables |
| Files | Edit: `_system/backlog.md` | Mark tasks done, create follow-up tasks |

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
