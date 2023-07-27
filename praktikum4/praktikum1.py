class Peneliti:
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul
        
class Jurnal:
    def __init__(self,nama, peneliti) -> None:
        self.nama = nama
        self.peneliti= peneliti

    def judul_jurnal(self):
        for peneliti in self.peneliti:
            print(peneliti.nama, peneliti.judul)

penelitiA = Peneliti("Nafisa Nurul Jasmine :", "Kesalahpahaman antar kucing")
penelitiB = Peneliti("Duyeh :", "Memahami bahasa kucing yang baik")
judul = Jurnal("Jurnal harian",[penelitiA, penelitiB])
judul.judul_jurnal()