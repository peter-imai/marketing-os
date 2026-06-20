# Starter Kit Changelog

All notable changes to the Marketing OS starter kit.

---

## v5.0 — 2026-05-29

The "austerity + onboard simplification" release. Main-system rewrite of CLAUDE.md (S752, −78.9%) propagated to kit. Install simplified to three steps: unzip → open in VS Code → `/start`. F-95 output-style setup now handled automatically by `/start` Step 0.

### Added
- **`START-HERE.md`** at kit root — single entry doc for new operators. Install + first session + key commands + when-things-feel-off. Replaces the old manifesto + scattered onboarding signposts.
- **`/align` command** — alignment protocol (interview operator before committing to a direction). Required by the new CLAUDE.md Hard Rules → Drafting → "Align first" gate (D174).
- **`/new-project` skill** — interactive client/workspace onboarding. Scaffolds folder, asks foundation questions, creates `/[client-name]` slash command.
- **`/build-skill` skill** — criteria-first skill building. Defines what good output looks like, then builds the skill, then proves it meets the standard.
- **`/market-research` skill** — phased research (ICP, market context, competitive landscape, buyer personas, customer evidence, niche data sources). Produces an actionable synthesis.
- **`.claude/hooks/no-newline-bash.sh`** — PreToolUse hook blocking multi-line Bash commands that defeat the permission allowlist. Heredoc-exempted. Wired in settings.json.
- **`_system/system-philosophy.md`** — principles, concepts, and system health model.
- **`_system/build-rules.md`** — durable design constraints.
- **`_system/artifact-creation-principles.md`** — naming, scope, hierarchy.
- **`.claude/skills/connect-tool/roadmap.md`** — flow roadmap for connect-tool.

