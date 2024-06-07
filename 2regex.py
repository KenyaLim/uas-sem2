import re
text = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)"

y=2024
m=6
d=2

x = (y*365)+(m*30)+(d)
y= re.findall(r'\d{4}-\d{2}-\d{2}', text)
for time in y:
    y,m,d = time.split('-')
    a=(int(y)*365)+(int(m)*30)+(int(d))
    selisih= x-a
    time2 = '-'.join([str(y),str(m),str(d)])
    print(f"{time} 00:00:00 selisih {selisih} hari")
