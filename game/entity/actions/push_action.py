from entity.actions.base_action import BaseAction
from entity.direction import Direction


class PushAction(BaseAction):
    def __init__(self, item_id: int, direction: Direction):
        self.__item_id = item_id
        self.__direction = direction

    def to_string(self) -> str:
        return 'PUSH {} {}'.format(self.__item_id, self.__direction.direction)
