import re

def cek_kodepos(kodePos):
    a = re.search(r'^[1-9][\d]{4}$', kodePos)
    b = re.findall(r'(\d)(?=\d\1)', kodePos)
    
    if a and len(b) < 2:
        print("Valid")
    else:
        print("Tidak Valid")

(cek_kodepos('12145'))  # Valid
(cek_kodepos('32432'))  # Valid
(cek_kodepos('55252'))  # Tidak Valid
(cek_kodepos('55511'))  # Valid
(cek_kodepos('55155'))  # Valid
