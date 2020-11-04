from carte import *
from paquet import *

c1 = Carte("DAME", "COEUR")
print(c1)
c1.valeur = "ROI"
print(c1)

p1 = Paquet()
#print(p1.cartes)
print(p1[35])
shuffle(p1)