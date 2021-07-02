from datetime import datetime
from time import sleep

from API import controller
from MODELS import models
from LANGUAGES import french as language


def input_what_do_you_want():
    sleep(1)
    action = (input(language.WHAT_DO_YOU_WANT))
    return action


def create_players_for_tournament():
    print(language.INFORM_INPUT_PLAYERS)
    tournament_id_players = []
    i = 1
    while i < 9:
        player = ""
        while not isinstance(player, int):
            try:
                player = int(input(f"ID player{i} : "))
                tournament_id_players.append(player)
            except ValueError:
                print(language.ERROR_INPUT_PLAYER)
        i += 1
    return tournament_id_players


def create_tournament():
    print(language.INFORM_CREATE_TOURNAMENT)
    tournament_name = str(input(language.INPUT_TOURNAMENT_NAME))
    tournament_location = str(input(language.INPUT_TOURNAMENT_LOCATION))
    tournament_date = datetime.today()
    tournament_date = tournament_date.strftime("%A %d %B %Y à %H:%m")

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
                                   tournament_date, controller.NUMBER_OF_ROUNDS,
                                   tournament_time_controller, tournoi_description,
                                   rounds=[])
    return tournament


def main_menu():
    print(language.SUMMARY_MAIN_MENU)


def main_menu_tournament():
    print(language.SUMMARY_MENU_TOURNAMENT)


def main_menu_rapport():
    print(language.SUMMARY_MENU_RAPPORT)


def menu_add_player():
    print(language.INFORM_CREATE_PLAYER)
    player_name = str(input(language.LAST_NAME_PLAYER)).upper()
    player_first_name = str(input(language.FIRST_NAME_PLAYER)).lower()
    player_birthday = ""
    while not isinstance(player_birthday, datetime):
        player_birthday = (input(language.BIRTHDAY_PLAYER))
        try:
            player_birthday = datetime.strptime(player_birthday, '%d/%m/%Y')
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
