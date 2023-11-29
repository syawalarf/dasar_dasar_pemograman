# Nomer 1
hasil_akhir = [
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]

lulus = []
for siswa in hasil_akhir:
    if siswa['nilai'] > 65:
        lulus.append(siswa['nama'])

print(lulus)

# Nomer 2
# balik = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
# balik_baru = []
# for i in range(len(balik)):
#         balik_baru.insert(0, balik[i])
# print(balik_baru)

# Nomer 3
# duplikasi = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
# duplikat = []
# for i in range(len(duplikasi)):
#         duplikat.extend([duplikasi[i], duplikasi[i]])
# print(duplikat)

# Nomer 4
# nama = "nurul fikri"
# konsonan = 'bcdfghjklmnpqrstvwxyz'
# string_baru = ''

# for karakter in nama:
#     if karakter in konsonan:
#         string_baru += karakter

# print(string_baru)

# Nomer 4 alternatif
# nama = 'Nurul Fikri'
# print(nama.replace('u','').replace('i','').replace(' ',''))