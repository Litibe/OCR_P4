from MODELS import models as models
from GPU import view
from LANGUAGES import french as language
from API import constants

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from fpdf import FPDF
from time import sleep
import os
import subprocess

ENGINE = create_engine('sqlite:///sql.db', echo=False)


def generate_rapport(name_class, order, title):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    listing = session.query(name_class).order_by(order)
    document = FPDF()
    document.add_page()
    document.set_font('helvetica', size=12)
    document.set_title(title)
    document.cell(txt=title)
    document.ln(10)
    for element in listing:
        document.cell(txt=str(element))
        document.ln(5)
    path = os.path.join(constants.EXPORT_DIR, "listing.pdf")
    document.output(path)
    sleep(1)
    subprocess.run(['open', path], check=True)
    return listing


def init_db():
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
            listing = generate_rapport(models.Players, models.Players.last_name,
                                       language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME)
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 12:
            # players by rank
            listing = generate_rapport(models.Players, models.Players.rank,
                                       language.RAPPORT_PLAYERS_LIST_BY_ORDER)
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_ORDER, listing)

        elif response_user == 21:
            # players by last_name in tournament
            listing = generate_rapport(models.PlayersForTournament,
                                       models.PlayersForTournament.id_players_for_tournament,
                                       language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 22:
            # players by rank in tournament
            listing = generate_rapport(models.Tournament.tournament_id, models.Players.rank,
                                       language.RAPPORT_TOURNAMENT_LIST_BY_ORDER)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_BY_ORDER, listing)

        elif response_user == 3:
            # list tournament by id
            listing = generate_rapport(models.Tournament, models.Tournament.tournament_id,
                                       language.RAPPORT_TOURNAMENT_LIST_ALL)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_ALL, listing)

        elif response_user == 4:
            # list rounds by tournament
            listing = generate_rapport(models.Tournament, models.Tournament.rounds,
                                       language.RAPPORT_LIST_ROUNDS_OF_TOURNAMENT)
            view.listing_rapport(language.RAPPORT_LIST_ROUNDS_OF_TOURNAMENT, listing)

        elif response_user == 5:
            # list matchs by tournament
            listing = generate_rapport(models.Tournament, models.Tournament.rounds.matchs,
                                       language.RAPPORT_LIST_MATCHS_OF_TOURNAMENT)
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
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(tournament)
            session.commit()

        elif response_user == 2:
            tournament_id_players = view.create_players_for_tournament()
            players = models.PlayersForTournament(tournament_id_players[0], tournament_id_players[1],
                                                  tournament_id_players[2], tournament_id_players[3],
                                                  tournament_id_players[4], tournament_id_players[5],
                                                  tournament_id_players[6], tournament_id_players[7])
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(players)
            session.commit()

        elif response_user == 0:
            execute = False


def launch():
    run = True
    while run:
        # view main menu with response choice user
        view.main_menu()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 1:
            # view create tournament
            main_create_tournament()

        if response_user == 2:
            # view create player
            player_name, player_first_name, player_birthday, player_sexe = view.menu_add_player()
            player = models.Players(player_name, player_first_name, player_birthday, player_sexe)
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
