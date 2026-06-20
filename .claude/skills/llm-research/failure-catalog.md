# Prompt Failure Catalog

**Loaded by:** Step 2 as a post-draft safety net — scan the active checklist, fix any that apply.
**Updated by:** Step 7 when a research session surfaces a new failure mode.
**Purpose:** Lean quality gate. Only items that caught real problems in real sessions.

---

## Active Checklist

### Composition Framing

- [ ] **Format labels trigger template-matching.** "Write a landing page" produces sales page templates regardless of voice direction. "Write the argument that makes someone sign up" produces argument-first composition. When composition keeps failing, change the format label.

### Prompt Design

- [ ] **No hints or examples that anchor the answer.** Parenthetical examples and candidate answers turn the model into a yes-man. Force it to derive, not confirm.
- [ ] **Context orients without prescribing.** Every context element should pass: "Does the model need this to understand the situation, or am I steering?" No internal jargon, no stakeholder details that imply what the answer should be.
- [ ] **Scope naming matches full intent.** If the research covers a full process, name the full scope — not just the most salient component.

### Interaction Architecture

- [ ] **Critique-first is a separate turn.** Placing critique instructions at the end of a substantive prompt gets ignored across all three models. If critique-first matters, it's a separate message. Enforced in SKILL.md Step 2: Paste 1 must be short (~300 words) with critique as the primary action.
- [ ] **Artifact separated from critique request.** All three models skip critique and jump to research when the full artifact is included alongside. Two-paste workflow enforced in SKILL.md Step 2.

### Cross-Pollination (Step 5)

- [ ] **Lead with evaluation, not integration.** "Evaluate these concepts — do they hold up?" preserves the receiving model's critical judgment. "Incorporate these strong findings" kills it.

### Scaffold

- [ ] **No `claude.md` filename in research folders.** macOS is case-insensitive — Claude Code auto-loads it as project instructions. Use `claude-desktop.md`.

Scan after drafting. Fix any that apply.

---

## Observation Log

*New failure modes discovered during research sessions go here before being promoted to the active checklist.*

*Empty at install. Grows through use.*
