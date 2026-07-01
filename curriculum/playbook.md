# How to Work in Marketing OS

How to shape sessions, use the backlog, talk to the system well, build pieces over time, and recover when things break.

If you remember nothing else: **start every session with a command**, **keep one focus per session**, **use the backlog as persistent memory**, and **always close with `/done`**. The rest explains why each matters.

Read end-to-end once. Come back to individual sections as questions surface in real work.

> First time? Run through `START-HERE.md` first.

---

## Slash Commands You Should Know

Slash commands are how you invoke the system — type `/` in any session and pick one. These are the stable core; you'll learn others as you go.

**Setup**
- `/start` — first-time setup. Walks you through your profile and onboards your first workspace.
- `/new-workspace` — onboard an additional workspace. You'll run this each time you add one.

**Every session starts with one of these**
- `/[workspace-name]` — when you're working in a workspace (e.g., `/acme`). You get one command per onboarded workspace. Loads that workspace's strategy, backlog, and where you left off.
- **System work** — when you're working on the system itself, just open a session and edit `_system/` directly. The system backlog (`_system/backlog.md`) and reference docs are yours to change.

**Every session ends with this**
- `/done` — captures what happened, routes learnings to their permanent homes, sets up the next session.

**Inside a session**
- `/debrief` — after a meeting or conversation that matters. Drop in the transcript or your notes. It pulls out the signals — what was said, what it means for the strategy, what needs to happen next — and routes them to the right places.
- `/compose` — when you need to write something with more care than a quick message. Emails, copy, data writeups, longer-form pieces. It loads your voice and context, asks what you need, and composes from what exists.
- `/llm-research` — deep research across multiple models. Use when one perspective isn't enough and you want to cross-pollinate.
- `/market-research` — structured research on an ICP, market, competitive landscape, or buyer persona. Phased — produces a synthesis you can act on.
- `/connect-tool` — when you want to wire up a new external tool or API. It researches the tool, evaluates alternatives, and generates a convention-compliant connector and profile.
- **Add a skill** — when you've done something three times the same way and want to mechanize it. Create `.claude/skills/[name]/SKILL.md` yourself — define what good output looks like, write the skill, then verify.
- `/align` — when you want the system to interrogate your thinking before you commit to a direction. Useful before a strategy writeup, a campaign launch, or any decision you'll have to live with.
- `/statusline` — set up a status line that shows your session's context usage, so you can see when it's filling up.

**Health**
- `/system` — quick status check, shows where you are.
- `/audit` — drift check, catches when the system is getting stale.

---

## What the System Knows

Each workspace folder has a structure the system reads at startup:

- **Context docs** (`context/`) — market, audience, product, voice, positioning. If the system keeps getting something wrong about a workspace, the context docs don't say otherwise. The fix is always: write it down.
- **Strategy docs** — engagement strategy (the relationship layer: goals, stakeholders, dynamics) and marketing strategy (the execution layer: positioning, hypotheses, approach). The two governing docs new information gets checked against.
- **Backlog** — what needs to happen next. Carries forward between sessions.
- **Artifacts** (`artifacts/`) — what you've built and shipped.
- **Research** (`research/`) — exploration that informed a decision.
- **Operations** (`operations/`) — working docs, SOPs, staging areas.
- **Meetings** (`meetings/`) — transcripts and debrief state.

`/[workspace-name]` reads context, strategy, and backlog so you start with full awareness. The `_system/` layer has its own backlog and conventions — edit them directly when you work on the system.

---

## Sessions Have a Shape

A session is a bounded unit of work, not a drifting conversation. The shape: load a workspace (or the system), box one piece of work, close with `/done`.

**Start with a command.** `/[workspace-name]` for workspace work; for system work, just open a session and edit `_system/` directly. Startup pulls in your strategy, backlog, and where you left off. Without it, every session starts from zero.

**One focus per session.** Strategy OR content OR tooling. Mixing degrades quality fastest — the system loses the thread, you lose the compound benefit of context loaded for one purpose. Switching? Close out and start fresh.

