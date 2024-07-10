from unittest import TestCase

from game import BaseballGame


class TestBaseballGame(TestCase):
    def setUp(self):
        self.game = BaseballGame()
        super().setUp()

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except Exception as exception:
            pass

    def test_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
