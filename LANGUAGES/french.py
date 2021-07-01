#####################
# MODELS
STR_PLAYER_1 = "Joueur ID : "
STR_PLAYER_2 = " né(e) le "
STR_PLAYER_3 = "  de sexe "

STR_TOURNAMENT_1 = "Voici les détails du tournoi de l'ID N°"
STR_TOURNAMENT_2 = "Nom du tournoi :"
STR_TOURNAMENT_3 = "Date et Lieu du tournoi : le"
STR_TOURNAMENT_4 = "Tournoi réalisé en "
STR_TOURNAMENT_5 = "tours dont les Id de Rounds sont"
STR_TOURNAMENT_6 = "selon le contrôle de temps"
STR_TOURNAMENT_7 = "Description du tournoi : "

STR_MATCH_1 = "Il s'agit du match id n°"
STR_MATCH_2 = "avec la configuration : "
STR_SCORE = "avec le score "
STR_ROUNDS_1 = "Il s'agit du Tour id n°"
STR_ROUNDS_2 = "avec les match ID N°"

#####################
# CONTROLLER
RETURN_MAIN_MENU = "--- Retour au menu principal ---"

#####################
# VIEWS
# MAIN_MENU
SUMMARY_MAIN_MENU = """
-----------------------------------------------------------------------------------------------------
    ♖♖♖ Bienvenue sur le programme de tournoi du Club d'Echec ! ♖♖♖ 
        Au Sommaire : 
            Choix 1 : Créer un nouveau tournoi ♖
            Choix 2 : Ajouter un joueur dans la base de données.
            Choix 3 : Accès au Menu RAPPORT
            
            Choix 0 : Sortie du programme
-----------------------------------------------------------------------------------------------------"""
WHAT_DO_YOU_WANT = "Que souhaitez vous faire : "
ERROR_INPUT_CHOICE = "\n Merci de saisir un choix valide !"

# MENU_TOURNAMENT
SUMMARY_MENU_TOURNAMENT = """
-----------------------------------------------------------------------------------------------------
    --- Menu TOURNOI --- 
              Choix 1 : Création d'un nouveau Tournoi" 
              Choix 2 : Ajouter les 8 joueurs au dernier tournoi créé
              Choix 3 : Lancer le tour de jeu
              Choix 4 : Modifier le Classement d'un joueur
                        
              Choix 0 : Retour au menu principal
-----------------------------------------------------------------------------------------------------"""
INFORM_CREATE_TOURNAMENT = "Vous avez sélectionné la création d'un nouveau Tournoi, " \
                           "merci de completer les champs requis : "
INPUT_TOURNAMENT_NAME = "\n Nom du Tournoi : "
INPUT_TOURNAMENT_LOCATION = "\n Lieu du Tournoi : "
INFORM_INPUT_PLAYERS = "\nMerci de saisir les ID des 8 joueurs pour le tournoi : "
ERROR_INPUT_PLAYER = " Vous n'avez pas taper de caractère compatible, merci de saisir un chiffre svp !"
CHOICE_TIME = ["Bullet", "Blitz", "Coup rapide"]
SELECT_CONTROL_TIME = "\nVoici la liste des contrôleur du temps disponibles : "
INPUT_DESCRIPTION_TOURNAMENT = "\nVous pouvez saisir une description de tournoi : "
INFORM_CREATE_TOURNAMENT_INTO_DB = "--- Création du Tournoi dans la base de données ---"
INFORM_CREATE_PLAYERS_TOURNAMENT_INTO_DB = "--- Création de la liste des joueurs rattachée" \
                                           " au Tournoi dans la base de données ---"

# MENU_ADD_PLAYER
INFORM_CREATE_PLAYER = "Vous avez sélectionné la création d'un nouveau Joueur dans la BDD, " \
                       "merci de completer les champs requis : "
LAST_NAME_PLAYER = "Le NOM du Joueur : "
FIRST_NAME_PLAYER = "Le PRENOM du Joueur : "
BIRTHDAY_PLAYER = "Sa Date de naissance au format dd/mm/yyyy : "
SEX_PLAYER = "Son Sexe M/F : "
INFORM_CREATE_PLAYER_INTO_DB = "--- Création du joueur dans la base de données ---"

# RAPPORT
SUMMARY_MENU_RAPPORT = """
-----------------------------------------------------------------------------------------------------
    --- Menu RAPPORT ---
            Liste de tous les acteurs
                Choix 11 : par ordre alphabétique
                Choix 12 : par classement
              
            Liste de tous les joueurs d'un tournoi 
                Choix 21 : par ordre alphabétique
                Choix 22 : par classement
            
            Liste de tous les tournois : Choix  3
            Liste de tous les tours d'un tournoi : Choix  4
            Liste de tous les matchs d'un tournoi : Choix  5 
                    
            Choix 0 => Retour au menu principal
-----------------------------------------------------------------------------------------------------"""
RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME = "--- Listing des Joueurs - Tri par NOM - ordre Alphabétique  ---"
RAPPORT_PLAYERS_LIST_BY_ORDER = "--- Listing des Joueurs - Tri par Classement de joueurs ---"
RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME = "--- Listing des Joueurs dans un Tournoi " \
                                           "- Tri par NOM - ordre Alphabétique  ---"
RAPPORT_TOURNAMENT_LIST_BY_ORDER = "--- Listing des Joueurs dans un Tournoi - Tri par Classement de joueurs ---"
RAPPORT_TOURNAMENT_LIST_ALL = "--- Listing des Tournoi - Tri par ID de Tournoi ---"
RAPPORT_LIST_ROUNDS_OF_TOURNAMENT = "--- Listing des tours d'un tournoi ---"
RAPPORT_LIST_MATCHS_OF_TOURNAMENT = "--- Listing des Matchs d'un tournoi ---"
