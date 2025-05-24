from typing import Optional

from entity.dictionaries import ProteinType


class BaseProtein:
    def __init__(self):
        self.type: Optional[ProteinType] = None
