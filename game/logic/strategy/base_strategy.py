from abc import ABC, abstractmethod

from entity.actions.base_action import BaseAction
from entity.player import Player


class BaseStrategy(ABC):
    @abstractmethod
    def execute(self, player: Player) -> BaseAction:
        ...
