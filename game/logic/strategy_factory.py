from entity.player import Player
from entity.strategy.base_strategy import BaseStrategy
from entity.strategy.walk_strategy import WalkStrategy
from game import Game


class StrategyFactory:
    def __init__(self, game: Game):
        self.game = game
        self.walk_strategy = WalkStrategy()

    def get_strategy(self, player: Player) -> BaseStrategy:
        return self.walk_strategy