# Governor

**Control AI resource use during execution while preserving the required quality and reliability floor.**

Governor manages model/effort choices, context, retrieval, tools, retries, reuse, verification depth, and stopping. It operates inside the execution envelope defined by the task and, when available, by **Scale**.

## Runtime identifier

`governor`

## Core boundary

- **Scale** decides the execution architecture, capability floor, dependencies, mandatory gates, and re-plan boundaries.
- **Governor** adapts resources inside that envelope using observed progress and failure signals.

Governor may reduce waste. It may not silently lower the user's goal, hard constraints, mandatory quality gates, permissions, or critical reliability requirements.

## Repository structure

- `SKILL.md` — canonical runtime.
- `references/` — operational governance, context/retrieval, benchmark, and contract guidance.
- `knowledge/` — 20 deeper Governor modules plus shared architecture knowledge.
- `scripts/validate_contract.py` — execution-contract validation.
- `scripts/aggregate_benchmarks.py` — evidence aggregation without invented precision.
- `scripts/audit_skill.py` — static Skill audit.
- `evaluation/STATUS.md` — evidence boundaries.

## Knowledge loading

Start with `SKILL.md`. Use `knowledge/README.md` as the retrieval map and load only modules relevant to the current decision.
