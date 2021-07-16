import datetime
import os
import subprocess
from time import sleep

from fpdf import FPDF
from sqlalchemy import create_engine, MetaData

import constants
from controllers.players import ControllersPlayers
from controllers.tournaments import ControllersTournament
from LANGUAGES import french as language
from models import models
import views.base

# create directory to export rapport pdf file
CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
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
    date = datetime.datetime.now(constants.TIME_ZONE)
    return date


class Menu:
    def __init__(self):
        self.db = init_db()
        self.control_player = ControllersPlayers()
        self.control_tournament = ControllersTournament()
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
                except ValueError:
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
                except ValueError:
                    self.views_error.input_choice()

            if response_user == 1:
                self.control_player.add_into_db()

            elif response_user == 2:
                self.views_players.choice_update_rank_player()
                modify = True
                id_player = ""
                while modify:
                    id_player = self.views_players.input_id_player()
                    table_players_id = self.control_player.extract_players_id()
                    if id_player == 0:
                        listing = self.control_player.extract_players_by(
                            models.Players.rank)
                        self.generate.rapport_pdf_for_players(
                            listing,
                            language.RAPPORT_PLAYERS_LIST_BY_RANK)
                    elif id_player not in table_players_id:
                        self.views_error.select_player_into_db()
                    else:
                        modify = False

                self.control_player.update_rank_player(id_player)
                listing = self.control_player.extract_players_by(
                        models.Players.rank)
                self.generate.rapport_pdf_for_players(
                        listing,
                        language.RAPPORT_PLAYERS_LIST_BY_RANK)
                player = self.control_player.extract_one_by_id(
                        id_player)
                self.views_players.watch_player_details(player)

            elif response_user == 0:
                self.views_menu.return_main_menu()
                run = False

    def main_tournament(self):
        execute = True
        while execute:
            self.views_menu.main_menu_tournament()
            count_of_tournaments, \
                last_tournament = self.control_tournament.extract_last()
            # control if tournament in SQL
            if last_tournament is None:
                self.views_tournaments.create_new_tournament()
                self.views_menu.choice_return_main_menu()
            # control if tournament not finished in SQL
            elif last_tournament.players is None:
                self.views_tournaments.last_tournament(last_tournament)
                sleep(1)
                # extract id player into DB
                table_players_id = self.control_player.extract_players_id()
                # while id player <8 into DB - create player
                while len(table_players_id) < 8:
                    self.views_error.min_players_into_db()
                    self.control_player.add_into_db()
                    table_players_id.append("")
                self.views_menu.choice_add_players_for_tournament()
                self.views_menu.choice_return_main_menu()
            elif last_tournament.players is not None:
                self.views_tournaments.last_tournament(last_tournament)
                if last_tournament.rounds1 is None:
                    self.views_rounds.rounds1_none()
                elif last_tournament.rounds2 is None:
                    self.views_rounds.rounds2_none()
                elif last_tournament.rounds3 is None:
                    self.views_rounds.rounds3_none()
                elif last_tournament.rounds4 is None:
                    self.views_rounds.rounds4_none()
                self.views_menu.choice_add_rounds()
                self.views_menu.choice_return_main_menu()

            choice = [0, 1, 2, 3]
            response_user = ""
            while response_user not in choice:
                try:
                    response_user = int(
                        self.views_input.what_do_you_want())
                except TypeError:
                    self.views_error.input_choice()
                except ValueError:
                    self.views_error.input_choice()

            # menu create tournament
            if response_user == 1:
                self.control_tournament.create_tournament()

            # menu add players into tournament
            elif response_user == 2:
                table_players_id = self.control_player.extract_players_id()
                # control if min players in database to create tournament
                if len(table_players_id) < 8:
                    self.views_error.min_players_into_db()
                else:
                    # else add players into database
                    input_players_id = self.control_tournament.add_players(
                        table_players_id
                    )
                    llp = self.control_tournament.last_listing_players(
                        count_of_tournaments
                    )
                    last_listing_players = llp
                    # erase listing if players already linked
                    if last_listing_players is not None:
                        self.control_tournament.update_last_listing_players(
                            input_players_id)
                    else:
                        # create link players with tournament
                        listing_players = models.PlayersForTournament(
                            input_players_id[0], input_players_id[1],
                            input_players_id[2], input_players_id[3],
                            input_players_id[4], input_players_id[5],
                            input_players_id[6], input_players_id[7]
                        )
                        self.control_tournament.add_listing_players_into_db(
                            listing_players, count_of_tournaments
                        )

            # menu add round
            elif response_user == 3:
                self.submenu_round()

            # return main menu
            elif response_user == 0:
                execute = False

    def submenu_round(self):
        execute = True
        while execute:
            self.views_menu.summary_submenu_rounds()
            count, last_tournament = self.control_tournament.extract_last()
            if last_tournament.rounds1 is None:
                self.control_tournament.add_round(
                    round_number=1,
                    count_of_tournaments=count)
                self.control_tournament.generate_first_round()
                self.views_menu.return_main_menu()
                execute = False
            elif last_tournament.rounds2 is None:
                count, last_tournament = self.control_tournament.extract_last()
                self.views_rounds.rounds2_none()
                self.control_tournament.add_round(
                    round_number=2,
                    count_of_tournaments=count)
                self.control_tournament.generate_second_round()
                self.views_menu.return_main_menu()
                execute = False
            elif last_tournament.rounds3 is None:
                count, last_tournament = self.control_tournament.extract_last()
                self.views_rounds.rounds3_none()
                self.control_tournament.add_round(
                    count_of_tournaments=count,
                    round_number=3)
                self.control_tournament.generate_other_round()
                self.views_menu.return_main_menu()
                execute = False
            elif last_tournament.rounds4 is None:
                count, last_tournament = self.control_tournament.extract_last()
                self.views_rounds.rounds4_none()
                self.control_tournament.add_round(
                    count_of_tournaments=count,
                    round_number=4)
                self.control_tournament.generate_other_round()
                self.views_menu.return_main_menu()
                # tournament date end
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
                listing = self.control_player.extract_players_by(
                    models.Players.last_name)
                self.generate.rapport_pdf_for_players(
                    listing,
                    language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME)
                self.views_rapports.listing_rapport(
                    language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing
                )

            elif response_user == 12:
                # players by rank
                listing = self.control_player.extract_players_by(
                    models.Players.rank)
                self.generate.rapport_pdf_for_players(
                    listing,
                    language.RAPPORT_PLAYERS_LIST_BY_RANK)
                self.views_rapports.listing_rapport(
                    language.RAPPORT_PLAYERS_LIST_BY_RANK, listing
                )

            elif response_user == 13:
                # players by id
                listing = self.control_player.extract_players_by(
                    models.Players.player_id)
                self.generate.rapport_pdf_for_players(
                    listing,
                    language.RAPPORT_PLAYERS_LIST_BY_ID)
                self.views_rapports.listing_rapport(
                    language.RAPPORT_PLAYERS_LIST_BY_ID, listing
                )

            elif response_user == 21:
                # players by last_name in tournament
                listing_p_for_t = self.control_tournament.players_per_t()
                i = 1
                for p_for_t in listing_p_for_t:
                    listing = self.control_player.players_by_abc(p_for_t)
                    self.views_rapports.listing_players_tournaments(
                        i, listing,
                        language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME
                    )
                    i += 1
                sleep(1)

            elif response_user == 22:
                listing_p_for_t = self.control_tournament.players_per_t()
                i = 1
                for p_for_t in listing_p_for_t:
                    p_l, p_l_id = self.control_player.reorder_players_by_rank(
                        p_for_t
                    )
                    self.views_rapports.listing_players_tournaments(
                        i, p_l,
                        language.RAPPORT_TOURNAMENT_LIST_BY_RANK
                    )
                    i += 1
                sleep(1)

            elif response_user == 3:
                # list tournament by id
                all_tournaments = self.control_tournament.extract_all()
                self.views_rapports.listing_rapport(
                    language.RAPPORT_TOURNAMENT_LIST_ALL, all_tournaments)
                sleep(1)

            elif response_user == 4:
                all_rounds = self.control_tournament.extract_all_rounds()
                for info_round in all_rounds:
                    self.views_players.watch_player_details(info_round)

            elif response_user == 5:
                # list matchs by tournament
                print("travaux")

            elif response_user == 0:
                execute = False


class GeneratePDF:
    @staticmethod
    def rapport_pdf_for_players(listing, title):
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
