import random

def noppa(tahkotnumero):
     return random.randint(1,tahkotnumero)
def main():
    tahkot = input("Anna nopan tahkojen määrä")
    tahkotnumero = int(tahkot)
    maksimi = input(f"Anna nopan maksimiluku (1-{tahkotnumero})")
    maksimiluku = int(maksimi)

    luku= 0
    while luku !=maksimiluku:
        luku= noppa(tahkotnumero)
        print(f"Nopan luku on: {luku}")
if __name__ == "__main__":
    main()
