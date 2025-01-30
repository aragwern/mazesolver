from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width=800, height=600):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, width=width, height=height, bg='white')
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__up = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()


    def wait_for_close(self):
        self.__up = True
        while self.__up:
            self.redraw()
        print("window closed...")


    def close(self):
        self.__up = False


    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def draw(self, canvas, fill_color:str):
        canvas.create_line(
            self.A.x,
            self.A.y,
            self.B.x,
            self.B.y,
            fill=fill_color,
            width=2
        )

