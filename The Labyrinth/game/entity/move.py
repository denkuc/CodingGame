from typing import Iterator

from common.collection import MutableCollection
from entity.cell import Cell
from entity.dictionaries import Direction


class Move:
    def __init__(self, direction: Direction, cell: Cell):
        self.direction: Direction = direction
        self.cell: Cell = cell
        self.weight: int = 0


class MoveCollection(MutableCollection):
    def first(self) -> Move:
        return super().first()

    def __iter__(self) -> Iterator[Move]:
        return super().__iter__()

    def get_best_move(self) -> Move:
        max_weight = -99999
        move_with_max_weight = None
        for move in self:
            if move.weight > max_weight:
                max_weight = move.weight
                move_with_max_weight = move

        return move_with_max_weight
