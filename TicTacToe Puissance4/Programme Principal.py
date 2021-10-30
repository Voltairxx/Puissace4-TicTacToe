###########################################################
#                                                         #
#                     Importation module                  #
#                                                         #
###########################################################


from random import *
from time import *
import sys


def choix_jeu():
    while True:
        choix=input("Quel jeu souhaitez vous choisir, le puissance 4 ou le tic tac toe (aussi appelé morpion) ?")
        if choix=="morpion" or choix=="tic-tac-toe" or choix=="tic tac toe":
            sys.path.append("tic_tac_toe")
            module="tic_tac_toe"
            return __import__(module)
        elif choix=="puissance_4" or choix=="puissance 4":
            sys.path.append("puissance_4")
            module="puissance_4"
            return __import__(module)


###########################################################
#                                                         #
#                Fonctions principales du jeu             #
#                                                         #
###########################################################


def nom_joueurs():
    """
    Fonction qui demande les noms des deux joueurs
    :return: Les noms des deux joueurs
    :rtype: tuple
    """
    print("Pour jouer contre une IA mettez ordinateur comme nom du joueur")
    j1=input("Quel sera le nom du joueur 1 ?")
    j2=input("Quel sera le nom du joueur 2 ?")
    print("Ce sont des noms ... particuliers")
    return (j1,j2)

def premier_joueur(joueur1, joueur2):
    """
    Fonction qui détermine au hasard le joueur qui jouera en premier
    :param: joueur_1 Nom du joueur 1
            joueur_2 Nom du joueur 2
    :param_type: joueur_1(str), joueur_2(str)
    :return: Nom du joueur qui commence
    :rtype: str
    """
    return choice([joueur1,joueur2])

def changer_joueur(joueur_courant, joueur1, joueur2):
    """
    Fontion qui change le joueur courant
    :param: joueur_courant Nom du joueur courant
            joueur1 Nom du joueur 1
            joueur2 Nom du joueur 2
    :param_type: joueur_courant(str), joueur_1(str), joueur_2(str)
    :return: Nom du joueur courant
    :rtype: str
    """
    if joueur_courant==joueur1:
        return joueur2
    else:
        return joueur1
    
def jouer():
    """
    Fonction principale du jeu
    """
    module=choix_jeu()
    joueur1,joueur2=nom_joueurs()
    if joueur1=="ordinateur" or joueur1=="ordi" or joueur1=="IA" or joueur1=="ia" or joueur2=="ordinateur" or joueur2=="ordi" or joueur2=="IA" or joueur2=="ia":
        profondeur=choix_profondeur()
    situation=module.initialiser_jeu()
    module.afficher_situation(situation)
    joueur_courant=premier_joueur(joueur1, joueur2)
    test=module.tester(situation, joueur_courant, joueur1)
    while module.fin_jeu(test, situation)==False:
        module.afficher_joueur(joueur_courant)
        if module.existence_coup(situation)==True:
            if joueur_courant=="ordinateur" or joueur_courant=="ordi" or joueur_courant=="IA" or joueur_courant=="ia":
                valeur,coup_suivant=min_max(module,situation,profondeur,joueur_courant,joueur1,joueur2)
                coup=module.choix_ordinateur(situation,coup_suivant)
                situation=module.miseajour_situation(coup,situation,joueur_courant,joueur1)
                module.afficher_choix(coup,joueur_courant)
            else:
                liste_coups=module.coups_autorises(situation)
                module.afficher_coups(liste_coups)
                coup=module.choix_coups(liste_coups)
                situation=module.miseajour_situation(coup,situation,joueur_courant,joueur1)
                module.afficher_choix(coup,joueur_courant)
            module.afficher_situation(situation)
            test=module.tester(situation, joueur_courant, joueur1)
        if module.fin_jeu(test, situation)==False:
            joueur_courant=changer_joueur(joueur_courant, joueur1, joueur2)
    module.resultat(test, joueur_courant)
    

###########################################################
#                                                         #
#                Fonctions liées à l'IA                   #
#                                                         #
###########################################################


def choix_profondeur():
    """
    Fonction que demande la profondeur de recherche de l'algorithme
    :return: Profondeur
    :rtype: int
    """
    print("Profondeur : 2 Mode Facile")
    print("Profondeur : 3 Mode Normal")
    print("Profondeur : 4 Mode Difficile")
    choix=input("Quelle profondeur désirez vous pour l'algorithme de recherche de l'IA ?")
    return int(choix)


def coefficient(tuple_valeur,joueur_courant):
    """
    Fonction qui détermine si le coefficient sera positif ou négatif
    :param: joueur_courant(str) Nom du joueur courant
            tuple_valeur(tule(int,list())) Tuple contenant la valeur et le coup joué
    :return: (valeur,coup_joué ou (-valeur,coup_joué)
    rtype: tuple
    """
    if joueur_courant=="ordinateur" or joueur_courant=="ordi" or joueur_courant=="IA" or joueur_courant=="ia":
        return tuple_valeur
    else:
        return (tuple_valeur[0]*-1,tuple_valeur[1])


def min_max(module,situation,profondeur,joueur_courant,joueur1,joueur2,tour=0):
    """
    Fonction qui gère l'intelligence artificilelle
    :param: module Module du jeu
            situation(list(list(str))) Situation actuelle du jeu
            profondeur(int) Profondeur de l'arbre  de recherhe
            joueur_courant(str) Nom du joueur courant
            joueur1(str) Nom du joueur 1
            joueur2(str) Nom du joueur 2
            tour(int) Determine à quel niveau on se trouve dans l'arbre de recherche
    :return: Un tuple comportant la situation la plus favorable à l'odinateur ainsi que sa valeur
    :rtype: tuple
    """
    test=module.tester(situation, joueur_courant, joueur1)
    if module.fin_jeu(test, situation) or profondeur==tour:
        return coefficient(module.evaluation(situation,joueur_courant,joueur1),joueur_courant)
    else:
        if tour!=0:
            joueur_courant=changer_joueur(joueur_courant, joueur1, joueur2)
        situations_suivantes=[module.miseajour_situation_ordinateur(coup, situation, joueur_courant, joueur1) for coup in module.coups_autorises(situation)]
        if joueur_courant=="ordinateur" or joueur_courant=="ordi" or joueur_courant=="IA" or joueur_courant=="ia":
            liste=[]
            for situations in situations_suivantes:
                liste.append(min_max(module,situations,profondeur,joueur_courant,joueur1,joueur2,tour+1))
            print(liste)
            liste_valeur=[liste[i][0] for i in range(len(liste))]
            print(liste_valeur)
            valeur_max=max(liste_valeur)
            print("max : ",valeur_max)
            indice=liste_valeur.index(valeur_max)
            coups_suivant=module.miseajour_situation_ordinateur(module.choix_ordinateur(situation,liste[indice][1]), situation, joueur_courant, joueur1)
        else:
            liste=[]
            for situations in situations_suivantes:
                liste.append(min_max(module,situations,profondeur,joueur_courant,joueur1,joueur2,tour+1))
            print(liste)
            liste_valeur=[liste[i][0] for i in range(len(liste))]
            print(liste_valeur)
            valeur_min=min(liste_valeur)
            print("min : ",valeur_min)
            indice=liste_valeur.index(valeur_min)
            coups_suivant=module.miseajour_situation_ordinateur(module.choix_ordinateur(situation,liste[indice][1]), situation, joueur_courant, joueur1)
        return (liste_valeur[indice],coups_suivant)


jouer()


