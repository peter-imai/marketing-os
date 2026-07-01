# Output Convention — File Placement and Naming

> **When to load:** At skill start, to determine where output files go.
> **Purpose:** Defines where market research files are written, how they're named, and the distinction between raw and processed output.

---

## Determining the Output Directory

Market research output goes into the workspace's context directory. The exact path depends on workspace structure:

**Simple engagement structure** (single engagement per workspace):
```
workspaces/[name]/context/
```

**Multi-engagement structure** (multiple engagements):
```
workspaces/[name]/engagements/[engagement]/context/
```

At skill start, check which structure the workspace uses:
1. Look for `workspaces/[name]/engagements/` — if it exists, ask the operator which engagement this research is for.
2. If no engagements directory, use `workspaces/[name]/context/`.
3. If the workspace directory doesn't exist yet, create it with the simple structure unless the operator specifies otherwise.

## File Map

### Deliverables (workspace context directory)

| File | Phase | Description | Loaded in sessions? |
|------|-------|-------------|-------------------|
| `market-research.md` | 4.5 | Primary synthesis — the document that gets loaded every session | Yes — always |
| `icp.md` | 1 | Detailed Ideal Customer Profile | On demand |
| `competitive-landscape.md` | 3 | Named competitors, do-nothing analysis, trigger events | On demand |
| `buyer-personas.md` | 4 | Detailed buyer personas | On demand |
| `customer-evidence.md` | 5 | URL catalog of social proof and case studies | On demand |
| `targeting-sources.md` | 6 | Niche data sources for list building | On demand |

### Raw Research (working materials)

All raw subagent output goes into `_inputs/research/` within the context directory:

| File | Phase | Content |
|------|-------|---------|
| `00-engagement-brief.md` | 0 | Operator interview capture |
| `01-icp-raw.md` | 1 | Raw subagent output |
| `02-market-context-raw.md` | 2 | Raw subagent output |
| `03-competitive-raw.md` | 3A | Raw subagent output (named competitors only) |
| `04-personas-raw.md` | 4 | Raw subagent output |
| `05-evidence-raw.md` | 5 | Raw subagent output (if phase was run) |
| `06-sources-raw.md` | 6 | Raw subagent output (if phase was run) |

### Why the Separation

- **Deliverables** are processed, synthesized, annotated with operator input, and designed to be loaded into future sessions. They're the product.
- **Raw outputs** are the working materials — useful for reviewing what the subagent found, checking sources, or re-processing. They're reference, not the deliverable.

## Naming Rules

- All filenames are lowercase, hyphenated, `.md` extension
- No date prefixes on deliverables (they get updated, not versioned)
- Raw files include their phase number prefix for sort order
- The `_inputs/` directory uses underscore prefix convention (working materials, not deliverables)
