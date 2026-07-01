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
- The reference connector implementation named in `_system/tool-integration-convention.md` — Python connector shape (loaded at Step 5)
- `_system/tool-integration-convention.md` — the governing convention (loaded at Step 5 for compliance check)
- `tools/index.md` — existing tool intelligence (loaded at Step 2 for dedup)

**Subagent strategy:**

| Operation | Sequential/Parallel | Agent Type | Context Needed | Output |
|-----------|-------------------|------------|---------------|--------|
| Tool research + evaluation | Parallel with user follow-up | general-purpose | Tool name or need description, job it does, preferences (CLI > SDK > raw HTTP) | Structured research brief |

**Coordination model:** Research subagent returns a structured brief (evaluation, alternatives, API shape). Main context consumes the brief for generation. Research runs in parallel with any follow-up questions to the operator.

---

## Step 1: Quick Interview

Get enough to start research. Ask conversationally — not a numbered list.

**Two entry modes:**

**A. Operator names a tool** (e.g., `/connect-tool super-dev` or "I want to connect Apollo"):
1. Confirm the tool name.
2. Ask: "What job does this do for you?" One sentence — what data or capability does this add?
3. Ask: "Will you use this in scripts/pipelines (Python connector) or through the agent interactively (MCP)?" If unclear, use the decision logic from the convention: batch/unattended → Python, agent-mediated → MCP.

**B. Operator describes a need** (e.g., "I need to verify phone numbers" or "I need company technographic data"):
1. Acknowledge the need. Don't pick a tool yet — that's the research subagent's job.
2. Ask: "Anything you've already looked at, or should I start from scratch?"
3. Note: the research subagent prompt in Step 3 changes for this mode — it's a discovery search, not a tool evaluation.

If the operator provided an argument, start in mode A with the name already known.

---

## Step 2: Dedup Check

Before any research, check if we already have this tool or something that does the same job.

1. Read `tools/index.md` — scan for the tool name, the API it wraps, or a tool serving the same job.
2. Glob `tools/*/client.py` — check for existing connectors.
3. **If the exact tool exists:**
   - Present what we have: connector location, profile summary, current state.
   - Ask: "We already have this. What needs updating — new endpoints, profile refresh, conformance fix?"
   - Proceed as an update session: read the existing connector, identify gaps vs. the convention, make targeted edits. Do NOT create a new connector. Do NOT scaffold from scratch.
4. **If a different tool serves the same job:**
   - Present what we have and ask: "We have [existing tool] for [same job]. Do you want a second option, or is this a replacement?"
5. **If nothing found** → proceed to Step 3.

---

## Step 3: Research

Launch a **general-purpose subagent** for research. Adapt the prompt to the entry mode from Step 1.

### Mode A: Named Tool

**Subagent prompt:**

