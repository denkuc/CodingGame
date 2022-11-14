import sys
import math

from common.coordinates import Coordinates
from entity.map import Map
from game import Game
from service.cell_builder import CellBuilder
from service.graph_updator import GraphUpdator
from service.log import Logger
from service.moves_definer import MovesDefiner
from service.moves_estimator import MovesEstimator

{placeholder}


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]


# game loop
game_map = Map(c, r)
game = Game(game_map)
moves_definer = MovesDefiner(game)
moves_estimator = MovesEstimator(game)
graph_updator = GraphUpdator(game)


while True:
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    kr, kc = [int(i) for i in input().split()]
    current_coordinates = Coordinates(kc, kr)

    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        for j, cell_type in enumerate(row):
            cell = CellBuilder.build_cell(j, i, cell_type)
            game.cells.update_or_create(cell)

    graph_updator.update_graph()
    current_cell = game.cells.get_by_coordinates(current_coordinates)
    if current_cell.is_control():
        game.time_is_running = True

    game.player = current_cell
    Logger.log(game.to_string())

    moves_definer.define_moves()
    moves_estimator.estimate_moves()
    selected_move = game.get_next_move()
    print(selected_move.direction.value)
