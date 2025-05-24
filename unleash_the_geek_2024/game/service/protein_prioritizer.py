import sys
from typing import Optional

from common.coordinates import Coordinates, CoordinatesCollection
from entity.cell import CellCollection
from entity.dictionaries import ProteinType
from entity.free_protein import FreeProteinCollection


class ProteinPrioritizer:
    def __init__(self, game):
        self.game = game

    def get_priority_proteins(self) -> 'FreeProteinCollection':
        harvested_proteins, not_harvested_proteins = self.game.free_proteins.get_harvested_and_not_by_me()

        lowest_protein_type = self.game.my_player.resource_proteins.get_lowest_resource()
        if not harvested_proteins.has_type(ProteinType.A):
            print("NO A PROTEIN harvested", file=sys.stderr, flush=True)
            priority_proteins = not_harvested_proteins.get_by_type(ProteinType.A)
        elif lowest_protein_type:
            priority_proteins = not_harvested_proteins.get_by_type(lowest_protein_type)
        else:
            priority_proteins = not_harvested_proteins

        return priority_proteins
