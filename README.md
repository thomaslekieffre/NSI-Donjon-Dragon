## Donjon & Dragon – version terminal
Petit jeu rogue‑lite : déplacer un héros, ouvrir coffres, affronter des monstres, et ouvrir les portes jusqu’à la victoire.

### Pré-requis
- Python 3.10+  
- Dépendance : `pip install colorama`

### Lancer la partie
```bash
python Game.py
```

### Commandes en jeu
- Déplacement : `z q s d` (ou `haut bas gauche droite`)  
- Inventaire : `i`  
- Boire potion : `p`  
- Quitter : `exit` / `quit` / `q!`

### Règles rapides
- Coffre (3) : loot aléatoire (potion, or, os).  
- Porte 2 / 7 : coûte 150 or.  
- Porte finale 6 : coûte 200 or + 15 os de poulet.  
- Monstre (4) : combat au tour par tour.  
- Victoire : ouvrir les trois portes.

### Légende de la carte
- `◼` mur, `_` porte, `✪` porte finale, `⊞` coffre, `☻` monstre, `♀` héros, `.` vide, `?` inconnu.

### Structure des modules
- `Game.py` : boucle de jeu, I/O joueur.  
- `affichage.py` : carte, visibilité, placement coffres/monstres, rendu.  
- `Deplacement.py` : mouvement du héros.  
- `Personnage.py` : classe héros, inventaire, potion.  
- `Monstre.py` : classe monstre, génération aléatoire.  
- `Affrontement.py` : combat tour par tour.

### Fonctionnalités principales (implémentation technique)

**Combat tour par tour** : Alternance héros/monstre selon la dextérité via booléen `tour_heros`, avec attaques normales (`randint(10, force)`) ou sorts (dictionnaire de sorts par classe, suppression avec `del` après utilisation, dégâts fixes).

**Vision** : Algorithme qui regarde ligne par ligne et colonne par colonne (BFS) avec `set` pour `cases_visibles` et `list` comme file FIFO (`pop(0)`/`append()`), propagation bloquée par murs (case == 1) et portes fermées (test d'appartenance avec `in`).

**Déplacement** : Validation des limites (`len(grille)`, `len(grille[0])`) et des murs (case == 1), puis mise à jour des attributs d'instance (`self.x`, `self.y`) et modification de la liste 2D globale `grille[y][x]`.

**Races/Classes** : Attributs de classe (`Personnage.races`, `Personnage.classes`) contenant dictionnaires imbriqués, stats et inventaire partagés par race (référence mutable), armes et sorts par classe.

**Portes** : Vérification avec `.get()` sur l'inventaire de la race (dictionnaire partagé), déduction si suffisant (`-=`), modification de la grille (`grille[y][x] = 5`) et mise à jour du dictionnaire `etat`.

**Génération de monstres** : `choice()` aléatoire parmi les clés des dictionnaires `Monstre.races.keys()` et `Monstre.classes.keys()`, puis instanciation avec `__init__()` utilisant les stats correspondantes.

**Coffres** : `randint(1,3)` pour choisir entre potion (`+= 1`), or (`randint(10, 100)`), ou os de poulet (`+= 3`), ajouté à l'inventaire partagé de la race via `.get()` avec valeur par défaut.

**Sorts** : Dictionnaire de sorts par classe (`Personnage.classes[classe]["sorts"]`), suppression après utilisation (`del` sur la clé), dégâts fixes appliqués via `decrement_PV()`.

**Pillage** : Itération sur l'inventaire du monstre avec `for element, quantite in monstre.races[...].items()`, ajout/incrémentation conditionnel (`if element in ...` puis `+=` ou assignation) dans l'inventaire partagé de la race du héros.

Projet réalisé dans le cadre du DM de spécialité NSI "Donjon & Dragon"
Made with 💖 By Lekieffre Thomas et Marchal Zoé