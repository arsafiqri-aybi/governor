# 16 — Model update policy

Model router tidak boleh menjadi museum nama model.

## Registry fields

Untuk setiap model/surface simpan:
- model name;
- surface availability;
- plan/workspace availability;
- reasoning controls;
- strength description dari sumber resmi;
- usage/allowance note;
- last verified date;
- source URL.

## Update trigger

Perbarui registry bila:
- model picker berubah;
- model baru dirilis;
- model pensiun;
- reasoning levels berubah;
- Work/Codex availability berubah;
- usage economics berubah secara material.

## Routing stability

Workflow menggunakan capability classes (`FAST`, `BALANCED`, `DEEP`, `FRONTIER`) sehingga pergantian model hanya membutuhkan update registry, bukan menulis ulang seluruh skill.