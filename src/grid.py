'''
Author: Jocelyn Miller
Last Modified: 09.19.26
Modification: Store Minesweeper cells and expose their status by coordinate
'''

from minesweeper_logic import Cell


class Grid:
    def __init__(self, size=10):
        if size <= 0:
            raise ValueError("Grid size must be positive")

        self.size = size
        self.cells = [
            [Cell() for _ in range(size)]
            for _ in range(size)
        ]

    def _cell_at(self, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise IndexError("Cell coordinates are outside the grid")
        return self.cells[row][col]

    def get_cell(self, row, col):
        return self._cell_at(row, col)

    def is_mine(self, row, col):
        return self._cell_at(row, col).mine

    def is_revealed(self, row, col):
        return self._cell_at(row, col).revealed

    def is_flagged(self, row, col):
        return self._cell_at(row, col).flagged

    def adjacent_mines(self, row, col):
        return self._cell_at(row, col).adjacent
