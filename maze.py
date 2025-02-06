from cell import Cell
import time
import random


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1=x1, y1=y1, x2=x2, y2=y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = {"i" : 0, "j" : 0}
        exit = {"i" : self._num_cols - 1, "j" : self._num_rows - 1}
        self._cells[entrance["i"]][entrance["j"]].has_top_wall = False
        self._draw_cell(entrance["i"], entrance["j"])
        self._cells[exit["i"]][exit["j"]].has_bottom_wall = False
        self._draw_cell(exit["i"], exit["j"])

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            if i > 0:
                left_neighbor = self._cells[i-1][j]
                if not left_neighbor._visited:
                    to_visit.append(("left", i-1, j))
            if i < self._num_cols - 1:
                right_neighbor = self._cells[i+1][j]
                if not right_neighbor._visited:
                    to_visit.append(("right", i+1, j))
            if j > 0:
                top_neighbor = self._cells[i][j-1]
                if not top_neighbor._visited:
                    to_visit.append(("top", i, j-1))
            if j < self._num_rows - 1:
                bottom_neighbor = self._cells[i][j+1]
                if not bottom_neighbor._visited:
                    to_visit.append(("bottom", i, j+1))
            if not to_visit:
                return
            where_to_go = random.choice(to_visit)
            direction = where_to_go[0]
            next_cell = self._cells[where_to_go[1]][where_to_go[2]]
            this_cell = self._cells[i][j]
            match direction:
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i, j)
                    self._cells[where_to_go[1]][where_to_go[2]].has_right_wall = False
                    self._draw_cell(where_to_go[1], where_to_go[2])
                case "right":
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i, j)
                    self._cells[where_to_go[1]][where_to_go[2]].has_left_wall = False
                    self._draw_cell(where_to_go[1], where_to_go[2])
                case "top":
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i, j)
                    self._cells[where_to_go[1]][where_to_go[2]].has_bottom_wall = False
                    self._draw_cell(where_to_go[1], where_to_go[2])
                case "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i, j)
                    self._cells[where_to_go[1]][where_to_go[2]].has_top_wall = False
                    self._draw_cell(where_to_go[1], where_to_go[2])
            self._break_walls_r(where_to_go[1], where_to_go[2])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False

    def get_cell(self, row, col):
        return self._cells[row][col]

    def get_cells(self):
        return self._cells

    def solve(self):
        return self._solver_r(0, 0)

    def _solver_r(self, i, j):
        directions = [("left", -1,0), ("right", 1,0), ("top", 0,-1), ("bottom", 0,1)]
        self._animate()
        self._cells[i][j].visit()
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        for direction in directions:
            if (
                i + direction[1] < 0 or
                i + direction[1] > self._num_cols - 1 or
                j + direction[2] < 0 or
                j + direction[2] > self._num_rows - 1
            ):
                continue
            this_cell = self._cells[i][j]
            next_cell = self._cells[i + direction[1]][j + direction[2]]
            match direction[0]:
                case "left":
                    if this_cell.has_left_wall or next_cell.has_right_wall:
                        continue
                case "right":
                    if this_cell.has_right_wall or next_cell.has_left_wall:
                        continue
                case "top":
                    if this_cell.has_top_wall or next_cell.has_bottom_wall:
                        continue
                case "bottom":
                    if this_cell.has_bottom_wall or next_cell.has_top_wall:
                        continue
            if next_cell.visited():
                continue
            this_cell.draw_move(next_cell)
            if self._solver_r(i + direction[1], j + direction[2]):
                return True
            this_cell.draw_move(next_cell, undo=True)
