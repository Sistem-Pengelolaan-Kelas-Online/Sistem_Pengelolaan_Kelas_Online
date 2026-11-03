# Sistem_Pengelolaan_Kelas_Online (KelasKu)

KelasKu merupakan aplikasi berbasis Command Line Interface (CLI) yang dikembangkan menggunakan bahasa pemrograman Python untuk mengelola data kelas secara sederhana. Aplikasi ini memiliki sistem registrasi, login, pembagian hak akses pengguna, serta pengelolaan data kelas dengan penyimpanan menggunakan file JSON.

### Tujuan

Proyek ini bertujuan untuk menerapkan materi dasar pemrograman Python dalam sebuah aplikasi, meliputi penggunaan struktur data, fungsi, percabangan, perulangan, autentikasi pengguna, operasi CRUD, serta penyimpanan dan pembaruan data menggunakan JSON.

## Anggota Kelompok dan Pembagian Tugas

| No. | Nama Anggota                    | NIM        | Peran dan Tanggung Jawab                                      |
|-----|---------------------------------|------------|---------------------------------------------------------------|
| 1   | Fery Sugiantoro                 | 2609116039 | Sebagai Ketua, koordinator, pengembangan program, dan pengelolaan GitHub |
| 2   | Ahmad Raihan Sangkan Ladunni    | 2609116037 | Membantu pengembangan Program tahap awal dan penyusunan laporan  dan pengisian Github                          |
| 3   | Bintang Dzikri Al Bukhari       | 2609116030 | Pembuatan flowchart, pengembangan, pengisian, dan revisi GitHub |
| 4   | Anggitha Chrisiten Wulandari    | 2609116036 | Pengembangan, penyusunan laporan dan pengisian Github                          |

# Fitur Aplikasi

## Admin
- Melihat daftar kelas.
- Menambahkan kelas baru.
- Mengubah informasi kelas.
- Menghapus kelas.
- Melihat seluruh akun pengguna.
- Melihat riwayat pembelian.
- Melihat riwayat top up.
- Melihat riwayat refund.
- Melihat seluruh aktivitas pengguna.

## User
- Melakukan registrasi akun.
- Login ke dalam sistem.
- Melihat daftar kelas.
- Melakukan top up saldo menggunakan Rupiah.
- Membeli kelas menggunakan saldo C.
- Melihat kelas yang telah dibeli.
- Mengajukan refund dengan batas waktu 45 menit setelah pembelian.
- Melihat saldo akun.

## Sistem Transaksi

- Menggunakan saldo C sebagai alat pembayaran dalam program.
- Konversi saldo berdasarkan ketentuan Rp1.000 = 1 C.
- Batas minimum top up Rp1.000.
- Batas maksimum top up Rp100.000.000.
- Menyimpan riwayat pembelian, top up, dan refund.
- Mengembalikan saldo C apabila pengajuan refund berhasil dan memenuhi ketentuan.

## Penyimpanan Data
- Data akun disimpan dalam file "akun.json".
- Data kelas disimpan dalam file "kelas.json".
- Data Invoice disimpan dalam file "invoice.json".
- Data aktivitas disimpan dalam file "aktivitas.json"
- Data refund disimpan dalam file "refund.json"
- Data top up disimpan dalam file "topup.json"
- Data diperbarui secara otomatis ketika terdapat perubahan melalui fitur yang tersedia.

## Teknologi dan Library
- Python — Bahasa pemrograman utama.
- JSON — Format penyimpanan data.
- PrettyTable — Menampilkan data kelas dalam bentuk tabel.
- pwinput — Menerima input kata sandi.
- os — Mendukung pembersihan layar terminal.
- time — Mengatur jeda waktu pada program.
- random — Untuk menghasilkan angka random yang diunakan untuk refund kelas

# Cara Menjalankan Program

## User
1. Masuk ke akun user
2. Pilih menu yang ingin di pilh 

## Admin
1. Masuk ke menu admin
2. Pilih menu admin yang inginn di pilih 

# Flowchart

## Halaman Login
<img width="1427" height="934" alt="Halaman Login drawio" src="https://github.com/user-attachments/assets/f6f6ada9-f032-48be-b35a-15eabedc5579" />

Berikut ini adalah flowchart alur dimana saat program ini di buka langsung menampilkan menu dimana terdapat Login, Registrasi, Keluar dari program.

## Halaman User(murid)
<img width="2521" height="2466" alt="halaman user drawio (5)" src="https://github.com/user-attachments/assets/fa0db961-5ef1-47f7-8d0c-4b417e230c6f" />


Berikut ini adalah flowchart alur dimana jika login sebagai user(murid) yang ada alur dimana user(murid) bisa memilih Melihat Daftar Kelas, Top Up Saldo, Beli Kelas, Melihat Kelas Yang Di Beli, Logout.

## Halamann Admin
<img width="3436" height="1652" alt="halaman admin drawio (5)" src="https://github.com/user-attachments/assets/e6307893-489c-4766-851e-654c459e6673" />

Berikut ini adalah flowchart alur dimana jika login sebagai admin yang dimana bisa memilih menu Melihat kelas, Tambah akelas, Ubah kelas, Hapus kelas, Lihat semua akun, Riwaayat pembelian, Riwayat top up, Riwayat refund, Semua riwayat.

# Output Program
## Menu Utama

<img width="561" height="240" alt="image" src="https://github.com/user-attachments/assets/02df237f-c9f2-4d8d-af54-d736a3308775" />

Menu utama menyediakan pilihan login, registrasi dan keluar dari aplikasi.

## Registrasi dan Login

<img width="340" height="152" alt="Screenshot 2026-10-19 000631" src="https://github.com/user-attachments/assets/ad6b5a74-d263-4cb1-8fcf-18f59124279a" />

