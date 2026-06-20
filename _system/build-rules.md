---
type: system
governance: core-ref
scope: system
description: "Durable design constraints — rules that every build decision checks against"
status: operator-reviewed
created: 1
last-updated: 570
updated-by: joint
---

# Architecture Principles

Durable rules for building Marketing OS. Implementation will vary; these shouldn't.

---

## Structure Follows Use

Don't pre-design folder structures. Let activities declare what they need. Structure emerges from onboarding real clients and executing real work.

This doesn't mean "don't plan." Studying how Anthropic designed their primitives, learning from what BMAD or other practitioners have built, scaffolding from known conventions — that's sharpening the axe. The anti-pattern is building a custom axe when a perfectly good one exists at the store. Or worse: building a shed to store an axe you haven't bought for a tree you haven't identified.

**Corollary:** If we're designing structure without a concrete use case in hand, we're probably being theoretical. But studying existing patterns to prepare for concrete work isn't theoretical — it's craft.

*(Refined Session 162 — Theme 1 from decision themes synthesis. Original principle stands; nuance added to distinguish scaffolding from speculation.)*

---

## Onboarding Is a Capability

The process of adding clients and activities is itself a repeatable skill. It should be a conversation that builds structure, not a manual setup process.

---

## Operator vs. Client

- **Operator level:** YOUR methodology, principles, preferences, how you work
- **Client level:** THEIR strategy, personas, voice, constraints, context

These are separate. Operator knowledge is stable across clients. Client knowledge varies.

---

## Patterns Earn Promotion (What to Build)

Capabilities come from repeated use, not anticipation.

- Used once → stays in workspace
- Used twice → notice the pattern
- Used three times → promote to capability

Don't build playbooks for things you haven't done yet.

---

## Methods Get Captured Immediately (How to Build)

When you figure out how to do something well, capture the blueprint right away. This is not premature abstraction — this is how the system compounds.

- **Resources:** Reference material that informs how the system works (practitioner research, best practices, frameworks)
- **Blueprints:** Reusable methods for recurring operations (how to create a persona, how to onboard a client)

When the operator says "create a persona," the system has the blueprint and executes. No reinventing, no waiting.

"Patterns Earn Promotion" governs WHAT to build. This principle governs capturing HOW once you've learned it.

---

## Protocols Are Core Infrastructure

The system only stays coherent if people use it correctly. You can't assume they will — you have to design the minimum habits into the system as non-negotiable protocols.

**Startup and shutdown are the system's only reliable hooks.** The operator runs startup at the beginning and shutdown at the end. That's the entire behavioral contract. Nothing else is guaranteed to happen.

This means: **if something needs to stay current, it must be wired into startup or shutdown.** A status table, a tracking doc, a progress log — if it's not updated by one of these two motions, it will rot. When evaluating any new artifact, the question isn't "is this useful?" It's "is this maintained by startup or shutdown?" If the answer is no, either wire it in or don't build it.

Protocols and best practices are not documentation — they're design elements. They're as fundamental as the folder structure or the CLAUDE.md. The system should:
- Ship with clear protocols for how to use it
- Make following them easier than skipping them
- Wire all maintenance into startup/shutdown — the only two guaranteed touch points
- Capture new protocols as they're discovered through use

**Known protocols so far:**
- Startup command (load context, orient to current state)
- Shutdown command (log session, update context, capture learnings, update system map)
- *(More will emerge from use)*

---

## Persistent Context Is the Foundation

The system's most fundamental mechanism is persistent, structured context across sessions. Everything else builds on that. The backlog, intelligence docs, strategy docs, voice kernels — they work because they survive session boundaries. A session that starts with context from the last session is compounding. A session that starts from zero is not.

This means: when evaluating what to build next, prioritize mechanisms that improve context persistence and quality over mechanisms that improve within-session capability. A better backlog format compounds across every future session. A fancier skill runs once.

**The test:** Does this improvement make the next session start better, or does it only help the current session? Both matter, but the former compounds.

**Corollary — Backlog items are session briefs.** Backlog items are persistent context. Their quality determines the next session's quality. A vague backlog item produces a vague future session. An over-specified item prevents the session from finding its natural shape. The standard: "specific enough for detail, open-minded enough for natural direction." Quality-gate backlog items before closing a session — review for detail, ordering, and clustering.

*(Added Session 468 — operator observation that the backlog is the system's most valued feature across installs. The reason: it's the simplest expression of persistent context, and persistent context is where the leverage lives. Corollary added Session 535 — R3 corpus evidence, durable across R2 and R3.)*

---

## Credentials Are a P0 Design Element

Credentials are load-bearing infrastructure, not operational housekeeping. When one goes missing, the system fails at its cheapest possible failure point — and the failures are usually silent (file fallbacks, "couldn't connect" warnings, degraded delivery paths). The leverage promise of Marketing OS dies at the foundation when you can't do the most basic thing.

Every credential the system depends on must be:

1. **Inventoried** — declared in `_system/credentials/INVENTORY.md` with source, consumers, canonical location, pointer mechanism, restoration ritual, and health check
2. **Stored in a backed-up location** — `_system/credentials/` (Dropbox-synced) is the canonical home. Tools that insist on writing to `~/` get configured via env var to read from the Dropbox path instead. The Dropbox sync IS the backup — no separate backup script
3. **Verified at startup** — `tools/credentials/check.py` runs as a hard-fail check. Soft warnings are the failure mode this rule exists to prevent

**The test:** If your laptop got wiped tomorrow, would the system still know what credentials it needs and where to get them from? If the answer depends on memory or grep-ability, you've already lost.

**Anti-pattern:** Credentials living in `~/.<tool>/` or `~/.config/<tool>/` without inventory or sync. Tools that default to these paths must be reconfigured before they're trusted in the system. Discovering a credential exists only because something failed silently is a structural defeat.

*(Added Session 570 — D131. Triggered by recurrence: `workspace-mcp` credentials lost twice between Session 193b setup and Session 570 attempt to use them, producing a silent `/compose` file fallback that left the operator pasting from terminal output. The asymmetry between Dropbox-synced client `.env` files (which always survived) and home-dir credentials (which kept disappearing) was the diagnosable root cause.)*

---

## Articulated Intent Transforms Work

When you force explicit articulation of purpose before work begins, the work is qualitatively different. Intent isn't overhead or preamble — it's a thinking tool that clarifies the operator's own understanding and gives the system something to check alignment against.

This shows up at every scale in the system. core.md's Intention section ("What's happening," "Success right now") forces the operator to declare what matters for an engagement — and the coherency agent checks session work against that declaration. data-story.md's strategic header forces "why does this data work matter?" before enrichment begins — without it, data sessions drift into mechanical processing. The multi-LLM research intent step forces "what are we trying to learn and why?" before any models are consulted — consistently producing better research than jumping straight to questions.

The mechanism: explicit intent benefits the operator (crystallized thinking) AND the system (alignment checking) simultaneously. A document that declares "here's what we're doing and why" is both a governance artifact and a cognitive tool.

**The test:** Before starting any significant work stream, can you state the intent in 2-3 sentences? If you can't, the work isn't ready to start — not because of missing information, but because the purpose hasn't been articulated. The articulation IS the readiness.

*(Added Session 486 — Theme 10 from decision themes synthesis. Decisions 104, 106, 108. Also validated by multi-LLM research intent step, which consistently improves output quality.)*

