'''
Author: Gaven Behrends
Last Modified: 09.20.26
Modification: Add reset buttons to ended games
'''

import pyray as rl
from menu import Menu, button
from board import Board


def main():
    rl.set_config_flags(rl.ConfigFlags.FLAG_MSAA_4X_HINT 
                        | rl.ConfigFlags.FLAG_VSYNC_HINT)
    rl.init_window(640, 480, "Minesweeper")
    rl.set_target_fps(60)

    font = rl.get_font_default()
    menu = Menu(font) 
    board = None # only creates when the player starts the game
    in_game = False # False when still in the menu, True when the game is running

    while not rl.window_should_close():
        # Reset the cursor each frame, so rendering code can set it per-frame
        rl.set_mouse_cursor(rl.MouseCursor.MOUSE_CURSOR_DEFAULT)

        rl.begin_drawing()
        draw_background()

        if not in_game:
            # menu.render returns True when the game is ready to start
            start_clicked = menu.render()
            if start_clicked:
                board = Board(font, menu.mines_slider.value)
                in_game = True
        else:
            assert board is not None
            # board.render() handles game logic and draws the frame
            board.render()
            # allow the player to reset
            if board.logic.game_over:
                button_width = (rl.get_screen_width() - 60) // 2
                menu_rect = rl.Rectangle(20, rl.get_screen_height() - 50, 
                                         button_width, 40)
                reset_rect = rl.Rectangle(40 + button_width,
                                          rl.get_screen_height() - 50,
                                          button_width, 40)
                # it's not possible for both buttons to be clicked at once,
                # so there is no `elif` here to prevent graphical jank
                if button(menu_rect, "Go to Menu", font):
                    in_game = False
                    board = None
                if button(reset_rect, "Reset", font):
                    board = Board(font, menu.mines_slider.value)

        rl.end_drawing()

    rl.unload_font(font)
    rl.close_window()


from math import sin


# Draw a subtle animated gradient background
def draw_background():
    t = (sin(rl.get_time()) + 1) / 2
    rl.draw_rectangle_gradient_v(0, 0, rl.get_screen_width(), rl.get_screen_height(),
                                 [0,0,56,255],
                                 rl.color_lerp([0,0,12,255],[0,0,30,255],t))


if __name__ == "__main__":
    main()
