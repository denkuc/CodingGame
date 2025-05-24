from typing import Optional, Iterator

from common.coordinates import Coordinates
from entity.dictionaries import CellType
from unleash_the_geek_2024.template import MutableCollection


class Cell:
    def __init__(self, coordinates: Coordinates):
        self.coordinates: Coordinates = coordinates
        self.type: Optional[CellType] = None
        self.value: Optional[str] = None
        self.distance_to_target: Optional[int] = 0
        self.region: int = 0

    def is_wall(self) -> bool:
        return self.type == CellType.WALL

    def is_organ(self) -> bool:
        return self.type == CellType.ORGAN

    def is_protein(self) -> bool:
        return self.type == CellType.PROTEIN


class CellCollection(MutableCollection):
    def __init__(self, elements: Optional[list] = None):
        super().__init__(elements)
        self.__map = {}

    def add(self, element_to_add: Cell):
        self.__map.setdefault(element_to_add.coordinates.x, {})[element_to_add.coordinates.y] = element_to_add
        super().add(element_to_add)

    def get_by_coordinates(self, coordinates: Coordinates) -> Optional[Cell]:
        return self.__map.get(coordinates.x, {}).get(coordinates.y, None)

    def __iter__(self) -> Iterator[Cell]:
        return super().__iter__()
