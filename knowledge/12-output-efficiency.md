# 12 — Output efficiency

Penghematan output bukan berarti jawaban selalu pendek. Output harus sepanjang yang dibutuhkan oleh pengguna berikutnya.

## Aturan

- Jangan mengulang prompt pengguna kecuali diperlukan untuk framing.
- Jangan menjelaskan langkah internal yang tidak membantu audit.
- Satukan informasi duplikat.
- Letakkan keputusan/actionable result di depan.
- Berikan detail tambahan hanya jika mengubah pemahaman atau tindakan.
- Untuk artefak, letakkan isi utama di file; respons chat cukup status, keputusan penting, dan link.

## Two-layer output

Untuk topik kompleks, gunakan:

1. **Decision layer:** ringkas, dapat ditindaklanjuti.
2. **Evidence/detail layer:** hanya ketika pengguna perlu menilai alasan atau melakukan audit.

Ini mempertahankan kedalaman tanpa memaksa setiap pembaca memproses semua detail.