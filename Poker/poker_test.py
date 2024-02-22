import poker_functions
import unittest


class TestPoker(unittest.TestCase):
    def test_royal_flush(self):
        drawn_cards = [8, 9, 10, 11, 12]
        combination = poker_functions.check_combinations(drawn_cards)
        self.assertEqual(combination, "royal_flush")

    def test_straight_flush(self):
        drawn_cards = [1, 2, 3, 4, 5]
        combination = poker_functions.check_combinations(drawn_cards)
        self.assertEqual(combination, "straight_flush")

    def test_4_of_kind(self):
        drawn_cards = [0, 13, 26, 39, 40]
        combination = poker_functions.check_combinations(drawn_cards)
        self.assertEqual(combination, "4_of_kind")


if __name__ == "main":
    unittest.main()
