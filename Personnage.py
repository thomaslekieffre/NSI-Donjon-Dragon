from random import randint
from Monstre import Monstre

class Personnage:
    
    races = {
            "humain": {"pv": 100, "force": 15, "dext": 1, "armure": 10, "inventaire":{"or": 50, "potion": 2}},
            "elfe": {"pv": 80, "force": 15, "dext": 2, "armure": 5, "inventaire":{"or": 50, "potion": 2}},
            "nain": {"pv": 90, "force": 20, "dext": 1, "armure": 15, "inventaire":{"or": 50, "potion": 2}},
            "orc": {"pv": 110, "force": 20, "dext": 0, "armure": 15, "inventaire":{"or": 50, "potion": 2}},
            "goblin": {"pv": 90, "force": 15, "dext": 2, "armure": 10, "inventaire":{"or": 50, "potion": 2}}
        }
    
    classes = {
            "magicien": {"armes": ["Bâton","Baguette pour enfants", "Baguette de suro"], "sorts": ["petite explosion","boule de feu","éclair"], "objets": ["Potion de vie"]},
            "guerrier": {"armes": ["Épee en plastique", "Épée de bois", "Sabre Flamboyant"], "sorts": ["Tranche", "Taillade Aérienne"], "objets": ["Potion de soin"]},
        }
    

    def __init__(self, nom, race, classe, x, y):
        self.nom = nom
        self.race = race
        self.classe = classe
        self.pt_vie = Personnage.races[self.race]["pv"]
        self.force = Personnage.races[self.race]["force"]
        self.dext = Personnage.races[self.race]["dext"]
        self.armure = Personnage.races[self.race]["armure"]
        self.lst_armes = Personnage.classes[self.classe]["armes"]
        self.lst_sorts = Personnage.classes[self.classe]["sorts"]
        self.lst_objets = Personnage.classes[self.classe]["objets"]
        self.x = x
        self.y = y

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
        return self.pt_vie

    def get_position(self):
        return self.x, self.y
    
    def get_arme(self):
        return self.lst_armes[randint(0, len(self.lst_armes)-1)]

    def decrement_PV(self, valeur):
        self.pt_vie -= valeur

    def get_inventaire(self):
        for element, quantite in self.races[self.race]["inventaire"].items():
            print(f"- {quantite}x {element}")
            
    def piller_monstre(self, monstre):
        for element, quantite in monstre.races[monstre.race]["inventaire"].items():
            if element in self.races[self.race]["inventaire"]:
                self.races[self.race]["inventaire"][element] += quantite
            else:
                self.races[self.race]["inventaire"][element] = quantite
        monstre.races[monstre.race]["inventaire"] = {}  
        return self.races[self.race]["inventaire"]