### Changed
- **`CLAUDE.md`** — full reshape to match main-system austerity rewrite (S752). 163 → 111 lines. Six-field frontmatter (`cap-lines: 200`, `cap-words-per-bullet: 25`). Hard Rules grouped by role (Session / Drafting / Knowledge / Tools / Files). Routing table genericized (no operator's hardcoded clients). Orchestrator/content/ingest commands deliberately excluded from kit routing — held back as advanced primitives.
- **`.claude/commands/start.md`** — new **Step 0** auto-installs `~/.claude/output-styles/base.md` if missing. No manual `mkdir + cat` for the operator. F-95 fix lands transparently.
- **`.claude/settings.json`** — `outputStyle: "Base"` added (F-95 fix). `no-newline-bash` PreToolUse hook wired. Operator-only `corpus-archive` / `corpus-analysis-trigger` SessionStart hooks dropped.
- **`_system/frontmatter-convention.md`** — stub → full (~580 lines). Type vocabulary, governance, Type Lifecycle, Pattern Capture Protocol.
- **`_system/marketing-principles.md`** — stub → full (162 lines).
- **`curriculum/playbook.md`** — editorial pass for clarity + economy. `/align`, `/build-skill`, `/market-research` added to the command roster. Pointer to `START-HERE.md` at the top for first-time readers.

### Removed
- **`curriculum/manifesto.md`** — core folded into `START-HERE.md` preface. Eliminates the "which doc do I read first?" problem.
- **`_system/system-map.md`** — operator-specific structural inventory; not appropriate as a kit doc. New operators grow their own structure organically.
- **`_system/system-architecture.md`** — obsolete (superseded by `system-philosophy.md` + `build-rules.md` in main; kit no longer ships it).

### Scrubbed
- **Client-specific references** stripped from all `_system/` docs. Examples in `frontmatter-convention.md`, `tool-integration-convention.md`, `build-rules.md`, `marketing-principles.md`, `system-philosophy.md` now use generic placeholders (`acme`, `your-agency`, `[your-client]`).

### Notes
- **Helpers unchanged this release.** Main system's three new helpers (Check-Pending-Reviews, Build-Convention, Build-Rule) are governance plumbing for mature systems — held back until kit users have base reflexes.
- **Jordan Crawford market-research files retained in the kit** (`resources/jordan-crawford/market-research/01-client-icp.md`, `02-market-context.md`, `03-buyer-persona.md`). Main system deleted these; kit keeps them as starter substance for new operators.
- **Git tag**: `kit-v5.0` (enables `tools/kit-sync/check.py --since kit-v5.0` for v5→v6 drift detection — `kit-v4.0` was never tagged, breaking v4→v5 detection).

---

## v4.0 — 2026-04-11

### Added
- **`/connect-tool` skill** — full tool integration skill. Researches tools, evaluates alternatives, checks for CLIs/packages, generates convention-compliant connectors with documentation and auth routing. Six-step flow with research subagent, decision checkpoint, and three generation paths (Python, MCP, existing package).
- **`_system/tool-integration-convention.md`** — governing convention for external tool connections. Auth scoping pattern (auth.yaml per client, with-auth.sh wrapper), MCP vs Python decision logic, connector shape, enrichment composition model, tool profile structure.
- **`blueprints/workflows/background-agent.md`** — the 5-step self-annealing loop pattern (Capture → Trigger → Analyze → Backlog → Operator). Full economics section, 5 use cases, non-negotiables, and "Before You Build" prerequisites.
- **`_system/frontmatter-convention.md`** — classification backbone. YAML schema, 22 types across three tiers, type lifecycle (creation/structure/read path/write path), staleness detection, log companion pattern, workflow and marketing-pattern required sections, file placement rules. Adapted from 44KB main system to ~20KB essentials.
- **`_system/core-log.md`** — log template with entry type vocabulary (Decision, Hypothesis, Signal, Shift, Dead end, Snapshot), sentinel pattern, example entries.
- **`blueprints/marketing-patterns/`** — marketing pattern library. `index.md` catalog explaining what patterns are and the 13-section method-card structure. `situation-variant-testing.md` reference specimen with fully articulated Forces section.
- **3 new helpers** — `Check-For-Doc-Logs` (companion log detection + entry drafting), `Build-Hook` (Claude Code hook creation procedure), `Log-Decision` (canonical decision recording)

### Changed
- **`CLAUDE.md`** — 8 core principles (added "The system stacks" + "Foundational context deserves disproportionate investment"). New workflow practices: "Sweep side findings before wrapping," "Multi-model comparison," "Operate with strategic awareness," expanded knowledge routing with marketing methodology distinction. 6 new routing entries (workflows, marketing patterns, data files, tool connection). File placement adds 5 types (workflow, marketing-pattern, tool-profile, log, criteria). New sections: Creation Verbs, Compact Instructions, Key References.
- **`done.md`** — full rewrite. Merged reflect+insight into single Step 1. Added Steps 3b-3e (content ideas, messaging candidates, tool learning, quality experiments). Added Step 4c (doc log entries via helper). Enhanced coherency agent with reverse governance check and core.md alignment. New ASCII banner wrap-up format with structured sections (routed, observations, coherency, logical next steps, onboarding).
- **`architect.md`** — 4 new behavioral rules: Adversarial Self-Check, Honesty About Limits, Accumulate Language Aggressively, plus renumbered existing rules.
- **`helpers.md`** — `Publish-To-Google-Docs` migrated from deprecated `gws` CLI to Google Workspace MCP. `Build-Criteria` completed with worked example reference and timing guidance.
- **`settings.json`** — removed 7 deprecated `gws` CLI permission entries. MCP-only Google Workspace access.
- **`_system/system-architecture.md`** — cross-references to new frontmatter convention, core-log template, workflows directory, marketing patterns directory.
- **`tools/index.md`** — references tool integration convention and `/connect-tool` skill.

---

## v3.0 — 2026-04-01

### Added
- **Curriculum** — `curriculum/manifesto.md` (7 principles in practitioner voice, J-curve expectation setting, "you won't break it" section) + `curriculum/playbook.md` (session lifecycle, backlog as strategic instrument, modular workflows, multiple terminals, build-while-working philosophy, two first-win paths)
- **`compact-reinject.sh` hook** — re-injects active session frame after auto-compaction to prevent context degradation
- **`Build-Criteria` helper** — guided quality criteria development (decision matrix, criteria blueprint, worked example)
- **`Quality-Experiments` helper** — lightweight hypothesis-test-learn loop for improving system output
- **`Route-Knowledge-To-Destination` helper** — expanded with tool learning destination and broader routing

### Changed
- **`audit.md`** — full rewrite from graduation check to 12-area diagnostic framework (context health, workflow reliability, knowledge routing, voice consistency, feedback loops, tool integration, backlog hygiene, session discipline, quality gates, architecture coherence, content pipeline, measurement)
- **`system-architecture.md`** — right-sized for starter kit: six-layer diagram, document taxonomy (D099), component inventory, conventions index. 184 lines (was 100, main system is 800+)
- **`CLAUDE.md`** — 4 workflow practices (ask don't assume, critique before presenting, enhanced context management, start over if bad), file placement D099, customization section, personality layer note, scale → 5-7 person
- **`architect.md`** — context budget discipline (~10K tokens), system articulation role, plan protocol (rule 4), enhanced behavioral rules, scope statement, core.md awareness
- **`done.md`** — coherency agent with core.md gate, cluster format in backlog maintenance, routing narration, expanded routing checks (artifact wiring, tool learnings, system failures), practitioner insight examples
- **`helpers.md`** — Capture-Backlog-Item (clusters, task-notes, cluster counter), two new helpers (Build-Criteria, Quality-Experiments), expanded knowledge routing
- **`settings.json`** — compact hook wired, ~/Desktop write permission, script ask permissions, api.openai.com network access
- **`done-enforcement.sh`** — system failures check (#6), enhanced wiring checks, data-state awareness, strategy doc checks
- **`debrief/SKILL.md`** — core.md strategic check (Step 8b), intelligence.md → core.md migration, removed Gmail permissions (routes to /compose), quality experiments reference, done-state checkbox
- **`compose/SKILL.md`** — quality experiments reference added
- **`compose/05-deliver.md`** — `deliverables/` → `artifacts/` aligned with document taxonomy convention
- **`client-command-template.md`** — `deliverables/` → `artifacts/`
- **`client-context-architecture.md`** — `deliverables/` → `artifacts/`

### Removed
- **Curriculum duplication** — eliminated derivative docs (system.md, marketing.md) per D111. Single curriculum location: `curriculum/manifesto.md` + `curriculum/playbook.md`
- **`intelligence.md` pattern** — replaced by core.md in debrief skill (simpler, one-doc strategic check)
- **Gold standard scoring in compose** — premature for new users; voice philosophy already in voice kernel template

---

## v2.1 — 2026-03-23

### Added
- **`/compose` skill** (9 files) — unified composition for emails, data writeups, and persuasive long-form. Voice-engineered with two-pass method, self-audit against 8-criterion rubric, correction feedback loop. Replaces `/email`.
- **Voice infrastructure** — `_system/voice-base.md` (universal editorial constants), `blueprints/voice-kernel-template.md` (how to build per-client voice kernels), `blueprints/criteria/voice.md` (8-criterion voice evaluation rubric, 1-5 scale)
- **`/system` command** — quick diagnostic (onboarding status, session count, focus queue), best practices reference, audit routing
- **`/audit` command** — onboarding graduation check (verifies core concepts introduced + reinforced, flips status on confirmation)
- **Onboarding system** — `/done` Step 4b (micro-teaching at shutdown, one concept per session, trigger-based detection), expanded `cadence-check.sh` (onboarding status, focus queue, early-warning suppression for new operators)
- **Google Docs pipeline** — `tools/gdocs/md_to_gdoc.py` converter + `Publish-To-Google-Docs` helper in `helpers.md`
- **`/done` Step 9 (Wrap Up)** — batches session summary, teaching moments, and feedback prompts into one closing message

### Changed
- **CLAUDE.md** — routing table updated for `/compose`, `/system`, `/audit`, Google Docs publish
- **`/debrief`** — email suggestion now references `/compose` (auto-suggests email format after debrief)
- **`/start`** — Step 6 orientation updated for `/compose`
- **`helpers.md`** — debrief pointer references `/compose`, added Publish-To-Google-Docs helper
- **`cadence-check.sh`** — full rewrite with onboarding, focus queue, and early-warning suppression
- **`system-architecture.md`** — full rewrite reflecting new architecture
- **`contacts.yaml`** — consumer reference updated

### Removed
- **`/email` skill** (3 files: SKILL.md, email-patterns.md, email-voice-guide.md) — absorbed into `/compose` email format

---

## v1.0 — 2026-03-21

Initial release. 33 files. `/start`, `/architect`, `/done`, `/email`, `/debrief`, `/llm-research`, 3 hooks, helpers, settings, blueprints, resources.
