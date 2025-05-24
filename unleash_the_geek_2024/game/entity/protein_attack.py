from typing import Optional

from entity.dictionaries import ProteinType
from entity.free_protein import FreeProtein
from entity.organ import Organ


class ProteinAttack:
    def __init__(self, distance: int, my_organ: 'Organ', protein: 'FreeProtein'):
        self.distance = distance
        self.my_organ = my_organ
        self.protein = protein

    def __str__(self):
        return f"PAttack(d={self.distance}, my_o={self.my_organ}, p={self.protein})"
