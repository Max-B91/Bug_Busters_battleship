import random

print("Bienvenue dans le jeu Battleship !\n")


def creer_grille():
    grille = [
        # x=0  x=1  x=2  x=3  x=4  x=5  x=6  x=7
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 1
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 2
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 3
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 4
        [0, 0, 0, 0, 0, 0, 0, 0]   # y = 5
    ]
    return grille


def placer_bateau(grille, taille):
    placer = False
    while not placer:
        orientation = random.choice(['H', 'V'])
        ligne_debut = random.randint(0, 5)   # Choisit une ligne aléatoire entre 0 et 5
        colonne_debut = random.randint(0, 7) # Choisit une colonne aléatoire entre 0 et 7

        if orientation == 'H':
            if colonne_debut + taille <= 8:
                libre = True
                for i in range(taille):
                    if grille[ligne_debut][colonne_debut + i] != 0:
                        libre = False
                        break

                if libre:
                    for i in range(taille):
                        grille[ligne_debut][colonne_debut + i] = taille
                    placer = True

        elif orientation == 'V':
            if ligne_debut + taille <= 6:
                libre = True
                for i in range(taille):
                    if grille[ligne_debut + i][colonne_debut] != 0:
                        libre = False
                        break

                if libre:
                    for i in range(taille):
                        grille[ligne_debut + i][colonne_debut] = taille
                    placer = True

    return grille


def afficher_grille(grille):
    print("\nGrille actuelle (0 = eau, X = touché, -1 = raté) :")
    for ligne in grille:
        # On crée une liste temporaire pour cacher les bateaux (> 0) au joueur
        ligne_affichage = []
        for cellule in ligne:
            if cellule > 0:
                ligne_affichage.append(0)  # Cache le bateau en affichant 0
            else:
                ligne_affichage.append(cellule)  # Affiche l'eau, 'X' ou -1
        print(ligne_affichage)
    print()


def demander_coordonnees():
    coordonnees_x = int(input("Entrez la coordonnée x (0 à 7) : "))
    coordonnees_y = int(input("Entrez la coordonnée y (0 à 5) : "))
    return coordonnees_x, coordonnees_y


def verifier_tir(grille, x, y):
    valeur = grille[y][x]
    if valeur > 0:
        grille[y][x] = 'X'  # Marque le tir réussi
        return True
    elif valeur == 0:
        grille[y][x] = -1   # Marque le tir raté
        return False
    else:
        # Déjà tiré sur cette case
        return False


def verifier_victoire(grille):
    """Vérifie s'il reste des parties de bateaux non touchées sur la grille."""
    for ligne in grille:
        for cellule in ligne:
            if isinstance(cellule, int) and cellule > 0:
                return False
    return True


