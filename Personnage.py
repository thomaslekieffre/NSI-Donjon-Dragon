from random import randint
from Monstre import Monstre

class Personnage:
    
    races = {
            "humain": {"pv": 100, "force": 35, "dext": 1, "armure": 10, "inventaire":{"or": 850, "potion": 2}},
            "elfe": {"pv": 80, "force": 25, "dext": 2, "armure": 5, "inventaire":{"or": 50, "potion": 2}},
            "nain": {"pv": 90, "force": 30, "dext": 1, "armure": 15, "inventaire":{"or": 50, "potion": 2}},
            "orc": {"pv": 110, "force": 30, "dext": 0, "armure": 15, "inventaire":{"or": 50, "potion": 2}},
            "goblin": {"pv": 90, "force": 25, "dext": 2, "armure": 10, "inventaire":{"or": 50, "potion": 2}}
        }
    
    classes = {
            "magicien": {"armes": ["Bâton","Baguette pour enfants", "Baguette de suro"], "sorts": {"Petite explosion":30,"Boule de feu":45,"Éclair":60}, "objets": ["Potion de vie"]},
            "guerrier": {"armes": ["Épee en plastique", "Épée de bois", "Sabre Flamboyant"], "sorts": {"Tranche":30, "Brisefer":45, "Taillade Aérienne":60}, "objets": ["Potion de soin"]},
        }
    

    def __init__(self, nom, race, classe, x=0, y=0):
        # Sécurisation des entrées utilisateur : on normalise et on fallback si inconnu
        race = (race or "").lower()
        classe = (classe or "").lower()
        if race not in Personnage.races:
            print("Race inconnue, utilisation de 'humain'.")
            race = "humain"
        if classe not in Personnage.classes:
            print("Classe inconnue, utilisation de 'guerrier'.")
            classe = "guerrier"

        self.nom = nom or "Heros"
        self.race = race
        self.classe = classe
        self.pv = Personnage.races[self.race]["pv"]
        self.max_pv = Personnage.races[self.race]["pv"]
        self.force = Personnage.races[self.race]["force"]
        self.dext = Personnage.races[self.race]["dext"]
        self.armure = Personnage.races[self.race]["armure"]
        self.lst_armes = Personnage.classes[self.classe]["armes"]
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
        return self.pv

    def get_max_pv(self):
        return self.max_pv

    def get_position(self):
        return self.x, self.y
    
    def get_arme(self):
        return self.lst_armes[randint(0, len(self.lst_armes)-1)]
    
    def get_sorts(self):
        """Retourne la liste des sorts disponibles pour le perso courant."""
        return list(self.classes[self.classe]["sorts"].items())

    def decrement_PV(self, valeur):
        self.pv -= valeur
        if self.pv < 0:
            self.pv = 0
        return self.pv

    def get_inventaire(self):
        for element, quantite in self.races[self.race]["inventaire"].items():
            print(f"- {quantite}x {element}")
            
    def piller_monstre(self, monstre):
        for element, quantite in monstre.races[monstre.race]["inventaire"].items():
            if element in self.races[self.race]["inventaire"]:
                self.races[self.race]["inventaire"][element] += quantite
            else:
                self.races[self.race]["inventaire"][element] = quantite
        return self.races[self.race]["inventaire"]
        
p1 = Personnage("zozo","orc","magicien")
