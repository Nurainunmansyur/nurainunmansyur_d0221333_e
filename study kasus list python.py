#menambah
#menghapus
#mengedit
#menampilkan
#mencari barang
#mencari index
#keluar

barang =[]
perintah = 0

while perintah != 7 :
    print('''1. Menambah
2. Menghapus
3. Mengedit
4. Menampilkan
5. Mencari Barang
6. Mencari Index
7. Keluar''')
    perintah = int(input("Masukkan Perintah : "))

    if perintah == 1 :
        while True :
            elemen = input("Masukkan Barang Yang dipilih : ")
            barang.append(elemen)

            stop = input("Ketik Y untuk berhenti, Selain Itu Lanjut : ").lower()
            if stop == 'y' :
                break
            
    elif perintah == 2 :
        while True :
            hapus = input("Masukkan index yang akan di hapus : ")
            barang.pop(hapus)

            stop = input("Ketik Y untuk berhenti, Selain Itu Lanjut : ").lower()
            if stop == 'y' :
                break

    elif perintah == 3 :
        while True :
            edit = int(input("Masukkan Barang Baru : "))

            if edit > (len(barang) -1) :
                print("Index tidak di temukan")
            else :
                barang[edit] = input("Masukkan Barang yang Baru : ")

            stop = input("Ketik Y untuk berhenti, Selain Itu Lanjut : ").lower()
            if stop == 'y' :
                break

    elif perintah == 4 :
        for i in range(len(barang)) :
            print(barang[i])

    elif perintah == 5 :
        cari = input("Masukkan barang yang di cari : ")
        flag = False

        for i in range (len(barang)) :
            if barang [i] == cari :
                print("Barang Ada dalam list : ")
            else :
                print("Barang Tidak di temukan : ")

    elif perintah == 6 :
        cariindex = input("Masukkan Index yang dicari :")

        if cariindex in barang :
            print("{cariindex} ada pada index ke- {barang.index(cariindex)}")
        else :
            print("index tidak ditemukan!")

    elif perintah == 7 :
        print("Masukkan kembali imputan anda : ")

print(barang)
                   
