# 09 — Tool dan retrieval routing

Sebelum menaikkan model, cek apakah kebutuhan sebenarnya adalah alat.

| Gejala | Resource pertama |
|---|---|
| fakta terbaru | web / sumber resmi |
| keputusan project lama/berkas | file search/read |
| aritmetika/statistik | calculator/code |
| perubahan repo | Codex + tests |
| lokasi data di banyak dokumen | retrieval/RAG |
| aksi eksternal | connector/app + verification |
| gambar/PDF visual | multimodal inspection |

## Tool call budget

Tool call harus menjawab dependency. Jangan mencari web hanya untuk “menambah kedalaman” jika sumber internal sudah cukup dan pertanyaan tidak berubah waktu.

Stop retrieval ketika:
- sumber authoritative sudah menjawab klaim utama;
- sumber tambahan hanya duplikat;
- quality gate evidence sudah terpenuhi;
- pencarian tambahan tidak mengubah keputusan.

Tetap lanjut jika ada konflik sumber material atau evidence belum mencakup klaim kritis.