import datetime
import os
import subprocess
from time import sleep

from fpdf import FPDF
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

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
            choice_menu = [0, 1, 2, 3]
            self.views_menu.main_menu_tournament()
            count_of_tournaments, \
                last_tournt = self.control_tournament.extract_last()
            # control if tournament in SQL
            if last_tournt is None or last_tournt.date_finished is not None:
                self.views_tournaments.create_new_tournament()
                self.views_menu.choice_return_main_menu()
            # control if tournament not finished in SQL
            elif last_tournt.players is None:
                self.views_tournaments.last_tournament(last_tournt)
                choice_menu.remove(1)
                print(choice_menu)
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
            elif last_tournt.players is not None:
                choice_menu.remove(1)
                choice_menu.remove(2)
                self.views_tournaments.last_tournament(last_tournt)
                if last_tournt.rounds1 is None:
                    self.views_rounds.rounds1_none()
                elif last_tournt.rounds2 is None:
                    self.views_rounds.rounds2_none()
                elif last_tournt.rounds3 is None:
                    self.views_rounds.rounds3_none()
                elif last_tournt.rounds4 is None:
                    self.views_rounds.rounds4_none()
                self.views_menu.choice_add_rounds()
                self.views_menu.choice_return_main_menu()

            response_user = ""
            while response_user not in choice_menu:
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
                execute = False

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
            elif last_tournament.rounds2 is None:
                count, last_tournament = self.control_tournament.extract_last()
                self.views_rounds.rounds2_none()
                self.control_tournament.add_round(
                    round_number=2,
                    count_of_tournaments=count)
                self.control_tournament.generate_second_round()
                self.views_menu.return_main_menu()
            elif last_tournament.rounds3 is None:
                count, last_tournament = self.control_tournament.extract_last()
                self.views_rounds.rounds3_none()
                self.control_tournament.add_round(
                    count_of_tournaments=count,
                    round_number=3)
                self.control_tournament.generate_other_round()
                self.views_menu.return_main_menu()
            elif last_tournament.rounds4 is None:
                count, last_tournament = self.control_tournament.extract_last()
                self.views_rounds.rounds4_none()
                self.control_tournament.add_round(
                    count_of_tournaments=count,
                    round_number=4)
                self.control_tournament.generate_other_round()
                self.views_menu.return_main_menu()
                # tournament date end
                self.control_tournament.update_time_finished_tournament()
                listing_players \
                    = self.control_tournament.last_listing_players(count)
                listing_id_actual_tournament = [
                    listing_players.player_1.player_id,
                    listing_players.player_2.player_id,
                    listing_players.player_3.player_id,
                    listing_players.player_4.player_id,
                    listing_players.player_5.player_id,
                    listing_players.player_6.player_id,
                    listing_players.player_7.player_id,
                    listing_players.player_8.player_id]
                for id_player in listing_id_actual_tournament:
                    self.control_player.erase_pts_match_player(id_player)
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
                except ValueError:
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
                count_of_tournaments, \
                    last_tournament = self.control_tournament.extract_last()

                wait_input = True
                while wait_input:
                    response_user = ""
                    while isinstance(response_user, str):
                        try:
                            response_user = int(
                                self.views_rapports.input_number_tournament(
                                    count_of_tournaments))
                        except TypeError:
                            self.views_error.input_choice()
                        except ValueError:
                            self.views_error.input_choice()
                    if response_user == 0:
                        all_tournaments = self.control_tournament.extract_all()
                        listing_tour = ""
                        for tour in all_tournaments:
                            listing_tour += language.STR_TOURNAMENT_1
                            listing_tour += str(tour.tournament_id)
                            listing_tour += "\n"
                            listing_tour += "\t" + str(tour.name)
                            listing_tour += " "
                            listing_tour += language.STR_TOURNAMENT_STARTED
                            listing_tour += tour.date_started.strftime(
                                '%d/%m/%Y %H:%M:%S')
                            listing_tour += "\n"
                        self.generate.rapport_pdf_for_players_tournament(
                            listing_tour,
                            language.RAPPORT_TOURNAMENT_LIST_ALL)
                    elif response_user < 0:
                        response_user = ""
                        print(language.ERROR_INPUT_CHOICE)
                    elif response_user > count_of_tournaments:
                        response_user = ""
                        print(language.ERROR_INPUT_CHOICE)
                    else:
                        wait_input = False

                # players by last_name in tournament
                Session = sessionmaker(bind=ENGINE)
                session = Session()
                players_for_t = session.query(
                    models.PlayersForTournament).get(
                    {"players_tournament_id": str(response_user)})

                players_listing = self.control_player.players_by_abc(
                        players_for_t)

                self.views_rapports.listing_players_tournaments(
                        response_user, players_listing,
                        language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME
                    )
                self.generate.rapport_pdf_for_players(
                    players_listing,
                    language.RAPPORT_TOURNAMENT_LIST_BY_RANK)
                sleep(1)

            elif response_user == 22:
                count_of_tournaments, \
                    last_tournament = self.control_tournament.extract_last()
                wait_input = True
                while wait_input:
                    response_user = ""
                    while isinstance(response_user, str):
                        try:
                            response_user = int(
                                self.views_rapports.input_number_tournament(
                                    count_of_tournaments))
                        except TypeError:
                            self.views_error.input_choice()
                        except ValueError:
                            self.views_error.input_choice()
                    if response_user == 0:
                        all_tournaments = self.control_tournament.extract_all()
                        listing_tour = ""
                        for tour in all_tournaments:
                            listing_tour += language.STR_TOURNAMENT_1
                            listing_tour += str(tour.tournament_id)
                            listing_tour += "\n"
                            listing_tour += "\t" + str(tour.name)
                            listing_tour += " "
                            listing_tour += language.STR_TOURNAMENT_STARTED
                            listing_tour += tour.date_started.strftime(
                                '%d/%m/%Y %H:%M:%S')
                            listing_tour += "\n"
                        self.generate.rapport_pdf_for_players_tournament(
                            listing_tour,
                            language.RAPPORT_TOURNAMENT_LIST_ALL)
                    elif response_user < 0:
                        response_user = ""
                        print(language.ERROR_INPUT_CHOICE)
                    elif response_user > count_of_tournaments:
                        response_user = ""
                        print(language.ERROR_INPUT_CHOICE)
                    else:
                        wait_input = False

                # players by last_name in tournament
                Session = sessionmaker(bind=ENGINE)
                session = Session()
                tournament = session.query(
                    models.Tournament).get(
                    {"tournament_id": str(response_user)})
                players_listing, \
                    p_id = self.control_player.reorder_players_by_rank(
                        tournament)
                self.views_rapports.listing_players_tournaments(
                        response_user, players_listing,
                        language.RAPPORT_TOURNAMENT_LIST_BY_RANK
                    )
                self.generate.rapport_pdf_for_players(
                    players_listing,
                    language.RAPPORT_TOURNAMENT_LIST_BY_RANK)
                sleep(1)

            elif response_user == 3:
                # list tournament by id
                all_tournaments = self.control_tournament.extract_all()
                self.generate.rapport_pdf_for_tournament(
                    all_tournaments,
                    language.RAPPORT_TOURNAMENT_LIST_ALL)
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

    @staticmethod
    def rapport_pdf_for_tournament(listing, title):
        document = FPDF()
        document.add_page()
        document.set_font('helvetica', size=12)
        document.set_title(title)
        document.cell(txt=title)
        document.ln(10)
        for element in listing:
            document.multi_cell(w=0, txt=str(element))
            document.ln(5)
        path = os.path.join(EXPORT_DIR, title[3:-4] + ".pdf")
        document.output(path)
        sleep(1)
        subprocess.run(['open', path], check=True)

    @staticmethod
    def rapport_pdf_for_players_tournament(listing, title):
        document = FPDF()
        document.add_page()
        document.set_font('helvetica', size=12)
        document.set_title(title)
        document.cell(txt=title)
        document.ln(10)
        document.multi_cell(w=0, txt=str(listing))
        path = os.path.join(EXPORT_DIR, title[3:-4] + ".pdf")
        document.output(path)
        sleep(1)
        subprocess.run(['open', path], check=True)
