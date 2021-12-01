from entity.actions.move_action import MoveAction
from entity.player import Player
from logic.strategy.base_strategy import BaseStrategy
from main import BaseAction


class MoveStrategy(BaseStrategy):
    """
        1. Get player current position (1, 1)
        2. Get player quest current position (5, 1)
        3. Get shortest way to quest (CoordinateCollection)
        4. Get next coordinates
        5. Transform coordinates to Direction
    """
    def execute(self, player: Player) -> BaseAction:
        action = MoveAction(player.tile.get_possible_directions().first())

        return action
