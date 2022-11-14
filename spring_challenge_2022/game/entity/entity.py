from entity.coordinates import Coordinates


class Entity:
    def __init__(self):
        self.id: int = 0
        self.point: Coordinates = Coordinates()
        self.shield_life: int = 0
        self.is_controlled: bool = False
