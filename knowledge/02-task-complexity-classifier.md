# 02 — Task Complexity Classifier

Nilai delapan dimensi dari 0–3. Skor adalah alat triase, bukan kebenaran mutlak.

| Dimensi | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Reasoning depth | langsung | beberapa langkah | multi-constraint | strategi/cross-domain sulit |
| Ambiguity | jelas | sedikit asumsi | banyak trade-off | tujuan perlu dibentuk |
| Freshness/evidence | stabil | 1 sumber | beberapa sumber | riset/konflik sumber |
| Context volume | kecil | satu dokumen | beberapa berkas | project besar/long context |
| Tool complexity | tidak ada | 1 tool | beberapa tool | agentic/multi-app |
| Deliverable | jawaban | draft | artefak | multi-file/production |
| Verification | ringan | cek utama | rubric/test | high-stakes/multi-gate |
| Coordination | satu tahap | 2–3 tahap | banyak tahap | multi-model handoff |

### Heuristik

- **0–5:** direct/low effort.
- **6–10:** standard reasoning.
- **11–16:** high reasoning atau workflow terstruktur.
- **17–24:** Work/Codex atau model kuat dengan orkestrasi.

### Hard gates

Skor rendah tidak boleh menurunkan proses bila ada hard gate:

- fakta terbaru yang menentukan keputusan → retrieval/web;
- hitungan kritis → calculator/code;
- dokumen pengguna → files/retrieval;
- software perubahan besar → tests/Codex;
- aksi eksternal → verification/permission;
- dampak tinggi → stronger evidence + review.

Classifier hanya memilih titik mulai. Acceptance test menentukan apakah perlu eskalasi.