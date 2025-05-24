import sys

from entity.organism import Organism
from game import Game
from logic.strategy.base_strategy import BaseStrategy
from logic.strategy.grow_strategy import GrowStrategy
from logic.strategy.spore_strategy import SporeStrategy
from logic.strategy.wait_strategy import WaitStrategy


class StrategyFactory:
    def __init__(self, game: Game):
        self.game = game
        self.grow_strategy = GrowStrategy(game)
        self.wait_strategy = WaitStrategy(game)
        self.spore_strategy = SporeStrategy(game)

    def get_strategy(self, organism: 'Organism') -> BaseStrategy:
        if self.__no_action_possible(organism):
            return self.wait_strategy
        elif self.__can_spore(organism):
            return self.spore_strategy
        else:
            return self.grow_strategy

    @staticmethod
    def __can_spore(organism: 'Organism') -> bool:
        if organism.organs.get_sporers().is_empty():
            return False

        return True

    def __no_action_possible(self, organism: 'Organism') -> bool:
        actionable_organs = organism.organs.get_actionable_organs(self.game)
        if actionable_organs.is_empty():
            return True

        return False
