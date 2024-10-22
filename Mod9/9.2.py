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
        print(f"Nopeus on {self.nopeus} km/h")


auto = Auto("ABC-123", 142, 0, 0)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

auto.kiihdyta(-200)
