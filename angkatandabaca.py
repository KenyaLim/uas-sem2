import re

def ganti_angka_dan_tandabaca(kalimat):
    if len(kalimat) > 0:
        kalimat = re.sub(r'[^\w\s]', '@', kalimat)
        kalimat = re.sub(r'\d', '#', kalimat)
        return kalimat
    else:
        return kalimat

# Contoh penggunaan
kalimat = "Pada tahun 2024, harga 1 Bitcoin mencapai $30.000!"
print(ganti_angka_dan_tandabaca(kalimat)) 
