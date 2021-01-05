# kostky

# mame 2 kostky, na kazde muze padnout nahodne cislo 1-6
# hra pokracuje, pokud padnou na obou kostkach stejne cislo nebo soucet je vyssi nez 7

from random import randint

dalsihod = "ano"

while dalsihod == "ano":
    k1 = randint(1,6)
    k2 = randint(1,6)
    
    print ("Padlo ti", k1, "a", k2)
    dalsihod = input("Chces hazet znovu? ano/ne" )
    