import random, sys
from abc import ABC, abstractmethod
from enum import Enum
from math import sqrt, acos
from typing import Optional, Iterator, List, Dict, Tuple


class StringifyInterface(ABC):
    @abstractmethod
    def to_string(self) -> str:
        ...


class Collection(ABC):
    FIRST_ELEMENT_INDEX = 0
    LAST_ELEMENT_INDEX = -1

    @abstractmethod
    def __init__(self, elements):
        self.__elements = elements

    def is_empty(self) -> bool:
        return self.count() == 0

    def count(self) -> int:
        return len(self.__elements)

    def __len__(self) -> int:
        return self.count()

    def first(self):
        return (self.__elements or [None])[self.FIRST_ELEMENT_INDEX]

    def last(self):
        return (self.__elements or [None])[self.LAST_ELEMENT_INDEX]

    def get_as_tuple(self) -> tuple:
        if isinstance(self.__elements, tuple) is False:
            return tuple(self.__elements)
        else:
            return self.__elements

    def get_as_list(self) -> list:
        if isinstance(self.__elements, list) is False:
            return list(self.__elements)
        else:
            return self.__elements

    def __iter__(self):
        return iter(self.__elements)

    def __next__(self):
        element = next(self.__elements) or None
        if element is None:
            raise StopIteration

        return element

    def get_with_limit(self, limit: int) -> list:
        elements_as_list = self.get_as_list()
        if limit > len(elements_as_list):
            return elements_as_list

        return self.__elements[:limit]


class MutableCollection(Collection):
    def __init__(self, elements: Optional[list] = None):
        if elements is None:
            elements = []
        super().__init__(elements)

    def add(self, element_to_add):
        self.get_as_list().append(element_to_add)

    def extend(self, collection_to_extend):
        raise Exception('This method is not allowed for collections. Please use merge() instead!')

    def copy(self):
        return self.get_as_list().copy()

    def pop(self):
        return self.get_as_list().pop()

    def merge(self, collection: Collection):
        self.get_as_list().extend(collection.get_as_list())

    def remove(self, element_to_remove):
        self.get_as_list().remove(element_to_remove)

    def remove_all(self):
        self.get_as_list().clear()

    def _insert_at_index(self, element_to_insert, index: int):
        elements = self.get_as_list()
        elements.insert(index, element_to_insert)
        self.__init__(elements)

{placeholder}

# width: columns in the game grid
# height: rows in the game grid
width, height = [int(i) for i in input().split()]
_map = Map(width, height)
game = Game(_map)
player_action_dispatcher = PlayerActionDispatcher(game)

game.my_player = Player(1)
game.enemy_player = Player(0)


# game loop
while True:
    game.free_proteins.remove_all()
    game.my_player.organs.remove_all()
    game.my_player.organisms.remove_all()
    game.enemy_player.organs.remove_all()
    game.enemy_player.organisms.remove_all()
    entity_count = int(input())
    for i in range(entity_count):
        inputs = input().split()
        x = int(inputs[0])
        y = int(inputs[1])  # grid coordinate
        _type = inputs[2]  # WALL, ROOT, BASIC, TENTACLE, HARVESTER, SPORER, A, B, C, D
        cell = CellBuilder.build_cell(x, y, _type)
        game.cells.add(cell)

        if cell.is_protein():
            free_protein = FreeProteinBuilder.build_free_protein(_type, cell)
            cell.value = _type
            game.free_proteins.add(free_protein)

        owner = int(inputs[3])  # 1 if your organ, 0 if enemy organ, -1 if neither
        organ_id = int(inputs[4])  # id of this entity if it's an organ, 0 otherwise
        if organ_id != 0:
            organ_dir = inputs[5]  # N,E,S,W or X if not an organ
            organ_parent_id = int(inputs[6])
            organ_root_id = int(inputs[7])
            cell.value = organ_id
            organ = OrganBuilder.build_organ(organ_id, _type, cell, organ_parent_id, organ_root_id, organ_dir)

            game.organs.add(organ)
            organ_root = game.organs.get_by_id(organ_root_id)
            if owner == 1:
                game.my_player.organs.add(organ)
                organism = game.my_player.organisms.get_or_create(organ_root)
                organism.organs.add(organ)
            elif owner == 0:
                game.enemy_player.organs.add(organ)
                organism = game.enemy_player.organisms.get_or_create(organ_root)
                organism.organs.add(organ)

    # my_d: your protein stock
    my_protein_resources = [int(i) for i in input().split()]
    game.my_player.add_proteins(my_protein_resources)

    # opp_d: opponent's protein stock
    opponent_protein_resources = [int(i) for i in input().split()]
    game.enemy_player.add_proteins(opponent_protein_resources)

    print(f'FPs: {game.free_proteins}', file=sys.stderr, flush=True)
    game.free_proteins.define_if_harvested_by_me(game)
    print(f'FPs: {game.free_proteins}', file=sys.stderr, flush=True)

    # game.map.redraw_map(game.cells)

    required_actions_count = int(input())  # your number of organisms, output an action for each one in any order

    actions = player_action_dispatcher.get_actions()
    for action in actions:
        print(action.to_string())
