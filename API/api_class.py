class Tournoi:
    def __init__(self, name, location, date, tours, joueurs, time, description, rounds):
        self.name = name
        self.location = location
        self.date = date
        self.tours = tours
        self.joueurs = joueurs
        self.time = time
        self.description = description
        self.rounds = rounds

    def __repr__(self):
        rep = "\nVoici les détails du tournoi : \n"
        rep += "\tNom du tournoi : " + self.name + "\n"
        rep += "\tDate et Lieu du tournoi : " + self.date + " à " + self.location
        rep += " réalisé en " + str(self.tours) + " tours dont les Id de Rounds sont " + str(self.rounds)
        rep += " \n\t Les ID de joueurs présents pour le tournoi" + (" - ".join(self.joueurs))
        rep += " selon le contrôle de temps " + self.time
        rep += " \n\tDescription du tournoi : " + self.description
        return rep


class Joueur:
    def __init__(self, name, first_name, birthday, sexe, classification):
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.classification = classification

    def __repr__(self):
        rep = "Il s'agit de " + self.first_name +" " + self.name + " né(e) le " + self.birthday + " de sexe "
        rep += self.sexe + " et qui a le classement " + self.classification
        return rep
