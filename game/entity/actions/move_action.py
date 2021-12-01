from entity.actions.base_action import BaseAction
from entity.direction import Direction


class MoveAction(BaseAction):
    def __init__(self, direction: Direction):
        self.__direction = direction