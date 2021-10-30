"""
:name: Tic Tac Toe

:author: Jean Pierre Pernautt 

:date: Avril 2021

Fonctionnalités:
initialiser_jeu() Fonction qui crée la situation initiale
fin_jeu(test,situation,joueur_courant) Fonction qui détermine si le jeu est terminé ou non
existence_coup(situation,joueur_courant) Prédicat qui teste s'il reste oui ou non des coups possibles
coups_authorises(situation) Fonction qui détermine mes coups possibles du joueur
resultat(test,situation,joueur_courant) Fonction qui affiche le vainqueur ou le match nul
afficher_joueur(joueur_courant) Fonction qui affiche le joueur courant
afficher_coups(coups) Fonction qui affiche les coups possibles du joueur
choix_coup(liste_coups) fonction qui renvoie le coup choisi par le joueur
afficher_choix(choix,joueur_courant) Fonction qui affihe le coup choisi par le joueur
miseajour_situation(choix,situation,joueur_courant,joueur1) Fonction qui met à jour la situation avec le coup joué
afficher_situation(situation) Fonction qui affiche la situation actuelle du jeu
choix_ordinateur(situation,coup_suivant) Fonction qui retrouve le choix de l'ordinateur et qui renvoie la coordonnée de ce choix
miseajour_situation_ordinateur(choix, situation, joueur_courant, joueur1) Fonction qui fait la mise à jour de l'ordinateur en copiant les listes pour évter des problèmes de mutabilités
evaluation(situation,joueur_couant,joueur1) Fonction qui détermine la valeur d'une situation de jeu
"""
from copy import deepcopy
from functools import reduce

###########################################################
#                                                         #
#                         Affichage                       #
#                                                         #
###########################################################

def afficher_joueur(joueur_courant):
    """
    Cette fonction permet d'afficher le nom du joueur corant.
    : param : joueur_courant
    : param type : str
    : return : None
    """
    print("C'est au tour de " + joueur_courant + " de jouer." )

def afficher_situation(situation):
    """
    Cette fonction affiche la situation après le coup joué.
    : param : situation
    : param type : str
    : return : None
    """
    for i in range(len(situation)):
        print("+"+ "---+" * len(situation[0]), end = "\n")
        print("| ", end= "")
        for j in range(len(situation[0])):
            print(str(situation[i][j]) + " | ", end="")
        print("",end="\n")
    print("+" + "---+" * len(situation[0]), end= "\n")

def afficher_coups(coups):
    """
    Cette fonction affiche l'ensemble des coups possibles.
    : param : coups
    : param type : liste
    : return : None
    """
    print("Les coups possibles sont : "+ str(coups))

def afficher_choix(choix, joueur_courant):
    """
    Cette fonction réalise l'affichage du coup choisi.
    : param : choix
              joueur_courant
    : param type : str
                   str
    : return : None
    """
    print(joueur_courant + " a choisi de jouer " + str(choix))

def resultat(test, joueur_courant):
    """
    Cette fonction affiche le vainqueur ou match nul.
    : param : test
              joueur_courant
    : param type : booléen
                   str
    : return : None
    """
    if test == True:
        print(joueur_courant+" a gagné la partie")
    else:
        print("Personne n'a gagné vous êtes nuls")
    

###########################################################
#                                                         #
#                  Initialisation du jeu                  #
#                                                         #
###########################################################

def initialiser_jeu():
    """
    Fonction permettant d'initialiser la grille de morpion
    """
    return[[" " for _  in range(3)] for _ in range (3)]
    
###########################################################
#                                                         #
#                  Fonction utilitaire                    #
#                                                         #
###########################################################

def recherche_symbole(joueur_courant, joueur1):
    """
    Cette fonction permet d'initialiser le jeu.
    : param : None
    : param type : None
    : return : renvoie la situation initiale
    : rtype : str
    """
    if joueur_courant==joueur1:
        return "X"
    else:
        return "O"

###########################################################
#                                                         #
#                  Fonctions liées aux coups              #
#                                                         #
###########################################################

def existence_coup(situation):
    """
    Cette fonction renvoie le symbole du joueur courant.
    : param : joueur_courant
              joueur1
    : param type : str
                   str
    : return : renvoie le signe du joueur courant ("X" ou "O")
    : rtype : str
    """
    possibilité=0
    for ligne in situation:
        for case in ligne:
            if case == " ":
                possibilité+=1
    if possibilité >= 1:
        return True
    else:
        return False

