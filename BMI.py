# BMI kalkulacka

vaha = int(input("Sem zadejte vahu v kg (napr. 75 kg): "))
vyska = float(input("Sem zadejte vysku v m (napr. 1.8 m), pouzivejte desetinnou tecku: "))
BMI = round((vaha)/(vyska**2), 2)

if BMI < 18.5:
    print ("Vase BMI je", BMI, "tedy podvaha.")
elif 18.5 <= BMI <= 24.99:
    print ("Vase BMI je", BMI, "tedy norma.")
elif 25 <= BMI <= 29.99:
    print ("Vase BMI je", BMI, "tedy mirna nadvaha.")
elif 30 <= BMI <= 34.99:
    print ("Vase BMI je", BMI, "tedy mirna obezita.")
elif 35 <= BMI <= 39.99:
    print ("Vase BMI je", BMI, "tedy stredni obezita.")
else:
    print ("Vase BMI je", BMI, "tedy silna obezita.")