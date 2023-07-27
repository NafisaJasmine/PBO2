class musik :
    def __init__(self, lagu, penyanyi) -> None:
        self.penyanyi = penyanyi
        self.lagu = lagu
        print(self.lagu, ",oleh :", self.penyanyi)

class penyanyi:
    def __init__(self) -> None:
        self.nama = []

    def add_nama(self, nama):
        self.nama.append(nama)

class karya:
    def __init__(self,penyanyi):
        self.penyanyi = penyanyi

musik1 = musik ("Nafisa Nurul Jasmine","Aaaaaaaa")
writer = penyanyi()
writer.add_nama(musik1)
create = karya(writer)
create.penyanyi.nama