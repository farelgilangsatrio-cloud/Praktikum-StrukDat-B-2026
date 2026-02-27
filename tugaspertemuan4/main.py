from tabulate import tabulate
from kurs import kurs
from konverter import konversi

data = []
for kode in kurs:
    data.append([kode, kurs[kode]])

print("=== KONVERTER MATA UANG ===")
print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

dari = input("Dari (IDR/USD/EUR/SGD/JPY):").upper()
ke = input("Ke  (IDR/USD/EUR/SGD/JPY):").upper()
jumlah = float(input("Jumlah: "))

hasil = konversi(dari, ke, jumlah)
jumlah_format = f"{jumlah:,.0f}".replace(",", ".")
print(f"Rp {jumlah_format} = {hasil:.2f} {ke}")

