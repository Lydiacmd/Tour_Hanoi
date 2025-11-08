import Part_A
import Part_B
import turtle
import Part_E
import Button
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Variable Global
"""
Toutes les variables déclarées ici en tant que variables globales ont été choisies pour permettre une implémentation plus flexible de certaines fonctions.
Cela était nécessaire en raison de la contrainte d'avoir des arguments limités dans certaines fonctions, en raison du cahier des charges.
"""

# Nom du fichier pour sauvegarder les scores en mode solo, 
# ne sera jamais réinitialisé et servira comme historique/classement de toutes les parties jouées.
fichier_solo_score = 'score.pkl' 

# Nom du fichier pour sauvegarder les scores en mode multijoueur
# ce fichier sera réinitialisé à chaque partie en multijoueu.
fichier_multi_score = 'score_multi.pkl'

# Variable utilisée ultérieurement dans d'autres fonctions
fichier_name = '' 

# Booléen indiquant si le mode multijoueur est activé ou non.
# initialisé à False et changé lorsqu'un joueur choisit le mode multijoueur
multi = False 

# Utiliser pour afficher le score.
pen = turtle.Turtle() 

# Nombre de disques.
n = 0 

# Liste du Plateau du jeu d'Hanoï.
plateau = [] 

# Dictionnaire des coups.
coups = {} 

# Clés liées au dictionnaire des coups.
key = 0 






# Partie C : interactions avec le joueur


def tour_filtre(tour_numero): 
    """Utiliser dans la fonction tour_D()
      pour Filter le numero des tour et revois un booleen """
    return 0 <= tour_numero <= 2


def tour_D(plateau):
    """Utiliser dans lireCoordos(plateau) 
    pour filter le choix de la tour de depart """
    tour_depart = int(input(" Tour de départ ? "))
    if tour_depart== -1 :
        return tour_depart
    else : 
        while tour_filtre(tour_depart)==False  : 
            tour_depart = int(input(" Tour invalide :/ \nTour de départ (0-2) ? "))
        while Part_A.nbDisques(plateau,tour_depart) == 0: 
            tour_depart = int(input(" Invalide ,tour vide :/ \n Tour de depart ? "))
        return tour_depart

def lireCoords(plateau): #(Obligatoire)
    """
    Fonction pour lire les coordonnées de l'utilisateur pour un déplacement.
    Args:
        plateau (list): Le plateau actuel du jeu d'Hanoï.
    Returns:
        tuple: Les coordonnées du déplacement (tour de départ, tour d'arrivée).
    """
    flag = True
    bloque = 0
    while flag:
        tour_depart = tour_D(plateau)  # Appel de la fonction tour_D pour obtenir la tour de départ
        while flag:
            tour_arrivee = int(input(" Tour d'arrivée ? "))
            if tour_arrivee == -1:  # Cas d'abandon
                flag = False
            if tour_filtre(tour_arrivee) == False:
                print(" Tour invalide :/ \n")
            elif Part_A.disqueSup(plateau, tour_arrivee) == -1:
                flag = False
            elif bloque == 1: 
                print("Reprenons depuis le début : ")
                tour_depart = tour_D(plateau)
                bloque = 0
            elif Part_A.disqueSup(plateau, tour_arrivee) < Part_A.disqueSup(plateau, tour_depart):
                print(" Invalide, disque plus petit. :/ \n")
                bloque +=1  # Pour éviter le cas où l'utilisateur est bloqué
            else:
                flag = False
    return tour_depart, tour_arrivee


def jouerUnCoup(plateau, n):    #(Obligatoire)
    """
    Fonction pour jouer un coup.
    Args:
        plateau (list): Le plateau actuel du jeu d'Hanoï.
        n (int): Nombre de disques sur le plateau.
    Returns:
        list: Le plateau mis à jour après le coup.
    """
    global coups
    global key
    deplacement = lireCoords(plateau) 
    coups[key] = deplacement
    key += 1 
    disque_a_deplacer = Part_A.disqueSup(plateau, deplacement[0])
    Part_B.effaceDisque(disque_a_deplacer, plateau, n)
    plateau[deplacement[0]].remove(disque_a_deplacer)
    plateau[deplacement[1]].append(disque_a_deplacer)
    Part_B.dessineDisque(disque_a_deplacer, plateau, n)
    return plateau


