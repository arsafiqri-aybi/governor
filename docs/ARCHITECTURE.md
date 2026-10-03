# Repository architecture

Governor is the adaptive controller inside a task execution envelope.

Authority order:
1. `SKILL.md` — active runtime.
2. `references/` — operational policies.
3. `knowledge/` — deeper resource-governance knowledge and evidence.
4. Git history — change provenance.

Scale defines architecture and protected floors. Governor controls resource allocation inside those boundaries. If the boundary becomes infeasible, Governor requests re-plan rather than weakening quality.

Stable control science must remain separate from fast-changing model/product registry facts.
