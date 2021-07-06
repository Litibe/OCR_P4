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
import datetime

ENGINE = create_engine('sqlite:///sql.db', echo=False)


def generate_rapport_pdf_actor(name_class, order, title):
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
    response_user = ""
    while run:
        try:
            response_user = function()
            response_user = int(response_user)
            run = False
        except ValueError:
            print(language.ERROR_INPUT_CHOICE)
    return response_user


def add_player_to_databse():
    # view create player
    player_name, player_first_name, player_birthday, player_sexe = view.menu_add_player()
    player = models.Players(player_name, player_first_name, player_birthday, player_sexe)
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    session.add(player)
    session.commit()


def add_players_tournaments(table_players_id):
    add_player = 0
    tournament_id_players =""
    while add_player == 0:
        tournament_id_players = []
        print(language.INFORM_INPUT_PLAYERS)
        i = 1
        while i < 9:
            player = ""
            while not isinstance(player, int):
                try:
                    player = int(view.add_player_for_tournament(i))
                    if player in table_players_id:
                        if player not in tournament_id_players:
                            tournament_id_players.append(player)
                            i += 1
                        elif player in tournament_id_players:
                            view.error_player_already_in_tournament()
                    else:
                        player = ""
                        view.error_input_player_for_tournament()
                        generate_rapport_pdf_actor(models.Players, models.Players.player_id,
                                                   language.RAPPORT_PLAYERS_LIST_BY_ID)
                except ValueError:
                    view.error_input_player_for_tournament()
        tournament_id_players.sort()
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        listing_players = []
        for player_id in table_players_id:
            listing_players.append(session.query(models.Players).get({"player_id": str(player_id)}))
        choice_confirm = ["Y", "N"]
        input_confirm = ""
        while input_confirm not in choice_confirm:
            try:
                input_confirm = str(view.confirm_listing_players_tournaments(listing_players)).upper()
            except ValueError:
                view.error_input_choice()
        if input_confirm == "Y":
            add_player = 1
    return tournament_id_players


def main_rapport():
    execute = True
    while execute:
        # view main menu with response choice user
        view.main_menu_rapport()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 11:
            # players by abc_order
            listing = generate_rapport_pdf_actor(models.Players, models.Players.last_name,
                                                 language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME)
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing)

        elif response_user == 12:
            # players by rank
            listing = generate_rapport_pdf_actor(models.Players, models.Players.rank,
                                                 language.RAPPORT_PLAYERS_LIST_BY_ORDER)
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_ORDER, listing)

        elif response_user == 21:
            # players by last_name in tournament
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            tournaments = session.query(models.PlayersForTournament).order_by(
                models.PlayersForTournament.players_tournament_id)
            i = 1
            for tournament in tournaments:
                players_listing = extract_players_by_abc(tournament)
                view.listing_players_tournaments(i, players_listing, language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME)
                i += 1
            sleep(1)

        elif response_user == 22:
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            tournaments = session.query(models.PlayersForTournament).order_by(
                models.PlayersForTournament.players_tournament_id)
            i = 1
            for tournament in tournaments:
                players_dict = extract_players_by_rank(tournament)
                players_listing = []
                for name, rank in sorted(players_dict.items(), key=lambda x: x[1]):
                    players_listing.append(name + " "+ language.STR_PLAYER_TOURNAMENT_rank + str(rank))
                players_listing = players_listing[::-1]
                view.listing_players_tournaments(i, players_listing, language.RAPPORT_TOURNAMENT_LIST_BY_ORDER)
                i += 1
            sleep(1)

        elif response_user == 3:
            # list tournament by id
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            listing = session.query(models.Tournament).order_by(models.Tournament.tournament_id)
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_ALL, listing)
            sleep(1)

        elif response_user == 4:
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            rounds = session.query(models.Rounds).order_by(models.Rounds.round_id)
            for round in rounds:
                print(round)

        elif response_user == 5:
            # list matchs by tournament
            print("travaux")

        elif response_user == 0:
            execute = False


