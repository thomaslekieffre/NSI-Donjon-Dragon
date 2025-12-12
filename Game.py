from random import randint
from colorama import Fore, Style

from affichage import (
    grille,
    afficher,
    ajouter_coffre,
    ajouter_monstres,
    trouver_position_depart,
)
from Deplacement import deplacer_personnage
from Personnage import Personnage
from Monstre import generer_monstre
from Affrontement import Affrontement

DIRECTIONS = {
    "z": "haut",
    "s": "bas",
    "q": "gauche",
    "d": "droite",
}

def saisie_option(prompt, options, default):
    """Renvoie la valeur si dans options sinon le défaut, sans crasher."""
    valeur = input(prompt).strip().lower()
    if valeur in options:
        return valeur
    if valeur:
        print(f"Choix inconnu, on prend '{default}'.")
    return default

def resoudre_case(personnage, case, etat):
    messages = []
    if case == 2:
        bourse = Personnage.races[personnage.race]["inventaire"]
        if bourse.get("or", 0) >= 150:
            bourse["or"] -= 150
            messages.append("Tu utilises 150 pièces pour ouvrir la porte. GG !")
            grille[personnage.y][personnage.x] = 5
            etat["porte1_ouverte"] = True
            return True, False, messages
        messages.append("Il faut 150 pièces pour ouvrir cette porte. (pas assez)")
        return True, True, messages
    
    if case == 7:
        bourse = Personnage.races[personnage.race]["inventaire"]
        if bourse.get("or", 0) >= 150:
            bourse["or"] -= 150
            messages.append("Tu utilises 150 pièces pour ouvrir la porte. GG !")
            grille[personnage.y][personnage.x] = 5
            etat["porte2_ouverte"] = True
            return True, False, messages
        messages.append("Il faut 150 pièces pour ouvrir cette porte. (pas assez)")
        return True, True, messages
    
    if case == 6:
        bourse = Personnage.races[personnage.race]["inventaire"]
        if bourse.get("or", 0) >= 200 and bourse.get("os de poulet", 0)>=15 :
            bourse["or"] -= 200
            bourse["os de poulet"]-= 15
            messages.append("Tu utilises 200 pièces et 15 os de poulet pour ouvrir le portail magique. GG !")
            grille[personnage.y][personnage.x] = 5
            etat["porte3_ouverte"] = True
            if etat["porte1_ouverte"] and etat["porte2_ouverte"] and etat["porte3_ouverte"]:
                etat["victoire"] = True
                messages.append("Porte finale ouverte : victoire !")
                return False, False, messages
            return True, False, messages
        messages.append("Il faut 200 pièces et 15 os de poulet pour ouvrir ce portail. (pas assez)")
        return True, True, messages

    if case == 3:
        aleatoire = randint(1, 3)
        sac = Personnage.races[personnage.race]["inventaire"]
        if aleatoire == 1:
            sac["potion"] = sac.get("potion", 0) + 1
            messages.append("Tu ouvres un coffre : +1 potion")
        elif aleatoire == 2:
            montant = randint(10, 100)
            sac["or"] = sac.get("or", 0) + montant
            messages.append(f"Tu ouvres un coffre : +{montant} or")
        else:
            sac["os de poulet"] = sac.get("os de poulet", 0) + 3
            messages.append("Tu ouvres un coffre : +3 os de poulet")
        
        return True, False, messages

    if case == 4:
        monstre = generer_monstre()
        combat = Affrontement()
        combat.combatAMort(personnage, monstre)
        if personnage.get_pv() <= 0:
            messages.append("Ton heros est tombe. Fin de partie.")
            return False, False, messages
        print(monstre.get_inventaire())
        personnage.piller_monstre(monstre)
        messages.append("Le monstre laisse son loot. Inventaire mis a jour.")
        return True, False, messages

    return True, False, messages


def creer_personnage():
    x, y = trouver_position_depart()
    nom = input("Nom du héros ? ").strip() or "Heros"
    race = saisie_option("Race (humain/elfe/nain/orc/goblin) ? ", Personnage.races.keys(), "humain")
    classe = saisie_option("Classe (magicien/guerrier) ? ", Personnage.classes.keys(), "guerrier")
    return Personnage(nom, race, classe, x, y)


def boucle_jeu():
    etat = {
        "porte1_ouverte": False,
        "porte2_ouverte": False,
        "porte3_ouverte": False,
        "victoire": False,
    }
    perso = creer_personnage()
    ajouter_monstres(nombre=randint(3, 8))
    ajouter_coffre(nombre = randint(2,5))

    en_cours = True
    messages = []
    while en_cours and perso.get_pv() > 0:
        afficher()
        for msg in messages:
            print(msg)
        messages = []
        print(Fore.MAGENTA + f"PV: {perso.get_pv()}/{perso.get_max_pv()} | Potions: {Personnage.races[perso.race]['inventaire'].get('potion',0)} | Or: {Personnage.races[perso.race]['inventaire'].get('or',0)}")
        print(Fore.CYAN + "Deplacement zqsd ou haut/bas/gauche/droite, i inventaire, p potion, exit pour quitter")
        print(Style.RESET_ALL)
        cmd = input("> ").strip().lower()
        quitter = cmd in ("exit", "quit", "q!")
        if quitter:
            en_cours = False
        elif cmd == "i":
            perso.get_inventaire()
        elif cmd == "p":
            messages.extend(perso.utiliser_potion() or [])
        else:
            direction = DIRECTIONS.get(cmd, cmd)
            if direction not in DIRECTIONS.values():
                print(Fore.YELLOW + "Commande inconnue. Utilise z/q/s/d ou haut/bas/gauche/droite.")
                print(Style.RESET_ALL)
                continue
            ancien_x, ancien_y = perso.x, perso.y
            deplace, case = deplacer_personnage(perso, direction)
            if deplace:
                en_cours, annuler, new_msgs = resoudre_case(perso, case, etat)
                messages.extend(new_msgs)
                if annuler:
                    grille[perso.y][perso.x] = case
                    perso.x, perso.y = ancien_x, ancien_y
                    grille[ancien_y][ancien_x] = 5
    if etat["victoire"]:
        print(Fore.GREEN + "🎉 VICTOIRE ! Tu as ouvert la porte finale et gagné la partie.")
        print(Style.RESET_ALL)
    elif perso.get_pv() <= 0:
        print(Fore.RED + "Fin du jeu. Vous avez perdu !")
        print(Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Fin de partie.")
        print(Style.RESET_ALL)

    rejouer = input('Voulez vous rejouer ? "oui" ou "non"\n ')
    if rejouer == "oui":
        boucle_jeu()
    else:
        print("Merci d'avoir joué !")
        return

boucle_jeu()