# Tools & Platforms

Operational profiles for tools and platforms used in the system. Check here before asserting tool capabilities from general knowledge.

**Convention:** `_system/tool-integration-convention.md` governs how tools connect — connector shape, auth scoping, enrichment composition, documentation standards. Read it before building your first connector.

**Adding a new tool:** Use `/connect-tool` — it researches the tool, evaluates alternatives, and generates a convention-compliant connector with documentation. Or follow the convention manually if you prefer.

## Internal Tools

*Tools built into this system (scripts, API wrappers, pipelines). Each tool gets a row here for selection, plus a deeper `tools/[name]/profile.md` for operational knowledge loaded on demand.*

| Tool | Location | Purpose | When to Use |
|------|----------|---------|-------------|
| *(empty — add tools as you build them)* | | | |

## External Platforms

*Third-party tools and APIs accessed via MCP or direct integration. Capture operational knowledge as you use them — quirks, limitations, rate limits, what the docs don't tell you.*

| Platform | API Domain | Purpose | Key Learnings |
|----------|-----------|---------|---------------|
| *(empty — add platforms as you integrate them)* | | | |

## Tool Profile Shape

Every tool gets two levels of documentation (index + depth pattern):

1. **Selection entry here** — what it does, when to use it, cost. Lightweight, always loadable.
2. **Operational profile at `tools/[name]/profile.md`** — deep knowledge: throughput, failure modes, quality data, usage examples. Loaded on demand.

Required profile fields: Data source, Input required, Output, Throughput, Cost, Strengths, Weaknesses, Failure mode. See `_system/tool-integration-convention.md` for the full specification.

**Progressive accumulation:** Profiles get smarter over time. When a session reveals something real — a capability confirmed, a cost discovered, a gotcha hit — update the profile immediately. Never pre-populate from general knowledge. Every line in a profile should trace to a real session.

---

*Updated by `/done` when tool learnings surface during sessions. Check `.claude/settings.json` → `sandbox.network.allowedDomains` to verify API domains are permitted before first use.*
