# AOD Feedback & Revision Protocol — Always Active

> Aturan wajib untuk menangani dokumen feedback, catatan revisi klien, atau Change Request (CR) yang ditaruh di dalam `docs/feedback/` atau `docs/revisions/`.
> AI harus mengikuti protokol ini secara disiplin untuk mencegah perubahan kode liar (*rogue coding*), pergeseran arsitektur yang tidak terkontrol (*architecture drift*), atau manipulasi file tanpa audit jejak rekam (*audit trail*).

---

## 🛑 1. Mandatory Planning Mode & Clarification Gate

1. **Dilarang Eksekusi Langsung:** Saat pengguna atau klien memberikan dokumen feedback/revisi, AI **DILARANG KERAS** langsung memodifikasi dokumen atau kode aplikasi secara sepihak.
2. **Wajib Beroperasi dalam Mode PLAN:** AI wajib mengawali dengan membaca seluruh isi dokumen feedback, membedah setiap butir permintaan, dan menyusun **Audit & Proposed Action Plan**.
3. **Pintu Klarifikasi (Clarification Gate):** Sebelum melakukan perubahan apa pun, AI **WAJIB** menyajikan rencana aksi tersebut kepada pengguna dan secara aktif meminta konfirmasi:
   - Klarifikasi atas butir permintaan yang ambigu atau memiliki multi-tafsir.
   - Konfirmasi klasifikasi scope (Scope A, B, atau C) untuk setiap butir.
   - Peringatan atas potensi *breaking changes* atau implikasi teknis yang signifikan.
4. **Tunggu Persetujuan Eksplisit:** Eksekusi hanya boleh dimulai setelah pengguna memberikan persetujuan atau konfirmasi atas rencana yang diajukan.

---

## 🎯 2. Klasifikasi Scope Dampak (3-Tier Scope Classification)

Setiap butir feedback/revisi wajib dikategorikan ke dalam salah satu dari 3 level berikut:

### Scope A: Documentation Only (Perubahan Dokumen Murni)
- **Karakteristik:** Perbaikan typo, klarifikasi use-case, penyesuaian SLA, alignment terminologi bisnis, atau pembaruan visual flow tanpa mengubah logika/kode aplikasi.
- **Tindakan AI:**
  1. Perbarui dokumen bersangkutan di folder `docs/`.
  2. Naikkan versi dokumen: **SemVer Patch (`v1.0.X`)** untuk koreksi kecil atau **Minor (`v1.X.0`)** untuk penambahan seksi dokumen baru.
  3. Perbarui field `Last Updated` dan tambahkan catatan ke tabel `Revision History`.
  4. *Tidak ada branch kode atau perubahan file source code.*

### Scope B: Existing Feature Modification (Penyesuaian Fitur yang Sudah Ada)
- **Karakteristik:** Perubahan aturan validasi, penyesuaian logika kalkulasi, perubahan syarat transisi status pada State Machine, modifikasi layout/komponen UI yang sudah ada, atau perbaikan bug fungsional.
- **Tindakan AI:**
  1. **Upstream-First:** Perbarui dokumen hulu terlebih dahulu (PRD, State Machine, API Contract, atau UI Style) dan naikkan versinya (**SemVer Minor/Patch**).
  2. **Isolasi Git Branch:** Buat atau beralih ke branch khusus: `feat/<module>-<slug>` atau `fix/<module>-<slug>`. Dilarang bekerja di `main`/`master`.
  3. **Implementasi Kode:** Modifikasi kode fitur sesuai dokumen hulu yang telah diperbarui.
  4. **Verifikasi Kualitas:** Validasi kepatuhan terhadap checklist `aod-dod`.
  5. **Commit:** Eksekusi commit atomik menggunakan `smart-git-commit`.

### Scope C: New Feature / Scope Expansion (Fitur Baru atau Perombakan Besar)
- **Karakteristik:** Penambahan modul baru, metode pembayaran baru, alur approval multi-tier baru, penambahan role baru, perubahan skema database besar, atau integrasi pihak ketiga baru.
- **Tindakan AI:**
  1. **Upstream Cascading:** Perbarui seluruh dokumen AOD secara berurutan:
     - PRD (`docs/business/PRD.md`) ➔ Tambah functional requirements baru (**SemVer Minor/Major**).
     - RBAC (`docs/business/RBAC.md`) & Data Dictionary (`docs/business/DATA_DICTIONARY.md`) ➔ Tambah permissions, tabel, atau kolom baru.
     - DBML (`docs/business/SCHEMA.dbml`) ➔ Perbarui skema ERD.
     - API Contract & UI Flow ➔ Tambah endpoint dan screen baru.
     - Tech Spec & Phase Plan ➔ Alokasikan ke fase implementasi / sprint baru.
  2. **Prompt Template Baru:** Hasilkan feature prompt baru di `docs/development/FEATURE_PROMPTS.md`.
  3. **Isolasi Git Branch:** Buat branch fitur baru: `feat/<module>-<feature-slug>`.
  4. **Eksekusi Koding & UAT:** Jalankan implementasi, validasi DoD, dan tambahkan skenario uji ke `docs/testing/UAT_SHEET.md`.

---

## ⚓ 3. Prinsip Hulu-ke-Hilir (Upstream-First Rule)

- Sumber kebenaran sistem terletak pada dokumen arsitektur, bukan pada hafalan kode.
- Jika ada permintaan revisi pada kode, **DOKUMEN SPESIFIKASINYA HARUS DIPERBARUI LEBIH DULU**.
- Dilarang membuat migration baru tanpa mencatatnya di `DATA_DICTIONARY.md`.
- Dilarang membuat endpoint baru tanpa mendefinisikannya di `API_CONTRACT.md`.
- Dilarang menambahkan state status baru tanpa memetakannya di `STATE_MACHINE.md`.

---

## 📊 4. Kewajiban Laporan Akhir (Mandatory Final Report)

Setelah seluruh butir feedback selesai dieksekusi dan diverifikasi, AI **WAJIB** menyusun dokumen laporan akhir:

- **Lokasi File:** `docs/feedback/FINAL_REPORT_<nama_dokumen_feedback>.md` (atau `docs/revisions/...`).
- **Komponen Wajib Laporan Akhir:**
  1. **Executive Summary:** Ringkasan hasil penanganan feedback dan status akhir.
  2. **Scope Breakdown:** Tabel butir feedback beserta klasifikasi scope (Scope A / B / C).
  3. **Document Audit Table:** Daftar dokumen yang diperbarui, versi lama vs versi baru (SemVer), dan tanggal pembaruan.
  4. **Git & Code Audit:** Nama branch yang digunakan, commit hash, dan daftar file kode yang dimodifikasi / dibuat.
  5. **DoD & Verification Check:** Bukti verifikasi fungsional dan kepatuhan Definition of Done.
  6. **Next Recommendations:** Tindakan lanjutan yang disarankan untuk menjaga kesehatan proyek.
