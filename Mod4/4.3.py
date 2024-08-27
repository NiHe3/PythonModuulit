lista = []

while True:
    luku_str= input("Anna luku")
    if luku_str == "": break

    luku=float(luku_str)
    lista.append(luku)
suurin = max(lista)
pieni = min(lista)

print("Pienin luku ", pieni)
print("Suurin luku ", suurin)