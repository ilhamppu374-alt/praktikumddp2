#Nama : Muhammad Ilham Zaini
#Kelas : Sistem Informasi C
#Nim : 2509116091
#Inventaris Alat Musik

from prettytable import PrettyTable

config = {
    "pesan_sukses": "Berhasil",
    "pesan_error": "Error!"
}

data_alat = [
    {"Nama": "Gitar", "Jenis":"Petik"},
    {"Nama": "Seruling", "Jenis":"Tiup"},
    {"Nama": "Drum", "Jenis":"Pukul"}
]

def list_alat():
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Jenis"]
    for alat in data_alat:
        tabel.add_row([alat["Nama"], alat["Jenis"]])
    print(tabel)

def tambah_alat():
    print("Tambahkan alat")
    Nama = input("Masukkan nama alat :")
    Jenis = input("Masukkan jenis alat :")
    data_alat.append({"Nama": Nama, "Jenis": Jenis})
    print("Berhasil menambahkan")
    list_alat

def edit_alat():
    print("Edit alat")
    list_alat()
    nama_alat = input("Masukkan nama alat yang ingin diedit: ")   

    found = False

    for alat in data_alat:
        if alat["Nama"].lower() == nama_alat.lower():
            print("Masukkan data baru (biarkan kosong jika tidak ingin mengubah):")
            new_nama = input(f"Nama ({alat['Nama']}): ") or alat['Nama']
            new_Jenis = input(f"Jenis ({alat['Jenis']}): ") or alat['Jenis'] 

            alat.update({"Nama": new_nama, "Jenis": new_Jenis})
            print(f"alat '{alat['Nama']}' berhasil diperbarui.")
            list_alat()
            found = True
            break

    if not found:
        print(f"alat '{nama_alat}' tidak ditemukan.")

def hapus_alat():
    print("Hapus alat")
    list_alat()
    nama_alat = input("Masukkan nama alat yang ingin dihapus: ")

    found = False

    for alat in data_alat:
        if alat["Nama"].lower() == nama_alat.lower():
            data_alat.remove(alat)
            print(f"alat '(nama_alat)' berhasil dihapus.")
            list_alat()
            found = True
            break

        if not found:
            print(f"alat '{nama_alat}' tidak ditemukan.")

def get_pesan(key):
    return config.get(key, "Pesan default")

def keluar():
    print(get_pesan("pesan_sukses"))

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == 'admin' and password == '12345':
    print("Selamat datang admin!")
    while True:
        menu_pilihan = [
            {"Nomor": "1", "Pilihan": "Tambah alat"},
            {"Nomor": "2", "Pilihan": "List alat"},
            {"Nomor": "3", "Pilihan": "Edit alat"},
            {"Nomor": "4", "Pilihan": "Hapus alat"},
            {"Nomor": "5", "Pilihan": "Keluar"},
        ]
        tabel = PrettyTable()
        tabel.field_names = ["Nomor", "Pilihan"]
        for menu in menu_pilihan:
            tabel.add_row([menu["Nomor"], menu["Pilihan"]])
        print(tabel)

        pilihan = input("Pilih opsi (1-5):")
        if pilihan == '1':
            tambah_alat()
        elif pilihan == '2':
            list_alat()
        elif pilihan == '3':
            edit_alat()
        elif pilihan == '4':
            hapus_alat()
        elif pilihan == '5':
            keluar()
            break
        else:
            print("Opsi tidak valid! silahkan pilih antara 1-5.")

elif username == 'pengunjung' and password == '123':
    print("Selamat datang pengunjung!")
    while True:
        print("Menu:")
        print("1. Lihat list alat")
        print("2. Keluar")

        pilihan = input("Pilih opsi (1-2):")

        if pilihan == '1':
            list_alat()

        elif pilihan == '2':
            keluar()
            break
        else:
            print("Opsi tidak valid!")

else:
    print("Tidak valid")                                             
