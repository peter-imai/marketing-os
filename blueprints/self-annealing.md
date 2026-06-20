# Self-Annealing Framework

A framework for evaluating and designing self-maintenance into system components. Applied to any system that needs to maintain coherence over time without constant manual intervention.

**Orienting methodology — Munger Inversion:** "What will cause us ruin? Work backwards to prevent it." Rather than asking "how do we keep this healthy?" start from "what kills this system's intelligence?" and design backwards from the failure modes.

---

## The Core Question

"If nobody actively maintains this component for 30 sessions, what breaks — and what catches it?"

Every system component drifts. Documentation goes stale. Conventions stop being followed. The question isn't whether drift happens — it's whether the system detects and corrects it, or whether it accumulates silently.

---

## Five Healing Categories

### Category 1: Within-Session Healing

Corrections during a single session. Startup loads context. Shutdown routes knowledge. Hooks enforce checks.

**Failure mode:** Only catches things that go wrong DURING a session. Cross-session drift is invisible.

### Category 2: Between-Session Healing

Next session starts → loads current state → connects dots. Memory carries state forward. Git preserves changes.

**Failure mode:** Only works if the next session is the right TYPE. 20 client sessions won't catch system-level drift.

### Category 3: Periodic Healing

Scheduled maintenance passes. Architecture audits. Decision reviews. Backlog triage.

**Failure mode:** Depends on maintenance actually happening. The cadence-check hook is your trigger mechanism.

### Category 4: Structural Prevention

Architecture that prevents drift entirely. Separation of concerns. Permission rules. Defense in depth.

**Failure mode:** Only covers anticipated failure modes.

### Category 5: Emergent Improvement

The system gets better through use. Knowledge routing compounds expertise. Decision logging preserves reasoning. Method capture improves blueprints.

**Failure mode:** First thing that degrades when Categories 1-4 break.

---

## Evaluation Dimensions

For any system component, evaluate across seven dimensions:

| Dimension | Question |
|-----------|----------|
| **Drift type** | What specifically goes wrong if nobody maintains this? |
| **Detection mechanism** | What catches the drift? Name it. |
| **Detection latency** | How many sessions before drift is noticed? |
| **Healing mechanism** | What corrects it? (Automatic? Agent-assisted? Manual?) |
| **Mechanism failure mode** | When does the healing itself fail? |
| **Compounding cost** | Is undetected drift linear or exponential? |
| **Structural option** | Could this be made self-healing? At what cost? |

### Detection Latency Is the Critical Variable

Components with detection latency >10 sessions AND high compounding cost are the highest-priority targets.

---

## Health Classification

| Classification | Meaning | Maintenance Burden |
|----------------|---------|-------------------|
| **Self-healing** | Drift detected and corrected automatically. | Zero |
| **Assisted healing** | Drift surfaced to operator who corrects it. | Low |
| **Periodic healing** | Drift only caught by deliberate inspection. | Medium |
| **Unmonitored** | No detection mechanism. Accumulates until failure. | High (hidden) |

**The danger zone: "unmonitored" + "high compounding cost."**

---

## Application Procedure

1. **Invert first.** What kills this component? Name the ruin scenario.
2. **Name the drift.** What specifically degrades?
3. **Map current healing.** Walk the five categories — what exists?
4. **Measure detection latency.** How many sessions before someone notices?
5. **Assess compounding cost.** If this drifts for 30 sessions — 5-minute fix or multi-session rebuild?
6. **Check the downstream chain.** Does the healing mechanism depend on another mechanism?
7. **Decide on intervention.** Self-healing? Assisted? Accepted periodic? Or low enough risk to leave?
8. **Wire it in.** Connect to an existing maintenance pathway (startup, shutdown, hook).

---

## Operator Hygiene Boundary

**System responsibility:** Detection, prevention, enforcement.
**Operator responsibility:** Triggering maintenance sessions on cadence, responding to warnings, confirming knowledge.

The system should make the operator's hygiene habits minimal and obvious. The ideal: 2-3 things done reliably, system handles the rest.
