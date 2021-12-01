from common.coordinates import Coordinates


class Player:
    def __init__(self, coordinates: Coordinates, tile: Tile):
        self.coordinates = coordinates
        self.tile = tile

    @property
    def coordinates(self) -> Coordinates:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: Coordinates):
        self.__coordinates = coordinates

    @property
    def tile(self) -> Tile:
        return self.__tile

    @tile.setter
    def tile(self, tile: Tile):
        self.__tile = tile
