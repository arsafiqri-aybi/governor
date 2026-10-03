# 08 — Orkestrasi proyek besar

## Pola umum

`Discover → Frame → Research → Architect → Execute → Verify → Integrate → Ship`

Setiap tahap boleh memakai resource berbeda.

### Discover / Frame
Tujuan: definisikan masalah, success criteria, unknowns. Biasanya Medium/High cukup; naik ke frontier jika domain sangat kompleks.

### Research
Utamakan retrieval dan sumber. Model kuat membantu sintesis, tetapi kualitas sumber lebih penting daripada model tier.

### Architect
Ini tahap dengan leverage besar. Gunakan reasoning lebih tinggi bila keputusan arsitektur memengaruhi banyak langkah downstream.

### Execute
Pecah menjadi task slices. Gunakan worker termurah yang lolos test untuk setiap slice. Jangan mempertahankan model frontier hanya karena ia membuat rencana awal.

### Verify
Gunakan tests, sources, deterministic checks, rubrics. Model kuat dipakai untuk review semantis sulit, bukan menggantikan test yang bisa dieksekusi.

### Integrate / Ship
Gunakan synthesizer yang mampu membaca state akhir dan mempertahankan konsistensi lintas output.

## Prinsip

**Strong planner → efficient workers → strong verifier when needed.**