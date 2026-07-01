# Artifact Creation Principles

How to create files and folder structures that remain useful over time.

---

## Why This Matters

Files are cheap to create and expensive to maintain. A poorly named file, a muddled document, or an over-nested folder structure creates drag on every future session. The agent spends tokens finding things. The operator spends time orienting. Entropy compounds.

These principles apply whenever you create files, folders, or document structures — regardless of output style or activity mode.

## The Principles

### 1. Plan the artifact set first

What documents does this work need? What's the hierarchy? Establish structure *before* you start writing files — not after.

If you don't know what you're building, you're not ready to create files yet. Sketch the artifact set, get alignment, then create.

### 2. Name for findability

Files should be named by what they *are*, not how they were made.

**Good:** `catalog.md`, `spec.md`, `voice-guide.md`
**Bad:** `brainstorm-output.md`, `2026-02-05-discussion.md`, `v2-final-FINAL.md`

Avoid vague names like "Resources," "Notes," or "Misc" — use specific nouns that match how someone would search for this artifact.

### 3. One purpose per document

Each artifact should have a single, clear reason to exist. If you're conflating strategic direction with execution details, or mixing working notes with finished outputs, split them.

Include context for *why* this document exists. Artifacts without stated purpose become dead weight that nobody dares delete.

### 4. Separate working materials from deliverables

Brainstorm outputs, raw LLM responses, and rough notes are *inputs*. Clean documents are *outputs*. Keep them physically distinct.

**Pattern:** Use an `_inputs/` subfolder for working materials. The underscore prefix signals "internal, not the main thing."

This prevents clutter in the main directory and makes it clear what's provisional vs. authoritative.

### 5. Limit hierarchy depth

3-4 levels maximum. Each additional level reduces findability by roughly 20%.

If you need more depth, restructure your top-level categories rather than nesting deeper. Wide and shallow beats narrow and deep.

### 6. Organize for the reader, not the creator

Who will open this file next? What do they need to understand immediately?

Structure documents to serve the reader — not to preserve the order you happened to think of things. Lead with context, then substance, then details.

"Inside-out organization" (structuring by how you created it) produces logical structures that don't match how users actually navigate.

## Application

These principles are embedded in output styles that involve artifact creation. They're also referenced in CLAUDE.md for baseline coverage.

When creating any file or folder:
1. Check: does this follow the six principles?
2. If not: adjust before creating, not after
