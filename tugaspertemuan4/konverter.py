from kurs import kurs

def konversi(dari, ke, jumlah):
    if dari == "IDR":
        hasil = jumlah / kurs[ke]
        return hasil
    if ke == "IDR":
        hasil = jumlah * kurs[dari]
        return hasil
    
    