import sys
from typing import Optional

from common.coordinates import Coordinates
from entity.actions.base_action import BaseAction
from entity.actions.spore_action import SporeAction
from entity.cell import CellCollection
from entity.organ import Organ
from entity.organism import Organism
from logic.strategy.base_strategy import BaseStrategy


class SporeStrategy(BaseStrategy):
    """
    """
    def execute(self, organism: Organism) -> Optional[SporeAction]:
        if not self.game.my_player.resource_proteins.enough_to_build_root():
            return None

        sporers = organism.organs.get_sporers()
        priority_proteins = self.game.protein_prioritizer.get_priority_proteins()
        print(f'priority_proteins: {priority_proteins}', file=sys.stderr, flush=True)
        enemy_roots = self.game.enemy_player.organisms.get_roots()

        for sporer in sporers:
            print(f'Sporer: {sporer}', flush=True, file=sys.stderr)
            for enemy_root in enemy_roots:
                spore_action = self.__get_spore_action(sporer, enemy_root.cell.coordinates, self.game.cells)
                if spore_action:
                    return spore_action

            longest_distance_to_protein = 0
            farther_protein = None
            for free_protein in priority_proteins:
                if self.__target_is_reachable(free_protein.cell.coordinates, sporer.cell.coordinates, self.game.cells):
                    distance = free_protein.cell.coordinates.get_manhattan_distance(sporer.cell.coordinates)
                    if distance > longest_distance_to_protein:
                        longest_distance_to_protein = distance
                        farther_protein = free_protein

            if farther_protein:
                spore_action = self.__get_spore_action(sporer, farther_protein.cell.coordinates, self.game.cells)
                if spore_action:
                    return spore_action

            return None

    def __target_is_reachable(
            self,
            target_xy: 'Coordinates',
            sporer_xy: 'Coordinates',
            all_cells: 'CellCollection'
    ) -> bool:
        if not self.game.coordinates_finder.coordinate_is_visible(target_xy, sporer_xy, all_cells):
            return False

        distance = target_xy.get_manhattan_distance(sporer_xy)
        if distance <= 3:
            return False

        return True

    def __get_spore_action(
            self,
            sporer: 'Organ',
            target_xy: 'Coordinates',
            all_cells: 'CellCollection'
    ) -> Optional['SporeAction']:
        if self.__target_is_reachable(target_xy, sporer.cell.coordinates, all_cells):
            spore_at = self.__step_back_two_cells(sporer.cell.coordinates, target_xy)
            print(f'Sporing at: {spore_at}', flush=True, file=sys.stderr)

            return SporeAction(sporer, spore_at)

        return None

    def __step_back_two_cells(self, first_xy: 'Coordinates', target_xy: 'Coordinates') -> 'Coordinates':
        print(f'First: {first_xy}, Target: {target_xy}', flush=True, file=sys.stderr)
        if first_xy.x == target_xy.x:
            if first_xy.y < target_xy.y:
                return Coordinates(target_xy.x, target_xy.y - 2)

            return Coordinates(target_xy.x, target_xy.y + 2)

        if first_xy.y == target_xy.y:
            if first_xy.x < target_xy.x:
                return Coordinates(target_xy.x - 2, target_xy.y)

            return Coordinates(target_xy.x + 2, target_xy.y)
