from common.coordinates import Coordinates
from entity.cell import Cell
from entity.dictionaries import OrganDirection


class DirectionDefiner:
    @staticmethod
    def define_direction(coordinates: Coordinates, target: Coordinates) -> 'OrganDirection':
        if coordinates.x < target.x:
            return OrganDirection.EAST
        if coordinates.x > target.x:
            return OrganDirection.WEST
        if coordinates.y < target.y:
            return OrganDirection.SOUTH
        if coordinates.y > target.y:
            return OrganDirection.NORTH

        return OrganDirection.NONE
