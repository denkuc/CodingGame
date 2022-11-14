from enum import Enum


class ThreadFor(Enum):
    NO_ONE = 'NO_ONE'
    ME = 'ME'
    OPPONENT = 'OPPONENT'

    def me(self):
        return self.value == self.ME

    def no_one(self):
        return self.value == self.NO_ONE

    def opponent(self):
        return self.value == self.OPPONENT
