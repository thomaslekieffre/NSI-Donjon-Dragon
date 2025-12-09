grille = []
with open("carte.txt", "r") as f:
    for ligne in f:
        l=[]
        for char in ligne.split():
            l.append(int(char))
        grille.append(l)
        
        
def afficher():
        symbols = {
            0: ".",
            1: "◼",
            2: "_",
            3: "⊞",
            4: "☻",
            5: "♀",
        }
        print("\n=== Carte ===")
        for ligne in grille:
            print(" ".join(symbols.get(element, "?") for element in ligne))
        print("Légende: ◼ mur | _ porte | ⊞ coffre | ☻ monstre | ♀ héros | . vide")
        
afficher()