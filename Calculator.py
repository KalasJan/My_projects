# calculator by class method

class kalkulacka(object):
    # definice zadani cisel
    def __init__(self, c1, c2): # c1 - cislo1, c2 - cislo2, na co se odkazuje
        self.c1 = c1
        self.c2 = c2
        
    # definujeme jednotlive operace
    def soucet(self):
        print (self.c1, "+", self.c2, "=", self.c1 + self.c2)
    
    def rozdil(self):
        print (self.c1, "-", self.c2, "=", self.c1 - self.c2)
    
    def soucin(self):
        print (self.c1, "*", self.c2, "=", self.c1 * self.c2)
    
    def podil(self):
        print (self.c1, "/", self.c2, "=", self.c1 / self.c2)
    
    def mocnina(self):
        print (self.c1, "^", self.c2, "=", self.c1 ** self.c2)
    
# priklady
# kolik je 6+3?
p1 = kalkulacka(6, 3) 
p1.soucet()

# kolik je 6-3?
p2 = kalkulacka(6, 3) 
p2.rozdil()

# kolik je 6*3?
p3 = kalkulacka(6, 3) 
p3.soucin()

# kolik je 6/3?
p4 = kalkulacka(6, 3) 
p4.podil()

# kolik je 6^3?
p5 = kalkulacka(6, 3) 
p5.mocnina()