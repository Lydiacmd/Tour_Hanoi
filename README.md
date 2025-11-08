# 🎮 Jeu des Tours de Hanoï

## 🧩 Présentation
Implémentation **graphique et interactive** du puzzle des **Tours de Hanoï**, codée en **Python** avec **`turtle`** pour l’affichage et **`tkinter`** pour les tableaux de scores.  
Objectif : déplacer tous les disques d’une tour à une autre **sans jamais poser un disque plus grand sur un plus petit**.  
Projet d’entraînement à la **POO**, à la **récursivité** et à la **création d’interfaces graphiques** simples.

---

## 🚀 Fonctionnalités principales

### 🎮 Menu principal
Au lancement de `Principal.py`, un **menu** s’affiche avec trois boutons :
- **Un joueur** — lance une partie solo  
- **Multijoueur** — plusieurs joueurs à tour de rôle  
- **Règles** — affiche les instructions dans une boîte de dialogue

- Choix du **nombre de disques**.
- Les **déplacements** des tours se font dans le **terminal** (0–2)  
  **Exemple :**  
  Tour de départ ? 0  
  Tour d’arrivée ? 1
- Boutons en jeu :
  - 🟥 **Abandonner** — quitte la partie
  - 🟥 **Scores** — affiche le classement (Tkinter)
  - 🟥 **Solution** — déroule la solution optimale (récursive)
  - 🟥 **Annuler** — annule le dernier coup
  - 🟥 **Indice** — propose le prochain meilleur mouvement
- Le compteur de coups devient **rouge** si le joueur dépasse le minimum \(2^n - 1\).

### 👥 Mode multijoueur
- Entrez le **nombre de joueur**
- Chaque joueur choisit son **nombre de disques**
- Le prochain joueur jouras une fois que le precedents a fini
- **Comparaison des scores** en fin de partie (moins de coups / plus grand n)
- **Annonce du gagnant** à l’écran

### 💾 Scores
- Persistance via **Pickle**
- Classement trié automatiquement (par **n** décroissant puis **coups** croissant)

---

## 🧠 Architecture du projet

| Fichier | Rôle principal |
|:--|:--|
| `Principal.py` | Point d’entrée, boucle de jeu, modes solo/multi, boutons |
| `Part_A.py` | Logique du plateau (init, règles, vérifs, condition de victoire) |
| `Part_B.py` | Dessins Turtle (support, tours, disques), helpers graphiques |
| `Button.py` | Composants de boutons et textes du menu / jeu, écrans “cover” |
| `Part_E.py` | Sauvegarde / chargement / reset des scores (Pickle) |
| `Rapport_Projet_Jeu_Hanoi.pdf` | Rapport de projet (conception, difficultés, choix) |

### Fichiers de scores (auxiliaires)
- `score.pkl` — historique solo  
- `score_multi.pkl` — scores de la partie multijoueur en cours  

> 💡 Les fichiers `.pkl/.plk` sont **générés et relus** automatiquement par le programme.  
> Il n’est pas nécessaire de les modifier à la main.

---

## 🧰 Technologies utilisées
- 🐍 **Python 3**
- 🐢 **Turtle** — affichage graphique
- 🪟 **Tkinter** — fenêtre et tableau des scores
- 💾 **Pickle** — persistance des scores
- ⚙️ **POO** & **récursivité**

---

## ⚙️ Installation & exécution

### 1️⃣ Prérequis
Vérifier que Python 3 est installé :
```bash
python --version
```

### 2️⃣ Lancement du jeu

Depuis le dossier du projet, exécutez la commande suivante dans un terminal :

```bash
python Principal.py
