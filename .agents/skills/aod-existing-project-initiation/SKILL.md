---
name: aod-existing-project-initiation
description: >-
  Screens an existing software repository before AOD adoption. Detects its tech
  stack, maps implemented domains and features from code evidence, audits current
  documentation and Agent Reference Context, then asks the user which evidence-
  based AOD documents to create. Use when the user wants to initiate, onboard,
  document, or build a development phase plan for an existing codebase.
---

# AOD Existing Project Initiation

Kamu membantu user mengadopsi AOD pada codebase yang sudah berjalan. Mulailah
dengan membaca kondisi repository. Perlakukan implementasi saat ini sebagai
baseline *as-is*; jangan memaksakan urutan scaffolding proyek baru.

Skill ini melakukan audit dan dokumentasi saja. Jangan mengubah kode aplikasi,
menjalankan migrasi, memasang dependency, atau membuat dokumen pilihan sebelum
user memilihnya.

## Hasil yang Dituju

1. Tech stack dan struktur aplikasi teridentifikasi dari bukti repository.
2. Domain, modul, fitur, integrasi, dan tingkat keyakinan pemetaan disajikan.
3. Gap, duplikasi, ketergantungan, serta konflik dokumen dan implementasi dicatat.
4. User menerima laporan screening di chat dan memilih dokumen AOD yang ingin
   dibuat berdasarkan temuan tersebut.
5. Dokumen terpilih menggambarkan sistem yang berjalan dan rencana pengembangan
   yang masih diperlukan. ARC mencatat konteks existing secara dapat ditelusuri.

## Aturan Screening

- Gunakan repository sebagai sumber kondisi teknis *as-is*. Gunakan dokumen yang
  ada sebagai bukti intent terdokumentasi, bukan bukti otomatis bahwa perilaku
  itu sudah diterapkan.
- Bedakan **Teramati** (didukung file, route, schema, test, atau konfigurasi),
  **Inferensi** (kesimpulan dari beberapa bukti), dan **Belum diketahui**.
- Jika kode, test, dan dokumen saling bertentangan, catat masing-masing bukti.
  Jangan memilih perilaku target secara sepihak. Tanyakan intent user sebelum
  menuliskannya sebagai spesifikasi.
- Jangan mengarang nama modul, fitur, API, aturan bisnis, versi package, status
  deployment, kualitas test, branch, commit, maupun bukti kelulusan.
- Jangan membuka atau menyalin nilai rahasia dari `.env`, credential, private
  key, token, dump data produksi, atau file sejenis. Catat hanya nama file atau
  keberadaan konfigurasi jika relevan.
- Pindai semua area aplikasi yang relevan, tetapi lewati dependency terpasang,
  cache, build output, binary, vendor, dan generated files kecuali diperlukan
  untuk menjawab pertanyaan spesifik. Catat area yang dilewati jika membatasi
  cakupan kesimpulan.
- Hindari menjalankan aplikasi, skrip proyek, migrasi, formatter, generator,
  install command, atau test suite selama screening awal. Pemeriksaan awal harus
  read-only. Minta izin terpisah jika tindakan berikutnya memerlukannya.
- Gunakan Context7 untuk dokumentasi resmi hanya bila tugas terpilih memerlukan
  verifikasi detail API, konfigurasi, atau perilaku library. Deteksi stack dari
  repository tidak memerlukan Context7.

## Alur Kerja

### 1. Kenali Repository dan Batas Audit

- Periksa instruksi agent lokal, struktur tingkat atas, status Git, dan dokumen
  AOD atau spesifikasi yang sudah tersedia.
- Kenali monorepo, beberapa aplikasi, package/workspace, service, dan area kode
  yang dikecualikan. Jangan menyamakan package dengan domain bisnis.
- Jangan menanyakan lokasi, framework, atau dokumen sebelum memeriksa repository.
  Ajukan pertanyaan hanya untuk ambiguitas yang tidak dapat dipastikan dari bukti.

### 2. Deteksi Tech Stack Terlebih Dahulu

Sebelum memetakan domain, identifikasi setiap aplikasi atau service dan catat
bukti yang mendukungnya. Periksa sesuai indikasi repository:

- Manifest dan lockfile untuk bahasa, runtime, framework, ORM, dependency, dan
  versinya.
- Build, workspace, compiler, dan konfigurasi untuk struktur monorepo serta
  pembagian frontend/backend.
- Konfigurasi koneksi dan migration untuk database serta tool schema.
- Routing, middleware, dependency injection, dan konfigurasi auth untuk pola
  aplikasi yang nyata.
- Container, CI workflow, dan konfigurasi deploy untuk toolchain/deployment yang
  dinyatakan repository. Jangan menyimpulkan kondisi production hanya dari file.
- Styling dan UI framework bila ada antarmuka.

