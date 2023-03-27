class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji

    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")

class Dokter:
    def __init__(self, spesialis):
        self.spesialis = spesialis

    def display_info(self):
        print(f"Spesialis: {self.spesialis}")

class DokterPekerja(Orang, Pekerja, Dokter):
    def __init__(self, nama, umur, pekerjaan, gaji, spesialis):
        Orang.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Dokter.__init__(self, spesialis)

    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Spesialis: {self.spesialis}")

# contoh penggunaan
dokter_pekerjaC = DokterPekerja("Anton", 30, "Dokter", "40.000.000", "Bedah")
dokter_pekerjaC.display_info()