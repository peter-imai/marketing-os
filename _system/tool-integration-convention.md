---
type: blueprint
description: "How the system integrates with external tools — connector shape, auth scoping, enrichment composition, documentation standard"
status: working-draft
created: 459
last-updated: 468
updated-by: joint
convention: _system/frontmatter-convention.md
---

# Tool Integration Convention

How external tools connect to the system. Covers connector architecture, auth scoping, enrichment composition, and the documentation standard every tool must meet.

---

## Purpose

The system uses external tools for enrichment, outreach, CRM, and research. 14 integrations exist today, built ad hoc. They independently reinvented the same patterns — env var auth, rate limiting, typed responses, JSONL caching, resume. This convention standardizes those patterns so the next connector takes hours, not days, and behaves predictably.

**This convention governs:**
- How tool intelligence is documented (`tools/index.md` + per-tool `profile.md`)
- How Python connectors are structured (`tools/[name]/`)
- How MCP connectors are documented and used
- How auth scopes to client commands
- How enrichment steps compose into pipelines

**Not governed here:** Pipeline-specific logic (what steps to run for a CRM audit). That's engagement-level, not convention-level.

---

## Two Connector Variants

Every tool integration falls into one of two variants. Both get the same tool profile documentation (see Tool Profile Shape). Execution mechanics differ.

### Python Connectors

Code we write and control. The connector wraps an external API with auth, rate limiting, typed responses, and batch support.

**Examples:** BlitzAPI, Pako, Serper, Instantly

**What we own:** Auth loading, rate limiting, response types, batch orchestration.

**File structure:**
```
tools/[name]/
├── client.py       # The connector — one file, stdlib only
├── SETUP.md        # First-run instructions (optional)
└── .env            # Never committed — .gitignore'd
```

**Required connector shape (`client.py`):**

1. **Module docstring** — what it wraps, auth method, rate limits, cost, usage examples. Include validated endpoint behaviors and known API quirks.
2. **`_load_env()` config** — walk up from script to find `.env`. All credentials from environment variables. Never hardcoded.
3. **Response types** — dataclasses for typed responses. Every API response maps to a named type. No raw dicts past the client boundary.
4. **Rate limiter** — client-side rate limiting. Start conservative (50% of documented limit). Add per-endpoint overrides from production experience. The rate limiter is part of the client, not the caller's responsibility.
5. **Client class** — methods map 1:1 to API endpoints. Each method: builds payload, calls `_post`/`_get`, returns typed response. No business logic in the client.
6. **Batch support** — if the tool supports concurrent calls, provide a `batch_*()` function. The caller should never loop sequentially when parallelism is available.

**What stays OUT of the client:** Retry logic (callers wrap with a RetryClient), JSONL caching (callers own persistence), pipeline orchestration (separate scripts).

**Reference implementation:** `tools/blitzapi/client.py`

### MCP Connectors

Tools the agent calls directly via MCP protocol. We don't control the interface. We document how to use them well.

**Examples:** Clay/Schematics (`mcp__schematics__*`)

**What we own:** Documentation, usage patterns, gotcha tracking, cost awareness. NOT the API shape.

**No file structure** — MCP tools are provided by servers configured in `.claude/settings.json`. Our contribution is the tool profile (in `tools/index.md` for selection, in per-tool `profile.md` for operational depth) and platform expertise docs in `resources/marketing/`.

**MCP-specific documentation requirements:**
- List all available MCP tool names and what each does
- Document which tools use cached vs. live data (and when to use which)
- Track tested vs. untested capabilities (capability matrix)
- Record platform-specific gotchas discovered in real sessions
- Note workspace selection and auth mechanics

### Decision Logic: Python vs. MCP

| Question | Python | MCP |
|----------|--------|-----|
| Do we call it from scripts that run unattended? | Yes | No — MCP tools are agent-only |
| Do we need rate limiting we control? | Yes | N/A — server handles it |
| Is it a data enrichment API we call at scale (100+ rows)? | Yes | Depends — some platforms handle scale internally |
| Is it a platform the client's team will use directly? | Build Python for our use | Yes — document MCP for interactive building |
| Does an MCP server already exist for it? | Only if we need script-level control | Yes — use MCP |

**The primary split:** Python connectors are for programmatic batch work that runs in scripts. MCP connectors are for agent-mediated interactive work. Some tools (Clay) serve both roles — MCP for interactive building, Python if we need bulk data push/pull.

---

## Tool Profile Shape

Every tool gets two levels of documentation, following the index+depth pattern used across the system:

1. **Selection entry in `tools/index.md`** — what the tool does, when to use it, cost. Lightweight, always loadable.
2. **Operational profile in `tools/[name]/profile.md`** — deep operational knowledge (throughput, failure modes, quality data, usage guides). Loaded on demand when working with the tool.

