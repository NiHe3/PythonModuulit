class Auto:
    def __init__(self, tunnus, hnopeus):
        self.tunnus = tunnus
        self.hnopeus = hnopeus
        self.nopeus = 0
        self.kmatka = 0

    def kiihdyta(self, kiihdytä):
        uusinopeus=self.nopeus + kiihdytä
        if uusinopeus > self.hnopeus:
            self.nopeus = self.hnopeus
        elif uusinopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus=uusinopeus

    def kulje(self, tunti):
        matkalisaus=self.nopeus*tunti
        self.kmatka+=matkalisaus

    def lajittele(self, lista):
        return lista['kmatka']

class Sahkoauto(Auto):
    def __init__(self, tunnus, hnopeus, akku):
        super().__init__(tunnus, hnopeus)
        self.akku = akku

class Polttomootoriauto(Auto):
    def __init__(self, tunnus, hnopeus, tankinkoko):
        super().__init__(tunnus, hnopeus)
        self.tankinkoko = tankinkoko