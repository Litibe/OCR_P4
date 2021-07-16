from sqlalchemy.orm import sessionmaker

import constants
from controllers import base, players,tournaments
from LANGUAGES import french as language
from models import models
import views.base
views_rapports = views.base.Rapports()

control_player = players.ControllersPlayers()
control_tournament = tournaments.ControllersTournament()
listing_p_for_t = control_tournament.players_per_t()
i = 1
print(listing_p_for_t)
for p_for_t in listing_p_for_t:
    print(p_for_t)
    p_l, p_l_id = control_player.reorder_players_by_rank(
        p_for_t
    )
    views_rapports.listing_players_tournaments(
        i, p_l,
        language.RAPPORT_TOURNAMENT_LIST_BY_RANK)
    i += 1