This is the system's operational knowledge — what we've learned from real usage, not vendor marketing.

### Required Fields

```markdown
### [Tool Name]

| Attribute | Value |
|-----------|-------|
| **Data source** | What data it accesses (database, website, search index, etc.) |
| **Input required** | Minimum input to get a result |
| **Output** | What comes back — be specific about fields |
| **Throughput** | Requests/sec or concurrency limits, validated from production |
| **Cost** | Per-call or plan cost. Include tier if relevant |
| **Strengths** | What it's best at — with evidence from real runs |
| **Weaknesses** | What it can't do or does poorly — with evidence |
| **Failure mode** | What happens when it fails (silent empty? HTTP error? timeout?) |
```

### Additional Fields (add when known)

- **Quality** — validation results, agreement rates, accuracy from real tests
- **Auth** — header format, env var name
- **Client** — path to connector, typed response classes
- **Endpoints** — if multiple endpoints with different behaviors

### Progressive Accumulation Rule

Profiles get smarter over time. When a session reveals something real — a capability confirmed, a cost discovered, a gotcha hit, a comparison validated — update the profile immediately. `/done` Step 3d checks for this. Never pre-populate from general knowledge. Every line in a profile should trace to a real session.

---

## Auth Scoping

### The Rule

**Commands own tool auth scope.** `/[your-agency]` = one set of API keys for all of that agency's engagements. `/[your-client]` = that client's keys. One client's API key never touches another client's work. This is non-negotiable — it's about costs and trust.

### Auth Loading Standard

Every Python connector loads credentials from environment variables via `_load_env()`:

```python
def _load_env():
    """Load .env file — walk up from script location."""
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        env_file = os.path.join(current, ".env")
        if os.path.exists(env_file):
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, value = line.partition("=")
                        key, value = key.strip(), value.strip().strip("'\"")
                        if key not in os.environ:
                            os.environ[key] = value
            return
        current = os.path.dirname(current)
```

**Env var naming convention:** `[TOOL]_API_KEY` (e.g., `BLITZ_API_KEY`, `SERPER_API_KEY`, `PAKO_API_KEY`).

### Per-Client Auth Mechanics (C1, Decision 105)

Each client has its own `.env` file and an `auth.yaml` manifest declaring what tools and credentials it needs.

**Auth manifest — `clients/[name]/auth.yaml`:**
Declares tool env var names, MCP workspace selections, and contextual account info. Machine-readable — `/audit` can verify, `/connect-tool` can populate, `/new-project` can scaffold. Does NOT contain secrets.

**Shell wrapper — `tools/with-auth.sh`:**
Sources the client's `.env` before running any command. Agent never sees raw secrets.

```bash
# Flat client
tools/with-auth.sh acme python3 tools/serper/client.py ...

# Agency + engagement (layered pattern)
tools/with-auth.sh your-agency/engagement-name python3 tools/instantly/client.py ...
```

**Layered sourcing (agency pattern):**
Agency clients have shared credentials across engagements, plus engagement-specific overrides. `with-auth.sh` handles this by sourcing two `.env` files in order:
1. `clients/your-agency/.env` — agency-level keys (shared APIs)
2. `clients/your-agency/engagements/engagement-name/.env` — engagement-specific overrides

Later values override earlier ones. Unoverridden vars inherit from the client level.

**Command activation:** Each client command reads `auth.yaml` at startup (Step 0) and uses `with-auth.sh` for all tool script invocations. MCP workspace selection happens lazily — when the first MCP tool is needed, not eagerly at startup.

**Existing `_load_env()` in connectors:** Still works as a fallback. `with-auth.sh` sets env vars before the script runs; `_load_env()` only sets vars not already in the environment. So client `.env` wins over project root `.env` without changing any connector code.

---

## Enrichment Composition Model

Enrichment is composable pieces, not monolithic pipelines.

### Three Layers

**Layer 1: Operations.** A single, testable enrichment action.
- Takes defined input (domain, LinkedIn URL, email, company name + location)
- Uses one connector
- Returns defined output (company profile, email address, industry classification)
- Examples: "domain → LinkedIn URL" (BlitzAPI), "classify industry from website" (Pako), "find street address" (Serper Maps)

**Layer 2: Provider Waterfalls.** Multiple providers for the same operation, tried in priority order.
- First success wins — stop calling providers once one returns data
- Same input/output contract regardless of which provider fulfills it
- Example: "find work email" → BlitzAPI Find Work Email → Clay email waterfall → Apollo
- Clay's waterfall columns are this pattern natively

