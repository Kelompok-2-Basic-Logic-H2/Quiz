# No 1

nama = input("Masukkan nama: ")
nim = int(input("Masukkan NIM: "))
nilai = int(input("Masukkan Nilai: "))

if nilai == 100 :
    grade = "S"
elif nilai <= 99 and nilai >= 85 :
    grade = "A"
elif nilai <= 84 and nilai >= 75 :
    grade = "B" 
elif nilai <= 74 and nilai >= 60 :
    grade = "C" 
elif nilai <= 59 and nilai >= 50 :
    grade = "D" 
elif nilai <= 49 and nilai >= 1 :
    grade = "E"
elif nilai == 0 :
    grade = "F"
else:
    grade = "Tidak Valid"
    
print("Nama: ", nama)
print("NIM: ", nim)
print("Grade: ", grade)


# No 2

panjang = int(input("Masukkan nilai panjang: "))
lebar = int(input("Masukkan nilai lebar: "))
tinggi = int(input("Masukkan nilai tinggi: "))


volume = panjang * lebar * tinggi

print("Volume Balok = ", volume)