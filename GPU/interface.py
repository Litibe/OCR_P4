from datetime import datetime

from API import api_class


def run_interface_summary():
    run = True
    while run:
        print("""\n Bienvenue sur le programme de gestion de tournoi du Club d'échec ! \n\t Au Sommaire : 
            1 => Créer un nouveau tournoi ♖
            2 => Ajouter un joueur dans la base de données.
            
            0 => Sortie du programme
        """)

        action = (input("Que souhaitez vous faire : "))
        try:
            action = int(action)
        except ValueError:
            print(f"\n !! Merci de saisir un choix valide")

        if action == 1:
            run_interface_tournoi()
            run = True
        elif action == 2:
            run_interface_add_player()
            run = True
        elif action == 3:
            run = True

        elif action == 0:
            run = False

        else:
            run = True

    print("Fin du programme")


def run_interface_tournoi():
    print("Vous avez sélectionné la création d'un nouveau Tournoi, merci de completer les champs requis : ")
    tournoi_name = str(input("\nNom du Tournoi : "))
    tournoi_location = str(input("\nLieu du Tournoi : "))
    tournoi_date = datetime.today()
    tournoi_date = tournoi_date.strftime("%A %d %B %Y à %H:%m")
    tournoi_tours = (input("\nNombre de tours, si vous voulez directement 4 tours , pressez la touche 'ENTRER' : "))
    if tournoi_tours == "":
        tournoi_tours = 4
    else:
        while not isinstance(tournoi_tours, int) or tournoi_tours < 0:
            tournoi_tours = (
                input("Nombre de tours, si vous voulez directement 4 tours , pressez la touche 'ENTRER' : "))
            try:
                tournoi_tours = int(tournoi_tours)
            except ValueError:
                print("Vous n'avez pas taper de caractère compatible, merci de saisir un chiffre svp !")
    tournoi_joueurs = []
    print("\nMerci de saisir les ID des 8 joueurs pour le tournoi : ")
    i = 1
    while i < 9:
        joueur = ""
        while not isinstance(joueur, int):
            try:
                joueur = int(input(f"ID joueur {i} : "))
                tournoi_joueurs.append(str(joueur))
            except ValueError:
                print("Vous n'avez pas taper de caractère compatible, merci de saisir un chiffre svp !")
        i += 1

    choice_time = ["Bullet", "Blitz", "Coup rapide"]
    print("\nVoici la liste des contrôleur du temps disponibles : ")
    i = 1
    for element in choice_time:
        print(f" \t Choix {i} pour {element}")
        i += 1
    tournoi_time = ""
    while tournoi_time not in choice_time:
        try:
            choix = int(input("Merci de faire votre choix :"))
            if choix == 1:
                tournoi_time = choice_time[choix - 1]
            elif choix == 2:
                tournoi_time = choice_time[choix - 1]
            elif choix == 3:
                tournoi_time = choice_time[choix - 1]
            else:
                pass
        except TypeError:
            print("\tMerci de faire un choix valable")
        except ValueError:
            print("\tMerci de faire un choix valable")

    tournoi_description = str(input("\nVous pouvez saisir une description de tournoi : "))

    tournoi_name = api_class.Tournoi(tournoi_name, tournoi_location,
                                     tournoi_date, tournoi_tours,
                                     tournoi_joueurs, tournoi_time, tournoi_description, rounds=[])
    print(repr(tournoi_name))


def run_interface_add_player():
    print("Vous avez sélectionné la création d'un nouveau Joueur dans la BDD, merci de completer les champs requis : ")
    player_name = str(input("Le NOM du Joueur :"))
    player_first_name = str(input("Le Prénom du joueur :"))
    player_birthday = str(input("Sa Date de naissance au format dd/mm/yyyy :"))
    player_sexe = str(input("Son Sexe M/F : "))

    player_name2 = api_class.Joueur(player_name, player_first_name, player_birthday,
                                    player_sexe, classification="none")
    print(player_name2)
