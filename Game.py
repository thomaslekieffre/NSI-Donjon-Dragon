from random import choice, sample, randint

from affichage import grille, afficher
from Deplacement import deplacer_personnage
from Personnage import Personnage
from Monstre import Monstre
from Affrontement import Affrontement

DIRECTIONS = {
    "z": "haut",
    "s": "bas",
    "q": "gauche",
    "d": "droite",
}


def trouver_position_depart():
    """Retourne les coordonnées où la carte contient un 5 (perso placé dans la map)."""
    for y, ligne in enumerate(grille):
        for x, valeur in enumerate(ligne):
            if valeur == 5:
                return x, y
    return 1, 1  # si la map n'a pas de 5, on place le personnage en 1,1


def generer_monstre():
    race = choice(list(Monstre.races.keys()))
    classe = choice(list(Monstre.classes.keys()))
    nom = f"{race.lower()} sauvage"
    return Monstre(nom, race, classe)


def resoudre_case(personnage, tile):
    messages = []
    if tile == 2:
        bourse = Personnage.races[personnage.race]["inventaire"]
        if bourse.get("or", 0) >= 200:
            bourse["or"] -= 200
            messages.append("Tu utilises 200 pieces pour ouvrir la porte. GG !")
            return False, False, messages
        messages.append("Il faut 200 pieces pour ouvrir cette porte. (pas assez)")
        return True, True, messages

    # TODO : Gérer coffre aléatoire (potion, or ...)
    if tile == 3:
        sac = Personnage.races[personnage.race]["inventaire"]
        sac["potion"] = sac.get("potion", 0) + 1
        messages.append("Tu ouvres un coffre : +1 potion")
        return True, False, messages

    if tile == 4:
        monstre = generer_monstre()
        combat = Affrontement()
        combat.combatAMort(personnage, monstre)
        if personnage.get_pv() <= 0:
            messages.append("Ton heros est tombe. Fin de partie.")
            return False, False, messages
        personnage.piller_monstre(monstre)
        messages.append("Le monstre laisse son loot. Inventaire mis a jour.")
        return True, False, messages

    return True, False, messages


def ajouter_monstres(nombre):
    cases_vides = [(x, y) for y, ligne in enumerate(grille) for x, v in enumerate(ligne) if v == 0]
    if not cases_vides:
        return
    # sample garantit des positions uniques (pas de doublons comme choice en boucle)
    # On choisit k le plus petit nombre entre le nombre de monstres à ajouter et le nombre de cases vides
    positions = sample(cases_vides, k=min(nombre, len(cases_vides)))
    for x, y in positions:
        grille[y][x] = 4


def utiliser_potion(personnage, soin=30):
    sac = Personnage.races[personnage.race]["inventaire"]
    potions = sac.get("potion", 0)
    if potions <= 0:
        return ["Aucune potion disponible."]
    if personnage.get_pv() >= personnage.get_max_pv():
        return ["PV deja au maximum."]
    sac["potion"] = potions - 1
    personnage.pv = min(personnage.get_pv() + soin, personnage.get_max_pv())
    return [f"Potion bue : +{soin} PV -> {personnage.get_pv()}/{personnage.get_max_pv()}"]


def creer_personnage():
    x, y = trouver_position_depart()
    nom = input("Nom du héros ? ") or "Héros"
    race = input("Race (humain/elfe/nain/orc/goblin) ? ") or "humain"
    classe = input("Classe (magicien/guerrier) ? ") or "guerrier"
    return Personnage(nom, race, classe, x, y)


def boucle_jeu():
    perso = creer_personnage()
    ajouter_monstres(nombre=randint(1, 5))

    en_cours = True
    messages = []
    while en_cours and perso.get_pv() > 0:
        afficher()
        for msg in messages:
            print(msg)
        messages = []
        print(f"PV: {perso.get_pv()}/{perso.get_max_pv()} | Potions: {Personnage.races[perso.race]['inventaire'].get('potion',0)} | Or: {Personnage.races[perso.race]['inventaire'].get('or',0)}")
        print("Deplacement zqsd ou haut/bas/gauche/droite, i inventaire, p potion, exit pour quitter")
        cmd = input("> ").lower()
        quitter = cmd in ("exit", "quit", "q!")
        if quitter:
            en_cours = False
        elif cmd == "i":
            perso.get_inventaire()
        elif cmd == "p":
            messages.extend(utiliser_potion(perso) or [])
        else:
            direction = DIRECTIONS.get(cmd, cmd)
            ancien_x, ancien_y = perso.x, perso.y
            deplace, tile = deplacer_personnage(perso, direction)
            if deplace:
                en_cours, revert, new_msgs = resoudre_case(perso, tile)
                messages.extend(new_msgs)
                if revert:
                    grille[perso.y][perso.x] = tile
                    perso.x, perso.y = ancien_x, ancien_y
                    grille[ancien_y][ancien_x] = 5

    print("Fin du jeu. Vous avez perdu !")

boucle_jeu()