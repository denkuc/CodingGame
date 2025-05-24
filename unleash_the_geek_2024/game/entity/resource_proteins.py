from typing import List, Optional

from entity.dictionaries import ProteinType


class ResourceProteins:
    def __init__(self, proteins: List[int]):
        self.count_a = proteins[0]
        self.count_b = proteins[1]
        self.count_c = proteins[2]
        self.count_d = proteins[3]

    def enough_to_build_harvester(self):
        """To grow a HARVESTER you need 1 C type protein and 1 D type protein."""
        return self.count_c >= 1 and self.count_d >= 1

    def enough_to_build_tentacle(self):
        """To grow a TENTACLE you need 1 B type protein and 1 C type protein."""
        return self.count_b >= 1 and self.count_c >= 1

    def enough_to_build_sporer(self):
        """To grow a SPORER you need 1 B type protein and 1 D type protein."""
        return self.count_b >= 1 and self.count_d >= 1

    def enough_to_build_root(self):
        """To spore a new ROOT you need 1 of each protein."""
        return self.count_a >= 1 and self.count_b >= 1 and self.count_c >= 1 and self.count_d >= 1

    def get_lowest_resource(self) -> Optional[ProteinType]:
        lowest_resource = min(self.count_a, self.count_b, self.count_c, self.count_d)
        if lowest_resource >= 4:
            return None

        if lowest_resource == self.count_a:
            return ProteinType.A
        if lowest_resource == self.count_b:
            return ProteinType.B
        if lowest_resource == self.count_c:
            return ProteinType.C
        if lowest_resource == self.count_d:
            return ProteinType.D
