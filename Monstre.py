from random import randint

class Monstre:
    
    races = {
            "Ogre": {"pv": 130, "force": 15, "dext": 0.2, "armure": 30, "inventaire":{"or": 50, "dague": 1, "potion": 2, "os de poulet": 2}},
            "Géant": {"pv": 60, "force": 15, "dext": 2, "armure": 5, "inventaire":{"or": 100, "dague": 0, "potion": 0, "os de poulet": 5}},
            "Gorille": {"pv": 90, "force": 20, "dext": 2, "armure": 10, "inventaire":{"or": 75, "dague": 0, "potion": 4, "os de poulet": 1}},
            "Troll": {"pv": 110, "force": 10, "dext": 0.5, "armure": 15, "inventaire":{"or": 25, "dague": 1, "potion": 2, "os de poulet": 3}},
        }
    
    classes = {
            "puissant": {"armes": ["Massue","Poing Américain"]},
            "rapide": {"armes": ["Dague","Couteau"]},
        }
    

    def __init__(self,nom, race, classe):
        self.nom = nom
        self.race = race
        self.classe = classe
        self.pv = Monstre.races[self.race]["pv"]
        self.force = Monstre.races[self.race]["force"]
        self.dext = Monstre.races[self.race]["dext"]
        self.armure = Monstre.races[self.race]["armure"]
        self.lst_armes = Monstre.classes[self.classe]["armes"]

    def get_nom(self):
        return self.nom
        
    def get_race(self):
        return self.race
    
    def get_classe(self):
        return self.classe
    
    def get_force(self):
        return self.force
    
    def get_dext(self):
        return self.dext
    
    def get_pv(self):
        return self.pv
    
    def get_arme(self):
        return self.lst_armes[randint(0,len(self.lst_armes)-1)]
    
    def get_inventaire(self):
        for element, quantite in self.races[self.race]["inventaire"].items():
            print(f"- {quantite}x {element}")

    def decrement_PV(self, valeur):
        self.pv -= valeur
        if self.pv < 0:
            self.pv = 0