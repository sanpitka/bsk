import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_something(self):
        f = Frame(5,2)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(0))

    def test_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

