#!/bin/bash
# Desktop notification when Claude Code needs attention.
# Fires on Notification event (permission prompts, idle prompts, etc.)
# macOS only — uses osascript.

osascript -e 'display notification "Claude Code needs your attention" with title "Marketing OS"' 2>/dev/null
exit 0
