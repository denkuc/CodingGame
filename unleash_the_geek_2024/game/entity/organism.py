import sys
from typing import Optional

from entity.organ import Organ, OrganCollection
from unleash_the_geek_2024.template import MutableCollection


class Organism:
    def __init__(self):
        self.organs = OrganCollection()
        self.root: Optional[Organ] = None


class OrganismCollection(MutableCollection):
    def __init__(self, elements: Optional[list] = None):
        super().__init__(elements)
        self.__map = {}

    def add(self, element_to_add: Organism):
        super().add(element_to_add)
        self.__map[element_to_add.root.id] = element_to_add

    def get_by_root_id(self, root_id: int) -> Optional[Organism]:
        return self.__map.get(root_id, None)

    def get_roots(self) -> 'OrganCollection':
        return OrganCollection([organism.root for organism in self])

    def get_or_create(self, organism_root: Organ) -> Organism:
        organism = self.get_by_root_id(organism_root.id)
        if organism is None:
            organism = Organism()
            organism.root = organism_root
            organism.organs.add(organism_root)

            self.add(organism)

        return organism

    def remove_all(self):
        self.__map = {}
        super().remove_all()
