import sys

from entity.dictionaries import CellType


class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [['.' for _ in range(width)] for _ in range(height)]

    def redraw_map(self, cells):
        for cell in cells:
            if cell.is_wall():
                self.grid[cell.coordinates.y][cell.coordinates.x] = '#'
            elif cell.is_protein():
                self.grid[cell.coordinates.y][cell.coordinates.x] = cell.value
            elif cell.is_organ():
                self.grid[cell.coordinates.y][cell.coordinates.x] = cell.value

        self.print_map()

    def print_map(self):
        print('MAP:', flush=True, file=sys.stderr)
        for row in self.grid:
            print(' '.join(map(str, row)), flush=True, file=sys.stderr)