def extract_players_by_abc(tournament):
    players_listing = []
    players_listing.append(tournament.player_1.last_name + " " + tournament.player_1.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_1.rank))
    players_listing.append(tournament.player_2.last_name + " " + tournament.player_2.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_2.rank))
    players_listing.append(tournament.player_3.last_name + " " + tournament.player_3.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_3.rank))
    players_listing.append(tournament.player_4.last_name + " " + tournament.player_4.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_4.rank))
    players_listing.append(tournament.player_5.last_name + " " + tournament.player_5.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_5.rank))
    players_listing.append(tournament.player_6.last_name + " " + tournament.player_6.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_6.rank))
    players_listing.append(tournament.player_7.last_name + " " + tournament.player_7.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_7.rank))
    players_listing.append(tournament.player_8.last_name + " " + tournament.player_8.first_name +
                           " " + language.STR_PLAYER_TOURNAMENT_rank + str(tournament.player_8.rank))
    players_listing.sort()
    return players_listing


def extract_players_by_rank(tournament):
    players_dict = {}
    name = tournament.player_1.last_name + " " + tournament.player_1.first_name
    players_dict[name] = tournament.player_1.rank
    name = tournament.player_2.last_name + " " + tournament.player_2.first_name
    players_dict[name] = tournament.player_2.rank
    name = tournament.player_3.last_name + " " + tournament.player_3.first_name
    players_dict[name] = tournament.player_3.rank
    name = tournament.player_4.last_name + " " + tournament.player_4.first_name
    players_dict[name] = tournament.player_4.rank
    name = tournament.player_5.last_name + " " + tournament.player_5.first_name
    players_dict[name] = tournament.player_5.rank
    name = tournament.player_6.last_name + " " + tournament.player_6.first_name
    players_dict[name] = tournament.player_6.rank
    name = tournament.player_7.last_name + " " + tournament.player_7.first_name
    players_dict[name] = tournament.player_7.rank
    name = tournament.player_8.last_name + " " + tournament.player_8.first_name
    players_dict[name] = tournament.player_8.rank
    return players_dict


def extract_players_by_rank_id(tournament):
    players_dict = {tournament.id_player1: tournament.player_1.rank, tournament.id_player2: tournament.player_2.rank,
                    tournament.id_player3: tournament.player_3.rank, tournament.id_player4: tournament.player_4.rank,
                    tournament.id_player5: tournament.player_5.rank, tournament.id_player6: tournament.player_6.rank,
                    tournament.id_player7: tournament.player_7.rank, tournament.id_player8: tournament.player_8.rank}
    return players_dict


def main_tournament():
    execute = True
    while execute:
        # view menu tournament
        view.main_menu_tournament()
        # print tournament [-1]
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_tournaments = session.query(models.Tournament.tournament_id).count()
        last_tournament = session.query(models.Tournament).get({"tournament_id": str(count_of_tournaments)})
        # control if tournament in SQL
        if last_tournament is None:
            last_tournament = language.LAST_TOURNAMENT_NONE
            view.create_new_tournament()
            view.choice_return_main_menu()
        # control if tournament not finished in SQL else create new tournament
        elif last_tournament.players is None:
            view.last_tournament(last_tournament)
            sleep(1)
            table_players = session.query(models.Players.player_id)
            table_players_id = []
            for element in table_players:
                table_players_id.append(element[0])
            tournament_id_players = []
            while len(table_players_id) < 8:
                view.error_min_players_in_database()
                add_player_to_databse()
                table_players_id.append("")
            view.choice_add_players_for_tournament()
            view.choice_return_main_menu()
        elif last_tournament.players is not None:
            view.last_tournament(last_tournament)
            view.modify_players_for_tournament()
            view.choice_add_rounds()
            view.choice_return_main_menu()

        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 1:
            tournament = view.create_tournament()
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            session.add(tournament)
            session.commit()

        elif response_user == 2:
            Session = sessionmaker(bind=ENGINE)
            session = Session()
            table_players = session.query(models.Players.player_id)
            table_players_id = []
            for element in table_players:
                table_players_id.append(element[0])
            tournament_id_players = []
            if len(table_players_id) < 8:
                view.error_min_players_in_database()
            else:
                tournament_id_players = add_players_tournaments(table_players_id)
                Session = sessionmaker(bind=ENGINE)
                session = Session()
                dico = {"players_tournament_id": str(count_of_tournaments)}
                last_listing_players = session.query(models.PlayersForTournament).get(dico)
                if last_listing_players is not None:
                    last_listing_players.id_player1 = tournament_id_players[0]
                    last_listing_players.id_player2 = tournament_id_players[1]
                    last_listing_players.id_player3 = tournament_id_players[2]
                    last_listing_players.id_player4 = tournament_id_players[3]
                    last_listing_players.id_player5 = tournament_id_players[4]
                    last_listing_players.id_player6 = tournament_id_players[5]
                    last_listing_players.id_player7 = tournament_id_players[6]
                    last_listing_players.id_player8 = tournament_id_players[7]
                else:
                    listing_players = models.PlayersForTournament(tournament_id_players[0], tournament_id_players[1],
                                                                  tournament_id_players[2], tournament_id_players[3],
                                                                  tournament_id_players[4], tournament_id_players[5],
                                                                  tournament_id_players[6], tournament_id_players[7])
                    session.add(listing_players)
                    # add foreignkey link between tournament and list_players_for_tournament
                    last_tournament = session.query(models.Tournament).get({"tournament_id": str(count_of_tournaments)})
                    last_tournament.players = int(count_of_tournaments)
                session.commit()

        elif response_user == 3:
            submenu_round()


        elif response_user == 0:
            execute = False


