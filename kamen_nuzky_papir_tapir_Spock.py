# Hrajeme "kamen - papir - nuzky" rozsirenou o "tapis - Spock" (viz Teorie velkeho tresku)
# pro zjednoduseni k = kamen, p = papir, n = nuzky, t = tapir, s = Spock
# k>n, n>p, p>k, k>t, t>s, s>n, n>t, t>p, p>s, s>k
# hrajeme "ja vs PC". kde PC si nahodne vybere jednu moznost (k,p,n,t,s), ja tez.

k = 1
p = 2
n = 3 
t = 4
s = 5 # konkretnim moznoste jsme priradili ciselne hodnoty

from random import randint

pc = randint(1, 5)
ja = int(input("Zadej cislo mezi 1 - 5:"))


# co vybral souper
if pc == 1:
    print ("PC vybral kamen.")
elif pc == 2:
    print ("PC vybral papir.")
elif pc == 3:
    print ("PC vybral nuzky.") 
elif pc == 4:
    print ("PC vybral tapira.")
else:
    print ("PC vybral Spocka.")

# vybiram ja:
if ja == 1:
    print ("Vybral jsem kamen.")
elif ja == 2:
    print ("Vybral jsem papir.")
elif ja == 3:
    print ("Vybral jsem nuzky.")
elif ja == 4:
    print ("Vybraj jsem tapira.")
else: 
    print ("Vybral jsem Spocka.")
    

# generujeme uz vysledky hry
if pc == ja:
    print ("Vysledek hry - remiza.")
elif (pc == 1 and ja == 3 or ja == 5) or (pc == 2 and ja == 1 or ja == 5) or (pc == 3 and ja == 2 or ja == 4) or (pc == 4 and ja == 2 or ja == 5) or (pc == 5 and ja == 1 or ja == 3):
    print ("Vysledek hry - PC vyhral.")
else:
    print ("Vysledek hry - ja jsem vyhral")
        
    

