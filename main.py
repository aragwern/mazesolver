from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(x1=50, y1=50, x2=100, y2=100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(x1=125, y1=125, x2=200, y2=200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(x1=225, y1=225, x2=250, y2=250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(x1=300, y1=300, x2=500, y2=500)

    win.wait_for_close()


main()
