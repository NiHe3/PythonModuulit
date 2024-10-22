from Kilpailu import Kilpailu
from Auto import Auto
import random

autot = []
for i in range(1, 11):
        maxnopeus=random.randint(100,200)
        rekkari=f"ABC-{i}"
        kuljettumatka=0
        nopeus=0
        autot.append(Auto(rekkari, maxnopeus, nopeus, kuljettumatka))

kilpailu=Kilpailu("Suuri romuralli", 8000, autot)
tunti=0

while True:
    if kilpailu.loppu():
        break
    kilpailu.tunti()
    tunti+=1

    if tunti % 10 == 0:
        print(f"\nTilanne {tunti} h jälkeen")
        kilpailu.tilanne()

    print("\nKilpailu päättyi Lopputilanne:")
    kilpailu.tilanne()