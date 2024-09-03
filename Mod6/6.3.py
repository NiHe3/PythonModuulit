#Indent <3
def laskin(gallona):
    return gallona * 3.785


def main():
    while True:
        maara=input("Anna gallonan määrä")
        gallona=float(maara)
        if gallona < 0:
            break
        litra = laskin(gallona)
        print(f"{gallona} galloonaa on {litra} litraa")

if __name__ == "__main__":
    main()