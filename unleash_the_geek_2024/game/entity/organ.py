import random
from typing import Optional, Iterator

from common.coordinates import Coordinates
from entity.cell import Cell
from entity.dictionaries import OrganType, OrganDirection
from game import Game
from unleash_the_geek_2024.template import MutableCollection


class Organ:
    def __init__(self):
        self.id: Optional[int] = None
        self.type: Optional['OrganType'] = None
        self.cell: Optional[Cell] = None
        self.parent_id: Optional[int] = None
        self.root_id: Optional[int] = None
        self.direction: Optional['OrganDirection'] = None
        self.children: 'OrganCollection' = OrganCollection()

    def __str__(self):
        return f'O{self.id} {self.type.value} {self.cell.coordinates}'


class OrganCollection(MutableCollection):
    def __init__(self, elements: Optional[list] = None):
        super().__init__(elements)
        self.start: Optional[Organ] = None
        self.control: Optional[Organ] = None
        self.__map = {}
        self.__organ_by_id = {}
        self.__organ_by_root_id = {}

    def add(self, element_to_add: Organ):
        self.__map.setdefault(element_to_add.cell.coordinates.x, {})[element_to_add.cell.coordinates.y] = element_to_add
        self.__organ_by_id[element_to_add.id] = element_to_add
        self.__organ_by_root_id.setdefault(element_to_add.root_id, []).append(element_to_add)
        self.__organ_by_id[element_to_add.id] = element_to_add
        super().add(element_to_add)

    def get_random(self) -> Organ:
        return self.__organ_by_id.get(random.choice(list(self.__organ_by_id.keys())), None)

    def get_by_coordinates(self, coordinates: Coordinates) -> Optional[Organ]:
        return self.__map.get(coordinates.x, {}).get(coordinates.y, None)

    def get_by_id(self, organ_id: int) -> Optional[Organ]:
        return self.__organ_by_id.get(organ_id, None)

    def get_by_root_id(self, root_id: int) -> 'OrganCollection':
        return OrganCollection(self.__organ_by_root_id.get(root_id, []))

    def get_by_type(self, organ_type: OrganType) -> 'OrganCollection':
        return OrganCollection([organ for organ in self if organ.type == organ_type])

    def get_harvesters(self) -> 'OrganCollection':
        return self.get_by_type(OrganType.HARVESTER)

    def get_sporers(self) -> 'OrganCollection':
        return self.get_by_type(OrganType.SPORER)

    def get_roots(self) -> 'OrganCollection':
        return self.get_by_type(OrganType.ROOT)

    #
    # def get_passable_cells_around(
    #         self,
    #         coordinates: Coordinates,
    #         explored_grid: List[Organ],
    #         new_organs_to_look_around: List[Organ],
    #         distance_to_target: int,
    #         player
    # ):
    #     passable_organs_around = []
    #     for vector in VECTORS.values():
    #         organ_around = self.get_by_coordinates(coordinates + vector)
    #         if organ_around is player:
    #             raise Exception
    #
    #         if not organ_around or not organ_around.is_passable():
    #             continue
    #
    #         if organ_around in explored_grid:
    #             continue
    #
    #         if organ_around in new_organs_to_look_around:
    #             continue
    #
    #         organ_around.distance_to_target = distance_to_target
    #         passable_organs_around.append(organ_around)
    #
    #     return passable_organs_around

    def get_closest(self, organ_to_find: Organ) -> Organ:
        closest_distance = 999999
        closest_organ = None
        for organ in self:
            distance = organ_to_find.coordinates.get_manhattan_distance(organ.coordinates)
            if distance < closest_distance:
                closest_distance = distance
                closest_organ = organ

        return closest_organ

    def get_actionable_organs(self, game: 'Game') -> 'OrganCollection':
        """
        Get all organs that can perform an action,
        if neighboring cells are not occupied by other organs, or harvested proteins, or walls.
        """
        organs = OrganCollection()
        for organ in self:
            actionable = False
            empty_neighbors = game.neighbors_finder.get_empty_neighbors(organ.cell.coordinates)
            for empty_neighbor in empty_neighbors:
                cell_occupied = game.cells.get_by_coordinates(empty_neighbor)
                if not cell_occupied:
                    actionable = True
                    break

                if cell_occupied.is_protein():
                    protein = game.free_proteins.get_by_coordinates(empty_neighbor)
                    if not protein.is_harvested_by_me:
                        actionable = True
                    break

            if actionable:
                organs.add(organ)

        return organs

    def __iter__(self) -> Iterator[Organ]:
        return super().__iter__()

    def __str__(self):
        return 'Os: ' + ', '.join([str(organ) for organ in self])