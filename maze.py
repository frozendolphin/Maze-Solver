import time
import random

from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
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
        time.sleep(0.01)
    
    def _break_entrance_and_exit(self):
        cell = self._cells[0][0]
        cell.top_wall = False
        self._draw_cell(0, 0, cell)
        i, j = self.num_rows - 1, self.num_cols - 1
        cell = self._cells[i][j]
        cell.bottom_wall = False
        self._draw_cell(i, j, cell)
        
    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if i + 1 < self.num_rows:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            if j + 1 < self.num_cols:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))   
            if len(to_visit) == 0:
                self._draw_cell(i, j, current_cell)
                return
            direction = random.choice(to_visit)
            chosen_cell = self._cells[direction[0]][direction[1]]
            if direction[0] > i:
                current_cell.bottom_wall = False
                chosen_cell.top_wall = False
            if direction[0] < i:
                chosen_cell.bottom_wall = False
                current_cell.top_wall = False
            if direction[1] > j:
                chosen_cell.left_wall = False
                current_cell.right_wall = False
            if direction[1] < j:
                chosen_cell.right_wall = False
                current_cell.left_wall = False
            self._draw_cell(i, j, current_cell)
            self._break_walls_r(direction[0], direction[1])
            
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False