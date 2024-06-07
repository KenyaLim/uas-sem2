import re

def cek_password(password):
    if len(password) < 6 or len(password) > 20 or re.search(r'[\s]+', password):
        print('Password tidak valid')
        return

    if re.search(r'[A-z]', password) and re.search(r'\d', password) and re.search(r'\W', password):
        print('Password kuat')
    else:
        print('Password lemah')

cek_password('T3stP4ssw0rd?') # Password kuat
cek_password('AlpRoTid4kSus$hk0q,j4NG4nku4tir12345') # Password tidak valid
cek_password('In1Passwordku') # Password lemah
