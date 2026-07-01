#!/bin/bash
# Context re-injection after compaction.
# Fires on SessionStart when the session was compacted (matcher: compact).
# Restores critical orientation context that compaction may have degraded.
#
# For SessionStart, plain stdout text is added to Claude's context.

STATE_FILE="$CLAUDE_PROJECT_DIR/_system/session-state.md"

if [ -f "$STATE_FILE" ]; then
  echo "COMPACTION RECOVERY (hook: compact-reinject) — Session state preserved before compaction:"
  echo ""
  cat "$STATE_FILE"
else
  cat <<'REORIENT'
COMPACTION RECOVERY (hook: compact-reinject) — Context was just compacted. Critical references:

- Current session: Check git log --oneline -5 to see recent work
- Marketing expertise index: resources/marketing/index.md (knowledge routing destination)
- System backlog: _system/backlog.md (task tracking)
- System architecture: _system/system-philosophy.md (what exists, conventions)

If you've lost track of the current activity, state what you remember and ask the operator to fill gaps. Do NOT guess or reconstruct from assumptions.

IMPORTANT: The operator's CLAUDE.md Compact Instructions should also be present. This hook supplements them — it doesn't replace them.

REORIENT
fi

exit 0
