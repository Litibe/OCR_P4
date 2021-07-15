#####################
# models
STR_PLAYER_1 = "Joueur ID N°"
STR_PLAYER_2 = " né(e) le "
STR_PLAYER_3 = "sexe: "
STR_PLAYER_RANK = "N°"
STR_PLAYER_RANK2 = "au classement"
STR_PLAYER_PTS_TOURNAMENT = "avec "
STR_PLAYER_PTS_TOURNAMENT2 = "points "


STR_PLAYER_TOURNAMENT_1 = "Voici les ID de joueurs présents " \
                          "lors du Tournoi N°"
STR_PLAYER_TOURNAMENT_rank = "N° "
STR_PLAYER_TOURNAMENT_rank2 = " au classement"

STR_TOURNAMENT_1 = "Voici les détails du tournoi de l'ID N°"
STR_TOURNAMENT_2 = "Nom du tournoi :"
STR_TOURNAMENT_3 = "Date de début de tournoi et son Lieu : le "
STR_TOURNAMENT_4 = "Tournoi réalisé en "
STR_TOURNAMENT_5 = "tours"
STR_TOURNAMENT_6 = "Le contrôle de temps est le"
STR_TOURNAMENT_7 = "Description du tournoi : "

STR_MATCH_1 = "Il s'agit du match ID n°"
STR_MATCH_2 = "avec la configuration : "
STR_SCORE = "(score="
STR_SCORE2 = "point)"
STR_ROUNDS_1 = "Il s'agit du Tour ID n°"
STR_ROUNDS_2 = "avec les match ID N°"
STR_ROUND_STARTED = "Date et Heure de Début : "
STR_ROUND_FINISHED = "Date et Heure de Fin : "
#####################
# CONTROLLER
RETURN_MAIN_MENU = "--- Retour au menu principal ---"
CHOICE_RETURN_MAIN_MENU = "Choix 0 : retour au menu principal"
#####################
# VIEWS
# MAIN_MENU
SUMMARY_MAIN_MENU = """
---------------------------------------------------------------
♖♖♖ Bienvenue sur le programme de tournoi du Club d'Echec ! ♖♖♖ 
    Au Sommaire : 
            Choix 1 : Accès au Menu BASE DE DONNEES :
                        - Gestion des joueurs
            Choix 2 : Accès au Menu TOURNOI ♖
            Choix 3 : Accès au Menu RAPPORTS
            
            Choix 0 : Sortie du programme
-------------------------------------------------------------"""
WHAT_DO_YOU_WANT = "Que souhaitez vous faire : "
ERROR_INPUT_CHOICE = "\n Merci de saisir un choix valide !"
ERROR_INPUT_DATE = "\n Merci de saisir une date valide !"
CONFIRM_INPUT = "Est ce que vous confirmez votre saisie ? (y/n) "

# MENU_TOURNAMENT
SUMMARY_MENU_TOURNAMENT = """
--------------------------------------------------------------------
    --- Menu TOURNOI --- 
"""

CREATE_NEW_TOURNAMENT = "Choix 1 : ♖ Créer un nouveau tournoi ♖"
ADD_PLAYERS_FOR_TOURNAMENT = "Choix 2 : Ajouter les huits joueurs pour " \
                             "le tournoi"
MODIFY_PLAYERS_FOR_TOURNAMENT = "Choix 2 : Modifier la liste des ID de " \
                                "joueurs avant lancement du 1er Round"

LAST_TOURNAMENT = "Le tournoi en cours est : "
LAST_TOURNAMENT_NONE = "Il n'y a aucun tournoi de créer dans la " \
                       "base à ce jour."
INFORM_CREATE_TOURNAMENT = "Vous avez sélectionné la création d'un nouveau" \
                           " Tournoi, " \
                           "merci de completer les champs requis : "
INPUT_TOURNAMENT_NAME = "Nom du Tournoi : "
INPUT_TOURNAMENT_LOCATION = "Lieu du Tournoi : "
INFORM_INPUT_PLAYERS = "Merci de saisir les ID des 8 joueurs pour le " \
                       "tournoi : "
ERROR_INPUT_PLAYER = " Merci de saisir un ID de joueur valide svp !"
LISTING_PLAYERS_TO_CONFIRM = "Voici la liste des joueurs que vous avez " \
                             "sélectionné :"
CHOICE_TIME = ["Bullet", "Blitz", "Coup rapide"]
SELECT_CONTROL_TIME = "Voici la liste des contrôleur du temps disponibles : "
YOUR_CHOICE = "Merci de faire votre choix : "
INPUT_DESCRIPTION_TOURNAMENT = "Vous pouvez saisir une description de " \
                               "tournoi : "
INFORM_CREATE_TOURNAMENT_INTO_DB = "--- Création du Tournoi dans la base" \
                                   " de données ---"
INFORM_CREATE_PLAYERS_TOURNAMENT_INTO_DB = "--- Création de la liste des " \
                                           "joueurs rattachée au Tournoi" \
                                           " dans la base de données ---"
