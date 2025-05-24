from typing import Optional

from common.coordinates import Coordinates
from entity.actions.base_action import BaseAction
from entity.dictionaries import OrganType, OrganDirection
from entity.organ import Organ


class SporeAction(BaseAction):
    def __init__(self, sporer_organ: 'Organ', coordinates: Coordinates):
        self.__sporer_organ = sporer_organ
        self.__coordinates = coordinates

    def to_string(self) -> str:
        return f'SPORE {self.__sporer_organ.id} {self.__coordinates.to_string()}'
