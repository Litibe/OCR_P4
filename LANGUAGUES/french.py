#####################
# MODELS
STR_PLAYER_1 = "Joueur ID : "
STR_PLAYER_2 = " né(e) le "
STR_PLAYER_3 = "  de sexe "

#####################
# CONTROLLER
INIT_DATABASE = "--- Initialisation de la base de données ---"
INFORM_CREATE_PLAYER_INTO_DB = "--- Création du joueur dans la base de données ---"
RETURN_MAIN_MENU = "--- Retour au menu principal ---"

#####################
# VIEWS
# MAIN_MENU
SUMMARY_MAIN_MENU = """\n ♖♖♖ Bienvenue sur le programme de tournoi du Club d'Echec ! ♖♖♖ \n\t Au Sommaire : 
            Choix 1 : Créer un nouveau tournoi ♖
            Choix 2 : Ajouter un joueur dans la base de données.
            Choix 3 : Accès au Menu RAPPORT
            
            Choix 0 : Sortie du programme
        """
WHAT_DO_YOU_WANT = "Que souhaitez vous faire : "
ERROR_INPUT_CHOICE = "\n Merci de saisir un choix valide !"

# MENU_ADD_PLAYER
INFORM_CREATE_PLAYER = "Vous avez sélectionné la création d'un nouveau Joueur dans la BDD, " \
                       "merci de completer les champs requis : "
LAST_NAME_PLAYER = "Le NOM du Joueur : "
FIRST_NAME_PLAYER = "Le PRENOM du Joueur : "
BIRTHDAY_PLAYER = "Sa Date de naissance au format dd/mm/yyyy : "
SEX_PLAYER = "Son Sexe M/F : "

# RAPPORT
SUMMARY_MENU_RAPPORT = "\n\n--- Menu RAPPORT --- " \
                       "" \
                       "\n\t Choix 11 : Liste de tous les acteurs par ordre alphabétique" \
                       "\n\t Choix 12 : Liste de tous les acteurs par classement" \
                       "" \
                       "\n\t Choix 21 : Liste de tous les joueurs d'un tournoi Par ordre alphabétique" \
                       "\n\t Choix 22 : Liste de tous les joueurs d'un tournoi Par classement" \
                       "" \
                       "\n\t Choix 3 : Liste de tous les tournois" \
                       "" \
                       "\n\t Choix 4 : Liste de tous les tours d'un tournoi" \
                       "" \
                       "\n\t Choix 5 : Liste de tous les matchs d'un tournoi" \
                       "" \
                       "\n\tChoix 0 => Retour au menu principal"
RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME = "--- Listing des Joueurs - Tri par NOM - ordre Alphabétique  ---"
RAPPORT_PLAYERS_LIST_BY_ORDER = "--- Listing des Joueurs - Tri par Classement de joueurs ---"
RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME = "--- Listing des Joueurs dans un Tournoi - Tri par NOM - ordre Alphabétique  ---"
RAPPORT_TOURNAMENT_LIST_BY_ORDER = "--- Listing des Joueurs dans un Tournoi - Tri par Classement de joueurs ---"
RAPPORT_TOURNAMENT_LIST_ALL = "--- Listing des Tournoi - Tri par ID de Tournoi ---"
RAPPORT_LIST_ROUNDS_OF_TOURNAMENT = "--- Listing des tours d'un tournoi ---"
RAPPORT_LIST_MATCHS_OF_TOURNAMENT = "--- Listing des Matchs d'un tournoi ---"