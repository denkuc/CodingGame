from common.coordinates import Coordinates
from entity.dictionaries import Direction, VECTORS
from entity.move import Move
from game import Game


class MovesDefiner:
    def __init__(self, game: Game):
        self.game: Game = game

    def define_moves(self):
        self.game.moves.remove_all()
        for direction, vector in VECTORS.items():
            next_coordinates = self.game.player.coordinates + vector
            if self.game.map.coordinates_are_possible(next_coordinates):
                next_cell = self.game.cells.get_by_coordinates(next_coordinates)
                if next_cell.is_wall():
                    continue

                move = Move(direction, next_cell)
                self.game.moves.add(move)
