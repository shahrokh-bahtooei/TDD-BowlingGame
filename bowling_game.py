
class Game(object):

    def __init__(self):
        self._rolls = []

    def roll(self, pins: int):
        self._raise_error_if_invalid_roll(pins)
        self._rolls.append(pins)

    def score(self) -> int:
        frame_score = 0
        first_in_frame = 0

        for frame in range(1, 11):
            frame_score += self._try_computing_frame_rolls_score(first_in_frame, frame)
            first_in_frame += self._get_steps_count_to_next_frame(first_in_frame)

        return frame_score

    def _raise_error_if_invalid_roll(self, pins):
        self._raise_error_if_out_of_scope_roll(pins)
        self._raise_error_if_more_than_10_pins_rolled_in_this_frame(pins)
        self._raise_error_if_rolled_more_than_21_times()
        self._raise_error_if_rolled_after_2_non_bonus_rolls_in_10th_frame()

    @staticmethod
    def _raise_error_if_out_of_scope_roll(pins):
        if pins > 10 or pins < 0:
            raise OutOfScopeRoll

    def _raise_error_if_more_than_10_pins_rolled_in_this_frame(self, pins):
        if self._is_2nd_roll_in_frame():
            if self._more_than_10_pins_are_rolled_in_this_frame(pins):
                raise MoreThan10PinsRolledInAFrame

    def _is_2nd_roll_in_frame(self):
        return (len(self._rolls) - self._count_strikes()) % 2 == 1

    def _count_strikes(self):
        strikes_count = 0
        for roll in self._rolls:
            if roll == 10:
                strikes_count += 1
        return strikes_count

    def _more_than_10_pins_are_rolled_in_this_frame(self, pins):
        return self._rolls[-1] + pins > 10

    def _raise_error_if_rolled_more_than_21_times(self):
        if self._rolled_more_than_21_times():
            raise RolledAfter10thFrame

    def _rolled_more_than_21_times(self):
        return len(self._rolls) > 20

    def _raise_error_if_rolled_after_2_non_bonus_rolls_in_10th_frame(self):
        if self._is_3rd_roll_of_10th_frame():
            has_bonus_for_strike = self._is_strike(len(self._rolls) - 2)
            has_bonus_for_spare = self._is_spare(len(self._rolls) - 2)
            if not has_bonus_for_spare and not has_bonus_for_strike:
                raise RolledAfter10thFrame

    def _is_3rd_roll_of_10th_frame(self):
        first_in_frame = 0
        frame = 1

        while frame < 10 and first_in_frame + 2 < len(self._rolls):

            if self._is_strike(first_in_frame):
                first_in_frame += 1
                frame += 1
            else:
                first_in_frame += 2
                frame += 1

        return frame == 10 and first_in_frame + 2 == len(self._rolls)

    def _is_strike(self, first_in_frame):
        return self._rolls[first_in_frame] == 10

    def _is_spare(self, first_in_frame):
        return self._rolls[first_in_frame] + self._rolls[first_in_frame + 1] == 10

    def _try_computing_frame_rolls_score(self, first_in_frame, frame):
        try:
            return self._compute_frame_rolls_score(first_in_frame)
        except IndexError:
            msg = write_up_to_which_frame_score_is_computable(frame - 1)
            raise GameIsNotFinishedDueToNotEnoughRolls(msg) from None

    def _compute_frame_rolls_score(self, first_in_frame):
        if self._is_strike(first_in_frame):
            rolls_score = 10 + self._next_two_balls_for_strike(first_in_frame)

        elif self._is_spare(first_in_frame):
            rolls_score = 10 + self._next_ball_for_spare(first_in_frame)

        else:
            rolls_score = self._two_balls_in_frame(first_in_frame)

        return rolls_score

    def _next_two_balls_for_strike(self, first_in_frame):
        return self._rolls[first_in_frame + 1] + self._rolls[first_in_frame + 2]

    def _next_ball_for_spare(self, first_in_frame):
        return self._rolls[first_in_frame + 2]

    def _two_balls_in_frame(self, first_in_frame):
        return self._rolls[first_in_frame] + self._rolls[first_in_frame + 1]

    def _get_steps_count_to_next_frame(self, steps):
        if self._is_strike(steps):
            steps = 1
        else:
            steps = 2

        return steps


class OutOfScopeRoll(RuntimeError):
    pass


class MoreThan10PinsRolledInAFrame(RuntimeError):
    pass


class RolledAfter10thFrame(RuntimeError):
    pass


def write_up_to_which_frame_score_is_computable(frame):
    return f'Score is computable just up to frame {frame}!'


class GameIsNotFinishedDueToNotEnoughRolls(RuntimeError):
    pass