def coups_autorises(situation):
    """
    Fonction permettant de determiner les differants coups possibles 
    :param: situation Situation du jeu
    :param_type: situation(list(list))
    :return: Liste des coups authorisés
    :rtype: list(int)
    """
    cord_coups_autorise=[]
    for i in range(len(situation)):
        for j in range(3):
            if situation[i][j] == " ":
                co=(i,j)
                cord_coups_autorise.append(co)
    return cord_coups_autorise

def choix_coups(liste_coups):
    """
    Fonction permettant de choisir un coup a jouer
    :param: liste_coups Liste des coups possibles
    :param_type: liste_coups(list(int))
    :return: Le coup choisi
    :rtype: int
    """
    ligne=int(input("Quelle ligne voulez vous jouer ?"))
    colonne=int(input("Quelle colonne voulez vous jouer ?"))
    choix=(ligne,colonne)
    if choix in liste_coups:
        return choix
    else:
        while not choix in liste_coups :
            ligne=int(input("Quelle ligne voulez vous jouer ?"))
            colonne=int(input("Quelle colonne voulez vous jouer ?"))
            choix=(ligne,colonne)
        return choix
            
###########################################################
#                                                         #
#                  Mise à jour situation                  #
#                                                         #
###########################################################

def miseajour_situation(choix, situation, joueur_courant, joueur1):
    """
    Fonction qui met à jour la situation suite au coup choisi
    :param: choix Coup à jouer
            situation Situation actuelle du jeu
            joueur_courant Nom du joueur qui est en train de jouer son tour
            joueur_1 Nom du joueur 1
    :param_type: choix(int), situation(list(list(str))), joueur_courant(str), joueur_1(str)
    :return: Situation mis à jour
    :rtype: list(list(str)))
    """
    i=choix[0]
    j=choix[1]
    signe=recherche_symbole(joueur_courant, joueur1)
    situation[i][j]=signe
    return situation

###########################################################
#                                                         #
#                  Détection fin du jeu                   #
#                                                         #
###########################################################

def tester_lignes(situation,symbole):
    """
    Fonction qui teste pour une ligne
    :param: situation Situation actuelle du jeu
            symbole Symbole du jeton
    :param_type: situation(list(list(str))), symbole(str)
    :return: Booléen
    :rtype: bool
    """
    for ligne in range(3) :
        if situation[ligne][0] == situation[ligne][1] == situation[ligne][2] == symbole :
            return True
    return False

def tester_colonnes(situation,symbole):
    """
    Fonction qui teste pour les colonnes
    :param: situation Situation actuelle du jeu
            symbole Symbole du jeton
    :param_type: situation(list(list(str))), symbole(str)
    :return: Booléen
    :rtype: bool
    """
    for colonne in range(3):
        if situation[0][colonne] == situation[1][colonne] == situation[2][colonne] == symbole :
            return True
    return False

def tester_diagonales(situation,symbole):
    """
     Fonction qui teste pour les diagonales
    :param: situation Situation actuelle du jeu
            symbole Symbole du jeton
    :param_type: situation(list(list(str))), symbole(str)
    :return: Booléen
    :rtype: bool
    """
    if situation[0][0] == situation[1][1] == situation[2][2] ==  symbole :
        return True
    elif situation[0][2] == situation[1][1] == situation[2][0] ==  symbole :
        return True
    return False

def tester(situation,joueur_courant,joueur1):
    """
   Fonction qui réalise les tests de victoires
    :param: situation Situation actuelle du jeu
            joueur_courant Nom du joueur à qui c'est le tour
            joueur1 Nom du joueur 1
    :param_type: situation(list(list(str))), joueur_courant(str), joueur1(str)
    :return: Booléen
    :rtype: bool
    """
    symbole = recherche_symbole(joueur_courant, joueur1)
    test = tester_lignes(situation, symbole)
    if test == False :
        test = tester_colonnes(situation, symbole)
        if test == False :
            test = tester_diagonales(situation, symbole)
    return test

