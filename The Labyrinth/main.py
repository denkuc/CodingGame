class Game:
    def __init__(self, game_map: Map):
        self.map: Map = game_map
        self.cells: CellCollection = CellCollection()
        self.player: Optional[Cell] = None
        self.time_is_running: bool = False


class RegionsExtractor:
    """
    Based on Sequential labeling algorithm from
    https://medium.com/@dellawen1997/connected-component-labeling-midterm-part-1-4b2aebfb277

    TODO: prettify and refactor
    """

    def __init__(self, cells: CellCollection, game_map: Map):
        self.__cells = cells
        self.__map = game_map

    def assign_regions(self):
        h = self.__map.height
        w = self.__map.width
        label = 0
        id_ = 0
        link = []

        for row in range(h):
            for col in range(w):
                cell = self.__cells.get_by_coordinates(Coordinates(col, row))
                if not cell.is_passable():
                    cell.region = 0
                else:
                    current_neighbors = self.__neighbors(col, row)
                    if current_neighbors == (0, 0):
                        label += 1
                        cell.region = label

                    else:
                        if min(current_neighbors) == 0 or current_neighbors[0] == current_neighbors[1]:
                            cell.region = max(current_neighbors)
                        else:
                            cell.region = min(current_neighbors)

                            if id_ == 0:
                                link.append(current_neighbors)
                                id_ = id_ + 1
                            else:
                                check = 0
                                for k in range(id_):
                                    # 交集
                                    tmp = set(link[k]).intersection(set(current_neighbors))
                                    if len(tmp) != 0:
                                        link[k] = set(link[k]).union(current_neighbors)
                                        np.array(link)
                                        check = check + 1

                                if check == 0:
                                    id_ = id_ + 1
                                    np.array(link)
                                    link.append(set(current_neighbors))

        for row in range(h):
            for col in range(w):
                for x in range(id_):
                    cell = self.__cells.get_by_coordinates(Coordinates(col, row))
                    if cell.region in link[x] and cell.region != 0:
                        cell.region = min(link[x])

    def __neighbors(self, i, j) -> Tuple[int, int]:
        left_cell = self.__cells.get_by_coordinates(Coordinates(i-1, j))
        above_cell = self.__cells.get_by_coordinates(Coordinates(i, j - 1))

        neighbors_tuple = (left_cell.region if left_cell else 0, above_cell.region if above_cell else 0)

        return neighbors_tuple


class PathFinder:
    """
    Based on the basic Sample algorythm from https://en.wikipedia.org/wiki/Pathfinding
    Can be improved with A* though
    """

    def __init__(self, game: Game):
        self.__game: Game = game

    def get_path(self, target: Cell) -> List[Cell]:
        explored_grid = []
        distance_to_target = 0
        target.distance_to_target = distance_to_target
        explored_grid.append(target)

        cells_to_look_around = [target]

        while True:
            distance_to_target += 1
            try:
                cells_to_look_around = self.__get_new_cells_to_look_around(
                    cells_to_look_around,
                    distance_to_target,
                    explored_grid,
                    self.__game.player
                )
            except Exception:
                break

            explored_grid += cells_to_look_around

        return self.__build_path_from_grid(explored_grid)

    def __get_new_cells_to_look_around(
            self,
            cells_to_look_around: List[Cell],
            distance_to_target: int,
            explored_grid: List[Cell],
            player: Cell
    ):
        new_cells_to_look_around = []
        for cell_to_look_around in cells_to_look_around:
            new_cells_to_look_around += self.__game.cells.get_passable_cells_around(
                cell_to_look_around.coordinates,
                explored_grid,
                new_cells_to_look_around,
                distance_to_target,
                player
            )

        return new_cells_to_look_around

    def __build_path_from_grid(self, explored_grid: List[Cell]) -> List[Cell]:
        """ removes redundant cells """
        clean_path = []

        closest = self.__game.player
        while explored_grid:
            cell_with_max_weight = explored_grid[-1]
            cells_with_max_weight = CellCollection([cell_with_max_weight])
            for cell in explored_grid:
                if cell is not cell_with_max_weight and cell.distance_to_target == cell_with_max_weight.distance_to_target:
                    cells_with_max_weight.add(cell)

            for cell in cells_with_max_weight:
                explored_grid.remove(cell)

            closest = cells_with_max_weight.get_closest(closest)
            clean_path.append(closest)

        return clean_path[::-1]


class DirectionDispatcher:
    def __init__(self, game: Game):
        self.__game: Game = game
        self.__path_finder = PathFinder(game)
        self.__path_to_start: List[Cell] = []
        self.__path_to_control: List[Cell] = []

    def get_next_direction(self) -> Direction:
        next_cell = self.__get_next_cell()

        return DirectionDefiner.get_direction(next_cell.coordinates, self.__game.player.coordinates)

    def __get_next_cell(self) -> Cell:
        # Player needs to return to the start if time is running
        if self.__game.time_is_running:
            if not self.__path_to_start:
                # save to cache, to not calculate each time
                self.__path_to_start = self.__path_finder.get_path(self.__game.cells.start)

            return self.__path_to_start.pop()

        region_cells = self.__game.cells.get_all_cells_of_region(self.__game.player.region)
        cells_border_with_unknown = self.__get_cells_near_unknown(region_cells)

        # If region is not yet fully explored
        if cells_border_with_unknown:
            closest_path = self.__find_closest_path_to_unknown(cells_border_with_unknown)

            return closest_path.pop()

        if not self.__path_to_control:
            # save to cache, to not calculate each time
            self.__path_to_control = self.__path_finder.get_path(self.__game.cells.control)

        return self.__path_to_control.pop()

    def __find_closest_path_to_unknown(self, cells_border_with_unknown):
        closest_path_length = 9999999
        closest_path = None

        # choose between several paths to avoid loops
        for cell_borders_with_unknown in cells_border_with_unknown.get_with_limit(2):
            path_to_unknown = self.__path_finder.get_path(cell_borders_with_unknown)
            if len(path_to_unknown) < closest_path_length:
                closest_path_length = len(path_to_unknown)
                closest_path = path_to_unknown

        return closest_path

    def __get_cells_near_unknown(self, region_cells: CellCollection) -> CellCollection:
        cells_near_unknown = CellCollection()
        for region_cell in region_cells:
            if self.__game.cells.is_near_unknown(region_cell.coordinates):
                cells_near_unknown.add(region_cell)

        return cells_near_unknown


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]


# labyrinth loop
game_map = Map(c, r)
game = Game(game_map)
for i in range(r):
    for j in range(c):
        cell = CellBuilder.build_cell(j, i)
        game.cells.add(cell)

direction_dispatcher = DirectionDispatcher(game)
regions_extractor = RegionsExtractor(game.cells, game_map)

turn = 0

while True:
    turn += 1
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    kr, kc = [int(i) for i in input().split()]
    current_coordinates = Coordinates(kc, kr)

    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        for j, cell_type in enumerate(row):
            game.cells.update_cell(j, i, cell_type)

    regions_extractor.assign_regions()

    current_cell = game.cells.get_by_coordinates(current_coordinates)
    if current_cell.is_control():
        game.time_is_running = True

    game.player = current_cell

    selected_direction = direction_dispatcher.get_next_direction()
    print(selected_direction.value)
