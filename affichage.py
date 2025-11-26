from sys import platform, stdout
from io import TextIOWrapper

# Configurer l'encodage UTF-8 pour Windows
if platform == 'win32':
    stdout = TextIOWrapper(stdout.buffer, encoding='utf-8')

grille = []
with open("carte.txt", "r") as f:
    for ligne in f:
        l=[]
        for char in ligne.split():
            l.append(int(char))
        grille.append(l)

def largeur_reelle(s):
    """Calcule la largeur réelle d'une chaîne (emojis = 2 caractères)"""
    import unicodedata
    largeur = 0
    for char in s:
        # Vérifier si c'est un emoji ou un caractère large
        if unicodedata.east_asian_width(char) in ('W', 'F'):
            largeur += 2
        else:
            largeur += 1
    return largeur

def pad_fixe(s, largeur_cible):
    """Pad une chaîne pour qu'elle prenne exactement largeur_cible caractères"""
    largeur_actuelle = largeur_reelle(s)
    if largeur_actuelle >= largeur_cible:
        return s
    return s + " " * (largeur_cible - largeur_actuelle)
        
def afficher():
        for ligne in grille:
            ligne_affichage = ""
            for element in ligne:
                if element==1: ligne_affichage += pad_fixe("◼", 3)
                elif element==2: ligne_affichage += pad_fixe("_", 3)
                elif element==3: ligne_affichage += pad_fixe("🎁", 3)
                elif element==4: ligne_affichage += pad_fixe("👾", 3)
                elif element==5: ligne_affichage += pad_fixe("🧍", 3)
                else: ligne_affichage += pad_fixe(".", 3)
            print(ligne_affichage.rstrip())

afficher()