from graphics import Line, Point


class Cell:
    def __init__(self, win, **kwargs):
        self.has_left_wall = kwargs.get('has_left_wall', True)
        self.has_right_wall = kwargs.get('has_right_wall', True)
        self.has_top_wall = kwargs.get('has_top_wall', True)
        self.has_bottom_wall = kwargs.get('has_bottom_wall', True)
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, **kwargs):
        self._x1 = kwargs.get('x1', 0)
        self._y1 = kwargs.get('y1', 0)
        self._x2 = kwargs.get('x2', 0)
        self._y2 = kwargs.get('y2', 0)

        if self.has_left_wall:
            left_wall = Line(
                Point(self._x1, self._y1),
                Point(self._x1, self._y2)
                )
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(
                Point(self._x2, self._y2),
                Point(self._x2, self._y1)
                )
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(
                Point(self._x1, self._y1),
                Point(self._x2, self._y1)
                )
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(
                Point(self._x2, self._y2),
                Point(self._x1, self._y2)
                )
            self._win.draw_line(bottom_wall)
