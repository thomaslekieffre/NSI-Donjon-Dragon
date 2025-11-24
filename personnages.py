class Personnage:
    
    races = {
            "humain": {"pv": 100, "force": 15, "dext": 1, "armure": 10},
            "elfe": {"pv": 80, "force": 15, "dext": 2, "armure": 5},
            "nain": {"pv": 90, "force": 20, "dext": 1, "armure": 15},
            "orc": {"pv": 110, "force": 20, "dext": 0, "armure": 15},
            "goblin": {"pv": 90, "force": 15, "dext": 2, "armure": 10}
        }
    
    classes = {
            "magicien": {"armes": ["d","g"], "sorts": [], "objets": []},
            "guerrier": {"armes": [], "sorts": [], "objets": []},
        }
    

    def __init__(self,nom, race, classe,  lst_armes, lst_sorts, lst_objets):
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
    
    def get_armes(self):
        return self.lst_armes
    
        
p1 = Personnage("Thomas", "nain", "magicien", [],[],[])
print(p1.get_race())
print(p1.get_classe())
print(p1.get_force())
print(p1.get_dext())
print(p1.get_pv())
print(p1.get_armes())