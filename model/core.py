from view.input_nilai import *

data = {}

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

# Mengubah data
def ubah_data():
    nama = input("Masukan nama untuk mengubah data: ")
    if nama in data.keys():
        print("Mau mengubah apa?")
        sub_data = input("(Semua), (Nama), (NIM), (Tugas), (UTS), (UAS) : ")
        if sub_data.lower() == "semua":
            print("==========================")
            print("Ubah data {}.".format(nama))
            print("==========================")
            data[nama][1] = input("Ubah NIM:")
            data[nama][2] = int(input("Ubah Nilai Tugas: "))
            data[nama][3] = int(input("Ubah Nilai UTS: "))
            data[nama][4] = int(input("Ubah Nilai UAS: "))
            data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4] *35/100 
            print("\nBerhasil ubah data!")
            print("___________________________________________________________________")
            print("| No |      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
            print("===================================================================")
            no = 1
            for tabel in data.values():
                print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                    (no, tabel[0],
                    tabel[1], tabel[2],
                    tabel[3], tabel[4], tabel[5]))
                no += 1
        elif sub_data.lower() == "nim":
            data[nama][1] = input("\nNIM:")
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "tugas":
            data[nama][2] = int(input("\nNilai Tugas: "))
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "uts":
            data[nama][3] = int(input("\nNilai UTS: "))
            print('\nData berhasil di ubah!')
        elif sub_data.lower() == "uas":
            data[nama][4] = int(input("\nNilai UAS: "))
            print('\nData berhasil di ubah!')
        else:
            print("\nmenu tidak ditemukan.")

    else:
        print("'{}' tidak ditemukan.".format(nama))

# Menghapus data
def hapus_data():
    nama = input("Masukan nama untuk menghapus data : ")
    if nama in data.keys():
        del data[nama]
        print("Data '{}' dihapus.".format(nama))
    else:
        print("'{}' tidak ditemukan.".format(nama))


