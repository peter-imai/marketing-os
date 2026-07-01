---
step: 1
title: "Orient — load voice stack, select format, load source material"
next: 02-intent.md
reads:
  - _system/voice-base.md
  - workspaces/[workspace]/context/voice-kernel.md
  - playbooks/[format].md
  - Workspace source material
  - contacts.yaml (email format)
writes: []
---

# Step 1: Orient

**Goal:** Load everything the agent needs to compose well — voice stack, format playbook, source material — and confirm the foundation with the operator before developing intent.

---

## Rules

- Load files in parallel where possible (voice base + kernel + source material in one batch).
- Never proceed to intent development without operator confirmation of the foundation.
- If a workspace is missing a voice kernel, note it: "No voice kernel for [workspace] yet. I'll compose from the voice base only. Corrections this session will seed the kernel."

---

## Instructions

### 1. Identify the active workspace

If already in a workspace command session, use that workspace. If invoked standalone, ask: "Which workspace is this for?"

### 2. Confirm or select format

Apply the format inference logic from SKILL.md. If the format is already determined (context inference or argument hint), confirm it: "Composing an email for [workspace]. Right?"

If not determined, present the menu: "What are we composing? **Email** / **data writeup** / **persuasive long-form**?"

### 3. Load the voice stack

Read in parallel:

1. **Voice base:** `_system/voice-base.md`
2. **Workspace voice kernel:** `workspaces/[workspace]/context/voice-kernel.md`
3. **Format playbook:** `.claude/skills/compose/playbooks/[format].md`

If the voice kernel doesn't exist for this workspace, load only the voice base. Flag it but don't block.

### 4. Load source material

Load the workspace's foundation docs:

- `workspaces/[workspace]/context/positioning.md` — required. If missing: "Copy without positioning produces generic output. Consider building this first."
- `workspaces/[workspace]/context/buyer-personas.md` or audience doc
- Product description or overview doc
- Messaging candidates or sharp language doc (if it exists)
- Any convictions or voice doc specific to this workspace

If the workspace is missing multiple foundation docs, don't work around it: "This workspace needs [missing docs] before we can write effective copy. Consider building them first."

**For email format, additionally:**
- Read `contacts.yaml` — look up recipients by name. Get email addresses, roles, company.
- If email is TBD for a recipient, flag it: "I don't have [name]'s email address yet."
- If replying to a thread: use `search_gmail_messages` + `get_gmail_thread_content` to pull conversation history. Match `user_google_email` to the send-from account.
- Infer send-from account from engagement → accounts mapping in `contacts.yaml`.

### 5. Present the foundation

Summarize what you're working from:

- "**Voice:** [base + kernel status]. Format playbook: [format name]."
- "**Positioning:** [1-2 sentence core thesis from loaded docs]"
- "**Sharpest language I found:** [2-3 lines from source docs]"
- "**Reader:** [who this is for + their current state]"

For email, also:
- "**To:** [names + emails]. **From:** [send account]. **Thread:** [new / reply to X]"

### 6. Confirm

"Does this feel right, or should I adjust the angle? Anything from your thinking that should be in the room?"

**Wait for operator confirmation before proceeding to Step 2.**

---

## Success Criteria

- [ ] Voice base loaded
- [ ] Client kernel loaded (or absence noted)
- [ ] Format playbook loaded
- [ ] Source material loaded
- [ ] Foundation summary presented to operator
- [ ] Operator confirmed before proceeding

---

## Next

Proceed to `02-intent.md`.
