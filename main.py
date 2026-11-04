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

        chances  5
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

def creer_grille():    #Matias
    grille = [
        # x=0  x=1  x=2  x=3  x=4  x=5  x=6  x=7 x=8
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 0
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 1
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 2
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 3
        [0, 0, 0, 0, 0, 0, 0, 0],  # y = 4
        [0, 0, 0, 0, 0, 0, 0, 0]   # y = 5
    ]
    return grille

def afficher_grille(grille):    #Jorge
    for ligne in grille:
        print(ligne)

def placer_bateau():    #Maxime important pas encore fini rappel
    # au moins 2 bateau max taille dun bateau 4 min 2
    ligne_bateau = random.randint(0, 5)
    colonne_bateau = random.randint(0, 7)
    return ligne_bateau, colonne_bateau

def demander_coordonnees():    #Matias
    ligne = int(input("Numéro de ligne (0-5): "))
    colonne = int(input("Numéro de colonne (0-7): "))
    return colonne, ligne

def verifier_coordonnees(colonne, ligne):    #Maxime
    if ligne >= 0 and ligne <= 5 and colonne >= 0 and colonne <= 7:
        return True
    else:
        print("Coordonnées invalides")
        return False

def verifier_tir(ligne, colonne, ligne_bateau, colonne_bateau):    #Jorge
    if ligne == ligne_bateau and colonne == colonne_bateau:
        print("Bravo ! Vous avez trouvé le bateau !")
        return True
    else:
        print("Tir raté !\n")
        return False

def partie_terminer(chances, bateau_trouve):    #Matias
    if chances == 0 or bateau_trouve is True:
        return True
    else:
        return False

def calculer_statistiques(tirs, bateau_trouve, stats):    #Maxime
    print("\n" + "=" * 30)
    print(" STATISTIQUES DE LA PARTIE")
    print(f"• Tirs effectués cette partie : {tirs}")
    if bateau_trouve:
        print("• Résultat : Victoire ")
    else:
        print("• Résultat : Défaite ")

    print("\n STATISTIQUES GLOBALES")
    print(f"• Victoires totales : {stats['Victoire']}")
    print(f"• Défaites totales : {stats['Défaite']}")
    print(f"• Tirs totaux cumulés : {stats['Tirs']}")
    print("=" * 30 + "\n")


if __name__ == "__main__":    #Maxime, Jorge, Matias
    recommencer = "oui"

    stats = {
        "Victoire": 0,
        "Défaite": 0,
        "Tirs": 0
    }

    while recommencer == "oui":
        grille = creer_grille()
        afficher_grille(grille)

        ligne_bateau, colonne_bateau = placer_bateau()

        tirs = 0
        chances = 5
        bateau_trouve = False

        while partie_terminer(chances, bateau_trouve) is False:
            ligne, colonne = demander_coordonnees()

            if verifier_coordonnees(ligne, colonne) is True:
                tirs = tirs + 1
                stats["Tirs"] = stats["Tirs"] + 1

                bateau_trouve = verifier_tir(ligne, colonne, ligne_bateau, colonne_bateau)

                if bateau_trouve is False:
                    chances = chances - 1
                    print(f"Il vous reste {chances} chance(s).\n")

                afficher_grille(grille)
            else:
                print("Veuillez entrer de nouvelles coordonnées\n")

        # Fin de partie
        if bateau_trouve is False:
            print(f"Le bateau était caché à la ligne {ligne_bateau}, colonne {colonne_bateau}")
            stats["Défaite"] = stats["Défaite"] + 1
        else:
            stats["Victoire"] = stats["Victoire"] + 1

        # Affichage des stats avec les données mises à jour
        calculer_statistiques(tirs, bateau_trouve, stats)

        recommencer = input("Voulez-vous recommencer (oui/non) : ").lower().strip()    #lower mets tout en lower case et strip enleve les espaces inutile
        print("\n" + "=" * 40 + "\n")

    print("Merci d'avoir joué !")






