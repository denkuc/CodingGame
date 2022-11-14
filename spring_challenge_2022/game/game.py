from typing import List

from entity.entity import Monster
from entity.map import Map
from entity.player import Player


class Game:
    def __init__(self, _map: Map):
        self.map: Map = _map
        self.monsters: List[Monster] = []
        self.me: Player = Player()
        self.opponent: Player = Player()
