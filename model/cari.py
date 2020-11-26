from controller.core import *

# Mencari data
def cari_data():
    print("Mencari data: ")
    print("=================================================")
    nama = input("Masukan nama untuk mencari data: ")
    if nama in data.keys():
        print('\nResult')
        print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}"
                .format(nama, data[nama][1],
                            data[nama][2], data[nama][3],
                            data[nama][4], data[nama][5]))
    else:
        print("'{}' tidak ditemukan.".format(nama))