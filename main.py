

from window import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "lightblue")
    win.draw_line(Line(Point(800, 0), Point(0, 600)), "teal")
    cell.left_wall = False
    cell.draw(50, 100, 100, 150)
    cell.draw(25, 40, 760, 550)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()