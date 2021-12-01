from typing import Optional

from common.collection import MutableCollection
from common.coordinates import Coordinates


class Item:
    def __init__(self, item_id: int, name: str):
        self.id = item_id
        self.name = name
        self.coordinates = None

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, item_id: int):
        self.__id = item_id

    @property
    def name(self) -> Optional[str]:
        return self.__name

    @name.setter
    def name(self, name: Optional[str]):
        self.__name = name

    @property
    def coordinates(self) -> Optional[Coordinates]:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates: Optional[Coordinates]):
        self.__coordinates = coordinates


class ItemCollection(MutableCollection):
    def get_or_create_by_id(self, item_id: int, name: str) -> Optional[Item]:
        for item in self:
            if item.id == item_id:
                return item
        new_item = Item(item_id, name)
        self.add(new_item)

        return new_item
