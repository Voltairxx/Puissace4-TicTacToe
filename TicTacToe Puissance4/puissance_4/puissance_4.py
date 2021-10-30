"""
:name: Module Puissance 4

:author: Herbert Viltourbidon

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

###########################################################
#                                                         #
#                         Affichage                       #
#                                                         #
###########################################################

def afficher_joueur(joueur_courant):
    """
    Affiche le nom du joueur courant
    :param: joueur_courant Nom du joueur courant
    :param_type: joueur_courant(str)
    :return: None
    """
    print("C'est le tour de :",joueur_courant)

def afficher_coups(coups):
    """
    Affiche les coupq possibles du joueur courant
    :param: coups Liste des coups possibles
    :param_type: coups(list(tuple))
    :return: None
    """
    print("Choisissez vertueusement :",coups)

def afficher_choix(choix, joueur_courant):
    """
    Affiche le choix du joueur courant
    :param: choix Coup choisi
            joueur_courant Nom du joueur courant
    :param_type: choix(tuple(int)) joueur_courant(str)
    :return: None
    """
    print(joueur_courant,"choisi de jouer son pion dans la colonne n°",choix," (je n'aurais pas fais ça mais bon...)")

def afficher_situation(situation):
    """
    Affiche la situation courante
    :param: situation Situation du jeu 
    :param_type: situation(list(list))
    :return: None
    """
    print(" +---+---+---+---+---+---+---+")
    for i in range(len(situation)):
        print(" | ",end="")
        for j in range(len(situation[0])):
            print(situation[i][j],"| ",end="")
        print("\n","+---+---+---+---+---+---+---+")
    print("   0   1   2   3   4   5   6")
            
def resultat(test, joueur_courant):
    """
    Affiche le vainqueur ou le match nul
    :param: test Booléen qui dis si oui ou non il y a victoire
            joueur_courant Nom du joueur courant
    :param_type: test(bool), joueur_courant(str)
    :return: None
    """
    if test==True:
        print(joueur_courant,"a fait découvrir le goût de la défaite et de la honte à son ennemi !")
    else:
        print("Vous êtes tellement incompétents que personne n'a gagné !")

###########################################################
#                                                         #
#                  Initialisation du jeu                  #
#                                                         #
###########################################################

def initialiser_jeu():
    """
    Fonction qui initialise un jeu de puissance 4
    :return: Situation initiale
    :rtype: list(list())
    """
    return [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]

###########################################################
#                                                         #
#                  Fonction utilitaire                    #
#                                                         #
###########################################################

def recherche_symbole(joueur_courant, joueur1):
    """
    Fonction qui recherche le symbole en fonction du joeur courant
    :param: joueur_courant Nom du joueur courant
            joueur1 Nom du joueur 1
    :param_type: joueur_courant(str) ,joueur1(str)
    :return: Symbole du joueur courant
    :rtype: str
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
    Fonction qui vérifie s'il y a encore des coups possibles à jouer
    :param: situation Situation du jeu
    :param_type: situation(list(list))
    :return: Booléen
    :rtype: bool
    """
    for j in situation[0]:
        if j==" ":
            return True
    return False
            
def coups_autorises(situation):
    """
    Fonction qui determine les coups authorisés
    :param: situation Situation du jeu
    :param_type: situation(list(list))
    :return: Liste des coups authorisés
    :rtype: list(int)
    """
    coups=[]
    for i in range(len(situation)-1,-1,-1):
        for j in range(len(situation[0])):
            if situation[i][j]==" ":
                if j not in coups:
                    coups.append(j)
    return coups
                

def choix_coups(liste_coups):
    """
    Fonction qui réalise le choix du coup à jouer
    :param: liste_coups Liste des coups possibles
    :param_type: liste_coups(list(int))
    :return: Le coup choisi
    :rtype: int
    """
    coup=input("Dans quelle colonne désirez vous placer votre jeton ?")
    while coup!="0" and coup!="1" and coup!="2" and coup!="3" and coup!="4" and coup!="5" and coup!="6":
        print("Il faut mettre le numéro d'une colone si tu veux un jour gagner !")
        coup=input("Dans quelle colonne désirez vous placer votre jeton ?")
    coup=int(coup)
    while not(coup in liste_coups):
        print("Il faut jouer un des coups proposés")
        coup=int(input("Dans quelle colonne désirez vous placer votre jeton ?"))
    return coup

###########################################################
#                                                         #
#                  Mise à jour situation                  #
#                                                         #
###########################################################

def miseajour_situation(choix, situation, joueur_courant, joueur1):
    """
    Fonction qui met à jour la situation suite au couop choisi
    :param: choix Coup à jouer
            situation Situation actuelle du jeu
            joueur_courant Nom du joueur qui est en train de jouer son tour
            joueur_1 Nom du joueur 1
    :param_type: choix(int), situation(list(list(str))), joueur_courant(str), joueur_1(str)
    :return: Situation mis à jour
    :rtype: list(list(str)))
    """
    jeton=recherche_symbole(joueur_courant, joueur1)
    for i in range(len(situation)):
        if situation[i][choix]=="X" or situation[i][choix]=="O":
            situation[i-1][choix]=jeton
            return situation
        elif i==len(situation)-1 and situation[i][choix]==" ":
            situation[i][choix]=jeton
            return situation
        

###########################################################
#                                                         #
#                  Détection fin du jeu                   #
#                                                         #
###########################################################

def test_quatre_cases(i, j, situation, symbole, di, dj):
    """
    Fonction qui teste si quatre mêmes jetons sont alignés
    :param: i Abscisse
            j Ordonnée
            situation Situation actuelle du jeu
            symbole Symbole du jeton
            di Direction en abscisse
            dj Direction en odronnée
    :param_type: i(int), j(int), situation(list(list(str))), symbole(str), di(int), dj(int)
    :return: Booléen
    :rtype: bool
    """
    for n in range(4):
        if situation[i][j]!=symbole:
            return False
        i=i+di
        j=j+dj
    return True
    
def test_lignes(situation, symbole):
    """
    Fonction qui teste pour une ligne
    :param: situation Situation actuelle du jeu
            symbole Symbole du jeton
    :param_type: situation(list(list(str))), symbole(str)
    :return: Booléen
    :rtype: bool
    """
    n=0
    for ligne in range(len(situation)):
        for colonne in range(len(situation[0])):
            if situation[ligne][colonne]==symbole:
                n=n+1
            elif situation[ligne][colonne]!=symbole:
                n=0
            if n==4:
                return True
        n=0
    return False

def test_colonnes(situation, symbole):
    """
    FOnction qui teste pour les colonnes
    :param: situation Situation actuelle du jeu
            symbole Symbole du jeton
    :param_type: situation(list(list(str))), symbole(str)
    :return: Booléen
    :rtype: bool
    """
    n=0
    for j in range(len(situation[0])):
        for i in range(len(situation)):
            if situation[i][j]==symbole:
                n=n+1
            elif situation[i][j]!=symbole:
                n=0
            if n==4:
                return True
        n=0
    return False

def test_diagonales(situation, symbole):
    """
    FOnction qui teste pour les diagonales
    :param: situation Situation actuelle du jeu
            symbole Symbole du jeton
    :param_type: situation(list(list(str))), symbole(str)
    :return: Booléen
    :rtype: bool
    """
    for i in range(0,3):
        for j in range(0,4):
            test1=test_quatre_cases(i, j, situation, symbole,1,1)
            if test1==True:
                return test1    
    for i in range(0,3):
        for j in range(3,7):
            test2=test_quatre_cases(i, j, situation, symbole,1,-1)
            if test2==True:
                return test2
    return False

def tester(situation, joueur_courant, joueur1):
    """
    Fonction qui réalise les tests de victoires
    :param: situation Situation actuelle du jeu
            joueur_courant Nom du joueur à qui c'est le tour
            joueur1 Nom du joueur 1
    :param_type: situation(list(list(str))), joueur_courant(str), joueur1(str)
    :return: Booléen
    :rtype: bool
    """
    symbole=recherche_symbole(joueur_courant, joueur1)
    test1=test_lignes(situation, symbole)
    test2=test_colonnes(situation, symbole)
    test3=test_diagonales(situation, symbole)
    return test1 or test2 or test3
    

def fin_jeu(test, situation):
    """
    Fonction qui détermine si le jeu est fini ou non
    :param: test Booléen de la victoire
            situation Situation actuelle du jeu
     :param_type: test(bool), situation(list(list(str)))
     :return: Booléen
     :rtype: bool
     """
    return test and existence_coup(situation)


###########################################################
#                                                         #
#                Fonctions liées à l'IA                   #
#                                                         #
###########################################################


def choix_ordinateur(situation,coup_suivant):
    """
    Fonction qui retrouve le choix de l'ordinateur et qui renvoie la coordonnée de ce choix
    :param: situation(list(list(str))) Situation actuelle du jeu
            coup_suivant(list(list(str))) Situation la plus favorable pour l'IA
            valeur(int) Valeur de l'évaluation de la situation la plus favorable à l'IA
            joueur_courant(str) Nom du joueur courant
    :return: La coordonnée du choix de l'IA
    :rtype: int
    """
    for i in range(len(situation)):
        for j in range(len(situation[0])):
            if situation[i][j]!=coup_suivant[i][j]:
                return j


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
    return (evaluation_ligne(situation,symbole)+ evaluation_colonne(situation,symbole)+ evaluation_diagonale(situation,symbole),situation)


def evaluation_ligne(situation,symbole):
    """
    Fontion qui évalue la valeur des lignes d'une situation
    :param: situation(list(list(str))) Situation actuelle du jeu
            symbole(str) Symbole du joueur courant
    :return: Valeur des lignes de la situation
    :rtype: int
    """
    valeur=0
    for x in range(4):
        for y in range(6):
            valeur=valeur+valeur_4_cases(situation[y][x:x+4],symbole)
    return valeur


def evaluation_colonne(situation,symbole):
    """
    Fontion qui évalue la valeur des colonnes d'une situation
    :param: situation(list(list(str))) Situation actuelle du jeu
            symbole(str) Symbole du joueur courant
    :return: Valeur des colonnes de la situation
    :rtype: int
    """
    valeur=0
    for x in range(7):
        for y in range(3):
            liste=[situation[y][x],situation[y+1][x],situation[y+2][x],situation[y+3][x]]
            valeur=valeur+valeur_4_cases(liste,symbole)
    return valeur


def evaluation_diagonale(situation,symbole):
    """
    Fontion qui évalue la valeur des diagonales d'une situation
    :param: situation(list(list(str))) Situation actuelle du jeu
            symbole(str) Symbole du joueur courant
    :return: Valeur des diagonales de la situation
    :rtype: int
    """
    valeur=0
    for x in range(4):
        for y in range(3):
            liste=[situation[y][x],situation[y+1][x+1],situation[y+2][x+2],situation[y+3][x+3]]
            valeur=valeur+valeur_4_cases(liste,symbole)
    for x in range(3,7):
        for y in range(3):
            liste=[situation[y][x],situation[y+1][x-1],situation[y+2][x-2],situation[y+3][x-3]]
            valeur=valeur+valeur_4_cases(liste,symbole)
    return valeur


def valeur_4_cases(liste,symbole):
    """
    Fonction qui renvoie la valeur d'une liste en fonction de son contenu
    :param: liste(list(str)) Une liste de 4 élements
            symbole(str) Symbole du joueur courant
    :return: Valeur de la liste
    :rtype: int
    """
    if symbole in liste:
        x=0
        for i in liste:
            x=x+int(symbole==i)
        if x==4:
            return 10000
        elif x==3:
            return 100
        elif x==2:
            return 10
        else:
            return 1
    else:
        return 0
        



















