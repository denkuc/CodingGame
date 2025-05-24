from typing import Optional

from common.coordinates import Coordinates, CoordinatesCollection
from entity.cell import CellCollection


class NeighborsFinder:
    def __init__(self, game):
        self.game = game

    def get_emtpy_neighbor(self, coordinates: Coordinates) -> Optional[Coordinates]:
        return self.get_empty_neighbors(coordinates).first()

    def get_empty_neighbors(self, coordinates: 'Coordinates') -> 'CoordinatesCollection':
        empty_neighbors = CoordinatesCollection()
        for neighbor in coordinates.neighbors():
            if not self.__is_within_map(neighbor):
                continue

            neighbor_cell = self.game.cells.get_by_coordinates(neighbor)
            if not neighbor_cell or neighbor_cell.is_protein():
                empty_neighbors.add(neighbor)

        return empty_neighbors

    def __is_within_map(self, coordinates: 'Coordinates') -> bool:
        return 0 <= coordinates.x < self.game.map.width and 0 <= coordinates.y < self.game.map.height
