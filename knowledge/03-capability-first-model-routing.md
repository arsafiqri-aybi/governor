# 03 — Capability-first model routing

## Jangan hard-code nama model sebagai logika inti

Nama model dan availability berubah. Router menyimpan dua lapis:

1. **Capability classes** yang stabil.
2. **Model registry** yang memetakan model tersedia saat ini ke capability class.

### Capability classes

**FAST** — respons cepat, transformasi sederhana, klasifikasi, ekstraksi mudah.

**BALANCED** — pekerjaan rutin yang butuh kualitas baik dengan biaya/latensi moderat.

**DEEP** — perencanaan, knowledge work, riset, debugging, reasoning multi-constraint.

**FRONTIER/PRO** — tugas paling sulit, lintas domain, professional workflows, computer use, kompleksitas tinggi, atau ketika kegagalan mahal dan model yang lebih ringan sudah gagal.

## Routing rule

Pilih capability class terendah yang diperkirakan lulus quality gate. Jika gagal karena kapasitas model, naik satu tier. Jika gagal karena data/tool, perbaiki data/tool tanpa menaikkan tier terlebih dahulu.

## Anti-pattern

- “Astra untuk semuanya.”
- “Luna selalu cukup karena murah.”
- Mengganti model ketika masalahnya sumber tidak ada.
- Menjadikan panjang prompt sebagai pengganti kemampuan model.