from affichage import grille, afficher
from Personnage import Personnage

personnage = Personnage("Toto", "nain", "magicien", [], [], [], 17, 15)

def deplacer_personnage(personnage, direction):
    """
    Déplace le personnage dans la direction spécifiée.
    
    Args:
        personnage: Instance de la classe Personnage
        direction: str - "haut", "bas", "gauche" ou "droite"
    
    Returns:
        bool: True si le déplacement a réussi, False sinon
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
        return False
    
    # Vérifier les limites de la grille
    if y_nouveau < 0 or y_nouveau >= len(grille):
        print("Déplacement impossible : sortie de la carte (haut/bas)")
        return False
    if x_nouveau < 0 or x_nouveau >= len(grille[0]):
        print("Déplacement impossible : sortie de la carte (gauche/droite)")
        return False
    
    # Vérifier si la case de destination est un mur (1 = mur)
    if grille[y_nouveau][x_nouveau] == 1:
        print("Déplacement impossible : vous ne pouvez pas traverser un mur")
        return False
    
    # Effectuer le déplacement
    # 1. Effacer l'ancienne position (remplacer par 0 = sol vide)
    grille[y_actuel][x_actuel] = 0
    # 2. Placer le personnage à la nouvelle position (5 = personnage)
    grille[y_nouveau][x_nouveau] = 5
    # 3. Mettre à jour les coordonnées du personnage
    personnage.x = x_nouveau
    personnage.y = y_nouveau
    
    return True


# Boucle de déplacement
continuer = True
while continuer:
    choix = input("\nVoulez-vous déplacer le personnage ? (o/n) : ")
    if choix.lower() == "n":
        print("Le personnage ne se déplace pas")
        continuer = False
        
    elif choix.lower() == "o":
        direction = input("Direction (haut/bas/gauche/droite) : ")
        if deplacer_personnage(personnage, direction):
            afficher()
    else:
        print("Choix invalide. Utilisez 'o' pour oui ou 'n' pour non")
    