import turtle


def window():
    wn = turtle.Screen()
    wn.bgcolor("black")


# Fixer des mesures
h_disque = 15  # Hauteur du disque
l_tour = 10    # Longueur de la tour
b_color = 'yellow'  # Couleur de la bordure
f_color = 'blue'  # Couleur de remplissage



# Classe utiliser Dans ce projet 

class Tower(turtle.Turtle):

    # Propriété 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.speed(0)
   
    # Se positionne aux coordonnées x, y où doit se trouver la tour 
    def cord(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()

    # Dessine la tour    
    def carateristique(self, h_tour):
        self.speed(0)
        self.color('blue','black')
        self.begin_fill()
        for i in range(4):
            if i % 2 == 0:
                self.forward(10)
            else:
                self.forward(h_tour)
            self.left(90)
        self.end_fill()
        self.hideturtle()

class disque(turtle.Turtle):
   
   # Propriété 
   def __init__(self):
      turtle.Turtle.__init__(self)
      self.speed(0)
      self.hideturtle()
      self.color("yellow")

      
   def draw(self,x,y,l_disque,f_color,b_color):
       """Fonction qui dessine un disque aux 
       coordonnées (x, y) et colore le disque"""

       # Positionné aux coordonnées de la tour
       self.penup()
       self.speed(0)
       self.goto(x,y)
       self.pendown()

       # Ajout de couleur 
       self.color(b_color,f_color)

       self.begin_fill()
       # Dessine un disque 
       self.forward(l_disque//2)
       self.left(90)
       self.forward(15)
       self.left(90)
       self.forward(l_disque)
       self.left(90)
       self.forward(15)
       self.left(90)
       self.forward(l_disque//2)
       self.end_fill()
       self.hideturtle()

class Support(turtle.Turtle):
   
   # Propriété 
   def __init__(self):
      turtle.Turtle.__init__(self)
      self.hideturtle()
      self.speed(0)
   
   # Dessiner le support 
   def set(self,n):
      escpace =  10 +30*n
      if n < 3 :
          escpace = 75
      else :
          escpace =  10 +30*n
      self.speed(0)
      self.penup()
      self.goto(0,0)
      self.pendown()

      self.color("blue","black")
      self.begin_fill()
      self.forward((escpace+5)*2)
      self.left(-90)
      self.forward(15)
      self.left(-90)
      self.forward((escpace+5)*4)
      self.left(-90)
      self.forward(15)
      self.left(-90)
      self.forward((escpace+5)*2)
      self.end_fill()
      self.hideturtle()

class remplissage_ligne(turtle.Turtle):
   """Class cree pour combler les bordure effacer apres l'appel
   des fonction effaceDisque() et effaceTout()"""
    
    # Propriété 
   def __init__(self,color):
      turtle.Turtle.__init__(self)
      self.hideturtle()
      self.color(color)
      self.speed(0)   

    # Se positionne aux coordonnées x, y où s'effectue le remplissage
   def cord_remplir(self,x,y):
        self.penup()
        self.goto(x,y)
        self.pendown()

    # Redessine les bordures effacées selon la longueur du disque effacé
   def ligne(self,l_disque_nd):
       l_disque_nd_part = l_disque_nd//2
       self.forward(l_disque_nd_part+5)
       self.forward((-l_disque_nd_part)*2-10)

class Button(turtle.Turtle):
    def __init__(self,color):
        turtle.Turtle.__init__(self)
        self.color(color)
        self.hideturtle()
        self.speed(0)

    def cord(self,x,y):
        self.penup()
        self.goto(x, y)
        self.pendown()

    def square(self):
        h_tour= 20
        for i in range(4):
            if i % 2 == 0:
                self.forward(80)
            else:
                self.forward(h_tour)
            self.left(90)
    
    def write_in(self,ch,x,y) : 
        self.penup()
        self.goto(x,y)
        self.write(ch,font=('Courier',8,'normal'))
        self.pendown()
    
       























# Fonctions support

def find_tour_cord_X(nd, cord_tow_X, plateau):
    """
    Trouve le numéro de la tour où se trouve le disque (nd) 
    et renvoie les coordonnées X pour le dessiner.
    Args:
        nd (int): Matricule (numéro) du disque.
        cord_tow_X (list): Les coordonnées X obtenues lors du placement des tours.
        plateau (list): Plateau de jeu.
    Returns:
        tuple: Coordonnées X du disque et le numéro de la tour.
    """
    for i in range(3):
        l = plateau[i]
        if nd in l:
            tour_numero = i
    if tour_numero == 0:
        X = cord_tow_X[0]
    elif tour_numero == 1:
        X = cord_tow_X[1]
    else:
        X = cord_tow_X[2]
    return X, tour_numero

def find_tour_cord_y(nd, plateau, n, tour_numero, h_disque):
    """
    Trouve la coordonnée Y du disque (nd) en fonction de la tour où il se trouve.
    Args:
        nd (int): Matricule (numéro) du disque.
        plateau (list): Plateau de jeu.
        n (int): Nombre de disques.
        tour_numero (int): Numéro de la tour où se trouve le disque (nd).
        h_disque (int): Hauteur du disque.
    Returns:
        int: Coordonnée Y du disque.
    """
    l = plateau[tour_numero]
    y = 0
    n_disque_precedent = 0
    while nd != l[n_disque_precedent]:
        n_disque_precedent = n_disque_precedent + 1
    y = n_disque_precedent * h_disque
    return y

def l_disque_somme(n, nd, l_disque_max):
    """
    Trouve la longueur du disque (nd) en fonction du nombre total de disques (n)
    et de la longueur du plus grand disque (l_disque_max).
    Args:
        n (int): Nombre de disques.
        nd (int): Matricule (numéro) du disque.
        l_disque_max (int): La longueur maximale du plus grand disque.
    Returns:
        int: Longueur du disque (nd).
    """
    i = 0
    l_disque_max_nv = 0
    while i != nd:
        i = i + 1
        ajout = l_disque_max // n
        l_disque_max_nv = ajout + l_disque_max_nv
    return l_disque_max_nv




















# Fonction Obligatoire

def dessinePlateau(n):
    """
    Dessine le plateau de jeu avec des tours et un espacement en fonction du nombre de disques.
    Args:
        n (int): Nombre de disques.
    """
    plat = Support()
    plat.set(n)

    tow = Tower()
    h_tour = n * h_disque + h_disque
    espace = 60 + 25 * n
    if espace >= 600:
        espace = 500
    espace = [-espace, 0, +espace]
    for i in espace:
        tow.cord(i, 0)
        tow.carateristique(h_tour)

def dessineDisque(nd, plateau, n):
    """
    Dessine un disque sur le plateau en fonction de sa matricule (nd) et de sa position.
    Args:
        nd (int): Matricule (numéro) du disque.
        plateau (list): Plateau de jeu.
        n (int): Nombre de disques.
    """
    espace = 60 + 25 * n
    if espace >= 600:
        espace = 500
    cord_tow_X = [-espace + 5, 0 + 5, espace + 5]

    X, tour_numero = find_tour_cord_X(nd, cord_tow_X, plateau)
    y = find_tour_cord_y(nd, plateau, n, tour_numero, h_disque)

    l_disque_max = (abs(cord_tow_X[0]) + abs(cord_tow_X[1])) // 1.5
    l_disque_nd = l_disque_somme(n, nd, l_disque_max)
    disc = disque()
    disc.draw(X, y, l_disque_nd, b_color, f_color)

def dessineConfig(plateau, n):
    """
    Dessine la configuration actuelle du plateau avec tous les disques.
    Args:
        plateau (list): Plateau de jeu.
        n (int): Nombre de disques.
    """
    for i in range(n):
        dessineDisque(i + 1, plateau, n)

def effaceDisque(nd, plateau, n):
    """
    Efface un disque du plateau en fonction de sa matricule (nd).
    Args:
        nd (int): Matricule (numéro) du disque.
        plateau (list): Plateau de jeu.
        n (int): Nombre de disques.
    """
    i = 0
    espace = 60 + 25 * n
    cord_tow_X = [-espace + 5, 0 + 5, espace + 5]

    X, tour_numero = find_tour_cord_X(nd, cord_tow_X, plateau)
    y = find_tour_cord_y(nd, plateau, n, tour_numero, h_disque)

    l_disque_max = (abs(cord_tow_X[0]) + abs(cord_tow_X[1])) // 1.5
    l_disque_nd = l_disque_somme(n, nd, l_disque_max)

    disc = disque()
    b_color = 'black'
    f_color = 'black'
    disc.draw(X, y, l_disque_nd, b_color, f_color)

    tour_complement = Tower()
    tour_complement.cord((cord_tow_X[tour_numero] - 5), y)
    tour_complement.carateristique(h_disque)

    ligne1 = remplissage_ligne(color='black')
    ligne1.cord_remplir(cord_tow_X[tour_numero], y + h_disque)
    ligne1.ligne(1)

    ligne2 = remplissage_ligne(color='blue')
    ligne2.cord_remplir(cord_tow_X[tour_numero], y)
    ligne2.ligne(l_disque_nd)

def effaceTout(plateau, n):
    """
    Efface tous les disques du plateau.
    Args:
        plateau (list): Plateau de jeu.
        n (int): Nombre de disques.
    """
    for i in range(n):
        effaceDisque(i + 1, plateau, n)



