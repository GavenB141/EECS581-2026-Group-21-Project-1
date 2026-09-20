'''
Author: Jocelyn Miller
Last Modified: 09.19.26
Modification: Store Minesweeper cells and expose their status by coordinate
'''

import pyray as rl


class Cell:
    def __init__(self):
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.adjacent = 0

    def reveal(self):
        if not self.flagged:
            self.revealed = True

    def flag(self):
        if not self.revealed:
            self.flagged = not self.flagged


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

    def render_status(self, font, mine_count, x=0, y=0, width=None, height=48):
        if width is None:
            width = rl.get_screen_width()

        flag_count = sum(
            1
            for row in self.cells
            for cell in row
            if cell.flagged
        )
        mines_left = mine_count - flag_count

        rl.draw_rectangle(x, y, width, height, rl.BLACK)
        rl.draw_text(
            f"Mines left: {mines_left}",
            x + 12,
            y + 12,
            24,
            rl.WHITE,
        )
