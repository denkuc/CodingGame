from typing import Optional

from entity.coordinates import Coordinates
from entity.hero_type import HeroType


class MyHero(HeroType):
    def __init__(self):
        super().__init__()
        self.target: Optional[Coordinates] = None
