---
name: connect-tool
description: "Connect a new external tool to the system. Researches the tool, evaluates alternatives, generates convention-compliant connector + profile.\nTRIGGER when: operator wants to integrate, hook up, or connect a new API, service, or external tool; needs a new connector or tool profile.\nDO NOT TRIGGER when: using an already-connected tool, or operator is doing quick ad-hoc API work without wanting the full setup."
argument-hint: [tool-name]
---

# Connect Tool

Connect a new external tool to Marketing OS. Researches the tool, evaluates alternatives, checks for CLI and existing Python packages, and generates a convention-compliant connector with documentation.

**Input:** Tool name, URL, or description of what data/capability is needed.
**Output:** Convention-compliant connector scaffold + `tools/index.md` selection entry + `tools/[name]/profile.md` operational profile.

**References:**
- `_system/tool-integration-convention.md` — the governing convention (loaded at Step 5)
- `tools/index.md` — existing tool intelligence (loaded at Step 2 for dedup)

---

## Step 1: Quick Interview

Get enough to start research. Ask conversationally — not a numbered list.

**Two entry modes:**

**A. Operator names a tool** (e.g., `/connect-tool apollo` or "I want to connect Instantly"):
1. Confirm the tool name.
2. Ask: "What job does this do for you?" One sentence.
3. Ask: "Will you use this in scripts/pipelines (Python connector) or through the agent interactively (MCP)?" If unclear: batch/unattended → Python, agent-mediated → MCP.

**B. Operator describes a need** (e.g., "I need to verify phone numbers"):
1. Acknowledge the need. Don't pick a tool yet — that's the research subagent's job.
2. Ask: "Anything you've already looked at, or should I start from scratch?"

---

## Step 2: Dedup Check

1. Read `tools/index.md` — scan for the tool name or a tool serving the same job.
2. Glob `tools/*/client.py` — check for existing connectors.
3. **If exact tool exists:** Present what we have, ask what needs updating. Proceed as update session.
4. **If different tool serves same job:** Present and ask — second option or replacement?
5. **If nothing found** → proceed to Step 3.

---

## Step 3: Research

Launch a **general-purpose subagent** for research. Adapt the prompt to the entry mode.

The subagent evaluates the tool (maintenance status, docs quality, pricing, red flags), checks for existing CLIs and Python packages (strong preference: CLI > package > raw HTTP), compares 2-3 alternatives, and extracts the API shape (auth, base URL, endpoints, rate limits, gotchas).

Output as a structured brief covering: Tool Evaluation, Existing Packages & CLIs, Alternatives comparison, Recommendation, and API Shape.

---

## Step 4: Decision Checkpoint

Present findings and surface decisions:

1. **If CLI or Python package exists:** Offer that path first — building a connector when a good package exists is wasted work.
2. **If alternatives look stronger:** Present the comparison.
3. **If red flags found:** Surface explicitly. Recommend against unless the operator has reason.
4. **If auth is complex (OAuth2):** Flag scope change.
5. **If Mode B:** Present top recommendation with rationale. Operator must confirm.
6. **If clean and simple:** Summarize API shape, proceed.

**Wait for operator decision before proceeding.**

---

## Step 5: Generate

Route based on operator's decision:

### Step 5-Python: Generate Python Connector

Create `tools/[name]/` with:
- `client.py` — stdlib only, one method per endpoint, typed responses, rate limiter at 50% of documented limit, persistent HTTP connections, batch support if applicable
- `SETUP.md` — first-run instructions
- `.env.example` — auth template

**Rules:** stdlib only. Methods map 1:1 to endpoints. All credentials via env vars. Rate limit at 50% of documented. Scripts that write data files MUST accept `--input`/`--output` arguments.

### Step 5-MCP: Document MCP Tool

No code — documentation only:
- `tools/index.md` entry + `tools/[name]/profile.md` with MCP-specific fields
- `resources/marketing/[platform].md` expertise stub
- MCP server configuration note for `.claude/settings.json`

### Step 5-Existing: Document CLI/Package

- `tools/index.md` entry + `tools/[name]/profile.md` with install method
- `tools/[name]/SETUP.md` with install + test
- No `client.py` — the package IS the client

---

## Step 6: Present, Route Auth, & Review

### 6a. Present What Was Created

**Before presenting, run `.claude/helpers.md#Self-Critique-Gate`** on the generated connector + docs. The bar: does it follow the connector convention (clean auth via the env-var/`.env` pattern, no hardcoded secrets, docstrings, real error handling, declared deps)? Would it actually run on a first call, or did I generate plausible-looking code I haven't traced? Fix what's broken; flag what I couldn't verify.

List files, research highlights, what needs verification.

### 6b. Auth Routing
Route the new tool into client auth manifests (`clients/[name]/auth.yaml`).

1. Compose the auth.yaml snippet from what Step 5 generated
2. List existing clients with auth.yaml files
3. Ask which clients need this tool
4. For each selected client: append to or create auth.yaml. Remind operator to add actual key to `.env`.

### 6c. Next Steps
- Python: "Copy `.env.example` → `.env`, add key, run `python tools/[name]/client.py` to test."
- MCP: "Add server config to settings.json, test via real interaction."
- Existing: "Install with `[command]`, then test."
- All: "After real usage, update `tools/index.md` with validated operational data."

---

## Error Handling

- **No API docs:** Ask for docs, Postman collection, or example requests. If nothing → abort.
- **Tool deprecated:** Surface + alternatives. Recommend against.
- **Unclear rate limits:** Conservative 1 req/sec default with TODO comment.
- **OAuth2 discovered:** Decision checkpoint in Step 4.
- **Tool already exists:** Update, don't duplicate (Step 2).
- **No good options found:** Tell operator, discuss alternatives.

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Write: `tools/**` | Create connector directory and files |
| Files | Edit: `tools/index.md` | Add tool profile |
| Files | Write: `resources/marketing/**` | Create expertise doc (MCP path) |
| Files | Read/Write: `clients/**/auth.yaml` | Auth routing |
| Network | WebSearch, WebFetch | Research tool docs and alternatives |
| Subagent | general-purpose agent | Tool research and evaluation |
