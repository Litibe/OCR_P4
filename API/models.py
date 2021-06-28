from LANGUAGUES import french as languague

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Base class used by my classes (my entities)
Base = declarative_base()  # Required for SQLAlchemy


# Definition of the Contact class
class Players(Base):
    __tablename__ = "Players"
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String)
    first_name = Column(String)
    birthday = Column(String)
    sex = Column(String)
    rank = Column(Integer)

    def __init__(self, last_name, first_name, birthday, sex, rank=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return f"{languague.STR_PLAYER_1}{self.player_id} - {self.last_name} " \
               f"{self.first_name} - {self.birthday} - {self.sex}"


class Match(Base):
    __tablename__ = "Match"
    match_id = Column(Integer, primary_key=True, autoincrement=True)
    player1 = Column(Integer, ForeignKey("Players.player_id"))
    result_player1 = Column(Integer)
    player2 = Column(Integer, ForeignKey("Players.player_id"))
    result_player2 = Column(Integer)

    def __str__(self):
        return f"""Il s'agit du match id n° {self.id} avec le score 
                {self.player1} - {self.result_player1} 
                &
                {self.player2} - {self.result_player2}
                """


class Rounds(Base):
    __tablename__ = "Rounds"
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    match1 = Column(Integer, ForeignKey("Match.match_id"))
    match2 = Column(Integer, ForeignKey("Match.match_id"))
    match3 = Column(Integer, ForeignKey("Match.match_id"))
    match4 = Column(Integer, ForeignKey("Match.match_id"))

    def __str__(self):
        return f"""Il s'agit du Tour id n° {self.id} avec les match ID N°
                    {self.match1} - {self.match2} - {self.match3} - {self.match4}
                """


class Tournament(Base):
    __tablename__ = "Tournament"
    tournament_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    date = Column(String)
    number_of_rounds = Column(Integer)
    players = Column(Integer, ForeignKey("Players.player_id"))
    time_controller = Column(String)
    description = Column(String)
    rounds = Column(Integer, ForeignKey("Rounds.round_id"))

    def __init__(self, name, location, date, number_of_rounds, players, time_controller, description, rounds):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.players = players
        self.time_controller = time_controller
        self.description = description
        self.id_rounds = rounds

    def __str__(self):
        return f"""
                \nVoici les détails du tournoi : \n
                Nom du tournoi : {self.name}
                Date et Lieu du tournoi : le {self.date} à {self.location}
                réalisé en {self.tours} tours dont les Id de Rounds sont {self.rounds}
                Les ID de joueurs présents pour le tournoi : {(" - ".join(self.joueurs))}
                selon le contrôle de temps {self.time}
                Description du tournoi : {self.description}
                """


