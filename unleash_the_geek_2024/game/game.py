from typing import Optional

from entity.cell import CellCollection
from entity.free_protein import FreeProteinCollection
from entity.map import Map
from entity.organ import OrganCollection
from entity.player import Player
from service.coordinates_finder import CoordinatesFinder
from service.neighbors_finder import NeighborsFinder
from service.protein_prioritizer import ProteinPrioritizer


class Game:
    def __init__(self, _map: Map):
        self.map: Map = _map
        self.my_player: Optional[Player] = None
        self.enemy_player: Optional[Player] = None
        self.cells: CellCollection = CellCollection()
        self.organs: OrganCollection = OrganCollection()
        self.free_proteins = FreeProteinCollection()
        self.turn_type = None
        self.coordinates_finder = CoordinatesFinder()
        self.neighbors_finder = NeighborsFinder(self)
        self.protein_prioritizer = ProteinPrioritizer(self)