Laporkan versi persis hanya jika manifest/lockfile menyediakannya. Jika versi
berbeda antar service, tampilkan per service. Tandai komponen yang tidak dapat
dipastikan sebagai belum diketahui; jangan mengisi kekosongan dengan tebakan.

### 3. Petakan Domain dan Fitur yang Berjalan

Lakukan penelusuran lintas repository, bukan hanya membaca README atau beberapa
folder pertama. Ikuti bukti yang tersedia dan relevan:

- struktur package/module, entry point, route/handler, halaman, dan navigasi;
- model/entity, schema, migration, query, event, job, dan alur data;
- service/use case, policy/guard, validasi, integrasi eksternal, dan konfigurasi;
- test unit/integrasi/E2E yang ada serta fixture/mock terkait;
- docs, changelog, issue/ADR yang tersedia, dan Git history bila membantu.

Kelompokkan hasil ke Domain → Modul → Submodul → Fitur/use case. Untuk setiap
fitur, sertakan bukti path/simbol yang representatif, interface penting bila
terlihat, dependency, dan tingkat keyakinan. Sebut sebagai "terimplementasi"
hanya jika alur implementasinya terlihat; keberadaan route atau tombol saja
tidak membuktikan alur lengkap. Catat test yang ditemukan, tetapi jangan klaim
test lulus kecuali memang dijalankan secara terpisah dan hasilnya tersedia.

### 4. Audit Kesiapan dan Kesenjangan Dokumen

Periksa artefak AOD maupun dokumen lain yang sudah ada. Kelompokkan statusnya:
ada dan relevan, ada tetapi stale/tidak lengkap, belum ada, atau bertentangan.
Nilai pula apakah tersedia cukup bukti untuk memperbarui atau membuat:

- **Development:** Tech Spec, Architecture Engineering Rules, Phase Plan,
  Feature Prompts, DoD, dan Progress Report.
- **Business yang dapat diturunkan:** domain glossary/CONTEXT, Business Flow
  *as-is*, Data Dictionary *as-is*, RBAC yang teramati, dan state lifecycle.
- **Interface dan UI bila relevan:** API Contract *as-is*, UI Flow, UI references,
  atau design documentation berbasis tampilan yang ada.
- **ARC:** feature reference untuk modul/use case yang dipetakan dan Master
  Reference Registry.

Gunakan lokasi standar berikut saat menawarkan pilihan: `TECH_SPEC.md`,
`PHASE_PLAN.md`, `FEATURE_PROMPTS.md`, `DOD.md`, dan `PROGRESS_REPORT.md` di
`docs/development/`; `BUSINESS_FLOW.md`, `DATA_DICTIONARY.md`, `RBAC.md`, dan
`PRD.md` di `docs/business/`; `STATE_MACHINE.md` dan `API_CONTRACT.md` di
`docs/system-design/`; serta feature references di
`docs/references/features/REF-FEAT-<module>-<slug>.md` dengan registry
`docs/references/INDEX.md`. Tawarkan UI references di `docs/references/ui/`
hanya jika audit menemukan halaman atau komponen antarmuka. Tawarkan DoD,
Feature Prompts, atau Progress Report hanya jika kebutuhan/masukan yang
diperlukan tersedia atau dapat ditandai sebagai gap.

Jangan menawarkan dokumen target/to-be sebagai fakta hasil reverse engineering.
Untuk PRD, BRD, roadmap produk, flow masa depan, atau keputusan bisnis yang tidak
bisa disimpulkan dari implementasi, jelaskan pertanyaan bisnis yang masih perlu
dijawab user. Tawarkan sebagai draft berbasis bukti plus bagian terbuka hanya
jika user bersedia memberikan/menyetujui intent yang hilang.

### 5. Bangun Laporan Screening di Chat

Tampilkan laporan tanpa membuat atau mengubah file. Sertakan:

1. Cakupan audit dan keterbatasan yang ditemukan.
2. Tabel stack per aplikasi/service, versi, serta bukti sumber.
3. Peta domain/modul/fitur dengan tingkat keyakinan dan bukti singkat.
4. Integrasi, alur data/dependensi utama, test yang tersedia, dan temuan
   arsitektur yang benar-benar didukung bukti.
5. Dokumen yang sudah ada, gap dokumentasi, konflik, dan pertanyaan intent.
6. Menu dokumen yang dapat dibuat. Untuk tiap opsi sebut tujuan, dasar bukti,
   batas yang tidak dapat disimpulkan, dan lokasi output yang disarankan.

Jangan menghasilkan dokumen pada langkah ini. Lalu minta user memilih satu atau
beberapa dokumen, urutan bila ada dependency, dan menjawab pertanyaan bisnis yang
memblokir dokumen pilihannya. Rekomendasikan urutan paling kecil yang masuk akal
berdasarkan repository, tanpa memaksa seluruh rantai Phase 1 sampai 5.

### 6. Buat Hanya Dokumen yang Dipilih

