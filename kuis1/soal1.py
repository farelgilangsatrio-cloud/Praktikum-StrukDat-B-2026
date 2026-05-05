def tambah_buku(nama, harga, stok) :
    if harga <= 0 or stok < 0 :
        print('error dan kembalikan nilai None.')
        return None

    return{
        "nama" : nama,
        "harga": harga,
        "stok" : stok,
    }

toko_buku = []
for i in range(3):
    print(f"masukkan buku ke - {i+1}")
    nama = str(input('masukkan nama buku:'))
    harga = float(input('masukkan harga buku: '))
    stok = int(input('masukkan stok buku: '))

    daftar_buku = tambah_buku(nama, harga, stok)
    if daftar_buku :
        toko_buku.append(daftar_buku)
print(toko_buku)



 