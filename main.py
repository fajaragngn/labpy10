from controller.core import data
from model.tambah import *
from model.ubah import *
from model.hapus import *
from view.tampilkan import *

    print("Sebelum akses program izin dulu sama yang punya :p")
    break

    #Mulai
    print("###############################################################")
    print("|                     Program Input Nilai                     |")
    print("###############################################################")

    while True:
        print("\n")
        menu = input("(L) Lihat, (T) Tambah, (H) Hapus, (U) Ubah, (C) Cari, (K) Keluar: ")
        print("\n")

        # menu
        if menu.lower() == 't':
            tambah_data()

        elif menu.lower() == 'c':
            cari_data()

        elif menu.lower() == 'l':
            lihat_data()

        elif menu.lower() == 'u':
            ubah_data()

        elif menu.lower() == 'h':
            hapus_data()

        # Keluar
        elif menu.lower() == 'k':
            break

        else:
            print("Upss ada yang salah, silahkan cek kembali.")
