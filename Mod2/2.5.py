import math

levi_str= input("Anna leiviskät. ")
naula_str= input("Anna naulat. ")
luoti_str=input("Anna luodit. ")
LG= 13.3
naula_l = 32
levi_naula = 20

levi=float(levi_str)
naula=float(naula_str)
luoti=float(luoti_str)

lasku =(levi * levi_naula* naula * naula_l) + (naula * naula_l * levi_naula ) + luoti
G = lasku * LG

kg =int(G //1000)
jakojaannos = G % 1000

print("Massa nykymittojen mukaan: ")
print(str(kg) +" kilogrammaa ja  "+ str(jakojaannos) +" grammaa")
