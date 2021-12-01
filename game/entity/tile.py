from typing import Optional

from common.collection import MutableCollection
from common.coordinates import Coordinates
from entity.direction import DirectionCollection, Direction


class Tile:
    def __init__(self, tile_string: str, coordinates: Optional[Coordinates] = None):
        self.tile_string = tile_string
        self.coordinates = coordinates

    @property
    def coordinates(self) -> Optional[Coordinates]:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: Optional[Coordinates]):
        self.__coordinates = coordinates

    def get_possible_directions(self) -> DirectionCollection:
        possible_directions = DirectionCollection()

        for index, direction_allowed in enumerate(self.tile_string):
            if int(direction_allowed) == 1:
                possible_directions.add(Direction(index))

        return possible_directions


class TileCollection(MutableCollection):
    ...
