from enum import Enum
from typing import Optional

from entity.coordinates import Coordinates
from entity.entity import Entity
from entity.threat_for import ThreadFor


class Monster(Entity):
    def __init__(self):
        super().__init__()
        self.health: int = 0
        self.vx: int = 0
        self.vy: int = 0
        self.near_base: bool = False
        self.threat_for: Optional[ThreadFor] = None
