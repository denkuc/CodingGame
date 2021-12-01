from entity.map import Map
from entity.player import PlayerCollection


class Game:
    def __init__(self, map: Map):
        self.map = map
        self.players = PlayerCollection()
        self.turn_type = None

    @property
    def map(self) -> Map:
        return self.__map

    @map.setter
    def map(self, map: Map):
        self.__map = map

    @property
    def players(self) -> PlayerCollection:
        return self.__players

    @players.setter
    def players(self, players: PlayerCollection):
        self.__players = players

    @property
    def turn_type(self) -> int:
        return self.__turn_type

    @turn_type.setter
    def turn_type(self, turn_type: int):
        self.__turn_type = turn_type


