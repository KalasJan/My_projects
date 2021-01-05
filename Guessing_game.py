# hádací hra

# hadame cislo od 1 do 10, mame celkem 3 pokusu

from random import randint

pokus = 3
while pokus > 0:
    typ = int(input("Hledane cislo mezi 1 a 10 je:" ))
    cislo = randint(1, 10) 
    
    if typ > cislo:
        print ("Hledane cislo je mensi.")
        pokus -= 1
    elif typ < cislo:
        print ("Hledane cislo je vetsi.")
        pokus -= 1
    else:
        print ("Uhadl jsi to")
        print ("Gratulace")
        pokus = 0
        
    if pokus == 2:
        print ("Mas jeste", pokus, "pokusu.")
    elif pokus == 1:
        print ("Tohle je posledni pokus.")
    else:
        print ("Neuhadl jsi. Priste hodne stesti.")