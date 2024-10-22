class Auto:
    def __init__(self, tunnus, hnopeus, nopeus, kmatka):
        self.tunnus = tunnus
        self.hnopeus = hnopeus
        self.nopeus = nopeus
        self.kmatka = kmatka

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

auto = Auto("ABC-123", 142, 0, 2000)

auto.kiihdyta(60)
print(auto.kmatka)
auto.kulje(1.5)
print(auto.kmatka)