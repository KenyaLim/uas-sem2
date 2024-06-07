import re
def sensor_komentar(kalimat, terlarang, pengganti):
    if len(terlarang) == 0 and type(pengganti) != list:
        return kalimat
    else:
        if type(pengganti) == str:
            for kata in terlarang:
                if re.search(kata, kalimat):
                    kalimat = re.sub(kata, pengganti, kalimat)
            return kalimat

kalimat = 'jancuk! aku dikibuli toko online.'
terlarang = ['jancuk']
pengganti = 'wkwkwk'
print(sensor_komentar(kalimat, terlarang, pengganti))
