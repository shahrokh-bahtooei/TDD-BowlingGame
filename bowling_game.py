
class Game(object):

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        score = 0
        i = 0
        for frame in range(10):
            if self._rolls[i] + self._rolls[i + 1] == 10:  # spare
                score += 10 + self._rolls[i + 2]
                i += 2
            else:
                score += self._rolls[i] + self._rolls[i + 1]
                i += 2
        return score
