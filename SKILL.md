---
name: governor
description: "Control AI resources during execution while preserving required quality: model and effort choices, context, retrieval, tools, verification, retries, reuse, and stopping. Use when resource choices materially affect cost, latency, reliability, or progress, or when the user asks for Governor. Do not change the user's goal, hard constraints, or mandatory quality gates."
---

# Governor

Minimize unnecessary total resource **subject to the required result still being accepted**. Resource includes reasoning effort, context, retrieval, tools, retries, coordination, verification, latency, and measured cost/quota when those values are actually known.

Governor does not grant tools, permissions, models, or account capabilities.

## 1. Read the active state

Start from the latest user goal, hard constraints, accepted artifacts, unresolved blockers, required quality gates, dependency versions, and known resource limits.

If a Scale execution contract exists, operate inside it. If no explicit contract exists, derive only the minimum working envelope from the current instructions. Do not invent budgets, permissions, model identity, or hidden limits.

Use [Governor policy](references/governor-policy.md) when the optimization boundary is unclear.

## 2. Diagnose before spending more

Classify the bottleneck before escalating:
- ambiguity;
- missing/stale information;
- lost context;
- reasoning deficit;
- model capability ceiling;
- environment/tool failure;
- weak verification;
- stale/corrupt state;
- workflow defect;
- security/trust issue;
- observed resource ceiling.

Do not solve every failure with “more reasoning”. Retrieval fixes information deficits; tools fix deterministic computation; state inspection fixes unknown effects; Scale re-plans workflow defects.

## 3. Choose the next resource action

Possible actions include:
- trim or expand active context;
- retrieve targeted evidence;
- reuse a still-valid verified artifact;
- change strategy;
- vary effort inside the allowed range;
- choose another available model/tool inside the envelope;
- add verification targeted at the failed property;
- stop a stagnant strategy and request re-plan.

Compare **total work until accepted**, not one-step cost. A cheap first attempt is wasteful when failure is predictable and repair is expensive.

Use [model and effort guidance](references/model-effort-guide.md) as a prior, never a universal ranking.

## 4. Context, retrieval, tools, and reuse

Use [context, retrieval, and tools](references/context-retrieval-tools.md).

Preserve:
- goal and hard constraints;
- exact numbers, negations, and exceptions;
- accepted decisions and artifact versions;
- blockers, gates, provenance, and material uncertainty.

Compress or archive superseded alternatives, redundant logs, duplicate evidence, and irrelevant history while keeping recoverable source material when audit value exists.

Cache/reuse is valid only when semantic fit, dependency versions, freshness, permissions, and quality state still match.

## 5. Retry and escalation

Retry only after a material success condition changes: arguments, evidence, strategy, state, capability, tool health, or environment.

Do not blindly repeat side-effecting actions when the previous effect is unknown. Inspect resulting state first.

Escalate effort/model only when reasoning or capability is the diagnosed bottleneck. Do not force a low→medium→high→max ladder.

If the contract boundary is reached with a failed required gate, request **Scale re-plan** rather than weakening the gate.

## 6. Stop with the right status

- `COMPLETE`: required outputs and required gates pass with evidence; required dependencies/effects are resolved.
- `BUDGET_EXHAUSTED`: an observed resource ceiling was reached before completion.
- `BLOCKED`: essential input, access, or capability is missing.
- `REPLAN_REQUIRED`: the current route/structure is no longer viable.
- `APPROVAL_REQUIRED`: a new authorization is genuinely needed.
- `FAIL_CLOSED`: stop risky action when authorization/integrity is uncertain.

If the accepted result is already achieved, stop additional work. If progress plateaus with an open gate, stop the **strategy**, not the goal.

## 7. Measure and learn

Use [benchmark policy](references/benchmark-policy.md) and `scripts/aggregate_benchmarks.py` for measured evidence. Keep published benchmarks, local behavioral tests, deterministic script tests, and heuristics as separate evidence classes.

Do not claim savings without a comparable baseline and actual measurement. Keep tokens, time, tool calls, retries, cost/quota, and quality separate unless a weighting scheme has been explicitly justified.

Normally do not narrate every micro-decision. Surface major route changes, escalations, blockers, approval needs, quality/resource trade-offs, and completion evidence.
