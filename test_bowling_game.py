import unittest
from bowling_game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_can_roll(self):
        self.g.roll(0)

    def test_gutter_game(self):
        for i in range(20):
            self.g.roll(0)
        self.assertEqual(0, self.g.score())


if __name__ == '__main__':
    unittest.main()
