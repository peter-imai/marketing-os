# Start Here

This is Marketing OS — a system that turns your marketing into compounding loops. Campaigns, meetings, research, outreach — every activity becomes a closed loop: execute → measure → learn → feed back → next cycle is sharper. And the loops connect: what you learn from a campaign feeds the next; a client meeting changes how you write their next email.

You'll be slower before you're faster. The first week feels like infrastructure. Then the backlog starts remembering what you forgot, last week's voice corrections show up in this week's drafts without asking, and the system holds you to the standard you set on your best day — even when you're rushing.

Read this once. Then start.

---

## Install

1. **Clone or download this repo somewhere stable.** Any folder you'll remember works — `~/marketing-os/` is a sensible default.
2. **Open the folder in VS Code** (with the Claude Code extension installed). If you don't have Claude Code yet: [docs.claude.com/claude-code](https://docs.claude.com/claude-code).
3. **Start a Claude Code session and run `/start`.**

`/start` handles everything else — output style setup, your profile, your first client, your tools. It explains what it's doing as it goes.

---

## How it works

You collaborate with the system. You tell it what you want; it runs the process; **it gets better every session because you give it feedback and codify what works.** A correction today becomes default behavior next time. A workflow you run three times the same way becomes a one-command step. That's the whole point.

Three rules:

1. **`/done` is mandatory.** Every session ends with `/done`. It captures what you learned, routes it to permanent homes, updates state. Skip it and the work evaporates.
2. **One focus per session.** Strategy *or* content *or* tooling. Mixing degrades quality fastest. Start fresh when you switch.
3. **The system is yours to change.** CLAUDE.md is living configuration. Add rules, build skills, restructure folders. You can't break it; `/audit` catches drift.

---

## Every session has a shape

**Open with a command.** `/[client-name]` for client work, `/architect` for system improvements. Startup loads that client's strategy, backlog, and where you left off.

**Box one piece of work.** Pick the focus before you start.

**Talk to it well.** Correct with reasons ("the tone is too empathetic — this client is direct, no hedging"). Push for specifics ("what specifically — give me the actual recommendation"). Make it critique its own work before you accept it. Three habits, outsized payoff.

**Close with `/done`.** Every time.

New client? Run `/new-project`. It scaffolds the folder, asks the foundation questions, creates a `/[client-name]` command. Next session you open them by name.

---

## Commands you'll use most

| Command | When |
|---|---|
| `/start` | Once, first time — system onboarding |
| `/[your-client-name]` | Every session of client work (e.g., `/acme`) |
| `/new-project` | New client or workspace |
| `/architect` | Improving the system itself |
| `/done` | Every session, always |
| `/debrief` | After a meeting — drop the transcript, get signals routed |
| `/compose` | Drafting emails, copy, data writeups — voice-engineered |
| `/align` | When you want the system to interrogate your thinking before you commit |
| `/audit` | Health check — roughly monthly |
| `/system` | Quick "where am I, what's next" |

You'll learn the others through use.

---

## When something feels off

**Cancel and retry.** Press Escape to stop, Escape again to rewind. Start clean.

**Correct with a reason.** "This is wrong because we don't position this way — we lead with X, not Y." The reason is the instruction — it generalizes; "make it better" doesn't.

**Make the implicit explicit.** If the system keeps getting the same thing wrong, it's correctly following incomplete instructions. Add the rule to CLAUDE.md or the client's strategy doc. Closed gap, permanent improvement.

**Reset when the conversation is too long.** If it's forgetting what you told it earlier, the session has stretched. Save progress to the backlog, run `/done`, start fresh.

---

## Where to go next

- **`curriculum/playbook.md`** — the practice depth. Session shape, backlog discipline, how to build the system in pieces, common early mistakes, advanced patterns. Read end-to-end once; come back to sections as questions surface.
- **`CLAUDE.md`** — the system's operating instructions. You don't need to read this — but know it's there, and know it's yours to edit.
- **`tools/index.md`** — what external tools the system can connect to, and how to add new ones.
- **`resources/marketing/index.md`** — marketing domain knowledge the system can pull from.

---

*One process running well teaches more about system-building than five sketched out. Start with one workflow, close one loop, build from there.*