> Research the external tool **[tool name]** for integration into a marketing automation system. The tool's job: [job description from Step 1].
>
> **Four jobs:**
>
> **Job 1: Evaluate the tool.**
> - Is it actively maintained? Last release/update date?
> - Documentation quality — clear API docs? Interactive explorer (Swagger, Postman)?
> - Pricing model — free tier? Per-call cost? Subscription?
> - Known reliability issues, outage history?
>
> **Job 2: Check for existing packages and CLIs.**
> We have a strong preference order: **CLI > existing Python package > raw HTTP connector.**
> - Is there a CLI? If yes: name, install command, what it can do.
> - Is there a well-maintained Python package on PyPI? If yes: name, install command, GitHub stars, last release, whether it's officially maintained by the vendor.
> - If a good CLI or Python package exists, note that we may not need to write a raw connector at all.
> - **Script interface check:** Does the CLI or package accept output file paths as arguments (e.g., `--output`, `-o`)? We require data-producing tools to accept `--input`/`--output` args rather than hardcoding destinations. Note whether this is natively supported or would need a thin wrapper.
>
> **Job 3: Check 2-3 alternatives for the same job.**
> - The job is: [job description from Step 1]
> - Compare: pricing, API quality, CLI/package availability, data quality/coverage, docs.
> - Flag if an alternative is clearly better for this job.
>
> **Job 4: Extract API shape** (for the tool we'll likely connect — original or best alternative).
> - Auth method (API key header, OAuth2, bearer token) and exact header format
> - Base URL
> - Key endpoints: name, HTTP method, path, input fields, output fields
> - Rate limits (documented)
> - Response format and key field names
> - Gotchas, quirks, or undocumented behaviors from docs/forums
> - **Auth complexity flag:** If auth requires OAuth2 with token refresh, PKCE, or any multi-step flow, flag this prominently — it changes the connector architecture.
>
> **Output as a structured brief:**
>
> ```
> ## Tool Evaluation
> - Name:
> - Website:
> - Docs URL:
> - Status: [active/maintained/stale/deprecated]
> - Docs quality: [good/adequate/poor/none]
> - Pricing:
> - Red flags: [or "none"]
>
> ## Existing Packages & CLIs
> - CLI: [name + install command, or "none found"]
> - Python package: [name + install + stars + last release, or "none found"]
> - Recommendation: [use CLI / use package / build raw connector]
>
> ## Alternatives
> | Alternative | Pricing | CLI/Package? | Docs | Why consider |
> |-------------|---------|--------------|------|-------------|
>
> ## Recommendation
> [Proceed with original / Consider [alternative] / Use existing [CLI/package] / Red flags — discuss]
>
> ## API Shape
> - Auth: [method, header format, env var suggestion]
> - Auth complexity: [simple API key / OAuth2 — describe flow]
> - Base URL:
> - Endpoints:
>   - [name]: [METHOD] [path] — [what it does]
>     - Input: [key fields]
>     - Output: [key fields]
>     - Rate limit: [if documented]
> - Response notes:
> - Gotchas:
> ```

### Mode B: Need-Based Discovery

**Subagent prompt:**

> I need to find the best tool for this job: **[need description from Step 1]**.
> Context: This is for a marketing automation system that does data enrichment, outreach, CRM, and research.
>
> **Three jobs:**
>
> **Job 1: Discover candidates.** Find 3-5 tools that serve this need. For each: name, what it does, pricing, docs quality, whether it has a CLI or Python package.
>
> **Job 2: Compare and recommend.** Rank them. Strong preference for: CLIs > Python packages > raw APIs. Factor in: data quality, pricing, docs, community, maintenance status.
>
> **Job 3: Extract API shape for the top recommendation.** Same format as the API Shape section above.
>
> **Output as a structured brief** — same format as above, but with the Alternatives section as the primary content and a clear top recommendation.

While the subagent researches, ask the operator any follow-up questions from Step 1 that weren't fully answered.

---

## Step 4: Decision Checkpoint

When the research subagent returns, present findings and surface decisions:

1. **If CLI or Python package exists:** "There's a [CLI/package] for this (`[install command]`). Want to use that instead of building a raw connector?" This is the first option to consider — building a connector when a good package exists is wasted work.

2. **If alternatives look stronger:** Present the comparison. "Research found [alternative] — [reason it's better]. Proceed with [original] or switch?"

3. **If red flags found** (stale, no docs, deprecated, opaque pricing): Surface explicitly. Recommend against unless the operator has a specific reason.

4. **If auth is complex (OAuth2, multi-step):** Flag it. "This tool uses [OAuth2/PKCE/etc.] — the connector will need token management and refresh logic, which is more complex than our standard API-key pattern. Worth the investment, or is there a simpler alternative?" This changes the scope of Step 5 significantly.

5. **If Mode B (need-based discovery):** Present the top recommendation with rationale. "Research recommends [tool] for [job] because [reasons]. Here are the other candidates: [brief comparison]." The operator must confirm which tool before proceeding — don't assume the recommendation.

6. **If everything is clean and simple API-key auth:** Summarize the API shape. "Looks solid — simple API key auth, [N] endpoints, documented rate limits. I'll generate the connector."

**Wait for operator decision before proceeding.**

---

## Step 5: Generate

**Route based on operator's decision in Step 4:**
- **Python connector** → Step 5-Python
- **MCP connector** → Step 5-MCP
- **Use existing CLI/package** → Step 5-Existing

---

### Step 5-Python: Generate Python Connector

**5-Python-a. Create folder + env template.**

```
tools/[name]/
├── client.py       # Generated connector
├── SETUP.md        # First-run instructions
└── .env.example    # Auth template (operator copies to .env)
```

`.env.example`:
```
# [Tool Name] API credentials
# Copy to .env and fill in your key: cp .env.example .env
[TOOL]_API_KEY=your-key-here
```

**5-Python-b. Generate `client.py`.**

Read the reference connector implementation named in `_system/tool-integration-convention.md`. Generate a new client following the same structural pattern, populated from the research brief:

- **Module docstring** — tool name, what it wraps, auth method, rate limits, cost, all endpoints with input/output, usage example. Include gotchas from research.
- **`_load_env()` + config** — copy verbatim from reference. Set `BASE_URL`, env var name (`[TOOL]_API_KEY`), `MAX_RPS` at 50% of documented rate limit with comment noting the documented limit.
- **Response types** — one `@dataclass` per endpoint response, based on API shape from research. Every response type gets a `raw: dict = field(default_factory=dict)` field. Use `Optional` for fields that may be absent.
- **Rate limiter** — `RateLimiter` class matching the reference. Add `ENDPOINT_RPS` dict if research suggests different endpoints have different limits.
- **Client class** — one method per endpoint. Each method: builds payload, calls `_post`/`_get`, returns typed response. Docstring with input/output example. No business logic.
- **HTTP layer** — use `http.client.HTTPSConnection` with persistent connection (matching reference), not `urllib.request`. Persistent connections matter for batch work.
- **Batch support** — if API supports concurrency, add `batch_[operation]()` using `concurrent.futures.ThreadPoolExecutor`. If unclear, add `# TODO: batch support — test concurrency limits` comment.
- **CLI quick-test** — `if __name__ == "__main__"` block testing the simplest endpoint.

**Rules:**
- stdlib only.
- Methods map 1:1 to API endpoints. No business logic in the client.
- All credentials via env vars from `_load_env()`. Never hardcoded.
- Rate limit at 50% of documented. Comment the documented limit.
- **Script interface:** If the connector includes a CLI entry point or batch function that writes data files, it MUST accept `--input`/`--output` arguments. Scripts don't hardcode file paths — the agent passes convention-correct paths at invocation time. See `_system/tool-integration-convention.md` § Script Interface.

**If auth is OAuth2** (flagged in Step 4): The connector needs additional infrastructure — a `_refresh_token()` method, token storage (file-based, in the tool directory), and automatic refresh on 401. This is significantly more complex. State this to the operator and generate the additional auth machinery. Reference: no existing connector uses OAuth yet, so this would be the first — flag any design decisions for the operator.

**5-Python-c. Generate `SETUP.md`.**

First-run instructions: where to get an API key, which plan, `cp .env.example .env`, test command, documented rate limits.

**5-Python-d. Add selection entry + operational profile.**

Two files, following the index+depth pattern:

1. **`tools/index.md`** — read the file, add a row to the API Clients table. One-line summary: what it does, when to use it, cost. Keep it lightweight.
2. **`tools/[name]/profile.md`** — create the full operational profile with **frontmatter** (`type: tool-profile`, `description`, `status: working-notes`, `created`/`last-updated` as session numbers, `updated-by: joint`). Follow the Tool Profile Shape in the convention (Required Fields table + any Additional Fields from research). Mark unverified fields with `(from docs — unverified)`. Reference an existing `tools/[name]/profile.md` for format. **Must include a Usage Example section** — a copy-pasteable code block showing correct instantiation (import path, env setup, rate limiter), a single API call, and how to read the response fields. This prevents the agent from rediscovering wiring on every use.

---

### Step 5-MCP: Generate MCP Connector

For MCP tools, the output is documentation only — no code.

1. **Add selection entry to `tools/index.md`** (one row in External Platforms table) **+ create `tools/[name]/profile.md`** with **frontmatter** (`type: tool-profile`, `description`, `status: working-notes`, `created`/`last-updated` as session numbers, `updated-by: joint`) and MCP-specific fields: all MCP tool names, cached vs. live data, tested vs. untested capabilities, workspace selection, auth mechanics. Include a Usage Example section showing a typical agent interaction pattern (which tools to call, in what order, what to expect back).

2. **Create expertise stub** at `knowledge/marketing/[platform].md` with frontmatter (`type: resource`, `status: working-notes`) and sections for Architecture Patterns and Gotchas — both "To be developed through use."

3. **Note MCP server configuration.** If the MCP server isn't already in `.claude/settings.json`, tell the operator what to add and present the configuration.

---

### Step 5-Existing: Document Existing CLI/Package

When the decision is to use an existing CLI or Python package instead of building a raw connector:

1. **Add selection entry to `tools/index.md`** + **create `tools/[name]/profile.md`** with **frontmatter** (`type: tool-profile`, `description`, `status: working-notes`, `created`/`last-updated`, `updated-by: joint`) — same Required Fields, but note the install method (`pip install X` or `brew install X`), link to the package docs, and any wrapper patterns we use. Include a Usage Example section with install + instantiation + a single call.

2. **Create `tools/[name]/SETUP.md`** with install instructions and a quick-test command.

3. **Don't create a `client.py`** — the package IS the client. If we need a thin wrapper (for auth loading or rate limiting the package doesn't handle), note that as a future task, don't build it speculatively.

