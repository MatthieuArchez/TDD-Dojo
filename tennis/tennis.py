#!/dlip_ref/s_dlip/Tools/LDT_LAB/linux64/python/python-3.6.3/bin/python
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
        self.tie_break = self._is_tie_break()

    @staticmethod
    def _get_index(winner_id):
        return (0, 1) if winner_id == 1 else (1, 0)

    def _is_tie_break(self):
        return True if self.games[-1] == [6, 6] else False

    def __str__(self):
        sp1, sp2 = self.sets
        score_str = "\nSETS : " + str(sp1) + " / " + str(sp2) + "\nGAMES : "
        for game in self.games:
            sp1, sp2 = game
            score_str += str(sp1) + "/" + str(sp2) + "  "

        if self.tie_break:
            sp1, sp2 = self.tb_points
            score_str += "\nTIE BREAK : " + str(sp1) + " / " + str(sp2) + "\n\n"
        else:
            sp1, sp2 = self.points
            score_str += "\n" + str(sp1) + " / " + str(sp2) + "\n\n"

        return score_str

    def inc_sets(self, winner_id):
        """
            Increments sets counter
            return updated sets score, True if Match is over, False otherwise
        """
        winner_index, _unused_loser_index = Score._get_index(winner_id)

        self.sets[winner_index] += 1

        return True if self.sets[winner_index] == NB_WINNING_SETS else False

    def inc_games(self, winner_id):
        """
            Tennis board computing games
            return the updated point score, and True if the set is over, False otherwise
        """
        winner_index, loser_index = Score._get_index(winner_id)

        self.games[-1][winner_index] += 1
        self.tie_break = Score._is_tie_break(self)

        return True if ((self.games[-1][winner_index] == 6 and\
                         self.games[-1][loser_index] < 5) or\
                        (self.games[-1][winner_index] == 7 and\
                         self.games[-1][loser_index] in (5, 6)))\
                    else False

    def inc_tie_break(self, winner_id):
        """
            Tennis tie break counter
        """
        winner_index, loser_index = Score._get_index(winner_id)

        self.tb_points[winner_index] += 1

        return True if self.tb_points[winner_index] >= 7 and\
                       self.tb_points[winner_index] - self.tb_points[loser_index] >= 2 else False


    def inc_points(self, winner_id):
        """
            Tennis board computing game points
            return the updated point score, and True if the point is over, False otherwise
        """
        game_end = False

        if self.tie_break:
            game_end = self.inc_tie_break(winner_id)
        else:
            winner_index, loser_index = Score._get_index(winner_id)

            if self.points[winner_index] == 0:
                self.points[winner_index] = 15
            elif self.points[winner_index] == 15:
                self.points[winner_index] = 30
            elif self.points[winner_index] == 30:
                self.points[winner_index] = 40
            elif self.points[winner_index] == 40:
                if self.points[loser_index] == 40:
                    self.points[winner_index] = "Ad."
                    self.points[loser_index] = " "
                else:
                    game_end = True
                    self.points[winner_index] = 0
                    self.points[loser_index] = 0
            elif self.points[winner_index] == "Ad.":
                game_end = True
                self.points[winner_index] = 0
                self.points[loser_index] = 0
            else:
                self.points[winner_index] = 40
                self.points[loser_index] = 40

        return game_end

def game_loop(score=Score()):
    """
        Example of game loop using the score class
    """
    def get_winner_id():
        """
            Getting winner_id from user input
        """
        winner_id = ""
        print("Who win ? (1/2)")

        while winner_id not in ("1", "2"):
            winner_id = input()

        return int(winner_id)

    match_over = False

    while not match_over:
        print(score)

        winner_id = get_winner_id()

        if score.inc_points(winner_id):
            if score.inc_games(winner_id):
                if score.inc_sets(winner_id):
                    match_over = True