---

## Coherence Over Organization

The value of the system comes from interconnection, not isolated files.

**The test:** "Will Claude find this when it's needed?"

If something should surface but doesn't → fix the trigger, not the folder structure.

**Cluster coherence check:** When a cluster produces multiple outputs across separate sessions (a product model, a playbook, a program page, a VSL), include a final step that reads all outputs as a set. Tasks created in different sessions drift — same concept, different language; one surface promises something another doesn't deliver. Individually good pieces can add up to an incoherent whole. The coherence pass catches this. First applied: {M-C4} (D116).

---

## Flexibility Within Principles

The principles are fixed. The implementation adapts.

We don't know yet:
- What folder structure clients need
- What goes in context docs
- Which capabilities will matter

We do know:
- How modes should behave
- How friction should be placed
- How learning should feed back into the system

Design the process, not the final state.

---

## Real Inputs Over Theoretical Structure

Anyone can design "strategy.md, personas.md, voice.md."

That's shallow. The hard question is: what information do you actually need to execute this activity well?

If we can't answer that from experience, we shouldn't be designing the structure yet.

---

## Workflow Reliability Standard

A workflow isn't real until it's reliable. A prompt that happened to work once is not a codified workflow — it's a prompt that got lucky.

**What makes a workflow reliable:**
- **Planned** — define what it does before building it
- **Step-explicit** — each step is deliberate and visible, not a black box
- **Success criteria defined** — you know what "worked" looks like before you run it
- **Self-auditing** — the workflow can check its own output or surface when something went wrong
- **Deterministic** — same input, same output. Run it Tuesday, run it Friday, it doesn't do something different

**Anti-pattern:** Build something, it looks like it works, ship it. Next run, it drifts or produces different output. That's not codification — that's a lucky prompt. The gap between "it worked once" and "it works every time" is the entire point of engineering.

*(Added Session 11 — moved from core principles. This is a build standard, not a product belief.)*

---

## Every Session Leaves the System Smarter

Workflows should produce two things: the deliverable AND a learning artifact. A campaign that ships without capturing what worked is a missed compounding opportunity. A draft that gets rejected without logging the correction means the system will make the same mistake again.

Design every workflow so that learning capture is baked in — not dependent on the operator remembering to do it. After a campaign ships, results get logged. After a client rejects a draft, the correction is captured. After a strategic pivot, the rationale is recorded. The system gets smarter because the workflows are designed to leave something behind.

**The test:** After this workflow runs, is there a file that didn't exist before that makes the next run better? If not, redesign the workflow.

**Corollary — The system stacks.** "Every session leaves the system smarter" is the session-level expression. At the engagement and capability level, the concept is **stacking**: every engagement, every workflow, every skill adds a permanent layer that makes the next one better. Voice kernel = layer. Campaign results captured = layer. Skill built from a repeated process = layer. Design every workflow, skill, and convention to stack. The mental model for new users is concrete: set up these things, each one compounds, over time you have a fully stacked system. This is the answer to "where do I start?" — not "learn the architecture" but "start stacking."

