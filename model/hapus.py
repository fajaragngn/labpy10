from view.input_nilai import *
from model.core import data

# Menghapus data
def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in data.keys():
        del data[nama]
        print("Data '{}' berhasil dihapus.".format(nama))
    else:
        print("'{}' tidak ditemukan.".format(nama))
