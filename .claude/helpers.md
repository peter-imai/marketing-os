# Shared Helpers

Reusable procedures referenced by commands and skills. Each section is a self-contained procedure that the agent reads and executes when directed.

**Reference convention:** Commands and skills point here by saying:
> Read and execute the procedure at `.claude/helpers.md#Section-Name`.

**Admission criteria:** A procedure earns a place here when it's (1) duplicated across 2+ consumers, (2) stable, (3) >5 lines, and (4) works across contexts with different inputs.

---

## Route-Knowledge-To-Destination

Determine where a piece of knowledge belongs in the system and route it there. Used during any session where reusable knowledge surfaces — not just shutdown.

**Procedure:**

1. Identify what kind of knowledge this is:
   - **Marketing domain knowledge** (how cold email works, campaign strategy, market dynamics) → Check `resources/marketing/index.md` for the relevant domain. Add to the domain file, or create one if it doesn't exist. Update the expertise index entry (depth, coverage, gaps).
   - **Practitioner convention** (a pattern for how to work, a session management technique, a quality pattern) → Route to a relevant blueprint or system doc. General patterns go in `blueprints/`.
   - **Architecture insight** (a design decision, a principle, a system pattern) → Route to `_system/decisions/` if it's a decision, `_system/system-architecture.md` if it's a structural insight, CLAUDE.md if it's a behavioral rule.
   - **Client intelligence** (what we learned about a specific client, their market, their preferences) → Route to the relevant context document (engagement-strategy.md, marketing-strategy.md, or context/ files).
   - **Tool learning** (how a tool behaves, limitations, cost data, gotchas) → Route to `tools/index.md` for selection-relevant info, or `tools/[name]/profile.md` for operational depth.

2. If the destination file exists, read it first. Add the knowledge in the right section. Don't duplicate what's already there — update or extend existing entries.

3. If you're unsure which category applies, ask the operator: "This seems like [X] — should it go to [destination], or do you see it differently?"

4. After routing, briefly confirm what was added and where: "Added [summary] to [file]."

---

## Capture-Backlog-Item

Add a new task to the appropriate backlog with proper formatting.

**Procedure:**

1. Determine which backlog:
   - **System-level** (architecture, conventions, skills) → `_system/backlog.md`
   - **Client-level** (deliverables, campaigns, client-specific work) → `clients/[client]/backlog.md`

2. Assign the next task number (check the task counter at the bottom of the backlog). Include: priority (P0-P3), status (`ready` unless it has dependencies), date added.

3. Write a clear subject line in imperative form: "Build X," "Design Y," "Research Z" — not "X needs to be built."

4. **Cluster check:** Does this task belong to an existing cluster? If yes, add it to that cluster's ordered list in the right sequence position. If you're creating 2+ related tasks at once, form a new cluster — give it a name, one-line goal, cluster ID (next C-number), and ordered task list.

5. If the task needs design context (more than a subject line to understand), add a section to `_system/task-notes.md` with the heading `### T-[N]: [Subject]`. Include: what the task is, why it matters, key design questions, and what "done" looks like.

6. Check for dependency relationships. Within a cluster, sequence handles dependencies. For cross-cluster or standalone dependencies, note the blocking relationship.

7. Update the task counter (and cluster counter if new cluster created) at the bottom of the backlog file.

---

## Load-Client-Strategy-Context

Load the governing strategy documents for the active client engagement. Commands supply the specific file paths — this helper provides the procedure.

**Inputs (provided by the calling command):**
- Engagement strategy path (e.g., `clients/acme/engagement-strategy.md`)
- Marketing strategy path (e.g., `clients/acme/marketing-strategy.md`)
- Any additional context files the command specifies

**Procedure:**

1. Read the **engagement strategy** document. This is the relationship layer — goals, stakeholders, dynamics, success criteria, concerns. Internalize the people and the politics, not just the deliverables.

2. Read the **marketing strategy** document. This is the execution brain — positioning, product understanding, audience, content strategy, growth thesis, active hypotheses.

