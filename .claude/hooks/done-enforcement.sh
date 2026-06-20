#!/bin/bash
# Structural enforcement hook — fires on every UserPromptSubmit.
# When /done is detected, injects critical shutdown checks as additional context.
# For all other prompts, passes through silently (zero overhead).
#
# DESIGN PRINCIPLE: Defense in Depth Through Multi-Channel Redundancy
# Critical behaviors are enforced through multiple layers with different failure modes.
# This hook is one layer — it fires through the infrastructure channel (system injection),
# which has different attention dynamics than command prompts or CLAUDE.md norms.
# The same checks exist in /done steps AND here. The redundancy is intentional.

INPUT=$(cat)

# Check if the submitted prompt is invoking /done
if echo "$INPUT" | grep -qE '(/done|"skill".*done)'; then
  cat <<'ENFORCEMENT'
STRUCTURAL ENFORCEMENT (hook: done-enforcement) — Critical shutdown checks:

1. KNOWLEDGE ROUTING: Did this session produce or discover reusable marketing knowledge (tools, techniques, domain insights, methodology)? If yes, verify it has been routed per resources/marketing/index.md. If not routed, route it now.

2. COMPONENT WIRING + MAINTENANCE: Did this session create new knowledge sources, reference docs, conventions, or system components? If yes: (a) Check which existing commands need awareness and update their startup sequences. (b) For each new artifact: name its read mechanism (how it gets loaded) and its update mechanism (how it stays current). Unwired components don't exist to the system.

3. CLIENT DOCS: If this was a client session, verify:
   - Strategy docs — Did we learn anything about the client, their market, or priorities? Update engagement-strategy.md or marketing-strategy.md.
   - Client backlog — Are task statuses current? New items captured? Completed items moved to Done?
   - data-state.md — If data work happened (list building, enrichment, exports), does it reflect current reality?

4. SYSTEM MAP: Did this session create new files, directories, conventions, or change system structure? If yes, update _system/system-architecture.md — component inventory, folder tree, conventions. If architecture changed, also update narrative sections. The system's self-description must stay current.

5. STRATEGIC AWARENESS: If this was a client session — did new information arrive? Was it analyzed through engagement + marketing strategy lenses, not just filed? Do strategy docs need updating? Stale strategy docs actively mislead.

6. SYSTEM FAILURES: Did the system violate any of its own principles or conventions this session? If yes, log what happened, which principle was violated, and what was done about it.

7. SESSION LOG: Append one line to _system/session-log.md with today's date, session number, command type, and a brief summary. If you skip this, the self-annealing cadence check breaks.

These checks fire through the infrastructure layer independently of /done steps. The redundancy is intentional.
ENFORCEMENT
fi

# Always exit 0 — never block prompt submission
exit 0
