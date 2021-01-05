# hra se 6 kostkami

# hra se sklada ze 6 kol. V prvnim kole hazime 6 kostkami, v dalsim 5 kostkami,... v poslednim hodu mame jen 1 kostku
# hru muzeme po jakemkoliv kole ukoncit
# po kazdem kole se dane hodnoty sectou, cilem je hodit nahodne vygenerovane cislo
# cilove cislo je v rozmezi 21 (padnou pouze hodnoty 1) po 126 (padnou jen hodnoty 6)

from random import randint

minimum = (6+5+4+3+2+1) # padnou pouze hodnoty 1
maximum = 6*6+5*6+4*6+3*6+2*6+1*6

cil = randint(minimum,maximum)
print ("Hrajeme na celkovy soucet", cil)

# kolo1
print ("Nyni hazime ze vsemi 6 kostkami")
k1c1 = randint (1,6)
k1c2 = randint (1,6)
k1c3 = randint (1,6)
k1c4 = randint (1,6)
k1c5 = randint (1,6)
k1c6 = randint (1,6)

print ("V prvnim kole padlo:", k1c1, k1c2, k1c3, k1c4, k1c5, k1c6)
soucet1 = k1c1 + k1c2 + k1c3 + k1c4 + k1c5 + k1c6
print ("Celkovy soucet je", soucet1)
if soucet1 > cil:
    print ("Konec hry")
else:
    volba = input ("Chcete pokracovat? a/n")

# kolo2
if volba == "a":
    print ("Druhe kolo. Nyni hazime s 5 kostkami.") 
    k2c1 = randint (1,6)
    k2c2 = randint (1,6)
    k2c3 = randint (1,6)
    k2c4 = randint (1,6)
    k2c5 = randint (1,6)
    
    print ("Ve druhem kole padlo:", k2c1, k2c2, k2c3, k2c4, k2c5)
    soucet2 = k2c1 + k2c2 + k2c3 + k2c4 + k2c5
    print ("Ve druhem kole padlo", soucet2)
    print ("Celkovy soucet je", soucet1 + soucet2)
    if soucet1 + soucet2 > cil:
        print ("konec hry")
    else:
        volba2 = input ("Chcete pokracovat? a/n")
else:
    print ("Konec hry")
    
# kolo3
if volba2 == "a":
    print ("Treti kolo. Nyni hazime se 4 kostkami.") 
    k3c1 = randint (1,6)
    k3c2 = randint (1,6)
    k3c3 = randint (1,6)
    k3c4 = randint (1,6)
    
    print ("Ve tretim kole padlo:", k3c1, k3c2, k3c3, k3c4)
    soucet3 = k3c1 + k3c2 + k3c3 + k3c4 
    print ("Ve tretim kole padlo", soucet3)
    print ("Celkovy soucet je", soucet1 + soucet2 + soucet3) 
    if soucet1 + soucet2 + soucet3 > cil:
        print ("konec hry")
    else:
        volba3 = input ("Chcete pokracovat? a/n")
else:
    print ("Konec hry")

# kolo4
if volba3 == "a":
    print ("Ve 4. kole jsou uz jen 3 kostky.") 
    k4c1 = randint (1,6)
    k4c2 = randint (1,6)
    k4c3 = randint (1,6)

    print ("Ve ctvrtem kole padlo:", k4c1, k4c2, k4c3)
    soucet4 = k4c1 + k4c2 + k4c3 
    print ("Ve tretim kole padlo", soucet4)
    print ("Celkovy soucet je", soucet1 + soucet2 + soucet3 + soucet4) 
    if soucet1 + soucet2 + soucet3 + soucet4 > cil:
        print ("konec hry")
    else:
        volba4 = input ("Chcete pokracovat? a/n")
else:
    print ("Konec hry")
    
# kolo5
if volba3 == "a":
    print ("Predposledni, pate kolo a zbyvaji 2 kostky.") 
    k5c1 = randint (1,6)
    k5c2 = randint (1,6)

    print ("V patem kole padlo:", k5c1, k5c2)
    soucet5 = k5c1 + k5c2
    print ("Ve tretim kole padlo", soucet5)
    print ("Celkovy soucet je", soucet1 + soucet2 + soucet3 + soucet4 + soucet5) 
    if soucet1 + soucet2 + soucet3 + soucet4 + soucet5 > cil:
        print ("konec hry")
    else:
        volba5 = input ("Chcete pokracovat? a/n")
else:
    print ("Konec hry")

# kolo6 a poseldni
if volba5 == "a":
    print ("Posledni, kolo 6 a posledni 1 kostka.") 
    k6c1 = randint(1,6)

    print ("V poslednim kole padlo:", k6c1)
    soucet6 = k6c1
    print ("Celkovy soucet je", soucet1 + soucet2 + soucet3 + soucet4 + soucet5 + soucet6) 
    if soucet1 + soucet2 + soucet3 + soucet4 +soucet5 + soucet6 > cil:
        print ("konec hry")
    else:
        print ("Cíl byl", cil, "ziskal jste", soucet1 + soucet2 + soucet3 + soucet4 +soucet5 + soucet6)