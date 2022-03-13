#percabangan
#fungsi IF
nilai = 50
if nilai > 45 :
    print(nilai)

#fungsi IF ELSE
nilai = 75
if nilai > 75 :
    print(lulus)
if nilai < 75 :
    print(tidak_lulus)

#fungsi IF ELIF ELSE
nilai = int(input("masukkan nilai siswa : "))
if nilai >= 85 :
    print("A/memuaskan", nilai)
elif nilai >= 75 :
    print("B/Bagus", nilai)
elif nilai >= 65 :
    print("C/Cukup", nilai)
elif nilai >= 55 :
    print("D/Kurang", nilai)
else :
    print("E/Sangat Kurang", nilai)
