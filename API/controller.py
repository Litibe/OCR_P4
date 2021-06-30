from API import models as models
from GPU import view
from LANGUAGES import french as language

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

NUMBER_OF_ROUNDS = 4
ENGINE = create_engine('sqlite:///sql.db', echo=False)

def generate_rapport(name_class,order):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing = session.query(name_class).order_by(order)
    return listing

def init_db():
    print(language.INIT_DATABASE)
    metadata = MetaData(ENGINE)
    models.Base.metadata.create_all(ENGINE)


def control_response_user(function):
    run = True
    while run:
        response_user = function()
        try:
            response_user = int(response_user)
            run = False
        except ValueError:
            print(language.ERROR_INPUT_CHOICE)
    return response_user


def main_rapport():
    execute = True
    while execute:
        # view main menu with response choice user
        view.main_menu_rapport()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 11:
            # players by abc_order
            listing = generate_rapport(models.Players, models.Players.last_name)
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 12:
            # players by rank
            listing = generate_rapport(models.PlayersForTournament, models.Players.rank)
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_ORDER, listing)

        elif response_user == 21:
            # players by last_name in tournament
            listing = generate_rapport(models.PlayersForTournament, models.PlayersForTournament.id_players_for_tournament)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 22:
            # players by rank in tournament
            listing = generate_rapport(models.Tournament.tournament_id, models.Players.rank)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_BY_ORDER, listing)

        elif response_user == 3:
            # list tournament by id
            listing = generate_rapport(models.Tournament, models.Tournament.tournament_id)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_ALL, listing)

        elif response_user == 4:
            # list rounds by tournament
            listing = generate_rapport(models.Tournament, models.Tournament.rounds)
            view.listing_rapport(language.RAPPORT_LIST_ROUNDS_OF_TOURNAMENT, listing)

        elif response_user == 5:
            # list matchs by tournament
            listing = generate_rapport(models.Tournament, models.Tournament.rounds.matchs)
            view.listing_rapport(language.RAPPORT_LIST_MATCHS_OF_TOURNAMENT, listing)

        elif response_user == 0:
            execute = False


def main_create_tournament():
    execute = True
    while execute:
        # view menu tournament with response choice user
        view.main_menu_tournament()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 1:
            tournament = view.create_tournament()
            print(language.INFORM_CREATE_TOURNAMENT_INTO_DB)
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(tournament)
            session.commit()

        elif response_user == 2:
            tournament_id_players = view.create_players_for_tournament()
            players = models.PlayersForTournament(int(tournament_id_players[0]), tournament_id_players[1],
                                                  tournament_id_players[2], tournament_id_players[3],
                                                  tournament_id_players[4], tournament_id_players[5],
                                                  tournament_id_players[6], tournament_id_players[7])
            print(players)
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(players)
            session.commit()
            print(language.INFORM_CREATE_PLAYERS_TOURNAMENT_INTO_DB)

        elif response_user == 0:
            execute = False






def launch():
    run = True
    while run:
        # view main menu with response choice user
        view.main_menu()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 1 :
            # view create tournament
            main_create_tournament()

        if response_user == 2:
            # view create player
            player_name, player_first_name, player_birthday, player_sexe = view.menu_add_player()
            player = models.Players(player_name, player_first_name, player_birthday, player_sexe)
            print(language.INFORM_CREATE_PLAYER_INTO_DB)
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(player)
            session.commit()
            print(language.RETURN_MAIN_MENU)

        elif response_user == 3:
            # view menu_rapport
            main_rapport()
            print(language.RETURN_MAIN_MENU)

        elif response_user == 0:
            run = False
