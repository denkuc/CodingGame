from common.coordinates import Coordinates
from entity.cell import Cell
from entity.dictionaries import CellType


class CellTyper:
    """
    WALL
    Organs: ROOT, BASIC, TENTACLE, HARVESTER, SPORER,
    Proteins: A, B, C, D
    """
    @staticmethod
    def get_type(_type: str) -> CellType:
        if _type == 'WALL':
            return CellType.WALL
        if _type == 'ROOT' or _type == 'BASIC' or _type == 'TENTACLE' or _type == 'HARVESTER' or _type == 'SPORER':
            return CellType.ORGAN
        if _type == 'A' or _type == 'B' or _type == 'C' or _type == 'D':
            return CellType.PROTEIN

        return CellType.EMPTY
