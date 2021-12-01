from game import Game
from logic.strategy.base_strategy import BaseStrategy
from logic.strategy.move_strategy import MoveStrategy
from logic.strategy.push_strategy import PushStrategy


class StrategyFactory:
    def __init__(self, game: Game):
        self.game = game
        self.move_strategy = MoveStrategy()
        self.push_strategy = PushStrategy()

    def get_strategy(self) -> BaseStrategy:
        if self.game.turn_type == 0:
            return self.push_strategy

        return self.move_strategy
