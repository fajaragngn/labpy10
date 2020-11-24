from model.core import data

# Menampilkan data
def lihat_data():
    print("Data Nilai Mahasiswa:")
    print("___________________________________________________________________")
    print("| No |      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
    print("===================================================================")
    if data.keys():
        no = 1
        for tabel in data.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                  (no, tabel[0],
                   tabel[1], tabel[2],
                   tabel[3], tabel[4], tabel[5]))
            no += 1
    else:
        print("=========================TIDAK ADA DATA============================")
        print("===================================================================")

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
    