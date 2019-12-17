import sys
import copy

class Grid:

    def __init__(self, default_val = None, symbols = None):
        self.dct = dict()
        self.default = default_val
        if symbols:
            self.symbols = symbols
        else:
            self.symbols = dict()

    def put(self, pos, val):
        x, y = pos
        if not x in self.dct.keys():
            self.dct[x] = dict()
        if not y in self.dct[x].keys():
            self.dct[x][y] = dict()
        self.dct[x][y] = val

    def get(self, pos):
        x, y = pos
        try:
            return self.dct[x][y]
        except:
            return self.default

    def range(self):
        min_x = min(self.dct.keys())
        max_x = max(self.dct.keys())

        min_y = sys.maxsize
        max_y = -sys.maxsize
        for x in self.dct.keys():
            smallest = min(self.dct[x].keys())
            largest = max(self.dct[x].keys())
            if smallest < min_y:
                min_y = smallest
            if largest > max_y:
                max_y = largest
        return (min_x, max_x), (min_y,max_y)


    def __str__(self):
        rows = []
        x_range, y_range = self.range()
        for y in reversed(range(y_range[0], y_range[1] + 1)):
            row = ''
            for x in range(x_range[0], x_range[1] + 1):
                value = self.get((x, y))
                if value in self.symbols.keys():
                    value = self.symbols[value]
                row += str(value)
            rows.append(row)
        return '\n'.join(rows)

    def __copy__(self):
        print('copying!')
        grid_copy = Grid(self.default)
        grid_copy.dct = copy.deepcopy(self.dct)
        grid_copy.symbols = self.symbols
        return grid_copy

    def count(self, val):
        total = 0
        for vals in self.dct.values():
            total += sum(value == val for value in vals.values())
        return total

    def find(self, val):
        matches = []
        for x in self.dct.keys():
            for y in self.dct[x].keys():
                if self.dct[x][y] == val:
                    matches.append((x,y))
        return matches
