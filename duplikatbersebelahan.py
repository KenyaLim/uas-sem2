import re
def hapus_duplikat_bersebelahan(data):
    if not data:
        return ()
    
    new_data = [data[0]]
    for i in range(1, len(data)):
        if data[i] != data[i - 1]:
            new_data.append(data[i])
    
    return tuple(new_data)

# Contoh penggunaan
data = (1, 1, 2.0, 'hello', 'hello', 3.5, 3.5, True, True, False, 'world', 'world')
print(hapus_duplikat_bersebelahan(data))
