# ========================================================================
# ===  Importation du fichier API_colors nécessaire a la présentation  ===
# ========================================================================
import API_colors

# =================================================================
# ===  Importation du module randint de la bibliothèque random  ===
# =================================================================
from random import randint


# ====================================
# ===  Creation de la classe Boss  ===
# ====================================
class Boss:
    
    # ==========================================================================================================
        # Méthode constructeur permettant l'initialisation de la classe en spécifiant les attributs de classes
    def __init__(self, nom, classe, points_de_vie, attaque, defense, resistance):
        self.nom_boss = nom
        self.classe = classe
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.defense = defense
        self.resistance = resistance
    
    # ===============================================================================================
        # Méthode permettant de retourner un booléen (True, False) en fonction de la quantité de pv
    @property
    def is_alive(self)-> bool:
        return self.points_de_vie > 0

    # ============================================================================================
        # Méthode permettant de retourner un résultat sous forme de chaîne de caractère (string)
    def __str__(self)-> str:
        return(f"{API_colors.red_color}{self.nom_boss} ({self.classe}) - PV : {self.points_de_vie} | Attaque : {self.attaque} | Défense : {self.defense} | Résistance magique : {self.resistance} %{API_colors.default_color}")
    
    # ====================================================
        # Méthode permettant de récuperer le nom du boss
    @property
    def get_nom_boss(self):
        return self.nom_boss
    
