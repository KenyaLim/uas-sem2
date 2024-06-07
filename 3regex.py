import random
import re
import string
t = """
     anton@mail.com punya anton
     budi@gmail.co.id punya budi
     slamet@getnda.com punya slamet
     matahari@toped.com punya matahari
     """
def pw(l=8):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for i in range(l))
x = re.findall(r'(\b[\w.-]+)@[\w.-]+',t)
for uname in x:
    pp = pw()
    print(f'{uname}@mail.com username: {uname}, password: {pp}')
