

from window import Window, Point, Line
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell2 = Cell(win)
    
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "lightblue")
    win.draw_line(Line(Point(800, 0), Point(0, 600)), "teal")
    cell1.draw(50, 100, 100, 150)
    cell2.draw(150, 200, 200, 250)
    cell1.draw_move(cell2, True)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()