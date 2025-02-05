import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_reset_cells_visited(self):
        num_rows = 2
        num_cols = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 10)

        for column in m1.get_cells():
            for cell in column:
                cell.visit()

        for column in m1.get_cells():
            for cell in column:
                self.assertTrue(cell.visited())

        m1._reset_cells_visited()

        for column in m1.get_cells():
            for cell in column:
                self.assertFalse(cell.visited())



if __name__ == "__main__":
    unittest.main()
