from entity.move import MoveCollection, Move


class Tile:
    def __init__(self, tile_string: str):
        self.tile_string = tile_string

    def get_possible_moves(self, player) -> MoveCollection:
        possible_moves = MoveCollection()

        for index, direction_allowed in enumerate(self.tile_string):
            if int(direction_allowed) == 1:
                possible_moves.add(Move(index))

        return possible_moves
