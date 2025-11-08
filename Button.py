# Importation du module turtle et d'un module appelé Part_B
import turtle
import Part_B

# Fonction pour afficher du texte du menu principal
def text_menu():
    text = turtle.Turtle()
    text.hideturtle()
    text.color("White")
    text.penup()
    text.goto(0, 80)
    text.pendown()
    text.write("Tour d'Hanoi", align="center", font=("courier", 20, "bold"))

# Fonction pour créer et afficher les boutons du menu principal
def button_menu():
    # Création d'un bouton pour le mode solo
    butt_solo = Part_B.Button("yellow")
    butt_solo.cord(50, 0)
    butt_solo.square()
    butt_solo.write_in("Un joueur", 60, 5)

    # Création d'un bouton pour le mode multijoueur
    butt_multi = Part_B.Button("blue")
    butt_multi.cord(-50, 0)
    butt_multi.square()
    butt_multi.write_in("Multimode", -40, 5)

    # Création d'un bouton pour afficher les règles
    butt_Regles = Part_B.Button("red")
    butt_Regles.cord(-150, 0)
    butt_Regles.square()
    butt_Regles.write_in(" Regles ", -140, 5)

# Fonction pour créer et afficher les boutons pendant le jeu
def button_jeu():
    # Bouton pour abandonner le jeu
    butt_abandon = Part_B.Button("red")
    butt_abandon.cord(-32, -50)
    butt_abandon.square()
    butt_abandon.write_in(" Abandonner ", -30, -47)

    # Bouton pour afficher les scores
    butt_Scores = Part_B.Button("red")
    butt_Scores.cord(-32, -80)
    butt_Scores.square()
    butt_Scores.write_in(" Scores ", -20, -76)

    # Bouton pour afficher la solution
    butt_Solu = Part_B.Button("red")
    butt_Solu.cord(-32, -110)
    butt_Solu.square()
    butt_Solu.write_in(" Solution ", -25, -105)

    # Bouton pour annuler une action
    butt_annul = Part_B.Button("red")
    butt_annul.cord(-32, -140)
    butt_annul.square()
    butt_annul.write_in(" annuler ", -25, -135)

    # Bouton pour obtenir un indice
    butt_indice = Part_B.Button("red")
    butt_indice.cord(-32, -170)
    butt_indice.square()
    butt_indice.write_in(" indice ", -20, -165)

# Fonction pour afficher un grand cercle noir couvrant la fenêtre turtle
#  utiliser pour 'Passer' d'une fenetre a une autre """
def blackhole_cover():
    blackhole = turtle.Turtle()
    blackhole.shape("circle")
    blackhole.shapesize(stretch_wid=200, stretch_len=200)

# Fonction pour afficher un disque noir couvrant une partie de la fenêtre turtle,
# utilisée pour recouvrir les textes affichés à l'écran.
def black_cover():
    
    cover = Part_B.disque()
    cover.draw(0, -200, 700, 'black', 'black')


