# SOAL 1

kendaraan = ["zx25r", "Motor", "250cc, 2"] 
kendaraan.append ("rp.120.000.000")
kendaraan.append ("manual")
kendaraan.insert (2,"kawasaki")
print(kendaraan)

# SOAL 2

pesan = """
menu:
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
pilih menu:
"""
pilihan=input(pesan)

match pilihan:
    case "1":
        print("anda memasukan angka 1 untuk menghitung luas persegi")
        sisi=int(input("masukan sisi:"))
        luas=sisi*sisi
        print("luas persegi dengan sisi",sisi,"adalah",luas)
    case "2":
        print("anda memasukan angka 2 untuk menghitung luas lingkaran")
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas1 = 3.14 * (r * r)
        print("luas lingkaran dengan jari-jari",r,"adalah",luas1)
    case "3":
        print("anda memasukan angka 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("masukan tinggi: "))
        luas2 = int(1/2*(alas*tinggi))
        print("luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah",luas2) 
    case "4":
        print("anda memasukan selain 1,2,3 salah input")
