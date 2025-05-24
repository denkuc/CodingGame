from abc import ABC, abstractmethod

from entity.actions.base_action import BaseAction
from entity.organism import Organism
from game import Game


class BaseStrategy(ABC):
    def __init__(self, game: Game):
        self.game: Game = game

    @abstractmethod
    def execute(self, organism: Organism) -> BaseAction:
        ...
