# ========================================================================
# ===  Importation du fichier API_colors nécessaire a la présentation  ===
# ========================================================================
import API_colors

# ==========================================
# ===  Creation de la classe Personnage  ===
# ==========================================
class Personnage:
    
    # ==========================================================================================================
        # Méthode constructeur permettant l'initialisation de la classe en spécifiant les attributs de classes
    def __init__(self, nom, classe, level, jauge_xp, pv_initiaux, pv_courant, defense, attaque_physique, attaque_magique, jauge_mana):
        self.nom = nom
        self.classe = classe
        self.level = level
        self.jauge_xp = jauge_xp
        
        self.pv_initiaux = pv_initiaux
        self.pv_courant = pv_courant
        self.defense = defense
        
        self.attaque_physique = attaque_physique
        self.attaque_magique = attaque_magique
        
        self.jauge_mana = jauge_mana

    # ===============================================================================================
        # Méthode permettant de retourner un booléen (True, False) en fonction de la quantité de pv
    @property
    def is_alive(self)-> bool:
        return self.pv_courant > 0

    # ============================================================================================
        # Méthode permettant de retourner un résultat sous forme de chaîne de caractère (string)
    def __str__(self)-> str:
        return (f"{API_colors.green_color}{self.nom} ({self.classe}) - PV : {self.pv_courant} | Défense : {self.defense} | Attaque physique : {self.attaque_physique} | Attaque magique : {self.attaque_magique} | Jauge mana : {self.jauge_mana}{API_colors.default_color}")

    # ========================================================================
        # Méthode permettant de récuperer le nombre de points d'xp du joueur
    def get_xp(self):
        return f"\nPour vos faits héroiques, vous obtenez {API_colors.blue_color}{20} xp{API_colors.default_color}\nVous êtes actuellement au {API_colors.blue_color}niveau {self.level}{API_colors.default_color} et possédez {API_colors.blue_color}{self.jauge_xp} xp{API_colors.default_color}\n"
    
    # ==================================================================
        # Méthode permettant d'ajouter une quantité d'xp au personnage
    def add_xp(self):
        self.jauge_xp += 20
        print(self.get_xp())
        
    # ============================================================
        # Méthode permettant de faire passer un niveau au joueur
    def level_up(self):
        self.level += 1
        self.jauge_xp -= 100
        return f"Félicitation, vous venez de passer un niveau [ {self.level - 1} --> {self.level} ]\nToute vos apttitudes de combat augmente de 5 %, vous regagner 20 % de vos PV max et 10 points mana !\n"
    
    # ============================================================
        # Méthode permettant d'augmenter les stats du personnage
    def up_stats_perso(self):
        
        if not self.pv_courant >= 100:
            self.pv_courant *= 1.20
            if self.pv_courant > 100:
                self.pv_courant = 100
        
        if not self.jauge_mana >= 100:
            self.jauge_mana += 10
            if self.jauge_mana > 100:
                self.jauge_mana = 100
                
        self.defense *= 1.05
        self.attaque_physique *= 1.05
        self.attaque_magique *= 1.05
