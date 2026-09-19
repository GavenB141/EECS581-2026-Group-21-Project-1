'''
Author: Jocelyn Miller
Last Modified: 09.19.26
Modification: Updated Documentation to work for the Minesweeper Project
'''
import pyray as rl
from minesweeper_logic import Logic
from minesweeper_logic import Cell

class Grid():

    def __init__(self, size=10, mine_count=10): #Initializes the Grid class
        self.size = size
        self.mine_count = mine_count
    # which class creates the grid? Grid or Logic?  

    def _place_mines(self):
        # Placeholder for mine placement logic
        pass

    def _calculate_adjacent_mines(self):
        # Placeholder for adjacent mine calculation logic
        pass
        # Reads the puzzle from the file and returns it as a list that the rest of the program can access.
        # currently commented out as we will not be reading board from a file, but i'm not sure how to change that as of rn.
        board = []
        '''
        with open("puzzle.txt", "r") as file:
                # This line splits the string by any whitespace, correctly
                # separating the numbers and underscores.
                cells = line.strip().split()
                board.append(cells)
        '''      
        return board
        
    def print(self): #prints the board to screen (should be edited by other members)
        column_labels = [str(col + 1) for col in range(len(self.board[0]))]
        print('   ' + ' '.join(f'{label:>2}' for label in column_labels))

        for row_number, row in enumerate(self.board):
            print(f'{row_number:>2} ' + ' '.join(f'{cell:>2}' for cell in row))
    
    def edit(self, row, col, entry): #allows edits to the board
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
            self.board[row][col] = entry

    def is_empty(self, row, col): #checks if a cell is empty 
        if self.board[row][col] == "_": # character will change if input for an empty square changes
            return True
        return False
    
    def is_valid(self, row, col, num): # checks if a move is valid by checking by row, column, and 3x3 box (should be modified to validate moves based on minesweeper game logic)
        if not self.is_in_row(row, num):
            return False
        if not self.is_in_col(col, num):
            return False
         #removed the is_in_box function, because it isn't needed for minesweeper
        return True

    def render(self): # will render the grid to the screeen
        # Placeholder for rendering logic
        pass
