import json
import os
import time
import random
import pwinput
from prettytable import PrettyTable

FILE_AKUN = "akun.json"
FILE_KELAS = "kelas.json"
FILE_INVOICE = "invoice.json"
FILE_TOPUP = "topup.json"
FILE_REFUND = "refund.json"
FILE_AKTIVITAS = "aktivitas.json"

KURS_C = 1000
MIN_TOPUP = 1000
MAX_TOPUP = 100_000_000
BATAS_REFUND = 45 * 60


# ==================== JSON DAN UTILITAS ====================

def simpan_json(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def baca_json(nama_file, data_awal):
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, type(data_awal)):
            return data

        print(f"Format {nama_file} tidak sesuai.")
        return data_awal

    except FileNotFoundError:
        simpan_json(nama_file, data_awal)
        return data_awal

    except json.JSONDecodeError:
        print(f"File {nama_file} rusak atau kosong.")
        return data_awal


def waktu_sekarang():
    return time.time()


def format_waktu(timestamp):
    return time.strftime(
        "%d-%m-%Y %H:%M:%S",
        time.localtime(timestamp)
    )


def rupiah_ke_c(nominal):
    return nominal / KURS_C


def c_ke_rupiah(nominal):
    return nominal * KURS_C


def format_c(nominal_rupiah):
    return f"{rupiah_ke_c(nominal_rupiah):g} C"


def format_rupiah(nominal):
    return f"Rp{nominal:,.0f}".replace(",", ".")


def input_bilangan(pesan, minimum=0):
    while True:
        try:
            angka = int(input(pesan))

            if angka < minimum:
                print(f"Nilai minimum adalah {minimum}.")
            else:
                return angka

        except ValueError:
            print("Masukkan bilangan bulat yang valid.")


def konfirmasi(pesan):
    while True:
        jawaban = input(pesan + " (y/n): ").strip().lower()

        if jawaban == "y":
            return True
        elif jawaban == "n":
            return False

        print("Masukkan y atau n.")


def catat_aktivitas(username, aktivitas, keterangan):
    data = baca_json(FILE_AKTIVITAS, [])

    data.append({
        "username": username,
        "aktivitas": aktivitas,
        "keterangan": keterangan,
        "waktu": waktu_sekarang()
    })

    simpan_json(FILE_AKTIVITAS, data)


def buat_id(prefix, data, kolom):
    nomor_terpakai = {
        str(item.get(kolom)) for item in data
    }

    while True:
        nomor = f"{prefix}{random.randint(100000, 999999)}"

        if nomor not in nomor_terpakai:
            return nomor


# ==================== DATA AWAL ====================

def data_awal_kelas():
    return [
        {
            "id": 1,
            "nama": "Dasar Pemrograman",
            "pengajar": "Admin",
            "biaya": 50000
        },
        {
            "id": 2,
            "nama": "Basis Data",
            "pengajar": "Admin",
            "biaya": 45000
        },
        {
            "id": 3,
            "nama": "Algoritma",
            "pengajar": "Admin",
            "biaya": 60000
        },
        {
            "id": 4,
            "nama": "Jaringan Komputer",
            "pengajar": "Admin",
            "biaya": 75000
        },
        {
            "id": 5,
            "nama": "Sistem Informasi",
            "pengajar": "Admin",
            "biaya": 40000
        }
    ]


def siapkan_data():
    akun = baca_json(
        FILE_AKUN,
        [{
            "username": "admin",
            "password": "admin123",
            "role": "admin",
            "saldo": 0,
            "kelas_dibeli": []
        }]
    )

    kelas = baca_json(FILE_KELAS, data_awal_kelas())
    baca_json(FILE_INVOICE, [])
    baca_json(FILE_TOPUP, [])
    baca_json(FILE_REFUND, [])
    baca_json(FILE_AKTIVITAS, [])

    for pengguna in akun:
        pengguna.setdefault("saldo", 0)
        pengguna.setdefault("kelas_dibeli", [])

    admin_ada = any(
        pengguna.get("username") == "admin"
        for pengguna in akun
    )

    if not admin_ada:
        akun.append({
            "username": "admin",
            "password": "admin123",
            "role": "admin",
            "saldo": 0,
            "kelas_dibeli": []
        })

    simpan_json(FILE_AKUN, akun)
    simpan_json(FILE_KELAS, kelas)

    return akun, kelas


