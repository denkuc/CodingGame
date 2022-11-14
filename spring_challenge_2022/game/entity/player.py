from typing import List

from entity.bases import Bases
from entity.coordinates import Coordinates
from entity.hero_type import HeroType


class Player:
    def __init__(self):
        self.heroes: List[HeroType] = []
        self.base: Bases = Bases()
        self.health: int = 0
        self.mana: int = 0
        self.towers: List[Coordinates] = []
