import unittest
from bowling_game import Game, \
    OutOfScopeRoll, MoreThan10PinsRolledInAFrame, RolledAfter10thFrame, GameIsNotFinishedDueToNotEnoughRolls


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def roll_many(self, n, pins):
        for _ in range(n):
            self.g.roll(pins)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        self.g.roll(10)

    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(self.g.score(), 0)

    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(self.g.score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(17, 0)
        self.assertEqual(self.g.score(), 16)

    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.g.score(), 24)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(self.g.score(), 300)

    def test_roll_of_greater_than_10_raises_error(self):
        with self.assertRaises(OutOfScopeRoll):
            self.g.roll(11)

    def test_negative_roll_raises_error(self):
        with self.assertRaises(OutOfScopeRoll):
            self.g.roll(-1)

    def test_frame_rolls_in_sum_greater_than_10_raises_error(self):
        self.roll_strike()
        self.roll_many(2, 4)
        self.g.roll(1)
        with self.assertRaises(MoreThan10PinsRolledInAFrame):
            self.g.roll(10)

    def test_more_than_21_rolls_raises_error(self):
        self.roll_many(18, 0)
        self.roll_spare()
        self.g.roll(0)
        with self.assertRaises(RolledAfter10thFrame):
            self.g.roll(3)

    def test_a_roll_after_2_non_bonus_rolls_in_10th_frame_raises_error(self):
        self.roll_many(9, 10)
        self.roll_many(2, 1)
        with self.assertRaises(RolledAfter10thFrame):
            self.g.roll(8)

    def test_getting_score_with_11_strikes_raises_error(self):
        self.roll_many(11, 10)
        with self.assertRaises(GameIsNotFinishedDueToNotEnoughRolls):
            self.g.score()

    def test_getting_score_with_10_spares_and_missed_bonus_raises_error(self):
        for _ in range(10):
            self.roll_spare()
        with self.assertRaises(GameIsNotFinishedDueToNotEnoughRolls):
            self.g.score()

    def test_getting_score_with_19_ones_raises_error(self):
        self.roll_many(19, 1)
        with self.assertRaises(GameIsNotFinishedDueToNotEnoughRolls):
            self.g.score()

    def test_getting_score_with_4_ones_raises_error(self):
        self.roll_many(4, 1)
        with self.assertRaises(GameIsNotFinishedDueToNotEnoughRolls):
            self.g.score()


if __name__ == '__main__':
    unittest.main()
