from typing import Optional

from common.coordinates import Coordinates
from entity.cell import Cell
from entity.dictionaries import OrganType, OrganDirection
from entity.organ import Organ


class OrganBuilder:
    @staticmethod
    def build_organ(_id: int, _type: str, cell: Cell, parent_id: int, root_id: int, organ_dir: str) -> Organ:
        organ = Organ()
        organ.id = _id
        organ.type = OrganType(_type)
        organ.cell = cell
        organ.parent_id = parent_id
        organ.root_id = root_id
        organ.direction = OrganDirection(organ_dir)

        return organ
