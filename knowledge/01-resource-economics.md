# 01 — Resource economics dan quality-per-resource

## Unit biaya yang relevan

Biaya AI bukan hanya jumlah token. Untuk proyek nyata, hitung:

- token/konteks input;
- panjang output;
- reasoning effort;
- model/surface allowance atau credit consumption;
- web/retrieval/tool calls;
- percobaan ulang;
- waktu verifikasi manusia;
- pekerjaan ulang akibat error.

Metrik operasional yang lebih baik daripada “murah per prompt” adalah:

`resource_cost_per_passed_result = total_resource_cost / number_of_outputs_passing_quality_gate`

Model murah yang sering gagal dapat lebih mahal daripada model kuat yang lulus sekali. Sebaliknya, model terkuat untuk transformasi sederhana adalah pemborosan.

## Marginal value test

Sebelum menambah resource, tanyakan:

1. Kegagalan apa yang sedang kita cegah?
2. Resource tambahan mana yang paling mungkin memperbaikinya?
3. Bisakah peningkatan tersebut diukur?
4. Jika output sudah lulus, apa alasan objektif untuk terus menambah effort?

Jika jawaban nomor 1 atau 2 tidak jelas, jangan otomatis naik kelas.