class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Mamalia:
    def __init__(self, jenis, kembangbiak):
        self.jenis = jenis
        self.kembangbiak = kembangbiak

    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Berkembang Biak: {self.kembangbiak}")


class Kucing(Mamalia):
    def __init__(self, nama, umur, jenis, kembangbiak):
        Hewan.__init__(self, nama, umur)
        Mamalia.__init__(self, jenis, kembangbiak)

    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jenis: {self.jenis}")
        print(f"Berkembang Biak: {self.kembangbiak}")
        
# contoh penggunaan
kucingA = Kucing("Kucing Persia", 2, "Mamalia", "Melahirkan")
kucingA.display_info()