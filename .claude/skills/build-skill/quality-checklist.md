# Skill Quality Checklist

Evaluate a completed skill against these criteria. Used during Phase 2 of the `/build-skill` workflow.

**Two sections:**
- **Section A (Structural Quality):** 13 criteria. Apply to every skill.
- **Section B (Output Quality):** 6 criteria. Apply only to skills that produce deliverables, content, or analytical output. Mark N/A for utility skills.

A skill ships when all applicable criteria pass. For each criterion: **Pass** or **Needs Work** (with the specific issue).

---

## Section A: Structural Quality

## 1. Description Accuracy

**Standard:** The description accurately communicates what the skill does and when to use it.

**How to evaluate:** Read the description as if you're an operator scanning the `/` menu. Would you know when to invoke this? Does it match what the skill actually does? For skills with `disable-model-invocation: true`, the description only shows in the menu — optimize for operator comprehension. For auto-invokable skills, also ask: would the agent match this description to the right conversational triggers?

---

## 2. Invocation Control

**Standard:** The frontmatter's invocation settings match the skill's risk profile.

**How to evaluate:**
- Does the skill modify files, call APIs, or run multi-step workflows? → Should have `disable-model-invocation: true`
- Is it reference/knowledge content the agent should apply automatically? → Can use default (auto-invokable)
- Does it need operator interaction mid-workflow? → Should NOT have `context: fork`
- Does it do heavy isolated processing with no interaction? → Consider `context: fork`

**Failure mode:** A skill with side effects that's auto-invokable. This means the agent could decide on its own to start modifying files or running workflows.

---

## 3. Procedure Prescriptiveness

**Standard:** Every step tells the agent exactly what to do. No step requires the agent to interpret intent or make unstated assumptions.

**How to evaluate:** Read each step as a very literal assistant. Does it say what to do, or describe a concept and hope you figure out the action?

**Look for:**
- Verbs: "Create," "Read," "Present to operator" = prescriptive. "Should be," "is typically," "can be" = descriptive.
- Specifics: file paths, bash commands, format specs inline at point of use — not "look it up somewhere."
- Ambiguity: if a step could be interpreted two different ways, it fails.

---

## 4. Quality Gates

**Standard:** The skill has explicit pause points where operator judgment is required, and the agent cannot proceed without approval.

**How to evaluate:** Identify every point in the workflow where the operator should make a decision. Is there an explicit gate at each one? Look for: "Wait for operator decision before proceeding," "Present to operator and ask," "Do not proceed without approval."

**Scrutinize:** A skill where the agent runs end-to-end with no operator checkpoints. Is it genuinely fully automatable, or are decisions being made implicitly that the operator should own?

---

## 5. Error Handling

**Standard:** Known failure modes are documented with specific recovery actions.

**How to evaluate:** Has this workflow failed before? Are those failure modes listed? For each error entry: does the handling tell the agent what to DO (not just what went wrong)? Common gaps: network failures, missing dependencies, invalid inputs, permission issues.

**Failure mode:** A skill with no error handling section — unless the workflow is genuinely trivial with no known failure modes.

---

## 6. Supporting File Integration

**Standard:** Every supporting file is referenced from SKILL.md at the point where it's needed, and every reference resolves to an actual file.

**How to evaluate:**
- Check each `[link](file.md)` in SKILL.md — does the file exist?
- Check each file in the skill directory — is it referenced from SKILL.md?
- For each reference: is it at the right point in the procedure? Would the agent load it too early (wasting context) or too late (missing needed information)?

**Failure mode:** Orphaned files (exist in directory but unreferenced from SKILL.md).

---

## 7. Size Discipline (Progressive Disclosure L1)

**Standard:** SKILL.md is under 500 lines AND under 5K tokens. It serves as the L1 orchestration layer — routing, quality gates, error handling, done state. Detailed workflow logic lives in L2 step/phase files. Templates, examples, and deep reference live in L3 resource files.

**How to evaluate:** Count the lines and estimate token count (~15 words/line × line count ÷ 0.75 ≈ tokens). If over budget, identify what can move to L2 step files (workflow detail) or L3 supporting files (reference material) without breaking the orchestration flow. The routing logic and quality gates stay in SKILL.md; everything else moves out.

**Three-level model (progressive disclosure):**
- **L1: SKILL.md** (<5K tokens) — loaded on invoke. Orchestration only.
- **L2: Step/phase files** — loaded on demand, one at a time. Detailed workflow.
- **L3: Templates, resources** — loaded when a specific step needs them.

Not every skill needs all three levels. Simple skills (≤3 short steps, no subagents) stay L1-only. Shard when SKILL.md exceeds budget or when steps are complex enough to benefit from focused context.

---

## 8. Done State

**Standard:** The skill clearly defines what "finished" looks like — what exists, what's been updated, what to present to the operator.

**How to evaluate:** Read the last section of the skill. Would the agent know when to stop? Is there a summary step? Does the skill leave the system in a defined state (files created, indexes updated, backlog marked)? A skill that trails off without a clear ending fails this criterion.

