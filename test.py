"""
    Test module for fizzbuzz and tennis

"""

import unittest
from .fizzbuzz import fizzbuzz
from .tennis import inc_points, inc_game, inc_tie_break, inc_sets, Score

class FizzbuzzTest(unittest.TestCase):
    """
        Unittest implementation for fizzbuzz
    """
    def test_no_fizz_no_buzz(self):
        """
            Basic nominal tests
        """
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(98), 98)

    def test_fizz(self):
        """
            Fizz mod 3 tests
        """
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(99), "fizz")

    def test_buzz(self):
        """
            Buzz mod 5 tests
        """
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")

    def test_fizzbuzz(self):
        """
            Fizzbuzz mod 15 tests
        """
        self.assertEqual(fizzbuzz(15), "fizzbuzz")
        self.assertEqual(fizzbuzz(60), "fizzbuzz")

class TennisTest(unittest.TestCase):
    """
        Unittest implementation for Tennis
    """

    def game_loop(score, id_winner):
        """
            Example of the content of a game loop
        """
        is_match_over = False

        if score.games[-1] == (6, 6):
            score.tb_points, is_game_over = inc_tie_break(score.tb_points, id_winner)
        else:
            score.points, is_game_over = inc_points(score.points, id_winner)

        if is_game_over:
            score.tb_points = (0, 0) # TODO refactorate
            score.games[-1], set_is_over = inc_game(score.games[-1], id_winner)
            if set_is_over:
                score.sets, is_match_over = inc_sets(score.sets, id_winner)

        return is_match_over


    def test_inc_points_no_advantage(self):
        """
            Basic counting
        """
        self.assertEqual(inc_points([0, 0], 1), ((15, 0), False))
        self.assertEqual(inc_points([15, 0], 1), ((30, 0), False))
        self.assertEqual(inc_points([30, 30], 1), ((40, 30), False))
        self.assertEqual(inc_points([0, 30], 1), ((15, 30), False))

        self.assertEqual(inc_points([30, 15], 2), ((30, 30), False))
        self.assertEqual(inc_points([0, 30], 2), ((0, 40), False))

    def test_inc_points_advantages(self):
        """
            Advantages handling
        """
        self.assertEqual(inc_points([40, 40], 2), ((" ", "Ad."), False))
        self.assertEqual(inc_points([40, 40], 1), (("Ad.", " "), False))
        self.assertEqual(inc_points(["Ad.", " "], 2), ((40, 40), False))
        self.assertEqual(inc_points([" ", "Ad."], 1), ((40, 40), False))

    def test_inc_points_end_game(self):
        """
            End game conditions
        """
        self.assertEqual(inc_points([40, 30], 1), ((0, 0), True))
        self.assertEqual(inc_points([" ", "Ad."], 2), ((0, 0), True))

    def test_inc_game(self):
        """
            General case w/o tie break and set
        """
        self.assertEqual(inc_game([0, 0], 1), ((1, 0), False))
        self.assertEqual(inc_game([0, 0], 2), ((0, 1), False))
        self.assertEqual(inc_game([1, 0], 1), ((2, 0), False))
        self.assertEqual(inc_game([4, 4], 1), ((5, 4), False))
        self.assertEqual(inc_game([5, 5], 2), ((5, 6), False))

    def test_inc_game_end(self):
        """
            Game ends
        """
        self.assertEqual(inc_game([5, 4], 1), ((6, 4), True))
        self.assertEqual(inc_game([4, 5], 2), ((4, 6), True))
        self.assertEqual(inc_game([6, 5], 1), ((7, 5), True))

    def test_inc_game_tie_break(self):
        """
            Tie Break test
        """
        self.assertEqual(inc_game([6, 5], 2), ((6, 6), False))

        self.assertEqual(inc_tie_break([5, 0], 1), ((6, 0), False))
        self.assertEqual(inc_tie_break([6, 0], 1), ((7, 0), True))
        self.assertEqual(inc_tie_break([6, 6], 1), ((7, 6), False))
        self.assertEqual(inc_tie_break([7, 6], 1), ((8, 6), True))
        self.assertEqual(inc_tie_break([17, 16], 2), ((17, 17), False))

    def test_inc_sets(self):
        """
            Test increments sets
        """
        self.assertEqual(inc_sets((2, 2), 1), ((3, 2), True))
        self.assertEqual(inc_sets((0, 2), 2), ((0, 3), True))
        self.assertEqual(inc_sets((0, 0), 1), ((1, 0), False))

    def test_score_class(self):
        """
            Test score class
        """
        score = Score()
        self.assertEqual(inc_points(score.points, 1), ((15, 0), False))

        score = Score()
        score.points = (40, 0)
        self.assertEqual(inc_points(score.points, 1), ((0, 0), True))

    def test_end_game_no_tie_break(self):
        """
            End game with no Tie break
        """
        points = (40, 0)
        games = [(6, 0), (6, 0), (6, 5)]
        sets = (2, 0)
        tb_points = (0, 0)
        score = Score(points, games, tb_points, sets)

        self.assertEqual(TennisTest.game_loop(score, 1), True)

    def test_end_game_tie_break(self):
        """
            End game with Tie break test
        """
        score = Score()
        points = (40, 0)
        games = [(6, 0), (6, 0), (6, 6)]
        sets = (2, 0)
        tb_points = (6, 0)
        score = Score(points, games, tb_points, sets)

        self.assertEqual(TennisTest.game_loop(score, 1), True)

    def test_no_end_game(self):
        """
            No end game, increment setss
        """
        score = Score()
        points = (40, 0)
        games = [(6, 0), (0, 5)]
        sets = (1, 0)
        tb_points = (0, 0)
        score = Score(points, games, tb_points, sets)

        self.assertEqual(TennisTest.game_loop(score, 2), False)


if __name__ == "__main__":
    unittest.main()
