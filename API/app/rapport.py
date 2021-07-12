
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
