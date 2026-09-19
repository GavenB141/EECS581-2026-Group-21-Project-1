'''
Author: Gaven Behrends
Last Modified: 09.17.26
Modification: Integrate menu and Logic class
'''

import pyray as rl
from menu import Menu
from grid import Grid

def main():
    rl.set_config_flags(rl.ConfigFlags.FLAG_MSAA_4X_HINT 
                        | rl.ConfigFlags.FLAG_VSYNC_HINT)
    rl.init_window(640, 480, "Minesweeper")
    rl.set_target_fps(60)

    font = rl.load_font("assets/font/NotoSerif-SemiBold.ttf")
    menu = Menu(font)
    grid = Grid(10, 10, 10)  # Example grid initialization

    while not rl.window_should_close():
        # Reset the cursor each frame, so rendering code can set it per-frame
        rl.set_mouse_cursor(rl.MouseCursor.MOUSE_CURSOR_DEFAULT)

        rl.begin_drawing()
        draw_background()
        menu.render()
        grid.render()
        rl.end_drawing()

    rl.unload_font(font)
    rl.close_window()

def draw_background():
    rl.draw_rectangle_gradient_v(0, 0, rl.get_screen_width(), rl.get_screen_height(),
                                 [0,0,56,255],[0,0,0,255])

if __name__ == "__main__":
    main()
