list = ["ainun",72,86.7,True]
#perulangan
for i in (list):
    print(i)
print("===============")
#perulangan while loop
i=0
while i < len(list):
    print(list[i])
    i += 1

#mengupdate nilai
list [0] = "nur ainun"
print(list)

#menghapus nilai
#remove,del,pop
#remove
list.remove("nur ainun")
print(list)
#del
del list [1]
print(list)
#pop
list.pop()
print(list)

#menambahkan nilai
#append,extend,insert
#append
list.append("februari")
print(list)
#extend
list.extend([27.6])
print(list)
#insert
list.insert(2,True)
print(list)
