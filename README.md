# Sistem_Pengelolaan_Kelas_Online (KelasKu)

KelasKu merupakan aplikasi berbasis Command Line Interface (CLI) yang dikembangkan menggunakan bahasa pemrograman Python untuk mengelola data kelas secara sederhana. Aplikasi ini memiliki sistem registrasi, login, pembagian hak akses pengguna, serta pengelolaan data kelas dengan penyimpanan menggunakan file JSON.

### Tujuan

Proyek ini bertujuan untuk menerapkan materi dasar pemrograman Python dalam sebuah aplikasi, meliputi penggunaan struktur data, fungsi, percabangan, perulangan, autentikasi pengguna, operasi CRUD, serta penyimpanan dan pembaruan data menggunakan JSON.

### Anggota Kelompok dan Pembagian Tugas

No.| Nama Anggota                                | Peran

1  | Fery Sugiantoro 2609116039                  | Sebagai Ketua,Koordinator,Pengembangan Program serta Mengisi Github

2  | Ahmad Raihan Sangkan Ladunni 2609116037     | pengembangan laporan, Penyusunan Laporan

3  | Nama Anggota 3                              | Penyusunan Laporan

4  | Bintang Dzikri Al Bukhari 2609116030        | Pembuatan Flowchart dan Revisi Github

# Fitur Aplikasi

## Admin
- Melihat daftar kelas.
- Menambahkan data kelas.
- Mengubah data kelas.
- Menghapus data kelas.
- Lihat semua akun.
- Riwayat pembelian.
- Riwayat topup.
- Riwayat refund.
- Semua riwayat.

## User
- Melihat daftar kelas.
- Top Up Saldo.
- Beli Kelas.
- Melihat Daftar Kelas Yang Sudah di Beli.
- Refund.

## Penyimpanan Data
- Data akun disimpan dalam file "akun.json".
- Data kelas disimpan dalam file "kelas.json".
- Data Invoice disimpan dalam file "invoice.json".
- Data aktivitas semua akun di simpan di "aktivitas.json"
- 
- Data diperbarui secara otomatis ketika terdapat perubahan melalui fitur yang tersedia.

## Teknologi dan Library
- Python — Bahasa pemrograman utama.
- JSON — Format penyimpanan data.
- PrettyTable — Menampilkan data kelas dalam bentuk tabel.
- pwinput — Menerima input kata sandi.
- os — Mendukung pembersihan layar terminal.
- time — Mengatur jeda waktu pada program.

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

Berikut ini adalah flowchart alur dimana jika login sebagai admin yang dimana bisa memilih menu Melihat kelas, Tambah akelas, Ubah kelas, Hapus kelas, Lihat semua akun, Riwaayat pembelian, Riwayat top up, riwayat refund, Semua riwayat.

# Output Program
## Menu Utama

<img width="561" height="240" alt="image" src="https://github.com/user-attachments/assets/02df237f-c9f2-4d8d-af54-d736a3308775" />


Menu utama menyediakan pilihan login,registrasi dan keluar dari aplikasi

## Registrasi dan Login

<img width="340" height="152" alt="Screenshot 2026-10-19 000631" src="https://github.com/user-attachments/assets/ad6b5a74-d263-4cb1-8fcf-18f59124279a" />

-

<img width="358" height="257" alt="Screenshot 2026-10-19 000656" src="https://github.com/user-attachments/assets/e281f3f0-c6a0-477e-aa12-438eef82551f" />

Pengguna dapat membuat akun baru dengan username yang unik,kemudian login menggunakan akun yang telah di daftarkan

## Menu admin dan Data kelas

<img width="565" height="341" alt="image" src="https://github.com/user-attachments/assets/95ca50a0-19a4-4c67-9a7a-5b3ab9778fb8" />


<img width="582" height="377" alt="image" src="https://github.com/user-attachments/assets/5098b026-d773-46d4-ac91-1ea4a5a9f1d9" />

Admin dapat melihat data kelas serta mengakses fitur tambah,ubah,dan hapus kelas

## Menu user

<img width="255" height="225" alt="image" src="https://github.com/user-attachments/assets/03d5e455-8308-49f0-b415-77f3f0352103" />

User dapat melihat daftar kelas dan keluar dari aplikasi

## Penyimpanan data

<img width="741" height="840" alt="image" src="https://github.com/user-attachments/assets/65ac2f7c-1c5f-422f-9686-d85d333c924e" />


<img width="741" height="840" alt="image" src="https://github.com/user-attachments/assets/2177e827-337c-43c2-9c6d-eae61b3aadcd" />

Data disimpan dalam format JSON sehingga dapat digunakan kembali ketika program dijalankan ulang

# Pengembangan Selanjutnya

Pengembangan berikutnya direncanakan mencakup fitur top up saldo, pembayaran kelas menggunakan saldo, pencetakan invoice, serta fitur tambahan lainnya sesuai persyaratan Project Akhir.

---

KelasKu — Sistem Pengelolaan Kelas Online
Project Akhir Praktikum Dasar Pemrograman Python.
