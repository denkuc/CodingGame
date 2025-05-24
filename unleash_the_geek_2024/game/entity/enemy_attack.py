from typing import Optional

from entity.dictionaries import ProteinType
from entity.organ import Organ


class EnemyAttack:
    def __init__(self, distance: int, my_organ: 'Organ', enemy_organ: 'Organ'):
        self.distance = distance
        self.my_organ = my_organ
        self.enemy_organ = enemy_organ

    def __str__(self):
        return f"EAttack(d={self.distance}, my_o={self.my_organ}, e_o={self.enemy_organ})"