# ==================== REGISTRASI DAN LOGIN ====================

def registrasi(akun):
    print("\n========== REGISTRASI ==========")

    username = input("Buat username: ").strip()

    if len(username) < 4:
        print("Username minimal 4 karakter.")
        return akun

    for pengguna in akun:
        if pengguna["username"].lower() == username.lower():
            print("Username sudah digunakan.")
            return akun

    password = pwinput.pwinput("Buat password: ")

    if len(password) < 4:
        print("Password minimal 4 karakter.")
        return akun

    akun_baru = {
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0,
        "kelas_dibeli": []
    }

    akun.append(akun_baru)
    simpan_json(FILE_AKUN, akun)

    catat_aktivitas(
        username,
        "Registrasi",
        "Membuat akun baru"
    )

    print("Registrasi berhasil!")
    print("Saldo awal: 0 C")

    return akun


def login(akun):
    print("\n========== LOGIN ==========")

    for percobaan in range(3):
        username = input("Username: ").strip()
        password = pwinput.pwinput("Password: ")

        for pengguna in akun:
            if (
                pengguna["username"] == username
                and pengguna["password"] == password
            ):
                print("Login berhasil!")

                catat_aktivitas(
                    username,
                    "Login",
                    "Berhasil masuk ke sistem"
                )

                return pengguna

        print(f"Login gagal. Sisa percobaan: {2 - percobaan}")

    print("Batas percobaan login tercapai.")
    return None


# ==================== TAMPILAN KELAS ====================

def tampil_kelas(kelas):
    print("\n========== DAFTAR KELAS ==========")

    if not kelas:
        print("Belum ada kelas tersedia.")
        return

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Kelas", "Pengajar", "Harga"]

    for data in kelas:
        tabel.add_row([
            data["id"],
            data["nama"],
            data["pengajar"],
            format_c(data["biaya"])
        ])

    print(tabel)


# ==================== CRUD KELAS ====================

def tambah_kelas(kelas):
    print("\n========== TAMBAH KELAS ==========")

    nama = input("Nama kelas: ").strip()
    pengajar = input("Nama pengajar: ").strip()

    if not nama or not pengajar:
        print("Nama kelas dan pengajar wajib diisi.")
        return kelas

    if any(
        data["nama"].lower() == nama.lower()
        for data in kelas
    ):
        print("Nama kelas sudah tersedia.")
        return kelas

    harga_c = input_bilangan("Harga kelas dalam C: ", 0)

    id_baru = max(
        (data["id"] for data in kelas),
        default=0
    ) + 1

    kelas.append({
        "id": id_baru,
        "nama": nama,
        "pengajar": pengajar,
        "biaya": c_ke_rupiah(harga_c)
    })

    simpan_json(FILE_KELAS, kelas)

    catat_aktivitas(
        "admin",
        "Tambah kelas",
        nama
    )

    print("Kelas berhasil ditambahkan.")
    return kelas


def ubah_kelas(kelas):
    tampil_kelas(kelas)

    if not kelas:
        return kelas

    id_kelas = input_bilangan("ID kelas yang diubah: ", 1)

    data_kelas = next(
        (data for data in kelas if data["id"] == id_kelas),
        None
    )

    if data_kelas is None:
        print("Kelas tidak ditemukan.")
        return kelas

    nama = input(
        f"Nama [{data_kelas['nama']}]: "
    ).strip()

    pengajar = input(
        f"Pengajar [{data_kelas['pengajar']}]: "
    ).strip()

    harga = input(
        f"Harga [{format_c(data_kelas['biaya'])}]: "
    ).strip()

    harga_baru = None

    if harga:
        try:
            harga_c = int(harga)

            if harga_c < 0:
                print("Harga tidak boleh negatif.")
                return kelas

            harga_baru = c_ke_rupiah(harga_c)

        except ValueError:
            print("Harga harus berupa bilangan bulat.")
            return kelas

    if nama and any(
        data["id"] != id_kelas
        and data["nama"].lower() == nama.lower()
        for data in kelas
    ):
        print("Nama kelas sudah digunakan.")
        return kelas

    nama_lama = data_kelas["nama"]

    if nama:
        data_kelas["nama"] = nama

    if pengajar:
        data_kelas["pengajar"] = pengajar

    if harga_baru is not None:
        data_kelas["biaya"] = harga_baru

    simpan_json(FILE_KELAS, kelas)

    catat_aktivitas(
        "admin",
        "Ubah kelas",
        f"{nama_lama} diperbarui"
    )

    print("Data kelas berhasil diubah.")
    return kelas


