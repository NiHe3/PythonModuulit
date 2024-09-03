luvut = []

while True:
    str= input("Syötä luku")
    if str == "":
        break
    Luku=int(str)
    luvut.append(Luku)

luvut.sort(reverse=True)
for Luku in luvut[:5]:
    print(Luku)