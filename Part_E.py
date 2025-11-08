import pickle


def sauvegarder_scores(fichier_name, scores):
    """
    Fonction auxiliaire pour sauvegarder les scores dans un fichier.
    Args:
        fichier_name (str): Le nom du fichier où sauvegarder les scores.
        scores (dict): Le dictionnaire des scores à sauvegarder.
    """
    with open(fichier_name, 'wb') as fichier_scores:
        pickle.dump(scores, fichier_scores)

def charger_scores(fichier_name):
    """
    Fonction auxiliaire pour charger les scores depuis un fichier.
    Args:
        fichier_name (str): Le nom du fichier à partir duquel charger les scores.
    Returns:
        dict: Le dictionnaire des scores chargés.
    """
    try:
        with open(fichier_name, 'rb') as fichier_scores:
            scores = pickle.load(fichier_scores)
    except FileNotFoundError:
        scores = {}  # Retourne un dictionnaire vide si le fichier n'est pas trouvé
    return scores

def reinitialiser_scores(fichier_name):
    """
    Cette fonction permet de réinitialiser le dictionnaire des scores en le remplaçant par un dictionnaire vide.
    Args:
        fichier_name (str): Le nom du fichier où réinitialiser les scores.
    """
    scores_vide = {}       
    with open(fichier_name, 'wb') as fichier:
        pickle.dump(scores_vide, fichier)




