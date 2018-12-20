"""
    Tennis module
"""
NB_WINNING_SETS = 3

class Score:
    """
        Data representation for tennis score
    """
    def __init__(self, points=[0, 0], games=[[0, 0]], tb_points=[0, 0], sets=[0, 0]):
        self.games = games
        self.points = points
        self.tb_points = tb_points
        self.sets = sets


def inc_sets(sets_score, winner_id):
    """
        Increments sets counter
        return updated sets score, True if Match is over, False otherwise
    """
    sets_p1, sets_p2 = sets_score[0], sets_score[1]
    sets_winner, sets_loser = ((sets_p1 + 1), sets_p2) if winner_id == 1 else\
                              ((sets_p2 + 1), sets_p1)

    is_match_over = True if sets_winner == NB_WINNING_SETS else False

    return ((sets_winner, sets_loser), is_match_over) if winner_id == 1 else\
           ((sets_loser, sets_winner), is_match_over)


def inc_game(game_score, winner_id):
    """
        Tennis board computing games
        return the updated point score, and True if the set is over, False otherwise
    """
    game_p1, game_p2 = game_score[0], game_score[1]
    game_winner, game_loser = ((game_p1 + 1), game_p2) if winner_id == 1 else\
                              ((game_p2 + 1), game_p1)

    is_set_over = True if ((game_winner == 6 and game_loser < 5) or\
        (game_winner == 7 and game_loser in (5, 6))) else False

    return ((game_winner, game_loser), is_set_over) if winner_id == 1 else\
           ((game_loser, game_winner), is_set_over)

def inc_tie_break(tb_score, winner_id):
    """
        Tennis tie break counter
    """
    tb_p1, tb_p2 = tb_score[0], tb_score[1]
    tb_winner, tb_loser = ((tb_p1 + 1), tb_p2) if winner_id == 1 else\
                          ((tb_p2 + 1), tb_p1)

    tie_break_over = True if tb_winner >= 7 and tb_winner - tb_loser >= 2 else False

    return ((tb_winner, tb_loser), tie_break_over) if winner_id == 1 else\
           ((tb_loser, tb_winner), tie_break_over)


def inc_points(pts_score, winner_id):
    """
        Tennis board computing game points
        return the updated point score, and True if the point is over, False otherwise
    """
    pts_p1, pts_p2 = pts_score[0], pts_score[1]
    pts_winner, pts_loser = (pts_p1, pts_p2) if winner_id == 1 else (pts_p2, pts_p1)

    game_end = False

    if pts_winner == 0:
        pts_winner = 15
    elif pts_winner == 15:
        pts_winner = 30
    elif pts_winner == 30:
        pts_winner = 40
    elif pts_winner == 40:
        if pts_loser == 40:
            pts_winner = "Ad."
            pts_loser = " "
        else:
            game_end = True
            pts_winner = 0
            pts_loser = 0
    elif pts_winner == "Ad.":
        game_end = True
        pts_winner = 0
        pts_loser = 0
    else:
        pts_winner = 40
        pts_loser = 40

    return ((pts_winner, pts_loser), game_end) if winner_id == 1 else\
           ((pts_loser, pts_winner), game_end)
