---
name: compose
description: Unified composition skill — emails, data writeups, persuasive long-form. Voice-engineered, two-pass method, self-auditing.
argument-hint: [format-or-context]
invokable: true
---

# /compose

One skill for all external composition. Emails, data writeups, landing pages, sales copy. Each format has its own playbook; the method is shared.

**The core method:** Load voice → select format → develop intent → compose in two passes (structure lock, then draft) → self-audit against rubric → capture corrections → deliver.

---

## Format Menu

On invocation, determine the format. Three paths:

**1. Context inference (preferred).** If the conversation already implies a format:
- After `/debrief` → suggest **email** with recipients from the debrief. "Looks like we need a follow-up email. Recipients: [names]. Sound right?"
- Operator said "landing page" or "sales page" → **persuasive**
- Operator said "write up the results" or "summarize the findings" → **data writeup**

**2. Argument hint.** `/compose email`, `/compose landing page`, `/compose writeup`.

**3. Ask.** If neither inference nor hint: "What are we composing? Email / data writeup / persuasive long-form?"

### Format Registry

| Format | Playbook | Delivery | Intent Weight |
|--------|----------|----------|---------------|
| **email** | `playbooks/email.md` | Gmail MCP (draft/send) or file fallback | Light — who, purpose, key info |
| **data-writeup** | `playbooks/data-writeup.md` | File | Light — what happened, for whom, your assessment |
| **persuasive** | `playbooks/persuasive.md` | File | Heavy — full Copy Intent (emotional arc, key moves, proof) |

Future formats (LinkedIn post, newsletter section, nurture sequence) add a playbook and a row. The method doesn't change.

---

## Workflow

```
Step 1: Orient     → 01-orient.md
Step 2: Intent     → 02-intent.md
Step 3: Compose    → 03-compose.md
Step 4: Review     → 04-review.md
Step 5: Deliver    → 05-deliver.md
```

Execute in order. Load one step file at a time. Each step has its own focused context.

---

## Source Material (Convention 6)

This skill composes from the operator's existing language. See `01-orient.md` for the full source material loading protocol.

Load the client's foundation docs: positioning (required), buyer personas, product description, messaging candidates. If the client is missing multiple foundation docs, don't work around them — build them first.

---

## Voice Stack

Every composition loads two voice files before writing:

1. `_system/voice-base.md` — operator constants (editorial posture, decision rules, language constraints). Universal.
2. `clients/[client]/context/voice-kernel.md` — client-specific patterns (audience model, register adjustments, domain vocabulary, transformation examples). Extends the base.

Plus a format playbook (loaded per format selection). The stack: base → kernel → playbook.

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Read: `_system/voice-base.md` | Voice base constants |
| Files | Read: `clients/*/context/voice-kernel.md` | Client voice kernel |
| Files | Read: `blueprints/criteria/voice.md` | Voice rubric for self-audit |
| Files | Read: `clients/*/context/*` | Source material, stakeholder maps |
| Files | Read: `contacts.yaml` | Contact/recipient lookup (email format) |
| Files | Write: `clients/*/measure/voice/` | Score logging |
| Files | Write: `clients/*/artifacts/` | Deliverable output |
| MCP | `mcp__google-workspace__search_gmail_messages` | Thread context (email format) |
| MCP | `mcp__google-workspace__get_gmail_thread_content` | Full thread for replies |
| MCP | `mcp__google-workspace__draft_gmail_message` | Create Gmail draft (default email delivery) |
| MCP | `mcp__google-workspace__send_gmail_message` | Send directly (ask tier — confirm before send) |

| Bash | `python3 tools/gdocs/md_to_gdoc.py *` | Google Docs publish (doc/persuasive delivery) |

Email format uses MCP tools. Other formats use file + optional Google Docs publish. No subagents.

---

## Subagent Strategy

No subagents. The workflow is linear and the operator is in the loop at every step. Composition quality depends on the main context holding the full voice stack + source material + conversation history. Subagent isolation would degrade output.

---

## Measurement

Every composition run scores against the voice rubric (Step 4). Scores log to `clients/[client]/measure/voice/index.md` — the living Score Trajectory. This is persistent quality telemetry. If the file doesn't exist yet for a client, create it from the template in Step 4.

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.

---

*v1.0 — Voice-engineered composition with two-pass method, self-audit, and correction feedback loop.*
