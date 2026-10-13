print("=== Alat Hitung Luas Bangun Datar ===")

print("Pilih 1 untuk menghitung luas persegi")
print("Pilih 2 untuk menghitung luas lingkaran")
print("Pilih 3 untuk menghitung luas segitiga")

pilihan = int(input("Masukkan pilihan (1/2/3) : "))

match pilihan:
    case 1:
        s = int(input("Masukkan panjang sisi persegi : "))
        luas = s * s
        print(f"Luas persegi adalah : {luas}")
    case 2:
        r = int(input("Masukkan jari jari lingkaran : "))
        pi = 3.14
        luas = pi * r ** 2
        print(f"Luas Lingkaran : {luas}")
    case 3:
        alas = int(input("Masukkan alas segitiga  : "))
        tinggi = int(input("Masukkan tinggi segitiga : "))
        luas = alas * tinggi / 2 
        print(f"Luas Segitiga : {luas}")
    case _:
        print(f"Masukkan pilihan dengan benar ")