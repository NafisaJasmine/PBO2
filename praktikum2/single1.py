class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bertelur(self):
        print(self.nama, "bertelur")

class ayam(Hewan):
    def __init__(self, nama, umur, jenis):
        super().__init__(nama, umur)
        self.jenis = jenis

    def bersuara(self):
        print("Petok!")
        
ayamA = ayam("Ayam", 1, "Bangkok")
ayamA.bertelur() # output: Ayam bertelur
ayamA.bersuara() # output: Petok!