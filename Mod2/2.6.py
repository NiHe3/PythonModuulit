import random

eka = ""

for i in range(3):
    eka += str(random.randint(0,9))

toka = ""

for i in range(4):
    toka += str(random.randint(1,6))

print(str(eka))
print(str(toka))