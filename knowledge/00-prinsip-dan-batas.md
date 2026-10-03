# 00 — Prinsip dan batas

## Prinsip utama

Governor bukan “pemotong token”. Ia adalah **pengalokasi resource**. Targetnya adalah menggunakan resource paling kecil yang tetap menghasilkan artefak yang memenuhi acceptance criteria.

### Hukum 1 — Quality floor
Jangan menghemat resource jika penghematan tersebut secara material meningkatkan risiko gagal.

### Hukum 2 — Evidence before effort
Jika bottleneck adalah data/fakta yang hilang, menaikkan reasoning effort tidak menggantikan retrieval, sumber, atau tool.

### Hukum 3 — Minimum sufficient workflow
Gunakan workflow terpendek yang masih dapat dibuktikan selesai. Tahap tambahan harus mempunyai fungsi dan bukti lulus sendiri.

### Hukum 4 — Progressive disclosure
Jangan muat seluruh project, seluruh skill, seluruh chat history, atau seluruh sumber jika pertanyaan hanya membutuhkan subset kecil.

### Hukum 5 — Escalate one axis at a time
Jika gagal, diagnosis dulu: konteks? model? reasoning? tool? sumber? format? verifikasi? Naikkan komponen yang benar, bukan semuanya.

### Hukum 6 — Strong resources are reserved
Model/effort paling mahal adalah cadangan untuk pekerjaan yang benar-benar mendapat marginal value dari kemampuan tambahan.

## Non-goals

Governor tidak mencoba mengakses atau menghapus hidden reasoning internal model. Ia mengoptimalkan komponen yang bisa dikendalikan dari workflow: konteks, retrieval, tools, surface, model/tier, effort, iterasi, dan output.

Governor juga tidak mengklaim satu model selalu terbaik. Rekomendasi bersifat capability-first dan harus berubah bersama produk.