ERROR_PLAYER_ALREADY_IN_TOURNAMENT = "Attention cet ID de joueur a déjà été " \
                                     "saisie dans la liste liée au tournoi"
TOURNAMENT_NOT_END = "Tournoi toujours en cours !"
# MENU_ADD_PLAYER
INFORM_CREATE_PLAYER = "Vous avez sélectionné la création d'un nouveau " \
                       "Joueur dans la BDD, " \
                       "merci de completer les champs requis : "
LAST_NAME_PLAYER = "Le NOM du Joueur : "
FIRST_NAME_PLAYER = "Le PRENOM du Joueur : "
BIRTHDAY_PLAYER = "Sa Date de naissance au format dd/mm/yyyy : "
SEX_PLAYER = "Son Sexe M ou F : "
INFORM_CREATE_PLAYER_INTO_DB = "--- Création du joueur dans la base de " \
                               "données ---"
ERROR_MIN_PLAYERS_IN_DATABASE = "ATTENTION, la base de données ne contient " \
                                "pas le minimum de joueurs requis" \
                                " \npour la création d'un tournoi, merci de " \
                                "rajouter des joueurs en BDD."

# RAPPORT
SUMMARY_MENU_RAPPORT = """
--------------------------------------------------------------------
    --- Menu RAPPORT ---
            Liste de tous les Joueurs
                Choix 11 : par ordre alphabétique
                Choix 12 : par classement
                Choix 13 : par ID de joueur
              
            Liste de tous les Joueurs d'un tournoi 
                Choix 21 : par ordre alphabétique
                Choix 22 : par classement
            
            Liste de tous les tournois : Choix 3
            Liste de tous les tours/matchs d'un tournoi : Choix 4
                    
            Choix 0 => Retour au menu principal
-------------------------------------------------------------------
"""
RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME = "--- Listing des Joueurs - " \
                                        "Tri par NOM - ordre Alphabétique  ---"
RAPPORT_PLAYERS_LIST_BY_RANK = "--- Listing des Joueurs - " \
                                "Tri par Classement de joueurs ---"
RAPPORT_PLAYERS_LIST_BY_ID = "--- Listing des Joueurs par ID ---"
RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME = "--- Listing des Joueurs dans " \
                                           "un Tournoi - Tri par NOM - " \
                                           "ordre Alphabétique  ---"
RAPPORT_TOURNAMENT_LIST_BY_RANK = "--- Listing des Joueurs dans un Tournoi" \
                                   " - Tri par Classement de joueurs ---"
RAPPORT_TOURNAMENT_LIST_ALL = "--- Listing des Tournoi - " \
                              "Tri par ID de Tournoi ---"
RAPPORT_LIST_ROUNDS_OF_TOURNAMENT = "--- Listing des Tours d'un tournoi ---"
RAPPORT_LIST_MATCHS_OF_TOURNAMENT = "--- Listing des Matchs d'un tournoi ---"

# ROUNDS
CHOICE_ADD_ROUNDS = "Choix 3 : Ajouter un nouveau tour au tournoi"
SUMMARY_SUBMENU_ROUNDS = """
----------------------------------------------------------------
    --- Sous Menu ROUNDS/TOURS --- 
"""
ROUNDS1_NONE = "Lancement du Round 1 "
ROUNDS2_NONE = "Lancement du Round 2 "
ROUNDS3_NONE = "Lancement du Round 3 "
ROUNDS4_NONE = "Lancement du Round 4 "
READY_GO = "A vos pions, prêt ? Partez !"
ADD_ROUND_MENU = "Procédure d'ajout de Round au Tournoi"
TOURNAMENT_NUMBER = " du Tournoi N° "
INPUT_SCORE_MATCH = "Merci de saisir le résultat du match"
WITH_PLAYER = " pour "
CHOICE_SCORE = "\t Le joueur a gagné (Tapez : 1), " \
               "est à égalité (Tapez : 2) ou a perdu (Tapez : 3) ?"

# SUBMENU DATABASE
SUMMARY_SUBMENU_DATABASE = """
--------------------------------------------------------------------
    --- Menu BASE DE DONNEES ---
            Choix 1 : Ajouter un joueur dans la base de données
            Choix 2 : Monter le classement d'un joueur manuellement
                 
            Choix 0 : Retour au menu principal
--------------------------------------------------------------------
"""
CHOICE_UPDATE_RANK_PLAYER = "Vous avez choisi de MONTER " \
                            "un joueur au classement : \n"\
                            "Si vous souhaitez avoir la liste des joueurs en" \
                            " base de données TAPER LE CHOIX 0 \n "
INPUT_ID_PLAYER = "Merci de saisir l'ID du joueur svp : "
UPDATE_RANK_PLAYER = "Vous avez choisi de modifier "
ERROR_SELECT_PLAYER_INTO_DB = "ERREUR : Merci de taper un ID de joueur" \
                              " présent dans la base de données svp."
YOU_SELECT = "Vous avez sélectionné : "
INPUT_NEW_RANK = "Merci de saisir le nouveau classement du joueur svp : "