def hapus_kelas(kelas):
    tampil_kelas(kelas)

    if not kelas:
        return kelas

    id_kelas = input_bilangan("ID kelas yang dihapus: ", 1)

    data_kelas = next(
        (data for data in kelas if data["id"] == id_kelas),
        None
    )

    if data_kelas is None:
        print("Kelas tidak ditemukan.")
        return kelas

    if not konfirmasi(
        f"Yakin menghapus {data_kelas['nama']}?"
    ):
        print("Penghapusan dibatalkan.")
        return kelas

    nama = data_kelas["nama"]
    kelas.remove(data_kelas)

    simpan_json(FILE_KELAS, kelas)

    catat_aktivitas(
        "admin",
        "Hapus kelas",
        nama
    )

    print("Kelas berhasil dihapus.")
    return kelas


# ==================== TOP UP ====================

def top_up(pengguna, akun):
    print("\n========== TOP UP SALDO ==========")
    print(f"Saldo saat ini: {format_c(pengguna['saldo'])}")
    print("Minimum top up : Rp1.000")
    print("Maksimum top up: Rp100.000.000")

    nominal = input_bilangan("Masukkan nominal Rupiah: ", 1)

    if not MIN_TOPUP <= nominal <= MAX_TOPUP:
        print("Nominal di luar batas top up.")
        return

    jumlah_c = rupiah_ke_c(nominal)

    print(f"Nominal top up: {format_rupiah(nominal)}")
    print(f"Koin diterima : {jumlah_c:g} C")

    if not konfirmasi("Lanjutkan top up?"):
        print("Top up dibatalkan.")
        return

    pengguna["saldo"] += nominal

    for data in akun:
        if data["username"] == pengguna["username"]:
            data["saldo"] = pengguna["saldo"]
            break

    simpan_json(FILE_AKUN, akun)

    daftar_topup = baca_json(FILE_TOPUP, [])
    id_topup = buat_id("TOP", daftar_topup, "id")

    transaksi = {
        "id": id_topup,
        "username": pengguna["username"],
        "nominal_rupiah": nominal,
        "jumlah_c": jumlah_c,
        "waktu": waktu_sekarang(),
        "status": "Berhasil"
    }

    daftar_topup.append(transaksi)
    simpan_json(FILE_TOPUP, daftar_topup)

    catat_aktivitas(
        pengguna["username"],
        "Top up",
        f"{format_rupiah(nominal)} atau {jumlah_c:g} C"
    )

    print("Top up berhasil!")
    print(f"Saldo sekarang: {format_c(pengguna['saldo'])}")


# ==================== PEMBELIAN KELAS ====================