---

## 9. System Integration

**Standard:** The skill is wired into the commands and systems that consume it.

**How to evaluate:**
- Which commands should reference this skill in their routing tables? Do they?
- If this skill migrates a blueprint, is the blueprint marked with migration status?
- Is the backlog updated (task marked done, dependent tasks unblocked)?
- Would the next operator who runs the relevant command discover this skill exists?

---

## 10. No Duplication

**Standard:** The skill doesn't duplicate context that consuming commands already provide. Common procedures use shared helpers rather than inline copies.

**How to evaluate:** Read the consuming command(s). What context do they load at session start? If the skill re-explains the same information, that's wasted context tokens. The skill should assume the command has set up the session correctly. If the skill needs specific context that no command provides, load it from a supporting file — don't inline it.

Also check: does the skill contain procedures that already exist in `.claude/helpers.md`? Knowledge routing, backlog capture, strategy loading, and meeting debriefs have shared helpers. Reference them rather than duplicating.

---

## 11. Subagent Strategy

**Standard:** Skills that use subagents (or have operations that could run in parallel) declare their parallel execution strategy explicitly.

**How to evaluate:** Are there operations in this skill that could run independently? If yes, is there a Subagent Strategy section (in SKILL.md for flat skills, or documented at the point of use for sharded skills)? Does it specify: which operations parallelize vs. must be sequential, agent type for each (general-purpose/Explore/Plan), what context each subagent receives, where subagents write output, and how results get synthesized?

For skills with no parallelizable operations, a brief note is sufficient: "All operations are sequential — no subagent strategy needed."

**Critical check:** Does the subagent prompt include all necessary context? Subagents cannot see the main conversation, session frame, or prior teaching checkpoint reactions. Everything they need must be passed explicitly.

