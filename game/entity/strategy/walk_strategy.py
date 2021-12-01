from entity.actions.move_action import MoveAction
from entity.player import Player
from entity.strategy.base_strategy import BaseStrategy
from main import BaseAction


class WalkStrategy(BaseStrategy):
    def execute(self, player: Player) -> BaseAction:
        action = MoveAction(player.tile.get_possible_directions().first())

        return action
