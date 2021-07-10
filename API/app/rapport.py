import os
import subprocess
from time import sleep

from fpdf import FPDF

from API import controller
from API.app import sql
from GPU import view
from LANGUAGES import french as language

# create directory to export rapport pdf file
CURRENT_DIR = os.path.dirname(os.path.dirname(__file__))
EXPORT_DIR = os.path.join(CURRENT_DIR, "EXPORT_PDF")
if not os.path.exists(EXPORT_DIR):
    os.makedirs(EXPORT_DIR)


def players_by_abc():
    # players by abc_order
    listing = sql.extract_players_by_abc()
    generate_rapport_pdf_players(
        listing,
        language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME
    )
    return listing


def players_by_rank():
    # players by rank
    listing = sql.extract_players_by_rank()
    listing = listing[::-1]
    generate_rapport_pdf_players(listing,
                                 language.RAPPORT_PLAYERS_LIST_BY_RANK
                                 )
    return listing


def players_by_id():
    # players by rank
    listing = sql.extract_players_by_id()
    generate_rapport_pdf_players(listing,
                                 language.RAPPORT_PLAYERS_LIST_BY_ID
                                 )
    return listing


# MAIN RAPPORT
def main_rapport():
    execute = True
    while execute:
        # view main menu with response choice user
        view.main_menu_rapport()
        response_user = controller.control_input_response_user(
            view.input_what_do_you_want
        )

        if response_user == 11:
            # players by abc_order
            listing = players_by_abc()
            view.listing_rapport(
                language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing
            )

        elif response_user == 12:
            # players by rank
            listing = players_by_rank()
            view.listing_rapport(language.RAPPORT_PLAYERS_LIST_BY_RANK,
                                 listing)


        elif response_user == 13:
            # players by id
            listing = players_by_id()
            view.listing_rapport(
                language.RAPPORT_PLAYERS_LIST_BY_ABC_LAST_NAME, listing
            )

        elif response_user == 21:
            # players by last_name in tournament
            listing_p_for_t = sql.extract_listing_players_for_tournament()
            i = 1
            for p_for_t in listing_p_for_t:
                players_listing = extract_players_by_abc(p_for_t)
                view.listing_players_tournaments(
                    i, players_listing,
                    language.RAPPORT_TOURNAMENT_LIST_BY_ABC_LAST_NAME
                )
                i += 1
            sleep(1)

        elif response_user == 22:
            listing_p_for_t = sql.extract_listing_players_for_tournament()
            i = 1
            for p_for_t in listing_p_for_t:
                players_listing, players_listing_id = reorder_players_by_rank(
                    p_for_t
                )
                view.listing_players_tournaments(
                    i, players_listing,
                    language.RAPPORT_TOURNAMENT_LIST_BY_RANK
                )
                i += 1
            sleep(1)

        elif response_user == 3:
            # list tournament by id
            all_tournaments = sql.extract_all_tournament()
            view.listing_rapport(language.RAPPORT_TOURNAMENT_LIST_ALL,
                                 all_tournaments)
            sleep(1)

        elif response_user == 4:
            all_rounds = sql.extract_all_rounds()
            for info_round in all_rounds:
                print(info_round)

        elif response_user == 5:
            # list matchs by tournament
            print("travaux")

        elif response_user == 0:
            execute = False


# ____________ FUNCTION EXTRACT ____________
def extract_players_by_abc(tournament):
    players_listing = [
        tournament.player_1.last_name + " " + tournament.player_1.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_1.rank),
        tournament.player_2.last_name + " " + tournament.player_2.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_2.rank),
        tournament.player_3.last_name + " " + tournament.player_3.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_3.rank),
        tournament.player_4.last_name + " " + tournament.player_4.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_4.rank),
        tournament.player_5.last_name + " " + tournament.player_5.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_5.rank),
        tournament.player_6.last_name + " " + tournament.player_6.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_6.rank),
        tournament.player_7.last_name + " " + tournament.player_7.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_7.rank),
        tournament.player_8.last_name + " " + tournament.player_8.first_name +
        " " + language.STR_PLAYER_TOURNAMENT_rank + str(
            tournament.player_8.rank)]
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


def reorder_players_by_rank(tournament):
    players_dict = extract_players_by_rank(
        tournament.listing_players
    )
    players_dict_id = extract_players_by_rank_id(
        tournament.listing_players
    )
    players_listing = []
    players_listing_id = []
    for name, rank in sorted(players_dict.items(), key=lambda x: x[1]):
        players_listing.append(
            name + " " + language.STR_PLAYER_TOURNAMENT_rank + str(rank)
            + " " + language.STR_PLAYER_TOURNAMENT_rank2)
    players_listing = players_listing[::-1]
    for player_id, rank in sorted(players_dict_id.items(), key=lambda x: x[1]):
        players_listing_id.append(
            str(player_id) + "#" +
            language.STR_PLAYER_TOURNAMENT_rank + str(rank) + " " +
            language.STR_PLAYER_TOURNAMENT_rank2
        )
    players_listing_id = players_listing_id[::-1]
    return players_listing, players_listing_id


# ____________ FUNCTION GENERATE PDF RAPPORT ____________
def generate_rapport_pdf_players(listing, title):
    document = FPDF()
    document.add_page()
    document.set_font('helvetica', size=12)
    document.set_title(title)
    document.cell(txt=title)
    document.ln(10)
    for element in listing:
        document.cell(txt=str(element))
        document.ln(5)
    path = os.path.join(EXPORT_DIR, title + ".pdf")
    document.output(path)
    sleep(1)
    subprocess.run(['open', path], check=True)
