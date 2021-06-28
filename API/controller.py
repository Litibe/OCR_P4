import os

from API import models as models
from GPU import view
from LANGUAGUES import french as languague

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
    print(languague.INIT_DATABASE)
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
            print(languague.ERROR_INPUT_CHOICE)
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
            view.listing_rapport(languague.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 12:
            # players by rank
            listing = generate_rapport(models.Players, models.Players.rank)
            view.listing_rapport(languague.RAPPORT_PLAYERS_LIST_BY_ORDER, listing)

        elif response_user == 21:
            # players by last_name in tournament
            listing = generate_rapport(models.Tournament.tournament_id, models.Players.last_name)
            view.listing_rapport(languague.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 22:
            # players by rank in tournament
            listing = generate_rapport(models.Tournament.tournament_id, models.Players.rank)
            view.listing_rapport(languague.RAPPORT_TOURNAMENT_LIST_BY_ORDER, listing)

        elif response_user == 3:
            # list tournament by id
            listing = generate_rapport(models.Tournament, models.Tournament.tournament_id)
            view.listing_rapport(languague.RAPPORT_TOURNAMENT_LIST_ALL, listing)

        elif response_user == 4:
            # list rounds by tournament
            listing = generate_rapport(models.Tournament, models.Tournament.rounds)
            view.listing_rapport(languague.RAPPORT_LIST_ROUNDS_OF_TOURNAMENT, listing)

        elif response_user == 5:
            # list matchs by tournament
            listing = generate_rapport(models.Tournament, models.Tournament.rounds.matchs)
            view.listing_rapport(languague.RAPPORT_LIST_MATCHS_OF_TOURNAMENT, listing)

        elif response_user == 0:
            execute = False
            launch()


def launch():
    run = True
    while run:
        # view main menu with response choice user
        view.main_menu()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 2:
            # view create player
            player_name, player_first_name, player_birthday, player_sexe = view.menu_add_player()
            player = models.Players(player_name, player_first_name, player_birthday, player_sexe)
            print(player)
            print(languague.INFORM_CREATE_PLAYER_INTO_DB)
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(player)
            session.commit()
            print(languague.RETURN_MAIN_MENU)

        elif response_user == 3:
            # view menu_rapport
            run = False
            main_rapport()

        elif response_user == 0:
            run = False
