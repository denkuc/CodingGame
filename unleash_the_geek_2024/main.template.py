import random
from abc import ABC, abstractmethod
from enum import Enum
from math import sqrt, acos
from typing import Optional, Iterator, List, Dict


{placeholder}

# width: columns in the game grid
# height: rows in the game grid
width, height = [int(i) for i in input().split()]
map = Map(width, height)
game = Game(map)
player_action_dispatcher = PlayerActionDispatcher(game)

game.my_player = Player(1)
game.enemy_player = Player(0)


# game loop
while True:
    entity_count = int(input())
    for i in range(entity_count):
        inputs = input().split()
        x = int(inputs[0])
        y = int(inputs[1])  # grid coordinate
        cell = CellBuilder.build_cell(x, y)
        game.cells.add(cell)
        _type = inputs[2]  # WALL, ROOT, BASIC, TENTACLE, HARVESTER, SPORER, A, B, C, D
        cell.type = CellTyper.get_type(_type)

        owner = int(inputs[3])  # 1 if your organ, 0 if enemy organ, -1 if neither
        organ_id = int(inputs[4])  # id of this entity if it's an organ, 0 otherwise
        if organ_id != 0:
            organ_dir = inputs[5]  # N,E,S,W or X if not an organ
            organ_parent_id = int(inputs[6])
            organ_root_id = int(inputs[7])
            parent_organ = game.organs.get_by_id(organ_parent_id)
            root_organ = game.organs.get_by_id(organ_root_id)
            organ = OrganBuilder.build_organ(organ_id, _type, cell, parent_organ, root_organ, organ_dir)

            game.organs.add(organ)
            if owner == 1:
                game.my_player.organs.add(organ)
            elif owner == 0:
                game.enemy_player.organs.add(organ)

    # my_d: your protein stock
    my_proteins = [int(i) for i in input().split()]
    game.my_player.add_proteins(my_proteins)

    # opp_d: opponent's protein stock
    opponent_proteins = [int(i) for i in input().split()]
    game.enemy_player.add_proteins(opponent_proteins)

    required_actions_count = int(input())  # your number of organisms, output an action for each one in any order

    actions = player_action_dispatcher.get_actions(required_actions_count)
    for action in actions:
        print(action.to_string())
