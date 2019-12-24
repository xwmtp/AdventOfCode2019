from copy import copy
from Grid import Grid

class Bug_simulator:

    def __init__(self, string):
        self.grid = self.string_to_grid(string)
        self.configurations = [str(self.grid)]

    def string_to_grid(self, string):
        grid = Grid(' ')
        for y, row in enumerate(string.splitlines()):
            for x, char in enumerate(row):
                grid.put((x, -y), char)
        return grid

    def step(self):

        new_grid = copy(self.grid)
        for x in range(5):
            for y in range(5):
                tile = self.grid.get((x, -y))
                bugs = self.get_adjacent_bugs(x, -y)
                if tile == '#' and bugs != 1:
                    new = '.'
                elif tile == '.' and (bugs == 1 or bugs == 2):
                    new = '#'
                else:
                    new = tile
                new_grid.put((x,-y), new)
        self.grid = new_grid
        if str(self.grid) in self.configurations:
            return self.grid
        self.configurations.append(str(self.grid))

    def biodiversity(self):
        biodiversity = 0
        power = 0
        for y in range(5):
            for x in range(5):
                if self.grid.get((x, -y)) == '#':
                    biodiversity += 2**power
                power+=1
        return biodiversity


    def get_adjacent_bugs(self, x, y):
        bugs = 0
        adj_positions = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for x_adj, y_adj in adj_positions:
            tile = self.grid.get((x_adj, y_adj))
            if tile == '#':
                bugs += 1
        return bugs