**Layer 3: Pipeline Waterfalls.** A sequence of operations with fallthrough logic.
- Each step feeds the next: search → email → phone → validate
- Steps can run on subsets (only contacts found in step 1 proceed to step 2)
- JSONL cache per step for resume capability
- Example: `contact_enrichment.py` — 4-phase pipeline with per-phase cache

### Composition Rules

1. **Operations are pure.** One input type, one connector, one output type. No side effects beyond the API call. Testable with a single record.

2. **Provider waterfalls own fallback logic.** The caller doesn't decide which provider to try — the waterfall does. The caller says "find work email" and gets an email (or doesn't).

3. **Pipeline waterfalls own sequencing and caching.** Each step writes results to JSONL. Resume reads the cache and picks up where it left off. The pipeline script is the orchestrator.

4. **Tool selection is data-subject-first.** Before picking a tool, ask: "What kind of business is this, and where does the data I need naturally live?" Local service businesses → Google Maps (Serper). Enterprise B2B → LinkedIn (BlitzAPI) + website (Pako). The business context determines the tool. (Validated in practice — Serper 87% vs Pako 3% for interior designer addresses.)

### The Recipe Pattern

For operations that deploy to remote infrastructure, use the recipe-dict pattern from `tools/remote/run.py`:

```python
RECIPES = {
    "recipe-name": {
        "description": "What this recipe does",
        "script": "tools/path/to/script.py",
        "args": ["--phase", "search"],
        "upload": ["input-file.csv", ".cache.jsonl"],
        "download": [".output-cache.jsonl"],
        "deps": ["tools/blitzapi/client.py"],
        "est_minutes": 300,
    },
}
```

Each recipe declares what goes up, what runs, what comes back, and how long it takes. The runner handles deployment mechanics (SSH/SCP/tmux).

---

## File Organization

| What | Where | Purpose |
|------|-------|---------|
| Tool selection index | `tools/index.md` | Catalog, selection matrix, experiment summaries |
| Tool operational profiles | `tools/[name]/profile.md` | Deep operational knowledge per tool — load on demand |
| Python connector code | `tools/[name]/client.py` | The connector — auth, rate limit, types, batch |
| Processing pipelines | `tools/[domain]/[pipeline].py` | Orchestration that composes connectors |
| Remote runner + recipes | `tools/remote/run.py` | Deploy long-running jobs to remote infrastructure |
| Platform expertise docs | `resources/marketing/[platform].md` | Deep knowledge beyond the profile (e.g., Clay architecture patterns) |
| Auth credentials | `.env` (project root, gitignored) | API keys loaded by `_load_env()` |
| MCP server config | `.claude/settings.json` | MCP server connections and permissions |

---

## Anti-Patterns

### Hardcoded credentials
**Precedent:** `tools/pako/client.py` — API key was hardcoded in source until a later conformance pass. Key was in git, couldn't be rotated without a code change, couldn't be scoped per-client. Fixed: migrated to `PAKO_API_KEY` env var with standard `_load_env()`.
**Rule:** All credentials in env vars via `_load_env()`. No exceptions.

### Rate limit discovery in production
**Precedent:** BlitzAPI email endpoint. Default 4.5 req/sec caused constant 429s; sustainable rate was 2.5 req/sec. ~30% of a long run wasted on retry overhead.
**Rule:** Start at 50% of documented limit. Record production-validated rates in the tool profile. Add per-endpoint overrides when endpoints have different limits.

### Duplicated retry logic
**Precedent:** `RetryBlitzClient` in `contact_enrichment.py` wraps `BlitzClient` — correct separation. But `bulk.py` has its own inline retry logic doing the same thing.
**Rule:** The client handles rate limiting. The caller handles retry via a wrapper class. Don't duplicate retry logic across callers — extract a reusable wrapper.

### Sequential calls when batch is available
**Precedent:** Pako's `batch_enrich()` runs 200 concurrent requests. At 846 records: parallel = 3 minutes, sequential would be ~14 hours.
**Rule:** If the tool supports concurrency, the connector MUST expose a batch method. Callers MUST use batch for 2+ records.

### Monolithic pipeline scripts
**Precedent:** `crm-cleanup/bulk.py` — full CRM validation in one file. Later work extracted phases into separate scripts (`contact_enrichment.py`, `pako_classify.py`, `contact_reconcile.py`), which proved more maintainable and composable.
**Rule:** One pipeline script per logical phase. Pipelines compose through JSONL handoff, not function calls within a monolith.

### Hardcoded file paths in scripts
**Precedent:** Enrichment scripts that write to fixed output paths break when reused across projects or when folder conventions change.
**Rule:** Scripts that produce data files MUST accept `--input`/`--output` arguments. The agent passes convention-correct paths at invocation time. Scripts are dumb about where files live — the data project convention (`_system/data-workspace-convention.md`) owns that. `/connect-tool` enforces this for new connectors.
