from affichage import grille, afficher


def deplacer_personnage(personnage, direction):
    """
    Déplace le personnage dans la direction spécifiée.
    
    Args:
        personnage: Instance de la classe Personnage
        direction: str - "haut", "bas", "gauche" ou "droite"
    
    Returns:
        tuple[bool, int|None]: (succès, valeur de la case ciblée ou None)
    """
    # Récupérer la position actuelle
    x_actuel = personnage.x
    y_actuel = personnage.y
    
    # Calculer la nouvelle position selon la direction
    if direction == "haut":
        x_nouveau = x_actuel
        y_nouveau = y_actuel - 1
    elif direction == "bas":
        x_nouveau = x_actuel
        y_nouveau = y_actuel + 1
    elif direction == "gauche":
        x_nouveau = x_actuel - 1
        y_nouveau = y_actuel
    elif direction == "droite":
        x_nouveau = x_actuel + 1
        y_nouveau = y_actuel
    else:
        print("Direction invalide. Utilisez: haut, bas, gauche ou droite")
        return False, None
    
    # Vérifier les limites de la grille
    if y_nouveau < 0 or y_nouveau >= len(grille):
        print("Déplacement impossible : sortie de la carte (haut/bas)")
        return False, None
    if x_nouveau < 0 or x_nouveau >= len(grille[0]):
        print("Déplacement impossible : sortie de la carte (gauche/droite)")
        return False, None
    
    tile = grille[y_nouveau][x_nouveau]

    # Vérifier si la case de destination est un mur (1 = mur)
    if tile == 1:
        print("Déplacement impossible : vous ne pouvez pas traverser un mur")
        return False, tile
    
    # Effectuer le déplacement
    grille[y_actuel][x_actuel] = 0
    grille[y_nouveau][x_nouveau] = 5
    personnage.x = x_nouveau
    personnage.y = y_nouveau
    
    return True, tile