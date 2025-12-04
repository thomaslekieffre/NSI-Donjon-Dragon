## TODO

# 1) Corrections critiques (nécessaires pour exécuter le jeu)
### - Standardiser les signatures de constructeur Personnage
  - Problème : appels actuels à Personnage utilisent différents nombres/ordres d'arguments (ex: Deplacement.py, Affrontement.py) alors que Personnage.__init__ attend (nom, race, classe, x, y).
  - Action : choisir une signature unique (ex: __init__(self, nom, race, classe, x=0, y=0)) et corriger tous les appels.
  - Fichiers à corriger : Deplacement.py, Affrontement.py, tout autre module instanciant Personnage.

### - Import manquant de randint dans Affrontement.py
  - Problème : Affrontement utilise randint sans l'importer.
  - Action : ajouter "from random import randint" en haut d'Affrontement.py ou utiliser random.randint.

### - Variables/attributs incohérents (pv vs pt_vie)
  - Problème : Personnage utilise self.pt_vie tandis que certains modules ou la logique peuvent attendre "pv".
  - Action : standardiser en "pv" ou "pt_vie" partout et adapter get_pv()/decrement_PV() en conséquence; documenter les noms.

### - Wildcard imports et exécution à l'import
  - Problème : utilisation de "from Monstre import *" et "from Personnage import *" ; Affrontement crée des instances et lance un combat au moment de l'import (bloc d'exécution global).
  - Action : supprimer exécution au niveau module ; utiliser "if __name__ == '__main__':" pour tests/exec. Remplacer wildcard imports par imports explicites.

### - Erreurs dans Deplacement / initialisation personnage
  - Problème : Deplacement crée Personnage avec trop d'arguments et ne place pas le personnage en se basant sur la carte (5).
  - Action : corriger instanciation, ajouter fonction pour trouver la position initiale (lire la grille pour trouver valeur 5) ou permettre spawn paramétré.

# 2) Bugs de logique et gameplay (haute priorité)
### - Combat : gestion du tour et conditions de victoire
  - Problème : variables is_attack/is_attack_heros/is_attack_mechant confuses ; is_attack défini mais pas utilisé ; gestion des dégâts simpliste.
  - Action : simplifier la logique de round (ex: bool turn_is_hero), s'assurer d'incrémenter __nbr_combat et __nbr_coups, prendre en compte l'armure dans les dégâts, ajouter messages clairs, retourner le gagnant.

### - Intégration déplacement / rencontres
  - Problème : rien n'arrive quand on marche sur 3 (cadeau) ou 4 (monstre).
  - Action : dans la fonction de déplacement, détecter la valeur de la case cible (2 porte, 3 cadeau, 4 monstre) et déclencher :
    - 3 : ajouter au sac/inventaire du personnage et remplacer par 0
    - 4 : instancier Monstre et lancer Affrontement ; si le personnage meurt, fin de partie ; si victoire, piller monstre
    - 2 : porte => possibilité de passer de niveau ou ouvrir la porte si clef, etc.

### - Affichage & alignement
  - Problème : affichage fonctionne mais peut être fragile selon terminal (emoji double-width).
  - Action : ajouter encodage utf-8 et fallback pour terminaux non-UTF8 ; centraliser logique d'affichage (constantes pour mapping case->symbole et largeur).

# 3) Fonctionnalités à implémenter (moyenne priorité)
### - Inventaire / objets
  - Prendre en charge ramassage, utilisation de potions, gestion d'or, affichage inventaire et sauvegarde.

### - Sauvegarde / chargement
  - Format simple JSON pour sauver personnage (position, pv, inventaire) et map (état), plus fonction load/save.

### - Gestion multi-monstres et spawn dynamique
  - Gérer plusieurs monstres, mobs aléatoires, équilibrage des rencontres.

# 4) Remarques techniques / suggestions rapides
### - Remplacer "from X import *" par "from X import Monstre" ou "import X".
### - Utiliser logging au lieu de prints pour debug.
### - Pour le calcul dégâts : utiliser formule (dégâts = max(1, attaque - armure/10)) ou chance critique pour variation.

Fin du TODO.
