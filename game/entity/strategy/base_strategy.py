from abc import ABC, abstractmethod

from entity.player import Player
from main import BaseAction


class BaseStrategy(ABC):
    @abstractmethod
    def execute(self, player: Player) -> BaseAction:
        ...