**Failure mode:** A skill that launches subagents without declaring what context they receive. The skill works when the builder runs it (because they know what's needed) but fails when someone else invokes it (because the subagent gets insufficient context).

---

## 12. Permission Declaration

**Standard:** The skill declares all platform permissions it requires for autonomous execution in a `## Permissions` section.

**How to evaluate:** Does SKILL.md have a `## Permissions` section with a table covering: Bash commands the skill invokes, network domains it needs, notable file paths it reads/writes, Claude Code tools beyond Read/Edit/Write, and MCP tools?

**Check each category:**
- **Bash** — Are all shell commands listed with glob patterns matching `settings.json` syntax?
- **Network** — Are all external domains listed (for sandbox `allowedDomains`)?
- **Files** — Are notable read/write paths documented (beyond the skill's own directory)?
- **Tools** — Are WebSearch, WebFetch, Task tool usage declared?
- **MCP** — Are MCP tool patterns listed?

Cross-reference against `settings.json`: are the declared requirements already allowed? If not, flag for the operator.

**Skills with no special requirements** still need the section — state explicitly: "This skill uses only Read, Edit, and Write tools within the project directory. No special permissions required."

**Failure mode:** A skill with undeclared Bash commands or network access. The operator configures permissions based on what's declared — undeclared requirements surface as unexpected prompts at runtime, or worse, silent sandbox failures.

---

## 13. Source Material Identification (Content-Producing Skills)

**Standard:** Skills that produce content carrying the operator's voice identify the operator source material they compose from and load it at the right step.

**How to evaluate:** Does this skill produce briefs, emails, posts, scripts, or any output that represents the operator's positions or voice? If yes, check:
- Are the operator source docs named (convictions, marketing principles, positioning, voice guides, system philosophy — whichever is relevant)?
- Are they loaded at the step where generation happens (not just at startup)?
- Do the generation instructions say "compose from" or "curate and assemble" — not "generate" or "brainstorm from scratch"?

**For skills that don't produce content:** This criterion is N/A. Note it and move on.

**Failure mode:** A skill that generates bland, generic language when dramatically sharper operator-authored lines already exist in the system. The agent's invented framing is almost always weaker than the operator's earned articulation.

**The test:** Could the operator point to a line they already wrote that says the same thing better? If yes, the skill should have found and used that line.

---

## Section B: Output Quality (Deliverable-Producing Skills)

These criteria apply to skills that produce deliverables, content, or analytical output — skills where the output's quality directly affects the operator or an external audience. Utility skills (transcript-acquisition, install-debrief) are covered by the 13 structural criteria above; mark these N/A.

---

## 14. Context Precision

**Standard:** Every generation/composition step names specific source files loaded at the point of generation. Reference material is deferred until the step that needs it — not loaded at startup.

**How to evaluate:** Find each step where the skill generates or composes output. Does it name the files it loads? Are those files loaded at THAT step (not earlier)? Does the skill avoid loading all reference material upfront?

**Look for:**
- Generation steps with no source file references — the agent will generate from general knowledge
- Startup loads that include reference material not needed until a later step — context bloat that degrades reasoning by the time generation happens
- Source files loaded at the wrong step — positioning docs loaded for a structural step, missing when the composition step runs

**Failure modes:** Context starvation (too little context at generation, agent invents) and context bloat (too much context everywhere, agent drowns).

---

## 15. Actionable Checkpoints

**Standard:** Every operator checkpoint presents a concrete intermediate artifact — not a description of intent or a plan the operator can't yet evaluate.

**How to evaluate:** Read each quality gate in the skill. What does the operator SEE when the gate fires? A draft? An analysis? A design? Or a plan for what will be produced? Gates that present "here's what I'm going to do" are rubber-stamp traps — the operator can't make a real judgment until they see actual output.

**The test:** At each gate, could the operator say "no, change X specifically" based on what they see? If they can only say "sounds good" or "I guess so," the gate isn't actionable.

**Failure mode:** Gates placed where the operator approves a plan, then the real quality issue surfaces 3 steps later when the plan becomes an artifact.

---

## 16. Degradation Paths

**Standard:** The skill defines what happens when expected inputs are missing — context docs, tools, APIs, MCP servers. At least one primary dependency has a fallback path, not just an error message.

**How to evaluate:** List the skill's external dependencies: files it expects to exist, tools it calls, APIs it connects to. For each: does the skill say what to do when it's missing? Is the fallback a viable alternative (file-based output instead of API call) or just "warn the operator and stop"?

**Look for:**
- Skills that assume all context docs exist — what happens for a new client with no positioning doc?
- Skills that assume MCP servers are available — what happens if Gmail is down?
- Hard stops where a graceful degradation would work — "write to file instead of API" patterns

**Failure mode:** The skill errors out or silently produces garbage when a dependency is missing, instead of falling back to a viable alternative.

---

## 17. Brief Anchoring

**Standard:** Generation/composition instructions reference the specific operator-approved output from a prior step — not the artifact type generically.

**How to evaluate:** Find each generation instruction. Does it say "compose a [artifact type]" (generic) or "compose based on [the job statement, failure modes, and criteria the operator approved in Step N]" (anchored)? Anchored instructions create a chain: the operator approves intermediate output → the skill uses that approved output as the specification for generation → the final output traces back to operator-approved decisions.

**The test:** If the prior step's output were different, would the generation instruction produce different output? If the instruction is generic enough to produce the same thing regardless of prior steps, it's not anchored.

**Failure mode:** The agent drifts toward what's easy to generate rather than what the operator specified. Generic instructions give the agent permission to drift.

---

## 18. Progressive Reveal

**Standard:** The skill shows intermediate output at natural phase boundaries, giving the operator the ability to course-correct before the final deliverable.

**How to evaluate:** Map the skill's phases. At each major transition (research → analysis, analysis → composition, composition → formatting), does the operator see what was produced? This is distinct from quality gates (which ask permission) — progressive reveal shows work so the operator's taste can enter the loop.

**Look for:**
- Skills that run end-to-end and present only the final output — the operator must accept or reject the whole thing
- Skills where the operator's first look at real output is the last step

**Failure mode:** The operator sees the final deliverable and has to reject it entirely because a decision in step 2 was wrong — but they never got to see step 2's output.

---

## 19. Quality Criteria Deployment

**Standard:** The skill has a corresponding criteria file in `blueprints/criteria/` containing 2-3 binary quality criteria specific to its output type, referenced at the generation step. (Decision 091.)

**How to evaluate:**
1. Does a criteria file exist in `blueprints/criteria/` that lists this skill as a consumer?
2. Does the skill's generation step include a Read instruction for that criteria file?
3. Are the criteria in the file binary (yes/no), specific to this output type, and tiered (prerequisite/optimizer)?

**Two valid consumption patterns:**
- **Self-audit** — the agent reads criteria, scores its own output, revises failures before presenting. Best when the agent generates without intermediate operator interaction.
- **Operator review** — present criteria alongside output for operator evaluation. Best when operator taste is the primary quality mechanism.

**Criteria vs. instructions:** Behavioral writing instructions in the skill prose ("write concisely," "lead with insight," "avoid jargon") are INSTRUCTIONS — they guide execution. Criteria are binary evaluation rubrics in standalone files — they score output. Both are valid. They're different things. Don't confuse embedded instructions for deployed criteria.

**Look for:**
- Skills with no criteria file — no binary quality teeth at the generation step
- Criteria dissolved into skill prose as vague behavioral instructions ("ensure specificity") instead of living in a scoreable file
- Self-audit loops bolted onto skills that already have operator discussion steps — redundant process

**Failure mode:** Agent behavior drift — the agent's natural tendencies go unchecked because no scoreable criteria exist. OR: criteria dissolution — binary rubrics get softened into behavioral instructions and lose their teeth.

**Where criteria come from:** Step 4 of Phase 1 (Design the Quality Loop) produces criteria and writes them to `blueprints/criteria/`. The Build-Criteria helper (`helpers.md#Build-Criteria`) is the invocation mechanism. If the skill was built before this convention, this criterion prompts creating a criteria file retroactively.
