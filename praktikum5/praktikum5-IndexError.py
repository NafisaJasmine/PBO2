list_angka = [11, 22, 33]
try:
    value = list_angka[44]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")