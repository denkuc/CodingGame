from entity.map import Map
from entity.player import PlayerCollection


class Game:
    def __init__(self, map: Map):
        self.map = map
        self.players = PlayerCollection()
        self.num_player_cards = None

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
    def num_player_cards(self) -> int:
        return self.__num_player_cards

    @num_player_cards.setter
    def num_player_cards(self, num_player_cards: int):
        self.__num_player_cards = num_player_cards
