class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nykyinen_kerros=alinkerros

    def siirry_kerrokseen(self, siirtyma):
            if siirtyma > self.ylinkerros or siirtyma < self.alinkerros:
              print("error")
              return

            while siirtyma > self.nykyinen_kerros:
                self.kerros_ylos()
            while siirtyma < self.nykyinen_kerros:
                self.kerros_alas()


    def kerros_ylos(self):
        self.nykyinen_kerros+=1
        print(f"kerros ylös: {self.nykyinen_kerros}")


    def kerros_alas(self):
        self.nykyinen_kerros-=1
        print(f"kerros alas: {self.nykyinen_kerros}")