Setelah user memilih:

- Konfirmasi pilihan dan pertanyaan yang belum terjawab secara ringkas. Jangan
  meminta konfirmasi ulang untuk detail yang sudah dipilih user.
- Ikuti skill AOD khusus untuk dokumen terpilih jika prasyaratnya tersedia.
  Untuk dokumen *as-is*, perlakukan bukti repository sebagai bahan audit dan
  jelaskan penyesuaian konteks existing. Jangan menolak pemetaan kondisi aktual
  hanya karena PRD atau dokumen scaffolding belum ada.
- Jika prasyarat skill khusus belum tersedia dan belum ada mode existing-project,
  gunakan format output dokumen tersebut untuk menghasilkan draft *as-is* dari
  bukti screening. Tandai bagian yang belum diketahui sebagai gap; jangan
  mengarang konten hanya untuk mengisi template.
- Jika dokumen pilihan saling bergantung, hasilkan upstream yang dipilih lebih
  dulu, lalu gunakan hasilnya untuk dokumen turunan.
- Pertahankan file dokumen yang sudah ada. Sebelum mengubahnya, baca isi, bump
  SemVer, tanggal, status, dan Revision History sesuai aturan AOD.
- Jangan membuat dokumen yang tidak dipilih. User dapat memilih semua opsi yang
  ditawarkan, tetapi pilihan harus eksplisit.
- Batasi klaim pada bukti repository dan jawaban user. Labeli asumsi, inferensi,
  keputusan yang menunggu, dan kontradiksi secara jelas.

## Phase Plan untuk Sistem yang Sudah Berjalan

Phase Plan hasil pilihan harus menjadi rencana dari baseline saat ini, bukan
pengulangan urutan bootstrap standar:

- Mulai dengan ringkasan baseline: stack, layanan, domain aktif, dan fitur
  existing yang menjadi fondasi.
- Pisahkan pekerjaan baru dari pekerjaan yang sudah berjalan. Tandai status
  existing sebagai *implemented/evidence observed*, *partial*, *unknown*, atau
  *planned*; jangan masukkan fitur selesai sebagai pekerjaan baru.
- Susun fase tersisa menurut dependensi teknis, prioritas bisnis yang diberikan
  user, risiko, dan kesiapan. Jika prioritas belum tersedia, tandai belum
  diputuskan dan tawarkan opsi pengurutan.
- Masukkan dokumentasi, pengurangan risiko, migrasi, testing, hardening, atau
  pengembangan fitur hanya bila didukung temuan atau dipilih user.
- Untuk setiap fase, catat objective, item yang dapat ditelusuri ke temuan atau
  keputusan user, prasyarat, deliverable, validasi, dan kondisi selesai.
- Gunakan target branch hanya bila diminta atau sesuai workflow repository.
  Jangan mengarang branch historis atau menyatakan branch sebagai bukti progres.

## Agent Reference Context untuk Modul Existing

Saat user memilih dokumentasi ARC, periksa `docs/references/INDEX.md` dan baca
referensi relevan sebelum memperbarui. Jika belum ada, gunakan
`docs/samples/MASTER_REFERENCE_INDEX_TEMPLATE.md`. Buat atau perbarui
`REF-FEAT-<module>-<slug>.md` dengan template
`docs/samples/FEATURE_REFERENCE_TEMPLATE.md` sebagai dasar, lalu sesuaikan
bagian template yang tidak memiliki bukti.

Untuk tiap referensi existing:

- Catat manifest file yang ditemukan, tanggung jawab yang dapat diamati, route
  atau event entry point, dan relasi dengan modul lain.
- Dokumentasikan lifecycle request/data hanya sejauh dapat ditelusuri. Tandai
  langkah yang belum ditemukan atau tidak diverifikasi.
- Pisahkan business invariant yang eksplisit di kode/test/dokumen dari dugaan.
  Jangan mengubah dugaan menjadi aturan domain.
- Petakan kontrak API, skema, state, otorisasi, dan test hanya bila bukti ada;
  tandai kontrak yang tidak terdokumentasi sebagai gap.
- Status referensi harus mencerminkan dokumentasi audit, bukan menyatakan fitur
  pasti selesai atau test passing. Jangan mengarang branch atau commit.
- Tambahkan cabang domain/modul dan registry entry ke `INDEX.md`. Tandai entri
  sebagai audit atas fitur existing dan sertakan link ke referensi.
- Perbarui versi, tanggal, dan Revision History pada dokumen registry yang
  diubah.

## Output Default dan Penutup

Screening awal selalu ditampilkan di chat. Setelah user memilih dokumen, simpan
hasil yang dipilih pada lokasi standar `docs/` yang sesuai dan patuhi aturan
versioning. Pada ringkasan akhir, sebutkan dokumen yang dibuat, pertanyaan/gap
yang masih terbuka, dan bukti verifikasi yang tersedia.