def beli_kelas(pengguna, kelas, akun):
    tampil_kelas(kelas)

    if not kelas:
        return

    id_kelas = input_bilangan("ID kelas yang dibeli: ", 1)

    pilihan = next(
        (data for data in kelas if data["id"] == id_kelas),
        None
    )

    if pilihan is None:
        print("Kelas tidak ditemukan.")
        return

    if id_kelas in pengguna["kelas_dibeli"]:
        print("Kamu sudah membeli kelas ini.")
        return

    biaya = pilihan["biaya"]

    print(f"Nama kelas : {pilihan['nama']}")
    print(f"Harga      : {format_c(biaya)}")
    print(f"Saldo      : {format_c(pengguna['saldo'])}")

    if pengguna["saldo"] < biaya:
        print("Saldo tidak mencukupi. Silakan top up.")
        return

    if not konfirmasi("Lanjutkan pembelian?"):
        print("Pembelian dibatalkan.")
        return

    waktu_beli = waktu_sekarang()

    pengguna["saldo"] -= biaya
    pengguna["kelas_dibeli"].append(id_kelas)

    for data in akun:
        if data["username"] == pengguna["username"]:
            data["saldo"] = pengguna["saldo"]
            data["kelas_dibeli"] = pengguna["kelas_dibeli"]
            break

    simpan_json(FILE_AKUN, akun)

    daftar_invoice = baca_json(FILE_INVOICE, [])
    id_invoice = buat_id("INV", daftar_invoice, "id")

    invoice = {
        "id": id_invoice,
        "username": pengguna["username"],
        "kelas_id": id_kelas,
        "nama_kelas": pilihan["nama"],
        "biaya": biaya,
        "waktu_beli": waktu_beli,
        "status": "Berhasil",
        "status_refund": "Tidak diajukan",
        "alasan_refund": "",
        "waktu_refund": None
    }

    daftar_invoice.append(invoice)
    simpan_json(FILE_INVOICE, daftar_invoice)

    catat_aktivitas(
        pengguna["username"],
        "Pembelian kelas",
        f"{pilihan['nama']} - {id_invoice}"
    )

    print("\n========== INVOICE ==========")
    print(f"No. Invoice : {id_invoice}")
    print(f"Username    : {pengguna['username']}")
    print(f"Kelas       : {pilihan['nama']}")
    print(f"Total       : {format_c(biaya)}")
    print(f"Waktu       : {format_waktu(waktu_beli)}")
    print("Status      : Berhasil")
    print("Masa refund : 45 menit")
    print(f"Sisa saldo  : {format_c(pengguna['saldo'])}")


# ==================== REFUND ====================

def ajukan_refund(pengguna, akun, kelas):
    print("\n========== PENGAJUAN REFUND ==========")

    daftar_invoice = baca_json(FILE_INVOICE, [])

    pembelian = [
    item for item in daftar_invoice
    if (
        item.get("username") == pengguna["username"]
        and item.get("status") == "Berhasil"
        and item.get("status_refund", "Tidak diajukan")
            == "Tidak diajukan"
        and item.get("waktu_beli") is not None
        and item.get("kelas_id") is not None
    )
]

    if not pembelian:
        print("Tidak ada pembelian yang bisa diajukan refund.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "No", "Invoice", "Kelas", "Harga", "Sisa Waktu"
    ]

    sekarang = waktu_sekarang()

    for nomor, item in enumerate(pembelian, start=1):
        sisa = BATAS_REFUND - (sekarang - item["waktu_beli"])
        sisa = max(0, int(sisa))

        menit = sisa // 60
        detik = sisa % 60

        tabel.add_row([
            nomor,
            item["id"],
            item["nama_kelas"],
            format_c(item["biaya"]),
            f"{menit}m {detik}s"
        ])

    print(tabel)

    nomor = input_bilangan(
        "Pilih nomor pembelian yang direfund: ", 1
    )

    if nomor > len(pembelian):
        print("Pilihan tidak tersedia.")
        return

    invoice = pembelian[nomor - 1]
    sekarang = waktu_sekarang()
    selisih = sekarang - invoice["waktu_beli"]

    if selisih > BATAS_REFUND:
        print("Refund ditolak: masa percobaan 45 menit telah berakhir.")
        return

    alasan = input("Alasan refund: ").strip()

    if len(alasan) < 5:
        print("Alasan refund minimal 5 karakter.")
        return

    print(f"Pengembalian: {format_c(invoice['biaya'])}")
    print(f"Alasan      : {alasan}")

    if not konfirmasi("Ajukan refund sekarang?"):
        print("Pengajuan dibatalkan.")
        return

    # Periksa ulang waktu saat pengajuan dikonfirmasi
    sekarang = waktu_sekarang()

    if sekarang - invoice["waktu_beli"] > BATAS_REFUND:
        print("Refund ditolak: batas waktu telah berakhir.")
        return

    # Kembalikan saldo dan cabut akses kelas
    pengguna["saldo"] += invoice["biaya"]
    pengguna["kelas_dibeli"].remove(invoice["kelas_id"])

    for data in akun:
        if data["username"] == pengguna["username"]:
            data["saldo"] = pengguna["saldo"]
            data["kelas_dibeli"] = pengguna["kelas_dibeli"]
            break

    simpan_json(FILE_AKUN, akun)

    # Perbarui invoice asli
    invoice["status"] = "Direfund"
    invoice["status_refund"] = "Berhasil"
    invoice["alasan_refund"] = alasan
    invoice["waktu_refund"] = sekarang

    simpan_json(FILE_INVOICE, daftar_invoice)

    # Simpan catatan refund terpisah
    daftar_refund = baca_json(FILE_REFUND, [])
    id_refund = buat_id("REF", daftar_refund, "id")

    daftar_refund.append({
        "id": id_refund,
        "invoice_id": invoice["id"],
        "username": pengguna["username"],
        "nama_kelas": invoice["nama_kelas"],
        "jumlah_rupiah": invoice["biaya"],
        "jumlah_c": rupiah_ke_c(invoice["biaya"]),
        "alasan": alasan,
        "waktu": sekarang,
        "status": "Berhasil"
    })

    simpan_json(FILE_REFUND, daftar_refund)

    catat_aktivitas(
        pengguna["username"],
        "Refund berhasil",
        f"{invoice['id']} - {invoice['nama_kelas']}"
    )

    print("\nRefund berhasil!")
    print(f"Koin dikembalikan: {format_c(invoice['biaya'])}")
    print(f"Saldo sekarang   : {format_c(pengguna['saldo'])}")
    print("Akses kelas telah dicabut.")


