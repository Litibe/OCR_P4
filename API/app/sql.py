from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from MODELS import models

# engine for sql database with sqlalchemy
ENGINE = create_engine('sqlite:///sql.db', echo=False)


def init_db():
    # init database link sqlAlchemy with models.py
    MetaData(ENGINE)
    models.Base.metadata.create_all(ENGINE)


# ____________ add into database ____________
def add_player_to_database(player):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(player)
    session.commit()


def add_listing_players_into_db(listing_players, count_of_tournaments):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(listing_players)
    # add foreignkey link between tournament
    # and list_players_for_tournament
    last_tournament = session.query(models.Tournament).get(
        {"tournament_id": str(count_of_tournaments)})
    last_tournament.players = int(count_of_tournaments)
    session.commit()


def add_tournament_to_database(tournament):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(tournament)
    session.commit()


def add_round_into_db(new_round):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(new_round)
    session.commit()


def add_match_into_db(new_match):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(new_match)
    session.commit()


def add_link_between_round_tournament():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_tournaments, last_tournament = extract_last_tournament()
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


def add_last_match_id_into_actual_round():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_rounds, actual_round = extract_last_round()
    count_of_match = extract_count_of_match()
    if actual_round.match1_id is None:
        actual_round.match1_id = int(count_of_match)
    elif actual_round.match2_id is None:
        actual_round.match2_id = int(count_of_match)
    elif actual_round.match3_id is None:
        actual_round.match3_id = int(count_of_match)
    elif actual_round.match4_id is None:
        actual_round.match4_id = int(count_of_match)
    session.commit()


def update_rank_player(id_player, points):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    player = session.query(models.Players).get(
        {"player_id": str(id_player)})
    player.rank += points
    session.commit()


def update_time_finished_round(date, hours):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    last_round = extract_last_round()
    last_round.date_finished = date
    last_round.hours_finished = hours
    session.commit()


# ____________ extract into database ____________
def commit_last_listing_players(last_listing_players,
                                input_players_id):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    last_listing_players.id_player1 = input_players_id[0]
    last_listing_players.id_player2 = input_players_id[1]
    last_listing_players.id_player3 = input_players_id[2]
    last_listing_players.id_player4 = input_players_id[3]
    last_listing_players.id_player5 = input_players_id[4]
    last_listing_players.id_player6 = input_players_id[5]
    last_listing_players.id_player7 = input_players_id[6]
    last_listing_players.id_player8 = input_players_id[7]
    session.commit()


def extract_players_id_into_database():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    table_players = session.query(models.Players.player_id)
    table_players_id = []
    for element in table_players:
        table_players_id.append(element[0])
    return table_players_id


def extract_last_tournament():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_tournaments = session.query(
        models.Tournament.tournament_id).count()
    last_tournament = session.query(models.Tournament).get(
        {"tournament_id": str(count_of_tournaments)})
    return count_of_tournaments, last_tournament


def last_listing_players(count_of_tournaments):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    last_listing_players = session.query(
        models.PlayersForTournament).get(
        {"players_tournament_id": str(count_of_tournaments)})
    return last_listing_players


def extract_listing_players(table_players_id):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing_players = []
    for player_id in table_players_id:
        listing_players.append(session.query(models.Players).get(
            {"player_id": str(player_id)}))
    return listing_players


def extract_table_players_into_database():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    table_players = session.query(models.Players.player_id)
    return table_players


def extract_last_round():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_rounds = session.query(models.Rounds.round_id).count()
    actual_round = session.query(models.Rounds).get(
            {"round_id": str(count_of_rounds)})
    return count_of_rounds, actual_round


def extract_last_match_to_update_rank():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_match = extract_count_of_match()
    last_match = session.query(models.Match).get(
            {"match_id": str(count_of_match)})
    return last_match.id_player1, last_match.result_player_1,\
           last_match.id_player2,last_match.result_player_2


def extract_count_of_match():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_match = session.query(models.Match.match_id).count()
    return count_of_match

def extract_one_player_by_this_id_into_db(player_id):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    one_player = session.query(models.Players).get(
            {"player_id": str(player_id)})
    return one_player


def extract_last_player_into_db():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_players = session.query(models.Players.player_id).count()
    last_player = session.query(models.Players).get(
            {"player_id": str(count_of_players)})
    return last_player


def extract_listing_players_for_tournament():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing_p_for_t = session.query(models.PlayersForTournament).order_by(
        models.PlayersForTournament.players_tournament_id)
    return listing_p_for_t


def extract_all_tournament():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    all_tournaments = session.query(models.Tournament).order_by(
        models.Tournament.tournament_id)
    return all_tournaments


def extract_all_rounds():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    all_rounds = session.query(models.Rounds).order_by(
        models.Rounds.round_id)
    return all_rounds


def extract_players_by_abc():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing = session.query(models.Players).order_by(
        models.Players.last_name)
    return listing


def extract_players_by_rank():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing = session.query(models.Players).order_by(
        models.Players.rank)
    return listing


def extract_players_by_id():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing = session.query(models.Players).order_by(
        models.Players.player_id)
    return listing