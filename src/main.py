import pyray as rl

def main():
    rl.init_window(640, 480, "Minesweeper")
    rl.set_target_fps(60)

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.BLACK)
        rl.draw_triangle([200, 360], [440, 360], [320, 120], rl.SKYBLUE)
        rl.end_drawing()

    rl.close_window()

if __name__ == "__main__":
    main()
