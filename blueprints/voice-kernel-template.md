---
type: blueprint
description: "Template for creating client voice kernels. Client kernels extend the shared base (_system/voice-base.md) with audience-specific conventions."
status: working-draft
convention: blueprints/frontmatter-convention.md
---

# Voice Kernel Template

Use this template when creating a voice kernel for a new client or engagement. Every kernel extends the shared base at `_system/voice-base.md` — don't duplicate base content here. This file contains ONLY what's different for this client.

**Loading order:** Composition skills load `_system/voice-base.md` first, then the client kernel. Client kernel content extends or overrides the base where specified.

---

## How to Build a Kernel

Kernels are **extracted from real work, not designed from imagination.** A kernel filled in from "describe your voice" produces adjective-driven specs that don't work.

### Path 1: Existing Deliverables (preferred)

A structured interview, not a form to fill:

1. **"Show me 2-3 pieces of writing you're proud of for this client."** These are the gold standards. Everything that follows is pattern extraction from them.
2. **Read each piece and extract:** Who is this written for? What do they already know? What pronouns does the author use for themselves, their team, the client? What's the structural pattern? What's conspicuously absent (jargon avoided, context not explained, sections that don't exist)?
3. **Cross-check against the shared base** (`_system/voice-base.md`). Which base decision rules are already visible in the gold standards? Which are violated intentionally (that's a register adjustment)? What's present in the gold standards that the base doesn't cover?
4. **Populate only what the gold standards demonstrate.** Leave sections empty if the evidence isn't there. A thin kernel extracted from real work beats a comprehensive kernel designed from theory.

### Path 2: Cold Start (no writing samples)

Compose bare → operator edits → the delta IS the kernel seed.

1. **Compose something real** for this client — not a test prompt, a real deliverable. No kernel loaded. Score against `blueprints/criteria/voice.md`.
2. **Operator edits the output.** Every correction is an editorial judgment call made explicit.
3. **Extract the corrections as kernel entries.** "Changed 'we recommend' to 'I think X — but want your thoughts'" → Decision Rule: recommend with invitation, not authority.
4. **Run again with the kernel loaded.** Score. Correct. Extract. The kernel grows from accumulated corrections.

### Maturity progression

A new kernel will be thin — 5-7 entries extracted from real evidence. That's correct. It grows through the correction feedback loop in `/compose` Step 4, not upfront specification.

---

## Template

```markdown
---
type: voice-kernel
description: "[Client name] editorial judgment patterns — how [operator] writes for this client's external content"
status: working-draft
workspace: [workspace-slug]
convention: blueprints/frontmatter-convention.md
---

# Voice Kernel — [Client Name]

[One sentence: what this kernel covers and what kind of content it applies to.]

**Extends:** `_system/voice-base.md` (loaded first, always)

---

## Audience Model

> **What this controls:** Everything downstream. Register, vocabulary ceiling, detail depth, assumption baseline. If the audience model is wrong, the voice is calibrated for the wrong listener.

[Who reads this content? What do they already know? What don't they know? What do they care about?]

The trap: describing demographics ("mid-level marketing managers, 30-45"). That tells the agent nothing about how to write. Instead: what does this reader already assume? What would bore them? What would lose their trust? What's the fastest way to show you're worth their time?

---

## Pronoun Convention

> **What this controls:** Attribution and agency. Readers subconsciously track who's responsible for what.

| Actor | Convention | Example |
|-------|-----------|---------|
| [Operator individually] | [I / my name] | "[Example from real content]" |
| [Operator's team] | [We / team name] | "[Example]" |
| [Client team] | [Client name / the team / they] | "[Example]" |
| [End users / audience] | [you / they / specific role] | "[Example]" |

---

## Register Adjustments

> **What this controls:** Where this client's voice DEVIATES from the operator's base.

Only list deviations from the base. If the base is right, this section can be empty. Deviations should state what changes AND why.

---

## Domain Vocabulary

> **What this controls:** The jargon boundary.

| Use | Instead of | Why |
|-----|-----------|-----|
| [domain term] | [generic alternative] | [audience context] |

Don't list every term. List the ones where the DEFAULT choice would be wrong.

---

## Format Conventions

> **What this controls:** Structural expectations. Structure is voice.

Capture the structural patterns that recur in this client's deliverables and that the agent wouldn't produce by default.

---

## Sensitivity Constraints

> **What this controls:** What can be said at all. Overrides every other section.

---

## Transformation Examples

> **What this controls:** Calibration. Real before/after pairs anchor the standard to concrete output.

**Generic:** "[Bad version]"
**On-brand:** "[Good version from real work]"
*What changed: [What the kernel did]*

The best transformation examples show the EDITORIAL JUDGMENT the kernel encodes, not just word substitution.
```

---

*The shared base (`_system/voice-base.md`) plus a thin client kernel should be sufficient for most engagements. Kernels grow through the correction feedback loop in `/compose`, not upfront specification. A 20-line kernel that captures the real differences is better than a 150-line kernel that restates the base.*
