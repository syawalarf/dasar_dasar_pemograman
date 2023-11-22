#nomer 1
def profil (nama,alamat,jk,umur,hobi):
    print("Nama Saya",nama)
    print("alamat saya berada di",alamat)
    print("kelamin saya",jk)
    print("umur saya", umur)
    print("hoby saya", hobi)
profil("syawal","Bogor","laki-laki","18","berenang")

#nomer 2
def cek_nilai(a):
    if a <= 60:
        return "Gagal"
    elif 61 >= a <= 70:
        return "Baik"
    elif 71 >= a <= 80:
        return "Sangat Baik"
    elif 81 >= a <= 100:
        return "Istimewa"
    else:
        return "nilai eror"

nilai_siswa = float(input("Masukan nilai siswa :"))
hasil = cek_nilai(nilai_siswa)
print(f"Siswa ini {hasil}.")

#nomer 3
def cetak_ganjil(n):
    for i in range(1, 101, 2):
        print(i)

cetak_ganjil(100)