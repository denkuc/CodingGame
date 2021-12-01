from entity.actions.base_action import ActionCollection, BaseAction
from entity.player import Player
from game import Game
from logic.strategy_factory import StrategyFactory


class PlayerActionDispatcher:
    def __init__(self, game: Game):
        self.game = game
        self.__strategy_factory = StrategyFactory()

    def get_actions(self) -> ActionCollection:
        actions = ActionCollection()
        for player in self.game.players.get_my_players():
            actions.add(self.get_action_for_player(player))

        return actions

    def get_action_for_player(self, player: Player) -> BaseAction:
        return self.__strategy_factory.get_strategy(player).execute(player)
