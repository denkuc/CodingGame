import math


class Coordinates:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

    def get_distance(self, other: 'Coordinates'):
        return math.hypot(self.x-other.x, self.y-other.y)
