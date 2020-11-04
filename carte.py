class InvalidCardValue(ValueError):
    pass

class InvalidCardColor(ValueError):
    pass

class Carte:

    valeurs_valides =  ["AS"] + [str(valeur) for valeur in range (2,11)] + ["VALET", "DAME", "ROI"]
    couleurs_valides = ["TREFLE", "CARREAU", "COEUR", "PIQUE"]

    def __init__(self, valeur, couleur:str):
        self.couleur = couleur
        self.valeur = valeur

    @property
    def valeur(self):
        return self.__valeur

    @property
    def couleur(self):
        return self.__couleur

    @valeur.setter
    def valeur(self, value:str):
        if value not in Carte.valeurs_valides:
            raise InvalidCardValue()
        self.__valeur = value

    @couleur.setter
    def couleur(self, value:int):
        if value not in Carte.couleurs_valides:
            raise InvalidCardColor()
        self.__couleur = value

    @property
    def points(self) -> int:
        return Carte.valeurs_valides.index(self.valeur) + 1

    def __repr__(self):
        return f"<{self.valeur} de {self.couleur}>"

    def __eq__(self, carte2):
        return self.couleur == carte2.couleur and self.valeur == carte2.valeur

    def __iter__(self):
        return iterateur_cartes(self)
        
class iterateur_cartes:

    def __init__(self, carte):
        self.liste_cartes = [Carte(valeur, couleur) for valeur in Carte.valeurs_valides 
            for couleur in Carte.couleurs_valides]
        self.index = self.liste_cartes.index(carte)

    def __next__(self):
        if self.index+1 == len(self.liste_cartes):
            raise StopIteration
        return self.liste_cartes[self.index+1]

    def __iter__(self):
        return self


if __name__ == "__main__":
    maCarte = Carte("ROI", "COEUR")
    print(maCarte.couleur)
    print(maCarte.points)