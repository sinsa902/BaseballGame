class BaseballGame:
    def guess(self, guessNumber):
        if not guessNumber:
            raise TypeError()

        if len(guessNumber) !=3:
            raise TypeError()
