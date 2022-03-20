#{}
#unordered = tidak berurut
#changeable = bisa berubah
#unique + tidak dapat menerima key yg sama

#membuat program dictionary
dictionary = {"cara" : "belajar python", "sumber" : "jago koding"}
#perulangan
for key in(dictionary):
    print(key,dictionary[key])
#mengupdate nilai pada dictionary
dictionary["cara"] = "belajar program"
print(dictionary)
#menghapus nilai pada dictionary
#pop
dictionary.pop("sumber")
print(dictionary)
#menambah nilai pada dictionary
dictionary["rekomendasi"] = "belajar pemrograman"
print(dictionary)
