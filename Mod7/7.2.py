
luettelo = set()

while True:
    nimi = str(input("Syötä nimi"))
    if nimi == "":
        for nimi in luettelo:
            print(nimi)
        break
    elif nimi in luettelo:
        print(f"Aiemmin syötetty nimi")
    else:
        print(f"Uusi nimi")
        luettelo.add(nimi)
