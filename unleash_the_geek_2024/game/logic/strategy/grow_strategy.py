import sys
from typing import Optional

from common.coordinates import Coordinates
from entity.actions.base_action import BaseAction
from entity.actions.grow_action import HarvesterGrowAction, BasicGrowAction, TentacleGrowAction, \
    SporerGrowAction
from entity.cell import Cell
from entity.dictionaries import ProteinType
from entity.enemy_attack import EnemyAttack
from entity.free_protein import FreeProtein, FreeProteinCollection
from entity.organ import Organ, OrganCollection
from entity.organism import Organism
from entity.protein_attack import ProteinAttack
from logic.strategy.base_strategy import BaseStrategy
from service.direction_definer import DirectionDefiner


class GrowStrategy(BaseStrategy):
    def execute(self, organism: Organism) -> BaseAction:
        """ define the action to be taken in the game """
        actionable_organs = organism.organs.get_actionable_organs(self.game)
        print(f'actionable_organs: {actionable_organs}', file=sys.stderr, flush=True)

        enemy_attack = self.__get_closest_enemy_attack(actionable_organs)
        print(enemy_attack, file=sys.stderr, flush=True)
        tentacle_grow_action = self.__get_tentacle_grow_action(enemy_attack)
        if tentacle_grow_action:
            return tentacle_grow_action

        enemy_roots = self.game.enemy_player.organs.get_roots()
        priority_proteins = self.game.protein_prioritizer.get_priority_proteins()
        print(f'priority_proteins: {priority_proteins}', file=sys.stderr, flush=True)

        sporer_grow_action = self.__get_spore_grow_action(actionable_organs, priority_proteins, enemy_roots)
        if sporer_grow_action:
            return sporer_grow_action

        protein_attack = self.__get_closest_protein_attack(actionable_organs, priority_proteins)
        if not protein_attack:
            print("NO FREE PROTEIN", file=sys.stderr, flush=True)

            emtpy_neighbor = self.game.neighbors_finder.get_emtpy_neighbor(actionable_organs.first().cell.coordinates)
            return BasicGrowAction(actionable_organs.first(), emtpy_neighbor)

        print(protein_attack, file=sys.stderr, flush=True)
        harvester_grow_action = self.__get_harvester_grow_action(protein_attack)
        if harvester_grow_action:
            return harvester_grow_action

        basic_grow_action = self.__get_basic_grow_action(protein_attack)
        if basic_grow_action:
            return basic_grow_action

    def __get_closest_enemy_attack(self, actionable_organs: 'OrganCollection') -> Optional[EnemyAttack]:
        closest_enemy_organ: Optional[Organ] = None
        closest_organ_to_enemy: Optional[Organ] = None
        closest_distance_to_enemy: int = 1000
        for organ in actionable_organs:
            organ_coordinates = organ.cell.coordinates
            for enemy_organ in self.game.enemy_player.organs:
                distance = organ_coordinates.get_manhattan_distance(enemy_organ.cell.coordinates)
                if distance < closest_distance_to_enemy:
                    closest_distance_to_enemy = distance
                    closest_organ_to_enemy = organ
                    closest_enemy_organ = enemy_organ

        if not closest_enemy_organ:
            return None

        return EnemyAttack(closest_distance_to_enemy, closest_organ_to_enemy, closest_enemy_organ)

    def __get_spore_grow_action(
            self,
            actionable_organs: 'OrganCollection',
            not_harvested_proteins: 'FreeProteinCollection',
            enemy_roots: 'OrganCollection'
    ) -> Optional['SporerGrowAction']:
        for organ in actionable_organs:
            for enemy_root in enemy_roots:
                sporer_grow_action = self.__get_sporer_grow_action(enemy_root.cell, organ)
                if sporer_grow_action:
                    return sporer_grow_action

            for protein in not_harvested_proteins:
                sporer_grow_action = self.__get_sporer_grow_action(protein.cell, organ)
                if sporer_grow_action:
                    return sporer_grow_action

        return None

    def __get_closest_protein_attack(
            self,
            actionable_organs: 'OrganCollection',
            not_harvested_proteins: 'FreeProteinCollection',
    ) -> Optional['ProteinAttack']:
        if not_harvested_proteins.is_empty():
            return None

        closest_protein: Optional[FreeProtein] = None
        closest_organ_to_protein: Optional[Organ] = None
        closest_distance_to_protein: int = 1000
        for organ in actionable_organs:
            organ_coordinates = organ.cell.coordinates

            for protein in not_harvested_proteins:

                distance = organ_coordinates.get_manhattan_distance(protein.cell.coordinates)
                if distance < closest_distance_to_protein:
                    closest_distance_to_protein = distance
                    closest_organ_to_protein = organ
                    closest_protein = protein

            if closest_protein:
                return ProteinAttack(closest_distance_to_protein, closest_organ_to_protein, closest_protein)

        return None

    def __get_sporer_grow_action(self, target_cell: Cell, organ: Organ) -> Optional['SporerGrowAction']:
        if not self.game.my_player.resource_proteins.enough_to_build_sporer():
            return None

        empty_neighbors = self.game.neighbors_finder.get_empty_neighbors(organ.cell.coordinates)
        for neighbor in empty_neighbors:
            if self.game.coordinates_finder.coordinate_is_visible(target_cell.coordinates, neighbor, self.game.cells):
                distance = neighbor.get_manhattan_distance(target_cell.coordinates)
                if distance < 7:
                    return None

                direction = DirectionDefiner.define_direction(neighbor, target_cell.coordinates)
                return SporerGrowAction(organ, neighbor, direction)

        return None

    def __get_tentacle_grow_action(self, enemy_attack: EnemyAttack) -> Optional['TentacleGrowAction']:
        if not enemy_attack:
            return None

        if not self.game.my_player.resource_proteins.enough_to_build_tentacle():
            return None

        if enemy_attack.distance > 2:
            return None

        new_coordinates = self.__get_new_coords(enemy_attack.my_organ, enemy_attack.enemy_organ.cell)
        direction = DirectionDefiner.define_direction(new_coordinates, enemy_attack.enemy_organ.cell.coordinates)

        return TentacleGrowAction(enemy_attack.my_organ, new_coordinates, direction)

    def __get_harvester_grow_action(self, protein_attack: ProteinAttack) -> Optional['HarvesterGrowAction']:
        if protein_attack.distance != 2:
            return None

        if not self.game.my_player.resource_proteins.enough_to_build_harvester():
            return None

        ideal_direction = self.__get_ideal_moving_direction(protein_attack.my_organ, protein_attack.protein.cell)
        new_coords = protein_attack.my_organ.cell.coordinates + ideal_direction
        if not self.__is_empty(new_coords):
            return None

        print(f'protein to harvest: {protein_attack.protein.cell.coordinates}', file=sys.stderr, flush=True)
        direction = DirectionDefiner.define_direction(new_coords, protein_attack.protein.cell.coordinates)

        return HarvesterGrowAction(protein_attack.my_organ, new_coords, direction)

    def __get_basic_grow_action(self, protein_attack: ProteinAttack) -> Optional['BasicGrowAction']:
        if protein_attack.distance == 1:
            new_coordinates = protein_attack.protein.cell.coordinates
            print('EATING CLOSEST', file=sys.stderr, flush=True)
        else:
            new_coordinates = self.__get_new_coords(protein_attack.my_organ, protein_attack.protein.cell)
            print('MOVING TO CLOSEST', file=sys.stderr, flush=True)

        if not new_coordinates:
            return None

        print(f'{new_coordinates}', file=sys.stderr, flush=True)
        return BasicGrowAction(protein_attack.my_organ, new_coordinates)

    def __get_ideal_moving_direction(self, organ: Organ, cell: Cell) -> Coordinates:
        """
        define the direction of the movement, based on the relative position of the protein and the organ,
        I can't move diagonally
        """

        if organ.cell.coordinates.x > cell.coordinates.x:
            return Coordinates(-1, 0)
        if organ.cell.coordinates.x < cell.coordinates.x:
            return Coordinates(1, 0)
        if organ.cell.coordinates.y > cell.coordinates.y:
            return Coordinates(0, -1)
        if organ.cell.coordinates.y < cell.coordinates.y:
            return Coordinates(0, 1)

    def __get_new_coords(self, closest_organ: Organ, target_cell: 'Cell') -> 'Coordinates':
        ideal_direction = self.__get_ideal_moving_direction(closest_organ, target_cell)
        print(f"ideal_direction {ideal_direction}", file=sys.stderr, flush=True)
        new_coords = closest_organ.cell.coordinates + ideal_direction
        print(f"new_coords {new_coords}", file=sys.stderr, flush=True)
        next_cell = self.game.cells.get_by_coordinates(new_coords)
        if not next_cell or next_cell.is_protein():
            print("MOVE IDEAL", file=sys.stderr, flush=True)
            return new_coords

        print("MOVE SIDEWAYS", file=sys.stderr, flush=True)
        return self.game.neighbors_finder.get_emtpy_neighbor(closest_organ.cell.coordinates)

    def __is_empty(self, coordinates: Coordinates) -> bool:
        cell = self.game.cells.get_by_coordinates(coordinates)
        return not cell or cell.is_protein()