# ==================== KELAS YANG DIBELI ====================

def tampil_kelas_user(pengguna, kelas):
    print("\n========== KELAS SAYA ==========")

    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Kelas", "Pengajar"]
    jumlah = 0

    for data in kelas:
        if data["id"] in pengguna["kelas_dibeli"]:
            tabel.add_row([
                data["id"],
                data["nama"],
                data["pengajar"]
            ])
            jumlah += 1

    if jumlah:
        print(tabel)
    else:
        print("Kamu belum memiliki kelas aktif.")


# ==================== RIWAYAT UNTUK ADMIN ====================

def tampilkan_tabel(judul, kolom, baris):
    print(f"\n========== {judul} ==========")

    if not baris:
        print("Belum ada data.")
        return

    tabel = PrettyTable()
    tabel.field_names = kolom

    for data in baris:
        tabel.add_row(data)

    print(tabel)


def admin_semua_akun(akun):
    baris = [
        [
            item["username"],
            item["role"],
            format_c(item.get("saldo", 0))
        ]
        for item in akun
    ]

    tampilkan_tabel(
        "SEMUA AKUN",
        ["Username", "Role", "Saldo"],
        baris
    )


def admin_riwayat_pembelian():
    invoice = baca_json(FILE_INVOICE, [])

    baris = [
        [
            item["id"],
            item["username"],
            item["nama_kelas"],
            format_c(item["biaya"]),
            format_waktu(item["waktu_beli"]),
            item["status"],
            item["status_refund"]
        ]
        for item in invoice
    ]

    tampilkan_tabel(
        "SEMUA RIWAYAT PEMBELIAN",
        [
            "Invoice", "Username", "Kelas", "Harga",
            "Waktu", "Status", "Refund"
        ],
        baris
    )


def admin_riwayat_topup():
    daftar = baca_json(FILE_TOPUP, [])

    baris = [
        [
            item["id"],
            item["username"],
            format_rupiah(item["nominal_rupiah"]),
            f"{item['jumlah_c']:g} C",
            format_waktu(item["waktu"]),
            item["status"]
        ]
        for item in daftar
    ]

    tampilkan_tabel(
        "SEMUA RIWAYAT TOP UP",
        ["ID", "Username", "Nominal", "Koin", "Waktu", "Status"],
        baris
    )


