# 07 — Model Handoff Protocol

Saat berpindah model/surface, jangan menyalin seluruh chat jika tidak perlu. Buat **handoff packet** yang ringkas dan loss-aware.

## Handoff packet minimum

```text
PROJECT:
CURRENT PHASE:
GOAL OF NEXT STEP:
STABLE DECISIONS:
ACTIVE CONSTRAINTS:
SOURCE/FILES + VERSION:
WHAT HAS BEEN DONE:
WHAT FAILED / WHY:
OPEN QUESTIONS:
NEXT TASK:
ACCEPTANCE TEST:
DO NOT REGRESS:
```

## Handoff quality gate

Model penerima harus dapat menjawab:
- apa tujuan tahap ini;
- apa yang sudah final;
- apa yang belum final;
- bahan mana authoritative;
- apa yang harus dihasilkan;
- bagaimana mengetahui tahap selesai.

Jika tidak, handoff terlalu agresif. Jika paket berisi seluruh riwayat tanpa struktur, handoff terlalu boros.

## Pattern

Gunakan model kuat untuk membuat keputusan arsitektural, simpan keputusan sebagai state file, lalu worker model menerima hanya state + task slice. Setelah selesai, hasil kritis kembali ke verifier/synthesizer.