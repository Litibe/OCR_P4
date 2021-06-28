from datetime import datetime

from API import models, controller
from LANGUAGUES import french as languague


def input_what_do_you_want():
    action = (input(languague.WHAT_DO_YOU_WANT))
    return action


def run_interface_tournoi():
    print("Vous avez sélectionné la création d'un nouveau Tournoi, merci de completer les champs requis : ")
    tournament_name = str(input("\nNom du Tournoi : "))
    tournament_location = str(input("\nLieu du Tournoi : "))
    tournament_date = datetime.today()
    tournament_date = tournament_date.strftime("%A %d %B %Y à %H:%m")
    tournament_id_players = []
    print("\nMerci de saisir les ID des 8 joueurs pour le tournoi : ")
    i = 1
    while i < 9:
        player = ""
        while not isinstance(player, int):
            try:
                player = int(input(f"ID player {i} : "))
                tournament_id_players.append(str(player))
            except ValueError:
                print("Vous n'avez pas taper de caractère compatible, merci de saisir un chiffre svp !")
        i += 1

    choice_time = ["Bullet", "Blitz", "Coup rapide"]
    print("\nVoici la liste des contrôleur du temps disponibles : ")
    i = 1
    for element in choice_time:
        print(f" \t Choix {i} pour {element}")
        i += 1
    tournament_time_controller = ""
    while tournament_time_controller not in choice_time:
        try:
            choix = int(input("Merci de faire votre choix :"))
            if choix == 1:
                tournament_time_controller = choice_time[choix - 1]
            elif choix == 2:
                tournament_time_controller = choice_time[choix - 1]
            elif choix == 3:
                tournament_time_controller = choice_time[choix - 1]
            else:
                pass
        except TypeError:
            print("\tMerci de faire un choix valable")
        except ValueError:
            print("\tMerci de faire un choix valable")

    tournoi_description = str(input("\nVous pouvez saisir une description de tournoi : "))

    tournament = models.Tournament(tournament_name, tournament_location,
                                   tournament_date, controller.NUMBER_OF_ROUNDS,
                                   tournament_id_players, tournament_time_controller, tournoi_description,
                                   rounds=[])
    print(tournament)


def main_menu():
    print(languague.SUMMARY_MAIN_MENU)


def main_menu_rapport():
    print(languague.SUMMARY_MENU_RAPPORT)


def menu_add_player():
    print(languague.INFORM_CREATE_PLAYER)
    player_name = str(input(languague.LAST_NAME_PLAYER))
    player_first_name = str(input(languague.FIRST_NAME_PLAYER))
    player_birthday = str(input(languague.BIRTHDAY_PLAYER))
    player_sexe = str(input(languague.SEX_PLAYER))
    return player_name, player_first_name, player_birthday, player_sexe


def listing_rapport(languague_rapport, listing):
    print(languague_rapport)
    for element in listing:
        print(element)
    print("----------------------------------------------------------------------------")
