#####################
# models
STR_PLAYER_1 = "Player ID N °"
STR_PLAYER_2 = "born on"
STR_PLAYER_3 = "sex:"
STR_PLAYER_RANK = "No."
STR_PLAYER_RANK2 = "in the ranking"
STR_PLAYER_PTS_TOURNAMENT = "with"
STR_PLAYER_PTS_TOURNAMENT2 = "points current tournament"
STR_PLAYER_PTS = "points"

STR_PLAYER_TOURNAMENT_1 = "Here are the IDs of players present" \
                          "during Tournament N °"
STR_PLAYER_TOURNAMENT_rank = "N °"
STR_PLAYER_TOURNAMENT_rank2 = "in the ranking"

STR_TOURNAMENT_1 = "Here are the tournament details - ID N °"
STR_TOURNAMENT_2 = "Tournament name:"
STR_TOURNAMENT_3 = "Tournament start date and location: on"
STR_TOURNAMENT_4 = "Tournament carried out in"
STR_TOURNAMENT_5 = "tours"
STR_TOURNAMENT_6 = "The time control is on"
STR_TOURNAMENT_7 = "Tournament description:"
STR_TOURNAMENT_STARTED = "Tournament start date:"
STR_TOURNAMENT_FINISHED = "End of tournament date:"


STR_MATCH_1 = "This is match ID #"
STR_MATCH_2 = "with the configuration:"
STR_SCORE = "(score ="
STR_SCORE2 = "point)"
STR_ROUNDS_1 = "Tours ID n °"
STR_ROUNDS_2 = "with match ID N °"
STR_ROUND_STARTED = "Start Date and Time:"
STR_ROUND_FINISHED = "End Date and Time:"
ROUNDS_NAME = "Rounds N °"
#####################
# CONTROLLER
RETURN_MAIN_MENU = "--- Return to the main menu ---"
CHOICE_RETURN_MAIN_MENU = "Choice 0: return to the main menu"
#####################
# VIEWS
# MAIN_MENU
SUMMARY_MAIN_MENU = """
-------------------------------------------------- -------------
♖♖♖ Welcome to the Chess Club tournament program! ♖♖♖
    In summary :
            Choice 1: Access to the DATABASE Menu:
                        - Player management
            Choice 2: Access to the TOURNAMENT Menu ♖
            Choice 3: Access to the REPORTS Menu
            Choice 0: Exit the program
-------------------------------------------------- -----------
"""
WHAT_DO_YOU_WANT = "What would you like to do:"
ERROR_INPUT_CHOICE = "\n Please enter a valid choice!"
ERROR_INPUT_DATE = "\n Please enter a valid date!"
CONFIRM_INPUT = "Do you confirm your entry? (Y / n)"

# MENU_TOURNAMENT
SUMMARY_MENU_TOURNAMENT = """
--------------------------------------------------------------------
    --- TOURNAMENT menu ---
"""
CREATE_NEW_TOURNAMENT = "Choice 1: ♖ Create a new tournament ♖"
ADD_PLAYERS_FOR_TOURNAMENT = "Choice 2: Add the eight players for" \
                             "tournament"
MODIFY_PLAYERS_FOR_TOURNAMENT = "Choice 2: Modify the list of IDs from" \
                                "players before the launch of the 1st Round"

LAST_TOURNAMENT = "The current tournament: "
LAST_TOURNAMENT_NONE = "There is no tournament to create in the" \
                       "base to date."
INFORM_CREATE_TOURNAMENT = "You have selected the creation of a new" \
                           "Tournament," \
                           "please complete the required fields:"
INPUT_TOURNAMENT_NAME = "Tournament name:"
INPUT_TOURNAMENT_LOCATION = "Tournament location:"
INFORM_INPUT_PLAYERS = "If you want to have the list of players in" \
                        "database TYPE CHOICE 0 \n" \
                       "Please enter the IDs of the 8 players for the" \
                       "tournament:"
ERROR_INPUT_PLAYER = "Please enter a valid player ID!"
LISTING_PLAYERS_TO_CONFIRM = "Here is the list of players you have" \
                             "selected:"
CHOICE_TIME = ["Bullet", "Blitz", "Quick hit"]
SELECT_CONTROL_TIME = "Here is the list of available time controllers:"
YOUR_CHOICE = "Please make your choice:"
INPUT_DESCRIPTION_TOURNAMENT = "You can enter a description of" \
                               "tournament:"
INFORM_CREATE_TOURNAMENT_INTO_DB = "--- Creation of the Tournament " \
                                   "in the database" \
                                   " of data ---"
INFORM_CREATE_PLAYERS_TOURNAMENT_INTO_DB = "--- Creation of the list of" \
                                           "players attached to the" \
                                           " Tournament" \
                                           "in the database ---"
