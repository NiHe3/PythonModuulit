from Auto import Auto
import random

class Kilpailu:
    def __init__(self, nimi, kilometrimaara, autolista):
        self.nimi = nimi
        self.kilometrimaara = kilometrimaara
        self.autolista = autolista

    def tunti(self):
        for auto in self.autolista:
            Auto.kiihdyta(self, random.randint(-10, 15))
            Auto.kulje(1)
    def tilanne(self):
        print(f"{'Auto':<15}{'Nopeus (km/h)':<15}{'Kuljettu matka (km)':<20}")
        print("=" * 50)
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15}{auto.kuljettu_matka:<20}")

    def loppu(self):
        for auto in self.autolista:
            if auto.kmatka >= self.kilometrimaara:
                return True
            return False