# Menginput data

def input_nama():
    print("Masukan data mahasiswa")
    print("...")
    global nama
    nama = input("\nNama: ")
    return nama


def input_nim():
    global nim
    nim = input("NIM: ")
    return nim


def input_ntugas():
    global nilai_tugas
    nilai_tugas = int(input("Masukan nilai tugas: "))
    return nilai_tugas


def input_nuts():
    global nilai_uts
    nilai_uts = int(input("Masukan nilai UTS: "))
    return nilai_uts


def input_nuas():
    global nilai_uas
    nilai_uas = int(input("Masukan nilai UAS: "))
    return nilai_uas


# Menghitung nilai akhir
def nakhir():
    global nilai_akhir
    a = nilai_tugas * 30 / 100
    b = nilai_uts * 35 / 100
    c = nilai_uas * 35 / 100
    nilai_akhir = a+b+c
    return nilai_akhir