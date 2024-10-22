import random
import pandas as pd

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

    def lajittele(self, lista):
        return lista['kmatka']

autot = []
for i in range(1, 11):
    maxnopeus=random.randint(100,200)
    rekkari=f"ABC-{i}"
    kuljettumatka=0
    nopeus=0
    autot.append(Auto(rekkari, maxnopeus, nopeus, kuljettumatka))

kilpailu = True
while kilpailu:
    for auto in autot:
        vauhtimuutos = random.randint(-10, 15)
        auto.kiihdyta(vauhtimuutos)

        auto.kulje(1)

        if auto.kmatka >=10000:
            kilpailu = False
            break

autot.sort(key=lambda auto: auto.kmatka, reverse=True)


for auto in autot:
    print(f'Rekisteri: {auto.tunnus}, Kuljettu matka: {auto.kmatka:.2f} km')