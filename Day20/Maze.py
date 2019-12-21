from Grid import Grid
from A_star import A_star

class Maze:

    def __init__(self, string):
        self.grid = self.get_grid(string)
        self.portals = self.get_portals()
        self.a_star = A_star()


    def get_grid(self, string):
        grid = Grid(' ')
        for y, row in enumerate(string.splitlines()):
            for x, char in enumerate(row):
                grid.put((x, -y), char)
        return grid

    def get_portals(self):

        def get_letters(x, y):
            letter = self.grid.get((x,y))
            for pos in [(x-1,y), (x, y+1)]:
                first = self.grid.get(pos)
                if first.isupper():
                    return first + letter
            for pos in [(x+1,y), (x,y-1)]:
                second = self.grid.get(pos)
                if second.isupper():
                    return letter + second

        portals = dict()
        found_letters = dict()
        (x1, x2), (y1, y2) = self.grid.range()
        for y in reversed(range(y1, y2+1)):
            for x in range(x1, x2+1):
                char = self.grid.get((x,y))
                if char.isupper() and '.' in self.get_neighbors(x,y):
                    letters = get_letters(x,y)
                    if letters == 'AA':
                        self.start = self.get_path_neighbor(x,y)
                        self.grid.put((x,y), '@')
                    if letters == 'ZZ':
                        self.end   = self.get_path_neighbor(x,y)
                        self.grid.put((x, y), '$')
                    if letters not in found_letters.keys():
                        found_letters[letters] = (x, y)
                    else:
                        portals[(x,y)] = found_letters[letters]
                        portals[found_letters[letters]] = (x,y)
        return portals

    def heuristic(self, n1, n2):
        return 0

    def adjacents(self, node):
        adjacents = []
        x, y = node
        for neigh in self.get_neighbors_pos(x, y):
            neigh_char = self.grid.get(neigh)
            if neigh_char == '.':
                adjacents.append(neigh)
            if neigh_char.isupper() and neigh_char != '@' and neigh_char != '$':
                letter_x, letter_y = self.portals[neigh]
                adjacents.append(self.get_path_neighbor(letter_x, letter_y))
        return adjacents

    def get_neighbors_pos(self, x, y):
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

    def get_neighbors(self, x, y):
        return [self.grid.get(n) for n in self.get_neighbors_pos(x, y)]

    def get_path_neighbor(self, x, y):
        for neigh in self.get_neighbors_pos(x,y):
            if self.grid.get(neigh) == '.':
                return neigh

    def print_maze(self, highlights=None):
        if highlights is None:
            highlights = []
        copy_grid = copy(self.grid)
        for x, y in highlights:
            copy_grid.put((x,y),'█')
        print(copy_grid)