from random import randint
from Monstre import Monstre
from Personnage import Personnage

class Affrontement :
    def __init__(self, niveau = "Easy"):
        self.__niveau = niveau
        self.__nbr_combat = 0
        self.__nbr_coups = 0
         
    def get_niveau(self):
        return self.__niveau
    
    def get_nbr_combat(self):
        return self.__nbr_combat
    
    def get_nbr_coups(self):
        return self.__nbr_coups
    
    def incr_nbCombat(self):
        self.__nbr_combat += 1
    
    def incr_nbCoupEchange(self):
        self.__nbr_coups += 1
        
    def combatAMort(self, heros, mechant):
        
        is_attack_heros = True
        is_attack_mechant = True
         
        print("Combat opposant " + heros.get_nom() + " (" + str(heros.get_pv()) + " PV) a " + mechant.get_nom() + "armé d'un " + mechant.get_arme() + " avec une dextérité de " + str(mechant.get_dext()))
        
        if heros.get_dext() > mechant.get_dext() :
            print( heros.get_nom() + " (" + str(heros.get_pv()) + " PV) attaque en premier")
            choix = 0
            while choix != 1 or choix != 2:
                choix = int(input("Souhaitez vous : \n attaquer normalement : 1 \n utiliser un sort : 2"))
                if choix == 1:
                    mechant.decrement_PV(randint(1,heros.get_force()))
                    is_attack = False
                elif choix == 2:
                    print("On lance un sort")
                    is_attack = False
            
        elif heros.get_dext() == mechant.get_dext() :
            print( heros.get_nom() + " (" + str(heros.get_pv()) + " PV) attaque en premier")
            choix = int(input("Souhaitez vous : \n attaquer normalement : 1 \n utiliser un sort : 2"))
            if choix == 1:
                mechant.decrement_PV(randint(1,heros.get_force()))
                is_attack = False
            elif choix == 2:
                print("On lance un sort")
                is_attack = False
            
        else :
            print( "Le monstre (" + str(mechant.get_pv()) + " PV) attaque en premier")
            pv_decremente = heros.decrement_PV(randint(1,mechant.get_force()))
            print(f"PAF ! Le monstre vous a retiré {pv_decremente} PV")
            print(pv_decremente)
            is_attack = False
        
        while heros.get_pv() > 0 and mechant.get_pv() > 0 :
            if is_attack_heros == True :
                choix = 0
                while choix != 1 and choix != 2:
                    choix = int(input("Souhaitez vous : \n attaquer normalement : 1 \n utiliser un sort : 2 \n Votre choix : "))
                    if choix == 1:
                        mechant.decrement_PV(randint(1,heros.get_force()))
                        is_attack_heros = False
                        is_attack_mechant = True
                    elif choix == 2:
                        print("On lance un sort")
                        is_attack_heros = False
                        is_attack_mechant = True
                
            elif is_attack_mechant == True :
                print("PAF")
                heros.decrement_PV(randint(1,mechant.get_force()))
                is_attack_heros = True
                is_attack_mechant = False
        
        print("AARRGGG")
        if heros.get_pv() <= 0:
            print( "Le monstre armé d'un " + mechant.get_arme() + " avec une force de " + str(mechant.get_force()) + " remporte le combat à mort ")
        elif mechant.get_pv() <= 0:
            print(heros.get_nom()  + " (" + str(heros.get_pv()) + " PV) ,  a remporté le combat à mort")
