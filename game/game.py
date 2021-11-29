from entity.map import Map


class Game:
    def __init__(self, map: Map):
        self.map = map

    @property
    def map(self) -> Map:
        return self.__map

    @map.setter
    def map(self, map: Map):
        self.__map = map
