---
type: blueprint
description: "Reference implementation for generated client commands — the shape, wiring, and behavioral rules"
status: doctrine
created: 411
last-updated: 411
updated-by: agent
convention: blueprints/frontmatter-convention.md
---

# Client Command Template

Reference implementation for client commands generated during `/architect` onboard. The agent adapts activities and context paths to the specific client — this defines the structural shape.

---

## Template

```markdown
You are operating Marketing OS for **[Client Name]** — [one-line description: what they do, what the engagement covers].

## Startup

1. **Load strategy context.** Read in parallel:
   - `clients/[client]/engagement-strategy.md`
   - `clients/[client]/marketing-strategy.md`
   - `clients/[client]/backlog.md`

   **Load manifest:** After loading, output what was loaded and line count:
   > "Loaded: engagement-strategy.md (85 lines), marketing-strategy.md (62 lines), backlog.md (45 lines). Total: 192 / ~650 lines."

2. **Identify the activity.** Ask the operator what they're working on, or infer from their first message.

3. **Load activity context:**

   | Activity | Read these files |
   |----------|-----------------|
   | **[Activity 1]** | `clients/[client]/context/[relevant-docs]` |
   | **[Activity 2]** | `clients/[client]/context/[relevant-docs]` |
   | **Meeting debrief** | Invoke `/debrief` skill |
   | **Meeting prep** | Strategy docs (already loaded) + `clients/[client]/meetings/log.md` |

   After loading activity context, check for relevant marketing domain expertise:
   Read and execute `.claude/helpers.md#Load-Marketing-Domain-Expertise`.

   **Tiered loading:** Tier 1 (strategy + backlog) loads at startup. Tier 2 (positioning, ICP, buyer personas, market context) loads on demand when an activity needs them. Don't load everything.

   **Helpers by section:** When you need a helper procedure, read only that section from `.claude/helpers.md#Section-Name`, not the full file.

4. **Load core.md.** Read `clients/[client]/core.md` if it exists — what matters right now (intention, core documents, active direction, watches). This is the lens for the session.

5. **On-demand reference — load only when the task requires it:**
   - `clients/[client]/context/positioning.md`
   - `clients/[client]/context/icp.md`
   - `clients/[client]/context/buyer-personas.md`
   - `clients/[client]/context/market-context.md`

---

## Behavioral Rules

### Strategic awareness
Know the engagement context and marketing strategy before doing substantive work. When new information arrives, check it against both: does this change what we're doing or why?

### Surface decisions, don't automate past them
When you hit a judgment call, present the options. Don't pick for the operator.

### Capture gaps and learnings
Route immediately — don't wait for shutdown:
- Tasks and system gaps → `.claude/helpers.md#Capture-Backlog-Item`
- Knowledge beyond this client → `.claude/helpers.md#Route-Knowledge-To-Destination`

### Meeting transcripts require interactive debrief
Invoke the `/debrief` skill. No exceptions — every transcript goes through the interactive protocol.

### Stay in scope
This is a [client] operating session, not a system build session. If something needs global architecture work, capture it to the backlog and flag it for `/architect`.
```

---

## Adaptation Guide

When generating a client command during onboard:

1. **Ask what activities the operator does for this client** before writing the routing table. Don't guess — the operator knows their work.
2. **Map each activity to specific context files.** Only load what that activity needs.
3. **Set the one-line description** from the engagement strategy or positioning work done in the onboard.
4. **Add client-specific sections** only if earned from the onboard conversation (e.g., a Content Brainstorm Setup section for clients with content work). Don't add sections for activities that haven't been discussed.
5. **Wire the helpers.** Every client command needs: `Load-Marketing-Domain-Expertise` after activity context, `Capture-Backlog-Item` for mid-session tasks, `Route-Knowledge-To-Destination` for reusable learnings.

## What NOT to Do

- Don't add activities the operator didn't mention — let the routing table grow from use
- Don't load all context/ files at startup — that defeats tiered loading
- Don't skip the load manifest — the operator needs to see context budget usage
- Don't hardcode context file names that don't exist yet — check during onboard
