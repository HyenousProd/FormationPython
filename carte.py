class Carte:

    valeurs_valides =  [str(valeur) for valeur in range (1,11)] + ["Valet", "Dame", "Roi"]
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
    def valeur(self, value:int):
        self.__valeur = value

    @couleur.setter
    def couleur(self, value:int):
        self.__couleur = value

    def points(self) -> int:
        return valeurs_valides.index(self.valeur) + 1


if __name__ == "__main__":
    maCarte = Carte("Roi", 'Coeur')
    print(maCarte.couleur)
    print(maCarte.points())