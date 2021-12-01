from entity.actions.base_action import ActionCollection
from game import Game


class PlayerActionDispatcher:
    def __init__(self, game: Game):
        self.game = game

    def get_actions(self) -> ActionCollection:
        actions = ActionCollection()

        return actions