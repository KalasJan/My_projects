# vytvorit vlastni (jednoduchou) kalkulacku

# zadavani cisel
a = float(input("Sem zadejte první číslo: a = "))
b = float(input("Sem zadejte druhe číslo: b = "))

# definujeme 5 zakladnich operaci - scitani, odcitani, nasobeni, deleni, mocnina

def scitani(a, b):
    return a + b

def odcitani(a, b):
    return a - b

def nasobeni(a, b):
    return a * b

def deleni(a, b):
    return a / b

def mocnina(a, b):
    return a ** b

# Výběr operace
print ("Zadejte operaci:")
print ("1 - Součet (a+b)")
print ("2 - Rozdíl, odčítání (a-b)")
print ("3 - Součin, násobení (a*b)")
print ("4 - Podíl, dělení (a/b)")
print ("5 - Mocnění (a^b)")

Vybrana_operace = input("Vybraná operace(1, 2, 3, 4, 5): ")

# Zjištění výsledku

if Vybrana_operace == "1":
    print (a, "+", b, "=", scitani(a, b))
elif Vybrana_operace == "2":
    print (a, "-", b, "=", odcitani(a, b))
elif Vybrana_operace == "3":
    print (a, "*", b, "=", nasobeni(a, b))
elif Vybrana_operace == "4":
    print (a, "/", b, "=", deleni(a, b))
elif Vybrana_operace == "5":
    print (a, "^", b, "=", mocnina(a, b))
else:
    print ("Taková operace neexistuje.")
        
