'''
Author: Max Toney, Cooper Fish
Last Modified: 09.17.26
Modification: Added check_win
'''

import random
from grid import Grid

class Logic: #determines the logic of the game
    def __init__(self, mine_count, size=10):
        self.mine_count = mine_count #mine counter
        self.game_over = False #status of if the game is still ongoing 
        self.grid = Grid(size)
    
    def place_mines(self, safe_row=None, safe_col=None): 
        all_cells = [
            (r, c)
            for r in range(self.grid.size)
            for c in range(self.grid.size)
        ] # builds list of all (r,c)
        if safe_row is not None and safe_col is not None:
            all_cells.remove((safe_row, safe_col)) # protect the first click cell from being a mine
        mine_locations = random.sample(all_cells, self.mine_count) # pick unique random cells for mines
        for row, col in mine_locations:
            self.grid.get_cell(row, col).mine = True # mark that cell as a mine
        self.calc_adjacency() # calculate adjacency counts now that mines are placed

    def calc_adjacency(self):
        for row in range(self.grid.size):
            for col in range(self.grid.size):
                cell = self.grid.get_cell(row, col) # targets the cell we're counting for
                if cell.mine:
                    continue # mines don't need a count
                count = 0
                for row_change in [-1, 0, 1]: # scan all 8 surrounding cells
                    for col_change in [-1, 0, 1]:
                        if row_change == 0 and col_change == 0: 
                            continue # skip the cell itself
                        next_row = row + row_change # row of the neighbor being checked
                        next_col = col + col_change # col of the neighbor being checked
                        if next_row < 0 or next_row >= self.grid.size:
                            continue # stay in bounds vertically
                        if next_col < 0 or next_col >= self.grid.size:
                            continue # stay in bounds horizontally
                        if self.grid.get_cell(next_row, next_col).mine:
                            count += 1 # found a neighboring mine
                cell.adjacent = count # store the final count on the cell

    def reveal_cell(self, row, col):
        cell = self.grid.get_cell(row, col) #targets the cell we are revealing
        if cell.revealed: #if already revealed, return
            return
        if cell.flagged: #if flagged, don't reveal
            return
        cell.reveal() #reveals cell
        if cell.mine: #checks if the cell is a mine
            self.loss() #if it is, game over :(
            return
        if cell.adjacent == 0: #checks if revealed cell has no adjacent mines
            self.recursive_reveal(row, col) #if yes, recurse

    def recursive_reveal(self, row, col):
        for row_change in [-1, 0, 1]: #changes the row and col to focus on adjacent cells
            for col_change in [-1, 0, 1]:
                if row_change == 0 and col_change == 0: #checks if its focusing on the orignal cell
                    continue #if yes, go back
                next_row = row + row_change #initializes the next row and col of focus
                next_col = col + col_change
                if next_row < 0 or next_row >= self.grid.size: #keeps a user from revealing a cell out of bounds
                    continue
                if next_col < 0 or next_col >= self.grid.size:
                    continue
                self.reveal_cell(next_row, next_col) #runs the reveal function on the next targeted cell.

    def check_win(self):
        for row in range(self.grid.size):
            for col in range(self.grid.size):
                cell = self.grid.get_cell(row, col) # targets the cell we're checking
                if not cell.mine and not cell.revealed:
                    return False # a safe cell is still hidden
        self.game_over = True # every safe cell is revealed
        return True

    def loss(self):
        self.game_over = True #changes the game over status to true
        #might add more. reveal all mines on loss maybe?
