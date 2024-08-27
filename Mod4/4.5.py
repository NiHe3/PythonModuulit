
while True :
    Ktunnus=input("Käyttäjätunnus")
    sala=input("salasana")

    if Ktunnus=="python" and sala=="rules":
     print("Tervetuloa")
     break
    elif Ktunnus!="python" or sala!="rules":
        print("Pääsy evätty")
