# 04 — Router Chat, Work, dan Codex

## Chat

Gunakan Chat untuk percakapan, penjelasan, perencanaan, analisis satu/few-step, review, dan keputusan yang tidak memerlukan agentic execution panjang.

## Work

Gunakan Work ketika tugas perlu dijalankan sampai menjadi deliverable: banyak langkah, browser/cloud computer, beberapa berkas/apps, riset-eksekusi-verifikasi, atau proyek yang membutuhkan state lebih panjang. Dokumentasi OpenAI mendeskripsikan Work sebagai agent untuk pekerjaan lebih panjang, multi-step, dan finished deliverables.

## Codex

Gunakan Codex ketika pusat pekerjaan adalah software engineering: membaca repo, mengubah banyak file, menjalankan test, debugging, terminal, dan technical workflow.

## Surface-first rule

Jangan memilih model sebelum surface bila surface sendiri menentukan kemampuan tool dan mode kerja. Contoh: tugas website yang hanya perlu strategi UI bisa selesai di Chat; implementasi repo sebaiknya berpindah ke Codex; audit lintas browser/files/apps mungkin lebih cocok Work.

Sumber: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex