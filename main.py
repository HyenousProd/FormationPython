from paquet import *
from carte import *
from random import shuffle

p1 = Paquet()
#print(p1)
print(p1[35])
p1[35] = Carte("2", "TREFLE")
print(p1[35])
print(p1[0:5])
shuffle(p1)
print(p1[0:5])

for carte in p1:
    print(carte)

maCarte = Carte("2", "COEUR")
for carte_i in maCarte:
    print(carte_i)