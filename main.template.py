import sys
import math

from common.coordinates import Coordinates
from entity.map import Map
from entity.player import Player
from entity.tile import Tile
from game import Game

{placeholder}

map = Map(7, 7)
game = Game(map)
game.players.add(Player(0))
game.players.add(Player(1))

while True:
    turn_type = int(input())
    for i in range(7):
        for tile in input().split():
            pass

    for i in range(2):
        inputs = input().split()
        player = game.players.get_by_id(i)
        player.num_player_cards = int(inputs[0])  # the total number of quests for a player (hidden and revealed)
        player.coordinates = Coordinates(int(inputs[1]), int(inputs[2]))
        player.tile = Tile(inputs[3])

    num_items = int(input())  # the total number of items available on board and on player tiles
    for i in range(num_items):
        inputs = input().split()
        item_name = inputs[0]
        item_x = int(inputs[1])
        item_y = int(inputs[2])
        item_player_id = int(inputs[3])
    num_quests = int(input())  # the total number of revealed quests for both players
    for i in range(num_quests):
        inputs = input().split()
        quest_item_name = inputs[0]
        quest_player_id = int(inputs[1])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# PUSH <id> <direction> | MOVE <direction> | PASS
print("MOVE RIGHT")