3. **Parse frontmatter on both documents.** Each should have a YAML frontmatter block. Extract `status`, `last-updated`, and `updated-by`. Then apply these checks:

   **Staleness check:** Compare `last-updated` to the current session number. Strategy docs have a 15-session staleness threshold.
   - If the gap exceeds the threshold → flag: `"⚠️ [Doc title] last updated Session {N} ({gap} sessions ago). May need review."`
   - If within threshold → no flag needed.

   **Trust calibration from `status`:**
   - `working-notes` → Unreviewed. May contain gaps or assumptions. Treat as directional, not authoritative.
   - `operator-reviewed` → Validated. Treat as current doctrine unless contradicted.
   - `doctrine` → Established and stable. Changes require explicit operator decision.

   **Trust calibration from `updated-by`:**
   - If `agent` and status is not `doctrine` → note: `"Last update was agent-synthesized — operator hasn't validated."`
   - If `operator` or `joint` → no flag.

4. After reading both, you should be able to articulate:
   - What is this engagement trying to accomplish?
   - What are the key stakeholder concerns?
   - What marketing approach are we taking and why?
   - What hypotheses are we testing?

   If you can't, flag the gap.

5. Throughout the session, when new information arrives, check it against both levels: does this change how we think about the engagement or the strategy?

---

## Load-Marketing-Domain-Expertise

After identifying the session's activity, check whether the system has accumulated domain expertise relevant to this work.

**Procedure:**

1. Read `resources/marketing/index.md` — the system's catalog of marketing domain knowledge.

2. Identify which domains are relevant to the current activity. Match the activity to domains listed in the index.

3. For each relevant domain that has a domain file with meaningful depth:
   - Load the domain file.
   - Briefly note: "Loaded [domain] expertise — [one-line summary]."

4. For each relevant domain with no file or only a placeholder:
   - Note: "We don't have deep domain expertise for [domain] yet. If this session produces reusable knowledge, we can start building it."

5. If no domains are relevant, skip silently.

---

## Route-Action-Items-To-Tasks

Extract action items with external deadlines and create Google Tasks. Distinction: **backlog items** are internal work. **Tasks** are commitments to other humans.

**Procedure:**

1. Review the conversation for action items with **external deadlines** — commitments to clients, collaborators, stakeholders.

2. For each item, draft:
   - **Title** — imperative, specific
   - **Due date** — ISO format. Convert relative dates to absolute.
   - **Notes** — one line of context

3. Present proposed tasks to the operator. Wait for confirmation.

4. On confirmation, create via MCP: `mcp__google-workspace__manage_task` with the operator's default task list.

5. Confirm what was created.

**When to invoke:**
- End of a meeting debrief
- When the operator requests it
- When commitments with deadlines surface — propose, don't assume

---

## Publish-To-Google-Docs

Push a markdown deliverable directly to Google Docs as a formatted document via the Google Workspace MCP. Headings, bold, italic, lists, tables, blockquotes, and links transfer cleanly. No CLI, no clipboard, no pasting.

**Prerequisites:** Google Workspace MCP authorized for the operator's Google account (one-time OAuth). If unauthorized, the MCP returns an authorization URL — present it, wait for the operator to complete OAuth, retry.

**Procedure:**

1. **Get the source.** Either a file path or markdown content from the current conversation.

2. **Call `mcp__google-workspace__import_to_google_doc`:**
   - `user_google_email`: the operator's Google account
   - `file_name`: doc title (the `.md` extension is ignored)
   - `source_format`: `"md"`
   - `content`: the markdown string (for inline content), OR
   - `file_path`: absolute path (for files on disk)

   Google Drive performs the conversion server-side — markdown → native Google Doc with formatting preserved.

3. **Share the result.** The MCP returns a Drive link. Give the URL to the operator.

**What it handles:** Headings (H1-H6), bold, italic, bold+italic, bullet lists, ordered lists, nested lists, tables (with bold headers), paragraphs, blockquotes, links. YAML frontmatter is included as text — strip it from `content` before sending if you don't want it visible.

**Styling:** Default Google Docs theme — clean and respectable, not design-forward.

**Fallback — Copy-To-Clipboard:** If MCP is unavailable or the operator prefers clipboard:
1. Convert markdown to semantic HTML (encode special chars as HTML entities)
2. Write to temp file and run: `textutil -format html -convert rtf "$TMPFILE" -stdout | pbcopy && rm "$TMPFILE"` (requires sandbox bypass)
3. Tell operator: "Formatted content is on your clipboard — Cmd+V into Google Docs."

