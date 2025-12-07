## TODO

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

# 3) Fonctionnalités à implémenter

### - Combat ++
  - Faire de meilleurs combats, gestion des sorts ...

### - Sauvegarde / chargement
  - Format simple JSON pour sauver personnage (position, pv, inventaire) et map (état), plus fonction load/save.

### - Équilibrer le jeu
  - Équilibrage des rencontres.

# 4) Remarques techniques / suggestions rapides
### - Remplacer "from X import *" par "from X import Monstre" ou "import X".
### - Pour le calcul dégâts : utiliser formule (dégâts = max(1, attaque - armure/10)) ou chance critique pour variation.

Fin du TODO.
