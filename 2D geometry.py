# obsahy a objemy utvaru

from math import sqrt, pi

# vycet utvaru:

print ("Stiskni 't' pro trojuhelnik.")
print ("Stiskni 's' pro ctverec.")
print ("Stiskni 'o' pro obdelnik.")
print ("Stiskni 'k' pro kosoctverec.")
print ("Stiskni 'd' pro kosodelnik.")
print ("Stiskni 'l' pro lichobeznik.")
print ("Stiskni 'c' pro kruh.")
utvar = str (input("Vyber si geometricky utvar: "))

if utvar == "t":
    a = float(input("Zadej 1. delku strany trojuhelnika: "))
    b = float(input("Zadej 2. delku strany trojuhelnika: "))
    c = float(input("Zadej 3. delku strany trojuhelnika: "))
    o = a + b + c
    s = o / 2
    S = sqrt(s*(s-a)*(s-b)*(s-c))
    print ("Obvod trojuhelnika je", o, "jeho obsah je", S)

if utvar == "s":
    strana = float(input("Zadej delku strany ctverce: "))
    print ("Delka strany je", strana, "obvod ctverce je", 4 * strana, "a obsah tohoto ctverce je", strana ** 2)

if utvar == "o":
    a = float(input("Zadej 1. delku strany obdelnika: "))
    b = float(input("Zadej 2. delku strany obdelnika: "))
    print ("Obvod obdelnika je", 2 * (a+b), "jeho obsah je", a * b)

if utvar == "k":
    a = float(input("Zadej delku strany kosoctverce: "))
    v = float(input("Zadej delku vysky kosoctverce: "))
    print ("Obvod kosoctverce je", 2 * (a+b), "jeho obsah je", a * v)
    
if utvar == "d":
    a = float(input("Zadej delku strany kosodelniku: "))
    v = float(input("Zadej delku vysky kosodelniku: "))
    print ("Obvod kosoctverce je", 2 * (a+b), "jeho obsah je", a * v)

if utvar == "l":
    a = float(input("Zadej delku 1 zakladny lichobeznika: "))
    b = float(input("Zadej delku 2. zakladny lichobeznika: "))
    v = float(input("Zadej vysku lichobeznika: "))
    pr = (a+c)/2
    S = (a+c)*v/2
    print ("Stredni pricka lichobeznika je", pr, "jeho obsah je", S)

if utvar == "c":
    r = float(input("Zadej polomer kruhu: "))
    o = 2 * pi * r
    S = pi * r **2
    print ("Obvod kruhu je", o, "jeho obsah je", S)
    