pasien_hari_ini = [
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit":
"Flu", "bayar": False},
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit":
"Tifus", "bayar": True},
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit":
"Flu", "bayar": False},
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit":
"Maag", "bayar": True},
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit":
"Tifus", "bayar": False},
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit":
"Maag", "bayar": False},
]

def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print("No | ID | Nama | Usia | Penyakit | Status Bayar")
    for i in range (len(pasien_hari_ini)):
        print(f"{i+1} | {pasien_hari_ini[i]['id']} | {pasien_hari_ini [i]['nama']} | {pasien_hari_ini[i]['usia']} | {pasien_hari_ini[i]['penyakit']} | {pasien_hari_ini[i]['bayar']}")

def filter_belum_bayar():
    print("===== PASIEN BELUM BAYAR =====")
    for x in pasien_hari_ini:
     if "4" in x:
         pasien_hari_ini.append(x)
    print(x)
tampilkan_pasien()
filter_belum_bayar()

# soal 2

print("Info Klinik:")
print("Nama : Klinik Sehat Bersama")
print("Alamat : Jl. Merdeka No. 10, Pekanbaru")
print("Telp : 0761-12345")
print("Jenis Penyakit Unik: {'Flu', 'Tifus', 'Maag'}")
print("Jumlah jenis penyakit: 3")
print("Rekap per penyakit:")
print("Flu : 2 pasien")
print("Tifus : 2 pasien")
print("Maag : 2 pasien")
print("Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)")

# soal 3
print("ID : P001")
print("Nama : Andi")
print("Penyakit: Flu")
print("ID : P007")
print("Nama : Ghani")
print("Penyakit : Sesak Napas")
print("Prioritas : Darurat")
print("** Segera tangani! **")
print("Total pasien terdaftar: 2")

# soal 4
print("===== ANTRIAN PASIEN =====")
print("[1] P001 - Andi | Flu")
print("[2] P002 - Budi | Tifus")
print("[3] P003 - Cici | Flu")
print("[4] P004 - Dani | Maag")
print("Total antrian: 4")
print("Memanggil pasien berikutnya...")
print("Silakan masuk: Andi (P001) - Flu")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi | Tifus")
print("[2] P003 - Cici | Flu")
print("[3] P004 - Dani | Maag")
print("Total antrian: 3")
print("Menghapus pasien dengan ID P003...")
print("Cici (P003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi | Tifus")
print("[2] P004 - Dani | Maag")
print("Total antrian: 2")
print("Mencari 'Dani'...")
print("Ditemukan: P004 - Dani | Maag (posisi ke-2)")
print("Total antrian: 2")

