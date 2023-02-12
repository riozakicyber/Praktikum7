# Praktikum7

Nama        : Rio Rinto Saki

NIM         : 312210715

Kelas       : TI.22.C.9


# Program Menghitung Nilai Mahasiswa 

Pada praktek kali ini, saya mencoba membuat program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa.

- Source Code
```
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



```
- Flowchart




# Screenshot Input
![Screenshot (70)](https://user-images.githubusercontent.com/123881535/218321174-97de640d-0a79-4fe5-935e-b60b1338bea9.png)


# Screenshot Ouput
![Screenshot (68)](https://user-images.githubusercontent.com/123881535/218321192-714dbe50-cca2-4a03-99f0-15a434eaf471.png)
![Screenshot (69)](https://user-images.githubusercontent.com/123881535/218321197-19a22aba-906d-43e2-bfe9-622e31d66c94.png)


