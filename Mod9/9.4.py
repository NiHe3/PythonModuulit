import random
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

autot = []
for i in range(1, 11):
    maxnopeus=random.randint(100,200)
    rekkari=f"ABC-{i}"

kilpailu = True
while kilpailu:
    for auto in autot:
        vauhtimuutos = random.randint(-10, 15)
        auto.kiihdyta(vauhtimuutos)

        auto.kulje(1)

        if auto.kmatka >=10000:
            kilpailu = False
            break
