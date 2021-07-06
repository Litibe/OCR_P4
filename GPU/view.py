import datetime
from time import sleep

from API import constants
from MODELS import models
from LANGUAGES import french as language


def input_what_do_you_want():
    sleep(1)
    action = (input(language.WHAT_DO_YOU_WANT))
    return action


def error_input_choice():
    print(language.ERROR_INPUT_CHOICE)


def add_player_for_tournament(i):
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
    input_confir = input(language.CONFIRM_INPUT)
    return input_confir


def create_tournament():
    print(language.INFORM_CREATE_TOURNAMENT)
    tournament_name = str(input(language.INPUT_TOURNAMENT_NAME))
    tournament_location = str(input(language.INPUT_TOURNAMENT_LOCATION))
    date_now = datetime.datetime.now(constants.TIME_ZONE)
    tournament_date_started = date_now.strftime("%d/%m/%Y")
    tournament_date_started = datetime.datetime.strptime(tournament_date_started, '%d/%m/%Y')
    tournament_hours_started = date_now.strftime("%H:%M")
    print(language.SELECT_CONTROL_TIME)
    i = 1
    for element in language.CHOICE_TIME:
        print(f" \t Choix {i} pour {element}")
        i += 1
    tournament_time_controller = ""
    while tournament_time_controller not in language.CHOICE_TIME:
        try:
            choix = int(input("Merci de faire votre choix :"))
            if choix == 1:
                tournament_time_controller = language.CHOICE_TIME[choix - 1]
            elif choix == 2:
                tournament_time_controller = language.CHOICE_TIME[choix - 1]
            elif choix == 3:
                tournament_time_controller = language.CHOICE_TIME[choix - 1]
            else:
                pass
        except TypeError:
            print(language.ERROR_INPUT_CHOICE)
        except ValueError:
            print(language.ERROR_INPUT_CHOICE)

    tournoi_description = str(input(language.INPUT_DESCRIPTION_TOURNAMENT))

    tournament = models.Tournament(tournament_name, tournament_location,
                                   tournament_date_started, tournament_hours_started, constants.NUMBER_OF_ROUNDS,
                                   tournament_time_controller, tournoi_description)
    return tournament


def main_menu():
    print(language.SUMMARY_MAIN_MENU)


def main_menu_tournament():
    print(language.SUMMARY_MENU_TOURNAMENT)


def create_new_tournament():
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


def choice_return_main_menu():
    print(language.CHOICE_RETURN_MAIN_MENU)


def return_main_menu():
    print(language.RETURN_MAIN_MENU)


def main_menu_rapport():
    print(language.SUMMARY_MENU_RAPPORT)


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
            player_birthday = datetime.datetime.strptime(player_birthday, '%d/%m/%Y')
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
    print("----------------------------------------------------------------------------")
    sleep(2)


def listing_players_tournaments(i, players_listing, title):
    print(title)
    print(language.STR_PLAYER_TOURNAMENT_1, i)
    for element in players_listing:
        print("\t", element)


# ROUNDS

def choice_add_rounds():
    print(language.CHOICE_ADD_ROUNDS)


def summary_submenu_rounds():
    print(language.SUMMARY_SUBMENU_ROUNDS)


def rounds1_none():
    print(language.ROUNDS1_NONE)


def str_round(round):
    print(round)


def generate_round1(players_listing):
    print("Match1")
    print(players_listing[0] + " VS " + players_listing[4])
    print("Match2")
    print(players_listing[1] + " VS " + players_listing[5])
    print("Match3")
    print(players_listing[2] + " VS " + players_listing[6])
    print("Match4")
    print(players_listing[3] + " VS " + players_listing[7])


def input_score_match(number_match, number_player, name):
    print(language.INPUT_SCORE_MATCH + str(number_match) + " " + language.WITH_PLAYER + str(number_player) + " :")
    print(name)
    result = ""
    while result not in [1, 2, 3]:
        try:
            result = int(input(language.CHOICE_SCORE))
        except TypeError:
            print(language.ERROR_INPUT_CHOICE)
    if result == 2:
        result = 0.5
    elif result == 3:
        result = 0
    else:
        pass
    return result
