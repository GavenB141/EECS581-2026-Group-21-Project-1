'''
Author: Jocelyn Miller
KUID: 3090871
Assignment 2
Last Modified: 09.10.2025
Modification: Created the SodokuSolver class to solve the puzzle
'''

class SodukuSolver():

    def __init__(self, file): #Initializes the SodukuSolver class
        self.file = file
        self.board = self._read_puzzle()
        self.solutions = [] # A list to store all solutions
        
    def _read_puzzle(self): # Code Fixed with ChatGPT
        # Reads the puzzle from the file and returns it as a list that the rest of the program can access.
        board = []
        with open(self.file, 'r') as f:
            for line in f:
                # This line splits the string by any whitespace, correctly
                # separating the numbers and underscores.
                cells = line.strip().split()
                board.append(cells)
        return board
    
    def print(self): #prints the board to screen
        for row in self.board:
            print(' '.join(row))

    def edit(self, row, col, entry): #allows edits to the board
        if 0 <= row < len(self.board) and 0 <= col < len(self.board[row]):
            self.board[row][col] = entry

    def is_empty(self, row, col): #checks if a cell is empty
        if self.board[row][col] == "_":
            return True
        return False
    
    def is_valid(self, row, col, num): # checks if a move is valid by checking by row, column, and 3x3 box
        if not self.is_in_row(row, num):
            return False
        if not self.is_in_col(col, num):
            return False
        if not self.is_in_box(row, col, num):
            return False
        return True
    
    def is_in_row(self, row, num): # checks if a number is already in the row.
        for col in range(9):
            if self.board[row][col] == num:
                return False
        return True
    
    def is_in_col(self, col, num): # checks if a number is already in the column.
        for row in range(9):
            if self.board[row][col] == num:
                return False
        return True
    
    def is_in_box(self, row, col, num): # checks if a number is already in the 3x3 box.
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range (3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True
    
    def find_empty_cell(self): # Iterates through the program to find an empty cell and returns it
        for row in range(9):
            for col in range(9):
                if self.is_empty(row, col):
                    return (row, col)
        return None
    
    def _deep_copy(self): # Sourced from ChatGPT as I am not to use external libraries
        # This creates a copy of the board(new_board) and then returns it back to self.solve(), which then appends it to the solutions list.
        new_board = []
        for row in self.board:
            new_board.append(row[:])
        return new_board

    def solve(self):
        # if there is no empty cells, we append the board to the solutions list
        find = self.find_empty_cell()
        if not find:
            self.solutions.append(self._deep_copy())
            #uses _deep_copy() to append a copy of the board to the solutions list
            return
        else:
        # starting with the first empty cell we find, we use num to brute force an answer, checking with is_valid() as we go.
            row, col = find
            for num in range(1,10):
                if self.is_valid(row, col, str(num)):
                    self.board[row][col] = str(num)
                # Recurses back through .solve() and allows for the program to find multiple solutions.
                    self.solve()
                    self.board[row][col] = "_"
