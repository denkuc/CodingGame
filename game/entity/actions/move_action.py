from entity.actions.base_action import BaseAction
from entity.direction import DirectionCollection


class MoveAction(BaseAction):
    def __init__(self, directions: DirectionCollection):
        self.__directions = directions

    def to_string(self) -> str:
        directions = ' '.join([direction.direction for direction in self.__directions])
        return 'MOVE {}'.format(directions)
