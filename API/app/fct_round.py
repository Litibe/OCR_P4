from API.app import sql, rapport, control_datetime
from GPU import view
from LANGUAGES import french as language
from MODELS import models


def submenu_round():
    execute = True
    while execute:
        view.summary_submenu_rounds()
        count_of_tournaments, last_tournament = sql.extract_last_tournament()
        if last_tournament.rounds1 is None:
            view.rounds1_none()
            # create round
            add_round(count_of_tournaments=count_of_tournaments,
                      round_number=1
                      )
            sql.add_link_between_round_tournament()
            # generate first round
            generate_first_round()
            view.return_main_menu()
            execute = False
        elif last_tournament.rounds2 is None:
            view.rounds2_none()
            add_round(count_of_tournaments=count_of_tournaments,
                      round_number=2
                      )
            sql.add_link_between_round_tournament()
            generate_other_round()
        elif last_tournament.rounds3 is None:
            view.rounds3_none()
            add_round(count_of_tournaments=count_of_tournaments,
                      round_number=3
                      )
            sql.add_link_between_round_tournament()
            generate_other_round()
        elif last_tournament.rounds4 is None:
            view.rounds4_none()
            add_round(count_of_tournaments=count_of_tournaments,
                      round_number=4
                      )
            sql.add_link_between_round_tournament()
            generate_other_round()


def add_round(round_number, count_of_tournaments):
    round_name = "Rounds N°" + str(
        round_number) + language.TOURNAMENT_NUMBER + str(count_of_tournaments)
    date_started, hours_started = control_datetime.create_datetime_now()
    new_round = models.Rounds(round_name, date_started, hours_started)
    new_round.link_tournament_id = int(count_of_tournaments)
    sql.add_round_into_db(new_round)


def input_result_match(tournament, player1, player2, match_number):
    players_listing, players_listing_id = rapport.reorder_players_by_rank(
        tournament
    )
    id_player1 = int(players_listing_id[int(player1) - 1].split("#")[0])
    name_player1 = players_listing[int(player1) - 1].split("(")[0]
    id_player2 = int(players_listing_id[int(player2) - 1].split("#")[0])
    name_player2 = players_listing[int(player2) - 1].split("(")[0]
    result_player1 = view.input_score_match(
        match_number, name_player1)
    result_player2 = view.input_score_match(match_number, name_player2)
    new_match = models.Match(
        id_player1, result_player1,
        id_player2, result_player2
    )
    return new_match


def add_match_with_update_player_rank_into_db(new_match):
    sql.add_match_into_db(new_match)
    sql.add_last_match_id_into_actual_round()
    # update rank
    id1, rank1, id2, rank2 = sql.extract_last_match_to_update_rank()
    sql.update_rank_player(id1, rank1)
    sql.update_rank_player(id2, rank2)


def generate_first_round():
    # extract list of players tournament by rank
    count_of_tournaments, tournament = sql.extract_last_tournament()
    players_listing, players_listing_id = rapport.reorder_players_by_rank(
        tournament
    )
    # view battle with players
    view.generate_round1(players_listing)

    # joueur 1 vs 5
    new_match = input_result_match(
        tournament, player1=1, player2=5, match_number=1)
    add_match_with_update_player_rank_into_db(new_match)

    # joueur 2 vs 6
    new_match = input_result_match(
        tournament, player1=2, player2=6, match_number=2)
    add_match_with_update_player_rank_into_db(new_match)

    # joueur 3 vs 7
    new_match = input_result_match(
        tournament, player1=3, player2=7, match_number=3)
    add_match_with_update_player_rank_into_db(new_match)
    # joueur 4 vs 8
    new_match = input_result_match(
        tournament, player1=4, player2=8, match_number=4)
    add_match_with_update_player_rank_into_db(new_match)
    # date finished round
    date, hours = control_datetime.create_datetime_now()
    sql.update_time_finished_round(date, hours)


def generate_other_round():
    pass


if __name__ == "__main__":
    pass
