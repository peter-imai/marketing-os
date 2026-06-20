#!/bin/bash
# Self-annealing cadence check — fires on every SessionStart.
# Reads _system/session-log.md for maintenance session freshness.
# If architect or audit sessions are overdue, injects a warning into context.
#
# DESIGN: Munger inversion applied — what causes system ruin? Silent degradation
# when maintenance sessions don't happen. This hook prevents that by making
# the gap visible at the start of every session.

LOG_FILE="${CLAUDE_PROJECT_DIR}/_system/session-log.md"

# Thresholds (in days)
ARCHITECT_THRESHOLD=14
AUDIT_THRESHOLD=28

# If no session log exists, warn about missing infrastructure
if [ ! -f "$LOG_FILE" ]; then
  echo "SELF-ANNEALING: No session log found at _system/session-log.md. Cadence tracking cannot run. Create the log and ensure /done maintains it."
  exit 0
fi

WARNINGS=""
TODAY_EPOCH=$(date +%s)

# Count sessions — suppress maintenance warnings during early onboarding (< 3 sessions)
SESSION_COUNT=$(grep -c '^| 20' "$LOG_FILE" 2>/dev/null) || SESSION_COUNT=0
SUPPRESS_MAINTENANCE=false
if [ "$SESSION_COUNT" -lt 3 ]; then
  ONBOARD_FILE="${CLAUDE_PROJECT_DIR}/_system/onboard-log.md"
  if [ -f "$ONBOARD_FILE" ]; then
    ONBOARD_STATUS=$(grep '^\*\*Status:\*\*' "$ONBOARD_FILE" | head -1 | sed 's/\*\*Status:\*\* //')
    if [ "$ONBOARD_STATUS" = "in-progress" ]; then
      SUPPRESS_MAINTENANCE=true
    fi
  fi
fi

# Find last architect session date (suppress during early onboarding)
if [ "$SUPPRESS_MAINTENANCE" = "false" ]; then
  LAST_ARCHITECT_DATE=$(grep '| architect |' "$LOG_FILE" | tail -1 | awk -F'|' '{print $2}' | xargs)
  if [ -n "$LAST_ARCHITECT_DATE" ]; then
    LAST_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST_ARCHITECT_DATE" +%s 2>/dev/null)
    if [ -n "$LAST_EPOCH" ]; then
      DAYS_SINCE=$(( (TODAY_EPOCH - LAST_EPOCH) / 86400 ))
      if [ "$DAYS_SINCE" -gt "$ARCHITECT_THRESHOLD" ]; then
        LAST_SESSION=$(grep '| architect |' "$LOG_FILE" | tail -1 | awk -F'|' '{print $3}' | xargs)
        WARNINGS="${WARNINGS}- ARCHITECT session overdue: last was ${DAYS_SINCE} days ago (${LAST_ARCHITECT_DATE}, ${LAST_SESSION}). Guideline: every ${ARCHITECT_THRESHOLD} days. System conventions, backlog, and architecture may have drifted.
"
      fi
    fi
  else
    WARNINGS="${WARNINGS}- ARCHITECT session: none found in session log. System maintenance has no recorded baseline.
"
  fi

  # Find last audit session date
  LAST_AUDIT_DATE=$(grep '| audit |' "$LOG_FILE" | tail -1 | awk -F'|' '{print $2}' | xargs)
  if [ -n "$LAST_AUDIT_DATE" ]; then
    LAST_EPOCH=$(date -j -f "%Y-%m-%d" "$LAST_AUDIT_DATE" +%s 2>/dev/null)
    if [ -n "$LAST_EPOCH" ]; then
      DAYS_SINCE=$(( (TODAY_EPOCH - LAST_EPOCH) / 86400 ))
      if [ "$DAYS_SINCE" -gt "$AUDIT_THRESHOLD" ]; then
        LAST_SESSION=$(grep '| audit |' "$LOG_FILE" | tail -1 | awk -F'|' '{print $3}' | xargs)
        WARNINGS="${WARNINGS}- AUDIT overdue: last was ${DAYS_SINCE} days ago (${LAST_AUDIT_DATE}, ${LAST_SESSION}). Guideline: every ${AUDIT_THRESHOLD} days. Run /audit for system health diagnostic.
"
      fi
    fi
  else
    WARNINGS="${WARNINGS}- AUDIT: none found in session log. No system health diagnostic on record.
