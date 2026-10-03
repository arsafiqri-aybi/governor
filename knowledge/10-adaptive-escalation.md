# 10 — Adaptive escalation dan fallback

## Escalation ladder

Mulai dari resource minimum yang rasional. Jika hasil gagal, klasifikasikan penyebab:

1. **Missing context** → ambil konteks relevan.
2. **Missing/fresh evidence** → retrieval/web.
3. **Computation/tool failure** → tool/correct execution.
4. **Ambiguous specification** → perbaiki task contract.
5. **Reasoning bottleneck** → naik effort.
6. **Capability bottleneck** → naik model tier.
7. **Long multi-step execution** → pindah Chat → Work/Codex.

Naik satu axis pada satu waktu jika memungkinkan agar sebab perbaikan dapat diketahui.

## De-escalation

Setelah tahap sulit menghasilkan struktur/keputusan, turunkan model untuk:
- formatting;
- batch extraction;
- simple transformation;
- repeated templated tasks;
- documentation dari hasil yang sudah tervalidasi.

Jika worker mulai gagal quality gate, naikkan kembali secara lokal, bukan seluruh proyek.