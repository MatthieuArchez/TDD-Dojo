import unittest
from fizzbuzz import fizzbuzz
from tennis import inc_points

class Fizzbuzz_Test(unittest.TestCase):
	def test_no_fizz_no_buzz(self):
		self.assertEqual(fizzbuzz(1), 1)
		self.assertEqual(fizzbuzz(2), 2)
		self.assertEqual(fizzbuzz(98), 98)

	def test_fizz(self):
		self.assertEqual(fizzbuzz(3), "fizz")
		self.assertEqual(fizzbuzz(99), "fizz")

	def test_buzz(self):
		self.assertEqual(fizzbuzz(5), "buzz")
		self.assertEqual(fizzbuzz(10), "buzz")

	def test_fizzbuzz(self):
		self.assertEqual(fizzbuzz(15), "fizzbuzz")
		self.assertEqual(fizzbuzz(60), "fizzbuzz")

class Tennis_Test(unittest.TestCase):
	def test_inc_points_no_advantage(self):
		self.assertEqual(inc_points(0, 0, 1), (15, 0))
		self.assertEqual(inc_points(15, 0, 1), (30, 0))
		self.assertEqual(inc_points(30, 30, 1), (40, 30))
		self.assertEqual(inc_points(0, 30, 1), (15, 30))

		self.assertEqual(inc_points(30, 15, 2), (30, 30))
		self.assertEqual(inc_points(0, 30, 2), (0, 40))

	def test_inc_points_advantages(self):
		self.assertEqual(inc_points(40, 40, 2), (" ", "Ad."))
		self.assertEqual(inc_points(40, 40, 1), ("Ad.", " "))
		self.assertEqual(inc_points("Ad.", " ", 2), (40, 40))
		self.assertEqual(inc_points(" ", "Ad.", 1), (40, 40))

	def test_inc_points_end_game(self):
		self.assertEqual(inc_points(40, 30, 1), (0, 0))
		self.assertEqual(inc_points(" ", "Ad.", 2), (0, 0))

if __name__ == "__main__":
	unittest.main()