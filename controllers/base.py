import datetime
import os
import subprocess
from time import sleep

from fpdf import FPDF
from sqlalchemy import create_engine, MetaData, sql
from sqlalchemy.orm import sessionmaker

import constants
from controllers.players import ControllersPlayers
from LANGUAGES import french as language
from models import models
import views.base

# create directory to export rapport pdf file
CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
EXPORT_DIR = os.path.join(CURRENT_DIR, "EXPORT_PDF")
if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)

# engine for sql database with sqlalchemy
ENGINE = create_engine('sqlite:///base_sql.db')


def init_db():
    # init database link sqlAlchemy with models.py
    MetaData(ENGINE)
    models.Base.metadata.create_all(ENGINE)
    return True


def create_datetime_now():
    date_now = datetime.datetime.now(constants.TIME_ZONE)
    date = date_now.strftime('%d/%m/%Y %H:%M:%S')
    # date = date_now.strftime('%d/%m/%Y')
    # date = datetime.datetime.strptime(date, '%d/%m/%Y')
    # hours = date_now.strftime("%H:%M")
    return date


class Menu:
    def __init__(self):
        self.db = init_db()
        self.control_player = ControllersPlayers()
        self.control_tournament = ControlTournament()
        self.views_error = views.base.Error()
        self.views_input = views.base.Input()
        self.views_match = views.base.Match()
        self.views_menu = views.base.Menu()
        self.views_players = views.base.Players()
        self.views_rounds = views.base.Rounds()
        self.views_tournaments = views.base.Tournament()
        self.views_rapports = views.base.Rapports()
        self.generate = GeneratePDF()

    def main(self):
        """ Main Menu of Application """
        run = True
        while run:
            # view main menu with response choice user
            self.views_menu.main_menu()
            choice = [0, 1, 2, 3]
            response_user = ""
            while response_user not in choice:
                try:
                    response_user = int(
                        self.views_input.what_do_you_want())
                except TypeError:
                    self.views_error.input_choice()

            if response_user == 1:
                self.main_database()
                self.views_menu.return_main_menu()

            elif response_user == 2:
                # view create tournament
                self.main_tournament()
                self.views_menu.return_main_menu()

            elif response_user == 3:
                # view menu_rapport
                self.main_rapport()
                self.views_menu.return_main_menu()

            elif response_user == 0:
                run = False

    def main_database(self):
        run = True
        while run:
            self.views_menu.main_database()
            choice = [0, 1, 2]
            response_user = ""
            while response_user not in choice:
                try:
                    response_user = int(
                        self.views_input.what_do_you_want())
                except TypeError:
                    self.views_error.input_choice()

            if response_user == 1:
                self.control_player.add_into_db()

            elif response_user == 2:
                self.views_players.choice_update_rank_player()
                modify = True
                id_player = ""
                while modify:
                    id_player = self.views_players.input_id_player()
                    if id_player == 0:
                        listing = self.control_player.extract_players_by(
                            models.Players.rank)
                        self.generate.rapport_pdf_for_players(
                            listing,
                            language.RAPPORT_PLAYERS_LIST_BY_RANK)
                    else:
                        modify = False
                try:
                    self.control_player.update_rank_player(id_player)
                    listing = self.control_player.extract_players_by(
                        models.Players.rank)
                    self.generate.rapport_pdf_for_players(
                        listing,
                        language.RAPPORT_PLAYERS_LIST_BY_RANK)
                    player = self.control_player.extract_one_by_id(
                        id_player)
                    self.views_players.watch_player_details(player)
                except IndexError:
                    self.views_error.select_player_into_db()

            elif response_user == 0:
                self.views_menu.return_main_menu()
                run = False

    def main_tournament(self):
        execute = True
        while execute:
            # view menu tournament
            self.views_menu.main_menu_tournament()
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
                if last_tournament.rounds1 is None:
                    view.modify_players_for_tournament()
                    view.rounds1_none()
                elif last_tournament.rounds2 is None:
                    view.rounds2_none()
                elif last_tournament.rounds3 is None:
                    view.rounds3_none()
                elif last_tournament.rounds4 is None:
                    view.rounds4_none()
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

    def main_rapport(self):
        execute = True
        while execute:
            # view main menu with response choice user
            self.views_menu.main_menu_rapport()
            choice = [0, 11, 12, 13, 21, 22, 3, 4, 5]
            response_user = ""
            while response_user not in choice:
                try:
                    response_user = int(
                        self.views_input.what_do_you_want())
                except TypeError:
                    self.views_error.input_choice()

            if response_user == 11:
                # players by abc_order
                listing = players_by_abc()
                view.listing_rapport(
                    language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing
                )

            elif response_user == 12:
                # players by rank
                listing = players_by_rank()
                view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_RANK,
                                     listing)


            elif response_user == 13:
                # players by id
                listing = players_by_id()
                view.listing_rapport(
                    language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing
                )

            elif response_user == 21:
                # players by last_name in tournament
                listing_p_for_t = sql.extract_listing_players_for_tournament()
                i = 1
                for p_for_t in listing_p_for_t:
                    players_listing = extract_players_by_abc(p_for_t)
                    view.listing_players_tournaments(
                        i, players_listing,
                        language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME
                    )
                    i += 1
                sleep(1)

            elif response_user == 22:
                listing_p_for_t = sql.extract_listing_players_for_tournament()
                i = 1
                for p_for_t in listing_p_for_t:
                    players_listing, players_listing_id = reorder_players_by_rank(
                        p_for_t
                    )
                    view.listing_players_tournaments(
                        i, players_listing,
                        language.RAPPORT_TOURNAMENT_LIST_BY_RANK
                    )
                    i += 1
                sleep(1)

            elif response_user == 3:
                # list tournament by id
                all_tournaments = sql.extract_all_tournament()
                view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_ALL,
                                     all_tournaments)
                sleep(1)

            elif response_user == 4:
                all_rounds = sql.extract_all_rounds()
                for info_round in all_rounds:
                    print(info_round)

            elif response_user == 5:
                # list matchs by tournament
                print("travaux")

            elif response_user == 0:
                execute = False


