#!/dlip_ref/s_dlip/Tools/LDT_LAB/linux64/python/python-3.6.3/bin/python
"""
    Test module for fizzbuzz and tennis

"""

import unittest
from fizzbuzz_module.fizzbuzz import fizzbuzz
from tennis_module.tennis import Score

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

    def test_inc_points_no_advantage(self):
        """
            Basic counting
        """
        score = Score()
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, [15, 0])

        score = Score([15, 0])
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, [30, 0])

        score = Score([30, 30])
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, [40, 30])

        score = Score([0, 30])
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, [15, 30])

        score = Score([30, 15])
        self.assertEqual(score.inc_points(2), False)
        self.assertEqual(score.points, [30, 30])

        score = Score([0, 30])
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, [15, 30])

        score = Score([0, 30])
        self.assertEqual(score.inc_points(2), False)
        self.assertEqual(score.points, [0, 40])

    def test_inc_points_advantages(self):
        """
            Advantages handling
        """
        score = Score([40, 40])
        self.assertEqual(score.inc_points(2), False)
        self.assertEqual(score.points, [" ", "Ad."])

        score = Score([40, 40])
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, ["Ad.", " "])

        score = Score(["Ad.", " "])
        self.assertEqual(score.inc_points(2), False)
        self.assertEqual(score.points, [40, 40])

        score = Score([" ", "Ad."])
        self.assertEqual(score.inc_points(1), False)
        self.assertEqual(score.points, [40, 40])

    def test_inc_points_end_game(self):
        """
            End game conditions
        """
        score = Score([40, 30])
        self.assertEqual(score.inc_points(1), True)
        self.assertEqual(score.points, [0, 0])

        score = Score([" ", "Ad."])
        self.assertEqual(score.inc_points(2), True)
        self.assertEqual(score.points, [0, 0])

    def test_inc_game(self):
        """
            General case w/o tie break and set
        """
        score = Score(games=[[0, 0]])
        self.assertEqual(score.inc_games(1), False)
        self.assertEqual(score.games, [[1, 0]])

        score = Score(games=[[0, 0]])
        self.assertEqual(score.inc_games(2), False)
        self.assertEqual(score.games, [[0, 1]])

        score = Score(games=[[6, 4], [1, 0]])
        self.assertEqual(score.inc_games(1), False)
        self.assertEqual(score.games, [[6, 4], [2, 0]])

        score = Score(games=[[4, 4]])
        self.assertEqual(score.inc_games(1), False)
        self.assertEqual(score.games, [[5, 4]])

        score = Score(games=[[6, 4], [5, 5]])
        self.assertEqual(score.inc_games(2), False)
        self.assertEqual(score.games, [[6, 4], [5, 6]])

    def test_inc_game_end(self):
        """
            Game ends
        """
        score = Score(games=[[5, 4]])
        self.assertEqual(score.inc_games(1), True)
        self.assertEqual(score.games, [[6, 4]])

        score = Score(games=[[4, 5]])
        self.assertEqual(score.inc_games(2), True)
        self.assertEqual(score.games, [[4, 6]])

        score = Score(games=[[6, 5]])
        self.assertEqual(score.inc_games(1), True)
        self.assertEqual(score.games, [[7, 5]])

    def test_inc_game_tie_break(self):
        """
            Tie Break test
        """
        score = Score(games=[[6, 5]])
        self.assertEqual(score.inc_games(2), False)
        self.assertEqual(score.games, [[6, 6]])

        score = Score(tb_points=[6, 6])
        self.assertEqual(score.inc_tie_break(2), False)
        self.assertEqual(score.tb_points, [6, 7])

        score = Score(tb_points=[6, 0])
        self.assertEqual(score.inc_tie_break(1), True)
        self.assertEqual(score.tb_points, [7, 0])

        score = Score(tb_points=[7, 6])
        self.assertEqual(score.inc_tie_break(1), True)
        self.assertEqual(score.tb_points, [8, 6])

        score = Score(tb_points=[16, 15])
        self.assertEqual(score.inc_tie_break(1), True)
        self.assertEqual(score.tb_points, [17, 15])

    def test_inc_sets(self):
        """
            Test increments sets
        """
        score = Score(sets=[2, 2])
        self.assertEqual(score.inc_sets(1), True)
        self.assertEqual(score.sets, [3, 2])

        score = Score(sets=[0, 2])
        self.assertEqual(score.inc_sets(2), True)
        self.assertEqual(score.sets, [0, 3])

        score = Score(sets=[0, 0])
        self.assertEqual(score.inc_sets(1), False)
        self.assertEqual(score.sets, [1, 0])


if __name__ == "__main__":
    unittest.main()
