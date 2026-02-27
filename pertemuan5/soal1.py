nilai_tugas = [70,85,90,65,80]
nilai_tugas.append(75)
nilai_tugas.remove(65)
print(nilai_tugas)

nilai_tugas = [70,85,90,65,80]
nilai_tugas.append(95)
nilai_tugas.sort()
print(nilai_tugas)

nilai_tugas = [70,85,90,65,80]
nilai_tugas.append(75)
nilai_tugas.append(95)
print(nilai_tugas)

total = sum(nilai_tugas)
print('total nilai', total)

if 100 in nilai_tugas:
    print("ada nilai sempurna")
else:
    print('tidak ada')