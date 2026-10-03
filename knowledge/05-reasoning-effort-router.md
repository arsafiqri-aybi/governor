# 05 — Reasoning-effort router

Reasoning effort mengatur seberapa banyak compute/thought yang dialokasikan oleh model yang mendukungnya. Jangan pilih effort dari panjang jawaban yang diinginkan; pilih dari **kesulitan keputusan internal**.

## Tier praktis

**Instant / Fast**
- Q&A sederhana;
- rewrite ringan;
- lookup yang sudah punya sumber;
- format/transformasi jelas.

**Medium / Standard**
- analisis beberapa constraint;
- planning biasa;
- review dokumen;
- keputusan dengan trade-off terbatas.

**High / Extended**
- masalah multi-step;
- architecture/design reasoning;
- riset sintetis dengan konflik;
- debugging sulit;
- rencana proyek besar.

**Extra High / Pro / Extended-Pro jika tersedia**
- masalah paling sulit;
- cross-domain synthesis;
- high-cost-of-error decision support;
- pekerjaan yang gagal pada High;
- satu tahap kritis yang menentukan banyak tahap berikutnya.

## Rule penting

Reasoning effort lebih tinggi tidak menggantikan fakta terbaru, file yang hilang, test software, kalkulator, atau evidence. Naikkan effort hanya jika bottleneck benar-benar reasoning.

Nama kontrol dapat berbeda antar surface/plan. Baca opsi yang benar-benar tersedia saat itu.