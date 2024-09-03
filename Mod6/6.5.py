
def laskin(luvut):
    parilliset = [luku for luku in luvut if luku % 2 == 0]
    return parilliset


def main():
    lista=[]
    while True:
        luku = input("Anna lukuja")
        numerot= int(luku)
        if numerot <= 0:
            break
        lista.append(numerot)

    parillisetlista=laskin(lista)
    print(f"Alkuperäinen lista: {lista}")
    print(f"Parilliset annetut luvut: {parillisetlista}")
if __name__ == "__main__":
    main()