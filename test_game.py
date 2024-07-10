from unittest import TestCase

from game import BaseballGame


class TestBaseballGame(TestCase):
    def setUp(self):
        self.game = BaseballGame()
        super().setUp()
    def test_exception_when_input_is_none(self):
        with self.assertRaises(Exception) as context:
            self.game.guess(None)

    def test_exception_when_input_is_unmatched(self):
        with self.assertRaises(Exception) as context:
            self.game.guess("12")
