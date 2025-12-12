from random import choice, sample

grille = []
with open("carte.txt", "r") as f:
    for ligne in f:
        l = []
        for char in ligne.split():
            l.append(int(char))
        grille.append(l)


PORTES = {2, 6, 7}  # valeurs des portes fermées sur la carte
DEPLACEMENTS = [(1, 0), (-1, 0), (0, 1), (0, -1)] 


def trouver_heros():
    """Retourne (x, y) du héros (valeur 5) ou None si absent."""
    for y, ligne in enumerate(grille):
        for x, valeur in enumerate(ligne):
            if valeur == 5:
                return x, y
    return None


def zones_visibles():
    """
    Calcule les cases visibles depuis le héros.

    - Les murs (1) bloquent la vision.
    - Les portes fermées (2, 6, 7) sont visibles mais ne laissent pas voir au‑delà.
    - Dès qu'une porte est ouverte (sa case passe à 0 quand on la traverse),
      la vision se propage dans la pièce derrière.
    """
    position_heros = trouver_heros()
    cases_visibles = {position_heros} # Cases déjà visitées
    file_positions = [position_heros] # File d'attente des autres cases à visiter

    while file_positions:
        position_x, position_y = file_positions.pop(0)  # défiler en ordre d'arrivée
        for decalage_x, decalage_y in DEPLACEMENTS:
            voisin_x = position_x + decalage_x
            voisin_y = position_y + decalage_y
            if voisin_y < 0 or voisin_y >= len(grille) or voisin_x < 0 or voisin_x >= len(grille[0]):
                continue
            if (voisin_x, voisin_y) in cases_visibles:
                continue

            valeur_case = grille[voisin_y][voisin_x]
            cases_visibles.add((voisin_x, voisin_y))

            # On montre les cases si ce n'est ni mur ni porte fermée.
            if valeur_case not in PORTES and valeur_case != 1:
                file_positions.append((voisin_x, voisin_y))

    return cases_visibles


def trouver_position_depart():
    """Renvoie la position du héros (5) ou (1,1) par défaut s'il n'est pas placé."""
    position = trouver_heros()
    if position:
        return position
    return 1, 1


def ajouter_coffre(nombre):
    """Place des coffres (3) sur des cases vides."""
    for _ in range(nombre):
        cases_vides = [(x, y) for y, ligne in enumerate(grille) for x, v in enumerate(ligne) if v == 0]
        if not cases_vides:
            return
        x, y = choice(cases_vides)
        grille[y][x] = 3


def ajouter_monstres(nombre):
    """Place des monstres (4) sur des cases vides sans doublon."""
    cases_vides = [(x, y) for y, ligne in enumerate(grille) for x, v in enumerate(ligne) if v == 0]
    if not cases_vides:
        return
    positions = sample(cases_vides, k=min(nombre, len(cases_vides)))
    for x, y in positions:
        grille[y][x] = 4


def afficher():
    symbols = {
        0: ".",
        1: "◼",
        2: "_",
        3: "⊞",
        4: "☻",
        5: "♀",
        6: "✪",
        7: "|",
    }
    visibles = zones_visibles()

    print("\n=== Carte ===")
    for y, ligne in enumerate(grille):
        ligne_affichee = []
        for x, element in enumerate(ligne):
            if (x, y) not in visibles:
                # On affiche quand même les murs non vus pour éviter des ? qui restent sur les côtés
                if element == 1:
                    ligne_affichee.append("◼")
                else:
                    ligne_affichee.append("?")
            else:
                ligne_affichee.append(symbols.get(element, "?"))
        print(" ".join(ligne_affichee))

    print("Légende: ◼ mur | _ porte | ✪ porte finale | ⊞ coffre | ☻ monstre | ♀ héros | . vide | ? inconnu")