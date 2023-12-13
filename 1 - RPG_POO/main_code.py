# =================================================================
# ===  Importation du module randint de la bibliothèque random  ===
# =================================================================
from random import randint

# =====================================================================
# ===  Importation des fichiers nécessaire au fonctonnement du jeu  ===
# =====================================================================
from API_personnage import Personnage
from API_donjon import Donjon

# ====================================================================
    # Crée le personnage du joueur avec des attributs spécifiques :
    # - nom
    # - classe
    # - level
    # - jauge_xp
    # - pv_initiaux
    # - pv_courant
    # - attaque_physique
    # - defense
    # - attaque_magique
    # - jauge_mana
    
joueur = Personnage("Arion",
                    "Le dernier espoir",
                    1,
                    0,
                    100,
                    100,
                    10,
                    20,
                    15,
                    100)

# ===========================================================
    # Définition du nombre d'étages que le donjon possedera
etages_du_donjon = randint(3,7)

# ======================
    # Crée l'objet Donjon
donjon = Donjon(etages_du_donjon,joueur)

# ====================
    # Lancement du jeu
print("\033c", end="") # Permet de nettoyer la console a chaque exécution du fichier "main_code.py"
donjon.jouer()