

from window import Line, Point

class Cell():
    def __init__(self, window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = window
    
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        color = "black"
        if self.left_wall:
            color = "#00FFFF"
        line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        self.win.draw_line(line, color) 
        color = "black"
        if self.right_wall:
            color = "#00FFFF"
        line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        self.win.draw_line(line, color) 
        color = "black"
        if self.top_wall:
            color = "#00FFFF"
        line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        self.win.draw_line(line, color) 
        color = "black"
        if self.bottom_wall:
            color = "#00FFFF"
        line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
        self.win.draw_line(line, color) 
    
    def draw_move(self, to_cell, undo=False):
        color = "#CCFF00"
        if undo:
            color = "#C71585"
        midx1 = (self.x1 + self.x2)/2
        midy1 = (self.y1 + self.y2)/2
        midx2 = (to_cell.x1 + to_cell.x2)/2
        midy2 = (to_cell.y1 + to_cell.y2)/2
        line = Line(Point(midx1, midy1), Point(midx2, midy2))
        self.win.draw_line(line, color)
