vuosi_str=input("Anna vuosiluku: ")
vuosi=int(vuosi_str)

if vuosi % 4 == 0 and vuosi % 100 != 0 or (vuosi % 400 == 0):
    print(str(vuosi) + " on karkausvuosi")
else:
    print(str(vuosi) + " ei ole karkausvuosi")