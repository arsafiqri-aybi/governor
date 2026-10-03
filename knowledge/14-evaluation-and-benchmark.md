# 14 — Evaluasi dan benchmark Governor

## Benchmark minimum

Bangun set tugas proyek nyata dengan kategori:
- trivial;
- routine;
- ambiguous;
- long-context;
- research/current;
- coding/tool-heavy;
- multi-step agentic;
- high-risk/verification-heavy.

Untuk setiap kasus catat:

`surface | model/tier | effort | context size | tools | iterations | outcome | fatal error | time/usage proxy`

## Metrik

- pass rate;
- fatal error rate;
- context/token proxy;
- tool calls;
- iteration count;
- time/allowance use;
- resource cost per passed result;
- escalation frequency;
- unnecessary escalation rate.

## A/B test

Bandingkan:
A. selalu model/effort tinggi;
B. Governor adaptive routing.

Governor berhasil jika B mempertahankan target quality/fatal-error threshold sambil menurunkan resource consumption secara material.