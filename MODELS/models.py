from LANGUAGES import french as language
from API import constants

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class used by my classes (my entities)
Base = declarative_base()  # Required for SQLAlchemy


class Players(Base):
    __tablename__ = "T_Players"
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String)
    first_name = Column(String)
    birthday = Column(Date)
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
    id_player1 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_1 = relationship('Players', foreign_keys="Match.id_player1")
    result_player_1 = Column(Integer)
    id_player2 = Column(Integer, ForeignKey("T_Players.player_id"))
    player_2 = relationship('Players', foreign_keys="Match.id_player2")
    result_player_2 = Column(Integer)

    def __str__(self):
        return f"""{language.STR_MATCH_1} {self.id} {language.STR_MATCH_2} 
                {self.player_1.player_id} - {self.player1.last_name} {self.player1.first_name} 
                {language.STR_SCORE} {self.result_player_1} 
                VS
                {self.player_2.player_id} - - {self.player1.last_name} {self.player1.first_name} 
                {language.STR_SCORE} {self.result_player_2}
                """


class Rounds(Base):
    __tablename__ = "T_Rounds"
    round_id = Column(Integer, primary_key=True, autoincrement=True)
    match1_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match1_details = relationship("Match", foreign_keys="Rounds.match1_id")
    match2_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match2_details = relationship("Match", foreign_keys="Rounds.match2_id")
    match3_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match3_details = relationship("Match", foreign_keys="Rounds.match3_id")
    match4_id = Column(Integer, ForeignKey("T_Match.match_id"))
    match4_details = relationship("Match", foreign_keys="Rounds.match4_id")

    def __str__(self):
        return f"""{language.STR_ROUNDS_1} {self.id} {language.STR_ROUNDS_1}
                    Match1 id N°{self.match1_id} :
                        {self.match1_details.player_1.last_name} {self.match1_details.player_1.first_name}
                        {self.match1_details.result_player_1}
                        VS
                        {self.match1_details.player_2.last_name} {self.match1_details.player_2.first_name}
                        {self.match1_details.result_player_2}
                    Match2 id N°{self.match2_id} -
                    Match3 id N°{self.match3_id} -
                    Match4 id N°{self.match4_id} -
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
    date_started = Column(Date)
    date_finished = Column(Date)
    number_of_rounds = Column(Integer)
    time_controller = Column(String)
    description = Column(String)
    rounds1 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_1 = relationship("Rounds", foreign_keys="Tournament.rounds1")
    rounds2 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_2 = relationship("Rounds", foreign_keys="Tournament.rounds2")
    rounds3 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_3 = relationship("Rounds", foreign_keys="Tournament.rounds3")
    rounds4 = Column(Integer, ForeignKey("T_Rounds.round_id"))
    rounds_details_4 = relationship("Rounds", foreign_keys="Tournament.rounds4")


    def __init__(self, name, location, date, number_of_rounds, time_controller, description):
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.time_controller = time_controller
        self.description = description

    def add_rounds1(self,rounds1):
        self.rounds1 = rounds1

    def add_rounds2(self,rounds2):
        self.rounds2 = rounds2

    def add_rounds3(self,rounds3):
        self.rounds3 = rounds3

    def add_rounds4(self,rounds4):
        self.rounds4 = rounds4

    def __str__(self):
        return f"""
                \n{language.STR_TOURNAMENT_1} {self.tournament_id} :\n
                {language.STR_TOURNAMENT_2} {self.name}
                {language.STR_TOURNAMENT_3} {self.date} - {self.location}
                {language.STR_TOURNAMENT_4} {constants.NUMBER_OF_ROUNDS} 
                {language.STR_TOURNAMENT_5} {self.rounds_details_1}
                #verifier si details rounds 1
                {language.STR_TOURNAMENT_6} {self.time_controller}
                {language.STR_TOURNAMENT_7} {self.description}
                """