class ControlTournament:
    def __init__(self):
        self.control_player = ControllersPlayers()
        self.views_error = views.base.Error()
        self.views_input = views.base.Input()
        self.views_match = views.base.Match()
        self.views_menu = views.base.Menu()
        self.views_players = views.base.Players()
        self.views_rounds = views.base.Rounds()
        self.views_tournaments = views.base.Tournament()
        self.views_rapports = views.base.Rapports()
        self.generate = GeneratePDF()

    def create_tournament(self):
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

    def add_players_tournaments(self, table_players_id):
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
                        player = int(
                            self.views_tournaments.input_player(i))
                        if player in table_players_id:
                            if player not in tournament_id_players:
                                tournament_id_players.append(player)
                                i += 1
                            elif player in tournament_id_players:
                                self.views_error.player_already_in_tournament()
                        else:
                            player = ""
                            self.views_error.input_player_for_tournament()
                            listing = self.control_player.extract_players_by(
                                models.Players.rank)
                            self.generate.rapport_pdf_players(
                                listing,
                                language.RAPPORT_PLAYERS_LIST_BY_ID)
                    except ValueError:
                        self.views_error.input_player_for_tournament()
            # reorder list id player input
            tournament_id_players.sort()
            # extract ID player into Name_player with database
            listing_players = sql.extract_listing_players(table_players_id)
            # confirm input ID players OK or Not
            choice_confirm = ["Y", "N"]
            input_confirm = ""
            while input_confirm not in choice_confirm:
                try:
                    input_confirm = str(
                        self.views_tournaments.input_confirm_listing_players(
                            listing_players)).upper()
                except ValueError:
                    self.views_error.input_choice()
            if input_confirm == "Y":
                add_player = 1
        return tournament_id_players

    def extract_all_tournament(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        all_tournaments = session.query(models.Tournament).order_by(
            models.Tournament.tournament_id)
        return all_tournaments

    def extract_last_tournament(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_tournaments = session.query(
            models.Tournament.tournament_id).count()
        last_tournament = session.query(models.Tournament).get(
            {"tournament_id": str(count_of_tournaments)})
        return count_of_tournaments, last_tournament

    def extract_count_of_match(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_match = session.query(models.Match.match_id).count()
        return count_of_match

    def extract_last_match_to_update_pts(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_match = self.extract_count_of_match()
        last_match = session.query(models.Match).get(
            {"match_id": str(count_of_match)})
        return last_match.id_player1, last_match.result_player_1, \
               last_match.id_player2, last_match.result_player_2

    def add_last_match_id_into_actual_round(self, actual_round):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_match = self.extract_count_of_match()
        if actual_round.match1_id is None:
            actual_round.match1_id = int(count_of_match)
        elif actual_round.match2_id is None:
            actual_round.match2_id = int(count_of_match)
        elif actual_round.match3_id is None:
            actual_round.match3_id = int(count_of_match)
        elif actual_round.match4_id is None:
            actual_round.match4_id = int(count_of_match)
        session.commit()

    def add_link_between_round_tournament(self, last_tournament):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_rounds = session.query(models.Rounds.round_id).count()
        if last_tournament.rounds1 is None:
            last_tournament.rounds1 = int(count_of_rounds)
            session.commit()
        elif last_tournament.rounds2 is None:
            last_tournament.rounds2 = int(count_of_rounds)
            session.commit()
        elif last_tournament.rounds3 is None:
            last_tournament.rounds3 = int(count_of_rounds)
            session.commit()
        elif last_tournament.rounds4 is None:
            last_tournament.rounds4 = int(count_of_rounds)
            session.commit()

    def extract_all_rounds(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        all_rounds = session.query(models.Rounds).order_by(
            models.Rounds.round_id)
        return all_rounds

    def extract_last_round(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_rounds = session.query(models.Rounds.round_id).count()
        actual_round = session.query(models.Rounds).get(
            {"round_id": str(count_of_rounds)})
        return count_of_rounds, actual_round

    def update_time_finished_round(self, date):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        last_round = self.extract_last_round()
        last_round.date_finished = date
        session.commit()

    def add_listing_players_into_db(self, listing_players,
                                    count_of_tournaments):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        session.add(listing_players)
        # add foreignkey link between tournament
        # and list_players_for_tournament
        last_tournament = session.query(models.Tournament).get(
            {"tournament_id": str(count_of_tournaments)})
        last_tournament.players = int(count_of_tournaments)
        session.commit()

    def extract_listing_players_for_tournament(self):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        listing_p_for_t = session.query(models.PlayersForTournament).order_by(
            models.PlayersForTournament.players_tournament_id)
        return listing_p_for_t

    def last_listing_players(self, count_of_tournaments):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        last_listing_players = session.query(models.PlayersForTournament).get(
            {"players_tournament_id": str(count_of_tournaments)})
        return last_listing_players

    def update_last_listing_players(self, input_players_id):
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_tournaments = session.query(
            models.Tournament.tournament_id).count()
        last_listing_players = session.query(models.PlayersForTournament).get(
            {"players_tournament_id": str(count_of_tournaments)})
        last_listing_players.id_player1 = input_players_id[0]
        last_listing_players.id_player2 = input_players_id[1]
        last_listing_players.id_player3 = input_players_id[2]
        last_listing_players.id_player4 = input_players_id[3]
        last_listing_players.id_player5 = input_players_id[4]
        last_listing_players.id_player6 = input_players_id[5]
        last_listing_players.id_player7 = input_players_id[6]
        last_listing_players.id_player8 = input_players_id[7]
        session.commit()


class GeneratePDF:
    def rapport_pdf_for_players(self, listing, title):
        document = FPDF()
        document.add_page()
        document.set_font('helvetica', size=12)
        document.set_title(title)
        document.cell(txt=title)
        document.ln(10)
        for element in listing:
            document.cell(txt=str(element))
            document.ln(5)
        path = os.path.join(EXPORT_DIR, title[3:-4] + ".pdf")
        document.output(path)
        sleep(1)
        subprocess.run(['open', path], check=True)
