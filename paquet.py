from carte import *

class Paquet:

    def __init__(self):
        self.cartes = [Carte(valeur, couleur) for valeur in Carte.valeurs_valides 
            for couleur in Carte.couleurs_valides]

    @property
    def cartes(self):
        return self.__cartes

    @cartes.setter
    def cartes(self, value):
        self.__cartes = value

    def __len__(self):
        return len(self.cartes)

    def __getitem__(self, index:int):
        if index > len(self):
            raise Exception(IndexError)
        return self.cartes[index]


if __name__ == "__main__":
    monPaquet = Paquet()
    #print(monPaquet.cartes)
    print(len(monPaquet))
    print(monPaquet[18])