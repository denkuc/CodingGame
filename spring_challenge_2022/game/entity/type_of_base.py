from enum import Enum


class TypeOfBase(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

    def is_left(self) -> bool:
        return self.value == self.LEFT

    def is_right(self) -> bool:
        return self.value == self.RIGHT
