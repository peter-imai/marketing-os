#!/usr/bin/env bash
# PreToolUse hook for Bash — blocks multi-line commands except heredocs.
#
# Why: newlines defeat the permission allowlist (Bash(gws *), Bash(git log *),
# etc.) because the matcher sees the whole compound as one string instead of
# distinct commands. Forcing ';' or '&&' chaining means the leading-token
# prefix matches cleanly, and the existing allowlist actually applies.
#
# Heredoc exemption: if the command contains '<<', allow as-is. Real
# multi-line scripts (python3 <<EOF, awk programs, JSON via cat <<EOF) are
# legitimate and shouldn't be blocked.
#
# Fail-open: if jq is unavailable or input parsing fails, allow the command
# and write a warning to stderr. This is an enforcement hook, not a security
# boundary — tooling glitches shouldn't brick all Bash calls.
#
# Exit codes:
#   0 — allow
#   2 — block (Claude Code surfaces stderr to the agent)

set -uo pipefail

payload=$(cat)
cmd=$(printf '%s' "$payload" | jq -r '.tool_input.command // ""' 2>/dev/null) || {
  echo "no-newline-bash hook: jq parse failed, allowing" >&2
  exit 0
}

# Heredoc exemption — pragmatic 'contains <<' check, not a real parse.
# False-negative risk (literal '<<' in an argument + a real newline) is
# acceptable; failure mode is missed enforcement, not blocked work.
if [[ "$cmd" == *"<<"* ]]; then
  exit 0
fi

# Strip trailing newline (some tools append one), then check for any newline.
stripped="${cmd%$'\n'}"
if [[ "$stripped" == *$'\n'* ]]; then
  preview=$(printf '%s' "$cmd" | head -c 200 | tr '\n' '|')
  cat >&2 <<MSG
BLOCKED: Bash command contains a newline.

Newlines defeat the permission allowlist (Bash(gws *), etc.) because
the matcher sees the whole compound as one string instead of separate
commands. Chain with ';' (sequential, ignore failures) or '&&' (stop
on first failure) instead.

Heredocs are allowed — if you need a real multi-line script, use
'python3 <<EOF ... EOF' or similar with the '<<' marker.

Command preview (| marks newline positions):
${preview}
MSG
  exit 2
fi

exit 0
