import time

from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        
    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                cell = Cell(self.win)
                row.append(cell)
                self._draw_cell(i, j, cell)
            self._cells.append(row)
            
    def _draw_cell(self, i, j, cell):
        if self.win == None:
            return
        x1 = self.x1 + (j * self.cell_size_x)
        y1 = self.y1 + (i * self.cell_size_y)
        x2 = x1 + self.cell_size_x 
        y2 = y1 + self.cell_size_y 
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        cell = self._cells[0][0]
        cell.top_wall = False
        self._draw_cell(0, 0, cell)
        i, j = self.num_rows - 1, self.num_cols - 1
        cell = self._cells[i][j]
        cell.bottom_wall = False
        self._draw_cell(i, j, cell)
        
        