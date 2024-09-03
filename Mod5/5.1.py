import random

luvut= []
maara_str = input("Anna arpakuutioiden määrä joita heität")
maara = int(maara_str)

summa = 0
for i in range(maara):
    luku=random.randint(1,6)
    summa=summa+luku
print(summa)