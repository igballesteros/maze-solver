from graphics import Window
from cell import Cell


def main():

    win = Window(600, 800)

    c = Cell(win)
    c.draw(10, 10, 30, 30)

    c.has_bottom_wall = False
    c.draw(35, 35, 55, 55)

    c.has_left_wall = False
    c.draw(60, 60, 80, 80)

    c.has_right_wall = False
    c.draw(85, 85, 105, 105)

    win.wait_for_close()


main()
