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
    Calcule les cases visibles depuis le héros avec un parcours en largeur (BFS simple).

    - Les murs (1) bloquent la vision.
    - Les portes fermées (2, 6, 7) sont visibles mais ne laissent pas voir au‑delà.
    - Dès qu'une porte est ouverte (sa case passe à 0 quand on la traverse),
      la vision se propage dans la pièce derrière.
    """
    start = trouver_heros()
    if start is None:
        return set()

    visibles = {start}
    file = [start]  

    while file:
        x, y = file.pop(0)  # dépiler dans l'ordre d'arrivée
        for dx, dy in DEPLACEMENTS:
            nx, ny = x + dx, y + dy
            if ny < 0 or ny >= len(grille) or nx < 0 or nx >= len(grille[0]):
                continue
            if (nx, ny) in visibles:
                continue

            valeur = grille[ny][nx]
            visibles.add((nx, ny))

            # On montre les cases si ce n'est ni mur ni porte fermée.
            if valeur not in PORTES and valeur != 1:
                file.append((nx, ny))

    return visibles


def afficher():
    symbols = {
        0: ".",
        1: "◼",
        2: "_",
        3: "⊞",
        4: "☻",
        5: "♀",
        6: "_",
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

    print("Légende: ◼ mur | _ porte | ⊞ coffre | ☻ monstre | ♀ héros | . vide | ? inconnu")