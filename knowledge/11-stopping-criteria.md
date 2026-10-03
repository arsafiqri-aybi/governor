# 11 — Stopping criteria dan anti-overthinking

Banyak token terbuang bukan karena task sulit, tetapi karena sistem tidak tahu kapan berhenti.

## Stop jika

- acceptance criteria wajib lulus;
- tidak ada error fatal terbuka;
- sumber kritis sudah terverifikasi;
- test yang diwajibkan lulus;
- tambahan iterasi diperkirakan hanya memperhalus gaya, bukan memperbaiki keputusan;
- user meminta hasil sekarang dan evidence cukup.

## Jangan lanjut hanya karena

- “mungkin bisa lebih sempurna” tanpa failure yang jelas;
- ingin mencari lebih banyak sumber setelah evidence sudah saturasi;
- self-review berulang tanpa informasi baru;
- menghasilkan lebih banyak alternatif tanpa kriteria pemilihan.

## Stop condition untuk agent

Setiap loop harus punya `max_attempts`, `success_signal`, dan `failure_exit`. Jika tidak ada kemajuan terukur setelah iterasi, ubah strategi atau laporkan blocker.