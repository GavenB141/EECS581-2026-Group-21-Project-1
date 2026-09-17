'''
Author: Max Toney
Last Modified: 09.16.26
Modification: Created cell class.
'''

class cell:
    def __init__(self): 
        self.mine = False #is it a mine?
        self.revealed = False #is it revealed?
        self.flagged = False #is it flagged?
        self.adjacent = 0 #is it adjacent to any mines?
    
    def reveal(self): #function to reveal a hidden cell
        if not self.flagged: #unless the cell is flagged. prevents user from accidentally revealing a flagged cell.
            self.revealed = True 
    
    def flag(self): #function to set a cell to a flagged or unflagged state, depending on which it already is
        if not self.revealed: #unless the cell is already revealed
            self.flagged = not self.flagged #makes the flagged status the opposite of what it already was