def boucleJeu(plateau, n):    #(Obligatoire)     
    """
    Fonction pour la boucle principale du jeu.
    Args:
        plateau (list): Le plateau actuel du jeu d'Hanoï.
        n (int): Nombre de disques sur le plateau.
    """
    Button.button_jeu()  # Appel de la fonction pour afficher les boutons du jeu
    flag2 = True
    global coups
    global key
    global multi 
    flag = False
    while not flag:
        score_mode()  # Affiche le score en mode solo
        plateau = jouerUnCoup(plateau, n)
        if Part_A.verifvictoire(plateau, n):  # Vérifie si le joueur a gagné
            score_mode()
            print("Bravo tu viens de Gagner en ", len(coups), " coups")
            nom = input("Entrez votre nom svp :) :")

            if multi:  
                sauvScore(nom, n, len(coups))  # Sauvegarde du score en mode multijoueur
            else:
                sauvScore(nom, n, len(coups))  # Sauvegarde du score en mode solo
            coups = {}
            key = 0
            flag = True












# Partie E: Comparaison des scores et temps de jeu

'''Les Autre fonction dans dans le fichier Part_E'''

def afficher_tableau_solo():
    """Fonction utiliser pour afficher"""
    fenetre_tableau = tk.Tk()
    fenetre_tableau.title("Tableau des scores")

    donnees = Part_E.charger_scores(fichier_name)

    
    tableau = ttk.Treeview(fenetre_tableau, columns=("Nom", "Nombre de Disques", "Nombre de Coups"), show="headings")

    tableau.heading("Nom", text="Nom")
    tableau.heading("Nombre de Disques", text="Nombre de Disques")
    tableau.heading("Nombre de Coups", text="Nombre de Coups")

    for joueur ,don in donnees:
        tableau.insert("", "end", values=(joueur, don['Nombre Disque'], don['Nombre coups']))
    
    tableau.pack()


def sauvScore(nom,n, score):
    """
    Fonction pour sauvegarder le score d'un joueur.
    Args:
        nom (str): Nom du joueur.
        n (int): Nombre de disques sur le plateau.
        score (int): Nombre de coups réalisés par le joueur.
    """
    scores_existant = dict(Part_E.charger_scores(fichier_name))

    if nom in scores_existant :
        for key in scores_existant[nom]: 
            clee = key
        if scores_existant[nom]['Nombre Disque'] < n :
            scores_existant[nom]['Nombre Disque'] = n 
            scores_existant[nom]['Nombre coups'] = score
        elif scores_existant [nom][key] > score :
            scores_existant[nom][key] = score

    else : 
        scores_existant[nom] = { 'Nombre Disque': n , 'Nombre coups' : score }
        Part_E.sauvegarder_scores(fichier_name,scores_existant)
    sorted_scores = sorted(scores_existant.items(), key=lambda x: (-x[1]['Nombre Disque'], x[1]['Nombre coups']))
    Part_E.sauvegarder_scores(fichier_name,sorted_scores)




            



      
        
# Boutons / Options : 

def buttonClick(x,y):
    """
    Gère les clics sur les boutons en fonction des coordonnées (x, y).
    Args:
        x (float): Coordonnée x du clic.
        y (float): Coordonnée y du clic.
    """
    global fichier_name
    if -32 < x < 50 and -50 < y < -30:
        # Bouton pour abandonner la partie
        if abondon():
            turtle.bye()
    if -32 < x < 50 and -80 < y < -50:
        # Bouton pour afficher le tableau des scores en solo
        afficher_tableau_solo()
    if -32 < x < 50 and -110 < y < -80:
        # Bouton pour résoudre automatiquement en mode solo
        recursive_solution()
        time.sleep(1)
        turtle.bye()
    if -32 < x < 50 and -140 < y < -90:
        # Bouton pour annuler le dernier coup
        annulerDernierCoup()
    if  50 < x < 150 and 0< y < 20:
        # Bouton pour commencer une partie solo
        Button.blackhole_cover()
        fichier_name = 'score.pkl'
        main_solo()
        turtle.bye()
    if -40 < x < 40 and 0< y < 20:
        # Bouton pour commencer une partie multijoueur
        Button.blackhole_cover()
        fichier_name = 'score_multi.pkl'
        main_multijoueurs()
    if -150 < x < -50 and 0< y < 20:
        # Bouton pour afficher les instructions
        afficher_instructions()
        # Bouton pour afficher un indice en solo
    if -32< x < 50 and -170< y < -120:
        indice()
        
def abondon():
    """
    Propose à l'utilisateur d'abandonner la partie.
    Returns:
        bool: True si l'utilisateur souhaite abandonner, False sinon.
    """
    turtle.hideturtle()  # Masquer la tortue pendant la saisie
    resp = turtle.textinput("Abandonner", "Tu souhaites abandonner (o/n)? ")
    turtle.showturtle()  # Afficher la tortue après la saisie
    if resp == 'o' :
        print(f"\nAbandon de la partie après {len(coups)} coups.")
        return True
    elif resp == 'n' :
        return False

