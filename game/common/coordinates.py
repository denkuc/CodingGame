from math import sqrt
from typing import Optional, Iterator

from common.collection import MutableCollection
from common.stringify_interface import StringifyInterface


class Coordinates(StringifyInterface):
    __LEFT_PIXEL = 0
    __TOP_PIXEL = 0

    def __init__(self, x: Optional[int] = None, y: Optional[int] = None):
        self.x = x
        if self.x is None:
            self.x = self.__LEFT_PIXEL

        self.y = y
        if self.y is None:
            self.y = self.__TOP_PIXEL

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    def get_distance(self, coordinates: 'Coordinates') -> int:
        return int(self.get_distance_float(coordinates))

    def get_distance_float(self, coordinates: 'Coordinates') -> float:
        x = (pow(coordinates.x - self.x, 2))
        y = (pow(coordinates.y - self.y, 2))

        return sqrt(x + y)

    def is_same(self, coordinates: 'Coordinates') -> bool:
        if self.to_string() == coordinates.to_string():
            return True

        return False

    def is_near(self, coordinates: 'Coordinates') -> bool:
        x_distance = abs(self.x - coordinates.x)
        y_distance = abs(self.y - coordinates.y)

        if (x_distance + y_distance) <= 1:
            return True

        return False

    def get_mirrored_coordinate(self, mirroring_coordinate: 'Coordinates') -> 'Coordinates':
        diff_x = mirroring_coordinate.x - self.x
        diff_y = mirroring_coordinate.y - self.y

        mirrored_x = mirroring_coordinate.x + diff_x
        mirrored_y = mirroring_coordinate.y + diff_y

        return Coordinates(mirrored_x, mirrored_y)

    def get_relative_to_coordinate(self, point: 'Coordinates') -> 'Coordinates':
        return Coordinates(self.x - point.x, self.y - point.y)

    def get_distance_to_vector_line(self, vector) -> int:
        circle_radius = self.get_distance_to_vector_line_from_zero_point(
            vector.get_relative_to_coordinate(self)
        )

        return round(circle_radius)

    @staticmethod
    def get_distance_to_vector_line_from_zero_point(vector) -> float:
        x_1 = vector.start.x
        x_2 = vector.end.x
        y_1 = vector.start.y
        y_2 = vector.end.y

        circle_radius = abs((x_2 - x_1) * y_1 + (y_1 - y_2) * x_1) / sqrt(pow(x_2 - x_1, 2) + pow(y_2 - y_1, 2))

        return circle_radius

    def to_string(self) -> str:
        return '{} {}'.format(self.x, self.y)

    def from_string(self, string: str) -> 'Coordinates':
        coordinates_pair = string.split(' ')
        return Coordinates(int(coordinates_pair[0]), int(coordinates_pair[1]))


class CoordinatesCollection(MutableCollection):
    def add(self, element_to_add: Coordinates):
        super().add(element_to_add)

    def first(self) -> Optional[Coordinates]:
        return super().first()

    def last(self) -> Optional[Coordinates]:
        return super().last()

    def __iter__(self) -> Iterator[Coordinates]:
        return super().__iter__()

    def has_coordinates(self, coordinates: Coordinates) -> bool:
        for existing_coordinates in self:
            if coordinates.is_same(existing_coordinates):
                return True

        return False

    def get_last_items(self, items_number: int) -> 'CoordinatesCollection':

        last_entities = self.get_as_list()
        if items_number < self.count():
            last_entities = last_entities[-items_number:0]

        last_items = CoordinatesCollection(last_entities)

        return last_items

    def sort_by_distance(self) -> 'CoordinatesCollection':
        ...
