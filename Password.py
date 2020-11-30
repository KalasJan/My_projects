# Generator hesla

# Bereme pouze mala a velka pismena, cislice

from random import choice
import string

# kolik znaku ma heslo obsahovat
delka = int(input("Jak dlouhe ma heslo byt? "))

# co by heslo melo obsahovat?
pismena = string.ascii_letters # pokud chceme v hesle mala nebo velka pismena
cislice = string.digits # chceme-li v hesle cislice
symboly = string.punctuation # chceme-li symboly, jako jsou: .,?:"

charakter = pismena + cislice # + symboly
# pokud chci jen pismena, dam jen to, co chci mit v hesle
# nerozlisujeme mala a velka pismena

heslo = []

for p in range (delka):
    heslo.append(choice(charakter))
# pro opakovany vyber podle pozadovane delky hesla
    
print ("Vase heslo je:", "".join(heslo))