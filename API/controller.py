from time import sleep

from API import constants
from API.app import sql, rapport, control_datetime, fct_round
from GPU import view
from LANGUAGES import french as language
from MODELS import models


def control_input_response_user(function):
    run = True
    response_user = ""
    while run:
        try:
            response_user = function()
            response_user = int(response_user)
            run = False
        except ValueError:
            print(language.ERROR_INPUT_CHOICE)
    return response_user


def add_players_tournaments(table_players_id):
    add_player = 0
    tournament_id_players = ""
    while add_player == 0:
        tournament_id_players = []
        print(language.INFORM_INPUT_PLAYERS)
        i = 1
        while i < 9:
            player = ""
            while not isinstance(player, int):
                try:
                    player = int(view.input_player_for_tournament(i))
                    if player in table_players_id:
                        if player not in tournament_id_players:
                            tournament_id_players.append(player)
                            i += 1
                        elif player in tournament_id_players:
                            view.error_player_already_in_tournament()
                    else:
                        player = ""
                        view.error_input_player_for_tournament()
                        listing_players = sql.extract_players_by_rank()
                        rapport.generate_rapport_pdf_players(listing_players,
                            language.RAPPORT_PLAYERS_LIST_BY_ID)
                except ValueError:
                    view.error_input_player_for_tournament()
        # reorder list id player input
        tournament_id_players.sort()
        # extract ID player into Name_player with database
        listing_players = sql.extract_listing_players(table_players_id)
        # confirm input ID players OK or Not
        choice_confirm = ["Y", "N"]
        input_confirm = ""
        while input_confirm not in choice_confirm:
            try:
                input_confirm = str(view.confirm_listing_players_tournaments(
                    listing_players)).upper()
            except ValueError:
                view.error_input_choice()
        if input_confirm == "Y":
            add_player = 1
    return tournament_id_players


def create_player_into_db():
    name, first_name, birthday, sexe = view.menu_add_player()
    player = models.Players(
        name, first_name, birthday, sexe
    )
    sql.add_player_to_database(player)


def create_tournament():
    name, location = view.input_tournament_name_location()
    date_started, hours_started, = control_datetime.create_datetime_now()
    i = 1
    for element in language.CHOICE_TIME:
        print(f" \t Choix {i} pour {element}")
        i += 1
    time_controller = ""
    while time_controller not in language.CHOICE_TIME:
        try:
            choice_time = int(view.input_tournament_choice_time())
            if choice_time == 1:
                time_controller = language.CHOICE_TIME[choice_time - 1]
            elif choice_time == 2:
                time_controller = language.CHOICE_TIME[choice_time - 1]
            elif choice_time == 3:
                time_controller = language.CHOICE_TIME[choice_time - 1]
            else:
                pass
        except TypeError:
            view.error_input_choice()
        except ValueError:
            view.error_input_choice()
    description = view.input_tournament_description()
    tournament = models.Tournament(name, location,
                                   date_started, hours_started,
                                   constants.NUMBER_OF_ROUNDS,
                                   time_controller, description)
    return tournament


def main_tournament():
    execute = True
    while execute:
        # view menu tournament
        view.main_menu_tournament()
        # print tournament [-1]
        count_of_tournaments, last_tournament = sql.extract_last_tournament()
        # control if tournament in SQL
        if last_tournament is None:
            view.create_new_tournament()
            view.choice_return_main_menu()
        # control if tournament not finished in SQL else create new tournament
        elif last_tournament.players is None:
            view.last_tournament(last_tournament)
            sleep(1)
            # extract id player into DB
            table_players = sql.extract_table_players_into_database()
            table_players_id = []
            for element in table_players:
                table_players_id.append(element[0])
            while len(table_players_id) < 8:
                view.error_min_players_in_database()
                create_player_into_db()
                table_players_id.append("")
            view.choice_add_players_for_tournament()
            view.choice_return_main_menu()
        elif last_tournament.players is not None:
            view.last_tournament(last_tournament)
            view.modify_players_for_tournament()
            view.choice_add_rounds()
            view.choice_return_main_menu()
        response_user = control_input_response_user(
            view.input_what_do_you_want
        )
        # menu create tournament
        if response_user == 1:
            tournament = create_tournament()
            sql.add_tournament_to_database(tournament)

        # menu add players into tournament
        elif response_user == 2:
            table_players_id = sql.extract_players_id_into_database()
            # control if min players in database to create tournament
            if len(table_players_id) < 8:
                view.error_min_players_in_database()
            else:
                # else add players into database
                input_players_id = add_players_tournaments(
                    table_players_id
                )
                last_listing_players = sql.last_listing_players(
                    count_of_tournaments
                )
                # erase listing if players already linked
                if last_listing_players is not None:
                    sql.commit_last_listing_players(last_listing_players,
                                                    input_players_id)
                else:
                    # create link players with tournament
                    listing_players = models.PlayersForTournament(
                        input_players_id[0], input_players_id[1],
                        input_players_id[2], input_players_id[3],
                        input_players_id[4], input_players_id[5],
                        input_players_id[6], input_players_id[7]
                    )
                    sql.add_listing_players_into_db(
                        listing_players, count_of_tournaments
                    )

        # menu add round
        elif response_user == 3:
            fct_round.submenu_round()

        # return main menu
        elif response_user == 0:
            execute = False


def update_rank_player(player_id):
    try :
        player = sql.extract_last_player_into_db(player_id)
        print(player)
    except IndexError :
        print("joueur pas dans la base")

def input_id_player():
    id_player = ""
    while isinstance(id_player, str):
        try:
            id_player = int(view.input_id_player_to_update())
        except ValueError:
            pass
    return id_player

def main_database():
    run = True
    while run:
        view.main_summary_database()
        response_user = control_input_response_user(
            view.input_what_do_you_want)

        if response_user == 1:
            create_player_into_db()

        elif response_user == 2:
            view.choice_update_rank_player()
            modify = True
            while modify :
                id_player = input_id_player()
                if id_player == 0:
                    rapport.players_by_abc()
                    rapport.players_by_rank()
                else :
                    modify = False
            update_rank_player(id_player)

        elif response_user == 3:
            # view menu_rapport
            rapport.main_rapport()
            view.return_main_menu()

        elif response_user == 0:
            view.return_main_menu()
            run = False


def launch():
    run = True
    while run:
        # view main menu with response choice user
        view.main_menu()
        response_user = control_input_response_user(
            view.input_what_do_you_want)

        if response_user == 1:
            main_database()
            view.return_main_menu()

        elif response_user == 2:
            # view create tournament
            main_tournament()

        elif response_user == 3:
            # view menu_rapport
            rapport.main_rapport()
            view.return_main_menu()

        elif response_user == 0:
            run = False
