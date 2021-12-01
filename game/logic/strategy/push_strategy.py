from main import BaseAction

from entity.actions.push_action import PushAction
from entity.direction import Direction
from entity.player import Player
from logic.strategy.base_strategy import BaseStrategy


class PushStrategy(BaseStrategy):
    def execute(self, player: Player) -> BaseAction:
        action = PushAction(0, Direction(1))

        return action
