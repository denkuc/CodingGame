from typing import Optional

from common.collection import MutableCollection
from common.coordinates import Coordinates


class Player:
    def __init__(self, player_id: int):
        self.id = player_id
        self.num_player_cards = None
        self.coordinates = None
        self.tile = None

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def num_player_cards(self) -> int:
        return self.__num_player_cards

    @num_player_cards.setter
    def num_player_cards(self, num_player_cards: int):
        self.__num_player_cards = num_player_cards

    @property
    def coordinates(self) -> Coordinates:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: Coordinates):
        self.__coordinates = coordinates

    @property
    def tile(self) -> Tile:
        return self.__tile

    @tile.setter
    def tile(self, tile: Tile):
        self.__tile = tile


class PlayerCollection(MutableCollection):
    def get_by_id(self, player_id: int) -> Optional[Player]:
        for player in self:
            if player.id == player_id:
                return player

        return None
