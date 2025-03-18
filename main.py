from graphics import Window
from cell import Cell


def main():

    win = Window(600, 800)

    c1 = Cell(win)

    c1.draw(10, 10, 50, 50)

    c2 = Cell(win)
    c2.draw(50, 10, 90, 50)

    c1.draw_move(c2, True)

    win.wait_for_close()


main()
