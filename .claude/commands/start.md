System onboarding for Marketing OS.

**This command explains what it's doing as it builds.** The onboard is a teaching moment — the operator should understand the system, not just have it installed.

---

## Step 0: Install Base output style

Before anything else: verify `~/.claude/output-styles/base.md` exists. If it doesn't, create it.

This file is what tells Claude Code that sessions in this workspace are marketing work, not coding work. Without it, every session runs with software-engineering instructions in the background and writing quality silently degrades. The kit's `settings.json` already points to this style — the file just needs to exist on the operator's machine.

**Check, then act:**

```bash
test -f ~/.claude/output-styles/base.md && echo "exists" || mkdir -p ~/.claude/output-styles && cat > ~/.claude/output-styles/base.md << 'EOF'
---
name: Base
description: Marketing OS base — suppresses coding instructions for strategy, writing, and analysis sessions
keep-coding-instructions: false
---

Think strategically. Push back on weak reasoning.
EOF
```

Tell the operator briefly what you just did and why:

> "First thing — I installed the Base output style at `~/.claude/output-styles/base.md`. This is what tells Claude Code that sessions here are marketing work, not coding work. One-time setup; you won't have to think about it again."

If the file already existed, say so and move on.

---

## Step 1: Welcome + Orient

Explain what Marketing OS is and how this onboard works:

> "This is Marketing OS — a system that turns your marketing activities into compounding loops. Every activity you run (campaigns, meetings, research, outreach) becomes a closed loop: execute → measure → learn → feed back → next cycle is better. And the loops connect — what you learn from campaign responses feeds into meeting prep, what you learn from research feeds into messaging.
>
> The directory structure is already in place. This onboard personalizes it — your identity, your clients, and queues up the client-specific setup for separate sessions.
>
> Three things to know upfront:
> 1. **Context quality compounds.** The better your client foundation docs are, the better the system works over time.
> 2. **`/done` is mandatory.** Every session ends with `/done`. It routes knowledge, updates backlogs, commits to git. Skip it and the session's work evaporates.
> 3. **`/architect` is your system builder.** When you want to improve how the system works — new workflows, new conventions, resolving problems — that's `/architect`.
>
> Let's get you set up."

## Step 2: Elicit Operator Identity

Ask these questions. Take each answer before moving on:

1. **What's your name?**
2. **What's your primary email address?** (Used for contact registry and email skill configuration)
3. **How many clients do you work with right now? What are their names?**
4. **Where is your current working directory?** (The folder you've been using with Claude Code. We'll reference it during client onboarding to import existing files.)

## Step 3: Elicit Operator's Practice

Before setting up clients, understand how the operator works. Ask:

1. **What does your typical week look like across clients?** (Meeting cadence, campaign cycles, reporting rhythms)
2. **What skills or workflows do you already have set up in Claude Code?** (Skills, commands, SOPs — anything we should know about or potentially port over)
3. **Do you use Google Workspace?** (Gmail for client email, Google Tasks for action items — affects which integrations are immediately useful)

Don't try to replicate their existing setup. Listen, understand, and note what's relevant for the system.

**After collecting Steps 2-3:** Write the operator's practice context to `_system/operator-profile.md`:

```markdown
# Operator Profile

- **Name:** [from Step 2]
- **Previous working directory:** [from Step 2 Q4, if any]
- **Weekly rhythm:** [from Step 3 Q1 — meeting cadence, campaign cycles, reporting rhythms]
- **Existing skills/workflows:** [from Step 3 Q2 — what they had before]
- **Google Workspace:** [yes/no from Step 3 Q3]

*Written by /start, Session 1.*
```

This file persists across sessions — `/architect` references it during client onboard (import step, integration decisions).

## Step 4: Configure API Access

Ask what external tools and APIs the operator uses. Keep it light:

> "What external tools and APIs do you work with? Email sending platform (Instantly, Smartlead, Lemlist), enrichment providers (FullEnrich, Clay, Apollo), CRM — anything with an API you'll want the system to call.
>
> I'm asking because the system runs in a sandbox that blocks network calls to domains that aren't explicitly permitted. I'll add yours now so nothing breaks when we start building."

