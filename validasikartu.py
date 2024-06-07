import re

def validasi_kartu_kredit(nomor_kartu):
    #valid = re.search('^[4-6]\d{15}$', nomor_kartu)
    valid = re.search(r'^[4-6]\d{15}$', nomor_kartu)
    #valid = re.search()
    if valid:
        plat = re.search('8888', nomor_kartu)
        if plat:
            return ("Valid Platinum")
        else:
            return ("Valid Reguler")
    else:
        return ("Tidak Valid")
    
print(validasi_kartu_kredit('1234567890'))
print(validasi_kartu_kredit('6111111111111111'))
