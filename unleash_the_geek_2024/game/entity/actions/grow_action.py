from typing import Optional

from common.coordinates import Coordinates
from entity.actions.base_action import BaseAction
from entity.dictionaries import OrganType, OrganDirection
from entity.organ import Organ


class GrowAction(BaseAction):
    def __init__(self, parent_organ: 'Organ', coordinates: Coordinates,
                 organ_type: 'OrganType', direction: Optional['OrganDirection'] = None):
        self.__parent_organ = parent_organ
        self.__coordinates = coordinates
        self.__type = organ_type
        self.__direction = direction

    def to_string(self) -> str:
        return f'GROW {self.__parent_organ.id} {self.__coordinates.to_string()} {self.__type.value}' + (
            f' {self.__direction.value}' if self.__direction else ''
        )


class BasicGrowAction(GrowAction):
    def __init__(self, parent_organ: 'Organ', coordinates: Coordinates):
        super().__init__(parent_organ, coordinates, OrganType.BASIC)


class TentacleGrowAction(GrowAction):
    def __init__(self, parent_organ: 'Organ', coordinates: Coordinates, direction: 'OrganDirection'):
        super().__init__(parent_organ, coordinates, OrganType.TENTACLE, direction)


class HarvesterGrowAction(GrowAction):
    def __init__(self, parent_organ: 'Organ', coordinates: Coordinates, direction: 'OrganDirection'):
        super().__init__(parent_organ, coordinates, OrganType.HARVESTER, direction)


class SporerGrowAction(GrowAction):
    def __init__(self, parent_organ: 'Organ', coordinates: Coordinates, direction: 'OrganDirection'):
        super().__init__(parent_organ, coordinates, OrganType.SPORER, direction)