-

<img width="358" height="257" alt="Screenshot 2026-10-19 000656" src="https://github.com/user-attachments/assets/e281f3f0-c6a0-477e-aa12-438eef82551f" />

Pengguna dapat membuat akun baru dengan username dan password, kemudian login menggunakan akun yang telah di daftarkan.

## Menu Admin
<img width="298" height="272" alt="Screenshot 2026-11-03 193306" src="https://github.com/user-attachments/assets/f9d81d3e-005e-496f-8a53-23cc54a7e0f0" />

Disini pengguna(admin) dapat melihat menu yang dapat digunakan untuk mengatur di program ini.

## 1. Melihat Kelas
<img width="692" height="267" alt="Screenshot 2026-11-03 193328" src="https://github.com/user-attachments/assets/36006780-bed4-43a1-85d8-b339b5d06e04" />

Disini admin dapat melihat semua kelas yang tersedia untuk user.

## 2. Menambahkan Kelas
<img width="397" height="153" alt="Screenshot 2026-11-03 193534" src="https://github.com/user-attachments/assets/5bfb0a37-025f-4037-9093-c0103f00e7ff" />

Disini admin dapat menambahkan pelajaran baru sekaligus pengajar pelajaran untuk user.

## 3. Mengubah Kelas
<img width="710" height="422" alt="WhatsApp Image 2026-11-03 at 19 12 24" src="https://github.com/user-attachments/assets/18bc9fa9-67e3-4de0-b496-f68aecc32cb4" />

Disini admin dapat mengubah kelas dengan memasuan id kelas, nama kelas, pengajar pengganti, dan harga.

## 4. Hapus Kelas
<img width="685" height="358" alt="Screenshot 2026-11-03 193616" src="https://github.com/user-attachments/assets/27befed6-3ef5-44e9-9321-a59a0c7661d4" />

Disini admin dapat menghapus kelas.

## 5. Tampilkan Semua Akun
<img width="402" height="311" alt="Screenshot 2026-11-03 193635" src="https://github.com/user-attachments/assets/3702e4b9-53b7-40e4-8a06-e6807a0f2777" />

Disini admin dapat melihat akun yang sudah terregistrasi dari pengguna.

## 6. Riwayat Pembelian 
<img width="997" height="300" alt="Screenshot 2026-11-03 193659" src="https://github.com/user-attachments/assets/dcac0948-5caa-4cc5-9c1c-0ba6dacf5c46" />

Disini admin dapat melihat seluruh riwayat pembelian yang telah dilakukan oleh user.

## 7. Riwayat Top Up
<img width="757" height="200" alt="Screenshot 2026-11-03 193725" src="https://github.com/user-attachments/assets/64325b61-f2e9-4473-adeb-b54f018375ab" />

Disini admin dapat melihat seluruh riwayat Top Up yang telah dilakukan oleh user.

## 8. Riwayat Refund
<img width="1338" height="198" alt="Screenshot 2026-11-03 193808" src="https://github.com/user-attachments/assets/3b4b516e-b564-4316-b70b-263ac0b84bad" />

Disini admin dapat melihat seluruh riwayat refund yang telah dilakukan oleh user.

## 9. Semua Riwayat
<img width="783" height="702" alt="Screenshot 2026-11-03 193835" src="https://github.com/user-attachments/assets/804c7818-ef82-48bf-beff-ec8d5de36c59" />

Disini admin dapat melihat seluruh riwayat yang telah dilakukan oleh user baik membeli kelas, top up, refund.

## Menu User 
<img width="291" height="215" alt="Screenshot 2026-11-03 194013" src="https://github.com/user-attachments/assets/24869b6a-b765-4819-82b2-cbba7b1b7317" />

Disini user dapat melihat menu yang dapat digunakan di program ini, dan tampilan ini user sudah termasuk menampilkan username dan saldo yang dimiliki oleh pengguna.

## 1. Lihat daftar Kelas
<img width="688" height="271" alt="Screenshot 2026-11-03 194032" src="https://github.com/user-attachments/assets/adeddf78-5f22-4d72-9286-3b401a1cfd6e" />

Disini user dapat melihat kelas yang dapat dibeli.

## 2 Top Up
<img width="395" height="270" alt="Screenshot 2026-11-03 194324" src="https://github.com/user-attachments/assets/d0d2118c-330f-46f1-b53c-734ad6701ded" />

Disini user top up dari tunai ke coin.

## 3 Beli Kelas
<img width="687" height="607" alt="Screenshot 2026-11-03 194502" src="https://github.com/user-attachments/assets/cdd320ba-1697-4f07-bef9-d6e5abb83288" />

Disini user dapat membeli kelas yang tersedia dengan saldo yang cukup.

## 4. Kelas yang Dapat Dapat di Akses
<img width="423" height="426" alt="Screenshot 2026-11-03 194523" src="https://github.com/user-attachments/assets/88aa2c25-a555-4ffc-ad5a-dcdf15f73182" />

Disini user dapat melihat kelas yang sudah di beli atau di akses untuk di pelajari.

## 5. Refund Kelas 
<img width="516" height="402" alt="Screenshot 2026-11-03 194825" src="https://github.com/user-attachments/assets/1f221f36-9025-47a6-880f-ca9c4be0c6f1" />

Disini user dapat mmelakukan refund untuk proses pengembalian dana karena merasa tidak cocok pada pelajaran tersebut. dan di refund sini ada batasan waktunya jika lebih dari 45 menit makan proses refund tidak akan bisa di ajukan.



---

KelasKu — Sistem Pengelolaan Kelas Online
Project Akhir Praktikum Dasar Pemrograman Python.
