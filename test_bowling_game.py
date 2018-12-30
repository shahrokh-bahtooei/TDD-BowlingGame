import unittest
from bowling_game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_can_roll(self):
        self.g.roll(0)


if __name__ == '__main__':
    unittest.main()