---

## Step 6: Present, Route Auth, & Review

### 6a. Present What Was Created

1. **What was created** — list all files with one-line descriptions.
2. **Research highlights** — pricing, alternatives considered, CLI/package options, any gotchas.
3. **What needs verification** — flag any endpoint implementations generated from docs that need real-call testing.

### 6b. Auth Routing

Route the new tool into workspace auth manifests so commands can load its credentials.

1. **Compose the auth.yaml snippet** from what Step 5 generated:
   - **Python / Existing path:** Extract env var names from the connector (e.g., `[TOOL]_API_KEY`). Snippet shape:
     ```yaml
     tools:
       [name]:
         env_vars: [[TOOL]_API_KEY]
     ```
   - **MCP path:** Extract workspace or account info. Snippet shape:
     ```yaml
     mcp:
       [name]:
         workspace: "[workspace name]"
     ```
   - If a tool needs both (env vars AND MCP workspace), compose both sections.

2. **List workspaces.** Glob `workspaces/*/auth.yaml` and `workspaces/*/engagements/*/auth.yaml`. Present: which workspaces exist, which already have auth.yaml, and the snippet to add.

3. **Ask:** "Which workspaces need this tool? (Or 'none' to skip.)"

4. **For each selected workspace:**
   - If `auth.yaml` exists: read it, append the tool entry under the appropriate section (`tools:` or `mcp:`). Don't duplicate if the tool already appears.
   - If `auth.yaml` doesn't exist: create a minimal one:
     ```yaml
     # [Workspace Name] — Workspace Auth Manifest
     # Convention: C1. See _system/tool-integration-convention.md § Auth Scoping.
     # Secrets: workspaces/[name]/.env (gitignored). This file declares WHAT — .env holds values.

     env_file: .env  # relative to this directory

     tools:
       [name]:
         env_vars: [[TOOL]_API_KEY]
     ```
   - Remind operator: "Add the actual key to `workspaces/[name]/.env` — the auth.yaml only declares the variable name."

