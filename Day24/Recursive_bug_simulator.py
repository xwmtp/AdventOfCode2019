from copy import copy, deepcopy
from Grid import Grid

class Recursive_bug_simulator:

    def __init__(self, string):
        self.grids = dict()
        self.grids[0]=self.string_to_grid(string)
        self.deepest = 0

    def string_to_grid(self, string):
        grid = Grid(' ')
        for y, row in enumerate(string.splitlines()):
            for x, char in enumerate(row):
                grid.put((x, -y), char)
        grid.put((2,-2),'?')
        return grid

    def step(self):

        def add_levels():
            for i in [1, -1]:
                new_level = (self.deepest + 1) * i
                if new_level not in self.grids.keys():
                    self.grids[new_level] = self.get_empty_grid()
            self.deepest += 1

        add_levels()
        self.new_grids = deepcopy(self.grids)


        for level, grid in self.grids.items():
            new_grid = copy(grid)
            for x in range(5):
                for y in range(5):
                    tile = grid.get((x, -y))
                    bugs = self.get_adjacent_bugs(x, -y, level)
                    if tile == '#' and bugs != 1:
                        new = '.'
                    elif tile == '.' and (bugs == 1 or bugs == 2):
                        new = '#'
                    else:
                        new = tile
                    new_grid.put((x,-y), new)
            self.new_grids[level] = new_grid
        self.grids = self.new_grids



    def count_bugs(self):
        bugs = 0
        for grid in self.grids.values():
            bugs += grid.count('#')
        return bugs

    def get_adjacent_bugs(self, x, y, level):

        def get_own_adjacent_bugs():
            bugs = 0
            adj_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for x_adj, y_adj in adj_positions:
                tile = self.grids[level].get((x_adj, y_adj))
                if tile == '#':
                    bugs += 1
            return bugs

        def get_outer_adjacent_bugs():
            bugs = 0
            adj_positions = []
            if x == 0:
                adj_positions.append((1, -2))
            if x == 4:
                adj_positions.append((3, -2))
            if y == 0:
                adj_positions.append((2, -1))
            if y == -4:
                adj_positions.append((2, -3))
            for x_adj, y_adj in adj_positions:
                tile = self.get_from_grid(x_adj, y_adj, level-1)
                if tile == '#':
                    bugs += 1
            return bugs

        def get_inner_adjacent_bugs():
            bugs = 0
            adj_positions = []
            if x == 1 and y == -2:
                adj_positions = [(0, -y_adj) for y_adj in range(5)]
            if x == 3 and y == -2:
                adj_positions = [(4, -y_adj) for y_adj in range(5)]
            if x == 2 and y == -1:
                adj_positions = [(x_adj,  0) for x_adj in range(5)]
            if x == 2 and y == -3:
                adj_positions = [(x_adj, -4) for x_adj in range(5)]
            for x_adj, y_adj in adj_positions:
                tile = self.get_from_grid(x_adj, y_adj, level + 1)
                if tile == '#':
                    bugs += 1
            return bugs

        bugs =  get_own_adjacent_bugs()
        bugs += get_outer_adjacent_bugs()
        bugs += get_inner_adjacent_bugs()

        return bugs



    def get_from_grid(self, x, y, level):

        if not level in self.grids.keys():
            self.new_grids[level] = self.get_empty_grid()
            return ' '
        else:
            return self.grids[level].get((x, y))

    def get_empty_grid(self):
        grid = Grid(' ')
        for x in range(5):
            for y in range(5):
                grid.put((x, -y), '.')
        grid.put((2,-2),'?')
        return grid

    def __str__(self):
        string = []
        for level, grid in sorted(self.grids.items()):
            if grid.count('#') > 0:
                string.append(f'Level: {level}\n{grid}')
        return '\n'.join(string)