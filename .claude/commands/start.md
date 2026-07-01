Entry point for Marketing OS. **Dual-mode:**

- **First run** (no `core.md` at the system root yet) → set up the workspace, then roll straight into a first real piece of work.
- **Later runs** (single-company users who use `/start` as their daily entry) → orient ("here's where you left off") and invite the next piece of work.

**This command explains what it's doing as it goes.** Setup is a teaching moment — the operator should understand the system, not just have it installed. But the teaching is light: you do **not** front-load market/audience/positioning knowledge to get value. The operator starts from real work; the structure fills as they go.

**Detect the mode first.** Check whether `core.md` exists at the system root.
- Exists → go to **Orient Mode** (bottom of this file).
- Doesn't exist → run **Setup Mode** (Steps 0–8 below).

---

# SETUP MODE

## Step 0: Install Base output style

Before anything else: verify `~/.claude/output-styles/base.md` exists. If it doesn't, create it.

This file tells Claude Code that sessions in this workspace are marketing/operations work, not coding work. Without it, every session runs with software-engineering instructions in the background and writing quality silently degrades. The kit's `settings.json` already points to this style — the file just needs to exist on the machine.

**Check, then act** (clean if/else — don't let the check short-circuit the create):

```bash
if [ -f ~/.claude/output-styles/base.md ]; then
  echo "exists"
else
  mkdir -p ~/.claude/output-styles
  cat > ~/.claude/output-styles/base.md << 'EOF'
---
name: Base
description: Marketing OS base — suppresses coding instructions for strategy, writing, and analysis sessions
keep-coding-instructions: false
---

Think strategically. Push back on weak reasoning.

Pitch before you pick up a task: name the task, the deliverable, and the keystone references you'd pull — then wait for the go. Don't pre-load context; don't dive in.
EOF
fi
```

Tell the operator briefly:

> "First thing — I installed the Base output style at `~/.claude/output-styles/base.md`. This tells Claude Code that sessions here are marketing work, not coding work. One-time setup; you won't think about it again."

If the file already existed, say so and move on.

## Step 1: Welcome + orient

> "This is Marketing OS — an **operations command center** for your work. The idea is simple: for anything you do that repeats — outreach, content, meetings, research, campaigns — the system learns your context and starts handling it the way you would. Set it up once, and you start doing the work of five people.
>
> Marketing *is* operations here — same thing, not a subset. The depth that ships in the box leans marketing, but the structure holds any repeatable work you do.
>
> Three things to know upfront:
> 1. **You start from real work, not setup.** You don't write a pile of strategy docs before the system helps you. We set up who you are in a few minutes, then go straight to a real piece of your work. The structure fills as you go.
> 2. **`/done` closes every session.** It routes what you learned, updates your state, commits to git, and sets up next time. Skip it and the session's work evaporates. This is the most important habit.
> 3. **You grow it through use.** The system gets sharper the more you work in it — it remembers your voice, your context, what's worked. You don't build the whole thing in a day.
>
> Let's get you set up — this part is quick."

## Step 2: Light identity interview

This seeds `core.md` — the durable identity of your work. Keep it conversational and brief. Take each answer before moving on.

**Who you are:**
1. **What's your name?**
2. **What's your primary email?** (Used for the contact registry and the email skill.)

**What the work is** (this becomes `core.md`):
3. **In a sentence or two — what's the business or practice you're running here?** (Who you are.)
4. **Who's on the other end of the work — who do you serve?** (Push for the situational version: "someone who is [situation] and needs [outcome]," not just a demographic.)
5. **What do you actually do for them, and why does it matter?** (How you create value.)
6. **What's the work that repeats?** (The activities the system will help you operate — outreach, content, reporting, etc.)

**How you work** (light — for context, not a full audit):
7. **What does a typical week look like?** (Cadence — meetings, campaign cycles, reporting rhythms.)
8. **Anything already set up in Claude Code worth knowing about?** (Skills, commands, SOPs — don't try to replicate it; just note what's relevant.)
9. **Do you use Google Workspace?** (Gmail, Tasks — affects which integrations are immediately useful.)

Don't interrogate. If an answer is thin, take it and move on — `core.md` is allowed to start light and sharpen through use.

## Step 3: Configure API access (light)

> "What external tools and APIs do you work with? Anything with an API you'll want the system to call — a CRM, an email or outreach platform, data or enrichment sources, project and docs tools. (If you run a marketing stack, that often means something like Instantly or Smartlead for email, Clay or Apollo for enrichment — but it's whatever *you* actually use.)
>
> I ask because the system runs in a sandbox that blocks network calls to domains that aren't explicitly allowed. I'll add yours now so nothing breaks later."

For each tool named:
1. Identify the API domain (e.g., `api.instantly.ai`, `api.fullenrich.com`).
2. **Verify the domain** — check the tool's API docs or ask the operator to confirm. Do not guess domains from training data; wrong guesses cause opaque sandbox failures.
3. Add verified domains to `.claude/settings.json` under `sandbox.network.allowedDomains`.

If they don't know yet: "No problem — when we set up a tool later, I'll add its domain before we use it."

## Step 4: Seed the workspace

Write the workspace base per `_system/workspace-folder-convention.md` (the light base — `core.md` + `operating-lens.md` + `backlog.md` + `context/`).

1. **Write `core.md`** at the system root, from the Step 2 answers, using the `core.md` template in `_system/workspace-folder-convention.md`. Who we are · who we serve · how we create value · what we do. Keep it short — identity, not a strategy treatise.

2. **Write `operating-lens.md`** at the system root, using the template. Seed it lightly: "What's happening now" = "Just set up — about to run a first piece of work." Active Direction and Watches can start near-empty; they fill through use.

3. **Write `_system/operator-profile.md`** from the practice answers (Steps 2 Q7–9):

```markdown
# Operator Profile

- **Name:** [Q1]
- **Weekly rhythm:** [Q7]
- **Existing skills/workflows:** [Q8]
- **Google Workspace:** [yes/no, Q9]

*Written by /start, Session 1.*
```

4. **Write `contacts.yaml`** with the operator's name, email, and any send-from accounts.

5. **Create the empty homes with charters.** Ensure `context/` exists with a one-line charter note (a `context/README.md` or a charter line — "workspace-specific knowledge accumulates here as you work"). Do not pre-build `content/`, `data/`, etc. — those are extensions earned by real work.

## Step 5: Single-company simplification (taught as a lesson)

Ask: **"Do you work with just this one company/practice, or several?"**

- **One** → teach it, don't just configure it:
  > "Then you don't need anything fancier than this. **`/start` is your entry, `/done` is your exit.** Every working session: open with `/start` — it'll show you where you left off and tee up the next thing — and close with `/done`. That's the whole rhythm. No per-workspace commands to juggle."

  No `/[workspace]` command is created. `/start`'s Orient Mode (below) becomes their daily entry.

- **Several** → 
  > "Then each company gets its own workspace so they don't bleed into each other. Run `/new-workspace` when you're ready to add the next one — it scaffolds a clean workspace and a `/[name]` command to drop into it. We'll set up this first one now and you can add the others as you need them."

  Note one `/new-workspace` task per additional company in `backlog.md` (light — a one-line charter each, not foundation-doc homework).

## Step 6: The first-work invitation (the make-or-break)

This is where setup ends and real work begins — **in this same session.** Don't hand the operator off to go build foundation docs. **Lead** them into a first real piece of work.

Ask: **"Do you know what you want to work on right now?"**

- **Yes** → facilitate that piece directly. Run it as a real session. Use the relevant skill if one fits (`/compose` for an email, `/debrief` for a transcript, `/market-research` for research).

- **Not sure** → don't present a blank menu. Probe **"What's something you do on a regular basis?"** and use the identity you just learned in Step 2 to **propose two or three candidate first pieces.** Bias toward a strong first piece — by this test:

  **The good-first-work heuristic:** a strong first piece of work
  1. produces a **tangible artifact the operator actually wants** (a draft, a brief, a cleaned list) — not internal plumbing,
  2. is **self-contained** — one loop, visible end, no dependencies to set up first,
  3. **shows the compounding idea once** ("see how it kept your voice / remembered your context?"),
  4. is **low-setup** — no API connection or foundation doc required to work.

  Good candidates: "draft this email in your voice," "turn this messy thing into a clean one," "write the first version of [a recurring piece]." Weak starters: anything that needs a transcript on hand, an API wired up, or a foundation doc written first.

Once they pick, **do the work with them.** The goal of the first session is one closed loop and one tangible artifact they wanted — that's what teaches the system better than any walkthrough.

## Step 7: Initialize tracking

**Session log.** Write the first entry to `_system/session-log.md`:

```
| YYYY-MM-DD | Session 1 | start | System setup + first work — [operator name] |
```

This initializes session numbering. Future sessions increment from here.

**Onboard log.** Create `_system/onboard-log.md` to track teaching progress. The concept definitions live in `curriculum/concepts.md` (the single registry); this log just tracks introduced/reinforced state per the `/done` micro-teaching and `/teach-me`:

```markdown
# Onboard Log

**Status:** in-progress
**Setup completed:** Session 1, [today's date]
**Graduated:** —

Concept definitions: `curriculum/concepts.md`. This log tracks which concepts have been introduced/reinforced — `/done` drips one per session, `/teach-me` walks them on demand. Both read the registry; neither re-teaches an introduced concept.

## Concepts

| # | Concept | Introduced | Reinforced | Notes |
|---|---------|-----------|------------|-------|
| 1 | The loop — close every session with /done | Session 1 | — | Experienced during setup |
| 2 | The backlog is your brain | — | — | |
| 3 | Quality gates — how to talk to the system | — | — | |
| 4 | You direct it — pitch before the work | — | — | |
| 5 | System hygiene | — | — | |

(Concepts, definitions, and triggers live in `curriculum/concepts.md` — the single registry, shared with `/teach-me` and `/done` micro-teaching. Concepts 1–3 are core/graduation-gating.)

## Milestones

- [Session 1] Setup completed. First piece of work run. First /done.
```

Concept 1 is marked introduced because the operator will experience the mechanism — they'll run `/done` at the end of this session and see what it captures.

## Step 8: Close setup

> "You're set up — and you've got [the artifact from Step 6] to show for it. Here's the whole rhythm from here:
>
> - **`/start`** opens a session — it'll show you where you left off and tee up the next thing.
> - **`/done`** closes it — that's mandatory; it's what makes the system remember.
> - Skills come up naturally: `/compose` to write in your voice, `/debrief` for meeting transcripts, `/market-research` for research. You don't need to memorize them.
>
> The system has more depth — knowledge routing, hooks, blueprints, domain expertise — but you'll meet that through use, not a lecture. Want me to walk you through the core concepts now? Run `/teach-me` anytime — it's self-paced and you can stop whenever.
>
> Let's close this session with `/done`."

Run `/done` to close. (The first `/done` reinforces Concept 1 live.)

---

# ORIENT MODE

`core.md` already exists — this is a returning single-company operator using `/start` as their daily entry. **Don't pre-load.** Same discipline as the workspace commands: load nothing eagerly, pick up the task, **pitch it**, pull on cue. (`_system/task-pickup-pitch.md`.)

1. **First move — find the task.** Ask what they're working on. If they came in with a specific task, take it. If they want direction, *now* pull `operating-lens.md` (where you left off) + `backlog.md` and surface the active thread first, then other high-priority items — don't make them re-decide what's already captured.

2. **Pitch the task before you build it.** Once there's a task, pitch the three legs and wait for the go:
   - **The task** — what's this really about, in your own words; is it framed right?
   - **The deliverable** — the concrete output + what "good" looks like, so "done" is checkable.
   - **The keystone references** — what you'd pull (`core.md` for identity, the relevant `context/` docs, the backlog item detail) + why + what you're skipping.

   One line and one round if it's dead clear; loop the legs if it's murky — converge, don't interrogate.

3. **Run the session** on the go-ahead. Use the right skill for the activity. Close with `/done` — which updates `operating-lens.md`, routes learnings, and (if onboarding isn't graduated) drips the next concept.
