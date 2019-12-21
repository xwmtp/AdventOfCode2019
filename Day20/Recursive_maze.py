from Grid import Grid
from A_star import A_star
from copy import copy

class Recursive_maze:

    def __init__(self, string):
        self.inner_range = None
        self.grid = self.get_grid(string)
        self.portals = self.get_portals()
        self.a_star = A_star()
        self.deepest_level = 0


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
                    return first  + letter
            for pos in [(x+1,y), (x,y-1)]:
                second = self.grid.get(pos)
                if second.isupper():
                    return letter + second

        def check_start_end(letters):
            if letters == 'AA':
                self.start = self.get_dot_neighbor(x, y)
                self.grid.put((x, y), '@')
            if letters == 'ZZ':
                self.end = self.get_dot_neighbor(x, y)
                self.grid.put((x, y), '$')

        portals = dict()
        found_letters = dict()
        (x1, x2), (y1, y2) = self.grid.range()
        for y in reversed(range(y1, y2+1)):
            for x in range(x1, x2+1):
                char = self.grid.get((x,y))
                if char.isupper() and '.' in self.get_neighbors(x,y):

                    letters = get_letters(x,y)
                    check_start_end(letters)

                    if letters not in found_letters.keys():
                        found_letters[letters] = (x, y)
                    else:
                        portal_pos = found_letters[letters]
                        portals.update({(x,y) : portal_pos, portal_pos : (x,y)})
        return portals

    def heuristic(self, n1, n2):
        return max(0,(n1[1]-1) * 30)

    def adjacents(self, node, max_level=25):
        adjacents = []
        (x, y), level = node
        for neigh in self.get_neighbors_pos(x, y):
            neigh_char = self.grid.get(neigh)
            if neigh_char == '.':
                adjacents.append((neigh, level))
            if neigh_char.isupper() and neigh_char != '@' and neigh_char != '$':

                letter_x, letter_y = self.portals[neigh]
                if self.is_inner_portal(neigh):
                    if level < max_level:
                        if level + 1 > self.deepest_level:
                            print(level + 1)
                            self.deepest_level = level + 1
                        adjacents.append((self.get_dot_neighbor(letter_x, letter_y), level+1))
                else:
                    if level > 0:
                        adjacents.append((self.get_dot_neighbor(letter_x, letter_y), level-1))


        return adjacents

    def get_neighbors_pos(self, x, y):
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

    def get_neighbors(self, x, y):
        return [self.grid.get(n) for n in self.get_neighbors_pos(x, y)]

    def get_dot_neighbor(self, x, y):
        for neigh in self.get_neighbors_pos(x,y):
            if self.grid.get(neigh) == '.':
                return neigh

    def is_inner_portal(self, pos):
        x, y = pos
        (_,max_x), (min_y,_) = self.grid.range()
        return x > 1 and x < max_x-1 and y < -1 and y > min_y+1

    def print_maze(self, highlights=None):
        if highlights is None:
            highlights = []
        copy_grid = copy(self.grid)
        for x, y in highlights:
            copy_grid.put((x,y),'█')
        print(copy_grid)