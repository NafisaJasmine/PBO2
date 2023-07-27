class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
kucing = Kucing("Duyeh", 3)
try:
    print(kucing.jenis)
except AttributeError:
    print("Objek tidak memiliki atribut yang diminta!")