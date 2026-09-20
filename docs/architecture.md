# Architecture Breakdown

### Goal: Discuss the purpose of each file, class, and associated functions to clarify how the program works
---

## main.py
* main -
* draw_background -
  
## board.py
* Board Class  
    * render -
    * _cell_at -
    * _handle_input -
    * _reveal_all_mines -
    * _draw_status_bar -
    * _draw_grid - 

## grid.py
* Cell Class  
The Cell class will hold the information for a given square in the Minesweeper board. This information includes if the cell is flagged, if the cell has a mine, if the cell has been revealed to the player, and how many mines are adjacent to the cell.
    * reveal - If the cell has not been flagged, it will be revealed to the player
    * flag - If the cell has not been revealed, the flagged property will be toggled, so the player can flag and unflag cells.
  
* Grid Class
The Grid class will create a 10 by 10 grid of cells, that can be used to render the board to screen and organize the board data.
    * _cell_at - When given a row and column, this private function will retrieve the Cell at the given location. It will throw an index error if the cell is unreachable.
    * get_cell - The public method that other classes will use to get information at a particular point, by giving it a row and column within the Grid.
    * is_mine - This checks if the Cell at the given row and column inputs is a mine.
    * is_flagged - This checks if the Cell at the given row and column inputs has been flagged.
    * is_revealed - This checks if the Cell at the given row and column inputs has been revealed by the player.
    * adjacent_mines - When given a specific row and column, it returns the number of adjacent mines to that Cell.
    * render_status - This renders the status bar on the top left of the screen. For now, it just shows the remaining number of mines, which is calculated by taking the number of mines and subtracting the number of flagged Cells from it

## minesweeper_logic.py
* Logic Class  
  * place_mines -
  * calc_adjacency -
  * reveal_cell -
  * recursive_reveal -
  * check_win -
  * loss - 

## menu.py
* Menu class  
    * render - 
    
* Slider class  
     * render -
     * _handle_mouse_input
* button -
