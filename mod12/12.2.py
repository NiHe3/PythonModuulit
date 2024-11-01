import requests
import json

kysely = input(str("Minkä paikkakunnan sään haluat nähdä?"))
avain ="76c21e8be95b7179a44459cfe09d13e3"
pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={kysely}&appid={avain}"
vastaus = requests.get(pyyntö).json()
teksti = str(vastaus)
print(teksti)
