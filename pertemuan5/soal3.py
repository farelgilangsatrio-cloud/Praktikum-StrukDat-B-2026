sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

nama_mahasiswa = sesi_pagi & sesi_siang
print('nama mahasiswa yang hadir di kedua sesi')
print(nama_mahasiswa)

daftar_mahasiswa = sesi_pagi | sesi_siang
print('daftar nama unik yang hadir hari itu')
print(daftar_mahasiswa)

sesi_hari_ini =sesi_pagi.union(sesi_siang)
print('sesi hari')
print(sesi_hari_ini)