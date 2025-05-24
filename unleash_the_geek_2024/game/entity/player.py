from typing import List, Optional

from entity.organ import OrganCollection
from entity.organism import OrganismCollection
from entity.resource_proteins import ResourceProteins


class Player:
    def __init__(self, player_id: int):
        self.id = player_id
        self.organs = OrganCollection()
        self.resource_proteins: Optional[ResourceProteins] = None
        self.organisms = OrganismCollection()

    def add_proteins(self, proteins: List[int]):
        self.resource_proteins = ResourceProteins(proteins)
