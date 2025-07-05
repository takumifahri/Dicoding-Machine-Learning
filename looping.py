#  For 
"""
    For merupakan salah satu keyword untuk pengulangan pada python dimana yang bersifat definite iteration
    yang artinya sebuah proses iterasi atau perulangan yg sudah diketuhi jumlahnya atau di deklarasikan sebelumnya. Biasanya bsia berupa
    variable, list, tuple, dictionary, set, string, atau range.
"""

# COntoh 1
for i in range(20):
    print(i) # ini akan membuat vertical hasilnya dari 0 sanpai 19

# Contoh 2
var_contoh = [1,2,3,4,5,6,7,8,9,10]
for i in var_contoh:
    print(i) # ini akan membuat vertical hasilnya dari 1 sampai 10


"""
    Range merupakan salah satu fungsi bawaan python yang digunakan untuk membuat sebuah iterable object yang berisi
    deretan angka. Fungsi ini sering digunakan dalam perulangan (looping) untuk menghasilkan urutan angka tertentu.

    Rumus Range 
    range(start, stop, step)
    - start: Angka awal dari deretan (default adalah 0).    
    - stop: Angka akhir dari deretan (tidak termasuk angka ini).
    - step: Langkah atau interval antar angka dalam deretan (default adalah 1).
"""

# Contoh 3
for i in range(2, 10, 2):
    print(i) # ini akan membuat vertical hasilnya dari 2 sampai 8 dengan interval 2


# WHILE
