import sys
from typing import Optional, Iterator, Tuple

from common.coordinates import Coordinates
from entity.base_protein import BaseProtein
from entity.cell import Cell
from entity.dictionaries import ProteinType, OrganDirection
from entity.organ import Organ, OrganCollection
from unleash_the_geek_2024.template import MutableCollection


class FreeProtein(BaseProtein):
    def __init__(self):
        super().__init__()
        self.cell: Optional[Cell] = None
        self.is_harvested_by_me = False

    def __str__(self):
        return f"FP {self.type.value} {self.cell.coordinates} {'H' if self.is_harvested_by_me else 'N'}"


class FreeProteinCollection(MutableCollection):
    def __init__(self, elements: Optional[list] = None):
        super().__init__(elements)
        self.__map = {}

    def add(self, element_to_add: FreeProtein):
        self.__map.setdefault(element_to_add.cell.coordinates.x, {})[element_to_add.cell.coordinates.y] = element_to_add
        super().add(element_to_add)

    def get_by_coordinates(self, coordinates: Coordinates) -> Optional[FreeProtein]:
        return self.__map.get(coordinates.x, {}).get(coordinates.y, None)

    def get_closest(self, organ_to_find: Organ) -> FreeProtein:
        closest_distance = 999999
        closest_protein = None
        for protein in self:
            distance = organ_to_find.cell.coordinates.get_manhattan_distance(protein.cell.coordinates)
            if distance < closest_distance:
                closest_distance = distance
                closest_protein = protein

        return closest_protein

    def __iter__(self) -> Iterator[FreeProtein]:
        return super().__iter__()

    def get_harvested_and_not_by_me(self) -> Tuple['FreeProteinCollection', 'FreeProteinCollection']:
        harvested = FreeProteinCollection()
        not_harvested = FreeProteinCollection()
        for protein in self:
            if protein.is_harvested_by_me:
                harvested.add(protein)
            else:
                not_harvested.add(protein)

        return harvested, not_harvested

    def has_type(self, _type: ProteinType) -> bool:
        for protein in self:
            if protein.type.value == _type.value:
                return True

        return False

    def get_by_type(self, _type: ProteinType) -> 'FreeProteinCollection':
        proteins_by_type = FreeProteinCollection()
        for protein in self:
            if protein.type.value == _type.value:
                proteins_by_type.add(protein)

        return proteins_by_type

    def define_if_harvested_by_me(self, game: 'Game') -> None:
        """ harvesters are located in the neighbor cells of proteins """
        harvesters = game.my_player.organs.get_harvesters()
        for harvester in harvesters:
            if harvester.direction.value == OrganDirection.NORTH.value:
                protein_coordinate = harvester.cell.coordinates + Coordinates(0, -1)
            elif harvester.direction.value == OrganDirection.SOUTH.value:
                protein_coordinate = harvester.cell.coordinates + Coordinates(0, 1)
            elif harvester.direction.value == OrganDirection.EAST.value:
                protein_coordinate = harvester.cell.coordinates + Coordinates(1, 0)
            else:
                protein_coordinate = harvester.cell.coordinates + Coordinates(-1, 0)

            protein = game.free_proteins.get_by_coordinates(protein_coordinate)
            if protein:
                protein.is_harvested_by_me = True

    def __str__(self):
        return ', '.join([str(protein) for protein in self])
