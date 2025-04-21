

from window import Window, Point, Line

def main():
    win = Window(800, 600)
    
    p3 = Point(800, 0)
    p4 = Point(0, 600)
    line2 = Line(p3, p4)
    win.draw_line(Line(Point(0, 0), Point(800, 600)), "lightblue")
    win.draw_line(Line(Point(800, 0), Point(0, 600)), "teal")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()