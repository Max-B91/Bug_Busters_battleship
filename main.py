"""
FONCTION creer_grille():
    Créer une grille de 6 lignes et 8 colonnes
    Remplir toutes les cases avec "0"
    RETOURNER grille


FONCTION afficher_grille(grille):
    POUR chaque ligne dans grille:
        AFFICHER la ligne


FONCTION placer_bateau():
    Choisir au hasard une ligne entre 0 et 5
    Choisir au hasard une colonne entre 0 et 7
    RETOURNER ligne_bateau et colonne_bateau


FONCTION demander_coordonnees():
    DEMANDER au joueur d'entrer une ligne entre 0 et 5
    DEMANDER au joueur d'entrer une colonne entre 0 et 7
    RETOURNER ligne et colonne


FONCTION verifier_coordonnees(ligne, colonne):
    SI la ligne est entre 0 et 5 ET la colonne est entre 0 et 7:
        RETOURNER VRAI
    SINON:
        AFFICHER "Coordonnées invalides"
        RETOURNER FAUX


FONCTION verifier_tir(ligne, colonne, ligne_bateau, colonne_bateau):
    SI la ligne correspond à la ligne du bateau ET
       la colonne correspond à la colonne du bateau:
        AFFICHER "Bravo ! Vous avez trouvé le bateau !"
        RETOURNER VRAI
    SINON:
        AFFICHER "Tir raté !"
        RETOURNER FAUX


FONCTION partie_terminer(chances, bateau_trouve):
    SI chances est égal à 0 OU bateau_trouve est VRAI:
        RETOURNER VRAI
    SINON:
        RETOURNER FAUX


FONCTION calculer_statistiques(tirs, bateau_trouve):
    AFFICHER le nombre de tirs effectués
    SI bateau_trouve est VRAI:
        AFFICHER "Victoire"
    SINON:
        AFFICHER "Défaite"


PROGRAMME PRINCIPAL
    recommencer  "oui"

    TANT QUE recommencer est égal à "oui":

        grille  creer_grille()
        afficher_grille(grille)

        ligne_bateau, colonne_bateau  placer_bateau()

        chances  15
        tirs  0
        bateau_trouve  FAUX

        TANT QUE partie_terminer(chances, bateau_trouve) est FAUX:

            ligne, colonne  demander_coordonnees()

            SI verifier_coordonnees(ligne, colonne) est VRAI:

                tirs  tirs + 1

                bateau_trouve  verifier_tir(
                    ligne, colonne,
                    ligne_bateau, colonne_bateau
                )

                SI bateau_trouve est FAUX:
                    chances  chances - 1

                afficher_grille(grille)

            SINON:
                AFFICHER "Veuillez entrer de nouvelles coordonnées"

        SI bateau_trouve est FAUX:
            AFFICHER la position du bateau

        calculer_statistiques(tirs, bateau_trouve)

        DEMANDER au joueur s'il veut recommencer
        LIRE recommencer

    AFFICHER "Merci d'avoir joué !"
"""
import random

def creer_grille():  # Matias
    grille = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    return grille

def afficher_grille(grille):  # Jorge
    print("\n   0  1  2  3  4  5  6  7")  # Affiche les numéros des colonnes
    for i in range(len(grille)):
        print(i, grille[i])  # Affiche le numéro et le contenu de chaque ligne

def placer_bateau():  # Maxime
    taille_bateau = random.randint(2, 4)
    orientation = random.choice(["horizontal", "vertical"])

    if orientation == "horizontal":
        ligne_bateau = random.randint(0, 5)
        colonne_bateau = random.randint(0, 8 - taille_bateau)   # Choisit une colonne de départ qui permet au bateau de rester dans la grille
    else:
        ligne_bateau = random.randint(0, 6 - taille_bateau)  # Choisit une ligne de départ qui permet au bateau de rester dans la grille
        colonne_bateau = random.randint(0, 7)

    lignes = []
    colonnes = []

    if orientation == "horizontal":
        for i in range(taille_bateau):
            lignes.append(ligne_bateau)
            colonnes.append(colonne_bateau + i)
    else:
        for i in range(taille_bateau):
            lignes.append(ligne_bateau + i)
            colonnes.append(colonne_bateau)

    return lignes, colonnes

