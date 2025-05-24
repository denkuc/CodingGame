from entity.cell import Cell
from entity.dictionaries import ProteinType
from entity.free_protein import FreeProtein


class FreeProteinBuilder:
    @staticmethod
    def build_free_protein(_type: str, cell: Cell) -> FreeProtein:
        free_protein = FreeProtein()
        free_protein.type = ProteinType(_type)
        free_protein.cell = cell

        return free_protein
