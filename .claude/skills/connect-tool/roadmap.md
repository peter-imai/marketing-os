# Connect Tool — Roadmap

V2+ ideas. Promote to `_system/backlog.md` when mature.

## V2: Conformance Mode

`/connect-tool --check [name]` — reads an existing connector and grades it against the convention. Reports: what's missing, what's non-conformant, what to fix. This is T-274 (conformance pass) packaged as a skill mode rather than a one-off task.

## V2: Batch Connect

When connecting multiple tools in sequence (e.g., during a new client onboard), skip redundant questions and streamline the research phase.

## V2: Auto-Detect from Usage

If a session uses a tool that has no profile in `tools/index.md`, prompt: "I noticed you're using [tool]. Want to run `/connect-tool` to document it?" Requires hook integration.

## V2: Connection Health Check

Periodic validation that existing connectors still work — API endpoints haven't changed, auth is valid, rate limits haven't shifted. Could integrate with `/audit`.
