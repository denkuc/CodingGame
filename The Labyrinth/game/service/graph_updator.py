from common.coordinates import Coordinates
from common.graph import Graph
from entity.dictionaries import Direction, VECTORS
from entity.move import Move
from game import Game


class GraphUpdator:
    def __init__(self, game: Game):
        self.game: Game = game

    def update_graph(self):
        graph = Graph()
        self.game.graph = graph
        for cell in self.game.cells:
            if cell.is_reachable():
                graph.add_vertex()
