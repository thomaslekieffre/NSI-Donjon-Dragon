grille = []
with open("carte.txt", "r") as f:
    for ligne in f:
        l=[]
        for char in ligne.split():
            l.append(int(char))
        grille.append(l)
        
        
def afficher():
        for ligne in grille:
            for element in ligne:
                if element==1: print("◼️️",end=" ")
                elif element==2: print(" _ ",end=" ")
                elif element==3: print("🎁",end=" ")
                elif element==4: print("👾",end=" ")
                elif element==5: print("🧍🏽‍♀️",end=" ")
                else: print("  .  ",end=" ")
            print()
        
afficher()