**When to invoke:**
- Operator says "send to Google Docs," "publish to Docs," "create a Doc from this"
- A skill produces a deliverable the operator wants in Google Docs
- After any document composition

---

## Build-Criteria

Build validated binary scoring criteria for a marketing artifact or workflow output. Loads the scored iteration toolkit and walks through the decision-to-criteria flow.

**When to invoke:**
- Building a new skill and need quality criteria
- Adding quality checks to an existing workflow
- Operator asks to "score," "evaluate," or "add criteria to" an output type
- Before any scored iteration work — the criteria must exist before looping

**Procedure:**

1. **Consult the decision matrix.** Read `blueprints/scored-iteration-decision-matrix.md` if it exists. Classify the application (artifact optimization / analytical sharpening / system infrastructure / adversarial resilience). Score the 5 heuristics. Determine spectrum level (2-3 self-audit / 10-20 scored / 50-100 overnight). Present recommendation to operator: "This looks like [family] at [level] because [reasons]. Worth building criteria?"

2. **Follow the criteria development blueprint.** Read `blueprints/criteria-development.md` if it exists. Execute all 4 phases in order:
   - Phase 1 (15 min): Define artifact job + 5 failure modes + spectrum position
   - Phase 2 (20 min): Select patterns from the 5-pattern menu, draft criteria
   - Phase 3 (15 min): Tier into prerequisites/optimizers, write in yes/no format
   - Phase 4 (20 min): Meta-evaluate against calibration set (known-good + known-bad outputs)

3. **Reference the worked example.** If the operator hasn't built criteria before, load `blueprints/criteria/voice.md` as a concrete reference for what a finished criteria file looks like — prerequisite/optimizer split, binary yes/no format.

4. **Write the criteria file.** Save to `blueprints/criteria/[artifact-type].md`. Include frontmatter: `type: criteria-rubric`, `spectrum-position: [self-audit | quality-gate | deep-optimization]`, `consumers: [skills/workflows that use these criteria]`, plus standard fields (description, status, created, etc.). The file is the single source of truth — criteria don't dissolve into skill prose.

5. **Lock.** Once validated, the criteria file is locked — the iteration loop can never edit it. Future changes require re-running Phase 4 meta-evaluation.

---

## Quality-Experiments

Convention for quality experiment integration in deliverable-producing skills. Referenced by all skills with a Quality Experiments section.

**Before running a skill:**
1. Check `_system/quality-engine-map.md` for active "Ready to Try" experiments for this skill (if the file exists)
2. If one exists, note what it asks and incorporate it into this run