**Finish with `/done`. Every time.** The single most-skipped practice and the one that decides whether a system gets smarter over time or stays flat. It routes what you learned to permanent homes, updates state, leaves breadcrumbs. Skip it and the work stays trapped in the conversation — useful today, invisible tomorrow.

**Start fresh often.** Switching activities, switching workspaces, finished a deliverable — open a new session. The work lives in your files, not the conversation.

**Watch your conversation length.** Quality degrades as conversations stretch. Set up a status line (`/statusline`) that shows context usage and keep an eye on it. When context is getting full, capture remaining work as backlog items and run `/done`. Don't push it to the limit — by the time quality visibly degrades, you've already lost ground. Splitting long work into multiple sessions is a core skill, not a workaround.

Session boundaries are deliberate. "Let's wrap and start fresh" is a quality move, not a concession.

---

## The Backlog Is Your Brain

The backlog is the most important file in the system. Not a task list — a persistent memory of what matters, with enough context that a fresh session can pick it up without you re-explaining anything.

You have one **system backlog** (`_system/backlog.md`) for improving the system itself, plus one **workspace backlog** inside every onboarded workspace's folder — one per workspace. The relevant one surfaces at startup, depending on whether you're working on the system or in a workspace (`/[workspace-name]`).

**Write items as session briefs, not reminders.** The standard: enough context that a fresh session can pick it up and execute from a clean slate. "Fix the email sequence" fails that test. "Fix the email sequence — open rates dropped after we changed the subject line formula; test whether the old pattern performs better on the new segment" passes it. Specific enough to run, open enough to let the session find its shape.

You don't have to hand-write these. The session already has the context — just ask: "create a backlog task for this with enough information to execute from a clean slate." The system drafts it; you confirm. This is the standard move for capturing deferred tangents, splitting long work into multiple sessions, and writing the next-step items at `/done`.

**Defer tangents, don't pursue them.** When something interesting surfaces mid-session — a tool idea, a content angle, a convention gap — capture it as a backlog item and stay on task. The cost of a captured tangent is one prompt. The cost of a pursued tangent is the main task half-done and the tangent half-done.

**Cluster related work.** When three or four items are clearly part of the same effort, group them — a named cluster with a one-line goal and an ordered sequence. Clusters keep the backlog from becoming a flat list of disconnected items.

**Audit regularly.** Backlogs accumulate stale entries, redundant tasks, and items overtaken by events across days of work. Periodically clean house — cluster, reorder, retire what's dead. The longer between audits, the more the backlog misleads you.

---

## How to Talk to the System

The difference between generic output and genuinely useful work is how you interact.

**Correct with reasons.** "The tone is too empathetic — this client is direct, they don't hold the reader's hand" teaches permanently. "Make it better" teaches nothing. The reason is the instruction; without it, the system can't generalize.

**Push for specifics.** The system defaults to safe abstractions to avoid being wrong. Don't let it. When you get a high-level summary, push: "What specifically? Give me the actual recommendation." The specific answer is where the value lives.

**Make it critique its own work.** Before accepting any deliverable: "What's weak? What did I miss? What would a skeptic say?" The first draft is most of the way there — the critique pass catches structural gaps, unsupported claims, and places where the system wrote confidently about things it doesn't actually know. One prompt, outsized payoff.

**Verify before trusting.** Before any complex execution — multi-step process, structural change, strategy recommendation — check its understanding. "Do you know what you're writing?" catches wrong assumptions before they compound. When it's wrong, correct it and make sure the correction gets logged.

---

## Build the System in Pieces

Your daily work IS system building. You don't need separate maintenance sessions — the system gets better because you make it better, one correction and one piece at a time.

**Wait for the signal.** When you've done something three times and you think "I keep doing this the same way" — that's the signal. Don't tackle an entire workflow at once. Break it into the smallest repeatable chunks — things you'd want done the same way twice.