def demander_coordonnees():  # Matias
    ligne = int(input("Numéro de ligne (0-5) : "))
    colonne = int(input("Numéro de colonne (0-7) : "))

    return ligne, colonne

def verifier_coordonnees(ligne, colonne):  # Maxime
    if ligne >= 0 and ligne <= 5 and colonne >= 0 and colonne <= 7:
        return True
    else:
        print("Coordonnées invalides")
        return False

def verifier_tir(ligne, colonne, lignes_bateau, colonnes_bateau, cases_touchees):  # Jorge
    for i in range(len(lignes_bateau)):
        if ligne == lignes_bateau[i] and colonne == colonnes_bateau[i]:
            print("Bravo ! Vous avez touché le bateau !")
            cases_touchees.append((ligne, colonne))

            if len(cases_touchees) == len(lignes_bateau):
                print("Félicitations ! Vous avez trouvé tout le bateau !")
                return True

            return False

    print("Tir raté !")
    return False

def partie_terminer(chances, bateau_trouve):  # Matias
    if chances == 0 or bateau_trouve is True:
        return True
    else:
        return False

def calculer_statistiques(tirs, bateau_trouve, stats):  # Maxime
    print("\n" + "=" * 30)
    print(" STATISTIQUES DE LA PARTIE")
    print(f"• Tirs effectués cette partie : {tirs}")

    if bateau_trouve:
        print("• Résultat : Victoire")
    else:
        print("• Résultat : Défaite")

    print("\n STATISTIQUES GLOBALES")
    print(f"• Victoires totales : {stats['Victoire']}")
    print(f"• Défaites totales : {stats['Défaite']}")
    print(f"• Tirs totaux cumulés : {stats['Tirs']}")
    print("=" * 30 + "\n")

if __name__ == "__main__":  # Maxime, Jorge, Matias

    recommencer = "oui"

    stats = {
        "Victoire": 0,
        "Défaite": 0,
        "Tirs": 0
    }

    while recommencer == "oui":

        grille = creer_grille()
        afficher_grille(grille)

        lignes_bateau, colonnes_bateau = placer_bateau()
        cases_touchees = []

        tirs = 0
        chances = 15
        bateau_trouve = False

        while partie_terminer(chances, bateau_trouve) is False:

            ligne, colonne = demander_coordonnees()

            if verifier_coordonnees(ligne, colonne) is True:

                if grille[ligne][colonne] != 0:
                    print("Vous avez déjà tiré sur cette case !\n")
                    continue

                tirs = tirs + 1
                stats["Tirs"] = stats["Tirs"] + 1

                bateau_trouve = verifier_tir(
                    ligne,
                    colonne,
                    lignes_bateau,
                    colonnes_bateau,
                    cases_touchees
                )

                if (ligne, colonne) in cases_touchees:
                    grille[ligne][colonne] = "X"
                else:
                    grille[ligne][colonne] = "-"
                    chances = chances - 1
                    print(f"Il vous reste {chances} chance(s).\n")

                afficher_grille(grille)

            else:
                print("Veuillez entrer de nouvelles coordonnées.\n")

        if bateau_trouve is False:
            print("Vous avez perdu !")
            print(
                f"Le bateau était caché aux coordonnées : "
                f"{list(zip(lignes_bateau, colonnes_bateau))}"
            )  # Combine les lignes et les colonnes pour former les coordonnées du bateau
            stats["Défaite"] = stats["Défaite"] + 1

        else:
            stats["Victoire"] = stats["Victoire"] + 1

        calculer_statistiques(tirs, bateau_trouve, stats)

        recommencer = input(
            "Voulez-vous recommencer (oui/non) : "
        ).lower().strip()

        print("\n" + "=" * 40 + "\n")

    print("Merci d'avoir joué !")
