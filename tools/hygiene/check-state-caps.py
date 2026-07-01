#!/usr/bin/env python3
"""
State-layer cap + register checker.

Checks auto-loaded state files against:
  - per-file line cap (from frontmatter cap-lines, or fallback registry)
  - aggregate auto-loaded token budget (~10K target)
  - per-bullet word cap in Active Direction / index bullets (frontmatter cap-words-per-bullet)
  - hedging-language regex scan (prohibited list)
  - session-stamp regex scan (date patterns where prohibited)

Fails are REPORTED, not blocking. Regex hits are signals, not verdicts — the
operator evaluates each per-instance. Exit code is always 0.

Usage:
  python3 tools/hygiene/check-state-caps.py            # human report
  python3 tools/hygiene/check-state-caps.py --quiet    # only print if problems (hook mode)
  python3 tools/hygiene/check-state-caps.py --workspace acme   # also check a workspace's state files
"""
import os, re, sys, glob

ROOT = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())

# Auto-loaded system files. Fallback caps for files without frontmatter cap-lines.
# token_budget: counts toward the ~10K aggregate auto-loaded target.
SYSTEM_FILES = [
    ("CLAUDE.md", 200, True),
    # Light base (single-company): core.md = slow-changing identity (loose cap),
    # operating-lens.md = volatile now-state (the re-bloat risk — tighter cap).
    ("core.md", 60, True),
    ("operating-lens.md", 40, True),
    ("_system/core.md", 60, True),  # system governance core, if present
    ("_system/backlog-index.md", 120, True),
    ("MEMORY.md", 200, False),  # harness-managed; counted but frontmatter-exempt
]
AGGREGATE_TOKEN_TARGET = 10000

HEDGES = [
    r"\bit may be that\b", r"\bevidence suggests\b", r"\bapproximately\b",
    r"\btends to\b", r"\boften\b", r"\bgenerally\b", r"\bperhaps\b",
    r"\bsomewhat\b", r"\brelatively\b", r"\bit seems\b", r"\bmight suggest\b",
]
SESSION_STAMP = re.compile(r"\b(S\d{3,}|20\d\d-\d\d-\d\d)\b")


def read(path):
    try:
        return open(path, encoding="utf-8").read()
    except FileNotFoundError:
        return None


def frontmatter_caps(text):
    caps = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return caps
    for line in m.group(1).splitlines():
        cm = re.match(r"(cap-lines|cap-words-per-bullet):\s*(\d+)", line.strip())
        if cm:
            caps[cm.group(1)] = int(cm.group(2))
    return caps


def check_file(relpath, fallback_cap, counts_toward_budget):
    path = os.path.join(ROOT, relpath)
    text = read(path)
    if text is None:
        return None
    lines = text.splitlines()
    nlines = len(lines)
    ntok = len(text) // 4
    caps = frontmatter_caps(text)
    cap = caps.get("cap-lines", fallback_cap)
    word_cap = caps.get("cap-words-per-bullet")

    problems = []
    if nlines > cap:
        problems.append(f"line cap: {nlines}/{cap}")

    if word_cap:
        for i, l in enumerate(lines, 1):
            bm = re.match(r"^\s*[-*]\s+(.*)", l)
            if bm:
                # strip markdown emphasis/links for a fair word count
                body = re.sub(r"[*`\[\]]", "", bm.group(1))
                wc = len(body.split())
                if wc > word_cap + 5:  # +5 tolerance band
                    problems.append(f"bullet L{i}: {wc}w (cap {word_cap})")

    hedge_hits = []
    for h in HEDGES:
        for i, l in enumerate(lines, 1):
            if re.search(h, l, re.I):
                hedge_hits.append((i, h.strip(r"\b")))
    stamp_hits = []
    for i, l in enumerate(lines, 1):
        if SESSION_STAMP.search(l):
            stamp_hits.append(i)

    return {
        "path": relpath, "lines": nlines, "cap": cap, "tokens": ntok,
        "budget": counts_toward_budget, "problems": problems,
        "hedges": hedge_hits, "stamps": stamp_hits,
    }


def run(workspace=None, quiet=False):
    targets = list(SYSTEM_FILES)
    if workspace:
        base = f"workspaces/{workspace}"
        targets += [
            (f"{base}/core.md", 60, True),
            (f"{base}/operating-lens.md", 40, True),
            (f"{base}/backlog-index.md", 120, True),
        ]

    results = [r for r in (check_file(*t) for t in targets) if r]
    agg = sum(r["tokens"] for r in results if r["budget"])

    has_problem = any(r["problems"] for r in results) or agg > AGGREGATE_TOKEN_TARGET
    if quiet and not has_problem:
        return 0

    out = []
    scope = f" (workspace: {workspace})" if workspace else ""
    out.append(f"STATE-LAYER HYGIENE{scope} — caps + register (reporting, not blocking):")
    flag = "OVER" if agg > AGGREGATE_TOKEN_TARGET else "ok"
    out.append(f"- Aggregate auto-loaded: ~{agg} tokens / {AGGREGATE_TOKEN_TARGET} target [{flag}]")
    for r in results:
        status = "; ".join(r["problems"]) if r["problems"] else "ok"
        out.append(f"- {r['path']}: {r['lines']}L/{r['cap']} ~{r['tokens']}tok [{status}]")
        if r["hedges"]:
            sample = ", ".join(f"L{i}:{w}" for i, w in r["hedges"][:4])
            out.append(f"    hedges ({len(r['hedges'])}): {sample}  — signals, evaluate per-instance")
        if r["stamps"] and "backlog-index" not in r["path"] and "MEMORY" not in r["path"]:
            out.append(f"    session-stamps: {len(r['stamps'])} lines (prohibited in terse tier)")
    if has_problem:
        out.append("Run /audit for full conformance pass, or trim before next commit.")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    quiet = "--quiet" in args
    workspace = None
    if "--workspace" in args:
        workspace = args[args.index("--workspace") + 1]
    sys.exit(run(workspace=workspace, quiet=quiet))
