kelas_A = {"struktur Data","Basis Data","AI","pemrograman web"}
kelas_B = {"struktur Data","machine learning","AI","cloud computing"}

# irisan = kelas_A.intersection(kelas_B)
mata_kuliah = kelas_A & kelas_B
print('mata kuliah kedua kelas')
print(mata_kuliah)

# irisan = kelas_A.difference(kelas_B)
mata_kuliah = kelas_A - kelas_B
print('mata kuliah kelas A')
print(mata_kuliah)

# union = kelas_A.union(kelas_B)
mata_kuliah = kelas_A | kelas_B
print('mata unik yang di ambil oleh kelas A dan B')
print(mata_kuliah)


