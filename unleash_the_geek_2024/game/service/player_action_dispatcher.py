import sys

from entity.actions.base_action import ActionCollection, BaseAction
from game import Game
from logic.strategy_factory import StrategyFactory


class PlayerActionDispatcher:
    def __init__(self, game: Game):
        self.game = game
        self.__strategy_factory = StrategyFactory(game)

    def get_actions(self) -> 'ActionCollection':
        actions = ActionCollection()

        print(f"ORs: {self.game.my_player.organisms.count()}", file=sys.stderr, flush=True)
        for organism in self.game.my_player.organisms:
            actions.add(self.get_action_for_organism(organism))

        return actions

    def get_action_for_organism(self, organism) -> BaseAction:
        selected_strategy = self.__strategy_factory.get_strategy(organism)
        action = selected_strategy.execute(organism)
        if action:
            print(f'Executing strategy: {str(selected_strategy)}', file=sys.stderr, flush=True)
            return action

        selected_strategy = self.__strategy_factory.grow_strategy

        print(f'Executing strategy: {str(selected_strategy)}', file=sys.stderr, flush=True)
        return selected_strategy.execute(organism)
