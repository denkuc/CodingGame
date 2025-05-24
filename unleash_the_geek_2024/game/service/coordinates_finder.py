from common.coordinates import Coordinates
from entity.cell import CellCollection


class CoordinatesFinder:
    def coordinate_is_visible(self, target: Coordinates, coordinates: Coordinates, cells: 'CellCollection') -> bool:
        if not coordinates.same_line(target):
            return False

        if self.__no_obstacles(coordinates, target, cells):
            return True

        return False

    @staticmethod
    def __no_obstacles(coordinates: Coordinates, target: Coordinates, cells: 'CellCollection') -> bool:
        coordinates_between = coordinates.get_coordinates_between(target)
        for coordinate in coordinates_between:
            cell = cells.get_by_coordinates(coordinate)
            if cell and not cell.is_protein():
                return False

        return True
