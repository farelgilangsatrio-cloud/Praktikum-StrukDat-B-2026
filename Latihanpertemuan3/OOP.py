'''
buatlah sebuah class dengan
-minumal 3 atribut/property
# -2 method
'''
class Hewan:
    def __init__(self, nama, tempat, kaki):
        self.nama = nama
        self.tempat = tempat
        self.kaki = kaki

    def Jenis(self):
        print("nama hewan = " + self.nama)
    
    def Hidup(self):
        print("tempat hidup = " + self.tempat)

    def Kelompok(self):
        print("berkaki = " + self.kaki)
    
    def ubah_nama(self, NamaBaru):
        self.nama = NamaBaru
    
hewan1= Hewan("gajah","di darat", "4")
hewan2= Hewan("burung cenderawasih","di udara", "2")
hewan3= Hewan("paus","di air", "tidak berkaki")

hewan1.Jenis()
hewan2.Hidup()
hewan3.Kelompok()

hewan1.ubah_nama("jerapah")
print(hewan1.nama)
