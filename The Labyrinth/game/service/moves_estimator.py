from common.coordinates import Coordinates
from entity.dictionaries import Direction
from entity.move import Move
from game import Game
from service.log import Logger


class MovesEstimator:
    def __init__(self, game: Game):
        self.game: Game = game

    def estimate_moves(self):
        for move in self.game.moves:
            if move.cell.is_start():
                self.__estimate_move_to_start(move)
            elif move.cell.is_control():
                self.__estimate_move_to_control(move)
            elif move.cell.is_empty():
                self.__estimate_move_to_empty(move)

    def __estimate_move_to_start(self, move: Move):
        if self.game.time_is_running:
            move.weight = 999999
        else:
            move.weight = -10000

    def __estimate_move_to_control(self, move: Move):
        if not self.game.time_is_running:
            move.weight = 999999
        else:
            move.weight = -10000

    def __estimate_move_to_empty(self, move: Move):
        if not self.game.time_is_running:
            if self.game.cells.control:
                move.weight = 10000/self.game.cells.control.coordinates.get_manhattan_distance(move.cell.coordinates)
            move.weight = 10*self.game.cells.count_unknown_around(move.cell.coordinates)
        else:
            move.weight = 10000/self.game.cells.start.coordinates.get_manhattan_distance(move.cell.coordinates)
