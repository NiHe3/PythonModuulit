kentat = {}

syote =str(input("Syötä uusi lentoasema(uusi), \nhae syötetty lentoasema ICAO(hae) \nlopetatko ohjelman(lopeta)"))
while True:
    if syote=="lopeta":
        break

    elif syote=="hae":
        icao=str(input("ICAO-koodi?"))
        if icao in kentat:
            print(f"Lentokenttä koodilla {icao} {kentat[icao]}")

    elif syote=="uusi":
        uusiicao=str(input("Icao numero?"))
        uusikentta=str(input("Lentoaseman nimi?"))
        if uusiicao in kentat:
            print(f"Kentän ICAO-koodi on jo tallennettu")
        else:
            kentat[uusiicao]=uusikentta