def admin_riwayat_refund():
    daftar = baca_json(FILE_REFUND, [])

    baris = [
        [
            item["id"],
            item["invoice_id"],
            item["username"],
            item["nama_kelas"],
            f"{item['jumlah_c']:g} C",
            item["alasan"],
            format_waktu(item["waktu"]),
            item["status"]
        ]
        for item in daftar
    ]

    tampilkan_tabel(
        "SEMUA RIWAYAT REFUND",
        [
            "ID Refund", "Invoice", "Username", "Kelas",
            "Koin", "Alasan", "Waktu", "Status"
            ],
        baris
    )


def admin_semua_aktivitas():
    daftar = baca_json(FILE_AKTIVITAS, [])

    baris = [
        [
            item["username"],
            item["aktivitas"],
            item["keterangan"],
            format_waktu(item["waktu"])
        ]
        for item in daftar
    ]

    tampilkan_tabel(
        "SEMUA AKTIVITAS",
        ["Username", "Aktivitas", "Keterangan", "Waktu"],
        baris
    )


# ==================== MENU ADMIN ====================

def menu_admin(akun, kelas):
    while True:
        print("\n========== MENU ADMIN ==========")
        print("1. Lihat kelas")
        print("2. Tambah kelas")
        print("3. Ubah kelas")
        print("4. Hapus kelas")
        print("5. Lihat semua akun")
        print("6. Riwayat pembelian")
        print("7. Riwayat top up")
        print("8. Riwayat refund")
        print("9. Semua aktivitas")
        print("10. Logout")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampil_kelas(kelas)
        elif pilihan == "2":
            kelas = tambah_kelas(kelas)
        elif pilihan == "3":
            kelas = ubah_kelas(kelas)
        elif pilihan == "4":
            kelas = hapus_kelas(kelas)
        elif pilihan == "5":
            admin_semua_akun(akun)
        elif pilihan == "6":
            admin_riwayat_pembelian()
        elif pilihan == "7":
            admin_riwayat_topup()
        elif pilihan == "8":
            admin_riwayat_refund()
        elif pilihan == "9":
            admin_semua_aktivitas()
        elif pilihan == "10":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu admin...")

    return kelas


# ==================== MENU USER ====================
def menu_user(pengguna, kelas, akun):
    while True:
        print("\n========== MENU USER ==========")
        print(f"Username : {pengguna['username']}")
        print(f"Saldo    : {format_c(pengguna['saldo'])}")
        print("1. Lihat kelas")
        print("2. Top up saldo")
        print("3. Beli kelas")
        print("4. Kelas yang diakses")
        print("5. Ajukan refund")
        print("6. Logout")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampil_kelas(kelas)
        elif pilihan == "2":
            top_up(pengguna, akun)
        elif pilihan == "3":
            beli_kelas(pengguna, kelas, akun)
        elif pilihan == "4":
            tampil_kelas_user(pengguna, kelas)
        elif pilihan == "5":
            ajukan_refund(pengguna, akun, kelas)
        elif pilihan == "6":
            catat_aktivitas(
                pengguna["username"],
                "Logout",
                "Keluar dari akun"
            )
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

        input("\nTekan Enter untuk kembali ke menu user...")


# ==================== PROGRAM UTAMA ====================

def main():
    akun, kelas = siapkan_data()

    while True:
        print("\n================================")
        print("          SISTEM KELASKU")
        print(" Sistem Pengelolaan Kelas Online")
        print("================================")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            pengguna = login(akun)

            if pengguna is not None:
                if pengguna["role"] == "admin":
                    kelas = menu_admin(akun, kelas)
                else:
                    menu_user(pengguna, kelas, akun)

        elif pilihan == "2":
            akun = registrasi(akun)
            input("\nTekan Enter untuk kembali ke menu utama...")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan KelasKu.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, PermissionError) as error:
        print(f"Terjadi kesalahan: {error}")