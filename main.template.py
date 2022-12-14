import sys
import math

from common.coordinates import Coordinates
from entity.map import Map
from entity.player import Player
from entity.tile import Tile
from game import Game
from service.player_action_dispatcher import PlayerActionDispatcher

{placeholder}

map = Map(7, 7)
game = Game(map)
player_action_dispatcher = PlayerActionDispatcher(game)
my_player_ids = [0]

while True:
    game.turn_type = int(input())
    map.tiles.remove_all()
    for y in range(7):
        for x, tile_string in enumerate(input().split()):
            map.tiles.add(Tile(tile_string, Coordinates(x, y)))

    for i in range(2):
        inputs = input().split()

        player = game.players.get_by_id(i)
        if player is None:
            player = Player(i)
            if i in my_player_ids:
                player.is_my = True
            game.players.add(player)

        player.num_player_cards = int(inputs[0])  # the total number of quests for a player (hidden and revealed)
        player.coordinates = Coordinates(int(inputs[1]), int(inputs[2]))
        player.tile = Tile(inputs[3])

    num_items = int(input())  # the total number of items available on board and on player tiles
    for item_index in range(num_items):
        inputs = input().split()
        player = game.players.get_by_id(int(inputs[3]))
        item = player.items.get_or_create_by_id(item_index, inputs[0])
        item.coordinates = Coordinates(int(inputs[1]), int(inputs[2]))

    num_quests = int(input())  # the total number of revealed quests for both players
    for i in range(num_quests):
        inputs = input().split()
        quest_item_name = inputs[0]
        quest_player_id = int(inputs[1])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # PUSH <id> <direction> | MOVE <direction> | PASS
    actions = player_action_dispatcher.get_actions()
    for action in actions:
        print(action.to_string())
