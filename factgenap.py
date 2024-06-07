def faktorialgenap(jumlah, awal):
    if jumlah == 0:
        return 1
    else:
        return awal * faktorialgenap(jumlah - 1, awal + 2)
print(faktorialgenap(2,2))
