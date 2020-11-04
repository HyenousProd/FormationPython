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
        

if __name__ == "__main__":
    maCarte = Carte("ROI", "COEUR")
    print(maCarte.couleur)
    print(maCarte.points)