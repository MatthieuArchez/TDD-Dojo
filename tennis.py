"""
    Tennis module
"""
class Score:
    def __init__(self):
        self.games  = [[0, 0]]
        self.points = [0, 0]
        self.tb_points = [0, 0]
        self.sets   = [0, 0]


def is_set_ending(game_winner, game_loser):
    """
        Determine if a set is over or not
    """
    return True if ((game_winner == 6 and game_loser < 5) or (game_winner == 7 and game_loser in (5, 6))) else False

def inc_game(game_p1, game_p2, winner_id):
    """
        Tennis board computing games
        return the updated point score, and True if the set is over, False otherwise
    """
    game_winner, game_loser = ((game_p1 + 1), game_p2) if winner_id == 1 else ((game_p2 + 1), game_p1)
    set_end = is_set_ending(game_winner, game_loser)
    return (game_winner, game_loser, set_end) if winner_id == 1 else (game_loser, game_winner, set_end)

def inc_tie_break(tb_p1, tb_p2, winner_id):
    """
        Tennis tie break counter
    """
    tb_winner, tb_loser = ((tb_p1 + 1), tb_p2) if winner_id == 1 else ((tb_p2 + 1), tb_p1)
    tie_break_over = True if tb_winner >= 7 and tb_winner - tb_loser >= 2 else False
    return (tb_winner, tb_loser, tie_break_over) if winner_id == 1 else (tb_loser, tb_winner, tie_break_over)


def inc_points(pts_p1, pts_p2, winner_id):
    """
        Tennis board computing game points
        return the updated point score, and True if the point is over, False otherwise
    """
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

    return (pts_winner, pts_loser, game_end) if winner_id == 1 else (pts_loser, pts_winner, game_end)
