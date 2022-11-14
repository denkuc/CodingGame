from typing import Optional

from entity.coordinates import Coordinates
from entity.type_of_base import TypeOfBase


class Bases:
    def __init__(self):
        self.point: Coordinates = Coordinates()
        self.type: Optional[TypeOfBase] = None
