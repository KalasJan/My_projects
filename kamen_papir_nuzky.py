# Hrajeme "kamen - papir - nuzky"
# pro zjednoduseni k = kamen, p = papir, n = nuzky
# k>n, n>p, p>k
# hrajeme "ja vs PC". kde PC si nahodne vybere jednu moznost (k,p,n), ja tez.

k = 1
p = 2
n = 3 # konkretnim moznoste jsme priradili ciselne hodnoty

from random import randint

pc = randint(1, 3)
ja = int(input("Zadej cislo 1, 2, nebo 3:"))

# co vybral souper
if pc == 1:
    print ("PC vybral kamen.")
elif pc == 2:
    print ("PC vybral papir.")
else:
    print ("PC vybral nuzky.") 

# vybiram ja:
if ja == 1:
    print ("Vybral jsem kamen.")
elif ja == 2:
    print ("Vybral jsem papir.")
else:
    print ("Vybral jsem nuzky.") 

# generujeme uz vysledky hry
if pc == ja: 
    print ("Vysledek hry - remiza.")
elif pc == 1 and ja == 3 or pc == 2 and ja == 1 or pc == 3 and ja == 2:
    print ("Vysledek hry - PC vyhral.")
else:
    print ("Vysledek hry - ja jsem vyhral.")
        






