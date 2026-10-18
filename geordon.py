import json
import os
import time
import random
import pwinput
from prettytable import PrettyTable

FILE_AKUN = "akun.json"
FILE_KELAS = "kelas.json"

STATUS_TUGAS = ("Belum", "Dikumpulkan", "Dinilai")

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def baca_json(nama_file, data_awal):
    try:
        with open(nama_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        simpan_json(nama_file, data_awal)
        return data_awal
    except json.JSONDecodeError:
        print("File JSON rusak atau kosong.")
        return data_awal

def simpan_json(nama_file, data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=4)

def data_awal_kelas():
    return [
        {"id": 1, "nama": "Dasar Pemrograman",
         "pengajar": "Admin", "biaya": 0},
        {"id": 2, "nama": "Basis Data",
         "pengajar": "Admin", "biaya": 0},
        {"id": 3, "nama": "Algoritma",
         "pengajar": "Admin", "biaya": 0},
        {"id": 4, "nama": "Jaringan Komputer",
         "pengajar": "Admin", "biaya": 0},
        {"id": 5, "nama": "Sistem Informasi",
         "pengajar": "Admin", "biaya": 0}
    ]

def siapkan_data():
    akun = baca_json(FILE_AKUN, [
        {
            "username": "admin",
            "password": "admin123",
            "role": "admin",
            "saldo": 0
        }
    ])
    kelas = baca_json(FILE_KELAS, data_awal_kelas())

    # Pastikan akun admin tersedia
    ada_admin = False
    for data in akun:
        if data["username"] == "admin" and data["role"] == "admin":
            ada_admin = True

    if not ada_admin:
        akun.append({
            "username": "admin",
            "password": "admin123",
            "role": "admin",
            "saldo": 0
        })

    simpan_json(FILE_AKUN, akun)
    simpan_json(FILE_KELAS, kelas)
    return akun, kelas

def registrasi(akun):
    print("\n=== REGISTRASI USER ===")
    username = input("Buat username: ").strip()

    if len(username) < 4:
        print("Username minimal 4 karakter.")
        return akun

    for data in akun:
        if data["username"].lower() == username.lower():
            print("Username sudah digunakan.")
            return akun

    password = pwinput.pwinput("Buat password: ")

    if len(password) < 4:
        print("Password minimal 4 karakter.")
        return akun

    akun.append({
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0
    })

    simpan_json(FILE_AKUN, akun)
    print("Registrasi berhasil.")
    return akun

def login(akun):
    print("\n=== LOGIN ===")
    username = input("Username: ").strip()
    password = pwinput.pwinput("Password: ")

    for data in akun:
        if (data["username"] == username
                and data["password"] == password):
            print("Login berhasil.")
            time.sleep(1)
            return data

    print("Username atau password salah.")
    return None

def tampil_kelas(kelas):
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama Kelas", "Pengajar", "Biaya"]

    for data in kelas:
        tabel.add_row([
            data["id"],
            data["nama"],
            data["pengajar"],
            data["biaya"]
        ])

    print(tabel)

def tambah_kelas(kelas):
    print("\n=== TAMBAH KELAS ===")
    nama = input("Nama kelas: ").strip()
    pengajar = input("Nama pengajar: ").strip()

    if nama == "" or pengajar == "":
        print("Nama kelas dan pengajar wajib diisi.")
        return kelas

    for data in kelas:
        if data["nama"].lower() == nama.lower():
            print("Nama kelas sudah ada.")
            return kelas

    try:
        biaya = int(input("Biaya kelas: "))
        if biaya < 0:
            print("Biaya tidak boleh negatif.")
            return kelas
    except ValueError:
        print("Biaya harus berupa angka.")
        return kelas

    id_baru = max([data["id"] for data in kelas], default=0) + 1

    kelas.append({
        "id": id_baru,
        "nama": nama,
        "pengajar": pengajar,
        "biaya": biaya
    })

    simpan_json(FILE_KELAS, kelas)
    print("Kelas berhasil ditambahkan.")
    return kelas

def ubah_kelas(kelas):
    tampil_kelas(kelas)

    try:
        id_kelas = int(input("ID kelas yang ingin diubah: "))
    except ValueError:
        print("ID harus berupa angka.")
        return kelas

    for data in kelas:
        if data["id"] == id_kelas:
            nama = input("Nama baru (Enter jika tetap): ").strip()
            pengajar = input("Pengajar baru (Enter jika tetap): ").strip()

            if nama != "":
                data["nama"] = nama
            if pengajar != "":
                data["pengajar"] = pengajar

            try:
                biaya = input("Biaya baru (Enter jika tetap): ")
                if biaya != "":
                    biaya = int(biaya)
                    if biaya < 0:
                        print("Biaya tidak boleh negatif.")
                        return kelas
                    data["biaya"] = biaya
            except ValueError:
                print("Biaya harus berupa angka.")
                return kelas

            simpan_json(FILE_KELAS, kelas)
            print("Data kelas berhasil diubah.")
            return kelas

    print("ID kelas tidak ditemukan.")
    return kelas

def hapus_kelas(kelas):
    tampil_kelas(kelas)

    try:
        id_kelas = int(input("ID kelas yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return kelas

    for data in kelas:
        if data["id"] == id_kelas:
            konfirmasi = input("Yakin hapus kelas? (y/n): ").lower()

            if konfirmasi == "y":
                kelas.remove(data)
                simpan_json(FILE_KELAS, kelas)
                print("Kelas berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")
            return kelas

    print("ID kelas tidak ditemukan.")
    return kelas

def menu_admin(kelas):
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat kelas")
        print("2. Tambah kelas")
        print("3. Ubah kelas")
        print("4. Hapus kelas")
        print("5. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampil_kelas(kelas)
        elif pilihan == "2":
            kelas = tambah_kelas(kelas)
        elif pilihan == "3":
            kelas = ubah_kelas(kelas)
        elif pilihan == "4":
            kelas = hapus_kelas(kelas)
        elif pilihan == "5":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak tersedia.")

def menu_user(kelas):
    while True:
        print("\n=== MENU USER ===")
        print("1. Lihat kelas")
        print("2. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampil_kelas(kelas)
        elif pilihan == "2":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak tersedia.")

def main():
    akun, kelas = siapkan_data()

    while True:
        bersihkan_layar()
        print("================================")
        print(" KELASKU - KELAS ONLINE")
        print("================================")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            pengguna = login(akun)

            if pengguna is not None:
                if pengguna["role"] == "admin":
                    menu_admin(kelas)
                elif pengguna["role"] == "user":
                    menu_user(kelas)

        elif pilihan == "2":
            akun = registrasi(akun)

        elif pilihan == "3":
            print("Terima kasih telah menggunakan KelasKu.")
            break

        else:
            print("Pilihan tidak tersedia.")
            time.sleep(1)

if __name__ == "__main__":
    main()