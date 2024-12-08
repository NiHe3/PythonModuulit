import requests


avain ="76c21e8be95b7179a44459cfe09d13e3"

pyynto = f"http://api.openweathermap.org/data/2.5/weather?"

kysely = input(str("Minkä paikkakunnan sään haluat nähdä?"))


def kelvin(k_temp):
    return k_temp - 273.15

def haku(kunta):
    parametri = {
        ""
    }