def afficher_instructions():
    """
    Affiche les instructions du jeu avec une boîte de dialogue.
    """
    # Afficher les instructions avec turtle.write
    message = "Bienvenue dans le monde des Tours de Hanoï !\n\n"\
              "- Règles en un clin d'œil :\n"\
              "1. Un à la fois : Bougez un disque à la fois.\n"\
              "2. Utilisez trois piliers pour déplacer les disques.\n"\
              "3. Les disques plus grands ne peuvent pas reposer sur des disques plus petits.\n\n"\
              "- Conseils :\n"\
              " Planifiez vos mouvements avec soin\n"\
              " Minimisez le nombre de coups pour obtenir un meilleur score.\n\n"\
              " Défiez-vous et Devenez un Maître de Hanoï !"

    turtle.hideturtle()  # Masquer la tortue pendant la saisie
    resp = turtle.textinput("Instructions - Tours de Hanoï", message)
    turtle.showturtle()




















# Partie F: Jeu automatique, fonction récursive

def jouerUnCoup_version2(plateau,n,deplacement):   # (Obligatoire)
    """
    Fonction inspirée de celle de la Partie C avec plus d'arguments
    et plus de retour.
    Args:
        plateau (list): Le plateau actuel du jeu d'Hanoï.
        n (int): Nombre de disques sur le plateau.
        deplacement (tuple): Tuple représentant le mouvement à effectuer (tour de départ, tour d'arrivée).
    """
    global coups
    global key
    disque_a_deplacer = Part_A.disqueSup(plateau,deplacement[0])
    Part_B.effaceDisque(disque_a_deplacer,plateau,n)
    plateau[deplacement[0]].remove(disque_a_deplacer)
    plateau[deplacement[1]].append(disque_a_deplacer)
    Part_B.dessineDisque(disque_a_deplacer,plateau,n)
    return plateau

def nombre_coup_min(n):
   """
    Calcule le nombre minimum de coups à faire.
    Args:
        n (int): Nombre de disques sur le plateau.
    Returns:
        int: Nombre minimum de coups nécessaires pour résoudre le puzzle.
    """
   return 2**n - 1


def hanoi_solution(n, depart, arrive, auxiliaire):
    """
    Algorithme récursif qui renvoie les mouvements à faire pour résoudre le casse-tête de la manière la plus optimale.
    Args:
        n (int): Nombre de disques sur le plateau.
        depart (int): Tour de départ.
        arrive (int): Tour d'arrivée.
        auxiliaire (int): Tour auxiliaire.
    Returns:
        list: Liste de tuples représentant les mouvements à faire.
    """
    if n == 1:
        return [(depart, arrive)]

    mouvements = hanoi_solution(n - 1, depart, auxiliaire, arrive)
    mouvements.append((depart, arrive))
    mouvements.extend(hanoi_solution(n - 1, auxiliaire, arrive, depart))

    return mouvements

def recursive_solution():
    """
    Annule les coups faits par l'utilisateur s'ils en ont fait, puis applique 
    les mouvements à faire en dessinant les déplacements des disques.
    """
    global plateau
    global n
    while len(plateau[0]) != n :
        annulerDernierCoup()
    depart, arrive, auxiliaire = 0, 2, 1
    resultat = hanoi_solution(n, depart, arrive, auxiliaire)

    min = nombre_coup_min(n)
    for i in range(min) :
        depl = resultat[i]
        jouerUnCoup_version2(plateau,n,depl)
    return















# Partie D: Annulation de coups

def dernierCoup(coups):         #(Obligatoire)
    """
    Fonction qui renvoie le dernier coup effectué.
    Args:
        coups (dict): Dictionnaire contenant les coups effectués.
    Returns:
        tuple: Tuple représentant le dernier coup (tour de départ, tour d'arrivée).
    """                
    cle = max(coups.keys())
    return coups[cle]
   

def annulerDernierCoup():       #(Obligatoire)
    """
    Fonction pour annuler le dernier coup effectué.
    """
    global plateau
    global coups
    global key
    if coups == {}:
        print("Pas de coup effectuer ! ")
        return
    coups_retour = []
    tour_depart,tour_arrivee = dernierCoup(coups)
    cle = max(coups.keys())
    
    del coups[cle]
    key = key - 1
    score_mode()
   
    coups_retour.append(tour_arrivee)
    coups_retour.append(tour_depart)
    plateau = jouerUnCoup_version2(plateau,n,coups_retour)
    return plateau
    



















# Option: Choix du mode de jeu

