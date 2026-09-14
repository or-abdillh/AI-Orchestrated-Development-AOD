# AOD Document Versioning Standard — Always Active

> Aturan wajib untuk setiap dokumen yang dihasilkan atau dimodifikasi oleh AI di dalam framework AOD.
> Berlaku untuk semua artefak di direktori `docs/` (`docs/business/`, `docs/system-design/`, `docs/ui-architecture/`, `docs/development/`, `docs/testing/`, `docs/proposal/`).

---

## 📌 Standard Header Requirement

Setiap dokumen Markdown yang dibuat atau di-generate oleh AI **WAJIB** menyertakan blok metadata versioning di bagian paling atas (setelah judul H1):

```markdown
# [Document Title]

> **Version:** `v1.0.0`  
> **Last Updated:** `YYYY-MM-DD`  
> **Status:** `Draft` | `In Review` | `Approved` | `Superseded`  
> **Author / Generator:** [AI Skill Name, misal: aod-prd]

---

### Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| `v1.0.0` | YYYY-MM-DD | aod-prd | Initial generation based on Study Case and BRD. |
```

---

## 🔢 Semantic Versioning Rules for Documents

AI wajib menggunakan format `vMAJOR.MINOR.PATCH` dengan ketentuan penomoran sebagai berikut:

### 1. MAJOR Version (`vX.0.0`)
Dinaikkan jika terjadi perubahan mendasar, *breaking changes*, atau perombakan struktural:
- Perubahan arsitektur sistem atau pergantian paradigma (misal: perubahan tech stack utama).
- Restrukturisasi alur bisnis inti yang membatalkan sebagian besar flow sebelumnya.
- Penghapusan atau perombakan menyeluruh pada modul/entitas database inti.
- Rekonsep total produk atau UI design system.

### 2. MINOR Version (`v1.X.0`)
Dinaikkan jika terdapat penambahan atau modifikasi substansial yang bersifat *backward-compatible*:
- Penambahan modul, fitur baru, atau use-case baru pada PRD.
- Penambahan entitas baru atau relasi baru pada Data Dictionary / DBML.
- Penambahan endpoint baru pada API Contract atau halaman baru pada UI Flow.
- Penambahan sprint/fase baru pada Phase Plan.
- Penambahan skenario uji baru pada UAT Sheet.

### 3. PATCH Version (`v1.0.X`)
Dinaikkan jika terjadi perubahan kecil, klarifikasi, atau perbaikan:
- Perbaikan typo, kesalahan tata bahasa, atau pemformatan markdown.
- Klarifikasi deskripsi field atau penyesuaian catatan implementasi.
- Perbaikan minor pada penamaan komponen atau styling tokens tanpa mengubah token inti.
- Penyesuaian kecil pada checklist DoD.

---

## 🔄 AI Document Update Protocol

Setiap kali pengguna meminta AI untuk **mengedit, merevisi, menambah, atau memperbarui** dokumen yang sudah ada:

1. **Periksa Header Saat Ini:** Baca versi terakhir dan tanggal `Last Updated` dari dokumen.
2. **Evaluasi Dampak Perubahan:** Tentukan apakah perubahan tergolong **Major**, **Minor**, atau **Patch**.
3. **Naikkan Versi (Version Bump):**
   - Major: `v1.2.3` ➔ `v2.0.0`
   - Minor: `v1.2.3` ➔ `v1.3.0`
   - Patch: `v1.2.3` ➔ `v1.2.4`
4. **Perbarui Timestamp:** Update field `Last Updated` dengan tanggal saat ini (`YYYY-MM-DD`).
5. **Catat Log Perubahan:** Tambahkan baris baru di tabel `Revision History` yang merangkum poin-poin yang diubah.
6. **Larangan Keras:** Dilarang mengedit isi dokumen tanpa memperbarui versi, tanggal, dan riwayat revisi!
