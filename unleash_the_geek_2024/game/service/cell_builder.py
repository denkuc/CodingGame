from common.coordinates import Coordinates
from entity.cell import Cell
from service.cell_typer import CellTyper


class CellBuilder:
    @staticmethod
    def build_cell(x: int, y: int, _type: str) -> Cell:
        cell = Cell(Coordinates(x, y))
        cell.type = CellTyper.get_type(_type)

        return cell
