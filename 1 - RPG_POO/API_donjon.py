# =================================================================
# ===  Importation du module randint de la bibliothèque random  ===
# =================================================================
from random import randint

# =====================================================================
# ===  Importation des fichiers nécessaire au fonctonnement du jeu  ===
# =====================================================================
from API_monstres import Monstres
from API_boss import Boss
import API_combat

# ========================================================================
# ===  Importation du fichier API_colors nécessaire a la présentation  ===
# ========================================================================
import API_colors


# ======================================
# ===  Creation de la classe Donjon  ===
# ======================================
class Donjon:
    
    # ================================================================
    # ===  Initialisation de la classe ===
    def __init__(self, etages, joueur):
        self.etages = etages  # Nombre d'étages dans le donjon
        self.niveau = 0  # Niveau actuel (étage)
        self.joueur = joueur  # Le personnage du joueur

    # ===================================================================================================================================================================================================================
    # ===  Creation de la méthode jouer  ===
    def jouer(self):
        
        print("""\
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Précision sur certain points :
    
    - Les points de vie du personnage ainsi que sa jauge de mana sont limités à une hauteur de 100.
    - Il se peut qu'il reste quelque bugs ou problemes d'équilibrage
    
Bon jeu !

----------------------------------------------------------------------------------------------------------------------------------------------------------------

LINK START !

Bienvenue au Royaume d'Éldoria.

Dans un monde en proie aux ténèbres, le royaume d'Éldoria est menacé par une magie maléfique.
Jadis prospère, le Cercle de l'Aube Noir, un culte maléfique, à plongé Éldoria dans le sang et le chaos.

Un héros solitaire, Arion, se lève pour affronter le Cercle de l'Aube Noir.

Accompagné de compagnons loyaux, il entreprend une quête périlleuse pour délivrer le royaume.
Leur objectif est de restaurer les runes antiques et ainsi, repousser les ténèbres qui menacent la capitale d'Éldoria.
Le destin du royaume repose entre les mains de ces valeureux héros. L'avenir est incertain, mais l'espoir demeure.

Vous arrivez après d'inombrables efforts, à votre destination finale, déterminer à venger la mort de vos compagnons, vous pénétrez, seul, dans ce donjon ...

----------------------------------------------------------------------------------------------------------------------------------------------------------------\n""")      
        
        while self.niveau < self.etages:
            self.niveau += 1
            print(f"Vous arrivez a l'étage {self.niveau} du donjon.")
            self.jouer_etage()

        print("L'aventure se termine.\n")

    # =============================================================================================================================
    
    # ===  Creation de la méthode jouer_étage  ===
    def jouer_etage(self):
        
        # Génération des monstres et du boss
            # Liste contenant autant de monstre que le numéros de l'étage actuel
        monstres = [Monstres(f"Monstre n°{i+1}",
                             "Bête",
                             40,
                             randint(5, 15),
                             randint(2, 10), 
                             0.9) for i in range(self.niveau)]

        boss = Boss(f"Démon au Yeux Azur",
                    "Boss",
                    125,
                    randint(20, 25),
                    randint(10, 20),
                    0.25)

        # Initialisation de la variable rencontre boss (servira pour la narration du jeu)
        rencontre_boss = False
        
        print(f"Vous reprerez {len(monstres)} monstres à cet étage.\n")

        # On boucle pour chaque monstre ...
        for monstre in monstres:
            
            # On répète les mêmes instructions tant que le joueur et le monstre courant sont toujours en vie
            while self.joueur.is_alive and monstre.is_alive:
                
                print(self.joueur)
                print("")
                
                print(monstre)
                
                print("\nQue voulez-vous faire ?\n1. Attaque physique\n2. Attaque Magique")
                
                choix = input("Choisissez une option : ")
                print("")

                if choix == "1":
                    API_combat.joueur_attaque_physique_monstre(self.joueur, monstre) # On récupère les événements situé dans API_combat
                
                elif choix == "2":
                    API_combat.joueur_attaque_magique_monstre(self.joueur, monstre) # On récupère les événements situé dans API_combat

                if monstre.is_alive:
                    API_combat.monstre_attaque_joueur(self.joueur, monstre) # On récupère les événements situé dans API_combat
                else:
                    print(f"{API_colors.blue_color}Le monstre est mort{API_colors.default_color}")
                
                if not monstre.is_alive:
                    self.joueur.add_xp()
                
                if self.joueur.jauge_xp >= 100:
                    print(self.joueur.level_up())
                    self.joueur.up_stats_perso()
        
        # -------------------------------------
        print("")
        # -------------------------------------
        
        # Si le joueur est en vie et qu'il est au dernier étage ...
        if self.joueur.is_alive and self.niveau == self.etages:
            
            print(f"Le boss du donjon apparait, ...\nVous rencontrez le {API_colors.red_color}Démon aux Yeux Azur.{API_colors.default_color}\n")
            rencontre_boss = True
            
            # ... On boucle tant que le joueur et le boss est en vie
            while self.joueur.is_alive and boss.is_alive:
                
                print(self.joueur)
                print("")
                
                print(boss)
                print("\nQue voulez-vous faire ?\n1. Attaque physique\n2. Attaque Magique")
                
                choix = input("Choisissez une option : ")
                print("")

                if choix == "1":
                    API_combat.joueur_attaque_physique_boss(self.joueur, boss) # On récupère les événements de fonction situées dans API_combat
                
                elif choix == "2":
                    API_combat.joueur_attaque_magique_boss(self.joueur, boss) # On récupère les événements de fonction situées dans API_combat
                    
                if boss.is_alive:
                    API_combat.boss_attaque_joueur(self.joueur, boss) # On récupère les événements de fonction situées dans API_combat


        
        if self.joueur.is_alive and self.niveau < self.etages:
            
            print(f"Vous avez vaincu tous les monstres de {API_colors.blue_color}l'étage {self.niveau}{API_colors.default_color} !\n")
        
        if self.joueur.is_alive and self.niveau == self.etages and not boss.is_alive:
            
            print(f"\nFélicitation ! Vous êtes venu a bout du donjon !\n")
            
        if not self.joueur.is_alive and self.niveau == self.etages and boss.is_alive:
            if rencontre_boss == True:
                
                print(self.joueur)
                print("")
                print(boss)
                
                print(f"\n----------------------------------------------------------------------\n\nVous avez été vaincu par le [ {API_colors.red_color}{boss.get_nom_boss}{API_colors.default_color} ] ...")
            
            else:
                print(f"Vous avez été vaincu par les monstres de l'étage {self.niveau} ...")
            
            print(f"Vous n'avez pas été en mesure de sauver Éldoria, le Cercle de l'Aube Noir acheva sont oeuvre sans plus personne pour l'arrêter ...\n")
        
    
