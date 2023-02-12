mahasiswa = []

def tambah(nama, nilai):
    mahasiswa.append({'nama': nama, 'nilai': nilai})

def tampilkan():
    if len(mahasiswa) == 0:
        print("Daftar mahasiswa kosong.")
        return
    print("Daftar Nilai Mahasiswa:")
    for i, mhs in enumerate(mahasiswa):
        print("{}. {}: {}".format(i + 1, mhs['nama'], mhs['nilai']))

def hapus(nama):
    for mhs in mahasiswa:
        if mhs['nama'] == nama:
            mahasiswa.remove(mhs)
            print("Data mahasiswa dengan nama '{}' berhasil dihapus.".format(nama))
            return
    print("Data mahasiswa dengan nama '{}' tidak ditemukan.".format(nama))

def ubah(nama, nilai_baru):
    for mhs in mahasiswa:
        if mhs['nama'] == nama:
            mhs['nilai'] = nilai_baru
            print("Data mahasiswa dengan nama '{}' berhasil diubah.".format(nama))
            return
    print("Data mahasiswa dengan nama '{}' tidak ditemukan.".format(nama))

if __name__ == '__main__':
    while True:
        print("\nPilih opsi:")
        print("(1) Tambah Data")
        print("(2) Tampilkan Daftar Nilai")
        print("(3) Hapus Data")
        print("(4) Ubah Data")
        print("(0) Keluar")
        pilihan = int(input("Masukkan opsi: "))
        
        if pilihan == 1:
            nama = input("Masukkan nama: ")
            nilai = int(input("Masukkan nilai: "))
            tambah(nama, nilai)
        elif pilihan == 2:
            tampilkan()
        elif pilihan == 3:
            nama = input("Masukkan nama: ")
            hapus(nama)
        elif pilihan == 4:
            nama = input("Masukkan nama: ")
            nilai_baru = int(input("Masukkan nilai baru: "))
            ubah(nama, nilai_baru)
        elif pilihan == 0:
            break
        else:
            print("Pilihan tidak tersedia.")
