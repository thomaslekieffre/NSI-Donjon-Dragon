from random import randint

class Monstre:
    
    races = {
            "Ogre": {"pv": 130, "force": 15, "dext": 0.2, "armure": 30},
            "Géant": {"pv": 60, "force": 15, "dext": 2, "armure": 5},
            "Gorille": {"pv": 90, "force": 20, "dext": 2, "armure": 10},
            "Troll": {"pv": 110, "force": 10, "dext": 0.5, "armure": 15},
        }
    
    classes = {
            "puissant": {"armes": ["Massue","Poing Américain"], "sorts": ["Grand coup de massue","Coup de poing américain"]},
            "rapide": {"armes": ["Dague","Couteau"], "sorts": ["Coup de dague","Coup de couteau"]},
        }
    

    def __init__(self,nom, race, classe):
        self.nom = nom
        self.race = race
        self.classe = classe
        self.pt_vie = Monstre.races[self.race]["pv"]
        self.force = Monstre.races[self.race]["force"]
        self.dext = Monstre.races[self.race]["dext"]
        self.armure = Monstre.races[self.race]["armure"]
        self.lst_armes = Monstre.classes[self.classe]["armes"]
        self.lst_sorts = Monstre.classes[self.classe]["sorts"]

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
    
    def get_arme(self):
        return self.lst_armes[randint(0,len(self.lst_armes)-1)]

    def decrement_PV(self, valeur):
        self.pt_vie -= valeur