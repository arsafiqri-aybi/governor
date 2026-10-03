# 19 — Chat playbook

## Prompt 1 — Route one task

`Governor: analisis tugas ini dan beri surface/model/effort paling efisien yang tidak menurunkan kualitas. Jelaskan hard gate dan kapan harus eskalasi: [tugas].`

## Prompt 2 — Route a project

`Governor: pecah project ini menjadi tahap. Untuk tiap tahap tentukan tujuan, Chat/Work/Codex, capability tier/model jika tersedia, reasoning effort, context yang harus dibawa, tool, quality gate, handoff, dan escalation trigger. Jangan memakai model terkuat jika tier lebih rendah diperkirakan lulus.`

## Prompt 3 — Audit workflow yang boros

`Governor: audit workflow ini. Temukan context, model tier, reasoning, tool call, iterasi, dan output yang tidak memberi marginal value. Pertahankan semua quality gate.`

## Prompt 4 — Handoff

`Governor: buat handoff packet minimum untuk memindahkan tahap ini ke model/surface berikut tanpa kehilangan keputusan, sumber, constraint, dan acceptance tests.`

## Output routing yang disarankan

```text
Task class:
Surface:
Model/capability tier:
Reasoning effort:
Context to load:
Tools:
Workflow:
Quality gate:
Escalate if:
Stop when:
Handoff:
```