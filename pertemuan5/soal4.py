transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

transaksi[0] = {"produk": "Buku", "harga": 10000, "jumlah": 3}
print('transaksi')

transaksi.append({"produk":"pensil warna","harga": 5000, "jumlah": 9})
transaksi.append({"produk":"penggaris","harga": 5000, "jumlah": 8})

for x in range(len(transaksi)):
    total = transaksi[x]['harga'] * transaksi[x]['jumlah']
    print(f"produk {transaksi[x]['produk']} | total = {total}")