For each tool they name:
1. Identify the API domain (e.g., `api.instantly.ai`, `api.fullenrich.com`, `api.clay.com`)
2. **Verify the domain** — check the tool's API documentation or ask the operator to confirm. Do not guess API domains from training data — they may be incorrect and will cause opaque sandbox failures.
3. Add verified domains to `.claude/settings.json` under `sandbox.network.allowedDomains`

If they don't know yet: "No problem. When we set up a tool later, I'll add its domain before we use it."

## Step 5: Create Contacts + Queue Client Onboards

1. **Write `contacts.yaml`** with the operator's name, email, and account mappings. If they have multiple send-from addresses (e.g., different domains per client), capture them in the accounts section.

2. **Update `_system/backlog.md`** with onboard tasks:
   - One task per client: `T-1: Onboard [Client Name] — produce foundation docs, create client command`
   - **If multiple clients:** Ask "Which client do you want to onboard first?" That client gets P0, rest get P1. Starting with the most active client gives the fastest payoff.
   - Number sequentially: T-1, T-2, T-3...
   - Update the task counter at the bottom

3. **If the operator mentioned existing skills or workflows worth porting:** Add a P1 task: `T-N: Review existing skills for system integration` with a note about what they described.

## Step 6: Orient the Operator

Give the operator the 3 things they need to know right now. Save the full walkthrough for `/architect` — they'll see the system in action there.

> **Three things to remember:**
>
> 1. **`/done` closes every session.** It routes decisions, updates backlogs, commits to git. Skip it and the session's work doesn't persist. This is the most important habit.
>
> 2. **`/architect` is your next step.** Start a fresh session, run `/architect`. It will see your client onboard tasks and guide you through setting up your first client. One client per session.
>
> 3. **Skills work from any session.** `/debrief` processes meeting transcripts, `/compose` drafts emails and writeups in your voice, `/llm-research` runs deep multi-model research. You don't need to memorize these — they'll come up naturally.
>
> The system has more depth — hooks, knowledge routing, domain expertise, blueprints — but you'll learn that through use, not a walkthrough. `/architect` will introduce concepts as they become relevant.

## Step 7: Initialize Tracking

**Session log.** Write the first entry to `_system/session-log.md`:

```
| YYYY-MM-DD | Session 1 | start | System onboard — [operator name] |
```

This initializes session numbering. All future sessions increment from here.

**Onboard log.** Create `_system/onboard-log.md`:

```markdown
# Onboard Log

**Status:** in-progress
**Setup completed:** Session 1, [today's date]
**Graduated:** —

## Concepts

| # | Concept | Introduced | Reinforced | Notes |
|---|---------|-----------|------------|-------|
| 1 | The loop | Session 1 | — | First /done completed during setup |
| 2 | How to work | — | — | |
| 3 | Quality gates | — | — | |
| 4 | Cross-loop compounding | — | — | |
| 5 | System hygiene | — | — | |

## Milestones

- [Session 1] Setup completed. First /done run.
```

Concept 1 is marked as introduced because the operator just experienced the mechanism — they ran `/done` and saw what it captured. Reinforcement comes when they start a fresh session and the system loads today's context.

This file activates the onboarding system: `/done` will deliver micro-teachings at shutdown, and the startup hook will surface concept nudges. Run `/system` to see your progress anytime.

## Step 8: Close System Onboard

> "System is set up. Your backlog has onboard tasks for each client.
>
> **What happens next:**
> 1. Start a fresh session. Run `/architect`.
> 2. The architect will see the P0 backlog items and guide you through your first client onboard.
> 3. One client per session — start with your most active client, the one you'll benefit from most immediately.
> 4. Client onboard produces your foundation docs: positioning, ICP, market context, buyer personas, marketing strategy, engagement strategy. This is where the system gets smart about your clients.
>
> The onboard is an investment — the foundation docs take real thought. But every session after that benefits from the context you build now."

## Step 9: Capture Onboard Feedback

Before closing, ask the operator for feedback on the onboard experience. Explain why:

> "Quick feedback request — your experience with this setup process helps us improve the system for everyone. I'll capture your answers in `_system/feedback.md`. When you're ready to share, you can zip that file and send it back."

Ask:
1. How long did this take?
2. What was clear about the process?
3. What was confusing or felt unnecessary?
4. What was missing that you expected to see?
5. What would you change?

Write their answers to the "System Onboard Feedback" section of `_system/feedback.md`.

Run `/done` to close this session.
