class knihy(object): # objekty - knihy a jejich autori
    def __init__(self, jmeno, nazev):
        self.jmeno = jmeno
        self.nazev = nazev
        
    def databaze(self): # detaily
        print ("{} napsal knihu {}.".format(self.jmeno, self.nazev))
 
k1 = knihy("Karel Čapek", "Bílá nemoc")
k1.databaze() # vysledek
k2 = knihy("Paulo Coelho","Alchymista")
k2.databaze()


