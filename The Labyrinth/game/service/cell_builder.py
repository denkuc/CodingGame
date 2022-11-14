from common.coordinates import Coordinates
from entity.cell import Cell
from entity.dictionaries import LocationType


class CellBuilder:
    @staticmethod
    def build_cell(x: int, y: int, cell_type: str) -> Cell:
        return Cell(Coordinates(x, y), LocationType(cell_type))
