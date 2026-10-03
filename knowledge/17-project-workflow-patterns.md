# 17 — Project workflow patterns

## A. Website besar

1. **Problem framing / requirements:** Chat Medium/High.
2. **Research UX/market/current standards:** Chat High atau Work dengan web/files.
3. **Information architecture / design system decisions:** High; frontier hanya jika banyak constraint/cross-domain.
4. **Implementation repo:** Codex; mulai model balanced/deep sesuai kompleksitas, Astra untuk hard architecture/refactor/debug jika perlu.
5. **Routine page/component generation:** worker tier lebih hemat + tests/lint.
6. **Visual/accessibility/performance QA:** tools + strong reviewer untuk issue kompleks.
7. **Final integration:** synthesizer/deep model membaca state final, bukan seluruh chat history.

## B. Deep research

Frame pertanyaan → retrieval sumber primer → extraction worker → synthesis High → contradiction audit → final evidence check. Naik model tidak menggantikan sumber.

## C. Skill Builder

Define behavior → map knowledge → architecture → compact active kernel → modular references → regression benchmark → package/install. Gunakan model kuat untuk architecture dan eval design; gunakan worker ringan untuk formatting/metadata yang deterministik.

## D. Coding project

Architecture in Chat/Work High bila perlu → implementation di Codex → tests → targeted escalation untuk failing modules → final review. Jangan menjalankan Astra pada semua file jika perubahan mekanis dapat dilakukan oleh tier lebih hemat dan test dapat menangkap kesalahan.