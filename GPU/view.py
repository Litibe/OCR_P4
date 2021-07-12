import datetime
from time import sleep

from LANGUAGES import french as language


def input_what_do_you_want():
    sleep(1)
    action = (input(language.WHAT_DO_YOU_WANT))
    return action


def error_input_choice():
    print(language.ERROR_INPUT_CHOICE)


def input_player_for_tournament(i):
    player = input(f"ID player{i} : ")
    return player


def error_input_player_for_tournament():
    print(language.ERROR_INPUT_PLAYER)


def error_player_already_in_tournament():
    print(language.ERROR_PLAYER_ALREADY_IN_TOURNAMENT)


def confirm_listing_players_tournaments(listing_players):
    print(language.LISTING_PLAYERS_TO_CONFIRM)
    for element in listing_players:
        print(element)
    input_confirm = input(language.CONFIRM_INPUT)
    return input_confirm


def input_tournament_name_location():
    print(language.CREATE_NEW_TOURNAMENT)
    name = str(input(language.INPUT_TOURNAMENT_NAME))
    location = str(input(language.INPUT_TOURNAMENT_LOCATION))
    return name, location


def choice_update_rank_player():
    print(language.CHOICE_UPDATE_RANK_PLAYER)

def input_id_player_to_update():
    id_player = input(language.INPUT_ID_PLAYER_TO_UPDATE)
    return id_player

def input_tournament_choice_time():
    print(language.SELECT_CONTROL_TIME)
    choice_time = int(input("Merci de faire votre choix :"))
    return choice_time


def input_tournament_description():
    description = str(input(language.INPUT_DESCRIPTION_TOURNAMENT))
    return description


def main_menu():
    print(language.SUMMARY_MAIN_MENU)


def main_menu_tournament():
    print(language.SUMMARY_MENU_TOURNAMENT)


def create_new_tournament():
    print(language.LAST_TOURNAMENT_NONE)
    print(language.CREATE_NEW_TOURNAMENT)


def choice_add_players_for_tournament():
    print(language.ADD_PLAYERS_FOR_TOURNAMENT)


def modify_players_for_tournament():
    print(language.MODIFY_PLAYERS_FOR_TOURNAMENT)


def error_min_players_in_database():
    print(language.ERROR_MIN_PLAYERS_IN_DATABASE)


def last_tournament(tournament):
    print(language.LAST_TOURNAMENT)
    print(tournament)

def update_rank_player(player):
        print(f"{language.YOU_SELECT}:\n{player}")
        modify_rank = ""
        while isinstance(modify_rank, str):
            try :
                modify_rank = int(input(language.INPUT_NEW_RANK))
                if modify_rank < 0:
                    modify_rank = ""
                    print(language.ERROR_INPUT_CHOICE)
            except TypeError:
                print(language.ERROR_INPUT_CHOICE)
        return modify_rank



def error_select_player_into_db() :
        print(language.ERROR_SELECT_PLAYER_INTO_DB)

def choice_return_main_menu():
    print(language.CHOICE_RETURN_MAIN_MENU)


def return_main_menu():
    print(language.RETURN_MAIN_MENU)


def main_menu_rapport():
    print(language.SUMMARY_MENU_RAPPORT)


def main_summary_database():
    print(language.SUMMARY_SUBMENU_DATABASE)


def menu_add_player():
    print(language.INFORM_CREATE_PLAYER)
    player_name = ""
    while len(player_name) < 1:
        player_name = str(input(language.LAST_NAME_PLAYER)).upper()
    player_first_name = ""
    while len(player_first_name) < 1:
        player_first_name = str(input(language.FIRST_NAME_PLAYER)).capitalize()
    player_birthday = ""
    while not isinstance(player_birthday, datetime.datetime):
        player_birthday = (input(language.BIRTHDAY_PLAYER))
        try:
            player_birthday = datetime.datetime.strptime(player_birthday,
                                                         '%d/%m/%Y')
        except ValueError:
            print(language.ERROR_INPUT_DATE)
    player_sexe = ""
    while player_sexe != "M" and player_sexe != "F":
        player_sexe = str(input(language.SEX_PLAYER)).capitalize()
    return player_name, player_first_name, player_birthday, player_sexe


def listing_rapport(language_rapport, listing):
    print(language_rapport)
    for element in listing:
        print(element)
    print(
        "-------------------------------------------------------------")
    sleep(2)


def listing_players_tournaments(i, players_listing, title):
    print(title)
    print(language.STR_PLAYER_TOURNAMENT_1, i)
    for element in players_listing:
        print("\t", element)


def watch_player_details(player):
    print(str(player))

# ROUNDS

def choice_add_rounds():
    print(language.CHOICE_ADD_ROUNDS)


def summary_submenu_rounds():
    print(language.SUMMARY_SUBMENU_ROUNDS)


def rounds1_none():
    print(language.ROUNDS1_NONE)


def rounds2_none():
    print(language.ROUNDS2_NONE)


def rounds3_none():
    print(language.ROUNDS3_NONE)


def rounds4_none():
    print(language.ROUNDS4_NONE)


def str_round(show_round):
    print(show_round)


def generate_round1(players_listing):
    print(f""" {language.ROUNDS1_NONE} : 
    Match1 : {players_listing[0]} VS {players_listing[4]}
    Match2 : {players_listing[1]} VS {players_listing[5]}
    Match3 : {players_listing[2]} VS {players_listing[6]}
    Match4 : {players_listing[3]} VS {players_listing[7]}
    \t{language.READY_GO}
        """)

def generate_round2(players_listing):
    print(f""" {language.ROUNDS2_NONE} : 
    Match1 : {players_listing[0]} VS {players_listing[4]}
    Match2 : {players_listing[1]} VS {players_listing[5]}
    Match3 : {players_listing[2]} VS {players_listing[6]}
    Match4 : {players_listing[3]} VS {players_listing[7]}
    \t{language.READY_GO}
        """)


def input_score_match(match_number, name_player):
    print(f"{language.INPUT_SCORE_MATCH} "
          f"{str(match_number)}"
          f"{language.WITH_PLAYER}"
          f"{name_player} :"
          )
    result = ""
    while result not in [1, 2, 3]:
        try:
            result = int(input(language.CHOICE_SCORE))
        except ValueError:
            print(language.ERROR_INPUT_CHOICE)
    if result == 2:
        result = 0.5
    elif result == 3:
        result = 0
    return result
