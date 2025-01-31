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
        if self._win is None:
            return
        
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

    def draw_move(self, to_cell, undo=False):
        xA, yA = self.get_center_coordinates()
        xB, yB = to_cell.get_center_coordinates()
        path = Line(Point(xA, yA), Point(xB, yB))
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        self._win.draw_line(path, fill_color=fill_color)


    def get_center_coordinates(self):
        x = self._x1 + (abs(self._x2 - self._x1) // 2)
        y = self._y1 + (abs(self._y2 - self._y1) // 2)
        return x, y