ERROR_PLAYER_ALREADY_IN_TOURNAMENT = "Attention this player ID has " \
                                     "already been" \
                                     "entered in the list linked to" \
                                     " the tournament"
TOURNAMENT_NOT_END = "Tournament still in progress!"
# MENU_ADD_PLAYER
INFORM_CREATE_PLAYER = "You have selected the creation of a new" \
                       "player, please complete the required fields:"
LAST_NAME_PLAYER = "The NAME of the Player:"
FIRST_NAME_PLAYER = "The NAME of the Player:"
BIRTHDAY_PLAYER = "His Date of birth in dd / mm / yyyy format:"
SEX_PLAYER = "His Gender MALE or FEMALE (m / f):"
INFORM_CREATE_PLAYER_INTO_DB = "--- Player creation in the database of" \
                               "data ---"
ERROR_MIN_PLAYERS_IN_DATABASE = "WARNING, the database does not contain" \
                                "not the minimum number of players required" \
                                "\n for creating a tournament, please" \
                                "add BDD players."

# RAPPORT
SUMMARY_MENU_RAPPORT = """
--------------------------------------------------------------------
    --- REPORT menu ---
            List of all Players
                Choice 11: in alphabetical order
                Choice 12: by ranking
                Choice 13: by player ID
            List of all Players in a tournament
                Choice 21: in alphabetical order
                Choice 22: by ranking
            List of all tournaments:
                Choice: 3
            List of all rounds and matches in a tournament:
                Choice: 4
            Choice 0 : Return to the main menu
-------------------------------------------------------------------
"""
RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME = "--- Player Listing -" \
                                        "Sort by NAME - Alphabetical order ---"
RAPPORT_PLAYERS_LIST_BY_RANK = "--- List of Players -" \
                                "Sorted by Player Ranking ---"
RAPPORT_PLAYERS_LIST_BY_ID = "--- List of Players by ID ---"
RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME = "--- List of Players in" \
                                           "a Tournament - Sorted by NAME -" \
                                           "alphabetical order  ---"
RAPPORT_TOURNAMENT_LIST_BY_RANK = "--- Listing of Players in a Tournament" \
                                   "- Sorted by Player Ranking ---"
RAPPORT_TOURNAMENT_LIST_ALL = "--- Tournament Listing -" \
                              "Sort by Tournament ID ---"
RAPPORT_LIST_ROUNDS_OF_TOURNAMENT = "--- Listing of Tours & Matches" \
                                    "of a tournament ---"
RAPPORT_LIST_MATCHS_OF_TOURNAMENT = "--- Listing of Tournament Matches ---"
RAPPORT_INPUT_NUMBER_TOURNAMENT = "Please enter the Tournament ID for" \
                                 "extraction: \n" \
                                 "If you want to have the" \
                                 "list of tournaments in" \
                                 "database TYPE CHOICE 0 \n"
INPUT_NUMBER_TOURNAMENT = "Please enter the Tournament ID in question:"
# ROUNDS
CHOICE_ADD_ROUNDS = "Choice 3: Add a new round to the tournament"
SUMMARY_SUBMENU_ROUNDS = """
----------------------------------------------------------------
    --- Sub Menu ROUNDS / TOURS ---
"""
ROUNDS1_NONE = "Launch of Round 1"
ROUNDS2_NONE = "Launch of Round 2"
ROUNDS3_NONE = "Launch of Round 3"
ROUNDS4_NONE = "Launch of Round 4"
READY_GO = "On your pawns, ready? Go!"
ADD_ROUND_MENU = "Procedure for adding a Round to the Tournament"
TOURNAMENT_NUMBER = "of Tournament N °"
INPUT_SCORE_MATCH = "Please enter the match result"
WITH_PLAYER = "for"
CHOICE_SCORE = "\t The player won (Type: 1)," \
               "tied (Type: 2) or lost (Type: 3)?"

# SUBMENU DATABASE
SUMMARY_SUBMENU_DATABASE = """
--------------------------------------------------------------------
    --- DATABASE menu ---
            Choice 1: Add a player to the database
            Choice 2: Manually move up a player's ranking
            Choice 0: Return to the main menu
--------------------------------------------------------------------
"""
CHOICE_UPDATE_RANK_PLAYER = "You have chosen to RISE" \
                            "a ranked player: \n" \
                            "If you want to have the list of players in" \
                            "database TYPE CHOICE 0 \n"
INPUT_ID_PLAYER = "Please enter the player ID:"
UPDATE_RANK_PLAYER = "You have chosen to modify"
ERROR_SELECT_PLAYER_INTO_DB = "ERROR: Please enter a player ID" \
                              "present in the database please."
YOU_SELECT = "You have selected:"
INPUT_NEW_RANK = "Please enter the new player rating:"
