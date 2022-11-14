from typing import Optional, Iterator

from common.collection import MutableCollection
from common.coordinates import Coordinates
from common.stringify_interface import StringifyInterface
from entity.dictionaries import LocationType


class Cell:
    def __init__(self, coordinates: Coordinates, type_: LocationType):
        self.coordinates: Coordinates = coordinates
        self.type: LocationType = type_
        self.neighbors = CellCollection()

    def is_reachable(self) -> bool:
        return self.is_empty() or self.is_control() or self.is_start()

    def is_wall(self) -> bool:
        return self.type == LocationType.WALL

    def is_empty(self) -> bool:
        return self.type == LocationType.EMPTY

    def is_control(self) -> bool:
        return self.type == LocationType.CONTROL_ROOM

    def is_start(self) -> bool:
        return self.type == LocationType.START

    def is_unknown(self) -> bool:
        return self.type == LocationType.UNKNOWN


class CellCollection(MutableCollection, StringifyInterface):
    __CELLS_AROUND = range(-2, 3)

    def __init__(self, elements: Optional[list] = None):
        super().__init__(elements)
        self.start: Optional[Cell] = None
        self.control: Optional[Cell] = None

    def update_or_create(self, cell: Cell):
        existing_cell = self.get_by_coordinates(cell.coordinates)
        if not existing_cell:
            if cell.is_start():
                self.start = cell

            if cell.is_control():
                self.control = cell

            self.add(cell)
            return

        if cell.is_control():
            self.control = cell
        existing_cell.type = cell.type

    def add(self, element_to_add: Cell):
        super().add(element_to_add)

    def get_by_coordinates(self, coordinates: Coordinates) -> Optional[Cell]:
        for cell in self:
            if cell.coordinates == coordinates:
                return cell

        return None

    def to_string(self):
        return f'Start_cell: {self.start}, control_cell: {self.control}'

    def count_unknown_around(self, coordinates: Coordinates) -> int:
        unknown_count = 0
        for delta_x in self.__CELLS_AROUND:
            for delta_y in self.__CELLS_AROUND:
                delta_coordinates = Coordinates(delta_x, delta_y)
                cell_around = self.get_by_coordinates(coordinates + delta_coordinates)
                if cell_around and cell_around.is_unknown():
                    unknown_count += 1

        return unknown_count

    def __iter__(self) -> Iterator[Cell]:
        return super().__iter__()
