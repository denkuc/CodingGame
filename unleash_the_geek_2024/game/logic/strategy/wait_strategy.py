from entity.actions.wait_action import WaitAction
from entity.organism import Organism
from logic.strategy.base_strategy import BaseStrategy


class WaitStrategy(BaseStrategy):
    def execute(self, organism: Organism) -> WaitAction:
        return WaitAction()
