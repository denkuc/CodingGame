from common.collection import Collection, MutableCollection


class Move:
    DIRECTIONS = {
        0: 'TOP',
        1: 'RIGHT',
        2: 'BOTTOM',
        3: 'LEFT'
    }

    def __init__(self, direction_index: int):
        self.direction = self.DIRECTIONS[direction_index]

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class MoveCollection(MutableCollection):
    ...
