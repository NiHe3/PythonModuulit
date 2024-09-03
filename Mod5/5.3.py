#Tulostaa vain viimeisen luvun
while True:
    alku= input("Syötä kokonaisluku")
    x = 0
    if alku == "":
        break
    Luku=int(alku)
    if Luku < 2:
        x = 0
    else:
        for i in range(2, int(Luku**0.5)+1):
            if Luku % i == 0:
                x= 0
                break
        else:
            x=1
if x==1:
    print(f"{Luku} on alkuluku.")
else:
    print(f"{Luku} ei ole alkuluku")