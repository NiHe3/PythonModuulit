spuoli = input("Oletko mies vai nainen")
Harvo_str =input("Hemoglobiiniarvo?")
Harvo=float(Harvo_str)

if (spuoli == "mies" and Harvo<=134 and Harvo>=195):
    print("Hemoglobiini arvo on normaali")
elif (spuoli == "mies" and Harvo>=195):
    print("Hemoglobiini arvo on Korkea")
elif (spuoli == "mies" and Harvo<=134):
    print("Hemoglobiini arvo on alhainen")

if (spuoli == "nainen" and Harvo <= 117 and Harvo >= 175):
    print("Hemoglobiini arvo on normaali")
elif (spuoli == "nainen" and Harvo >= 175):
    print("Hemoglobiini arvo on Korkea")
elif (spuoli == "nainen" and Harvo <= 117):
    print("Hemoglobiini arvo on alhainen")