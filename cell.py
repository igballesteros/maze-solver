from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            l = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(l)

        if self.has_right_wall:
            l = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(l, "black")

        if self.has_top_wall:
            l = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(l, "black")

        if self.has_bottom_wall:
            l = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(l, "black")

    def draw_move(self, to_cell, undo=False):

        middle_dist_y = (self._y2 - self._y1) / 2 + self._y1
        middle_dist_x = (self._x2 - self._x1) / 2 + self._x1
        middle_current = Point(middle_dist_x, middle_dist_y)

        next_middle_y = (to_cell._y2 - to_cell._y1) / 2 + to_cell._y1
        next_middle_x = (to_cell._x2 - to_cell._x1) / 2 + to_cell._x1
        middle_next = Point(next_middle_x, next_middle_y)

        l = Line(middle_current, middle_next)
        if undo:
            self._win.draw_line(l, "red")
        else:
            self._win.draw_line(l, "gray")