def main_solo():
    """
    Fonction principale pour le mode solo du jeu.
    """
    global n
    global plateau
    n= int(turtle.textinput("Nombre de Disque","Entez le nombre de disques  :"))
    plateau=Part_A.init(n)
    Part_B.dessinePlateau(n)
    Part_B.dessineConfig(plateau,n)
    boucleJeu(plateau,n)


def main_multijoueurs():
    """
    Fonction principale pour le mode multijoueurs du jeu.
    """
    global n
    global plateau
    global multi
    Part_E.reinitialiser_scores(fichier_name)
    n_joueurs = int(turtle.textinput("Mode multijoueurs", "Bienvenue au mode multijoueurs du jeu de Hanoï !\nRègles :\n\n1- Chaque joueur joue à tour de rôle.\n\n2- Le joueur qui termine le jeu avec le mininum de coups remporte la partie.\n\n3- Grades et Points :\n    -Le joueur avec le moins de coup l'emporte.\n    -En cas d'égalite il ya pas de gagnant.\n\n4- Classement :\n    - Les joueurs sont classés par ordre decroissant de nombre de coups.\n    \n\nAmusez-vous bien !\nNombre de Joueurs :"))
    for i in range(n_joueurs):
        main_solo()
        if i != n_joueurs-1 :
            Button.blackhole_cover()
        else :
            gagnant()






















# Option: Affichage du compteur de coups et du nombre minimal de coups

def score_mode():
    """
    Fonction pour afficher le compteur de coups et le nombre minimal de coups.
    """
    global pen
    global n
    global coups
    min = turtle.Turtle()
    min.color("white")
    min.hideturtle()
    min.penup()
    min.goto(120,-40)
    min.pendown()

    pen.clear()
    pen.color("white")
    pen.hideturtle()
    pen.penup()
    pen.goto(-200,-40)
    pen.pendown()
    mini =nombre_coup_min(n)
    if len(coups) > mini : 
        # Le compteur des coups tourne rouge quand on dépasse le nombre minimum de coups
        pen.color("red") 
    pen.write(f"Coups : {len(coups)}",font=("courier",10,"normal"))
    min.write(f"Mininum : {mini}",font=("courier",10,"normal"))























# Option : Affichage gagnant 

def afficher_gagnant():
    scores_joueurs = list(Part_E.charger_scores(fichier_name))
    print(scores_joueurs)
    miin = 10000
    for info_joueurs in scores_joueurs : 
        if info_joueurs[1]['Nombre coups'] < miin :
            miin = info_joueurs[1]['Nombre coups']
            ism = info_joueurs[0]
            return [ism,miin]

      
def gagnant() : 
    Button.blackhole_cover()
    player_gagant = afficher_gagnant()
    min = turtle.Turtle()
    min.color("white")
    min.hideturtle()
    min.penup()
    min.goto(-200,0)
    min.pendown()
    min.write(f"Gagnant est : {player_gagant[0]} ! avec {n} disques est un score de {player_gagant[1]}. Bravo ! :) ",font=("courier",10,"normal"))






















# Option: Donner des indices aux joueurs

def dernierCoup_clee(coups):
    """
    Fonction qui renvoie la clé du dernier coup effectué.
    Args:
        coups (dict): Dictionnaire contenant les coups effectués.
    Returns:
        int: Clé du dernier coup.
    """
    cle = max(coups.keys())
    return cle


def indice():
   """
    Fonction pour donner des indices aux joueurs.
    """
   global n
   global coups     
   depart, arrive, auxiliaire = 0, 2, 1
   resultat = hanoi_solution(n, depart, arrive, auxiliaire)
   min = turtle.Turtle()
   min.hideturtle()
   min.color("white")
   

   if coups == {} :
        min.penup()
        min.goto(-130,-200)
        min.pendown()
        min.write(f"Commencer de la Tour {resultat[0][0]} à la Tour {resultat[0][1]}",font=("courier",10,"normal"))
        time.sleep(2)
        Button.black_cover()


   else :
         deplace = dernierCoup(coups)
         num = dernierCoup_clee(coups)
         if deplace == resultat[num] :
            min.penup()
            min.goto(-175,-200)
            min.pendown() 
            min.write(f"Pour votre prochain coup, essayez de la tour {resultat[num+1][0]} à la tour {resultat[num+1][1]}",font=("courier",10,"normal"))
            time.sleep(2)
            Button.black_cover()
         else : 
            min.penup()
            min.goto(-100,-200)
            min.pendown()
            min.write("Annulez votre dernier coup",font=("courier",10,"normal"))
            time.sleep(1)
            Button.black_cover()

         return     

    





if __name__ == "__main__":
    Part_B.window()
    Button.text_menu()
    Button.button_menu()
    turtle.onscreenclick(buttonClick)
    turtle.done()

