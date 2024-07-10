class BaseballGame:
    def guess(self, guessNumber):
        if not guessNumber:
            raise TypeError()