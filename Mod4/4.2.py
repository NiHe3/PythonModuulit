#Traceback TypeError float and str
while True :
    tuuma_str = input("Anna tuumamäärä (negatiivinen lopettaa) ")
    tuuma = float(tuuma_str)
    if tuuma < 0:
        break
    lasku = tuuma * 2.54
    print(lasku + " senttimetriä")