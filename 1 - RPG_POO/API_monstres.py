# ========================================================================
# ===  Importation du fichier API_colors nécessaire a la présentation  ===
# ========================================================================
import API_colors


# ========================================
# ===  Creation de la classe Monstres  ===
# ========================================
class Monstres:
    
    # ==========================================================================================================
        # Méthode constructeur permettant l'initialisation de la classe en spécifiant les attributs de classes
    def __init__(self, nom, classe, points_de_vie, attaque, defense, resistance):
        self.nom = nom
        self.classe = classe
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.defense = defense
        self.resistance = resistance
    
    # ===============================================================================================
        # Méthode permettant de retourner un booléen (True, False) en fonction de la quantité de pv
    @property
    def is_alive(self):
        return self.points_de_vie > 0

    # ============================================================================================
        # Méthode permettant de retourner un résultat sous forme de chaîne de caractère (string)
    def __str__(self):
        return(f"{API_colors.red_color}{self.nom} ({self.classe}) - PV : {self.points_de_vie} | Attaque : {self.attaque} | Défense : {self.defense} | Résistance magique : {self.resistance} %{API_colors.default_color}")
    
