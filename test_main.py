import pytest
from main import *
from échauffement_liste import resultat


def test_verifier_coordonnees():       #Jorge
    ligne = 9
    colonne = 9
    resultat_attendu = False
    assert verifier_coordonnees(ligne, colonne) == resultat_attendu

def test_verifier_bateau():    #Maxime
    ligne_bateau = 0
    colonne_bateau = 0
    ligne = 0
    colonne = 0
    resultat_attendu = True
    assert verifier_tir(ligne, colonne, ligne_bateau, colonne_bateau) == resultat_attendu

def test_partie_terminer():    #Matias
    chance = 1
    bateau_trouve = False
    resultat_attendu = False
    assert partie_terminer(chance, bateau_trouve) == resultat_attendu

def test_calculer_statistique():    #Matias et Maxime
    stats = {
        "Victoire": 4,
        "Défaite": 2,
        "Tirs": 27
    }
    resultat_attendu_1 = 4
    resultat_attendu_2 = 2
    resultat_attendu_3 = 27
    assert stats["Victoire"] == resultat_attendu_1
    assert stats["Défaite"] == resultat_attendu_2
    assert stats["Tirs"] == resultat_attendu_3