def submenu_round():
    execute = True
    while execute:
        view.summary_submenu_rounds()
        Session = sessionmaker(bind=ENGINE)
        session = Session()
        count_of_tournaments = session.query(models.Tournament.tournament_id).count()
        last_tournament = session.query(models.Tournament).get({"tournament_id": str(count_of_tournaments)})
        if last_tournament.rounds1 is None:
            view.rounds1_none()
            round_number = 1
            round1 = add_round(round_number, count_of_tournaments, last_tournament)
            generate_round(round_number)
            view.return_main_menu()
            execute = False
        elif last_tournament.rounds2 is None:
            view.rounds2_none()
            round_number = 2
            add_round(round_number, count_of_tournaments, last_tournament)
        elif last_tournament.rounds3 is None:
            view.rounds3_none()
            round_number = 3
            add_round(round_number, count_of_tournaments, last_tournament)
        elif last_tournament.rounds4 is None:
            view.rounds4_none()
            round_number = 4
            add_round(round_number, count_of_tournaments, last_tournament)


def add_round(round_number, count_of_tournaments, last_tournament):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    round_name = "Rounds N°" + str(round_number) + language.TOURNAMENT_NUMBER + str(count_of_tournaments)
    date_now = datetime.datetime.now(constants.TIME_ZONE)
    round_date_started = date_now.strftime("%d/%m/%Y")
    round_date_started = datetime.datetime.strptime(round_date_started, '%d/%m/%Y')
    round_hours_started = date_now.strftime("%H:%M")
    round = models.Rounds(round_name, round_date_started, round_hours_started)
    round.link_tournament_id = int(count_of_tournaments)
    session.add(round)
    session.commit()
    count_of_rounds = session.query(models.Rounds.round_id).count()
    if round_number == 1:
        last_tournament.rounds1 = int(count_of_rounds)
        session.commit()
    elif round_number == 2:
        last_tournament.rounds2 = int(count_of_rounds)
        session.commit()
    elif round_number == 3:
        last_tournament.rounds3 = int(count_of_rounds)
        session.commit()
    elif round_number == 4:
        last_tournament.rounds4 = int(count_of_rounds)
        session.commit()
    return round


