from sqlalchemy.orm import sessionmaker

import constants
from controllers import base, players
from LANGUAGES import french as language
from models import models
import views.base


class ControllersTournament:
    def __init__(self):
        self.controller = base
        self.control_player = players.ControllersPlayers()
        self.views_error = views.base.Error()
        self.views_input = views.base.Input()
        self.views_match = views.base.Match()
        self.views_menu = views.base.Menu()
        self.views_players = views.base.Players()
        self.views_rounds = views.base.Rounds()
        self.views_tournaments = views.base.Tournament()
        self.views_rapports = views.base.Rapports()
        self.generate = base.GeneratePDF()

    def create_tournament(self):
        name, location = self.views_tournaments.input_name_location()
        date = base.create_datetime_now()
        i = 1
        for element in language.CHOICE_TIME:
            self.views_tournaments.watch_choice_time_to_choice(i, element)
            i += 1
        time_controller = ""
        while time_controller not in language.CHOICE_TIME:
            try:
                choice_time = int(
                    self.views_tournaments.input_tournament_choice_time())
                if choice_time == 1:
                    time_controller = language.CHOICE_TIME[choice_time - 1]
                elif choice_time == 2:
                    time_controller = language.CHOICE_TIME[choice_time - 1]
                elif choice_time == 3:
                    time_controller = language.CHOICE_TIME[choice_time - 1]
            except TypeError:
                self.views_error.input_choice()
            except ValueError:
                self.views_error.input_choice()
        description = self.views_tournaments.input_tournament_description()
        tournament = models.Tournament(name, location,
                                       date,
                                       constants.NUMBER_OF_ROUNDS,
                                       time_controller, description)
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        session.add(tournament)
        session.commit()

    def add_players(self, table_players_id):
        add_player = 0
        tournament_id_players = ""
        while add_player == 0:
            tournament_id_players = []
            self.views_tournaments.inform_input_players()
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
                            self.generate.rapport_pdf_for_players(
                                listing,
                                language.RAPPORT_PLAYERS_LIST_BY_ID)
                    except ValueError:
                        self.views_error.input_player_for_tournament()
            # reorder list id player input
            tournament_id_players.sort()
            # extract ID player into Name_player with database
            listing_players = self.control_player.extract_listing_players(
                table_players_id)
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

    @staticmethod
    def extract_all():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        all_tournaments = session.query(models.Tournament).order_by(
            models.Tournament.tournament_id)
        return all_tournaments

    @staticmethod
    def extract_last():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_tournaments = session.query(
            models.Tournament.tournament_id).count()
        last_tournament = session.query(models.Tournament).get(
            {"tournament_id": str(count_of_tournaments)})
        return count_of_tournaments, last_tournament

    @staticmethod
    def players_per_t():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        listing_p_for_t = session.query(models.PlayersForTournament).order_by(
            models.PlayersForTournament.players_tournament_id)
        return listing_p_for_t

    @staticmethod
    def extract_count_of_match():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_match = session.query(models.Match.match_id).count()
        return count_of_match

    def extract_last_match(self):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_match = self.extract_count_of_match()
        last_match = session.query(models.Match).get(
            {"match_id": str(count_of_match)})
        return last_match

    @staticmethod
    def add_last_match_id_into_actual_round():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_rounds = session.query(models.Rounds.round_id).count()
        actual_round = session.query(models.Rounds).get(
            {"round_id": str(count_of_rounds)})
        count_of_match = session.query(models.Match.match_id).count()
        if actual_round.match1_id is None:
            actual_round.match1_id = int(count_of_match)
        elif actual_round.match2_id is None:
            actual_round.match2_id = int(count_of_match)
        elif actual_round.match3_id is None:
            actual_round.match3_id = int(count_of_match)
        elif actual_round.match4_id is None:
            actual_round.match4_id = int(count_of_match)
        session.commit()

    @staticmethod
    def add_link_between_round_tournament(last_tournament):
        Session = sessionmaker(bind=base.ENGINE)
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

    @staticmethod
    def extract_all_rounds():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        all_rounds = session.query(models.Rounds).order_by(
            models.Rounds.round_id)
        return all_rounds

    @staticmethod
    def extract_last_round():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_rounds = session.query(models.Rounds.round_id).count()
        actual_round = session.query(models.Rounds).get(
            {"round_id": str(count_of_rounds)})
        return count_of_rounds, actual_round

    def update_time_finished_round(self, date):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        last_round = self.extract_last_round()
        last_round.date_finished = date
        session.commit()

    @staticmethod
    def add_listing_players_into_db(listing_players, count_of_tournaments):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        session.add(listing_players)
        # add foreignkey link between tournament
        # and list_players_for_tournament
        last_tournament = session.query(models.Tournament).get(
            {"tournament_id": str(count_of_tournaments)})
        last_tournament.players = int(count_of_tournaments)
        session.commit()

    @staticmethod
    def last_listing_players(count_of_tournaments):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        last_listing_players = session.query(models.PlayersForTournament).get(
            {"players_tournament_id": str(count_of_tournaments)})
        return last_listing_players

    @staticmethod
    def update_last_listing_players(input_players_id):
        Session = sessionmaker(bind=base.ENGINE)
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

    # ROUNDS#####
    def add_round(self, round_number, count_of_tournaments):
        round_name = "Rounds N°" + str(
            round_number) + language.TOURNAMENT_NUMBER + str(
            count_of_tournaments)
        date = self.controller.create_datetime_now()
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        new_round = models.Rounds(round_name, date)
        new_round.link_tournament_id = int(count_of_tournaments)
        session.add(new_round)
        session.commit()

    def input_result_match(self, tournament, player1, player2, match_number):
        players_listing, \
            players_listing_id = self.control_player.reorder_players_by_rank(
                tournament)
        id_player1 = int(players_listing_id[int(player1) - 1].split("#")[0])
        name_player1 = players_listing[int(player1) - 1].split("(")[0]
        id_player2 = int(players_listing_id[int(player2) - 1].split("#")[0])
        name_player2 = players_listing[int(player2) - 1].split("(")[0]
        result_player1 = self.views_input.score_match(
            match_number, name_player1)
        result_player2 = self.views_input.score_match(
            match_number, name_player2)
        new_match = models.Match(id_player1, result_player1,
                                 id_player2, result_player2)
        return new_match

    def add_match_with_update_player_pts_into_db(self, new_match):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        session.add(new_match)
        session.commit()
        self.add_last_match_id_into_actual_round()
        # update rank
        last_match = self.extract_last_match()
        self.control_player.update_pts_match(
            last_match.id_player1, last_match.result_player_1)
        self.control_player.update_pts_match(
            last_match.id_player2, last_match.result_player_2)

    def erase_pts_tournament_players(self, players_listing_id):
        for id_player in players_listing_id:
            self.control_player.erase_pts_match_player(id_player)

    def generate_first_round(self):
        # extract list of players tournament by rank
        count, tournament = self.extract_last()
        players_listing, p_l_id = self.control_player.reorder_players_by_rank(
            tournament
        )
        # view battle with players
        self.views_match.generate_round1(players_listing)

        # joueur 1 vs 5
        new_match = self.input_result_match(
            tournament, player1=1, player2=5, match_number=1)
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 2 vs 6
        new_match = self.input_result_match(
            tournament, player1=2, player2=6, match_number=2)
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 3 vs 7
        new_match = self.input_result_match(
            tournament, player1=3, player2=7, match_number=3)
        self.add_match_with_update_player_pts_into_db(new_match)
        # joueur 4 vs 8
        new_match = self.input_result_match(
            tournament, player1=4, player2=8, match_number=4)
        self.add_match_with_update_player_pts_into_db(new_match)
        # date finished round
        date = base.create_datetime_now()
        self.update_time_finished_round(date)

    def generate_second_round(self):
        # extract list of players tournament by rank
        count_of_tournaments, tournament = self.extract_last()
        players_listing, p_l_id = self.control_player.reorder_players_by_pts(
            tournament
        )
        # view battle with players
        self.views_match.generate_round2(players_listing)

    def generate_other_round(self):
        pass
