from LANGUAGES import french as language
from API import controller

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class used by my classes (my entities)
Base = declarative_base()  # Required for SQLAlchemy


# Definition of the Contact class
class Players(Base):
    __tablename__ = "T_Players"
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
        return f"{language.STR_PLAYER_1}{self.player_id} - {self.last_name} " \
               f"{self.first_name} - {self.birthday} - {self.sex}"


class Match(Base):
    __tablename__ = "T_Match"
    match_id = Column(Integer, primary_key=True, autoincrement=True)
    player1 = Column(Integer, ForeignKey("T_Players.player_id"))
    result_player1 = Column(Integer)
    player2 = Column(Integer, ForeignKey("T_Players.player_id"))
    result_player2 = Column(Integer)

    def __str__(self):
        return f"""Il s'agit du match id n° {self.id} avec le score 
                {self.player1} - {self.result_player1} 
                &
                {self.player2} - {self.result_player2}
                """


class Rounds(Base):
    __tablename__ = "T_Rounds"
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    match1 = Column(Integer, ForeignKey("T_Match.match_id"))
    match2 = Column(Integer, ForeignKey("T_Match.match_id"))
    match3 = Column(Integer, ForeignKey("T_Match.match_id"))
    match4 = Column(Integer, ForeignKey("T_Match.match_id"))

    def __str__(self):
        return f"""Il s'agit du Tour id n° {self.id} avec les match ID N°
                    {self.match1} - {self.match2} - {self.match3} - {self.match4}
                """


class PlayersForTournament(Base) :
    __tablename__ = "T_PlayersForTournament"
    id_players_for_tournament = Column(Integer, primary_key=True, autoincrement=True)
    id_player1 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_1 = relationship('Players', foreign_keys="PlayersForTournament.id_player1")
    id_player2 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_2 = relationship('Players', foreign_keys="PlayersForTournament.id_player2")
    id_player3 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_3 = relationship('Players', foreign_keys="PlayersForTournament.id_player3")
    id_player4 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_4 = relationship('Players', foreign_keys="PlayersForTournament.id_player4")
    id_player5 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_5 = relationship('Players', foreign_keys="PlayersForTournament.id_player5")
    id_player6 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_6 = relationship('Players', foreign_keys="PlayersForTournament.id_player6")
    id_player7 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_7 = relationship('Players', foreign_keys="PlayersForTournament.id_player7")
    id_player8 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_8 = relationship('Players', foreign_keys="PlayersForTournament.id_player8")

    def __init__(self, id1, id2, id3, id4, id5, id6, id7, id8):
        self.id_player1 = id1
        self.id_player2 = id2
        self.id_player3 = id3
        self.id_player4 = id4
        self.id_player5 = id5
        self.id_player6 = id6
        self.id_player7 = id7
        self.id_player8 = id8

    def __str__(self):
        return f"""
                Voici les ID de joueurs présents lors du Tournoi 
                {self.id_player1} - {self.player_1.last_name} - {self.player_1.first_name}
                {self.id_player2} - {self.player_2.last_name} - {self.player_2.first_name}
                {self.id_player3} - {self.player_3.last_name} - {self.player_3.first_name}
                {self.id_player4} - {self.player_4.last_name} - {self.player_4.first_name}
                {self.id_player5} - {self.player_5.last_name} - {self.player_5.first_name}
                {self.id_player6} - {self.player_6.last_name} - {self.player_6.first_name}
                {self.id_player7} - {self.player_7.last_name} - {self.player_7.first_name}
                {self.id_player8} - {self.player_8.last_name} - {self.player_8.first_name}
                """


class Tournament(Base):
    __tablename__ = "T_Tournament"
    tournament_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    date = Column(String)
    number_of_rounds = Column(Integer)
    time_controller = Column(String)
    description = Column(String)
    rounds = Column(Integer, ForeignKey("T_Rounds.round_id"))

    def __init__(self, name, location, date, number_of_rounds, time_controller, description, rounds):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.time_controller = time_controller
        self.description = description
        self.id_rounds = rounds

    def __str__(self):
        return f"""
                \n{language.STR_TOURNAMENT_1} {self.tournament_id} :\n
                {language.STR_TOURNAMENT_2} {self.name}
                {language.STR_TOURNAMENT_3} {self.date} - {self.location}
                {language.STR_TOURNAMENT_4} {controller.NUMBER_OF_ROUNDS} {language.STR_TOURNAMENT_5} {self.rounds}
                {language.STR_TOURNAMENT_6} {self.time_controller}
                {language.STR_TOURNAMENT_7} {self.description}
                """


