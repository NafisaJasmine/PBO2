class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def belajar(self):
        print(f"{self.nama} sedang belajar.")

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim

    def membaca(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang membaca.")
    
mhsA = Mahasiswa("Nafisa", 19, "210511041")
mhsA.belajar() # Output: Nafisa sedang belajar.
mhsA.membaca() # Output: Nafisa dengan NIM 210511041 sedang membaca.