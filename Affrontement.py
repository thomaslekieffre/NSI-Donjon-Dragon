from random import randint
from Monstre import Monstre
from Personnage import Personnage

class Affrontement :
    def __init__(self):
        self.__nbr_combat = 0
        self.__nbr_coups = 0
        
    def get_nbr_combat(self):
        return self.__nbr_combat
    
    def get_nbr_coups(self):
        return self.__nbr_coups
    
    def incr_nbCombat(self):
        self.__nbr_combat += 1
    
    def incr_nbCoupEchange(self):
        self.__nbr_coups += 1
        
    def choix_int(self, prompt, options):
        """Demande un entier parmi options"""
        while True:
            val = input(prompt).strip()
            try:
                num = int(val)
            except ValueError:
                print("Entrée invalide. Tape un nombre.")
                continue
            if num in options:
                return num
            print(f"Choix possible: {', '.join(map(str, options))}")

    def choisir_sort(self, heros):
        sorts = Personnage.classes[heros.get_classe()]["sorts"]
        noms = list(sorts.keys())
        print("Choisis un sort:")
        for idx, nom in enumerate(noms, 1):
            print(f"  {idx}. {nom} ({sorts[nom]} dégâts)")
        idx = self.choix_int("Numéro du sort: ", range(1, len(noms) + 1))
        nom_sort = noms[idx - 1]
        return nom_sort, sorts[nom_sort]

    def attaque_heros(self, heros, mechant):
        choix = self.choix_int(
            "\nAction ? 1: attaque normale | 2: lancer un sort : ",
            [1, 2],
        )
        if choix == 1:
            degats = randint(1, heros.get_force())
            reel = mechant.decrement_PV(degats)
            print(f"{heros.get_nom()} frappe ({degats} bruts) -> {reel} dégâts appliqués. Monstre: {mechant.get_pv()} PV")
        else:
            if Personnage.classes[heros.get_classe()]["sorts"] == {}:
                print("Plus de sorts disponibles ! Attaque normale à la place.")
                degats = randint(1, heros.get_force())
                reel = mechant.decrement_PV(degats)
                print(f"{heros.get_nom()} frappe ({degats} bruts) -> {reel} dégâts appliqués. Monstre: {mechant.get_pv()} PV")
                return
            nom_sort, degats = self.choisir_sort(heros)
            print(Personnage.classes[heros.get_classe()]["sorts"][nom_sort])
            del Personnage.classes[heros.get_classe()]["sorts"][nom_sort]
            reel = mechant.decrement_PV(degats)
            print(f"{heros.get_nom()} lance {nom_sort} ({degats} bruts) -> {reel} dégâts. Monstre: {mechant.get_pv()} PV")

    def attaque_monstre(self, heros, mechant):
        degats = randint(1, mechant.get_force())
        reel = heros.decrement_PV(degats)
        print(f"{mechant.get_nom()} attaque ({degats} bruts) -> {reel} dégâts. Héros: {heros.get_pv()} PV")

    def combatAMort(self, heros, mechant):
        print("\n=== Combat ===")
        print(
            f"{heros.get_nom()} ({heros.get_pv()} PV, dext {heros.get_dext()}) "
            f"vs {mechant.get_nom()} ({mechant.get_pv()} PV, dext {mechant.get_dext()}, arme {mechant.get_arme()})"
        )

        tour_heros = heros.get_dext() >= mechant.get_dext()
        if tour_heros:
            print(f"{heros.get_nom()} est plus rapide et commence.")
        else:
            print(f"{mechant.get_nom()} est plus rapide et commence.")

        while heros.get_pv() > 0 and mechant.get_pv() > 0:
            if tour_heros:
                self.attaque_heros(heros, mechant)
            else:
                self.attaque_monstre(heros, mechant)
            tour_heros = not tour_heros

        print("\n=== Résultat ===")
        if heros.get_pv() <= 0:
            print(f"{mechant.get_nom()} remporte le combat.")
        else:
            print(f"{heros.get_nom()} triomphe ! Il reste {heros.get_pv()} PV.")