**Examples of pieces that stack:**
- **Cold email:** define segment → clean list → flag exclusions → draft sequence → review claims → send → log results.
- **Meeting workflow:** pull transcript → extract signals → route to destinations → update strategy docs → draft follow-ups.
- **Content production:** research → outline → draft → voice check → format → publish → repurpose → measure.

Each step is a piece. Each piece can be codified independently.

**Pieces multiply across workflows.** "Build a process for cleaning a list" is one session of work. Once you have it, you have it for cold email, analytics, research, reporting — anywhere a clean list matters. That's how the multiplier grows: not by building one giant workflow, but by building pieces that stack.

**If one piece breaks, the rest still works.** Chain everything together and one problem cascades. Build in pieces and you fix the broken step, keep going. Checkpoint between steps — run a step, see what happened, then proceed. This is how trust in the system gets built: each piece verifiable on its own.

**Go as far as you can and stop.** Not everything is easy to codify. Sometimes you do part of a process manually and just record how you did it — that's still a building block. Next time, the system has your notes. The time after that, maybe you're ready to lock it in as a command. No pressure to automate everything at once.

**Route knowledge to its permanent home.** When something important surfaces — a tool insight, a marketing principle, a sharp phrase — ask: where in the system does this live? Tool learnings → tool profiles. Architecture decisions → decision records. Domain knowledge → resource files. Voice corrections → voice kernels. Not sure? Ask the system — it knows the folder structure. Sharp thinking evaporates fast; capture in real time.

**CLAUDE.md is living config.** It's the system's operating instructions and it's yours to edit. If the system keeps drafting emails in the wrong tone for a client, add a rule: "When writing for [client], lead with the metric, keep it under 3 sentences, no hedging." Next session, it just works. After any session where something went wrong, ask: could a rule have prevented this? If yes, add it.

**Wire new pieces up.** When you create something new — a process, a command, a set of instructions — make sure the system can find it. Add it to CLAUDE.md, reference it from the relevant workspace doc, or link it from your backlog. Built but unreferenced = invisible next session.

One process running well teaches more about system-building than five sketched out.

---

## When Things Go Wrong

The system will confidently produce things that are wrong. It will misunderstand positioning, apply one workspace's conventions to another, present assumptions as facts. This isn't a bug — it's the nature of the tool. Handling it is a core skill.

**Immediate fix: undo or correct.** Escape to cancel, Escape again to rewind. Try from a clean state. If the output is subtly wrong — tone off, facts invented, strategy drifted — correct with a reason. The correction, added to the workspace's strategy doc or CLAUDE.md, prevents the same mistake forever.

**Structural fix: something is missing.** If the system keeps getting the same thing wrong, it's correctly following incomplete instructions. Make the implicit explicit. Every closed gap is a permanent improvement.

**Context fix: the session is too long.** If it's forgetting what you told it earlier or contradicting itself, the session has stretched. Save progress to the backlog, run `/done`, start fresh.

**Common early mistakes:** codifying processes before doing them enough to know their shape; keeping one session open too long; mixing too many work types in one session; writing backlog items without enough context for a fresh session to use; leaving a sharp insight in the conversation instead of routing it home. All normal. A few sessions of discipline and you'll feel the difference.

---

## As You Get Comfortable

**Run multiple terminals.** Once the session rhythm is second nature, run two or three terminals at once — one per workspace or activity. While the system works in one, start something in another. Each terminal stays bounded: one workspace, one task. Don't have two terminals touching the same files.

**Bridge context between sessions.** When a result in one terminal matters to another, paste it across with a note. You start directing work across parallel tracks — while the system builds in one terminal, you're thinking in another.

**Handle discoveries deliberately.** When a session produces a major insight or novel direction, resist the urge to fully explore it right there. Capture everything as backlog items. Close the session. The compound value of a discovery comes from methodical follow-up, not frantic same-session exploration.

---

*These practices come from hundreds of sessions across multiple clients. They're not theory — they're what we learned by doing the work.*
