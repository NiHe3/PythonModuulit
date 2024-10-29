class Julkaisu:
    def __init__(self, nimi):
        self.nimi=nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjottaja=kirjoittaja
        self.sivumaara=sivumaara
    def tulosta(self):
        print(f"Kirja{self.nimi} \n Kirjottaja: {self.kirjottaja} \n Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja=toimittaja

    def tulosta(self):
        print(f"Lehti: {self.nimi} \n Päätoimittaja: {self.toimittaja}")
