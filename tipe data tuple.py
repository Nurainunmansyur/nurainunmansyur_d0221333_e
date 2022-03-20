#()

tuple =("bilangan",283,7.9,False)
#perulangan
for i in (tuple):
    print(i)
print("======================")
#perulangan while loop
i=0
while i < len(tuple):
    print(tuple)
    i += 1

#mengupdate nilai tuple dengan cara di konversi
tup = list(tuple)
tup [0] = "nilai"
print(tup)

#menghapus nilai pada tuple
#remove, pop
#remove
tup.remove(False)
print(tup)
#pop
tup.pop()
print(tup)

#menambahkan nilai pada tuple
#append,extend, insert
#append
tup.append("angka")
print(tup)
#extend
tup.extend(["sembilan","sepuluh"])
print(tup)
#insert
tup.insert(2,"daftar")
print(tup)
           
