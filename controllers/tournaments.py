from random import randint
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
        self.listing_id_actual_tournament = []

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
                                models.Players.player_id)
                            self.generate.rapport_pdf_for_players(
                                listing,
                                language.RAPPORT_PLAYERS_LIST_BY_ID)
                    except ValueError:
                        self.views_error.input_player_for_tournament()
            # reorder list id player input
            tournament_id_players.sort()
            # extract ID player into Name_player with database
            listing_players = self.control_player.extract_listing_players(
                tournament_id_players)
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

    @staticmethod
    def update_time_finished_round_with_link_tournament():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_rounds = session.query(models.Rounds.round_id).count()
        actual_round = session.query(models.Rounds).get(
            {"round_id": str(count_of_rounds)})
        date = base.create_datetime_now()
        actual_round.date_finished = date
        count_of_tournament = session.query(
            models.Tournament.tournament_id).count()
        actual_tournament = session.query(models.Tournament).get(
            {"tournament_id": str(count_of_tournament)})
        if actual_tournament.rounds1 is None:
            actual_tournament.rounds1 = int(count_of_rounds)
        elif actual_tournament.rounds2 is None:
            actual_tournament.rounds2 = int(count_of_rounds)
        elif actual_tournament.rounds3 is None:
            actual_tournament.rounds3 = int(count_of_rounds)
        elif actual_tournament.rounds4 is None:
            actual_tournament.rounds4 = int(count_of_rounds)
        session.commit()

    @staticmethod
    def update_time_finished_tournament():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_tournaments = session.query(
            models.Tournament.tournament_id).count()
        last_tournament = session.query(models.Tournament).get(
            {"tournament_id": str(count_of_tournaments)})
        last_tournament.date_finished = base.create_datetime_now()
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

    def input_result_match(self, id_player1, id_player2, match_number):
        player_1 = self.control_player.extract_one_by_id(id_player1)
        result_player1 = self.views_input.score_match(
            match_number, player_1)
        result_player2 = ""
        if result_player1 == 0:
            result_player2 = 1
        elif result_player1 == 0.5:
            result_player2 = 0.5
        elif result_player1 == 1:
            result_player2 = 0
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
            id_player1=p_l_id[0],
            id_player2=p_l_id[4], match_number=1)
        self.control_player.update_adversary_match(
            p_l_id[0], p_l_id[4])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 2 vs 6
        new_match = self.input_result_match(
            id_player1=p_l_id[1],
            id_player2=p_l_id[5], match_number=2)
        self.control_player.update_adversary_match(
            p_l_id[1], p_l_id[5])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 3 vs 7
        new_match = self.input_result_match(
            id_player1=p_l_id[2],
            id_player2=p_l_id[6], match_number=3)
        self.control_player.update_adversary_match(
            p_l_id[2], p_l_id[6])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 4 vs 8
        new_match = self.input_result_match(
            id_player1=p_l_id[3],
            id_player2=p_l_id[7], match_number=4)
        self.control_player.update_adversary_match(
            p_l_id[3], p_l_id[7])
        self.add_match_with_update_player_pts_into_db(new_match)
        # date finished round
        self.update_time_finished_round_with_link_tournament()

    @staticmethod
    def sorted_player_id_after_rank(dico_id_pts, pts, dico_id_rank):
        list_player_by_pts = []
        for id_player, pts_player in dico_id_pts.items():
            if pts_player == pts:
                list_player_by_pts.append(id_player)
            else:
                pass
        liste_rank = []
        for id_player in list_player_by_pts:
            try:
                player_rank = dico_id_rank.get(id_player)
                liste_rank.append(player_rank)
            except ValueError:
                pass
        liste_rank.sort()
        return liste_rank

    def generate_second_round(self):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count = session.query(
            models.PlayersForTournament.players_tournament_id).count()
        l_players = session.query(models.PlayersForTournament).get(
            {"players_tournament_id": str(count)})
        id_players_for_round2 = []

        dico_players_id_pts = dict()
        dico_players_id_pts["id" + str(
            l_players.player_1.player_id)] = float(
            l_players.player_1.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_2.player_id)] = float(
            l_players.player_2.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_3.player_id)] = float(
            l_players.player_3.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_4.player_id)] = float(
            l_players.player_4.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_5.player_id)] = float(
            l_players.player_5.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_6.player_id)] = float(
            l_players.player_6.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_7.player_id)] = float(
            l_players.player_7.pts_tournament)
        dico_players_id_pts["id" + str(
            l_players.player_8.player_id)] = float(
            l_players.player_8.pts_tournament)

        dico_players_id_rank = dict()
        dico_players_id_rank["id" + str(
            l_players.player_1.player_id)] = l_players.player_1.rank
        dico_players_id_rank["id" + str(
            l_players.player_2.player_id)] = l_players.player_2.rank
        dico_players_id_rank["id" + str(
            l_players.player_3.player_id)] = l_players.player_3.rank
        dico_players_id_rank["id" + str(
            l_players.player_4.player_id)] = l_players.player_4.rank
        dico_players_id_rank["id" + str(
            l_players.player_5.player_id)] = l_players.player_5.rank
        dico_players_id_rank["id" + str(
            l_players.player_6.player_id)] = l_players.player_6.rank
        dico_players_id_rank["id" + str(
            l_players.player_7.player_id)] = l_players.player_7.rank
        dico_players_id_rank["id" + str(
            l_players.player_8.player_id)] = l_players.player_8.rank

        l1pts = self.sorted_player_id_after_rank(
            dico_players_id_pts, 1, dico_players_id_rank)
        l0_5pts = self.sorted_player_id_after_rank(
            dico_players_id_pts, 0.5, dico_players_id_rank)
        l0pts = self.sorted_player_id_after_rank(
            dico_players_id_pts, 0, dico_players_id_rank)
        id_players_for_round2.extend(l1pts)
        id_players_for_round2.extend(l0_5pts)
        id_players_for_round2.extend(l0pts)
        id_players_round2 = []
        for element in id_players_for_round2:
            for key, values in dico_players_id_rank.items():
                if values == element:
                    id_players_round2.append(key[2:])
        listing_players_for_round2 = []
        for id_player in id_players_round2:
            player = self.control_player.extract_one_by_id(id_player)
            listing_players_for_round2.append(player)
        self.views_match.generate_other_round(listing_players_for_round2)

        # joueur 1 vs 2
        new_match = self.input_result_match(
            id_player1=id_players_round2[0],
            id_player2=id_players_round2[1], match_number=1)
        self.control_player.update_adversary_match(
            id_players_round2[0],
            id_players_round2[1])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 3 vs 4
        new_match = self.input_result_match(
            id_player1=id_players_round2[2],
            id_player2=id_players_round2[3], match_number=2)
        self.control_player.update_adversary_match(
            id_players_round2[2],
            id_players_round2[3])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 5 vs 6
        new_match = self.input_result_match(
            id_player1=id_players_round2[4],
            id_player2=id_players_round2[5], match_number=3)
        self.control_player.update_adversary_match(
            id_players_round2[4],
            id_players_round2[5])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 7 vs 8
        new_match = self.input_result_match(
            id_player1=id_players_round2[6],
            id_player2=id_players_round2[7], match_number=4)
        self.control_player.update_adversary_match(
            id_players_round2[6],
            id_players_round2[7])
        self.add_match_with_update_player_pts_into_db(new_match)
        # date finished round
        self.update_time_finished_round_with_link_tournament()

    def generate_other_round(self):
        count_of_tournaments, last_tournament = self.extract_last()
        last_listing_players = self.last_listing_players(count_of_tournaments)
        listing_id_actual_tournament = [
            last_listing_players.player_1.player_id,
            last_listing_players.player_2.player_id,
            last_listing_players.player_3.player_id,
            last_listing_players.player_4.player_id,
            last_listing_players.player_5.player_id,
            last_listing_players.player_6.player_id,
            last_listing_players.player_7.player_id,
            last_listing_players.player_8.player_id]

        listing_id_players_for_future_round = []
        while len(listing_id_players_for_future_round) != 8:
            self.listing_id_actual_tournament = listing_id_actual_tournament
            print(self.listing_id_actual_tournament)
            while len(self.listing_id_actual_tournament) > 1:
                id_player0, id_player1 = self.search_adversary_round(
                    self.listing_id_actual_tournament)

                listing_id_players_for_future_round.append(id_player0)
                listing_id_players_for_future_round.append(id_player1)
            try:
                if listing_id_players_for_future_round[7] == "":
                    listing_id_players_for_future_round = []
            except IndexError:
                listing_id_players_for_future_round = []

        listing_players_for_round = []
        for id_player in listing_id_players_for_future_round:
            player = self.control_player.extract_one_by_id(id_player)
            listing_players_for_round.append(player)
        self.views_match.generate_other_round(
            listing_players_for_round)

        # joueur 1 vs 2
        new_match = self.input_result_match(
            id_player1=listing_id_players_for_future_round[0],
            id_player2=listing_id_players_for_future_round[1], match_number=1)
        self.control_player.update_adversary_match(
            listing_id_players_for_future_round[0],
            listing_id_players_for_future_round[1])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 3 vs 4
        new_match = self.input_result_match(
            id_player1=listing_id_players_for_future_round[2],
            id_player2=listing_id_players_for_future_round[3], match_number=2)
        self.control_player.update_adversary_match(
            listing_id_players_for_future_round[2],
            listing_id_players_for_future_round[3])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 5 vs 6
        new_match = self.input_result_match(
            id_player1=listing_id_players_for_future_round[4],
            id_player2=listing_id_players_for_future_round[5], match_number=3)
        self.control_player.update_adversary_match(
            listing_id_players_for_future_round[4],
            listing_id_players_for_future_round[5])
        self.add_match_with_update_player_pts_into_db(new_match)

        # joueur 7 vs 8
        new_match = self.input_result_match(
            id_player1=listing_id_players_for_future_round[6],
            id_player2=listing_id_players_for_future_round[7], match_number=4)
        self.control_player.update_adversary_match(
            listing_id_players_for_future_round[6],
            listing_id_players_for_future_round[7])
        self.add_match_with_update_player_pts_into_db(new_match)
        # date finished round
        self.update_time_finished_round_with_link_tournament()

    def search_adversary_round(self, listing_id_actual_tournament):
        id_player0 = self.listing_id_actual_tournament.pop(0)
        player0 = self.control_player.extract_one_by_id(id_player0)
        search = True
        id_player1 = ""
        while search:
            print(listing_id_actual_tournament)
            id_player = listing_id_actual_tournament[
                randint(0, len(listing_id_actual_tournament)-1)]

            if str(id_player) not in player0.adversary_tournament:
                id_player1 = int(id_player)
                id_to_remove = self.listing_id_actual_tournament.index(
                            id_player)
                self.listing_id_actual_tournament.pop(id_to_remove)
                search = False
            else:
                pass
        return id_player0, id_player1
