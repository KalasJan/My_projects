# V prosincové výzvě uběhni 1 - 24 km od 1/12 do 24/12, každou vzdálenost pouze 1.
# Výstup: Dnes "datum" ubehni "vybrany pocet" km.

Vyber = (
        1, 2, 3, 
        4, 5, 6, 
        7, 8, 9, 
        10, 11, 12, 
        13, 14, 15, 
        16, 17, 18, 
        19, 20, 21, 
        22, 23, 24
        )

# volba

from random import choice 

y = choice(Vyber)

# datum 

import datetime 

x = datetime.datetime.now()

den = x.strftime("%A") # den v tydnu
datum = x.strftime("%d") # datum
mesic = x.strftime("%m") # mesic

print ("Dnes v", den, datum,"/", mesic, "uběhni celkem", y, "km." )