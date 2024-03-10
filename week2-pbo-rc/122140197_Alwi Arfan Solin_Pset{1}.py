import random

class Ayah:
    def __init__(self):
        self.alel = None

    def input_alel(self):
        self.alel = input("Masukkan alel Ayah: ").upper()

class Ibu:
    def __init__(self):
        self.alel = None

    def input_alel(self):
        self.alel = input("Masukkan alel Ibu: ").upper()

class Anak(Ayah, Ibu):
    def __init__(self):
        super().__init__()

    def wariskan_alel(self, ayah, ibu):
        self.alel = random.choice(ayah.alel) + random.choice(ibu.alel)
        print("\nAlel anak:", self.alel)
        self.tentukan_golongan_darah()

    def tentukan_golongan_darah(self):
        pemetaan_golongan_darah = {
            "AA": "A",
            "AB": "AB",
            "AO": "A",
            "BB": "B",
            "BO": "B",
            "OO": "O"
        }

        golongan_darah_anak = pemetaan_golongan_darah.get(self.alel, "Tidak Diketahui")
        print("Golongan darah anak:", golongan_darah_anak)

ayah = Ayah()
ayah.input_alel()

ibu = Ibu()
ibu.input_alel()

anak = Anak()
anak.wariskan_alel(ayah, ibu)
