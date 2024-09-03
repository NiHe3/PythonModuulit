
def laskin(luvut):
    return sum(luvut)


def main():
    lista=[]
    while True:
        luku = input("Anna lukuja")
        numerot= int(luku)
        if numerot < 0:
            break
        lista.append(numerot)


    summa = laskin(lista)
    print(f"Lukujen summa on: {summa}")
if __name__ == "__main__":
    main()