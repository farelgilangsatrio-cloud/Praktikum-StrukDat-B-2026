katalog = [
 {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
 {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
 {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

def cari_buku(katalog, keyword):
    hasil_cari = []
    for buku in katalog:
        if keyword in buku:
            hasil_cari.append(buku)
    return hasil_cari

key = input('cari buku: ')
hasil = cari_buku(katalog, key)

if not hasil:
     print("buku tidak di temukan")
else:
     print(hasil)