*(Added Session 11 — from principle question Q23. This is a design rule for workflows, not a belief about marketing. Stacking corollary added Session 535 — R3 corpus evidence + operator articulation. See CLAUDE.md Core Principle #5.)*

---

## Progressive Context, Not Comprehensive Context

The context window is not a dumping ground. Every token that doesn't serve the current task degrades the model's performance. More context ≠ better results. Focused context = better results.

Load the overview first. Go deeper on demand. Skills are entry points, not encyclopedias. CLAUDE.md stays minimal — universal essentials only. Task-specific commands load exactly the files relevant to the current workflow. Raw data is the deep layer, accessed rarely.

**The test:** For any piece of context being loaded — does this serve the current task? If not, don't load it.

**Corollary — Startup budgets:** Command startup reads should stay under ~10K tokens (~650 lines) of file content. Reference material needed only for specific activities belongs in on-demand loading, not startup. When adding a file to a command's startup sequence, justify the addition against the cumulative budget. File growth is invisible until measured — the prevention is cheaper than the audit.

*(Added Session 11 — from principle question Q26. Build rule for context architecture design. Startup budget corollary added Session 219 — T-144 context budget audit.)*

---

## Encode Knowledge into Structure, Not Conversation

The model is smart but inconsistent. Structure is reliable. Don't rely on the model's intelligence to remember your knowledge, your organizational logic, or your quality standards. If they live only in the conversation, they're ephemeral. If they're encoded in files, conventions, and schemas, they persist.

It's easy to get lulled into complacency — the model is extremely capable, so you start treating the chat as the system. But chat is random. Structure is dependable. Your knowledge belongs in files. Your organizational logic belongs in directory conventions. Your quality standards belong in schemas and gates. The model reads and applies them — it doesn't replace them.

The architectural reason this rule exists: in LLM systems, code and data are the same thing. The system prompt, the skill file, the user message, the conversation history — all tokens in a sequence the model reads and continues. An instruction in CLAUDE.md doesn't execute in the traditional sense — it's text that shapes what the model does next, with no privileged enforcement status. Under context pressure, it fades like any other text. It's hard to keep things on the rails because it's all text. This isn't a flaw — it's the architecture. Structure outside the text layer (hooks, file-system shape, startup scripts, filename conventions) restores the boundary between enforcement and data that the context window structurally cannot provide.

**The test:** If you started a fresh session right now, would the system still know what matters? If the answer depends on conversation history, something needs to be encoded into structure.

*(Added Session 11 — from principle question Q27. The model is powerful but unreliable as a memory system. Structure compensates. Architectural warrant added S625 — B10 integration from VanClief corpus, proven by F-2/F-6/F-64/F-73: rules in text degrade under pressure, recur until converted to structural enforcement.)*

---

## Simplicity Is the Default Until Proven Insufficient

Start with the simplest tool that works. 80% of Marketing OS value will live at Level 2 (reusable commands that load the right context for a task). The promotion pipeline is strict:

**Ad hoc → Reusable command → Specialized skill → Sub-agent orchestration**

Always sit as far left on this spectrum as the work requires. Each rightward move earns its place through demonstrated friction with the simpler approach — not anticipated future needs, not architectural elegance.

A 50-line slash command that loads 3 files and works reliably is better than an elaborate multi-agent pipeline that does the same thing with more failure modes. Move right when the simpler version genuinely constrains you. Not before.

"Patterns Earn Promotion" governs *what* gets built. This principle governs *how complex* it gets built.

*(Added Session 11 — from principle question Q28. Complements "Patterns Earn Promotion.")*

---

## Prescribe, Don't Describe

Instructions to agents must be directive, not descriptive. "Feeds backlog" describes a relationship. "Create a task in the backlog" prescribes an action. The model will interpret descriptions loosely; it will follow prescriptions literally.

When writing commands, prompts, or behavioral rules:
- **Bad:** "System gaps feed the backlog" (agent notes the gap, moves on)
- **Good:** "For each system gap, create a task in the backlog or explicitly note why it's parked"

**The test:** Read your instruction as if you're a very literal assistant. Does it tell you exactly what to do, or does it describe a concept and hope you figure out the action?

**Corollary — Flag with action, not observation.** When the system identifies a problem (coherency flag, convention violation, stale reference), the default should be proposing the fix, not just flagging the issue. "This is stale" is description. "This is stale — here's the update, approve it" is prescription. The operator shouldn't have to ask "so what should we do?" after every flag.

*(Added Session 28 — learned from routing failure where "feeds backlog" was interpreted as description, not instruction. Corollary added Session 535 — R3 corpus evidence, durable across R2 and R3.)*

---

## Platform Mastery Is Foundational Infrastructure

Marketing OS is built ON Claude Code. The system's ceiling is determined by how well it understands and leverages the platform it runs on. Platform expertise isn't optional knowledge — it's the foundation every other capability stands on.

Three layers of platform expertise, internally connected:
1. **Tools** — What Claude Code primitives exist and when to use each
2. **Architecture** — How we've composed those primitives into our system (decisions, principles, system-philosophy)
3. **Knowledge** — How to use them well, learned from practice and practitioners (conventions, patterns)

These layers reinforce each other: architectural decisions reference platform capabilities. Practitioner patterns pressure-test design decisions. Validated practices promote into conventions. When one layer changes, the others respond.

**The test:** When making any system design decision, can you state (a) which Claude Code primitive you're using, (b) why that primitive over alternatives, and (c) what practitioner wisdom informs the choice? If you can't answer all three, you're building blind.

*(Added Session 130 — Decision 046. Triggered by discovering 84% platform coverage gap. The three-layer model is the system's expertise architecture.)*

---

## Defense in Depth Through Multi-Channel Redundancy

Critical behaviors must be enforced through multiple layers with different delivery channels, timing, and failure modes. Redundancy across channels is not waste — it's the mechanism. Each layer catches what the others miss.

| Layer | Channel | Timing | Failure Mode | Substrate |
|-------|---------|--------|-------------|-----------|
| CLAUDE.md norms | Always-on context | Every request | Fades under context pressure | Text |
| Command steps | On-demand prompt | When invoked | Can be rushed in long procedures | Text |
| Hooks | Infrastructure injection | Event-triggered | Short + focused, but depends on event firing | Infrastructure |
| Startup loading | Next session context | Session start | Catches what prior session missed | Infrastructure |
| Structural shape | Folder hierarchy, frontmatter types, naming conventions, file existence | Always (passive) | Fails only when the structure itself is violated — and violations are visible | Structural |

A behavior enforced by only one channel is one failure away from silent degradation. When you identify something as critical (knowledge routing, client doc updates, system map maintenance), map its enforcement layers. If there's only one, add another with a different failure mode.

Three substrates, not two. **Text-layer** channels (CLAUDE.md norms, command steps) operate in the same substance as everything else in the context window — they fade under pressure. **Infrastructure-layer** channels (hooks, startup loading) fire deterministically outside the text, but depend on events or session boundaries. **Structural-layer** enforcement (folder hierarchy, frontmatter types, naming conventions, required sections, file existence/absence) is passive — the workspace shape itself constrains what's valid without any instruction or event needing to fire. A `type: workflow` declaration means required sections; a file in `artifacts/` means it's a deliverable; the absence of `data-state.md` means the data layer isn't scaffolded. The structure declares the rules the model reads. A defense that only uses text-layer channels is multiple instances of the same failure mode, not independent defenses. The diversity across substrates is the load-bearing property, not the channel count.

**The test:** For any behavior you consider critical, can you name at least two layers enforcing it through different delivery channels? If not, you're one failure away from the behavior silently stopping. **And:** do those layers span the text/non-text boundary? Two text-layer channels are better than one, but they share a failure mode.

**Corollary:** "Structural enforcement > instructions" is itself an instruction. Hooks are the mechanism that breaks this recursion — they fire deterministically, outside the text layer, without the LLM choosing to remember them.

*(Added Session 138 — Decision 049. Surfaced from the meta-tension of Session 137: enforcing "structural enforcement > instructions" with more instructions. Hooks resolve the recursion. Text/non-text substrate distinction added S625 — B10 integration. Channel 5 (structural shape) + three-substrate model added S625 — C4/C5 integration. Sub-structure of Channel 5 flagged for deeper exploration in M-148.)*

---

## Separation of Concerns

Build from layers that do different jobs and compose independently. Each layer should have a single, clear responsibility — and changing one layer should not require changing another.

This is the system's most practiced principle. Commands set up sessions (context loading). Skills execute workflows (the actual work). Output styles control cognition (how the agent thinks). These three are orthogonal — you can run any skill from any session in any cognitive mode. That composability exists because the layers don't depend on each other's internals.

But composability is the surface benefit. The deeper reason is **independent evolution.** When concerns are coupled, changing one thing breaks another. We lived this: the analyst command owned five workflows AND a persona AND context loading. Improving one workflow meant navigating the entire bundle. When skills became standalone (Decision 053), each could evolve at its own pace — update market research without touching pressure-test, change architect session setup without affecting any skill's execution logic. In an LLM-driven system where you're iterating constantly, the ability to change one thing without breaking other things is survival.

The pattern applies at every level of the system:
- **Architecture:** commands vs. skills vs. output styles (Decision 053)
- **Knowledge:** `_system/` (crafted) vs. `resources/` (external) — different compounding properties, different maintenance cycles
- **Documents:** state tracking (updated every session) vs. strategic direction (updated rarely) — when one doc serves two lifecycles, both degrade (Decision 037)
- **Skills:** orchestration (SKILL.md) vs. step execution (step files) vs. templates — each piece loads independently and changes independently

**The test:** Can each piece evolve independently without breaking the other? If changing a skill requires changing a command, or updating a convention requires updating every file that uses it, the concerns aren't separated — they're coupled.

*(Added Session 162 — Theme 5 from decision themes synthesis. Decisions 009, 019, 037, 045, 053. The system's most practiced principle, now its 14th written rule.)*

---

## Teaching Before Filing

When a skill or workflow produces knowledge artifacts, teach the operator the key insights BEFORE filing the output. Don't generate a document and move on — pause, surface the 3-5 things that matter most, and let the operator react.

The operator's reactions are the point. They confirm ("yes, that matches what I'm seeing"), challenge ("that's wrong, here's why"), redirect ("this matters more than what you emphasized"), or add context ("I heard from the client that..."). These reactions get annotated into the deliverable and carried forward as input to downstream work.

This pattern does double duty: it builds the system (better artifacts) AND builds the operator's understanding (shared mental model). Without it, the system over-generates artifacts the operator never internalized — which is slop regardless of how well-researched the content is. AI's propensity to confidently produce volume without operator comprehension is the failure mode this principle prevents.

**The deeper mechanism — cementation:** The operator's confirmation is what turns observation into knowledge. The LLM identifies patterns. Some are real. Some are noise. Without a confirmation step, you accumulate patterns of unknown quality. With it, knowledge enters the system only when the operator has endorsed it. This is bidirectional learning: system → operator (teaching), operator → system (confirming). The cementation protocol: LLM identifies → system teaches → operator confirms or rejects → only confirmed patterns get cemented into structure.

**Where it applies:** Any skill or workflow that produces knowledge artifacts from research. Currently: `/build-primitive` (teaching step after extraction), `/market-research` (teaching checkpoints between phases), `/pressure-test` (teach & route step). Should propagate to any future knowledge-producing workflow.

**The protocol:**
1. Present the research output in condensed form
2. Surface the 3-5 most important things with conviction ("Here's what matters...")
3. Flag surprises against prior assumptions
4. Check source confidence (what's solid, what's qualified, what can't be claimed)
5. Wait for operator reaction — this is not optional
6. Annotate deliverable with operator input and carry forward

**The test:** After a skill produces a knowledge artifact, can the operator explain the 3 most important things in it from memory? If they can't, the teaching step failed or was skipped.

*(Added Session 147 — Propagated from `/build-primitive` teaching pattern (Session 142, T-107). Operator directive: "This is how any new information should be taken in." Cementation protocol framing added Session 162 — Theme 6 from decision themes synthesis.)*

---

## Mark Confidence, Not Just Content

Strategic documents are working tools, not prescriptions. Every claim carries an implicit confidence level — make it explicit. Positions are things we've decided. Hypotheses are things we believe but haven't tested. Open questions are things we don't know. Projections are guesses informed by reasoning.

The failure mode: the agent writes speculation as settled fact. The next reader — human or model — treats the document's tone as its confidence level. A funnel revenue projection written with the same authority as a confirmed pricing decision gets treated as equally reliable. It isn't. Worse, when another LLM reviews the document, it absorbs the confident framing and builds on it rather than challenging it. The document forecloses the debate it should be inviting.

This matters most for documents that will be reviewed by collaborators or external models. A document that says "we believe X because Y, but this is untested" invites productive challenge. A document that says "X works like this" invites agreement or wholesale rejection — neither is useful.

**The test:** Read each claim in the document. Can the reader tell whether this is something you've decided, something you think is probably true, or something you're guessing? If every sentence reads with the same confidence, the document is lying about what you actually know.

**Context-scope corollary — cross-session artifacts (added S655, D148):**

Confidence isn't just about *claim type* (position / hypothesis / open question / projection). It's also about **the gap between the writing session's context scope and the document's read audience.** A claim that would be well-founded if the writer had full strategic context can still be overclaimed when the writer has only single-workstream context. The topic's apparent confidence and the writing session's actual context scope are different things.

This failure mode is especially load-bearing in **cross-session artifacts** — documents that future sessions read to orient themselves. Examples: folder indexes, `core.md`, `*-log.md`, engagement/marketing strategy docs, meeting debrief outputs, backlog task bodies. A narrow-scope writer produces confident-sounding prose; a broad-scope reader treats it as authoritative; the orientation cascade corrupts downstream.

Section-type taxonomy for confidence calibration in cross-session writes:

| Section type | Confidence | Voice |
|--------------|-----------|-------|
| Work done / artifacts created / decisions made | High — observable | Direct, factual, definitive |
| Current state / what's here / pointers | High — observable | Direct, factual |
| Future work / blocked items / what's not here yet | Medium — inferential about scope | Hedged where the inference came from a narrow context |
| Recommendations / prioritizations / "Next steps" | **Lower — inferential under partial context** | **Hedge explicitly. Name the writing session's context scope. Invite validation against broader sources** (`core.md` Active Direction, `engagement-strategy.md`, operator) before treating items as committed. |

**Reference shape:** A folder index's "Next steps" section — context-calibration callout at section top, "Candidates worth considering" not "Recommended," each item names what's known vs. what's inferred, closing validation note.

**Mechanism pointer:** `.claude/helpers.md` § `Check-For-Folder-Index` Voice calibration section — same taxonomy, applies when proposing or scaffolding new index content.

*(Corollary added Session 655, D148 — first real-use update to a pilot folder index wrote definitive prose from a single-workstream mining context, corrupting next-session orientation. Enforcement mechanism (write-path hook, frontmatter marker, audit sweep) deferred pending T-450 revisit — see T-449 revisit and T-450 for the evidence-driven path to mechanical enforcement.)*

---

*(Parent rule added Session 228 — operator feedback on product spec writing. The agent's tendency to write projections as facts degrades document utility for collaborative review and multi-model workflows.)*

---

## Compose From What Exists

The operator's existing language — convictions, positions, articulations — is the base material for everything the system produces. When sharp language already exists in the system, find it and compose from it. Don't generate substitutes.

This applies whether you're drafting a brief, brainstorming angles, or exploring new territory. The operator's positions are the launchpad, not a constraint. Be creative, be expansive — but build from the base.

The failure mode: the agent confidently generates bland language when dramatically sharper operator-authored lines already exist. The agent's invented framing is almost always weaker than the operator's earned articulation.

**The test:** Could the operator point to a line they already wrote that says the same thing better? If yes, the skill should have found and used that line.

*(Added Session 345 — Decision 078. Content pipeline generated weaker language than what existed in operator source docs.)*

---

## Accumulate Language Aggressively

When capturing patterns, principles, insights, observations, or any reference material: err on the side of capturing **too much** language, not too little. Different articulations of the same concept at different altitudes — principle → behavior → architectural move → specific instance → verbatim quote → metaphor → raw phrase — are all valuable. They are the raw material the system composes from later.

**Why this rule is load-bearing:** "Compose From What Exists" says the operator's language is the base material for everything the system produces. But composition only works if the language *exists in the system* in the first place — and exists in **multiple authentic variations**, not a single smoothed-out version. Content creators need the same concept articulated at multiple altitudes and registers to find the version that lands with a specific audience. The pattern model, curriculum inventory, content idea inbox, build rules, decision docs, session logs, debriefs, marketing-pattern Known Uses blocks — every reference artifact in the system is simultaneously a reference *and* a language bank. Cutting for "this is a repeat of another concept" strips the composition engine of the variation it lives on.

**The matched quartet.** "Accumulate Language Aggressively" is the **accumulation rule** — capture rich variation. "Surface, Don't Just Capture" (D154) is the **visibility rule** — make captured artifacts visible where attention is. "Filter for Novelty" (D158) is the **discrimination rule** — reserve the surface for what genuinely changed/surfaced. "Compose From What Exists" is the **production rule** — produce from the discriminated base. Skip any of the four and the loop breaks: accumulate without surface → invisible library; surface without filter → wallpaper; filter without accumulate → nothing to discriminate; compose without any → bland synthesized output.

**How to apply:**

1. **Default action when you notice overlap is keep-and-capture, not consolidate.** Ask: "Is this overlap creating *routing* confusion, or is it accumulating *language* variation?" If the latter, keep it.
2. **Name the altitude** when the same concept shows up at multiple levels ("principle" / "behavioral pattern" / "architectural move" / "specific instance" / "verbatim phrasing"). The altitude is part of the capture and is itself information.
3. **Treat verbatim operator quotes as raw content material.** Don't paraphrase them in cross-references. Don't smooth them. Include timestamps and session IDs where possible for traceability.
4. **Capture variation actively.** If the operator articulates the same idea three ways in a single session ("you're stacking structured knowledge" / "I boom boom boom stack my shit" / "every layer makes the next one better"), capture all three. The multiplicity IS the resource.
5. **Do NOT auto-consolidate docs that "say similar things"** unless the overlap creates routing confusion, not just language overlap.

**Distinguish from anti-sprawl discipline:** the Consolidate-Before-Expanding pattern still applies to *routing infrastructure* — multiple partially-redundant routing docs create real agent confusion and the agent starts guessing where to file things. But *within reference artifacts that function as language banks* (pattern model, curriculum, content inbox, decision rationale, attribution blocks), overlap is accumulation, not sprawl. The test: **routing confusion vs. language variation.** If the overlap makes the agent file things wrong, consolidate. If the overlap makes content creation richer, keep.

**The test:** Before consolidating or cutting anything in a reference artifact, ask: *"If I was writing a Wake-Up Call post about this six months from now, would I regret losing this phrasing?"* If yes, keep it. The decision is not "is this redundant?" — it's "is this language worth having in the bank when composition needs it?"

**Where this rule fires:** every R{n} corpus review, every `/done` routing decision, every `/debrief` capture, every curriculum-inventory entry, every content-idea capture, every build-rule attribution block, every marketing-pattern Known Uses stamp, every decision-doc rationale — **forever**. The scope is universal to all knowledge capture in the system.

**Routing destinations include the product foundation layer, not just system docs.** When a deep session surfaces product-essence material (convictions, positioning, messaging anchors), the captures route to `clients/{client}/context/foundation/convictions.md`, `positioning.md`, and `content-production/clients/marketing-os/content-positioning.md` directly — these are hand-curated narrative docs and they get touched when essence-capture sessions produce relevant material. Distinguish from pipeline-fed docs (`content-queue.md`) which route through their producing skill (`/content-prep`), not hand edits. Full routing discipline: route meta-learnings into the cores AND foundation docs at session end (`/architect` Rule 9). The accumulation rule (this rule) governs WHAT to capture; the routing discipline governs WHERE to route it. They're a matched pair within the broader matched pair of Compose From What Exists ↔ Accumulate Language Aggressively.

*(Added Session 570 — operator articulation during R4 walk-through. The agent offered to consolidate Pattern #31 on grounds of overlap with #29 and #30; operator corrected: "just because it's a repeat of another concept doesn't mean it shouldn't be thought about, talked about, articulated, language captured... erring on the side of capturing too much language, because that language can be used for content... saying similar things in different ways is like a core practice of content creators... having authentic language and different altitudes is definitely important." Then expanded scope explicitly: "for all time" / "the rest of them" — principle is universal, not scoped to R{n} walk-throughs. Memory protection: `feedback_capture-language-aggressively.md`. Instruction-doc wiring: `/architect` behavioral rules — per the Defense in Depth rule, a memory alone is single-channel and insufficient for a behavior this load-bearing.)*

---

## Surface, Don't Just Capture

Every artifact the system produces — a backlog item from a background agent, a new decision doc, a pattern candidate, a captured operator quote, a curriculum entry — has two separate events: the moment it's *written* (capture) and the moment the operator *sees it* (surface). Capture without surface is invisible accumulation. The agent ran, the report exists on disk, and the operator forgot it existed.

**Why this rule is load-bearing:** Write paths are easy to build and easy to verify — the file exists, the task is filed, the entry is in the log. Read paths are the opposite: a read path only works if the operator encounters the artifact at a moment when the artifact is *actionable for what they're doing*. Files on disk don't enforce encounters. Backlog items in `backlog.md` don't enforce encounters. "They'll see it at next `/architect` startup" is a hope, not a mechanism — and the failure mode (R5 + R6 corpus reports sat unread while the operator worked in client commands for five consecutive sessions) is the empirical proof that hope fails.

**The matched quartet.** Combined with existing rules, the knowledge loop is four steps and four rules:

- **Accumulate Language Aggressively** — capture rich variation (accumulation rule)
- **Surface, Don't Just Capture** — make captured artifacts visible where attention is (visibility rule)
- **Filter for Novelty** (D158) — reserve the surface for what genuinely changed/surfaced (discrimination rule)
- **Compose From What Exists** — produce from the discriminated base (production rule)

Skip any of the four and the loop breaks. Accumulate without surface → invisible library. Surface without filter → wallpaper. Filter without accumulate → nothing to discriminate. Compose without any → bland synthesized output.

**How to apply:**

1. **For every write path you build, name the read path in the same session.** Ask: "Where does the operator see this, and at what moment?" If the answer is "they'll look eventually," you haven't built a surface.
2. **Scope surfaces to where the artifact is actionable.** Firing a badge in every command is noise. Fire it where the operator can act on the artifact. Reflective contexts (`/architect`) surface reflective findings; execution contexts (the per-client commands) stay silent.
3. **Zero state is silent.** A surface that fires when nothing is pending trains the operator to ignore the surface entirely.
4. **Clearing mechanism is part of the design.** Name how an artifact leaves the surface queue. If the clearing mechanism is "operator manually edits a list," you've built a chore, not a surface. Default: existing status transitions (`ready` → `done`) do the work.
5. **Stable selectors decouple surfaces from framings.** When the surface keys on a specific wording inside the artifact, the next framing revision breaks it. Key on stable title prefixes or type markers, not descriptor sections that evolve.

**The test:** If you built this artifact-producing mechanism, ran it, and then did nothing — would the operator encounter the output within a week as part of their normal workflow? If the answer is "only if they think to check," capture is shipped and surface isn't.

**Where this rule fires:** every background agent (piece #7 of `blueprints/workflows/background-agent.md` is the required Surfacing Mechanism section), every `/done`-produced artifact that needs operator review, every new decision doc (surfaced via `_system/decisions/` revisit triggers + `/architect` Rule 1b check), every convention addition, every hook output, every tool profile update — any time the system writes something the operator needs to know about.

*(Added Session 671 — operator S666 principle verbatim: "having an agent with the right tool log is probably not ideal. Capturing language is fine, but surfacing is always crucial." Empirical trigger: R5 + R6 corpus reports sat unreviewed for 10 and 2 days respectively while the operator ran client-command sessions; backlog items T-436 and T-455 were correctly filed by sentinel insertion but never surfaced because `backlog.md` is read only at `/architect` startup. The agent's write path worked; the operator's read path didn't exist. Paired with D154. Instruction-doc wiring: piece #7 of `blueprints/workflows/background-agent.md` (required Surfacing Mechanism section) + helper `Check-Pending-Reviews` in `.claude/helpers.md` wired into `/architect` and `/marketing-os` Step 1 — per Defense in Depth, a build rule alone is single-channel; the pattern doc's required section is the mechanical channel.)*

---

## Filter for Novelty

Background agents must filter for novelty before they report — silence by default, hell-yeah bar at the agent level, novel findings stratified to the top under a hard cap, every claim audited against current state, every instance dry-run-calibrated before scheduling. Bookkeeping-as-equal-weight is the failure mode this rule exists to prevent: a report that treats restated practices, hedged speculation, and forced product-insight slot-fills as peers of genuinely new findings trains the operator to skim and eventually ignore the surface.

**Why this rule is load-bearing:** Background agents have a write path (capture, per piece #6 of `blueprints/workflows/background-agent.md`) and a surface path (per piece #7, D154). What sits between them — what the agent decides to *write in the first place* — is the discrimination step. Without it, the surface fires on noise, the operator's attention erodes, and the agent's value collapses regardless of how clean the capture and surface mechanics are. The corpus pipeline's S675 walk-terminal evidence (1.5 captures per 5 entries walked, framework re-iterated three times mid-walk under slot-filling pressure) is the empirical case for promoting this from prompt-level discipline to architecture-level rule.

**The matched quartet.** Combined with the existing knowledge-loop rules:

- **Accumulate Language Aggressively** — capture rich variation (accumulation rule)
- **Surface, Don't Just Capture** — make captured artifacts visible where attention is (visibility rule)
- **Filter for Novelty** — reserve the surface for what genuinely changed/surfaced (discrimination rule)
- **Compose From What Exists** — produce from the discriminated base (production rule)

Skip any of the four and the loop breaks. Accumulate without surface → invisible library. Surface without filter → wallpaper. Filter without accumulate → nothing to discriminate. Compose without any → bland synthesized output.

**How to apply:**

1. **Default to silence.** When you build (or operate) any background agent, treat the null report as a valid run. If the agent's design produces a report shell every cycle regardless of yield, the rule is violated.
2. **Hell-yeah bar at the agent level (D157).** The agent asks *"would the operator say hell yeah?"* before including any finding. Bookkeeping fails by definition. Encode the test in the prompt, not as an editorial post-hoc.
3. **Stratify novelty in the output.** Top section = New / Surprising / Unsaid, hard cap **N=5** by default (instances may override with written rationale in the instance doc). Confirmed / Bookkeeping demoted to appendix or eliminated.
4. **Audit-before-claim (F-78 family).** Generic-knowledge claims ("X is being ignored," "Y is stale") must be verified against current state before reporting. Cite the verification.
5. **Dry-run calibration before scheduling.** Before any new instance runs autonomously, run it manually against a known-state window. Operator verifies real findings vs. noise. Calibrate. Then schedule.

**The test:** If you were the operator opening a fresh session and the background agent's surface said *"new review pending,"* would you be excited to walk through it, or would you anticipate slop? If the answer is slop, the agent is producing under-filtered output regardless of how clean the rest of its mechanics are.

**Where this rule fires:** every background agent at design time (piece #5 of `blueprints/workflows/background-agent.md` is the required Output Discipline section), every `/build-agent` flow (T-376 — must scaffold the five rules + dry-run calibration step at instance creation), every existing instance retrofit (corpus pipeline reference implementation lands via T-488), every operator review of a background agent's output (Pattern #35 walk-throughs become the calibration data for the agent's hell-yeah translation).

*(Added Session 676 — D158. Empirical trigger: S675 walk-terminal diagnostic on R5/R6 corpus reports — 1.5 captures per 5 entries walked, framework reframed three times mid-walk under slot-filling pressure, bookkeeping treated as equal-weight to novel findings. Operator articulated the upstream concept S674 as the **hell-yeah bar** (D157) — *"we want to be excited about adding this stuff. Use that as like the bar. Like, oh hell yeah, this is gonna help."* This rule formalizes the bar as architecture, extending it from a Lane 2 product-insight filter to a system-wide background-agent output discipline. Pattern doc amendment lives at `blueprints/workflows/background-agent.md` § Report artifact § Output Discipline. Sister rule "Surface, Don't Just Capture" (D154) is the matched-pair predecessor — surface visibility was the gap that created over-capture pressure; novelty filter is the discrimination that prevents the surface from becoming wallpaper. Per Defense in Depth (D049), build rule is the principle channel; pattern-doc piece #5 is the mechanical channel; both required.)*

---

## Test Generatively, Not Manually

When validating a workflow, don't run it manually with synthetic data. Define personas and scenarios, run them through the flow analytically at agent speed, score findings by severity, and invert into mechanical quality criteria. The output is guards and rubrics, not pass/fail.

Manual testing with fake data produces low signal — you're performing instead of analyzing. Generative scenario testing produces the criteria that persist: "what breaks for a 6-client agency owner at Step 5?" is a question that generates a rubric check, not a checkbox.

**The method:**
1. Define 3-5 user personas with distinct constraints (different tools, different experience levels, different scale)
2. Launch parallel agents — each traces a persona through the full flow
3. Score findings by severity (critical / moderate / minor) and type (structural gap / flow confusion / UX issue / silent failure)
4. Invert findings into mechanical rubric criteria the audit can check
5. The rubric criteria ARE the test — they persist after the analysis is done

**What this produces that manual testing doesn't:**
- Coverage across persona types simultaneously (not one walkthrough at a time)
- Severity-ranked findings (not "it worked" / "it didn't")
- Audit-ready criteria (not observations)
- Repeatable for future versions (same personas, updated flow)

**The test:** After validating a workflow, do you have a set of mechanical criteria that `/audit` can check? If you only have "it seemed to work when I tried it," you tested but didn't validate.

*(Added Session 408 — T-178 starter kit quality analysis. First application of the autoresearch pattern (T-195) to workflow validation. Three agents, four personas, 10 ranked findings, 16 rubric criteria in 11 minutes.)*

---

## Define Quality Before Building

Before building anything repeatable — skills, templates, workflows, rubrics — define what good output looks like in binary terms. Criteria are a design tool that comes first, not a review gate that comes last.

The shift: most build processes define quality after the artifact exists (review phase, QA checklist, "does this look right?"). Criteria-first design inverts this. You articulate failure modes, draft binary criteria that catch them, then let those criteria shape what you build. The artifact comes out different — not just better-reviewed — because the criteria constrained the design decisions.

**Three deployment mechanisms for quality criteria:**
- **Self-audit loop** — agent produces, scores, revises before presenting. Best for composition skills where the agent generates without intermediate operator interaction.
- **Behavioral instructions** — criteria inform generation constraints ("ensure X, avoid Y"). Best for interactive skills where operator discussion IS the quality loop.
- **Operator checklist** — criteria become items the operator checks. Best when operator taste is the primary quality mechanism.

Same criteria, different delivery. The builder chooses the mechanism that fits the skill's workflow — don't force self-audit onto interactive skills or behavioral constraints onto autonomous generation.

**The test:** Before shipping a new skill or workflow, can you name 2-3 binary criteria that would catch its most common failure modes? If you can't articulate what bad output looks like, you're not ready to build the thing that produces it.

*(Added Session 410 — T-209 /build-skill overhaul. Companion to "Test Generatively, Not Manually." That principle validates workflows after building. This one shapes them before. First application: /build-skill Step 4 (Design the Quality Loop) + 6 output-quality criteria.)*

---

## Articulate Forces at Creation, Not Retrofitted

When creating any structured artifact whose solution resolves competing values — a marketing pattern, a framework, an atomic primitive, an architectural decision — articulate the forces at the moment of creation, not after the fact. The tensions that drove the solution disappear into the solution once it exists. Capturing forces while you're still living in the trade-off space is cheap; reconstructing them later is epistemically fragile guesswork.

**Why this rule is load-bearing:** A pattern with named forces is auditable — you can argue with it by arguing with the forces. A pattern that says "use a 5-brick matrix at 500 emails per cell" looks arbitrary after the fact. The same pattern with "Force 1: enough signal to trust, as few emails as possible spent getting it. The 500 floor is the resolution" is earned. The numbers become readable as compromises against specific values, not arbitrary rules.

**The retrofit problem:** When you try to articulate forces for an existing artifact, you're guessing at reasoning that was in the author's head at the time of design. The author was weighing competing pulls live. After the solution exists, those pulls have collapsed into the result and are invisible. You can reconstruct them — but you'll miss the ones that were in the author's gut and never made it to the surface, and you'll probably impose forces that sound plausible but weren't actually what drove the call.

**The mechanism:** Forces is an atomic framework — a structural primitive that names the competing values a solution resolves. Two altitudes: domain forces live in framework files (the tensions inherent to a problem space), pattern forces live in marketing-pattern files (the tensions a particular solution is resolving, often inheriting from a parent framework). Both are required at creation.

**Where the rule fires today:**
- New `marketing-pattern` files MUST include a Forces section at creation (per `_system/frontmatter-convention.md` § Marketing Pattern Required Sections)
- New `framework` files MUST include a Forces section if the framework resolves competing values (per the same convention; existing frameworks get retrofit treatment via T-384)
- Major architectural decisions that resolve tensions should articulate forces in the decision record, not just the choice and the alternatives

**The test:** For any artifact you're about to ship, can you name 2-4 specific values that pull in different directions and would have produced a different solution if weighted differently? If you can't, either the artifact isn't resolving any real tensions (it's a recipe, not a pattern) or you haven't done the thinking — and forcing the articulation now will reveal which.

*(Added Session 553 — D124. Driven by the realization that forces are the load-bearing section of the marketing-pattern type, and forces articulated after the fact tend to be vague trade-offs rather than the real tensions that drove the design. The conversation that surfaced this rule was itself the worked example: forces drafted after the pattern was written produced floaty hand-waving until they were grounded in the specific commitments of the source material. The lesson: don't ship a pattern, framework, or design decision whose forces section you'd have to reconstruct.)*

---

## Think Through the Quality Engine

When approaching any work that involves producing, evaluating, or improving output, think through the Quality Engine dimensions first. Not as a checklist step — as the lens through which you see the work.

The five dimensions are entry points, not a sequence: **before** (do criteria exist?), **during** (is the skill self-auditing?), **after** (can we test generatively?), **over-time** (are we scoring and iterating?), **meta** (are the criteria themselves good?). Enter wherever the current situation demands.

The Zipper — nested loops sharing state across skills — is where compounding happens. When building or modifying any skill, ask: does this skill's quality loop connect to another skill's? Voice criteria that evaluate `/compose` output should also inform `/content-prep` briefs. Meeting debrief quality should feed into email voice. These connections exist in the quality engine map (`_system/quality-engine-map.md`). Consult it.

The failure mode this prevents: treating each piece of work as isolated quality problem-solving when the system already has a framework that connects them. The operator should not need a moment of insight to see that "voice evaluation" is "Quality Engine Dimension 2 applied to composition." The agent should see it immediately because this is how it thinks.

**The test:** When someone says "let's evaluate X" or "how do we improve Y," can you immediately name which Quality Engine dimension applies, whether criteria exist, and what Zipper connections are relevant? If you're reasoning from scratch instead of reaching for the framework, you're ignoring the system's most powerful thinking tool.

*(Added Session 421 — T-175 voice criteria development. The agent had all the pieces (quality engine map, Zipper connections, Dimension 2) but defaulted to task-level thinking instead of framework-level thinking. The Quality Engine should be the default lens for all quality and evaluation work.)*

---

## Decompose by Incompatible Perspective

When considering whether work should involve agents (separate context windows with distinct constraints), the question is not "how many roles exist?" but "which perspectives are so incompatible they must run in separate contexts to avoid contaminating each other?"

The cost model is the **Semantic Tax:** every handoff between agents loses 5-10% of intent fidelity, and the loss compounds across chains. A three-agent pipeline doesn't lose 15% — it loses ~27%. This means most work should stay in a single context. An agent earns its existence only when the perspective value it adds exceeds the fidelity it costs.

Three conditions that justify a separate agent:

- **Context contamination:** The creation context prevents honest evaluation. Self-audit is structurally compromised when you hold the reasoning that produced the output. Example: evaluating your own writing cold is impossible if you hold the creation context.
- **Parallel independence:** The work runs independently without shared state. Example: three persona agents stress-testing a draft simultaneously.
- **Cost asymmetry:** The work can run on a cheaper model or with lower effort without quality loss. Example: bulk pattern extraction on Haiku instead of Opus.

If none of these apply, keep it in the current context. A perspective that doesn't need isolation is just a prompt adjustment, a skill step, or a mode switch — not an agent.

**Prove before adding.** Don't design a multi-agent architecture and build toward it. Build one agent. Prove it earns its coordination cost through 5-10 real runs. Only then consider the next. The promotion pipeline from "Simplicity Is the Default" applies: start with the simplest version that works, decompose only when the simpler version genuinely constrains you.

**The principal boundary.** Agents may watch, evaluate, propose, disagree, prepare, and queue. The operator decides what becomes true in the world. No external sends without confirmation. No canon changes without approval. This isn't a limitation — it's the mechanism that keeps taste and judgment as the atomic units while the system develops additional senses.

**Designed disagreement.** If agents will sometimes disagree, design which pair disagrees about what. Log resolutions as institutional precedent ("case law") that future disagreements reference. Uncontrolled disagreement across multiple agent pairs turns the operator into a babysitter refereeing consensus meetings instead of doing strategic work.

**The test:** Before creating an agent definition, can you name the specific perspective it holds that would contaminate (or be contaminated by) the current session context? If you can't name the contamination, the work belongs in the current session — not an agent.

**Confidence level:** These principles are derived from multi-model research (Claude, ChatGPT, Gemini — March 2026) and system design reasoning. The system has zero deployed agents. These are strong hypotheses — structurally sound, empirically untested. Revisit after 5+ agents have been built and run in production.

*(Added Session 447 — Agent leverage research synthesis. Governing insight: decompose by incompatible perspective. Cost model: Semantic Tax. Boundary: agents sense and propose, the principal decides.)*

---

## Route Tool Learnings to Profiles

Every tool interaction session must leave the tool's profile smarter. When the operator discovers a capability, corrects a tool selection error, hits a rate limit, measures a cost, or figures out a technique that worked — that learning gets routed to `tools/[name]/profile.md`. Tools are not black boxes; they are long-lived system capabilities whose depth accumulates from use.

**Why this rule is load-bearing:** Without logged tool learning, every session that touches a tool starts from the agent's base knowledge. The operator's domain expertise — Clay formulas, merge operations, enrichment column conventions, vendor economics — never compounds. The system operates as a "low-level operator" pushing buttons instead of building mastery. Multiplied across dozens of sessions per week, the delta between "tool knowledge compounds" and "tool knowledge evaporates" is the difference between a system that earns expertise and one that rents it from the LLM's priors.

**The practice: pause and sweep at the end of tool work.** The rule fires during a specific ritual — a cleanup pause at the end of any tool session or tool-building flow. Before closing, ask three questions out loud:

- **Anything to clean up?** (partial state, half-written profile entries, stale TODOs)
- **Anything to wire up?** (new tool not in `tools/index.md`, new capability not in the profile, new recipe not cross-referenced, auth.yaml not updated)
- **Anything we're missing?** (credentials noted but not stored per D131, consumer references not added, index entry stale)

The trigger cases this practice covers:
- **After `/connect-tool`** — did the flow leave the tool cataloged, profiled, and auth-wired end-to-end? `/connect-tool` scaffolds the shape; the cleanup pause verifies nothing is half-built.
- **After a tool-heavy work session** — enrichment run, Clay operation, Serper batch. Did the session add real learnings to the profile (capabilities, costs, gotchas)?
- **After a tool correction** — "that's not a Blitz thing, use Paco" should produce a logged failure AND a tool-selection note in both profiles.

The pause is the mechanism. Without it, learnings evaporate into conversation history and the next session re-learns them.

**What counts as a learning worth logging:**
- A capability the agent didn't know existed (Clay AI formula patterns, BlitzAPI rate limit behavior, Serper vs. Paco address resolution characteristics)
- A correction to tool selection — logged as both the correction and the reasoning
- Cost data from a real run (cost per row, cost per credit, total spend)
- A technique discovered under load (session cookie behavior, paywall detection, pagination tricks)
- A limitation that bit you (silent failure modes, schema quirks, column naming rules)

**Where to route it:** The canonical home is `tools/[name]/profile.md` (type: `tool-profile`, D113). If the tool doesn't have a profile yet, `/connect-tool` scaffolds one. The `tools/index.md` entry gets updated when the profile materially changes.

**The test:** After a tool-heavy session, can you point to a line in a tool profile (or index, or auth.yaml) that wasn't there before? If the session worked with Clay/BlitzAPI/Serper for an hour and the tool state looks identical, you either operated without learning anything (unlikely) or skipped the cleanup pause (the failure mode this rule exists to prevent).

**Anti-pattern:** "I'll note that" / "I'll remember that next time." Same family as "Sweep side findings before wrapping" (CLAUDE.md workflow practice) — the conversational mention creates the feeling of having addressed something while leaving it as residue. For tool work specifically, there is no "later." The cleanup pause is the only time the routing happens.

**Sister rule:** OP74 (Wire up tool references — every new tool, every time) covers the *install* discipline — a new tool isn't installed until it's cataloged. This rule covers the *use* discipline — a tool session isn't done until its learnings are logged. Together they cover the tool lifecycle: install-time cataloging + use-time knowledge compounding.

*(Added Session 570 — R4 corpus evidence. 10+ tool-learning prompts across 6 sessions in R4, driven by enrichment-heavy operation on BlitzAPI, Serper, Paco, Clay, OpenAI. Verbatim operator mandate: "Anytime you enact a tool, you should be connecting to the tool resources and updating the tool about the session." Refined same session after operator feedback: "whenever you're creating a tool, say /connect-tool, use it and then at the end just make sure — let's clean up. Let's make sure everything's cleaned up. Anything we need to wire up, anything we're missing. That is always helpful practice." The cleanup pause is the ritual that makes the rule fire. Precursor convention: tool-integration-convention (S459), tool-profile frontmatter type (T-342/S535). Sister: CLAUDE.md "Sweep side findings before wrapping" workflow practice, OP74 "Wire up tool references." Operator-patterns #30. This rule promotes the convention from "recommended" to "required.")*

---

## Self-Documenting Structure

Architecture should be readable without external documentation. Someone browsing the folder should see the workflow sequence without reading a single file. Someone opening a stage directory should know what it does, what it needs, and what it produces from the structure alone — before reading a single line of content.

**Three named conventions that make structure self-documenting:**
1. **Numbered prefixes** (01_, 02_, 03_) encode execution order. The workflow sequence is visible in the directory listing.
2. **Type prefixes or markers** (underscore for support folders, frontmatter type fields for documents) distinguish "stages I work through" from "reference material I pull from." A newcomer can immediately tell the difference.
3. **Explicit handoff points** — the output of one stage is the input for the next, and that relationship is visible in the structure (output directories, named artifacts, stage contracts).

**The handoff test:** Before declaring a workspace, workflow, or project directory done, verify: (1) Can someone open the folder and know what it is? (2) Can someone see the workflow? (3) Can someone run a stage without asking you? (4) Can someone change a reference without breaking things? (5) Can someone understand *why* things are this way?

**Why this rule is load-bearing:** When structure requires external documentation to understand, the documentation drifts from the structure. The gap between what the structure says and what the docs say is where errors live. Self-documenting structure eliminates that gap by making the structure itself the documentation. This is the same principle as our frontmatter convention (the type field IS the classification, not a separate catalog of classifications).

**Anti-pattern:** A project directory where you need to read a README to understand the order of operations. If the README could be deleted and the workflow would still be followable from directory structure alone, the README is supplementary documentation. If the README is required to understand the workflow, the structure isn't self-documenting.

**Sister rules:** *Encode Knowledge into Structure, Not Conversation* (same family — structure over prose). *Separation of Concerns* (the principle that makes self-documentation possible — each unit has one job, so its name can describe that job). *Prescribe, Don't Describe* (the instruction-layer version of the same move — tell the model what to do, not what things are).

*(Added Session 625 — VanClief Vault absorption, Pass 2. Source: Constraint 08 (handoff readiness) + operator mandate S621: "I think we should try to practice more of this as a common approach, so like cement it in our build principles." External validation from VanClief's self-documenting workspace conventions: numbered prefixes, underscore markers, output directories, handoff checklists. Complements existing conventions — our frontmatter types, `_system/` prefix, session stamps (S{n}), task IDs (T-{n}) are already instances of this principle; this rule names the principle explicitly.)*

---

## Design Lenses

Evaluation criteria for any new system element. Each lens has a corresponding principle elsewhere in the system — the value is having all the questions in one place as a design review checklist.

| Lens | Question to Ask |
|------|-----------------|
| **Friction** | Where should friction be high vs. low for this element? High on irreversible/high-stakes actions. Low on exploratory/reversible ones. |
| **Mode Discipline** | How do we enforce this boundary, not just suggest it? Modes should be constraints, not suggestions. Humans under pressure collapse phases. |
| **Adversarial Quality** | What challenges this output before it ships? A system that only generates agreement accumulates blind spots. |
| **Failure as Input** | What's the path from failure → diagnosis → system update? Every failure should leave the system smarter. *(See: Every Session Leaves the System Smarter)* |
| **Context Accumulation** | How does this element accumulate useful context over time? Exemplars, principles, institutional memory, patterns, vocabulary. *(See: marketing-principles.md #2)* |
| **Output Mode** | What output mode does this activity need — structured/precise or expansive/generative? Different cognitive tasks require different output behaviors from the same model. |
| **Human-in-the-Loop** | When must the human engage vs. can engage? HITL isn't binary — it's a spectrum. Make placement explicit. *(See: marketing-principles.md #3)* |
| **Externalized Judgment** | Does this capture judgment or just steps? Capabilities that capture only steps require human judgment every time. Capabilities that capture judgment earn more autonomy. |
| **Inversion (Munger)** | What will cause this component to fail catastrophically? Work backwards from ruin. Instead of "how do we keep this healthy?", ask "what kills it?" and design prevention for each failure mode. Anticipated failures get structural prevention; unanticipated ones get detection mechanisms. *(See: Self-Annealing Framework, `blueprints/self-annealing.md`)* |
| **Framework Fit** | What existing frameworks apply to this decision? An expert doesn't reason from scratch — they reach for the right thinking tool. For any non-trivial design decision, name 1-3 applicable frameworks before proceeding. If no framework applies, that's either a novel problem (rare) or a gap in the framework library. |
| **Self-Annealing** | If nobody maintains this for 30 sessions, what breaks? What catches it? Every new component needs a detection mechanism and a healing mechanism. If you can't name both, you're creating future drift. *(See: `blueprints/self-annealing.md`)* |

*(Added Session 36 — absorbed from conceptual-frameworks.md. Lenses 9-11 added Session 193 — Munger inversion, framework-native design discipline, self-annealing evaluation.)*