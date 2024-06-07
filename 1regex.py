import re
txt = "Sang mata-mata sedang memata-matai kasus kaca mata di toko Matahari"
x = re.findall("mata", txt)
y = re.findall("saya", txt)
for i in x:
    print(i)
if (y):
    print("Ada yang cocok!")
else:
    print("Tidak ada yang cocok!") 