"
  fi
fi

# Focus queue check
BACKLOG_FILE="${CLAUDE_PROJECT_DIR}/_system/backlog.md"
FOCUS_NEXT=""
if [ -f "$BACKLOG_FILE" ]; then
  FOCUS_NEXT=$(awk '/^## Focus Queue/{found=1;next} /^## /{found=0} found && /\[ \]/' "$BACKLOG_FILE" | head -1 | sed 's/^[0-9]*\. \[ \] //')
fi

# Onboarding check
ONBOARD_FILE="${CLAUDE_PROJECT_DIR}/_system/onboard-log.md"
ONBOARD_MSG=""
if [ -f "$ONBOARD_FILE" ]; then
  ONBOARD_STATUS=$(grep '^\*\*Status:\*\*' "$ONBOARD_FILE" | head -1 | sed 's/\*\*Status:\*\* //')
  if [ "$ONBOARD_STATUS" = "in-progress" ]; then
    # Count milestones as proxy for session count
    MILESTONE_COUNT=$(grep -c '^\- \[Session' "$ONBOARD_FILE" 2>/dev/null) || MILESTONE_COUNT=0

    # Check if all core concepts (1-3) have both Introduced and Reinforced filled
    CORE_REINFORCED=true
    for CONCEPT_NUM in 1 2 3; do
      ROW=$(grep "^| ${CONCEPT_NUM} |" "$ONBOARD_FILE")
      INTRODUCED=$(echo "$ROW" | awk -F'|' '{print $4}' | xargs)
      REINFORCED=$(echo "$ROW" | awk -F'|' '{print $5}' | xargs)
      if [ "$INTRODUCED" = "—" ] || [ -z "$INTRODUCED" ] || [ "$REINFORCED" = "—" ] || [ -z "$REINFORCED" ]; then
        CORE_REINFORCED=false
        break
      fi
    done

    if [ "$CORE_REINFORCED" = "true" ]; then
      ONBOARD_MSG="- ONBOARDING: Core concepts complete. Ready for graduation. Run \`/audit\` to graduate and transition to maintenance cadence."
    elif [ "$MILESTONE_COUNT" -ge 5 ]; then
      # Find next un-introduced core concept
      NEXT_CONCEPT=""
      for CONCEPT_NUM in 1 2 3; do
        ROW=$(grep "^| ${CONCEPT_NUM} |" "$ONBOARD_FILE")
        INTRODUCED=$(echo "$ROW" | awk -F'|' '{print $4}' | xargs)
        if [ "$INTRODUCED" = "—" ] || [ -z "$INTRODUCED" ]; then
          NEXT_CONCEPT=$CONCEPT_NUM
          break
        fi
      done
      if [ -n "$NEXT_CONCEPT" ]; then
        ONBOARD_MSG="- ONBOARDING: Session ${MILESTONE_COUNT}+ and core concept ${NEXT_CONCEPT} not yet introduced. The /done step will deliver it this session."
      fi
    fi
  fi
fi

# State-layer cap + register check (Phase 2 spec § Enforcement model).
# Reporting, not blocking — fires only when a file is over cap or aggregate over budget.
STATE_CHECK="${CLAUDE_PROJECT_DIR}/tools/hygiene/check-state-caps.py"
STATE_MSG=""
if [ -f "$STATE_CHECK" ]; then
  STATE_MSG=$(python3 "$STATE_CHECK" --quiet 2>/dev/null)
fi

# Output
if [ -n "$WARNINGS" ] || [ -n "$FOCUS_NEXT" ] || [ -n "$ONBOARD_MSG" ] || [ -n "$STATE_MSG" ]; then
  echo "SELF-ANNEALING CADENCE CHECK (hook: cadence-check):"
  if [ -n "$WARNINGS" ]; then
    printf "%s" "$WARNINGS"
  fi
  if [ -n "$ONBOARD_MSG" ]; then
    echo "$ONBOARD_MSG"
  fi
  if [ -n "$STATE_MSG" ]; then
    echo "$STATE_MSG"
  fi
  if [ -n "$FOCUS_NEXT" ]; then
    echo "- FOCUS QUEUE: Next up → ${FOCUS_NEXT}"
    echo ""
  fi
  echo "This is a structural reminder. The operator decides whether to act now or defer."
fi

exit 0
