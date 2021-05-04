from cell import Cell
import random

def remove_wall(cell1, cell2):
    if cell1.i - cell2.i == 1:
        cell1.walls[0] = False
        cell2.walls[2] = False
    if cell2.i - cell1.i == 1:
        cell1.walls[2] = False
        cell2.walls[0] = False
    if cell1.j - cell2.j == 1:
        cell1.walls[3] = False
        cell2.walls[1] = False
    if cell2.j - cell1.j == 1:
        cell1.walls[1] = False
        cell2.walls[3] = False

class Grid:
    def __init__(self, rows, cols, res):
        self.rows = rows
        self.cols = cols
        self.res = res
        self.cells = [Cell(i, j, self.res) for i in range(self.rows) for j in range(self.cols)]

        self.current = self.cells[0]
        self.current.visited = True
        self.stack = [self.current]

    def render(self, surface):
        for cell in self.cells:
            cell.render(surface, self.current)

    def update(self):
        neighbors = self.current.get_neighbors(self)

        if len(neighbors) == 0:
            if len(self.stack) == 0:
                return

            self.current = self.stack.pop()
            self.current.visited = True
            return

        random_neighbor = random.choice(neighbors)

        remove_wall(self.current, random_neighbor)
        self.current = random_neighbor
        self.current.visited = True

        self.stack.append(self.current)

    def get_cell(self, index):
        try:
            if index < 0:
                return None

            return self.cells[index]
        except:
            return None
