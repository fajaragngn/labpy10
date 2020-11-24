from view.input_nilai import *
from model.core import data

# Menambahkan data
def tambah_data():
    global data
    nama = input_nama()
    nim = input_nim()
    nilai_tugas = input_ntugas()
    nilai_uts = input_nuts()
    nilai_uas = input_nuas()
    nilai_akhir = nakhir()
    data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]
    print('\nData berhasil di tambah!')
    return data