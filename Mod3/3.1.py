
kuha_str = input("Kuhan pituus senttimetreinä?")

kuha=float(kuha_str)

mitta = 37

if kuha <= mitta :
    ali = mitta - kuha
    print("Laske kuha takaisin Kuha on " + str(ali) + " liian pieni")
else:
 print("Kuha on sallitun kokoinen.")