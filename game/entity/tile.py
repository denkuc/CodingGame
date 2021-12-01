from entity.direction import DirectionCollection, Direction


class Tile:
    def __init__(self, tile_string: str):
        self.tile_string = tile_string

    def get_possible_directions(self, player) -> DirectionCollection:
        possible_directions = DirectionCollection()

        for index, direction_allowed in enumerate(self.tile_string):
            if int(direction_allowed) == 1:
                possible_directions.add(Direction(index))

        return possible_directions
