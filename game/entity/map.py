class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


class Dot(Map):
    ...