def generate_round(round_number):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    count_of_tournaments = session.query(models.Tournament.tournament_id).count()
    tournament = session.query(models.Tournament).get({"tournament_id": str(count_of_tournaments)})
    players_dict = extract_players_by_rank(tournament.listing_players)
    players_dict_id = extract_players_by_rank_id(tournament.listing_players)
    players_listing = []
    players_listing_id = []
    for name, rank in sorted(players_dict.items(), key=lambda x: x[1]):
        players_listing.append(name + " " + language.STR_PLAYER_TOURNAMENT_rank + str(rank))
    players_listing = players_listing[::-1]
    for id, rank in sorted(players_dict_id.items(), key=lambda x: x[1]):
        players_listing_id.append(str(id) + "#" + language.STR_PLAYER_TOURNAMENT_rank + str(rank))
    players_listing_id = players_listing_id[::-1]
    if round_number == 1:
        count_of_rounds = session.query(models.Rounds.round_id).count()
        round = session.query(models.Rounds).get({"round_id": str(count_of_rounds)})
        view.generate_round1(players_listing)
        #joueur 1 vs 5
        id_player1 = int(players_listing_id[0].split("#")[0])
        result_player1 = view.input_score_match(1, 1, players_listing[0])
        id_player2 = int(players_listing_id[4].split("#")[0])
        result_player2 = view.input_score_match(1, 2, players_listing[4])
        match1 = models.Match(id_player1, result_player1, id_player2, result_player2)
        session.add(match1)
        session.commit()
        count_of_match = session.query(models.Match.match_id).count()
        round.match1_id = int(count_of_match)
        tournament.listing_players.player_1.rank += result_player1
        tournament.listing_players.player_5.rank += result_player2
        session.commit()
        # joueur 2 vs 6
        id_player1 = int(players_listing_id[1].split("#")[0])
        result_player1 = view.input_score_match(2, 1, players_listing[1])
        id_player2 = int(players_listing_id[5].split("#")[0])
        result_player2 = view.input_score_match(2, 2, players_listing[5])
        match2 = models.Match(id_player1, result_player1, id_player2, result_player2)
        session.add(match2)
        session.commit()
        count_of_match = session.query(models.Match.match_id).count()
        round.match2_id = int(count_of_match)
        tournament.listing_players.player_2.rank += result_player1
        tournament.listing_players.player_6.rank += result_player2
        session.commit()
        # joueur 3 vs 7
        id_player1 = int(players_listing_id[2].split("#")[0])
        result_player1 = view.input_score_match(3, 1, players_listing[2])
        id_player2 = int(players_listing_id[6].split("#")[0])
        result_player2 = view.input_score_match(3, 2, players_listing[6])
        match3 = models.Match(id_player1, result_player1, id_player2, result_player2)
        session.add(match3)
        session.commit()
        count_of_match = session.query(models.Match.match_id).count()
        round.match3_id = int(count_of_match)
        tournament.listing_players.player_3.rank += result_player1
        tournament.listing_players.player_7.rank += result_player2
        session.commit()
        # joueur 4 vs 8
        id_player1 = int(players_listing_id[3].split("#")[0])
        result_player1 = view.input_score_match(4, 1, players_listing[3])
        id_player2 = int(players_listing_id[7].split("#")[0])
        result_player2 = view.input_score_match(4, 2, players_listing[7])
        match4 = models.Match(id_player1, result_player1, id_player2, result_player2)
        session.add(match4)
        session.commit()
        count_of_match = session.query(models.Match.match_id).count()
        round.match4_id = int(count_of_match)
        tournament.listing_players.player_4.rank += result_player1
        tournament.listing_players.player_8.rank += result_player2
        session.commit()
        #date finished round
        date_now = datetime.datetime.now(constants.TIME_ZONE)
        round_date_finished = date_now.strftime("%d/%m/%Y")
        round_date_finished = datetime.datetime.strptime(round_date_finished, '%d/%m/%Y')
        round_hours_finished = date_now.strftime("%H:%M")
        round.date_finished = round_date_finished
        round.hours_finished = round_hours_finished
        session.commit()




def launch():
    run = True
    while run:
        # view main menu with response choice user
        view.main_menu()
        response_user = control_response_user(view.input_what_do_you_want)

        if response_user == 1:
            add_player_to_databse()
            view.return_main_menu()

        if response_user == 2:
            # view create tournament
            main_tournament()

        elif response_user == 3:
            # view menu_rapport
            main_rapport()
            view.return_main_menu()

        elif response_user == 0:
            run = False
