# STUDY CASE DOCUMENT

## 1. Company Overview

[Deskripsi bisnis secara objektif]

## 2. Operational Context

- Jumlah cabang:
- Jumlah karyawan:
- Rata-rata transaksi per hari:
- Struktur organisasi:

## 3. Current Process

Saat ini proses berjalan seperti berikut:

1. Sales menerima pesanan melalui WhatsApp.

2. Sales mencatat pesanan di Excel.

3. Sales mengirim file Excel ke Finance via email.

4. Finance memverifikasi pembayaran.

5. Jika valid, Finance mengirim konfirmasi ke Warehouse.

6. Warehouse mengirim barang.

## 4. Pain Points

- File Excel sering tertimpa.
- Tidak ada tracking status.
- Approval lambat.
- Tidak ada audit trail.

## 5. Actors & Responsibilities

### 5.1. Sales

- Membuat pesanan
- Berinteraksi dengan customer

### 5.2. Finance

- Verifikasi pembayaran
- Approve pesanan

### 5.3. Warehouse

- Mengirim barang

## 6. Business Rules

1. Order tidak boleh dikirim sebelum pembayaran diverifikasi.

2. Sales hanya bisa mengedit order sebelum disubmit.

3. Finance hanya bisa approve order yang statusnya submitted.

4. Order yang sudah approved tidak boleh diubah.

5. Semua aktivitas harus tercatat.

## 7. Exception Scenarios

- Customer membatalkan setelah submit.
- Pembayaran tidak valid.
- Barang tidak tersedia.
- Finance salah approve.

## 8. Constraints

- Sistem berbasis web.
- Tidak ada mobile app.
- Maksimal 200 concurrent user.
- Menggunakan Laravel + MySQL.
- Data harus tersimpan minimal 5 tahun.

## 9. Expected Outcomes

- Status order dapat dipantau real-time.
- Approval maksimal 1 hari.
- Tidak ada kehilangan data.
- Semua aktivitas terekam log.

## 10. Non-Functional Expectations

- Response time < 2 detik.
- Role-based access control.
- Audit trail wajib.
- Data tidak boleh bisa dihapus permanen (soft delete).
