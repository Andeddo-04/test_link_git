# =====================================================================
# === Gestion des attaques possible du personnage contre un monstre ===
# =====================================================================
def joueur_attaque_physique_monstre(joueur, monstre):
    
    dgt_subi = joueur.attaque_physique - monstre.defense
    
    if dgt_subi > 0:
    
        monstre.points_de_vie -= dgt_subi
        
        print(f"Monstre : - {dgt_subi} pv")
    
    else:
        print(f"Ce n'est pas très efficace ... ")
    
# *************************************************************************************************

def joueur_attaque_magique_monstre(joueur, monstre):

    if joueur.jauge_mana > 0 :
        
        joueur.jauge_mana -= 10
        dgt_subi = joueur.attaque_magique * monstre.resistance
        
        if dgt_subi > 0:
        
            monstre.points_de_vie -= dgt_subi
            
            print(f"Monstre : - {dgt_subi} pv | Il vous reste {joueur.jauge_mana} pts de mana")
        
        else:
            print(f"Ce n'est pas très efficace ... | Il vous reste {joueur.jauge_mana} pts de mana")
    
    else:
        print(f"Il ne vous reste plus assez de mana pour lancer un sort ...")

    
    
    
    
    
# ==================================================================
# === Gestion des attaques possible du personnage contre le boss ===
# ==================================================================
def joueur_attaque_physique_boss(joueur, boss):
    
    dgt_subi = joueur.attaque_physique - boss.defense
    
    if dgt_subi > 0:
    
        boss.points_de_vie -= dgt_subi
        
        print(f"Boss : - {dgt_subi} pv")
    
    else:
        print(f"Ce n'est pas très efficace ... | Le Boss à toujours {boss.points_de_vie} pv")
    
# ***********************************************************************************************

def joueur_attaque_magique_boss(joueur, boss):

    if joueur.jauge_mana > 0 :
        
        joueur.jauge_mana -= 10
        dgt_subi = joueur.attaque_magique * boss.resistance
        
        if dgt_subi > 0:
        
            boss.points_de_vie -= dgt_subi
            
            print(f"Boss : - {dgt_subi} pv | Il à désormait {boss.points_de_vie} pv")
        
        else:
            print(f"Ce n'est pas très efficace ... | Le Boss à toujours {boss.points_de_vie} pv")
    else:
        print(f"Il ne vous reste plus assez de mana pour lancer un sort ...")

    
    
    
    
    
# ========================================================================
# === Gestion des attaques des monstre et du boss contre le personnage ===
# ========================================================================
def monstre_attaque_joueur(joueur, monstre):
    
    dgt_subi = monstre.attaque - joueur.defense
    
    if dgt_subi > 0:
    
        joueur.pv_courant -= dgt_subi
        
        print(f"Vous : - {dgt_subi} pv | Il vous reste désormait {joueur.pv_courant} pv\n")
    
    else:
        print(f"Vous parez l'attaque du monstre, vous conservez vos {joueur.pv_courant} pv\n")
    
# *****************************************************************************************************************

def boss_attaque_joueur(joueur, boss):

    dgt_subi = boss.attaque - joueur.defense
    
    if dgt_subi > 0:
    
        joueur.pv_courant -= dgt_subi
        
        print(f"Vous : - {dgt_subi} pv | Il vous reste désormait {joueur.pv_courant} pv\n")
    
    else:
        print(f"Vous parez l'attaque du [ {boss.get_nom_boss} ] | Vous conservez vos {joueur.pv_courant} pv\n")