**After running:**
- `/done` logs your observation about the experiment's effect and surfaces it in the wrap-up
- The operator decides: **keep** (promote to permanent instruction in SKILL.md, clear from map), **modify** (adjust the map entry), or **drop** (clear from map, note what didn't work)

If no experiment is active for this skill, skip.

---

## Check-For-Doc-Logs

Detect parent docs with companion `*-log.md` files that were touched this session, draft a log entry per detected pair, and surface as a proposal. Both `/done` and `/debrief` invoke this procedure — one source of truth for log-write detection.

**Inputs (provided by the calling command/skill):**
- **Touched files list** — output of `git diff --name-only` or explicit list of files modified.
- **Session number** — current session for the entry header.
- **Trigger source** — `session` (from `/done`) or `meeting` (from `/debrief`). Determines entry framing.

**Procedure:**

1. **Build the parent-log map.** For each touched file, check whether a sibling file exists at `{parent-folder}/{parent-name}-log.md`. Rule: `core.md` → `core-log.md`, `engagement-strategy.md` → `engagement-strategy-log.md`.

   Derive the candidate log path by inserting `-log` before `.md`. Verify it exists.

2. **Skip non-parent touches.** A touched file with no sibling log is not in scope. Skip silently.

3. **Verify the log file is `type: log`.** Read the candidate log's frontmatter. If `type` is not `log`, skip — it's a name collision.

4. **Draft one entry per detected pair.** Format:

   ```
   ### YYYY-MM-DD · S{N} · {Type}
   **What:** One-line fact about what changed in the parent doc.
   **Why:** Reasoning — what drove the change.
   **Implication:** Forward hook — what this enables or changes downstream.
   ```

   **Type selection** (`Decision` | `Hypothesis` | `Signal` | `Shift` | `Dead end`):
   - **Decision** — a choice was made
   - **Hypothesis** — trying something, outcome unknown
   - **Signal** — observation changed understanding
   - **Shift** — direction change at the meta level
   - **Dead end** — tried X, didn't work, here's why
   - Skip `Snapshot` — that type is for retroactive bootstrap only

5. **Surface the draft(s) for approval:**

   > "{Parent doc name} touched. Propose log entry:
   > [draft entry]
   > Apply / edit / skip?"

   - **Apply** → Find the `<!-- log-insert -->` sentinel in the log file. Insert the new entry on the line immediately after the sentinel. Update the log's `last-updated` field.
   - **Edit** → Accept the operator's wording, write that.
   - **Skip** → Do not write.

6. **Write protection.** Never write to a log without explicit operator approval.

7. **If no parent-log pairs detected, skip silently.**

**When invoked:**
- `/done` shutdown (session-driven entries)
- `/debrief` wrap-up (meeting-driven entries)

---

## Build-Hook

Create a new Claude Code hook — event-triggered shell script that runs at session start, prompt submit, notification, or other lifecycle events. Use when something needs to fire mechanically without the agent remembering.

**When to use:**
- A pattern needs enforcement beyond agent instruction
- The operator wants ambient automation (recurring checks, reminders, context injection)

**Procedure:**

1. **Decide the event.** Choose one:
   - `SessionStart` — matcher `""` = always fires; matcher `compact` = only after auto-compaction
   - `UserPromptSubmit` — fires on every user prompt. Use sparingly.
   - `Notification` — fires on desktop notifications
   - `PostToolUse` / `PreToolUse` — fire around tool execution
   - `Stop` — fires when the agent finishes responding

2. **Name the script.** Convention: `.claude/hooks/{verb-noun}.sh`. Examples: `cadence-check.sh`, `done-enforcement.sh`, `compact-reinject.sh`.

3. **Create the script** at `.claude/hooks/{name}.sh`. Required elements:
   - Shebang: `#!/bin/bash`
   - Exit code: `exit 0` for normal. Nonzero can block events (`UserPromptSubmit`, `PreToolUse`).
   - Use `$CLAUDE_PROJECT_DIR` for paths — never assume cwd.
   - Make it idempotent if it fires repeatedly.

4. **Make executable:** `chmod +x .claude/hooks/{name}.sh`

5. **Register in `.claude/settings.json`** under `"hooks"`:
   ```json
   "{EventName}": [{
     "matcher": "",
     "hooks": [{ "type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/{name}.sh" }]
   }]
   ```

6. **Test manually:** `bash .claude/hooks/{name}.sh`

7. **Update `_system/system-architecture.md`** — add the hook with a one-line description.

**Failure modes to avoid:**
- Non-executable script (silent failure)
- Hardcoded paths (use `$CLAUDE_PROJECT_DIR`)
- Slow hooks on `UserPromptSubmit` (fires every turn)

---

## Log-Decision

Record a design decision in `_system/decisions/` with canonical structure. Used when an architectural choice is made that will outlive the current session.

**When to use:**
- An architectural choice changes how the system is built or operated
- An alternative was considered and rejected for reasons worth preserving
- A convention, pattern, or rule was created or retired
- A recurring question was resolved

**Procedure:**

1. **Check the counter.** Read the decision counter at the bottom of `_system/backlog.md` (`Decision counter: {N}`). Next decision is D{N+1}.

2. **Name the file:** `_system/decisions/{YYYY-MM-DD}-{N}-{slug}.md`

3. **Required frontmatter:**
   ```yaml
   ---
   type: decision
   description: "One-line — what was decided and why it matters"
   status: operator-reviewed
   created: {date}
   ---
   ```

4. **Required body sections:**
   - **Heading:** `# D{N}: {Title}`
   - **Decision** — what was decided, concrete and unambiguous
   - **Rationale** — why this choice, including evidence
   - **Alternatives Considered** — numbered list with specific rejection reasons
   - **What Would Make Us Revisit** — concrete, testable trigger conditions

5. **Increment the decision counter** in `_system/backlog.md`.

---

## Meeting-Debrief-Protocol

**This procedure has been promoted to a standalone skill.** Invoke `/debrief` for all meeting transcript processing. The skill handles context detection, signal analysis, operator discussion, update routing, and preference management.

For email composition after a debrief, use `/compose` (email format will be auto-suggested).
