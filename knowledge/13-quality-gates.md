# 13 — Quality gates

Governor boleh menghemat resource hanya jika kualitas bisa dibuktikan cukup.

## Gate umum

1. **Task fit:** menjawab tujuan yang benar.
2. **Correctness:** fakta/hitungan/logic utama benar.
3. **Completeness:** syarat wajib terpenuhi.
4. **Evidence:** klaim yang butuh sumber memiliki dukungan.
5. **Execution:** artefak/test/aksi benar-benar terjadi bila diminta.
6. **Risk:** tidak ada error fatal atau pelanggaran constraint.
7. **Usability:** format dapat dipakai oleh tahap berikut/pengguna.

## Gate untuk routing model

Sebuah model/tier dianggap “cukup” jika mencapai target pass rate pada benchmark tugas nyata, bukan karena satu output terlihat bagus.

Jika dua tier sama-sama lulus, pilih yang resource cost lebih rendah. Jika tier murah memiliki failure fatal lebih tinggi, jangan gunakan hanya karena tokennya sedikit.