def fin_jeu(test, situation):
    """
    Fonction qui détermine si le jeu est fini ou non
    :param: test Booléen de la victoire
            situation Situation actuelle du jeu
     :param_type: test(bool), situation(list(list(str)))
     :return: Booléen
     :rtype: bool
    """    
    if not test is True:
        if existence_coup(situation) == False:
            return True
        else:
            return False
    else:
        return True


###########################################################
#                                                         #
#                Fonctions liées à l'IA                   #
#                                                         #
###########################################################


def choix_ordinateur(situation,coup_suivant):
    """
    Fonction qui retrouve le choix de l'ordinateur et qui renvoie les coordonnées de ce choix
    :param: situation(list(list(str))) Situation actuelle du jeu
            coup_suivant(list(list(str))) Situation la plus favorable pour l'IA
            valeur(int) Valeur de l'évaluation de la situation la plus favorable à l'IA
            joueur_courant(str) Nom du joueur courant
    :return: Les coordonnées du choix de l'IA
    :rtype: int
    """
    for i in range(len(situation)):
        for j in range(len(situation[i])):
            if situation[i][j]!=coup_suivant[i][j]:
                return (i,j)


def miseajour_situation_ordinateur(choix, situation, joueur_courant, joueur1):
    """
    Fonction qui fait la mise à jour de l'ordinateur en copiant les listes pour évter des problèmes de mutabilités
    :param: choix Coup à jouer
            situation Situation actuelle du jeu
            joueur_courant Nom du joueur qui est en train de jouer son tour
            joueur_1 Nom du joueur 1
    :param_type: choix(int), situation(list(list(str))), joueur_courant(str), joueur_1(str)
    :return: Situation mis à jour
    :rtype: list(list(str)))
    """
    situation_suivante=deepcopy(situation)
    return miseajour_situation(choix,situation_suivante,joueur_courant,joueur1)


def evaluation(situation,joueur_courant,joueur1):
    """
    Fonction qui détermine la valeur d'une situation de jeu
    :param: situation(list(list(str))) Situation du jeu
            joueur_courant(str) Nom du joueur courant
            joueur1(str) Nom du joueur 1
    :return: Un tuple contenant la valeur et la situation
    :rtype: tuple
    """
    symbole=recherche_symbole(joueur_courant, joueur1)
    return (valeur_ligne(situation,symbole)+ valeur_colonne(situation,symbole)+ valeur_diagonale(situation,symbole),situation)


def valeur_ligne(situation,symbole):
    """
    Fontion qui évalue la valeur des lignes d'une situation
    :param: situation(list(list(str))) Situation actuelle du jeu
            symbole(str) Symbole du joueur courant
    :return: Valeur des lignes de la situation
    :rtype: int
    """
    valeur=0
    for i in situation:
        valeur=valeur+valeur_liste(i,symbole)
    return valeur


def valeur_colonne(situation,symbole):
    """
    Fontion qui évalue la valeur des colonnes d'une situation
    :param: situation(list(list(str))) Situation actuelle du jeu
            symbole(str) Symbole du joueur courant
    :return: Valeur des colonnes de la situation
    :rtype: int
    """
    valeur=0
    for x in range(3):
        liste=[situation[0][x],situation[1][x],situation[2][x]]
        valeur=valeur+valeur_liste(liste,symbole)
    return valeur

    
def valeur_diagonale(situation,symbole):
    """
    Fontion qui évalue la valeur des diagonales d'une situation
    :param: situation(list(list(str))) Situation actuelle du jeu
            symbole(str) Symbole du joueur courant
    :return: Valeur des diagonales de la situation
    :rtype: int
    """
    liste=[situation[0][0],situation[1][1],situation[2][2]]
    liste1=[situation[0][2],situation[1][1],situation[2][0]]
    return valeur_liste(liste,symbole)+valeur_liste(liste1,symbole)


def valeur_liste(liste,symbole):
    """
    Fonction qui renvoie la valeur d'une liste en fonction de son contenu
    :param: liste(list(str)) Une liste de 3 élements
            symbole(str) Symbole du joueur courant
    :return: Valeur de la liste
    :rtype: int
    """
    if symbole in liste:
        x=0
        for i in liste:
            x=reduce(lambda acc,x:acc+int(x==symbole),liste,0)
        if x==3:
            return 1000
        elif x==2:
            return 100
        else:
            return 1
    else:
        return 0
    