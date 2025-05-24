from entity.actions.base_action import BaseAction
from entity.cell import Cell
from entity.dictionaries import OrganType
from entity.organ import Organ


class WaitAction(BaseAction):
    def to_string(self) -> str:
        return 'WAIT'
