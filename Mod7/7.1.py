kuukaudet = {3: "kevät", 4: "kevät", 5: "kevät",
            12: "talvi", 1: "talvi", 2: "talvi",
            6: "kesä", 7: "kesä",  8: "kesä",
             9: "syksy", 10: "syksy", 11: "syksy",}
season = int(input("Anna kuukauden numero (1-12)"))
if 1<= season <= 12:
        season = kuukaudet[season]
        print(f"Kuukauden vuodenaika on {season}")
else:
    print("Virhe")