5. **If "none":** Skip cleanly. No auth.yaml changes.

### 6c. Next Steps

- For Python connectors: "Copy `.env.example` → `.env`, add your key, run `python tools/[name]/client.py` to test."
- For MCP: "Add the server config to `.claude/settings.json`, then test via a real interaction."
- For existing packages: "Install with `[command]`, then test."
- All paths: "After real usage, update `tools/index.md` with validated operational data — hit rates, actual throughput, gotchas discovered."

---

## Error Handling

- **No API docs found:** Tell the operator. Ask for docs, Postman collection, or example requests. If nothing → abort. Don't generate from guesses.
- **Tool is deprecated or unmaintained:** Surface finding + alternatives. Recommend against unless operator has specific reason.
- **Unclear rate limits:** Generate with conservative 1 req/sec default and `# TODO: validate rate limit` comment. Flag in review.
- **OAuth2 or complex auth discovered mid-research:** Handled in Step 4 as a decision checkpoint. Not an error — a scope change.
- **Tool already exists (dedup):** Handled in Step 2. Update, don't duplicate.
- **MCP server doesn't exist for the tool:** Recommend Python path. Building MCP servers is out of scope.
- **Need-based search finds no good options:** Tell the operator. Discuss whether the need can be met differently (manual process, different data source, combining existing tools).

---

## Permissions

| Category | Requirement | Purpose |
|----------|-------------|---------|
| Files | Write: `tools/**` | Create connector directory and files |
| Files | Edit: `tools/index.md` | Add tool profile |
| Files | Write: `knowledge/marketing/**` | Create MCP expertise doc (MCP path only) |
| Files | Read/Write: `workspaces/**/auth.yaml` | Auth routing — read existing, append or create |
| Network | WebSearch, WebFetch | Research tool docs and alternatives |
| Subagent | general-purpose agent | Tool research and evaluation |

---

## Quality Experiments

See `.claude/helpers.md#Quality-Experiments`.
