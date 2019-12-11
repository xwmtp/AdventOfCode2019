import sys

class Grid:

    def __init__(self, default_val=None):
        self.dct = dict()
        self.default = default_val

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


    def print(self, symbols=None):
        if symbols is None:
            symbols = dict()
        x_range, y_range = self.range()
        for y in reversed(range(y_range[0], y_range[1] + 1)):
            row = ''
            for x in range(x_range[0], x_range[1] + 1):
                value = self.get((x, y))
                if value in symbols.keys():
                    value = symbols[value]
                row += str(value)

            print(row)