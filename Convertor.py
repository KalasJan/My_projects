# Prevodnik jednotek
 
volba = input ("Co chcete prevest? Vzdalenost, teplotu, rychlost? ")

while volba == "vzdalenost":
    distance = input ("Chcete prevest km na mile nebo mile na km? ")
    if distance == "km na mile":
        dk = float(input("Jakou vzdalenost v km chcete prevest na mile: "))
        Km_Mil = round(dk * 0.62137, 2) # prevod km na mile
        print ("Vzdalenost", dk, "km je", Km_Mil , "mil.", end="")
    else:
        dm = float(input("Jakou vzdalenost v mil chcete prevest na km: "))
        Mil_Km = round(dm * 1.609, 2) # prevod mile na km
        print ("Vzdalenost", dm, "mil je", Mil_Km , "km.", end="")
    break      
    
while volba == "teplota":
    stupnice = input ("Chcete prevest °C na F nebo F na °C? ")
    if stupnice == "C na F":
        CF = float(input("Jakou teplotu v °C chcete prevest na F: "))
        prevodCF = round(9/5 * CF + 32, 2) # prevod C na F
        print ("Teplota", CF, "°C je", prevodCF , "F.", end="")
    else:
        FC = float(input("Jakou teplotu v F chcete prevest na °C: "))
        prevodFC = round(5/9 * FC - 32, 2) # prevod F na C
        print ("Teplota", FC, "F je", prevodFC , "°C.", end="")
    break
    
while volba == "rychlost":
    speed = input("Chcete prevod km/h na mph nebo mph na km/h? ")
    if speed == "kmh na mph":
        kmh = float(input ("Jakou rychlost v km/h chcete prevest? "))
        kmhMPH = round(0.621 * kmh, 2) # prevod kmh na mph (miles per hour)
        print ("Rychlost", kmh, "km/h je", kmhMPH, "mph.")
    else:
        mph = float(input ("Jakou rychlost v mph chcete prevest? "))
        mphKMH = round(1.609 * mph, 2) # prevod mph (miles per hour) na km/h
        print ("Rychlost", mph, "mph je", mphKMH, "km/h.")
    break