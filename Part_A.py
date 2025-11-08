# Partie A: Plateau de jeu et listes

def init(n):
    """
    Initialise le plateau de jeu avec n disques sur la première tour.
    Args:
        n (int): Nombre de disques à initialiser.
    Returns:
        list: Plateau de jeu initialisé.
    """
    plateau = [[], [], []]
    for i in range(n, 0, -1):
        plateau[0].append(i)
    return plateau

def nbDisques(plateau, numtour):
    """
    Renvoie le nombre de disques présents sur une tour donnée.
    Args:
        plateau (list): Plateau de jeu.
        numtour (int): Numéro de la tour.
    Returns:
        int: Nombre de disques sur la tour spécifiée.
    """
    i = 0
    while i < len(plateau):
        if i == numtour:
            nb = len(plateau[i])
        i += 1
    return nb

def disqueSup(plateau, numtour):
    """
    Renvoie le disque supérieur d'une tour donnée.
    Args:
        plateau (list): Plateau de jeu.
        numtour (int): Numéro de la tour.
    Returns:
        int: Numéro du disque supérieur, -1 si la tour est vide.
    """
    i = 0
    if nbDisques(plateau, numtour) == 0:
        return -1
    else:
        l = plateau[numtour]
        return l[-1]

def posDisque(plateau, numdisque):
    """
    Renvoie la position d'un disque sur le plateau.
    Args:
        plateau (list): Plateau de jeu.
        numdisque (int): Numéro du disque.
    Returns:
        int: Numéro de la tour où se trouve le disque.
    """
    i = 0
    for i in range(len(plateau)):
        if numdisque in plateau[i]:
            return i

def verifDepl(plateau, nt1, nt2):
    """
    Vérifie si un déplacement de disque est autorisé.
    Args:
        plateau (list): Plateau de jeu.
        nt1 (int): Numéro de la tour de départ.
        nt2 (int): Numéro de la tour d'arrivée.
    Returns:
        bool: True si le déplacement est autorisé, False sinon.
    """
    flag = False

    # Si la tour d'arrivée est vide
    if disqueSup(plateau, nt2) == -1:
        flag = True
    # Si le disque à déplacer est plus petit que le disque à nt2
    elif disqueSup(plateau, nt2) > disqueSup(plateau, nt1):
        flag = True
    # Si la tour de départ est vide
    elif disqueSup(plateau, nt1) != -1:
        flag = False
    # Si le disque à déplacer est plus grand que celui à nt2
    elif disqueSup(plateau, nt2) < disqueSup(plateau, nt1):
        flag = False

    return flag

def verifvictoire(plateau, n):
    """
    Vérifie si le joueur a gagné en déplaçant tous les disques à la dernière tour.
    Args:
        plateau (list): Plateau de jeu.
        n (int): Nombre total de disques.
    Returns:
        bool: True si le joueur a gagné, False sinon.
    """
    verif = False
    if nbDisques(plateau, 0) == 0 and nbDisques(plateau, 1) == 0 and nbDisques(plateau, 2) == n:
        verif = True
    return verif
