# Skill Template

Reference structure for building a new SKILL.md. Adapt to fit the specific workflow — not every section applies to every skill.

**Design conventions:** progressive disclosure, helpers, step-file sharding, and subagent strategy.

---

## Frontmatter

Place at the very top of SKILL.md between `---` markers.

| Field | Guidance |
|-------|----------|
| `name` | Lowercase, hyphenated — what the operator types after `/` |
| `description` | What the skill does + when to use it — written for the operator scanning the menu |
| `argument-hint` | Expected arguments, e.g., `[youtube-url]` or `[workflow-name]`. Omit if none. |
| `disable-model-invocation` | `true` ONLY for dangerous/irreversible operations (deploy, push, delete) where auto-invocation would be harmful even with operator gates. Omit for standard workflow skills — use built-in operator approval gates (wait steps, triage decisions) for safety instead. Note: `true` removes the skill from context entirely — Claude won't know it exists, and `/skill-name` invocation will fail. |

Optional fields: `context: fork` (isolated execution), `allowed-tools` (tool restrictions), `agent` (subagent type when forked).

---

## Complexity Assessment

Before building, determine the skill's complexity tier. This drives structural decisions:

| Tier | Criteria | Structure |
|------|----------|-----------|
| **Simple** | ≤3 short steps, no subagents | L1 only: everything in SKILL.md |
| **Medium** | 4+ steps, or subagent coordination | L1 + L2: SKILL.md orchestrates, step files contain detail |
| **Complex** | Multiple phases, deep reference material, output templates | All three levels: SKILL.md → step files → templates/resources |

**L1 budget:** SKILL.md stays under 5K tokens (~300-350 lines). If it's larger, move workflow detail to L2 step files.

---

## Sections to Include in SKILL.md (L1)

### Title + Summary
- H1 heading with the skill name
- One sentence describing what the skill does
- **Input:** what's needed to start
- **Output:** what's produced, with file paths
- **References:** links to supporting files with brief description of each

### Procedure Steps (for simple/medium skills)
- Each step is an H2: `## Step N: [Verb + Object]`
- Prescriptive instructions — what to do, not what should happen
- Inline bash commands, file paths, format specs where the agent needs them
- Quality gates at decision points: "**Wait for operator decision before proceeding.**"
- Steps separated by `---` horizontal rules for visual clarity
- For shared procedures (backlog routing, knowledge routing, strategy loading), reference `.claude/helpers.md#Section-Name` instead of inlining

### Step Routing (for sharded skills)
When steps are complex enough to warrant their own files (see Complexity Assessment), SKILL.md provides routing instead of inline procedures:

```markdown
## Workflow

1. Read the deliverable (if it exists) and check `stepsCompleted` in frontmatter for resumption.
2. Load and execute each step file in sequence:
   - `steps/step-01-[name].md` — [goal summary]
   - `steps/step-02-[name].md` — [goal summary]
   - `steps/step-03-[name].md` — [goal summary]
3. Never load multiple step files simultaneously. Complete each step before loading the next.
```

### Subagent Strategy (when applicable)
Include this section when the skill has operations that could run in parallel. Declare:

| Operation | Sequential/Parallel | Agent Type | Context Needed | Output |
|-----------|-------------------|------------|---------------|--------|
| [operation] | [choice + reasoning] | [general-purpose/Explore/Plan] | [what to pass] | [where it writes] |

**Coordination model:** How results get synthesized (file-based coordination, main-context synthesis, etc.)

For purely sequential skills, a brief note: "All operations are sequential — no subagent strategy needed."

### Error Handling
- H2 section listing known failure modes
- Each entry: **bold failure** followed by specific recovery action
- Grows with use — add failures as you encounter them

### After Completion
- Summary step: what was produced, counts, any issues
- Next action: what the operator can do next

---

## Step-File Scaffold (L2)

When a skill shards into step files, each step file follows this structure:

```markdown
---
step: [number]
title: "[Verb] [Object]"
next: steps/step-[N+1]-[name].md
output: [path to deliverable, if this step produces/updates one]
reads: [files this step needs to load]
writes: [files this step creates or updates]
---

# Step N: [Verb] [Object]

**Goal:** [Single sentence — what this step accomplishes]

## Rules

[Step-specific constraints only. Universal rules belong in SKILL.md.]

## Instructions

[Numbered prescriptive procedure. Quality gates inline.]

## Success Criteria

- [ ] [Checkable criterion]
- [ ] [Checkable criterion]

## Next

Update deliverable frontmatter: `stepsCompleted: [1, ..., N]`
Then read and execute `steps/step-[N+1]-[name].md`.
```

**Just-in-time loading rules (non-negotiable):**
1. Never load multiple step files simultaneously
2. Always read the entire step file before executing
3. Never skip steps or optimize the sequence
4. Always update deliverable frontmatter before loading next step
5. Never pre-read future steps to "plan ahead"

---

## Directory Structure

```
skills/<name>/
├── SKILL.md              # L1: orchestration + routing (<5K tokens)
├── steps/                # L2: step files (one per workflow phase)
│   ├── step-01-[name].md
│   ├── step-02-[name].md
│   └── ...
├── templates/            # L3: output scaffolds
├── resources/            # L3: deep reference, prompt libraries
└── roadmap.md            # V2+ ideas (every skill gets one)
```

Simple skills skip the `steps/`, `templates/`, and `resources/` directories entirely.

---

## Supporting Files

Each supporting file in the skill directory should:
1. **State its purpose** in the opening line — what is this file and when does the agent load it?
2. **Be referenced from SKILL.md** (or from the step file that uses it) at the point in the procedure where it's needed
3. **Contain complete reference material** — the agent shouldn't need to look elsewhere
