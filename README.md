# Praktikum7
# Program Menghitung Nilai Mahasiswa 

Pada praktek kali ini, saya mencoba membuat program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa.

- Source Code dan Penjelasan
```
dataMhs = {}                                                                                     ## Membuat Dictionary kosong
print("==================================================================")
print("|                  PROGRAM INPUT NILAI MAHASISWA                 |")
print("==================================================================")

while True:                                                                                      ## LOOPING AKTIF
    c = input("\nL)ihat, T)ambah, U)bah, C)ari H)apus, K)eluar: ")                               ## Membuat Menu

    ## MENU LIHAT
    if (c.lower() == 't'):                                                                       ## MENU LIHAT
        print("\n=========================")
        print("| TAMBAH DATA MAHASISWA |")
        print("=========================")
        nama          = input("Masukkan Nama        : ")                                         ## Menginput Nama
        nim           = input("Masukkan NIM         : ")                                         ## Menginput NIM
        nilaiTugas    = int(input("Masukkan Nilai Tugas : "))                                    ## Menginput Nilai Tugas
        nilaiUts      = int(input("Masukkan Nilai UTS   : "))                                    ## Menginput Nilai UTS
        nilaiUas      = int(input("Masukkan Nilai UAS   : "))                                    ## Menginput Nilai UAS
        nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)              ## Menghitung Nilai Akhir
        dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                          ## Menambahkan data yang sudah diinput ke Dictionary
        print("\nData Berhasil Ditambahkan!")

    ## MENU UBAH
    elif (c.lower() == 'u'):                                                                     ## Menu UBAH
        print("\n=======================")
        print("| EDIT DATA MAHASISWA |")
        print("=======================")
        nama = input("Masukkan Nama: ")                                                          ## Cari nama yang akan diedit
        if nama in dataMhs.keys():                                                               ## Mengambil key dari Dictionary
            nim           = input("Masukkan NIM Baru         : ")                                ## Menginput NIM baru
            nilaiTugas    = int(input("Masukkan Nilai Tugas Baru : "))                           ## Menginput Nilai Tugas Baru
            nilaiUts      = int(input("Masukkan Nilai UTS Baru   : "))                           ## Menginput Nilai UTS Baru
            nilaiUas      = int(input("Masukkan Nilai UAS Baru   : "))                           ## Menginput Nilai UAS Baru
            nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)          ## Menghitung Nilai Akhir Baru
            dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir                      ## Mengupdate data ke Dictionary
            print("\nData Berhasil Di Update!")
        else:                                                                                    
            print("Data tidak ditemukan!")                                                       ## Jika nama tidak ditemukan maka muncul perintah tsb.

    ## MENU CARI
    elif (c.lower() == 'c'):                                                                     ## Menu CARI
        print("\n=======================")
        print("| CARI DATA MAHASISWA |")
        print("=======================")
        nama = input("Masukan Nama:  ")                                                          ## Masukkan nama yang akan dicari
        if nama in dataMhs.keys():                                                               ## Mengambil keys dari Dictionary
            print("\n                   DAFTAR NILAI MAHASISWA                   ")
            print("==============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==============================================================")
            print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir))      ## Format tabel
            print("==============================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))                                        ## Jika data tidak ditemukan, akan muncul perintah tsb.

    ## MENU HAPUS
    elif (c.lower() == 'h'):                                                                    ## Menu HAPUS
        nama = input("Masukkan Nama:  ")                                                        ## Masukkan nama yang akan didelete
        if nama in dataMhs.keys():                                                              ## Mengambil keys dari Dictionary
            del dataMhs[nama]                                                                   ## Menghapus data yang dipilih
            print("Data Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada".format(nama))                                      ## Jika data tidak ditemukan, akan muncul perintah tsb.

    ## MENU LIHAT
    elif (c.lower() == 'l'):                                                                    ## Menu LUHAT
        if dataMhs.items():                                                                     ## Mengambil items dari Dictionary
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in dataMhs.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))  ## Format tabel
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")        ## Jika data masih kosong, akan muncul pesan tsb.

    ## MENU KELUAR
    elif (c.lower() == 'k'):                                                                   ## Menu KELUAR
        print("\n Rio Rinto Saki \n 3112210715 \n TI.22.C.9")
        break                                                                                  ## Mengakhiri LOOPING

    else:
        print("Pilih menu yang tersedia: ")                                                    ## Jika menu yang dipilih tidak valid, akan muncul pesan tsb.
        


```
- Flowchart
![Flowchart Program Nilai Mahasiswa](https://user-images.githubusercontent.com/123881535/218318093-6677a619-37f7-45bb-aee8-35dcfc68bd53.jpg)



# Screenshot Input
![Screenshot (61)](https://user-images.githubusercontent.com/123881535/218318101-916a8365-a4dc-4dec-b70b-a2ca8a04c226.png)
![Screenshot (62)](https://user-images.githubusercontent.com/123881535/218318117-b0977f94-2be8-4b04-b5cb-381ac5706a46.png)



# Screenshot Ouput
![Screenshot (63)](https://user-images.githubusercontent.com/123881535/218318108-6639764c-160a-451a-a81c-b800f99e75d1.png)

