# 18 — Integrasi dengan Prompting Skill dan skill lain

## Urutan tanggung jawab

**Governor** — menentukan resource dan workflow.

**Prompting Skill** — merancang instruction/context/evidence/output agar hasil AI maksimal.

**Skill Builder** — merancang dan mengevaluasi skill reusable.

**Domain skill** — memberi pengetahuan/prosedur spesifik seperti website, finance, desain, atau riset.

## Integration contract

Governor tidak boleh menimpa constraint kualitas dari Prompting Skill atau domain skill. Ia hanya boleh:
- memilih subset konteks;
- memilih surface/model/effort;
- menentukan stage split/handoff;
- menentukan tool dan escalation;
- menghentikan iterasi ketika gate sudah lulus.

Jika penghematan membuat domain quality gate gagal, penghematan tersebut dibatalkan.

## Progressive loading

Muat Governor kernel terlebih dahulu. Setelah routing selesai, muat hanya modul Prompting Skill/domain yang dibutuhkan oleh tahap saat ini. Ini mencegah semua skill dimasukkan sekaligus ke konteks aktif.