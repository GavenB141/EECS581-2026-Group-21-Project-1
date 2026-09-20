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
    * reveal -
    * flag -
  
* Grid Class
    * _cell_at -
    * get_cell -
    * is_mine -
    * is_flagged -
    * adjacent_mines -
    * render_status - 

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
