# coding: utf-8
import os
import random

reset = True

while reset:

    # Variables
    continu = True
    niveauBool = True
    compteur = int(0)
    resetChoix = str()

    # Détermination des bornes et du nombre aléatoire
    while niveauBool:
        print(" ——————————————————————————————————————")
        print("| Choississez un niveau de difficulté: |")
        print("| 1 - Facile                           |")
        print("| 2 - Moyen                            |")
        print("| 3 - Difficile                        |")
        print(" ——————————————————————————————————————")
        niveau = int(input(" Niveau: "))
        print(" ——————————————————————————————————————")

        if niveau == 1:
            borne = int(10)
            resultat = (random.randrange(10) + 1)
            niveauBool = False
        elif niveau == 2:
            borne = int(50)
            resultat = (random.randrange(50) + 1)
            niveauBool = False
        elif niveau == 3:
            borne = int(100)
            resultat = (random.randrange(100) + 1)
            niveauBool = False

    # Lancement du Jeu !
    while continu:
        choix = int(0)

        while not(0 < choix <= borne):

            print(" Choisissez un nombre entre 1 et", borne, ": ")
            choix = int(input(" Choix: "))

        if resultat == choix:
            continu = False
        elif resultat > choix:
            print(" Plus !")
        elif resultat < choix:
            print(" Moins !")
        print(" --------------------------------------")

        compteur += 1

    # Affichage suite victoire
    print(" ——————————————————————————————————————")
    print("| Super ! vous avez gagné en", compteur, "coups ! |")
    print(" ——————————————————————————————————————")

    # Nouvelle partie ?
    while resetChoix.lower() != "o" and resetChoix.lower() != "n":
        print(" Voulez-vous faire une nouvelle partie ? O/N")
        resetChoix = input(" Choix: ")

    # Arrêt du jeu
    if resetChoix.lower() == "n":
        print (" Merci d'avoir joué et à bientôt !")
        reset = False

# System en pause à la fin de la partie
os.system("pause")
