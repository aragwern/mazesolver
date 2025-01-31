from graphics import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(x1=50, y1=50, x2=100, y2=100)

    c2 = Cell(win)
    c2.has_right_wall = False
    c2.draw(x1=125, y1=125, x2=200, y2=200)

    c1.draw_move(c2)

    c3 = Cell(win)
    c3.has_bottom_wall = False
    c3.draw(x1=225, y1=225, x2=250, y2=250)

    c2.draw_move(c3)

    c4 = Cell(win)
    c4.has_top_wall = False
    c4.draw(x1=300, y1=300, x2=500, y2=500)

    c3.draw_move(c4, True)


    win.wait_for_close()


main()
