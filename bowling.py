from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self._frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) == 10:
            raise BowlingError("Bowling game already has 10 frames")
        self._frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self._frames):
            raise BowlingError
        return self._frames[i]

    def calculate_score(self) -> int:
        score = 0
        spare_flag = False
        strike_flag = False
        for frame in self._frames:
            if spare_flag:
                score += frame.get_first_throw()
                spare_flag = False
            if strike_flag:
                score += frame.get_first_throw()
                score += frame.get_second_throw()
                strike_flag = False
            if frame.is_spare():
                spare_flag = True
            if frame.is_strike():
                strike_flag = True
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
