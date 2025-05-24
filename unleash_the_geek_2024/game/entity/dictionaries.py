from enum import Enum

from common.coordinates import Coordinates


class CellType(Enum):
    ORGAN = 'O'
    PROTEIN = 'P'
    WALL = 'W'
    EMPTY = '.'


class OrganType(Enum):
    """ROOT, BASIC, TENTACLE, HARVESTER, SPORER"""
    ROOT = 'ROOT'
    BASIC = 'BASIC'
    TENTACLE = 'TENTACLE'
    HARVESTER = 'HARVESTER'
    SPORER = 'SPORER'


class ProteinType(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'


class OrganDirection(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    NONE = 'X'


VECTORS = {
    OrganDirection.NORTH: Coordinates(0, -1),
    OrganDirection.EAST: Coordinates(1, 0),
    OrganDirection.SOUTH: Coordinates(0, 1),
    OrganDirection.WEST: Coordinates(-1, 0)
}