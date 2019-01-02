
class Game(object):

    def __init__(self):
        self._rolls = [0] * 21
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def score(self):
        score = 0
        first_in_frame = 0
        for frame in range(10):
            if self._rolls[first_in_frame] == 10:  # strike
                score += 10 + self._rolls[first_in_frame + 1] + self._rolls[first_in_frame + 2]
                first_in_frame += 1
            elif self._is_spare(first_in_frame):
                score += 10 + self._rolls[first_in_frame + 2]
                first_in_frame += 2
            else:
                score += self._rolls[first_in_frame] + self._rolls[first_in_frame + 1]
                first_in_frame += 2
        return score

    def _is_spare(self, first_in_frame):
        return self._rolls[first_in_frame] + self._rolls[first_in_frame + 1] == 10
