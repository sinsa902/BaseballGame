from unittest import TestCase

from game import BaseballGame


class TestBaseballGame(TestCase):
    def test_exception_when_input_is_none(self):
        self.game = BaseballGame()
        with self.assertRaises(Exception) as context:
            self.game.guess(None)
