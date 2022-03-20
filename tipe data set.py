#{}
#sifatnya imutable
#tidak dapat diakses menggunakan index
#random
#nilai yang dimasukkan kedalam variabel tidak boleh sama

#menampung beberapa nilai yang tipe datanya berbeda
set = {"angka",15,2.5,True}
#perulangan loop
for i in (set):
    print(set)
#mengupdate nilai pada set
#set = {"menang"}
#print(set[0])

#menghapus nilai pada set
#remove,discard,clear
#remove
set.remove("angka")
print(set)
#discard
set.discard(2.5)
print(set)
#clear
set.clear()
print(set)

#menambahkan nilai pada set
#add,update
#add
set.add("menang")
print(set)
#update
set.update(["alhamdulillah","yesssssssss"])
print(set)
