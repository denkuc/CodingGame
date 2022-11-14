from typing import Optional

from common.graph import Graph
from common.stringify_interface import StringifyInterface
from entity.cell import Cell, CellCollection
from entity.move import MoveCollection, Move
from entity.map import Map


class Game(StringifyInterface):
    def __init__(self, game_map: Map):
        self.map: Map = game_map
        self.moves: MoveCollection = MoveCollection()
        self.cells: CellCollection = CellCollection()
        self.graph: Graph = Graph()
        self.player: Optional[Cell] = None
        self.time_is_running: bool = False
        self.path = MoveCollection()

    def get_next_move(self) -> Move:
        if not self.path.is_empty():
            next_move = self.path.first()
            self.path.remove(next_move)

            return next_move

        return self.moves.get_best_move()

    def to_string(self) -> str:
        return f"""Player:{self.player.coordinates.to_string()},time_is_running:{self.time_is_running},{self.cells.to_string()}"""
