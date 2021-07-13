from sqlalchemy.orm import sessionmaker

from controllers import base
from LANGUAGES import french as language
import views.base
from models import models


class ControllersPlayers:
    def __init__(self):
        self.views_error = views.base.Error()
        self.views_input = views.base.Input()
        self.views_match = views.base.Match()
        self.views_menu = views.base.Menu()
        self.views_players = views.base.Players()

    def add_into_db(self):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_players = session.query(models.Players.player_id).count()
        name, first_name, birthday, sexe = self.views_menu.menu_add_player()
        player = models.Players(
            name, first_name, birthday, sexe, rank=count_of_players+1
        )
        session.add(player)
        session.commit()
        player = self.extract_one_by_id(count_of_players+1)
        self.views_players.watch_player_details(player)

    @staticmethod
    def extract_one_by_id(player_id):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        one_player = session.query(models.Players).get(
            {"player_id": str(player_id)})
        return one_player

    @staticmethod
    def extract_last_player():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        count_of_players = session.query(models.Players.player_id).count()
        last_player = session.query(models.Players).get(
            {"player_id": str(count_of_players)})
        return last_player

    @staticmethod
    def extract_players_by(order):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        listing = session.query(models.Players).order_by(order)
        return listing

    @staticmethod
    def extract_listing_players(table_players_id):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        listing_players = []
        for player_id in table_players_id:
            listing_players.append(session.query(models.Players).get(
                {"player_id": str(player_id)}))
        return listing_players

    @staticmethod
    def extract_players_id():
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        table_players = session.query(models.Players.player_id)
        table_players_id = []
        for element in table_players:
            table_players_id.append(element[0])
        return table_players_id

    @staticmethod
    def extract_players_by_rank_id(tournament):
        players_dict_id = {
            tournament.id_player1: tournament.player_1.rank,
            tournament.id_player2: tournament.player_2.rank,
            tournament.id_player3: tournament.player_3.rank,
            tournament.id_player4: tournament.player_4.rank,
            tournament.id_player5: tournament.player_5.rank,
            tournament.id_player6: tournament.player_6.rank,
            tournament.id_player7: tournament.player_7.rank,
            tournament.id_player8: tournament.player_8.rank
        }
        return players_dict_id

    @staticmethod
    def players_by_abc(tournament):
        players_listing = [
            tournament.player_1.last_name + " " +
            tournament.player_1.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_1.rank),
            tournament.player_2.last_name + " " +
            tournament.player_2.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_2.rank),
            tournament.player_3.last_name + " " +
            tournament.player_3.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_3.rank),
            tournament.player_4.last_name + " " +
            tournament.player_4.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_4.rank),
            tournament.player_5.last_name + " " +
            tournament.player_5.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_5.rank),
            tournament.player_6.last_name + " " +
            tournament.player_6.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_6.rank),
            tournament.player_7.last_name + " " +
            tournament.player_7.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_7.rank),
            tournament.player_8.last_name + " " +
            tournament.player_8.first_name +
            " " + language.STR_PLAYER_TOURNAMENT_rank + str(
                tournament.player_8.rank)]
        players_listing.sort()
        return players_listing

    @staticmethod
    def extract_players_by_rank(tournament):
        players_dict = {}
        name = (tournament.player_1.last_name + " " +
                tournament.player_1.first_name)
        players_dict[name] = tournament.player_1.rank
        name = (tournament.player_2.last_name + " " +
                tournament.player_2.first_name)
        players_dict[name] = tournament.player_2.rank
        name = (tournament.player_3.last_name + " " +
                tournament.player_3.first_name)
        players_dict[name] = tournament.player_3.rank
        name = (tournament.player_4.last_name + " " +
                tournament.player_4.first_name)
        players_dict[name] = tournament.player_4.rank
        name = (tournament.player_5.last_name + " " +
                tournament.player_5.first_name)
        players_dict[name] = tournament.player_5.rank
        name = (tournament.player_6.last_name + " " +
                tournament.player_6.first_name)
        players_dict[name] = tournament.player_6.rank
        name = (tournament.player_7.last_name + " " +
                tournament.player_7.first_name)
        players_dict[name] = tournament.player_7.rank
        name = (tournament.player_8.last_name + " " +
                tournament.player_8.first_name)
        players_dict[name] = tournament.player_8.rank
        return players_dict

    def reorder_players_by_rank(self, tournament):
        players_dict = self.extract_players_by_rank(
            tournament.listing_players
        )
        players_dict_id = self.extract_players_by_rank_id(
            tournament.listing_players
        )
        players_listing = []
        players_listing_id = []
        for name, rank in sorted(players_dict.items(), key=lambda x: x[1]):
            players_listing.append(
                name + " " + language.STR_PLAYER_TOURNAMENT_rank + str(rank)
                + language.STR_PLAYER_TOURNAMENT_rank2)

        for player_id, rank in sorted(players_dict_id.items(),
                                      key=lambda x: x[1]):
            players_listing_id.append(
                str(player_id)
            )
        return players_listing, players_listing_id

    def reorder_players_by_pts(self, tournament):
        players_dict = self.extract_players_by_rank(
            tournament.listing_players
        )
        players_dict_id = self.extract_players_by_rank_id(
            tournament.listing_players
        )
        players_listing = []
        players_listing_id = []
        for name, pts_tournament, rank in sorted(
                players_dict.items(), key=lambda x: x[1]
        ):
            players_listing.append(
                name + " " + language.STR_PLAYER_PTS_TOURNAMENT +
                str(pts_tournament) + language.STR_PLAYER_PTS_TOURNAMENT2
                + language.STR_PLAYER_RANK + str(
                    rank) + language.STR_PLAYER_RANK2)
        players_listing = players_listing[::-1]
        for player_id, pts_tournament in sorted(
                players_dict_id.items(), key=lambda x: x[1]
        ):
            players_listing_id.append(
                str(player_id) + "#" +
                language.STR_PLAYER_PTS_TOURNAMENT + str(
                    pts_tournament) + " " +
                language.STR_PLAYER_PTS_TOURNAMENT2 + "#"
            )
        players_listing_id = players_listing_id[::-1]
        return players_listing, players_listing_id

    @staticmethod
    def update_pts_match(id_player, pts_player):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        player = session.query(models.Players).get(
            {"player_id": str(id_player)})
        player.pts_tournament += int(pts_player)
        session.commit()

    @staticmethod
    def update_adversary_match(id_player, id_adversary):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        player = session.query(models.Players).get(
            {"player_id": str(id_player)})
        player.pts_tournament += (str(id_adversary) + " , ")
        session.commit()

    def update_rank_player(self, id_player):
        player_to_change_rank = self.extract_one_by_id(
            id_player)
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        modify_rank = 0
        table_players_id = self.extract_players_id()
        while modify_rank not in table_players_id:
            modify_rank = self.views_players.input_new_rank(
                player_to_change_rank)

        ranks_players = self.extract_players_by(models.Players.rank)
        for players in ranks_players:
            if players.rank >= modify_rank:
                player = session.query(models.Players).get(
                    {"player_id": str(players.player_id)})
                player.rank += 1
            else:
                pass
        player_to_change_rank = session.query(models.Players).get(
                    {"player_id": str(id_player)})
        player_to_change_rank.rank = modify_rank
        session.commit()

    @staticmethod
    def erase_pts_match_player(id_player):
        Session = sessionmaker(bind=base.ENGINE)
        session = Session()
        player = session.query(models.Players).get(
            {"player_id": str(id_player)})
        player.pts_tournament = 0
        player.adversary_tournament = ""
        session.commit()
