import random
numero= random.randint(1,10)
while True :
    arvaus=input("arvaa numero 1 ja 10 välillä")
    arvaus=int(arvaus)
    if arvaus==numero:
        print("Oikein")
        break
    elif arvaus>numero:
        print("Liian suuri arvaus")
    elif arvaus<numero:
        print("Liian pieni arvaus")