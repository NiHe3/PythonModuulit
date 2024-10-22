class Auto:
    def __init__(self, tunnus, hnopeus, nopeus, kmatka):
        self.tunnus = tunnus
        self.hnopeus = hnopeus
        self.nopeus = nopeus
        self.kmatka = kmatka

auto = Auto("ABC-123", 142, 0, 0)
print(f"{auto.tunnus} huippu nopeus on {auto.hnopeus}")
