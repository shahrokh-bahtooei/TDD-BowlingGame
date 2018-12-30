import unittest
from bowling_game import Game


class TestGame(unittest.TestCase):

    def test_can_create_game(self):
        g = Game()


if __name__ == '__main__':
    unittest.main()
