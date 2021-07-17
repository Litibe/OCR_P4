import datetime
from time import sleep

from LANGUAGES import french as language


class Error:
    @staticmethod
    def input_choice():
        print(language.ERROR_INPUT_CHOICE)

    @staticmethod
    def input_player_for_tournament():
        print(language.ERROR_INPUT_PLAYER)

    @staticmethod
    def player_already_in_tournament():
        print(language.ERROR_PLAYER_ALREADY_IN_TOURNAMENT)

    @staticmethod
    def min_players_into_db():
        print(language.ERROR_MIN_PLAYERS_IN_DATABASE)

    @staticmethod
    def select_player_into_db():
        print(language.ERROR_SELECT_PLAYER_INTO_DB)


class Input:
    @staticmethod
    def score_match(match_number, name_player):
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

    @staticmethod
    def what_do_you_want():
        action = (input(language.WHAT_DO_YOU_WANT))
        return action


class Match:
    @staticmethod
    def generate_round1(players_listing):
        print(f""" {language.ROUNDS1_NONE} : 
        Match1 : {players_listing[0]} VS {players_listing[4]}
        Match2 : {players_listing[1]} VS {players_listing[5]}
        Match3 : {players_listing[2]} VS {players_listing[6]}
        Match4 : {players_listing[3]} VS {players_listing[7]}
        \t{language.READY_GO}
            """)

    @staticmethod
    def generate_other_round(players_listing):
        print(f"""
        Match1 : {players_listing[0]} 
                VS {players_listing[1]}
        Match2 : {players_listing[2]} 
                VS {players_listing[3]}
        Match3 : {players_listing[4]} 
                VS {players_listing[5]}
        Match4 : {players_listing[6]} 
                VS {players_listing[7]}
        \t{language.READY_GO}
            """)


class Menu:
    @staticmethod
    def main_menu():
        print(language.SUMMARY_MAIN_MENU)

    @staticmethod
    def main_menu_tournament():
        print(language.SUMMARY_MENU_TOURNAMENT)

    @staticmethod
    def choice_add_players_for_tournament():
        print(language.ADD_PLAYERS_FOR_TOURNAMENT)

    @staticmethod
    def choice_return_main_menu():
        print(language.CHOICE_RETURN_MAIN_MENU)

    @staticmethod
    def return_main_menu():
        print(language.RETURN_MAIN_MENU)

    @staticmethod
    def main_menu_rapport():
        print(language.SUMMARY_MENU_RAPPORT)

    @staticmethod
    def main_database():
        print(language.SUMMARY_SUBMENU_DATABASE)

    @staticmethod
    def menu_add_player():
        print(language.INFORM_CREATE_PLAYER)
        player_name = ""
        while len(player_name) < 1:
            player_name = str(input(language.LAST_NAME_PLAYER)).upper()
        player_first_name = ""
        while len(player_first_name) < 1:
            player_first_name = str(
                input(language.FIRST_NAME_PLAYER)).capitalize()
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

    @staticmethod
    def choice_add_rounds():
        print(language.CHOICE_ADD_ROUNDS)

    @staticmethod
    def summary_submenu_rounds():
        print(language.SUMMARY_SUBMENU_ROUNDS)


class Players:

    @staticmethod
    def choice_update_rank_player():
        print(language.CHOICE_UPDATE_RANK_PLAYER)

    @staticmethod
    def input_id_player():
        id_player = ""
        while isinstance(id_player, str):
            try:
                id_player = int(input(language.INPUT_ID_PLAYER))
            except TypeError:
                pass
            except ValueError:
                pass
            return id_player
        return id_player

    @staticmethod
    def input_new_rank(player):
        print(f"{language.YOU_SELECT}:\n{player}")
        modify_rank = ""
        while isinstance(modify_rank, str):
            try:
                modify_rank = int(input(language.INPUT_NEW_RANK))
                if modify_rank < 0:
                    modify_rank = ""
                    print(language.ERROR_INPUT_CHOICE)
            except TypeError:
                print(language.ERROR_INPUT_CHOICE)
        return modify_rank

    @staticmethod
    def watch_player_details(player):
        print(player)


class Rapports:
    @staticmethod
    def listing_rapport(language_rapport, listing):
        print(language_rapport)
        for element in listing:
            print(element)
        print(
            "-------------------------------------------------------------")
        sleep(2)

    @staticmethod
    def listing_players_tournaments(i, players_listing, title):
        print(title)
        print(language.STR_PLAYER_TOURNAMENT_1, i)
        for element in players_listing:
            print("\t", element)

    @staticmethod
    def input_number_tournament():
        print(language.RAPPORT_INPUT_NUMBER_TOURNAMENT)
        number_tournament = ""
        while isinstance(number_tournament, str):
            try:
                number_tournament = int(input(
                    language.INPUT_NUMBER_TOURNAMENT))
            except TypeError:
                print(language.ERROR_INPUT_CHOICE)
            except ValueError:
                print(language.ERROR_INPUT_CHOICE)
        return number_tournament


class Rounds:

    @staticmethod
    def rounds1_none():
        print(language.ROUNDS1_NONE)

    @staticmethod
    def rounds2_none():
        print(language.ROUNDS2_NONE)

    @staticmethod
    def rounds3_none():
        print(language.ROUNDS3_NONE)

    @staticmethod
    def rounds4_none():
        print(language.ROUNDS4_NONE)

    @staticmethod
    def str_round(show_round):
        print(show_round, "\n")


class Tournament:

    @staticmethod
    def create_new_tournament():
        print(language.CREATE_NEW_TOURNAMENT)

    @staticmethod
    def input_name_location():
        print(language.CREATE_NEW_TOURNAMENT)
        name = ""
        while len(name) < 3:
            name = str(input(language.INPUT_TOURNAMENT_NAME))
        location = ""
        while len(location) < 3:
            location = str(input(language.INPUT_TOURNAMENT_LOCATION))
        return name, location

    @staticmethod
    def watch_choice_time_to_choice(i, element):
        print(f" \t Choix {i} pour {element}")

    @staticmethod
    def input_confirm_listing_players(listing_players):
        print(language.LISTING_PLAYERS_TO_CONFIRM)
        for element in listing_players:
            print(element)
        input_confirm = input(language.CONFIRM_INPUT)
        return input_confirm

    @staticmethod
    def input_player(i):
        player = input(f"ID player{i} : ")
        return player

    @staticmethod
    def input_tournament_choice_time():
        print(language.SELECT_CONTROL_TIME)
        choice_time = int(input(language.YOUR_CHOICE))
        return choice_time

    @staticmethod
    def input_tournament_description():
        description = str(input(language.INPUT_DESCRIPTION_TOURNAMENT))
        return description

    @staticmethod
    def inform_input_players():
        print(language.INFORM_INPUT_PLAYERS)

    @staticmethod
    def modify_players_for_tournament():
        print(language.MODIFY_PLAYERS_FOR_TOURNAMENT)

    @staticmethod
    def last_tournament(tournament):
        print(language.LAST_TOURNAMENT)
        print(tournament)
