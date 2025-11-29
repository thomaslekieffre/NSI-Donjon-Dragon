# Charger la carte depuis le fichier
from Personnage import Personnage


grille = []
with open("carte.txt", "r") as fichier:
    for ligne_texte in fichier:
        ligne_nombres = []
        for nombre_str in ligne_texte.split():
            nombre = int(nombre_str)
            ligne_nombres.append(nombre)
        grille.append(ligne_nombres)

def compter_largeur(texte):
    """Compte combien d'espaces prend un texte dans le terminal
    Les emojis prennent 2 espaces, les lettres normales 1 espace"""
    from unicodedata import east_asian_width
    largeur = 0
    for caractere in texte:
        # Les emojis sont des caractères "larges" (W ou F)
        if east_asian_width(caractere) in ('W', 'F'):
            largeur += 2  # Emoji = 2 espaces
        else:
            largeur += 1  # Caractère normal = 1 espace
    return largeur

def ajouter_espaces(texte, largeur_voulue):
    """Ajoute des espaces à la fin pour que le texte prenne exactement largeur_voulue espaces
    Exemple: ajouter_espaces('.', 3) donne '.  ' (1 caractère + 2 espaces = 3)"""
    largeur_actuelle = compter_largeur(texte)
    espaces_manquants = largeur_voulue - largeur_actuelle
    if espaces_manquants <= 0:
        return texte  # Le texte est déjà assez large
    return texte + " " * espaces_manquants
        
def afficher():
    """Affiche la carte dans le terminal avec un alignement correct"""
    for ligne in grille:
        ligne_a_afficher = ""
        for case in ligne:
            # Chaque case prend 3 espaces de largeur pour que tout soit aligné
            if case == 1:
                ligne_a_afficher += ajouter_espaces("◼", 3)  # Mur
            elif case == 2:
                ligne_a_afficher += ajouter_espaces("_", 3)   # Porte
            elif case == 3:
                ligne_a_afficher += ajouter_espaces("🎁", 3)  # Cadeau
            elif case == 4:
                ligne_a_afficher += ajouter_espaces("👾", 3)  # Monstre
            elif case == 5:
                ligne_a_afficher += ajouter_espaces("🧍", 3)  # Personnage
            else:
                ligne_a_afficher += ajouter_espaces(".", 3)  # Sol vide
        print(ligne_a_afficher.rstrip())  # Enlever les espaces à la fin de la ligne

afficher()