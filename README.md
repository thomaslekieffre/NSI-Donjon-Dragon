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

Projet réalisé dans le cadre du DM de spécialité NSI "Donjon & Dragon"
Made with 💖 By Lekieffre Thomas et Marchal Zoé