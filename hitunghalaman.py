def hitung_total_halaman(buku, pilihan):
    buku_dict = dict(buku)
    total_halaman = 0
    for index in pilihan:
        if 0 <= index < len(buku):
            judul = buku[index][0]
            total_halaman += buku_dict[judul]
    return total_halaman

buku = [
    ('Harry Potter', 350), ('Sherlock Holmes', 300), ('The Hobbit', 330),
    ('1984', 250), ('To Kill a Mockingbird', 200), ('The Great Gatsby', 180), ('Moby Dick', 270)
]
pilihan = [0, 1, 2]  # Harry Potter, Sherlock Holmes, The Hobbit => 350 + 300 + 330 = 980
print(hitung_total_halaman(buku, pilihan))  # Output: 980

buku = [
    ('Harry Potter', 350), ('Sherlock Holmes', 300), ('The Hobbit', 330),
    ('1984', 250), ('To Kill a Mockingbird', 200), ('The Great Gatsby', 180), ('Moby Dick', 270)
]
pilihan = [6, 0, 1, 3]  # Moby Dick, Harry Potter, Sherlock Holmes, 1984 => 270 + 350 + 300 + 250 = 1170
print(hitung_total_halaman(buku, pilihan))  # Output: 1170
