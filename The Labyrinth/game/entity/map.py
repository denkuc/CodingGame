from common.coordinates import Coordinates


class Map:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def coordinates_are_possible(self, coordinates: Coordinates) -> bool:
        if 0 <= coordinates.x < self.width and 0 <= coordinates.y < self.height:
            return True

        return False

