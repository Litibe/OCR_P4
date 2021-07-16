from sqlalchemy.orm import sessionmaker

import constants
from controllers import base, players,tournaments
from LANGUAGES import french as language
from models import models
import views.base

control = tournaments.ControllersTournament()

control.generate_other_round()